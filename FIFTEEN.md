# 15-Minute 1¢ Study

*Updated Wed Oct 28, 6:51 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3045 finished bets | 1% | $78.00 | +23% | +2.56¢ | $83.55 / -$5.55 |

*Expect about **99 buys a day** (~$14.85/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2825 | $40.55 | +13% |
| Volatility model ≥ 2%, hold to the close | 5629 | $1.25 | +0% |
| Momentum model ≥ 2%, hold to the close | 4656 | -$65.05 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 37191 | 37183 | 139 (0%) | 1.07% | -$2,591.80 (-57%) | Hold to the close: -$2,591.80 (-57%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 23113 | 4.7% | 0.4% (92) | -680% | ❌ Worse |
| Momentum model | 23113 | 4.6% | 0.4% (92) | -703% | ❌ Worse |
| Mean-reversion model | 23113 | 8.1% | 0.4% (92) | -825% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23113 | 92 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5629 | 49 | +0% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3045 | 30 | +23% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1727 | 19 | +56% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4656 | 34 | -12% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2825 | 25 | +13% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1850 | 17 | +27% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9449 | 63 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6630 | 53 | -12% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4427 | 38 | -3% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23313 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8881 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4989 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 37183 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 139 | 0% | -$2,591.80 | -57% | — |
| Sell at 2¢ | 1414 | 4% | -$3,974.16 | -88% | 47 sec |
| Sell at 3¢ | 973 | 3% | -$3,962.33 | -87% | 48 sec |
| Sell at 5¢ | 675 | 2% | -$3,903.05 | -86% | 63 sec |
| Sell at 10¢ | 409 | 1% | -$3,750.01 | -83% | 65 sec |
| Sell at 25¢ | 219 | 1% | -$3,462.91 | -76% | 83 sec |
| Sell at 50¢ | 144 | 0% | -$3,131.80 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1662 | 8 | 11% | 4% | -54% | -80% | -81% |
| 2–5 min | 11874 | 66 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9417 | 32 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14226 | 33 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2610 | 12 | 5% | 2% | -41% | -88% | -88% |
| HYPE | 2604 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2603 | 15 | 5% | 2% | -28% | -85% | -83% |
| SOL | 2596 | 7 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2591 | 11 | 6% | 3% | -49% | -85% | -85% |
| DOGE | 2589 | 5 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2575 | 11 | 3% | 1% | -47% | -89% | -89% |
| NEAR | 2573 | 12 | 5% | 2% | -40% | -82% | -82% |
| BTC | 2572 | 13 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1400 | 5 | 4% | 2% | -57% | -82% | -83% |
| SILVER | 1371 | 6 | 4% | 2% | -48% | -82% | -82% |
| WTI | 1354 | 4 | 3% | 1% | -65% | -93% | -94% |
| PLATINUM | 1217 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1155 | 4 | 1% | 1% | -68% | -74% | -73% |
| EURUSD | 1141 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1118 | 7 | 2% | 1% | -42% | -80% | -79% |
| GBPUSD | 1083 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1079 | 2 | 1% | 0% | -83% | -89% | -90% |
| USDJPY | 1063 | 5 | 2% | 1% | -56% | -97% | -96% |
| AUDUSD | 618 | 4 | 1% | 1% | -40% | -83% | -82% |
| USDCAD | 585 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 187 | 0 | 1% | 1% | -100% | -99% | -99% |
| 10YRRATE | 133 | 0 | 5% | 1% | -100% | -92% | -90% |
| 30YRRATE | 125 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 124 | 1 | 4% | 1% | -25% | -18% | -16% |
| 5YRRATE | 117 | 1 | 6% | 3% | -20% | -90% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18814 | 77 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 18369 | 62 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3838 | 19 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 4019 | 14 | 3% | 2% | -48% | -92% | -92% |
| 0.1–0.2% | 6066 | 22 | 5% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6859 | 29 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2527 | 10 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9232 | 42 | 4% | 2% | -48% | -86% | -85% |
| Afternoon (12–6pm) | 8852 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 9870 | 33 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,553 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 6:44:48 PM | WTI | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:44:48 PM | PALLADIUM | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:44:48 PM | PLATINUM | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:44:48 PM | ETH | UP | 12 sec | -0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 6:44:32 PM | BTC | UP | 28 sec | -0.089% | 0¢ | ❌ Lost | $0.00 |
| 10/28 6:44:16 PM | XRP | UP | 44 sec | -0.068% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:44:16 PM | DOGE | UP | 44 sec | -0.119% | 0¢ | ❌ Lost | $0.00 |
| 10/28 6:44:01 PM | GOLD | UP | 58 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 6:43:29 PM | SILVER | UP | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 6:43:13 PM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:43:13 PM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:43:13 PM | USDCAD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:42:41 PM | NEAR | UP | 2.3 min | -0.390% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 6:42:41 PM | AUDUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:42:25 PM | GBPUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:42:25 PM | USDJPY | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:41:03 PM | HYPE | UP | 4.0 min | -0.326% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 6:40:47 PM | ZEC | UP | 4.2 min | -0.649% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:40:47 PM | SOL | UP | 4.2 min | -0.260% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 6:38:38 PM | BNB | UP | 6.3 min | -0.297% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 6:29:48 PM | PALLADIUM | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:29:48 PM | USDJPY | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:29:48 PM | WTI | DOWN | 12 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 6:29:48 PM | ETH | UP | 12 sec | -0.091% | 0¢ | ❌ Lost | $0.00 |
| 10/28 6:29:32 PM | BNB | DOWN | 28 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/28 6:29:32 PM | HYPE | UP | 28 sec | -0.068% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:29:32 PM | NEAR | UP | 28 sec | -0.282% | 0¢ | ❌ Lost | $0.00 |
| 10/28 6:29:32 PM | XRP | UP | 28 sec | -0.075% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 6:29:32 PM | AUDUSD | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:29:01 PM | DOGE | DOWN | 58 sec | +0.054% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
