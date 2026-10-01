# 15-Minute 1¢ Study

*Updated Thu Oct 1, 5:18 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 130 finished bets | 2% | $8.95 | +47% | +6.88¢ | $18.25 / -$9.30 |

*Expect about **39 buys a day** (~$5.80/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 246 | $1.00 | +4% |
| Volatility model ≥ 5%, sell at 25¢ | 240 | -$2.47 | -9% |
| Volatility model ≥ 5%, sell at 10¢ | 240 | -$3.23 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4207 | 4201 | 14 (0%) | 1.07% | -$319.25 (-62%) | Hold to the close: -$319.25 (-62%) |

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
| Volatility model | 2407 | 3.4% | 0.2% (6) | -577% | ❌ Worse |
| Momentum model | 2407 | 3.5% | 0.2% (6) | -628% | ❌ Worse |
| Mean-reversion model | 2407 | 6.4% | 0.2% (6) | -742% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2407 | 6 | -69% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 489 | 3 | -30% | -61% | -63% | -58% |
| Volatility model ≥ 5% | 240 | 1 | -47% | -26% | -28% | -22% |
| Volatility model ≥ 10% | 141 | 1 | +4% | +23% | +21% | +28% |
| Momentum model ≥ 2% | 429 | 2 | -44% | -56% | -60% | -57% |
| Momentum model ≥ 5% | 246 | 2 | +4% | -33% | -37% | -31% |
| Momentum model ≥ 10% | 161 | 1 | -10% | +1% | +2% | +6% |
| Mean-reversion model ≥ 2% | 909 | 3 | -65% | -85% | -88% | -83% |
| Mean-reversion model ≥ 5% | 598 | 3 | -46% | -82% | -84% | -78% |
| Mean-reversion model ≥ 10% | 380 | 2 | -41% | -78% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2603 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1241 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 357 | 3% | 2% | 1% | 1% | 1% | 1% |
| **All** | 4201 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$319.25 | -62% | — |
| Sell at 2¢ | 154 | 4% | -$461.21 | -90% | 47 sec |
| Sell at 3¢ | 91 | 2% | -$465.76 | -90% | 49 sec |
| Sell at 5¢ | 68 | 2% | -$457.05 | -89% | 66 sec |
| Sell at 10¢ | 49 | 1% | -$423.06 | -82% | 78 sec |
| Sell at 25¢ | 24 | 1% | -$407.81 | -79% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$378.25 | -73% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 130 | 2 | 12% | 3% | +47% | -80% | -88% |
| 2–5 min | 1369 | 6 | 7% | 3% | -58% | -88% | -89% |
| 1–2 min | 1093 | 4 | 3% | 2% | -61% | -94% | -93% |
| Under 1 min | 1609 | 2 | 1% | 0% | -82% | -89% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 294 | 1 | 4% | 1% | -56% | -91% | -91% |
| NEAR | 291 | 0 | 5% | 1% | -100% | -88% | -91% |
| ETH | 291 | 2 | 5% | 3% | -15% | -89% | -87% |
| ZEC | 290 | 1 | 5% | 2% | -59% | -88% | -93% |
| BTC | 288 | 0 | 7% | 3% | -100% | -84% | -87% |
| XRP | 288 | 3 | 2% | 1% | +33% | -52% | -51% |
| HYPE | 288 | 1 | 5% | 3% | -58% | -90% | -88% |
| BNB | 288 | 0 | 4% | 1% | -100% | -91% | -94% |
| SOL | 285 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 215 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 201 | 0 | 1% | 0% | -100% | -97% | -97% |
| WTI | 191 | 1 | 3% | 1% | -45% | -94% | -95% |
| COPPER | 175 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 161 | 1 | 4% | 2% | -42% | -92% | -90% |
| PLATINUM | 151 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 147 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 129 | 1 | 4% | 2% | -28% | -93% | -94% |
| EURUSD | 125 | 1 | 2% | 1% | -25% | -96% | -98% |
| USDJPY | 103 | 2 | 2% | 2% | +81% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2138 | 8 | 4% | 2% | -57% | -92% | -93% |
| DOWN (bought NO) | 2063 | 6 | 4% | 2% | -67% | -86% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 304 | 1 | 1% | 1% | -38% | -34% | -33% |
| 0.05–0.1% | 370 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 625 | 1 | 4% | 2% | -79% | -91% | -92% |
| 0.2–0.5% | 881 | 2 | 6% | 3% | -75% | -89% | -89% |
| Over 0.5% | 422 | 4 | 7% | 3% | -2% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1087 | 2 | 4% | 1% | -79% | -92% | -94% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,234 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 5:14:51 AM | GBPUSD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:14:19 AM | NEAR | UP | 40 sec | -0.315% | 0¢ | ❌ Lost | $0.00 |
| 10/1 5:13:47 AM | COPPER | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:13:47 AM | PALLADIUM | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:13:31 AM | DOGE | UP | 88 sec | -0.148% | 2¢ | ❌ Lost | -$0.15 |
| 10/1 5:13:31 AM | SOL | UP | 88 sec | -0.165% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:13:15 AM | GOLD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:13:15 AM | HYPE | UP | 1.7 min | -0.216% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 5:13:15 AM | BNB | UP | 1.7 min | -0.088% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:12:59 AM | BTC | UP | 2.0 min | -0.104% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 5:12:43 AM | XRP | UP | 2.3 min | -0.261% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 5:12:27 AM | ETH | UP | 2.5 min | -0.149% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 5:12:11 AM | NATGAS | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:10:51 AM | SILVER | UP | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 5:10:19 AM | WTI | DOWN | 4.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 5:10:03 AM | ZEC | UP | 4.9 min | -0.684% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
