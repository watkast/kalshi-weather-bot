# 15-Minute 1¢ Study

*Updated Thu Oct 1, 8:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 147 finished bets | 1% | $6.40 | +30% | +4.35¢ | $17.05 / -$10.65 |

*Expect about **37 buys a day** (~$5.50/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 303 | -$5.15 | -16% |
| 5+ min left, sell at 50¢ | 147 | -$8.10 | -38% |
| Volatility model ≥ 5%, sell at 25¢ | 294 | -$8.32 | -26% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4973 | 4967 | 15 (0%) | 1.07% | -$396.00 (-65%) | Hold to the close: -$396.00 (-65%) |

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
| Volatility model | 2857 | 3.5% | 0.2% (6) | -700% | ❌ Worse |
| Momentum model | 2857 | 3.7% | 0.2% (6) | -755% | ❌ Worse |
| Mean-reversion model | 2857 | 6.6% | 0.2% (6) | -892% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2857 | 6 | -73% | -85% | -87% | -84% |
| Volatility model ≥ 2% | 585 | 3 | -41% | -64% | -66% | -62% |
| Volatility model ≥ 5% | 294 | 1 | -57% | -37% | -37% | -34% |
| Volatility model ≥ 10% | 166 | 1 | -11% | +5% | +4% | +10% |
| Momentum model ≥ 2% | 524 | 2 | -54% | -62% | -65% | -62% |
| Momentum model ≥ 5% | 303 | 2 | -16% | -44% | -46% | -42% |
| Momentum model ≥ 10% | 203 | 1 | -30% | -21% | -20% | -17% |
| Mean-reversion model ≥ 2% | 1081 | 3 | -70% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 713 | 3 | -54% | -82% | -85% | -79% |
| Mean-reversion model ≥ 10% | 453 | 2 | -50% | -78% | -81% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3053 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1466 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 448 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 4967 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 15 | 0% | -$396.00 | -65% | — |
| Sell at 2¢ | 179 | 4% | -$545.46 | -90% | 45 sec |
| Sell at 3¢ | 107 | 2% | -$550.27 | -91% | 49 sec |
| Sell at 5¢ | 78 | 2% | -$541.30 | -89% | 66 sec |
| Sell at 10¢ | 56 | 1% | -$504.64 | -83% | 81 sec |
| Sell at 25¢ | 26 | 1% | -$477.94 | -79% | 1.6 min |
| Sell at 50¢ | 13 | 0% | -$448.25 | -74% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 144 | 2 | 12% | 3% | +32% | -78% | -89% |
| 2–5 min | 1630 | 7 | 7% | 3% | -58% | -88% | -89% |
| 1–2 min | 1306 | 4 | 3% | 2% | -67% | -94% | -93% |
| Under 1 min | 1884 | 2 | 1% | 0% | -84% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 345 | 1 | 4% | 1% | -62% | -91% | -93% |
| ZEC | 341 | 1 | 5% | 2% | -65% | -89% | -93% |
| BNB | 341 | 0 | 4% | 1% | -100% | -92% | -94% |
| ETH | 340 | 2 | 5% | 3% | -28% | -89% | -86% |
| BTC | 339 | 0 | 6% | 3% | -100% | -84% | -88% |
| HYPE | 339 | 1 | 4% | 3% | -64% | -90% | -88% |
| NEAR | 337 | 0 | 5% | 1% | -100% | -87% | -91% |
| XRP | 336 | 3 | 1% | 1% | +15% | -58% | -57% |
| SOL | 335 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 253 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 236 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 222 | 1 | 3% | 1% | -53% | -95% | -96% |
| COPPER | 209 | 0 | 1% | 0% | -100% | -98% | -99% |
| NATGAS | 188 | 1 | 4% | 2% | -50% | -94% | -92% |
| PLATINUM | 184 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 174 | 0 | 2% | 1% | -100% | -97% | -99% |
| GBPUSD | 159 | 1 | 4% | 2% | -41% | -92% | -93% |
| EURUSD | 157 | 1 | 4% | 2% | -41% | -93% | -93% |
| USDJPY | 132 | 3 | 3% | 2% | +112% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2526 | 9 | 4% | 2% | -59% | -92% | -92% |
| DOWN (bought NO) | 2441 | 6 | 4% | 1% | -72% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 365 | 1 | 1% | 1% | -48% | -44% | -44% |
| 0.05–0.1% | 432 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 739 | 1 | 4% | 1% | -82% | -91% | -92% |
| 0.2–0.5% | 1028 | 2 | 6% | 3% | -78% | -88% | -89% |
| Over 0.5% | 488 | 4 | 7% | 2% | -15% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1469 | 4 | 3% | 2% | -68% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,190 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 8:44:47 PM | XRP | DOWN | 13 sec | +0.020% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:44:47 PM | PALLADIUM | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:44:47 PM | HYPE | DOWN | 13 sec | +0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:44:47 PM | SOL | UP | 13 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:44:31 PM | PLATINUM | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:44:31 PM | ETH | DOWN | 29 sec | +0.031% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:44:15 PM | NEAR | DOWN | 45 sec | +0.134% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:44:15 PM | USDJPY | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:44:09 PM | BTC | DOWN | 51 sec | +0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:44:09 PM | ZEC | DOWN | 51 sec | +0.260% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:43:52 PM | DOGE | DOWN | 67 sec | +0.097% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:43:20 PM | BNB | DOWN | 1.6 min | +0.019% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:43:20 PM | SILVER | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:43:04 PM | GOLD | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:29:47 PM | GBPUSD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:29:05 PM | PALLADIUM | DOWN | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:28:17 PM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:28:17 PM | SILVER | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:28:17 PM | HYPE | UP | 1.7 min | -0.184% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:28:17 PM | SOL | UP | 1.7 min | -0.301% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:28:01 PM | PLATINUM | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:28:01 PM | GOLD | DOWN | 2.0 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:26:23 PM | EURUSD | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:26:07 PM | XRP | UP | 3.9 min | -0.326% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:25:35 PM | DOGE | UP | 4.4 min | -0.453% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:25:19 PM | ETH | UP | 4.7 min | -0.329% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:25:19 PM | BNB | UP | 4.7 min | -0.237% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:25:19 PM | BTC | UP | 4.7 min | -0.254% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:25:19 PM | ZEC | UP | 4.7 min | -0.841% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:14:21 PM | HYPE | DOWN | 39 sec | +0.055% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
