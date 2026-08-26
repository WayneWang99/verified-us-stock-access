# Interactive Brokers（IBKR）开户与首单

最后人工核验：`2026-08-26`

官方可接受国家与地区列表包含中国；IBKR 还提供“中国居民个人/联名申请人”的材料说明。最终是否开户、账户归属实体和可交易产品以申请结果为准（[S-IBKR-01](../SOURCES.md#s-ibkr-01)、[S-IBKR-02](../SOURCES.md#s-ibkr-02)）。

## 适合谁

- 需要美国及其他全球市场；
- 未来可能使用期权、债券、外汇转换、API 或专业客户端；
- 能接受更复杂的权限、行情订阅和费用设置；
- 有合适的同名银行电汇路径。

## 开户前准备

- 本人有效身份证件；IBKR 中国居民说明称，中国身份证在地址与申请一致时可同时作为身份和住址证明；
- 如身份证地址不同，准备护照、户口、银行账单、手机账单等页面当前接受的地址材料；
- 税务居民信息与税号；
- 雇主/职业、资产、收入、资金来源和投资经验；
- 本人银行资料，用于预计入金和后续提款。

材料清单可能因个案变化，以申请页面补件要求为准。

## 开户步骤

1. 从 IBKR 官方个人账户页点 `Open Account`。
2. 创建用户名，验证邮箱。
3. 选择个人账户；新手优先现金账户，保证金账户需理解借款、日内交易和强平规则。
4. 填写法定姓名、出生日期、国籍、常住地址和联系方式。
5. 填写税务居民身份、职业、财务状况、资金来源和投资目标。
6. 按真实经验申请股票等交易权限；不需要一次申请所有衍生品。
7. 上传身份证件和地址材料。
8. 阅读客户协议并完成电子签署。
9. 提交审核；补件只通过 Client Portal 的通知处理。

## 入金

1. 登录 Client Portal，进入 `Transfer & Pay → Transfer Funds → Make a Deposit`。
2. 选择目标币种和 `Bank Wire`，创建入金通知。
3. 抄录账户里当次显示的收款银行、SWIFT/ABA、收款人和附言信息。
4. 从本人同名银行发起小额测试电汇。
5. 在 Portal 查看通知与实际到账；入金通知本身不会移动资金。
6. 到账后再决定是否在 IBKR 内换成美元，并查看换汇佣金和最小费用。

不要使用网上旧截图里的收款账号，IBKR 可能按币种、账户实体或时期调整指示。

## 第一笔美股订单

1. 在 Client Portal、IBKR Mobile 或 TWS 搜索股票代码。
2. 核对交易所、币种和公司全名，避免选到 CFD、期权或同名海外股票。
3. 选择 `Buy`、数量和限价单；查看预估佣金。
4. 检查是否在常规盘或延长时段，订单有效期是 DAY 还是 GTC。
5. 小额提交，在 `Orders & Trades` 查看成交。
6. 在 `Portfolio` 和 `Statements` 核对持仓、成本和交易确认。

## 费用与数据

IBKR 的固定/阶梯佣金、市场数据订阅、换汇和第三方费用因账户计划、地区、交易所和订单而不同。不要把美国居民的 IBKR Lite“零佣金”直接套到国际账户；在申请实体的定价页和订单预估中核对。

## 退出

- 银行出金：`Transfer & Pay → Withdraw Funds`，只用本人同名账户并先小额测试；
- 转仓：在 `Transfer Positions` 查看支持的 ACATS/FOP 等方式和费用；
- 保存活动报表、月结单、股息/预扣税和年度税务文件。

## 官方来源

- [IBKR 可接受国家和地区](https://portal.interactivebrokers.com/en/accounts/open-account-country-list.php)
- [中国居民开户材料说明](https://www.interactivebrokers.com/en/includes/general/wyn-protrack-cn-individuals.php)
- [个人账户说明](https://www.interactivebrokers.com/en/accounts/individual.php)

