# 15-Minute 1¢ Study

*Updated Tue Oct 27, 11:37 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2867 finished bets | 1% | $82.15 | +25% | +2.87¢ | $79.60 / $2.55 |

*Expect about **97 buys a day** (~$14.60/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2675 | $41.25 | +14% |
| Volatility model ≥ 2%, hold to the close | 5322 | -$6.55 | -1% |
| Momentum model ≥ 2%, hold to the close | 4422 | -$54.15 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34910 | 34902 | 132 (0%) | 1.07% | -$2,403.15 (-57%) | Hold to the close: -$2,403.15 (-57%) |

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
| Volatility model | 22040 | 4.6% | 0.4% (88) | -672% | ❌ Worse |
| Momentum model | 22040 | 4.6% | 0.4% (88) | -697% | ❌ Worse |
| Mean-reversion model | 22040 | 8.0% | 0.4% (88) | -816% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22040 | 88 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5322 | 46 | -1% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2867 | 29 | +25% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1628 | 18 | +56% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4422 | 33 | -10% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2675 | 24 | +14% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1748 | 16 | +26% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8944 | 59 | -28% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6262 | 49 | -14% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4179 | 35 | -6% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22240 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8246 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4416 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34902 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 132 | 0% | -$2,403.15 | -57% | — |
| Sell at 2¢ | 1319 | 4% | -$3,712.21 | -87% | 47 sec |
| Sell at 3¢ | 898 | 3% | -$3,704.93 | -87% | 48 sec |
| Sell at 5¢ | 621 | 2% | -$3,651.50 | -86% | 62 sec |
| Sell at 10¢ | 383 | 1% | -$3,497.42 | -82% | 65 sec |
| Sell at 25¢ | 207 | 1% | -$3,229.98 | -76% | 1.5 min |
| Sell at 50¢ | 137 | 0% | -$2,906.40 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1551 | 8 | 11% | 4% | -51% | -81% | -82% |
| 2–5 min | 11186 | 62 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 8850 | 31 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 13311 | 31 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2491 | 12 | 5% | 2% | -39% | -89% | -89% |
| HYPE | 2482 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2482 | 15 | 5% | 2% | -24% | -84% | -83% |
| SOL | 2478 | 6 | 4% | 2% | -70% | -92% | -92% |
| ETH | 2472 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2467 | 5 | 4% | 2% | -75% | -91% | -90% |
| NEAR | 2460 | 12 | 5% | 2% | -37% | -82% | -82% |
| XRP | 2456 | 9 | 3% | 1% | -55% | -89% | -89% |
| BTC | 2452 | 12 | 5% | 2% | -34% | -88% | -89% |
| GOLD | 1314 | 5 | 4% | 2% | -55% | -81% | -83% |
| SILVER | 1283 | 6 | 4% | 2% | -45% | -82% | -82% |
| WTI | 1263 | 4 | 3% | 1% | -62% | -93% | -94% |
| PLATINUM | 1135 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1087 | 4 | 1% | 1% | -66% | -72% | -72% |
| EURUSD | 1057 | 3 | 2% | 1% | -74% | -87% | -87% |
| NATGAS | 1045 | 6 | 2% | 1% | -46% | -79% | -78% |
| PALLADIUM | 1002 | 2 | 1% | 0% | -81% | -89% | -89% |
| GBPUSD | 997 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 983 | 5 | 1% | 1% | -53% | -98% | -97% |
| AUDUSD | 542 | 3 | 1% | 1% | -48% | -81% | -79% |
| USDCAD | 502 | 0 | 1% | 0% | -100% | -98% | -98% |
| BRENT | 117 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 92 | 0 | 4% | 0% | -100% | -92% | -92% |
| 30YRRATE | 82 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 81 | 1 | 4% | 1% | +15% | +22% | +22% |
| 5YRRATE | 80 | 1 | 5% | 2% | +17% | -91% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17653 | 73 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 17249 | 59 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3651 | 18 | 2% | 1% | -16% | -81% | -80% |
| 0.05–0.1% | 3805 | 13 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 5776 | 20 | 5% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 6557 | 29 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2447 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8700 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,648 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 11:29:44 AM | SILVER | DOWN | 15 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 11:29:28 AM | GOLD | DOWN | 31 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:29:12 AM | XRP | DOWN | 47 sec | +0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/27 11:29:12 AM | ZEC | DOWN | 47 sec | +0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/27 11:29:12 AM | BNB | UP | 47 sec | -0.111% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:28:41 AM | NEAR | DOWN | 79 sec | +0.059% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:28:25 AM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:28:09 AM | SOL | DOWN | 1.9 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:27:53 AM | ETH | DOWN | 2.1 min | +0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:26:22 AM | BTC | DOWN | 3.6 min | +0.206% | 2¢ | ❌ Lost | -$0.15 |
| 10/27 11:25:04 AM | HYPE | DOWN | 4.9 min | +0.554% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:24:33 AM | DOGE | DOWN | 5.4 min | +0.423% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:14:46 AM | SILVER | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:14:46 AM | BTC | UP | 13 sec | -0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:14:46 AM | 10YRRATE | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:14:46 AM | SOL | UP | 13 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/27 11:14:46 AM | ETH | UP | 13 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 10/27 11:14:30 AM | 30YRRATE | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:14:30 AM | BNB | DOWN | 29 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/27 11:14:14 AM | ZEC | UP | 45 sec | -0.210% | 0¢ | ❌ Lost | $0.00 |
| 10/27 11:13:58 AM | NEAR | UP | 61 sec | -0.347% | 0¢ | ❌ Lost | $0.00 |
| 10/27 11:13:58 AM | XRP | UP | 61 sec | -0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:13:58 AM | PALLADIUM | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:13:27 AM | DOGE | UP | 1.6 min | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:13:27 AM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:13:27 AM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:12:39 AM | HYPE | DOWN | 2.3 min | +0.313% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:12:07 AM | GBPUSD | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 10:59:57 AM | 2YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:59:57 AM | 30YRRATE | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
