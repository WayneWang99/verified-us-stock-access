# OKX：统一代币化股票与股票永续完整教程

最后人工核验：`2026-08-26`

**[通过专属入口注册 OKX，领取 20% 手续费优惠](https://www.promooboost.com/join/OFFHOURS)**（邀请码：`OFFHOURS`，适用范围以落地页和账户费率为准）

截至核验日，OKX 的中心化平台主要提供两类美股价格入口：统一代币化股票（UTS）和股票永续。OKX Wallet 的 DEX 还可交易第三方代币化股票，但这是另一个钱包与链上路径。

## 产品地图

| 产品 | 示例 | 本质 | 主要特点 |
| --- | --- | --- | --- |
| Unified Tokenized Stocks | `xAAPL/USDT`（API ID 仍可能为 `XAAPL-USDT`） | OKX 账户中的合同权益，对应第三方发行的代币化股票敞口 | 24/7、USDT、非底层股票所有权、可支持提链 |
| Stock Perpetuals | `AAPLUSDT` 等 | USDT 保证金永续合约 | 24/7、多空、保证金、资金费率和强平 |
| OKX Wallet DEX Tokenized Stocks | Ondo 等第三方代币 | 自托管钱包中的链上资产 | 需要 Gas、滑点设置和合约核验 |

## 一、注册与准备

1. 打开专属入口，确认邀请码 `OFFHOURS` 后创建账户。
2. 完成真实身份认证、适当性与产品风险确认。
3. 开启验证器 2FA、防钓鱼码、设备管理与提现白名单。
4. 准备 USDT；链上充值必须让发送网络与接收网络一致，并先小额测试。
5. 更新 App。UTS 的显示格式在 2026-07-29 从 `XAAPL` 调整为 `xAAPL`，旧版界面可能仍显示大写格式。

## 二、Unified Tokenized Stocks（UTS）

### 产品本质

OKX 条款把 UTS 定义为：记录在 OKX 平台内、以股票等值单位计量的合同权益。你的 UTS 余额本身不是链上代币，底层链上代币由第三方发行人发行；它提供股票/ETF 的价格和部分经济敞口，但不产生底层公司的所有权或投票权（[S-OKX-01](../SOURCES.md#s-okx-01)、[S-OKX-02](../SOURCES.md#s-okx-02)）。

当前产品由 xStocks/Backed Assets 框架提供支持，交易对用 USDT，部分资产支持通过 Solana 或 X Layer 充提。具体发行人可能扩展，不能把所有 UTS 永久理解为同一发行结构。

### App/网页买入

1. App 进入 `Trade → Spot`；网页进入 `Trade → TradFi/Stocks → Spot`。
2. 搜索带 `x` 前缀的代码，例如 `xAAPL`、`xTSLA`。API 和部分旧界面可能仍用 `XAAPL`。
3. 确认交易对为 UTS 现货，不是 `AAPLUSDT Perpetual`。
4. 第一次交易前阅读并同意产品风险披露。
5. 选择限价单或市价单，输入股票等值数量/USDT 金额。
6. 预览订单，核对交易费、点差、标的、数量和周末流动性提示。
7. 成交后到 `Assets → Spot` 查看份额、平均成本和未实现盈亏。
8. 在资产详情的 `Corporate actions` 查看股息与公司行动记录。

官方操作说明见 [S-OKX-03](../SOURCES.md#s-okx-03)。

### 股息和费用

- 股息通常不是现金派发，而是在发行人层面税后再投资，通过增加份额/调整 Multiplier 反映。
- 标准 OKX 现货交易费适用；RFQ/Convert 报价可能包含点差。
- 发行人还可能收取年度管理费并每日通过 Multiplier 扣除；直接申购/赎回可能有发行人费用。
- 周末或美股休市时，RFQ/订单簿价格可能基于上次收盘价与做市估值，点差可能扩大。

因此，不能只看 OKX 现货费率；还要看发行人 Final Terms 和成交前价格。

### 提链前核对

1. 资产详情是否对你的账户显示 `Withdraw`；
2. 支持 Solana 还是 X Layer；
3. 接收钱包是否支持该链和真实合约地址；
4. 提币费、最低额和公司行动暂停窗口；
5. 提到链上后由哪个发行人条款管辖，以及普通用户能否赎回。

## 三、股票永续

### 产品本质

OKX 股票永续是跟踪公开交易股票价格的 USDT 保证金永续掉期。它不是证券，不产生股票受益所有权、股息或投票权。官方说明其 24/7 交易，采用独立订单簿和自己的指数/标记价格机制（[S-OKX-04](../SOURCES.md#s-okx-04)、[S-OKX-05](../SOURCES.md#s-okx-05)）。

### App/网页路径

1. App 首页点 `TradFi`；网页进入 `Trade → Futures → TradFi`。
2. 搜索目标代码，确认名称含 `Perpetual`/`USDT`。
3. 打开 `Overview → Index Components/Contract Specifications`。
4. 核对最大杠杆、合约乘数、最小数量、资金费率和结算周期；不同合约可能不同。
5. 划转小额 USDT 到 Trading Account。
6. 初次使用逐仓和低杠杆，设置限价单、方向与止损。
7. 持仓期间关注标记价格、保证金率、下一期资金费率和周末价差。

不要照搬某个旧教程的固定杠杆数字。OKX 官方要求以每份合约规格页为准。

## 四、OKX Wallet DEX 的第三方股票代币

这不是 OKX 交易所 UTS 余额。官方 FAQ 的通用步骤为：

1. 打开 `OKX Wallet → DEX`；
2. 选择代币化股票并核对发行人、合约地址和网络；
3. 准备 USDT/USDC 作为交易资产，并准备链上原生币支付 Gas；
4. 输入金额，查看滑点、Gas 和最低成交；
5. 签名交易后在区块浏览器核对。

DEX 路径增加自托管、合约、授权、Gas、MEV 和流动性风险。不要把搜索结果中同名代币当成官方支持资产。

## 五、怎么选

- 想用 USDT 24/7 持有股票价格敞口、不需要投票：比较 UTS 的发行人、管理费和提链能力。
- 想开多/开空：使用股票永续，但先把资金费率、强平和独立订单簿写进计划。
- 想把资产拿到自托管钱包：只有在能核对合约和发行人、理解链上授权后再走 DEX/提链。
- 想要传统券商式真实股票与完整股东权利：截至本次核验，不应把 OKX UTS 当作这一类产品。

## 官方来源

- [Unified Tokenized Stocks 官方说明](https://www.okx.com/en-ae/help/unified-tokenized-stocks)
- [UTS 交易条款](https://www.okx.com/en-us/help/unified-tokenized-stock-trading-terms-and-conditions)
- [如何买卖 UTS](https://www.okx.com/en-us/help/how-do-i-buy-sell-unified-tokenized-stocks)
- [Stock Perpetuals 官方说明](https://www.okx.com/en-gb/help/stock-perpetuals)
- [Stock Perpetuals FAQ](https://www.okx.com/en-gb/help/stock-perpetuals-faq)

