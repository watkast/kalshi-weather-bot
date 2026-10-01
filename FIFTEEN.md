# 15-Minute 1¢ Study

*Updated Thu Oct 1, 12:56 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 123 finished bets | 2% | $9.85 | +54% | +8.01¢ | $18.85 / -$9.00 |

*Expect about **39 buys a day** (~$5.81/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 233 | $2.50 | +10% |
| Volatility model ≥ 5%, sell at 25¢ | 229 | -$1.27 | -5% |
| Volatility model ≥ 5%, sell at 10¢ | 229 | -$2.03 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4060 | 4052 | 14 (0%) | 1.07% | -$299.90 (-60%) | Hold to the close: -$299.90 (-60%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 2321 | 3.4% | 0.3% (6) | -580% | ❌ Worse |
| Momentum model | 2321 | 3.4% | 0.3% (6) | -624% | ❌ Worse |
| Mean-reversion model | 2321 | 6.4% | 0.3% (6) | -744% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2321 | 6 | -68% | -84% | -86% | -83% |
| Volatility model ≥ 2% | 463 | 3 | -26% | -60% | -61% | -56% |
| Volatility model ≥ 5% | 229 | 1 | -44% | -24% | -24% | -19% |
| Volatility model ≥ 10% | 133 | 1 | +10% | +28% | +28% | +35% |
| Momentum model ≥ 2% | 408 | 2 | -41% | -54% | -58% | -54% |
| Momentum model ≥ 5% | 233 | 2 | +10% | -30% | -33% | -27% |
| Momentum model ≥ 10% | 153 | 1 | -5% | +6% | +9% | +13% |
| Mean-reversion model ≥ 2% | 870 | 3 | -63% | -85% | -87% | -83% |
| Mean-reversion model ≥ 5% | 574 | 3 | -44% | -83% | -84% | -77% |
| Mean-reversion model ≥ 10% | 366 | 2 | -39% | -77% | -81% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2517 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1194 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 341 | 3% | 2% | 1% | 1% | 1% | 1% |
| **All** | 4052 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$299.90 | -60% | — |
| Sell at 2¢ | 149 | 4% | -$443.16 | -89% | 47 sec |
| Sell at 3¢ | 90 | 2% | -$446.80 | -90% | 49 sec |
| Sell at 5¢ | 67 | 2% | -$438.35 | -88% | 66 sec |
| Sell at 10¢ | 48 | 1% | -$405.02 | -82% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$388.46 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$358.90 | -72% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 123 | 2 | 11% | 3% | +54% | -80% | -87% |
| 2–5 min | 1318 | 6 | 7% | 3% | -56% | -88% | -89% |
| 1–2 min | 1046 | 4 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 1565 | 2 | 1% | 0% | -81% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 285 | 1 | 4% | 1% | -55% | -92% | -91% |
| NEAR | 281 | 0 | 5% | 1% | -100% | -89% | -91% |
| ETH | 281 | 2 | 5% | 3% | -12% | -89% | -87% |
| ZEC | 280 | 1 | 5% | 2% | -58% | -88% | -93% |
| XRP | 279 | 3 | 2% | 1% | +37% | -50% | -49% |
| HYPE | 279 | 1 | 5% | 3% | -57% | -90% | -88% |
| BTC | 278 | 0 | 7% | 3% | -100% | -84% | -87% |
| BNB | 278 | 0 | 4% | 1% | -100% | -92% | -94% |
| SOL | 276 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 208 | 0 | 5% | 1% | -100% | -89% | -92% |
| SILVER | 191 | 0 | 2% | 1% | -100% | -97% | -97% |
| WTI | 184 | 1 | 3% | 1% | -43% | -94% | -95% |
| COPPER | 169 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 154 | 1 | 4% | 3% | -39% | -93% | -90% |
| PLATINUM | 147 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 141 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 121 | 1 | 4% | 2% | -23% | -93% | -94% |
| EURUSD | 118 | 1 | 3% | 1% | -21% | -96% | -98% |
| USDJPY | 102 | 2 | 2% | 2% | +83% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2068 | 8 | 4% | 2% | -56% | -92% | -92% |
| DOWN (bought NO) | 1984 | 6 | 4% | 2% | -65% | -86% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 293 | 1 | 1% | 1% | -36% | -31% | -30% |
| 0.05–0.1% | 355 | 0 | 2% | 0% | -100% | -95% | -97% |
| 0.1–0.2% | 605 | 1 | 4% | 2% | -78% | -90% | -92% |
| 0.2–0.5% | 850 | 2 | 6% | 3% | -74% | -88% | -89% |
| Over 0.5% | 413 | 4 | 7% | 3% | +0% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 938 | 2 | 4% | 2% | -76% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,294 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 12:56:18 AM | DOGE | DOWN | 3.7 min | +0.337% | — | In play | — |
| 10/1 12:55:29 AM | HYPE | DOWN | 4.5 min | +0.320% | — | In play | — |
| 10/1 12:44:52 AM | GBPUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:44:52 AM | COPPER | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:44:20 AM | NATGAS | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:44:04 AM | USDJPY | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:42:27 AM | ZEC | UP | 2.5 min | -0.299% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:42:11 AM | EURUSD | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:41:56 AM | XRP | UP | 3.0 min | -0.279% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:41:56 AM | HYPE | UP | 3.0 min | -0.527% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:41:38 AM | PLATINUM | UP | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:41:22 AM | NEAR | UP | 3.6 min | -0.765% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:41:22 AM | DOGE | UP | 3.6 min | -0.316% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:41:22 AM | GOLD | UP | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:41:06 AM | ETH | UP | 3.9 min | -0.292% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:40:52 AM | BNB | UP | 4.1 min | -0.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:40:35 AM | BTC | UP | 4.4 min | -0.240% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:40:19 AM | SOL | UP | 4.7 min | -0.327% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:40:03 AM | SILVER | UP | 5.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:39:48 AM | PALLADIUM | UP | 5.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:38:13 AM | WTI | DOWN | 6.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:29:59 AM | XRP | UP | 1 sec | +0.020% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:29:59 AM | DOGE | DOWN | 1 sec | +0.024% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:29:43 AM | GOLD | UP | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:29:43 AM | SOL | DOWN | 16 sec | +0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:29:27 AM | USDJPY | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:29:11 AM | ETH | DOWN | 48 sec | +0.039% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:29:11 AM | WTI | UP | 48 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:28:38 AM | NEAR | UP | 82 sec | -0.499% | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:28:38 AM | BTC | UP | 82 sec | -0.071% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
