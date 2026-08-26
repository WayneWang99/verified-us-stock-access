#!/usr/bin/env python3
"""Validate source metadata, local documentation links, freshness, and URLs.

The network check proves reachability only. Semantic accuracy still requires a
human to reopen the source, compare the claim, and update last_verified.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


SOURCE_ID_RE = re.compile(r"S-[A-Z]+-\d{2}")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
ACCEPTED_BLOCK_CODES = {401, 403, 405, 429}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--data", type=Path)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--no-network", action="store_true")
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--max-workers", type=int, default=8)
    return parser.parse_args()


def parse_iso_date(value: str, field: str, source_id: str) -> tuple[dt.date | None, str | None]:
    try:
        return dt.date.fromisoformat(value), None
    except (TypeError, ValueError):
        return None, f"{source_id}: {field} must be YYYY-MM-DD, got {value!r}"


def check_url(source: dict[str, Any], timeout: float) -> dict[str, Any]:
    base_headers = {
        "User-Agent": "verified-us-stock-access-source-watch/1.0 (+https://github.com/WayneWang99/verified-us-stock-access)",
        "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
        "Connection": "close",
    }
    last_result: dict[str, Any] | None = None
    # Some government and CDN endpoints intermittently reject byte ranges or
    # close an SSL handshake. Try ranged GET, normal GET, then lightweight HEAD.
    attempts = (("GET", True), ("GET", False), ("HEAD", False))
    for method, use_range in attempts:
        headers = dict(base_headers)
        if use_range:
            headers["Range"] = "bytes=0-2047"
        request = urllib.request.Request(source["url"], headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                if method == "GET":
                    response.read(256)
                status = response.getcode() or 200
                return {
                    "id": source["id"],
                    "ok": 200 <= status < 400,
                    "hard_fail": False,
                    "status": status,
                    "final_url": response.geturl(),
                    "detail": "reachable" if 200 <= status < 400 else "unexpected status",
                }
        except urllib.error.HTTPError as exc:
            reachable = exc.code in ACCEPTED_BLOCK_CODES
            if reachable:
                return {
                    "id": source["id"],
                    "ok": True,
                    "hard_fail": False,
                    "status": exc.code,
                    "final_url": exc.geturl(),
                    "detail": "reachable but automated client blocked/rate-limited",
                }
            last_result = {
                "id": source["id"],
                "ok": False,
                "hard_fail": exc.code in {404, 410},
                "status": exc.code,
                "final_url": exc.geturl(),
                "detail": str(exc.reason),
            }
        except Exception as exc:  # Network stacks expose several platform-specific errors.
            last_result = {
                "id": source["id"],
                "ok": False,
                "hard_fail": False,
                "status": None,
                "final_url": source["url"],
                "detail": f"{type(exc).__name__}: {exc}",
            }
    assert last_result is not None
    return last_result


def check_local_markdown_links(root: Path) -> list[str]:
    errors: list[str] = []
    for markdown_file in sorted(root.rglob("*.md")):
        if ".git" in markdown_file.parts:
            continue
        text = markdown_file.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip().split()[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue
            resolved = (markdown_file.parent / path_part).resolve()
            try:
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{markdown_file.relative_to(root)}: link escapes repository: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{markdown_file.relative_to(root)}: missing local target: {target}")
    return errors


def validate_repository(root: Path, data: dict[str, Any]) -> tuple[list[str], list[str], list[dict[str, Any]]]:
    errors: list[str] = []
    warnings: list[str] = []
    stale: list[dict[str, Any]] = []

    if data.get("schema_version") != 1:
        errors.append("data/sources.json: unsupported schema_version")

    sources = data.get("sources")
    referrals = data.get("referrals")
    if not isinstance(sources, list) or not sources:
        errors.append("data/sources.json: sources must be a non-empty list")
        sources = []
    if not isinstance(referrals, list) or len(referrals) != 4:
        errors.append("data/sources.json: referrals must contain exactly four platforms")
        referrals = []

    ids: list[str] = []
    today = dt.date.today()
    default_days = int(data.get("default_review_after_days", 30))
    for source in sources:
        source_id = source.get("id", "<missing-id>")
        ids.append(source_id)
        for field in ("id", "publisher", "title", "url", "kind", "last_verified", "supports"):
            if not source.get(field):
                errors.append(f"{source_id}: missing required field {field}")
        if not str(source.get("url", "")).startswith("https://"):
            errors.append(f"{source_id}: source URL must use HTTPS")
        verified, date_error = parse_iso_date(source.get("last_verified"), "last_verified", source_id)
        if date_error:
            errors.append(date_error)
        elif verified:
            review_days = int(source.get("review_after_days", default_days))
            age = (today - verified).days
            if age > review_days:
                stale.append({"id": source_id, "age": age, "limit": review_days, "url": source.get("url")})

    duplicates = sorted({source_id for source_id in ids if ids.count(source_id) > 1})
    if duplicates:
        errors.append(f"duplicate source IDs: {', '.join(duplicates)}")

    defined = set(ids)
    docs_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted(root.rglob("*.md"))
        if ".git" not in path.parts
    )
    referenced = set(SOURCE_ID_RE.findall(docs_text))
    unknown = sorted(referenced - defined)
    if unknown:
        errors.append(f"documentation references undefined source IDs: {', '.join(unknown)}")

    sources_page = (root / "SOURCES.md").read_text(encoding="utf-8") if (root / "SOURCES.md").exists() else ""
    missing_from_catalog = sorted(source_id for source_id in defined if source_id not in sources_page)
    if missing_from_catalog:
        errors.append(f"SOURCES.md is missing IDs: {', '.join(missing_from_catalog)}")

    platforms = {item.get("platform") for item in referrals}
    expected_platforms = {"Binance", "OKX", "Bitget", "Gate"}
    if platforms != expected_platforms:
        errors.append(f"referral platforms must be {sorted(expected_platforms)}, got {sorted(str(x) for x in platforms)}")

    readme = (root / "README.md").read_text(encoding="utf-8") if (root / "README.md").exists() else ""
    for item in referrals:
        platform = item.get("platform", "<missing-platform>")
        url = item.get("url", "")
        if not url.startswith("https://"):
            errors.append(f"{platform} referral URL must use HTTPS")
        if item.get("referral_code") != "OFFHOURS" or "OFFHOURS" not in url:
            errors.append(f"{platform} referral must preserve OFFHOURS in metadata and URL")
        if item.get("claimed_discount_percent") != 20:
            errors.append(f"{platform} claimed_discount_percent must be 20")
        if url not in readme:
            errors.append(f"README.md is missing exact {platform} referral URL")
        if item.get("automated_check") is not False:
            warnings.append(f"{platform}: dynamic referral is marked for automated checking; expect redirect false positives")

    errors.extend(check_local_markdown_links(root))
    return errors, warnings, stale


def render_report(
    *,
    root: Path,
    errors: list[str],
    warnings: list[str],
    stale: list[dict[str, Any]],
    network_results: list[dict[str, Any]],
    network_skipped: bool,
) -> str:
    today = dt.date.today().isoformat()
    failed_network = [item for item in network_results if item.get("hard_fail")]
    inconclusive_network = [item for item in network_results if not item["ok"] and not item.get("hard_fail")]
    outcome = "PASS" if not errors and not stale and not failed_network else "FAIL"
    lines = [
        f"# Source Watch Report — {today}",
        "",
        f"**Outcome: {outcome}**",
        "",
        "Automated checks cover metadata, freshness, local links and URL reachability. They do not prove that a source still supports the same claim; a human must re-read changed or stale pages.",
        "",
        "## Summary",
        "",
        f"- Schema/local errors: {len(errors)}",
        f"- Stale sources: {len(stale)}",
        f"- Network hard failures (404/410): {len(failed_network)}" if not network_skipped else "- Network checks: skipped",
        f"- Network inconclusive warnings: {len(inconclusive_network)}" if not network_skipped else "- Network warnings: skipped",
        f"- Warnings: {len(warnings)}",
    ]

    if errors:
        lines.extend(["", "## Schema and local-link errors", ""])
        lines.extend(f"- {item}" for item in errors)
    if stale:
        lines.extend(["", "## Sources due for human review", ""])
        lines.extend(
            f"- [{item['id']}]({item['url']}): {item['age']} days since review; limit {item['limit']} days"
            for item in stale
        )
    if network_results:
        lines.extend(["", "## URL reachability", "", "| Source | Status | Result | Final URL |", "| --- | ---: | --- | --- |"])
        for item in sorted(network_results, key=lambda value: value["id"]):
            status = item["status"] if item["status"] is not None else "—"
            if item["ok"]:
                result = "OK"
            elif item.get("hard_fail"):
                result = f"FAIL: {item['detail']}"
            else:
                result = f"WARN: {item['detail']}"
            lines.append(f"| {item['id']} | {status} | {result} | {item['final_url']} |")
    if warnings:
        lines.extend(["", "## Warnings", ""])
        lines.extend(f"- {item}" for item in warnings)

    lines.extend(["", f"Repository root checked: `{root}`", ""])
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    data_path = (args.data or root / "data" / "sources.json").resolve()
    try:
        data = json.loads(data_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Unable to load {data_path}: {exc}", file=sys.stderr)
        return 2

    errors, warnings, stale = validate_repository(root, data)
    sources = data.get("sources", [])
    network_results: list[dict[str, Any]] = []
    if not args.no_network:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.max_workers)) as executor:
            futures = [executor.submit(check_url, source, args.timeout) for source in sources]
            network_results = [future.result() for future in concurrent.futures.as_completed(futures)]

    report = render_report(
        root=root,
        errors=errors,
        warnings=warnings,
        stale=stale,
        network_results=network_results,
        network_skipped=args.no_network,
    )
    print(report)
    if args.report:
        report_path = args.report if args.report.is_absolute() else root / args.report
        report_path.write_text(report, encoding="utf-8")

    network_failed = any(item.get("hard_fail") for item in network_results)
    return 1 if errors or stale or network_failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
