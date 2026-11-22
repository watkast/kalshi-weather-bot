# 15-Minute 1¢ Study

*Updated Sun Nov 22, 5:56 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4711 finished bets | 1% | $198.45 | +38% | +4.21¢ | $70.50 / $127.95 |

*Expect about **85 buys a day** (~$12.79/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4471 | $94.75 | +20% |
| Volatility model ≥ 2%, hold to the close | 8806 | $39.00 | +4% |
| Momentum model ≥ 2%, hold to the close | 7337 | -$39.00 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 64483 | 64449 | 247 (0%) | 1.07% | -$4,353.70 (-56%) | Hold to the close: -$4,353.70 (-56%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 38505 | 4.5% | 0.4% (159) | -639% | ❌ Worse |
| Momentum model | 38505 | 4.4% | 0.4% (159) | -663% | ❌ Worse |
| Mean-reversion model | 38505 | 7.8% | 0.4% (159) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 38505 | 159 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8806 | 78 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4711 | 51 | +38% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2716 | 30 | +62% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7337 | 57 | -5% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4471 | 41 | +20% | -75% | -74% | -71% |
| Momentum model ≥ 10% | 2906 | 26 | +28% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15675 | 109 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10889 | 89 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7235 | 64 | +1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 38711 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15273 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 64449 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 247 | 0% | -$4,353.70 | -56% | — |
| Sell at 2¢ | 2614 | 4% | -$6,838.06 | -88% | 47 sec |
| Sell at 3¢ | 1758 | 3% | -$6,832.08 | -87% | 48 sec |
| Sell at 5¢ | 1195 | 2% | -$6,712.95 | -86% | 62 sec |
| Sell at 10¢ | 729 | 1% | -$6,450.71 | -83% | 65 sec |
| Sell at 25¢ | 392 | 1% | -$5,954.18 | -76% | 80 sec |
| Sell at 50¢ | 255 | 0% | -$5,376.45 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3335 | 17 | 10% | 4% | -52% | -82% | -83% |
| 2–5 min | 20893 | 110 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 16102 | 57 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 24106 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4328 | 19 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4321 | 14 | 5% | 2% | -58% | -89% | -88% |
| SOL | 4320 | 19 | 4% | 2% | -43% | -86% | -87% |
| BNB | 4311 | 22 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 4306 | 11 | 4% | 2% | -67% | -90% | -89% |
| ETH | 4303 | 19 | 7% | 3% | -45% | -82% | -82% |
| BTC | 4280 | 23 | 5% | 2% | -26% | -86% | -88% |
| NEAR | 4277 | 18 | 5% | 2% | -45% | -85% | -86% |
| XRP | 4265 | 16 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2265 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2257 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2209 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2012 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1968 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1900 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1895 | 6 | 2% | 1% | -70% | -77% | -77% |
| NATGAS | 1858 | 10 | 2% | 1% | -50% | -76% | -76% |
| USDJPY | 1855 | 6 | 2% | 1% | -70% | -96% | -96% |
| PALLADIUM | 1808 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1406 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1340 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 969 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 499 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 476 | 4 | 4% | 2% | -22% | -54% | -53% |
| 30YRRATE | 462 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 451 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32955 | 128 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31494 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5680 | 25 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 6215 | 25 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 9615 | 35 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12097 | 53 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5095 | 23 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15520 | 48 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15462 | 81 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15735 | 67 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17732 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,134 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/22 5:44:23 AM | BTC | DOWN | 36 sec | +0.236% | 0¢ | ❌ Lost | $0.00 |
| 11/22 5:43:49 AM | DOGE | DOWN | 71 sec | +0.193% | 0¢ | ❌ Lost | $0.00 |
| 11/22 5:43:49 AM | XRP | DOWN | 71 sec | +0.228% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 5:43:49 AM | SOL | DOWN | 71 sec | +0.204% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 5:43:49 AM | ETH | DOWN | 71 sec | +0.213% | 0¢ | ❌ Lost | $0.00 |
| 11/22 5:43:49 AM | NEAR | DOWN | 71 sec | +0.248% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 5:43:33 AM | BNB | DOWN | 87 sec | +0.225% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 5:42:46 AM | HYPE | DOWN | 2.2 min | +0.369% | 0¢ | ❌ Lost | $0.00 |
| 11/22 5:41:58 AM | ZEC | DOWN | 3.0 min | +0.741% | 0¢ | ❌ Lost | $0.00 |
| 11/22 5:28:36 AM | NEAR | UP | 84 sec | -1.308% | 0¢ | ❌ Lost | $0.00 |
| 11/22 5:28:20 AM | BNB | UP | 1.7 min | -0.427% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 5:26:13 AM | SOL | UP | 3.8 min | -0.714% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 5:25:26 AM | DOGE | UP | 4.6 min | -0.911% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 5:25:26 AM | XRP | UP | 4.6 min | -1.118% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 5:25:26 AM | ETH | UP | 4.6 min | -0.982% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 5:24:31 AM | BTC | UP | 5.5 min | -1.103% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 5:24:31 AM | ZEC | UP | 5.5 min | -1.909% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 5:24:31 AM | HYPE | UP | 5.5 min | -1.030% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 5:14:28 AM | ZEC | DOWN | 31 sec | +0.157% | 0¢ | ❌ Lost | $0.00 |
| 11/22 5:14:12 AM | DOGE | DOWN | 48 sec | +0.099% | 0¢ | ❌ Lost | $0.00 |
| 11/22 5:13:40 AM | HYPE | DOWN | 80 sec | +0.172% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 5:12:35 AM | BTC | DOWN | 2.4 min | +0.251% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 5:12:35 AM | ETH | DOWN | 2.4 min | +0.214% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 5:11:14 AM | XRP | DOWN | 3.8 min | +0.313% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 5:11:14 AM | BNB | DOWN | 3.8 min | +0.206% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 5:09:04 AM | NEAR | DOWN | 5.9 min | +0.697% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 4:59:38 AM | XRP | UP | 21 sec | -0.118% | 0¢ | ❌ Lost | $0.00 |
| 11/22 4:59:22 AM | SOL | UP | 37 sec | -0.099% | 0¢ | ❌ Lost | $0.00 |
| 11/22 4:59:06 AM | ZEC | DOWN | 54 sec | +0.160% | 0¢ | ❌ Lost | $0.00 |
| 11/22 4:59:06 AM | ETH | DOWN | 54 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
