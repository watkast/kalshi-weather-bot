# 15-Minute 1¢ Study

*Updated Thu Oct 1, 12:36 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 121 finished bets | 2% | $10.15 | +57% | +8.39¢ | $19.00 / -$8.85 |

*Expect about **38 buys a day** (~$5.74/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 232 | $2.65 | +10% |
| Volatility model ≥ 5%, sell at 25¢ | 229 | -$1.27 | -5% |
| Volatility model ≥ 5%, sell at 10¢ | 229 | -$2.03 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4039 | 4033 | 14 (0%) | 1.07% | -$297.05 (-60%) | Hold to the close: -$297.05 (-60%) |

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
| Volatility model | 2312 | 3.4% | 0.3% (6) | -581% | ❌ Worse |
| Momentum model | 2312 | 3.5% | 0.3% (6) | -625% | ❌ Worse |
| Mean-reversion model | 2312 | 6.5% | 0.3% (6) | -745% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2312 | 6 | -67% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 462 | 3 | -26% | -60% | -61% | -56% |
| Volatility model ≥ 5% | 229 | 1 | -44% | -24% | -24% | -19% |
| Volatility model ≥ 10% | 133 | 1 | +10% | +28% | +28% | +35% |
| Momentum model ≥ 2% | 407 | 2 | -41% | -54% | -58% | -54% |
| Momentum model ≥ 5% | 232 | 2 | +10% | -29% | -32% | -27% |
| Momentum model ≥ 10% | 153 | 1 | -5% | +6% | +9% | +13% |
| Mean-reversion model ≥ 2% | 869 | 3 | -63% | -85% | -87% | -83% |
| Mean-reversion model ≥ 5% | 573 | 3 | -44% | -83% | -84% | -77% |
| Mean-reversion model ≥ 10% | 366 | 2 | -39% | -77% | -81% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2508 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1187 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 338 | 3% | 2% | 1% | 1% | 1% | 1% |
| **All** | 4033 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$297.05 | -60% | — |
| Sell at 2¢ | 149 | 4% | -$440.31 | -89% | 47 sec |
| Sell at 3¢ | 90 | 2% | -$443.95 | -90% | 49 sec |
| Sell at 5¢ | 67 | 2% | -$435.50 | -88% | 66 sec |
| Sell at 10¢ | 48 | 1% | -$402.17 | -82% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$385.61 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$356.05 | -72% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 121 | 2 | 12% | 3% | +57% | -80% | -87% |
| 2–5 min | 1305 | 6 | 7% | 3% | -55% | -88% | -89% |
| 1–2 min | 1046 | 4 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 1561 | 2 | 1% | 0% | -81% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 284 | 1 | 4% | 1% | -54% | -92% | -91% |
| NEAR | 280 | 0 | 5% | 1% | -100% | -89% | -91% |
| ETH | 280 | 2 | 5% | 3% | -12% | -88% | -86% |
| ZEC | 279 | 1 | 5% | 2% | -57% | -88% | -93% |
| XRP | 278 | 3 | 2% | 1% | +38% | -50% | -49% |
| HYPE | 278 | 1 | 5% | 3% | -56% | -89% | -88% |
| BTC | 277 | 0 | 7% | 3% | -100% | -84% | -87% |
| BNB | 277 | 0 | 4% | 1% | -100% | -91% | -94% |
| SOL | 275 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 207 | 0 | 5% | 1% | -100% | -89% | -92% |
| SILVER | 190 | 0 | 2% | 1% | -100% | -97% | -97% |
| WTI | 183 | 1 | 3% | 1% | -42% | -94% | -95% |
| COPPER | 168 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 153 | 1 | 4% | 3% | -39% | -93% | -90% |
| PLATINUM | 146 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 140 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 120 | 1 | 4% | 2% | -22% | -93% | -94% |
| EURUSD | 117 | 1 | 3% | 1% | -20% | -96% | -98% |
| USDJPY | 101 | 2 | 2% | 2% | +85% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2052 | 8 | 4% | 2% | -55% | -92% | -92% |
| DOWN (bought NO) | 1981 | 6 | 4% | 2% | -65% | -86% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 293 | 1 | 1% | 1% | -36% | -31% | -30% |
| 0.05–0.1% | 355 | 0 | 2% | 0% | -100% | -95% | -97% |
| 0.1–0.2% | 605 | 1 | 4% | 2% | -78% | -90% | -92% |
| 0.2–0.5% | 843 | 2 | 6% | 3% | -74% | -88% | -89% |
| Over 0.5% | 411 | 4 | 7% | 3% | +1% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 919 | 2 | 4% | 2% | -75% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,285 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 12:29:59 AM | XRP | UP | 1 sec | +0.020% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:29:59 AM | DOGE | DOWN | 1 sec | +0.024% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:29:43 AM | GOLD | UP | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:29:43 AM | SOL | DOWN | 16 sec | +0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:29:27 AM | USDJPY | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:29:11 AM | ETH | DOWN | 48 sec | +0.039% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:29:11 AM | WTI | UP | 48 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:28:38 AM | NEAR | UP | 82 sec | -0.499% | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:28:38 AM | BTC | UP | 82 sec | -0.071% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:28:38 AM | HYPE | DOWN | 82 sec | +0.191% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:28:22 AM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:28:22 AM | BNB | DOWN | 1.6 min | +0.032% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:28:22 AM | SILVER | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:28:06 AM | GBPUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:27:18 AM | COPPER | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:26:32 AM | PLATINUM | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:25:12 AM | ZEC | DOWN | 4.8 min | +0.637% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:25:12 AM | PALLADIUM | UP | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:14:45 AM | XRP | UP | 15 sec | -0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:14:29 AM | DOGE | DOWN | 31 sec | +0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:13:57 AM | ETH | DOWN | 63 sec | +0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:13:41 AM | ZEC | UP | 79 sec | -0.218% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:13:41 AM | GOLD | DOWN | 79 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:13:25 AM | NEAR | DOWN | 1.6 min | +0.312% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:13:09 AM | SOL | DOWN | 1.9 min | +0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 12:13:09 AM | HYPE | DOWN | 1.9 min | +0.190% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:12:37 AM | PLATINUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:12:21 AM | USDJPY | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:12:05 AM | EURUSD | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:12:05 AM | BTC | DOWN | 2.9 min | +0.079% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
