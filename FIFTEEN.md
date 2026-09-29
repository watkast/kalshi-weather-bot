# 15-Minute 1¢ Study

*Updated Tue Sep 29, 7:26 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 65 finished bets | 3% | $18.25 | +187% | +28.08¢ | $23.20 / -$4.95 |

*Expect about **46 buys a day** (~$6.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 239 | $10.95 | +35% |
| 5+ min left, sell at 50¢ | 65 | $3.75 | +38% |
| Volatility model ≥ 5%, sell at 25¢ | 86 | $0.93 | +10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1872 | 1865 | 8 (0%) | 1.07% | -$112.85 (-50%) | Hold to the close: -$112.85 (-50%) |

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
| Volatility model | 983 | 2.8% | 0.4% (4) | -407% | ❌ Worse |
| Momentum model | 983 | 2.9% | 0.4% (4) | -473% | ❌ Worse |
| Mean-reversion model | 983 | 6.0% | 0.4% (4) | -499% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 983 | 4 | -48% | -90% | -92% | -88% |
| Volatility model ≥ 2% | 192 | 1 | -39% | -86% | -88% | -83% |
| Volatility model ≥ 5% | 86 | 0 | -100% | -74% | -74% | -64% |
| Volatility model ≥ 10% | 45 | 0 | -100% | -74% | -71% | -52% |
| Momentum model ≥ 2% | 156 | 0 | -100% | -87% | -91% | -89% |
| Momentum model ≥ 5% | 90 | 0 | -100% | -84% | -92% | -87% |
| Momentum model ≥ 10% | 57 | 0 | -100% | -90% | -85% | -75% |
| Mean-reversion model ≥ 2% | 367 | 3 | -12% | -86% | -88% | -82% |
| Mean-reversion model ≥ 5% | 239 | 3 | +35% | -84% | -85% | -77% |
| Mean-reversion model ≥ 10% | 152 | 2 | +48% | -79% | -81% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1178 | 4% | 2% | 2% | 2% | 1% | 1% |
| Commodities | 576 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 111 | 4% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1865 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$112.85 | -50% | — |
| Sell at 2¢ | 61 | 3% | -$208.99 | -93% | 47 sec |
| Sell at 3¢ | 35 | 2% | -$211.20 | -94% | 47 sec |
| Sell at 5¢ | 25 | 1% | -$208.60 | -93% | 81 sec |
| Sell at 10¢ | 23 | 1% | -$194.72 | -87% | 1.9 min |
| Sell at 25¢ | 13 | 1% | -$181.82 | -81% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$164.10 | -73% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 65 | 2 | 9% | 3% | +187% | -84% | -88% |
| 2–5 min | 623 | 5 | 6% | 3% | -22% | -89% | -90% |
| 1–2 min | 514 | 1 | 2% | 1% | -79% | -96% | -96% |
| Under 1 min | 663 | 0 | 1% | 0% | -100% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 134 | 2 | 4% | 3% | +87% | -90% | -87% |
| ZEC | 133 | 1 | 5% | 2% | -8% | -88% | -95% |
| DOGE | 132 | 1 | 5% | 2% | -5% | -89% | -87% |
| XRP | 132 | 2 | 3% | 2% | +92% | -93% | -92% |
| NEAR | 131 | 0 | 5% | 2% | -100% | -88% | -94% |
| BTC | 131 | 0 | 8% | 2% | -100% | -81% | -89% |
| SOL | 130 | 0 | 2% | 2% | -100% | -94% | -91% |
| BNB | 128 | 0 | 2% | 1% | -100% | -95% | -95% |
| HYPE | 127 | 0 | 2% | 2% | -100% | -95% | -95% |
| GOLD | 99 | 0 | 2% | 0% | -100% | -96% | -100% |
| WTI | 91 | 0 | 1% | 0% | -100% | -98% | -100% |
| SILVER | 91 | 0 | 2% | 0% | -100% | -95% | -96% |
| COPPER | 83 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 78 | 0 | 4% | 1% | -100% | -93% | -90% |
| PLATINUM | 73 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 61 | 0 | 2% | 0% | -100% | -97% | -100% |
| GBPUSD | 42 | 0 | 2% | 0% | -100% | -96% | -94% |
| USDJPY | 35 | 2 | 6% | 6% | +433% | -90% | -85% |
| EURUSD | 34 | 0 | 3% | 0% | -100% | -95% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 980 | 5 | 4% | 2% | -40% | -92% | -92% |
| DOWN (bought NO) | 885 | 3 | 3% | 1% | -61% | -94% | -96% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 118 | 0 | 3% | 2% | -100% | -91% | -91% |
| 0.05–0.1% | 141 | 0 | 1% | 0% | -100% | -98% | -100% |
| 0.1–0.2% | 275 | 0 | 4% | 1% | -100% | -90% | -91% |
| 0.2–0.5% | 447 | 2 | 4% | 2% | -51% | -91% | -92% |
| Over 0.5% | 197 | 4 | 7% | 4% | +113% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 369 | 4 | 3% | 1% | +26% | -94% | -95% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,752 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 7:24:39 AM | PALLADIUM | UP | 5.3 min | — | — | In play | — |
| 9/29 7:14:54 AM | PLATINUM | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:14:54 AM | SILVER | DOWN | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:14:38 AM | XRP | UP | 21 sec | -0.090% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:14:22 AM | SOL | DOWN | 37 sec | +0.116% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:14:22 AM | BNB | DOWN | 37 sec | +0.004% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:14:08 AM | DOGE | DOWN | 52 sec | +0.144% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:13:34 AM | ZEC | DOWN | 86 sec | +0.276% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:13:18 AM | BTC | DOWN | 1.7 min | +0.083% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:13:18 AM | WTI | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:13:03 AM | GOLD | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:13:03 AM | NEAR | UP | 1.9 min | -0.484% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:13:03 AM | GBPUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:10:37 AM | PALLADIUM | DOWN | 4.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:10:05 AM | HYPE | DOWN | 4.9 min | +0.618% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:59:55 AM | GBPUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:59:37 AM | WTI | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:59:21 AM | BTC | UP | 39 sec | -0.038% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:59:21 AM | SOL | DOWN | 39 sec | +0.167% | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:59:21 AM | ZEC | DOWN | 39 sec | +0.144% | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:59:05 AM | BNB | UP | 55 sec | -0.087% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:59:05 AM | SILVER | UP | 55 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 9/29 6:58:50 AM | XRP | UP | 69 sec | -0.322% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:58:50 AM | EURUSD | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:58:50 AM | ETH | UP | 69 sec | -0.134% | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:58:50 AM | DOGE | UP | 69 sec | -0.217% | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:58:17 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:57:45 AM | PALLADIUM | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:57:45 AM | USDJPY | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:57:45 AM | GOLD | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
