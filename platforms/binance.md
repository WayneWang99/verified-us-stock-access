# Binance：Stocks、bStocks 与股票永续完整教程

最后人工核验：`2026-08-26`

**[通过专属入口注册 Binance，领取 20% 手续费优惠](https://www.bsmkweb.cc/join?ref=OFFHOURS)**（邀请码：`OFFHOURS`，适用范围以落地页和账户费率为准）

Binance 是四家中产品分层最清楚的一家：同一个账户可能同时看到真实证券服务、代币化股票和股票永续。三者不能混用名称。

## 你能买到什么

| 产品 | 你持有什么 | 结算/购买资产 | 交易时间 | 权益与主要机制 |
| --- | --- | --- | --- | --- |
| Binance Stocks | 合作券商托管的股票受益权益 | 主要用 USDC；支持部分资产自动转换 | 最多 24/5，视标的 | 官方称有股息及适用公司行动权益 |
| bStocks | BTech Holdings 发行的 BEP-20 代币化证券 | 现货/转换 | 24/7 | 1:1 底层股票支持；不是直接持股；股息税后再投资 |
| Stock Perpetuals | USDT 本位永续合约 | USDT/多资产保证金 | 24/7 | 多空、最高杠杆当前 10x、每 8 小时资金费率 |

产品是否对你开放，以登录后的 `Trade`、`Stocks`、`Futures → TradFi` 实际显示为准。

## 一、注册与准备

1. 打开上方专属入口，确认邀请码显示为 `OFFHOURS`，再创建账户。
2. 使用本人真实身份完成平台要求的身份认证与适当性问卷。
3. 开启验证器 2FA、防钓鱼码、设备管理和提现白名单。
4. 准备平台支持的 USDC/USDT；链上充值先核对网络并小额测试。
5. 更新 App。产品入口和名称在 2026 年变化较快，旧版本可能不显示。

20% 优惠是注册入口标示的交易手续费优惠，不应自动理解为 Binance Stocks 的证券平台费、ADR 费或全部产品费用都会减免。最终看订单预览和账户费率页。

## 二、Binance Stocks：平台内买真实股票

### 产品本质

Binance 官方说明称，该服务由 Nest Trading Limited 提供并与外部券商合作；合格用户可交易 7,000 多只股票和 ETF，最低 5 美元。买入后用户是股票的受益所有人，股份由合作券商托管，适用时可获得股息和公司行动权益（[S-BIN-01](../SOURCES.md#s-bin-01)）。

这仍不等于股票一定以你的个人姓名直接登记，也不等于所有账户或地区都开放。开户时阅读证券服务实体、托管、转仓和客户资产条款。

### App 下单

1. 进入 `Trade → Stocks`。
2. 搜索完整公司名或股票代码，例如 `AAPL`。
3. 打开详情页，确认页面写的是 `Stocks`，不是 `bStocks` 或 `Perpetual`。
4. 选择市价单或限价单。
5. 输入金额/股数，选择 Funding 或 Spot 账户作为付款来源。
6. 若使用 USDT、BNB 等非 USDC 资产，先看清自动转换率。
7. 点 `Preview`，核对交易时段、有效期、费用、预计股数和结算资产。
8. 确认后，在资产页查看股票持仓和订单状态。

网页版路径为 `Trade → Stock → 搜索标的 → 选择订单与付款账户 → Preview → Convert to Buy`。

### 当前交易规则

- 主要使用 USDC 买入；官方列出的部分其他资产会在下单时自动换成 USDC。
- 市价单只在美股常规时段激活；限价单可按标的选择常规、延长或 24 小时交易时段。
- DAY 订单当日失效；GTC 最长可保留 90 天，但碎股不支持 GTC。
- 部分股票支持碎股。
- 卖出所得以 USDC 进入 Funding Account。

### 当前费用快照

官方 2026-06-04 页面列示：

- 不另收股票交易佣金；
- 订单金额不高于 350 美元时，最低平台费 0.35 美元；
- 高于 350 美元时，页面说明为 0.1% 点差；
- ADR 可能每股收取约 0.01–0.03 美元的周期性费用；
- 还可能有兑换、监管、股息、税费等成本。

这些是核验日快照，不是永久价格。以每一笔 `Preview` 为准。

## 三、bStocks：24/7 代币化股票

### 产品本质

bStocks 由 Binance 关联方 BTech Holdings Limited 发行，是 BNB Smart Chain 上的 BEP-20 代币化证券。官方称每枚由受监管托管人持有的一股美国股票 1:1 支持，并提供 Proof of Collateral；但持有人不是底层公司的直接股东（[S-BIN-02](../SOURCES.md#s-bin-02)）。

股息不是现金发到 Funding 账户。官方说明是先按适用规则预扣税，再买入更多底层股票，通过 `Multiplier` 增加你的 bStock 余额；拆股也通过余额调整处理。

### 三种获得方式

1. **买股票时自动转换**  
   `Trade → Stock → 选择标的 → 打开 Token Conversion → 下单`。成交后转成对应 bStock。

2. **把已有 Binance Stocks 转成 bStocks**  
   `Wallet → 选择支持转换的股票 → Token Conversion → 输入数量 → Confirm`。官方称符合条件时可 1:1 双向转换且无转换费；公司行动或维护时可能暂停。

3. **直接在现货买**  
   `Spot → bStocks → 选择交易对 → 限价/市价买入`。现货可 24/7 交易。

### 下单前核对

- 代币合约地址与官方产品页是否一致；
- 是否允许你当前账户提到链上；
- 现货深度、买卖价差和周末价格偏离；
- Proof of Collateral 的更新时间和覆盖率；
- 普通用户是否能走回/转换，最低金额和费用；
- 适用的发行人条款、托管与破产处理。

自托管增加了控制权，也增加私钥、网络、合约和 DeFi 协议风险。不要因为能提链就把它等同于在券商转仓。

## 四、股票永续：开多、开空与杠杆

### 产品本质

Binance 股票永续是 USDⓈ-M TradFi Perps，跟踪股票参考价格但不持有股票。官方 2026-04-23 页面列示：24/7 交易、USDT 结算、当前最高 10x 杠杆、每 8 小时资金费率，股票合约的名义下单门槛示例为 5 USDT（[S-BIN-03](../SOURCES.md#s-bin-03)）。

### 操作路径

1. 进入 `Futures → TradFi`。
2. 搜索股票代码并确认完整合约名，例如 `MSTRUSDT`、`AMZNUSDT`。
3. 打开 `Overview/Contract Specifications`，核对指数来源、标记价格、资金费率周期、杠杆档位和最小数量。
4. 把小额保证金划入 Futures 账户。
5. 初次优先选择逐仓与低杠杆。
6. 选择限价、市价或止损限价订单，明确 `Buy/Long` 或 `Sell/Short`。
7. 同时设置能承受的止损；不要拿强平价当止损。
8. 成交后持续查看标记价格、保证金率、下一次资金费率和强平价。

### 周末价格

底层股票周末休市，永续仍交易。Binance 在 2026 年更新了股票永续的订单簿 EWMA 定价模式，以平滑指数和标记价格。平台价格可能与上一个美股收盘价明显不同；这不自动构成可无风险套利，重新开盘时也可能出现跳空。

## 五、怎么选

- 要长期持有、收现金股息并希望尽量接近券商体验：先看 Binance Stocks 的账户条款和可转出能力。
- 要 24/7、链上自托管和碎片化：比较 bStocks 的储备、价差、链上费用和公司行动机制。
- 要开空/杠杆：才使用股票永续，并把资金费率纳入总成本。

不要用股票永续长期代替股票，也不要因为 bStocks 有 1:1 储备就假定拥有投票权或 SIPC 保护。

## 官方来源

- [Binance Stocks Trading 官方指南](https://www.binance.com/en/academy/articles/what-is-binance-stocks-trading)
- [bStocks 官方指南](https://www.binance.com/en/academy/articles/what-are-bstocks-a-guide-to-tokenized-stocks-on-binance)
- [股票永续官方指南](https://www.binance.com/en/academy/articles/how-to-trade-stock-perpetual-contracts-on-binance)

