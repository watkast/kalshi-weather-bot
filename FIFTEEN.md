# 15-Minute 1¢ Study

*Updated Tue Sep 29, 7:05 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 65 finished bets | 3% | $18.25 | +187% | +28.08¢ | $23.20 / -$4.95 |

*Expect about **45 buys a day** (~$6.80/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 235 | $11.55 | +38% |
| 5+ min left, sell at 50¢ | 65 | $3.75 | +38% |
| Volatility model ≥ 5%, sell at 25¢ | 85 | $1.08 | +12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1857 | 1851 | 8 (0%) | 1.07% | -$111.35 (-50%) | Hold to the close: -$111.35 (-50%) |

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
| Volatility model | 975 | 2.8% | 0.4% (4) | -406% | ❌ Worse |
| Momentum model | 975 | 2.9% | 0.4% (4) | -475% | ❌ Worse |
| Mean-reversion model | 975 | 5.9% | 0.4% (4) | -493% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 975 | 4 | -47% | -90% | -92% | -88% |
| Volatility model ≥ 2% | 190 | 1 | -39% | -86% | -88% | -83% |
| Volatility model ≥ 5% | 85 | 0 | -100% | -74% | -74% | -63% |
| Volatility model ≥ 10% | 44 | 0 | -100% | -73% | -70% | -50% |
| Momentum model ≥ 2% | 155 | 0 | -100% | -87% | -91% | -89% |
| Momentum model ≥ 5% | 89 | 0 | -100% | -84% | -92% | -86% |
| Momentum model ≥ 10% | 57 | 0 | -100% | -90% | -85% | -75% |
| Mean-reversion model ≥ 2% | 363 | 3 | -11% | -86% | -88% | -82% |
| Mean-reversion model ≥ 5% | 235 | 3 | +38% | -84% | -85% | -77% |
| Mean-reversion model ≥ 10% | 149 | 2 | +52% | -79% | -81% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1170 | 4% | 2% | 2% | 2% | 1% | 1% |
| Commodities | 571 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 110 | 4% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1851 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$111.35 | -50% | — |
| Sell at 2¢ | 61 | 3% | -$207.49 | -93% | 47 sec |
| Sell at 3¢ | 35 | 2% | -$209.70 | -94% | 47 sec |
| Sell at 5¢ | 25 | 1% | -$207.10 | -93% | 81 sec |
| Sell at 10¢ | 23 | 1% | -$193.22 | -87% | 1.9 min |
| Sell at 25¢ | 13 | 1% | -$180.32 | -81% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$162.60 | -73% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 65 | 2 | 9% | 3% | +187% | -84% | -88% |
| 2–5 min | 621 | 5 | 6% | 3% | -22% | -89% | -90% |
| 1–2 min | 508 | 1 | 2% | 1% | -79% | -96% | -96% |
| Under 1 min | 657 | 0 | 1% | 0% | -100% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 134 | 2 | 4% | 3% | +87% | -90% | -87% |
| ZEC | 132 | 1 | 5% | 2% | -7% | -88% | -95% |
| DOGE | 131 | 1 | 5% | 2% | -5% | -89% | -87% |
| XRP | 131 | 2 | 3% | 2% | +92% | -93% | -92% |
| NEAR | 130 | 0 | 5% | 2% | -100% | -88% | -94% |
| BTC | 130 | 0 | 8% | 2% | -100% | -81% | -89% |
| SOL | 129 | 0 | 2% | 2% | -100% | -94% | -91% |
| BNB | 127 | 0 | 2% | 1% | -100% | -95% | -95% |
| HYPE | 126 | 0 | 2% | 2% | -100% | -95% | -95% |
| GOLD | 98 | 0 | 2% | 0% | -100% | -96% | -100% |
| WTI | 90 | 0 | 1% | 0% | -100% | -98% | -100% |
| SILVER | 90 | 0 | 2% | 0% | -100% | -95% | -96% |
| COPPER | 83 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 78 | 0 | 4% | 1% | -100% | -93% | -90% |
| PLATINUM | 72 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 60 | 0 | 2% | 0% | -100% | -97% | -100% |
| GBPUSD | 41 | 0 | 2% | 0% | -100% | -96% | -94% |
| USDJPY | 35 | 2 | 6% | 6% | +433% | -90% | -85% |
| EURUSD | 34 | 0 | 3% | 0% | -100% | -95% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 977 | 5 | 4% | 2% | -40% | -92% | -92% |
| DOWN (bought NO) | 874 | 3 | 3% | 1% | -60% | -94% | -96% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 117 | 0 | 3% | 2% | -100% | -90% | -90% |
| 0.05–0.1% | 139 | 0 | 1% | 0% | -100% | -98% | -100% |
| 0.1–0.2% | 273 | 0 | 4% | 1% | -100% | -90% | -91% |
| 0.2–0.5% | 445 | 2 | 4% | 2% | -50% | -91% | -92% |
| Over 0.5% | 196 | 4 | 7% | 4% | +115% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 355 | 4 | 3% | 1% | +31% | -94% | -95% |
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
| 9/29 6:57:45 AM | HYPE | UP | 2.2 min | -0.354% | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:56:25 AM | NATGAS | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:59:52 AM | ZEC | DOWN | 7 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:59:36 AM | COPPER | DOWN | 23 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:59:20 AM | BTC | DOWN | 39 sec | +0.019% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:59:04 AM | DOGE | DOWN | 56 sec | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:58:31 AM | GOLD | DOWN | 88 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:58:31 AM | ETH | DOWN | 88 sec | +0.121% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:58:31 AM | NATGAS | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:58:15 AM | SOL | DOWN | 1.7 min | +0.111% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:57:27 AM | WTI | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:57:11 AM | BNB | DOWN | 2.8 min | +0.054% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:57:11 AM | USDJPY | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:56:54 AM | HYPE | DOWN | 3.1 min | +0.213% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:56:20 AM | XRP | DOWN | 3.6 min | +0.326% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
