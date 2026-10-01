# 15-Minute 1¢ Study

*Updated Thu Oct 1, 8:57 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 137 finished bets | 1% | $7.90 | +39% | +5.77¢ | $17.80 / -$9.90 |

*Expect about **39 buys a day** (~$5.85/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 258 | -$0.50 | -2% |
| Volatility model ≥ 5%, sell at 25¢ | 249 | -$3.52 | -13% |
| Volatility model ≥ 5%, sell at 10¢ | 249 | -$4.28 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4352 | 4343 | 14 (0%) | 1.07% | -$336.80 (-63%) | Hold to the close: -$336.80 (-63%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 2484 | 3.4% | 0.2% (6) | -621% | ❌ Worse |
| Momentum model | 2484 | 3.5% | 0.2% (6) | -672% | ❌ Worse |
| Mean-reversion model | 2484 | 6.5% | 0.2% (6) | -790% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2484 | 6 | -70% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 503 | 3 | -32% | -62% | -64% | -60% |
| Volatility model ≥ 5% | 249 | 1 | -49% | -29% | -31% | -25% |
| Volatility model ≥ 10% | 144 | 1 | +0% | +19% | +17% | +24% |
| Momentum model ≥ 2% | 446 | 2 | -47% | -57% | -61% | -58% |
| Momentum model ≥ 5% | 258 | 2 | -2% | -36% | -40% | -35% |
| Momentum model ≥ 10% | 169 | 1 | -16% | -5% | -4% | -0% |
| Mean-reversion model ≥ 2% | 932 | 3 | -66% | -85% | -88% | -83% |
| Mean-reversion model ≥ 5% | 612 | 3 | -48% | -82% | -84% | -77% |
| Mean-reversion model ≥ 10% | 391 | 2 | -43% | -77% | -80% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2680 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1288 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 375 | 3% | 2% | 1% | 1% | 1% | 1% |
| **All** | 4343 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$336.80 | -63% | — |
| Sell at 2¢ | 161 | 4% | -$476.94 | -90% | 45 sec |
| Sell at 3¢ | 94 | 2% | -$482.14 | -90% | 48 sec |
| Sell at 5¢ | 70 | 2% | -$473.30 | -89% | 65 sec |
| Sell at 10¢ | 50 | 1% | -$439.30 | -82% | 78 sec |
| Sell at 25¢ | 24 | 1% | -$425.36 | -80% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$395.80 | -74% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 1 | 0 | 100% | 0% | -100% | +73% | +160% |
| 5–10 min | 136 | 2 | 13% | 3% | +40% | -77% | -88% |
| 2–5 min | 1417 | 6 | 7% | 3% | -59% | -88% | -89% |
| 1–2 min | 1133 | 4 | 3% | 2% | -63% | -94% | -93% |
| Under 1 min | 1656 | 2 | 1% | 0% | -82% | -89% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 303 | 1 | 4% | 1% | -57% | -90% | -92% |
| ETH | 300 | 2 | 5% | 3% | -18% | -89% | -86% |
| NEAR | 298 | 0 | 5% | 1% | -100% | -88% | -91% |
| ZEC | 298 | 1 | 5% | 2% | -60% | -89% | -93% |
| XRP | 297 | 3 | 2% | 1% | +30% | -53% | -52% |
| HYPE | 297 | 1 | 4% | 3% | -59% | -90% | -89% |
| BNB | 297 | 0 | 4% | 1% | -100% | -91% | -95% |
| BTC | 296 | 0 | 7% | 3% | -100% | -84% | -87% |
| SOL | 294 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 224 | 0 | 4% | 1% | -100% | -90% | -93% |
| SILVER | 207 | 0 | 2% | 1% | -100% | -96% | -95% |
| WTI | 198 | 1 | 3% | 1% | -47% | -94% | -96% |
| COPPER | 181 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 168 | 1 | 4% | 2% | -44% | -93% | -91% |
| PLATINUM | 157 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 153 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 135 | 1 | 4% | 1% | -31% | -94% | -94% |
| EURUSD | 130 | 1 | 2% | 1% | -28% | -96% | -98% |
| USDJPY | 110 | 2 | 3% | 2% | +70% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2221 | 8 | 4% | 2% | -59% | -92% | -93% |
| DOWN (bought NO) | 2122 | 6 | 4% | 2% | -68% | -86% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 311 | 1 | 1% | 1% | -40% | -36% | -35% |
| 0.05–0.1% | 380 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 643 | 1 | 4% | 2% | -80% | -91% | -92% |
| 0.2–0.5% | 904 | 2 | 6% | 3% | -76% | -88% | -89% |
| Over 0.5% | 441 | 4 | 7% | 2% | -6% | -86% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1073 | 6 | 4% | 2% | -36% | -91% | -91% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,214 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 8:56:32 AM | BNB | UP | 3.5 min | -0.255% | — | In play | — |
| 10/1 8:55:43 AM | ZEC | UP | 4.3 min | -0.774% | — | In play | — |
| 10/1 8:55:43 AM | GBPUSD | UP | 4.3 min | — | — | In play | — |
| 10/1 8:44:49 AM | HYPE | UP | 10 sec | -0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:44:31 AM | COPPER | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:44:15 AM | XRP | UP | 45 sec | -0.195% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:44:15 AM | BTC | UP | 45 sec | -0.148% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:44:15 AM | DOGE | UP | 45 sec | -0.148% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:43:57 AM | ZEC | UP | 63 sec | -0.285% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:43:57 AM | WTI | DOWN | 63 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:43:41 AM | GOLD | DOWN | 79 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:43:41 AM | SOL | UP | 79 sec | -0.200% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:43:41 AM | EURUSD | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:43:10 AM | PALLADIUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:42:36 AM | ETH | UP | 2.4 min | -0.285% | 5¢ | ❌ Lost | -$0.15 |
| 10/1 8:42:05 AM | NEAR | UP | 2.9 min | -1.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:42:05 AM | BNB | UP | 2.9 min | -0.188% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:40:13 AM | SILVER | DOWN | 4.8 min | — | 11¢ | ❌ Lost | -$0.15 |
| 10/1 8:33:37 AM | USDJPY | UP | 11.4 min | — | 3¢ | ❌ Lost | -$0.15 |
| 10/1 8:29:29 AM | NATGAS | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:29:13 AM | BNB | DOWN | 47 sec | +0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:28:56 AM | PALLADIUM | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:28:40 AM | XRP | DOWN | 79 sec | +0.385% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:28:24 AM | HYPE | UP | 1.6 min | -0.436% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:27:17 AM | SOL | DOWN | 2.7 min | +0.379% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:27:17 AM | DOGE | DOWN | 2.7 min | +0.654% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:27:02 AM | GOLD | DOWN | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:27:02 AM | ETH | DOWN | 3.0 min | +0.421% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:27:02 AM | USDJPY | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:26:13 AM | BTC | DOWN | 3.8 min | +0.346% | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
