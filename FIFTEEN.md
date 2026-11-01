# 15-Minute 1¢ Study

*Updated Sun Nov 1, 2:31 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3437 finished bets | 1% | $120.00 | +31% | +3.49¢ | $75.35 / $44.65 |

*Expect about **99 buys a day** (~$14.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3175 | $46.55 | +13% |
| Volatility model ≥ 2%, hold to the close | 6343 | $44.15 | +6% |
| Momentum model ≥ 2%, hold to the close | 5234 | -$45.10 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41575 | 41564 | 156 (0%) | 1.07% | -$2,872.50 (-57%) | Hold to the close: -$2,872.50 (-57%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 25963 | 4.7% | 0.4% (103) | -685% | ❌ Worse |
| Momentum model | 25963 | 4.6% | 0.4% (103) | -707% | ❌ Worse |
| Mean-reversion model | 25963 | 8.1% | 0.4% (103) | -833% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 25963 | 103 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6343 | 58 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3437 | 36 | +31% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 1949 | 21 | +54% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5234 | 40 | -7% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3175 | 28 | +13% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 2074 | 19 | +28% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10709 | 73 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7503 | 63 | -7% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5019 | 45 | +2% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26165 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41564 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 156 | 0% | -$2,872.50 | -57% | — |
| Sell at 2¢ | 1626 | 4% | -$4,409.74 | -87% | 47 sec |
| Sell at 3¢ | 1118 | 3% | -$4,396.48 | -87% | 48 sec |
| Sell at 5¢ | 776 | 2% | -$4,300.10 | -85% | 63 sec |
| Sell at 10¢ | 468 | 1% | -$4,121.42 | -82% | 65 sec |
| Sell at 25¢ | 248 | 1% | -$3,801.62 | -75% | 83 sec |
| Sell at 50¢ | 161 | 0% | -$3,451.75 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1958 | 9 | 11% | 4% | -56% | -80% | -82% |
| 2–5 min | 13314 | 73 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10516 | 37 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 15765 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2930 | 13 | 5% | 3% | -43% | -88% | -88% |
| SOL | 2920 | 10 | 4% | 2% | -57% | -91% | -91% |
| HYPE | 2918 | 9 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2918 | 17 | 5% | 2% | -27% | -85% | -84% |
| ETH | 2907 | 11 | 7% | 3% | -54% | -85% | -84% |
| DOGE | 2907 | 6 | 4% | 2% | -74% | -90% | -90% |
| BTC | 2890 | 14 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 2888 | 14 | 5% | 2% | -37% | -83% | -83% |
| XRP | 2887 | 11 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1515 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1481 | 7 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1476 | 4 | 3% | 1% | -67% | -93% | -93% |
| PLATINUM | 1314 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1253 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1249 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1212 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1185 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1178 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1171 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 705 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 685 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 283 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21097 | 86 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20467 | 70 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4289 | 21 | 2% | 1% | -15% | -82% | -81% |
| 0.05–0.1% | 4510 | 17 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 6764 | 23 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 7705 | 33 | 7% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2892 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10303 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9742 | 35 | 4% | 2% | -58% | -87% | -87% |
| Evening (6pm–12am) | 11006 | 37 | 3% | 2% | -61% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,786 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 2:29:43 PM | SOL | DOWN | 17 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 11/1 2:29:43 PM | ETH | DOWN | 17 sec | +0.009% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 2:29:27 PM | BTC | DOWN | 33 sec | +0.015% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 2:29:27 PM | XRP | DOWN | 33 sec | +0.032% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:28:56 PM | BNB | DOWN | 63 sec | +0.023% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:28:40 PM | NEAR | UP | 79 sec | -0.171% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:27:35 PM | HYPE | DOWN | 2.4 min | +0.219% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:25:03 PM | ZEC | DOWN | 4.9 min | +0.508% | 1¢ | In play | — |
| 11/1 2:14:49 PM | BTC | UP | 11 sec | -0.012% | 0¢ | ❌ Lost | $0.00 |
| 11/1 2:14:29 PM | SOL | DOWN | 31 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 11/1 2:14:13 PM | DOGE | DOWN | 47 sec | +0.021% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 2:14:13 PM | ZEC | DOWN | 47 sec | +0.020% | 0¢ | ❌ Lost | $0.00 |
| 11/1 2:14:13 PM | XRP | DOWN | 47 sec | +0.032% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 2:13:57 PM | ETH | DOWN | 63 sec | +0.019% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 2:13:41 PM | HYPE | UP | 79 sec | -0.097% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:12:45 PM | BNB | UP | 2.2 min | -0.112% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:12:45 PM | NEAR | UP | 2.2 min | -0.285% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 1:59:10 PM | DOGE | UP | 49 sec | -0.052% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:59:10 PM | ZEC | DOWN | 49 sec | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 11/1 1:59:10 PM | BNB | UP | 49 sec | -0.037% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 1:58:52 PM | HYPE | DOWN | 68 sec | +0.052% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:58:52 PM | BTC | DOWN | 68 sec | +0.030% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:58:52 PM | ETH | DOWN | 68 sec | +0.035% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 1:58:20 PM | SOL | DOWN | 1.7 min | +0.056% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:57:15 PM | XRP | UP | 2.8 min | -0.136% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 1:56:20 PM | NEAR | DOWN | 3.7 min | +0.197% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:44:33 PM | ZEC | DOWN | 26 sec | +0.037% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 1:42:48 PM | BTC | DOWN | 2.2 min | +0.089% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 1:42:22 PM | BNB | DOWN | 2.6 min | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:40:03 PM | SOL | DOWN | 5.0 min | +0.251% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
