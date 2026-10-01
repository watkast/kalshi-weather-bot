# 15-Minute 1¢ Study

*Updated Thu Oct 1, 5:08 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 130 finished bets | 2% | $8.95 | +47% | +6.88¢ | $18.25 / -$9.30 |

*Expect about **39 buys a day** (~$5.82/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 244 | $1.30 | +5% |
| Volatility model ≥ 5%, sell at 25¢ | 239 | -$2.32 | -9% |
| Volatility model ≥ 5%, sell at 10¢ | 239 | -$3.08 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4191 | 4185 | 14 (0%) | 1.07% | -$317.00 (-62%) | Hold to the close: -$317.00 (-62%) |

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
| Volatility model | 2398 | 3.4% | 0.3% (6) | -578% | ❌ Worse |
| Momentum model | 2398 | 3.5% | 0.3% (6) | -629% | ❌ Worse |
| Mean-reversion model | 2398 | 6.4% | 0.3% (6) | -743% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2398 | 6 | -69% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 485 | 3 | -30% | -61% | -63% | -58% |
| Volatility model ≥ 5% | 239 | 1 | -47% | -26% | -27% | -22% |
| Volatility model ≥ 10% | 141 | 1 | +4% | +23% | +21% | +28% |
| Momentum model ≥ 2% | 426 | 2 | -44% | -56% | -59% | -56% |
| Momentum model ≥ 5% | 244 | 2 | +5% | -32% | -36% | -31% |
| Momentum model ≥ 10% | 161 | 1 | -10% | +1% | +2% | +6% |
| Mean-reversion model ≥ 2% | 905 | 3 | -65% | -85% | -88% | -83% |
| Mean-reversion model ≥ 5% | 598 | 3 | -46% | -82% | -84% | -78% |
| Mean-reversion model ≥ 10% | 380 | 2 | -41% | -78% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2594 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1235 | 3% | 1% | 1% | 1% | 0% | 0% |
| Financials | 356 | 3% | 2% | 1% | 1% | 1% | 1% |
| **All** | 4185 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$317.00 | -62% | — |
| Sell at 2¢ | 154 | 4% | -$458.96 | -89% | 47 sec |
| Sell at 3¢ | 91 | 2% | -$463.51 | -90% | 49 sec |
| Sell at 5¢ | 68 | 2% | -$454.80 | -89% | 66 sec |
| Sell at 10¢ | 49 | 1% | -$420.81 | -82% | 78 sec |
| Sell at 25¢ | 24 | 1% | -$405.56 | -79% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$376.00 | -73% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 130 | 2 | 12% | 3% | +47% | -80% | -88% |
| 2–5 min | 1362 | 6 | 7% | 3% | -57% | -88% | -89% |
| 1–2 min | 1086 | 4 | 3% | 2% | -61% | -94% | -93% |
| Under 1 min | 1607 | 2 | 1% | 0% | -82% | -89% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 293 | 1 | 4% | 1% | -56% | -91% | -91% |
| NEAR | 290 | 0 | 5% | 1% | -100% | -88% | -91% |
| ETH | 290 | 2 | 5% | 3% | -15% | -89% | -87% |
| ZEC | 289 | 1 | 5% | 2% | -59% | -88% | -93% |
| BTC | 287 | 0 | 7% | 3% | -100% | -84% | -87% |
| XRP | 287 | 3 | 2% | 1% | +33% | -51% | -51% |
| HYPE | 287 | 1 | 5% | 3% | -58% | -90% | -88% |
| BNB | 287 | 0 | 4% | 1% | -100% | -91% | -94% |
| SOL | 284 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 214 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 200 | 0 | 2% | 0% | -100% | -97% | -97% |
| WTI | 190 | 1 | 3% | 1% | -45% | -94% | -95% |
| COPPER | 174 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 160 | 1 | 4% | 2% | -42% | -92% | -90% |
| PLATINUM | 151 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 146 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 128 | 1 | 4% | 2% | -27% | -93% | -94% |
| EURUSD | 125 | 1 | 2% | 1% | -25% | -96% | -98% |
| USDJPY | 103 | 2 | 2% | 2% | +81% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2124 | 8 | 4% | 2% | -57% | -92% | -92% |
| DOWN (bought NO) | 2061 | 6 | 4% | 2% | -67% | -86% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 304 | 1 | 1% | 1% | -38% | -34% | -33% |
| 0.05–0.1% | 369 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 621 | 1 | 4% | 2% | -79% | -91% | -92% |
| 0.2–0.5% | 878 | 2 | 6% | 3% | -75% | -89% | -89% |
| Over 0.5% | 421 | 4 | 7% | 3% | -1% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1071 | 2 | 4% | 1% | -79% | -91% | -94% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,227 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 4:59:58 AM | COPPER | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:59:43 AM | ZEC | UP | 17 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/1 4:59:43 AM | WTI | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:59:43 AM | EURUSD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:59:43 AM | HYPE | UP | 17 sec | -0.090% | 0¢ | ❌ Lost | $0.00 |
| 10/1 4:59:11 AM | NEAR | DOWN | 49 sec | +0.183% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:59:11 AM | GOLD | DOWN | 49 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:59:11 AM | GBPUSD | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:58:39 AM | SOL | DOWN | 81 sec | +0.127% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:58:23 AM | SILVER | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:58:23 AM | XRP | DOWN | 1.6 min | +0.181% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:57:19 AM | NATGAS | UP | 2.7 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/1 4:57:19 AM | BNB | UP | 2.7 min | -0.213% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:55:10 AM | DOGE | DOWN | 4.8 min | +0.438% | 2¢ | ❌ Lost | -$0.15 |
| 10/1 4:55:10 AM | BTC | DOWN | 4.8 min | +0.208% | 2¢ | ❌ Lost | -$0.15 |
| 10/1 4:54:54 AM | ETH | DOWN | 5.1 min | +0.316% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:43:42 AM | GOLD | DOWN | 78 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:43:26 AM | PALLADIUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:43:10 AM | NEAR | DOWN | 1.8 min | +0.474% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:43:10 AM | WTI | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:42:55 AM | COPPER | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:42:22 AM | BTC | DOWN | 2.6 min | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:42:06 AM | SILVER | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:41:51 AM | ETH | DOWN | 3.1 min | +0.170% | 0¢ | ❌ Lost | $0.00 |
| 10/1 4:41:51 AM | SOL | DOWN | 3.1 min | +0.274% | 0¢ | ❌ Lost | $0.00 |
| 10/1 4:41:35 AM | XRP | DOWN | 3.4 min | +0.338% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:40:31 AM | ZEC | DOWN | 4.5 min | +0.454% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:40:15 AM | DOGE | DOWN | 4.7 min | +0.314% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:39:59 AM | BNB | DOWN | 5.0 min | +0.148% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:38:39 AM | HYPE | DOWN | 6.3 min | +0.728% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
