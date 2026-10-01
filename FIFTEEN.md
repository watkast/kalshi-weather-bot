# 15-Minute 1¢ Study

*Updated Thu Oct 1, 9:48 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 139 finished bets | 1% | $7.60 | +37% | +5.47¢ | $17.65 / -$10.05 |

*Expect about **39 buys a day** (~$5.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 266 | -$1.25 | -4% |
| Volatility model ≥ 5%, sell at 25¢ | 256 | -$4.12 | -15% |
| Volatility model ≥ 5%, sell at 10¢ | 256 | -$4.88 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4419 | 4413 | 14 (0%) | 1.07% | -$345.65 (-64%) | Hold to the close: -$345.65 (-64%) |

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
| Volatility model | 2519 | 3.5% | 0.2% (6) | -655% | ❌ Worse |
| Momentum model | 2519 | 3.6% | 0.2% (6) | -706% | ❌ Worse |
| Mean-reversion model | 2519 | 6.5% | 0.2% (6) | -827% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2519 | 6 | -70% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 513 | 3 | -33% | -62% | -64% | -59% |
| Volatility model ≥ 5% | 256 | 1 | -50% | -31% | -32% | -27% |
| Volatility model ≥ 10% | 147 | 1 | +0% | +19% | +17% | +24% |
| Momentum model ≥ 2% | 457 | 2 | -48% | -58% | -62% | -58% |
| Momentum model ≥ 5% | 266 | 2 | -4% | -37% | -40% | -34% |
| Momentum model ≥ 10% | 176 | 1 | -19% | -8% | -8% | -4% |
| Mean-reversion model ≥ 2% | 944 | 3 | -66% | -85% | -88% | -83% |
| Mean-reversion model ≥ 5% | 622 | 3 | -48% | -82% | -85% | -78% |
| Mean-reversion model ≥ 10% | 396 | 2 | -44% | -77% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2715 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1312 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 386 | 4% | 2% | 2% | 2% | 1% | 1% |
| **All** | 4413 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$345.65 | -64% | — |
| Sell at 2¢ | 166 | 4% | -$484.49 | -89% | 46 sec |
| Sell at 3¢ | 98 | 2% | -$489.43 | -90% | 49 sec |
| Sell at 5¢ | 73 | 2% | -$480.20 | -89% | 66 sec |
| Sell at 10¢ | 52 | 1% | -$445.53 | -82% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$434.21 | -80% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$404.65 | -75% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 136 | 2 | 13% | 3% | +40% | -77% | -88% |
| 2–5 min | 1448 | 6 | 7% | 3% | -60% | -88% | -89% |
| 1–2 min | 1153 | 4 | 3% | 2% | -63% | -94% | -93% |
| Under 1 min | 1673 | 2 | 1% | 0% | -83% | -89% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 307 | 1 | 4% | 1% | -58% | -90% | -92% |
| ETH | 304 | 2 | 5% | 3% | -19% | -89% | -86% |
| ZEC | 302 | 1 | 5% | 2% | -61% | -89% | -93% |
| NEAR | 301 | 0 | 5% | 1% | -100% | -88% | -91% |
| XRP | 301 | 3 | 2% | 1% | +28% | -53% | -52% |
| HYPE | 301 | 1 | 5% | 3% | -60% | -90% | -88% |
| BNB | 301 | 0 | 4% | 1% | -100% | -91% | -95% |
| BTC | 300 | 0 | 7% | 3% | -100% | -84% | -87% |
| SOL | 298 | 0 | 3% | 1% | -100% | -92% | -91% |
| GOLD | 227 | 0 | 4% | 1% | -100% | -90% | -93% |
| SILVER | 211 | 0 | 2% | 1% | -100% | -96% | -95% |
| WTI | 199 | 1 | 3% | 1% | -48% | -94% | -96% |
| COPPER | 185 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 172 | 1 | 4% | 2% | -46% | -93% | -91% |
| PLATINUM | 161 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 157 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 139 | 1 | 5% | 2% | -33% | -91% | -93% |
| EURUSD | 134 | 1 | 3% | 1% | -30% | -95% | -96% |
| USDJPY | 113 | 2 | 3% | 2% | +65% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2266 | 8 | 4% | 2% | -60% | -92% | -92% |
| DOWN (bought NO) | 2147 | 6 | 4% | 2% | -68% | -87% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 314 | 1 | 1% | 1% | -40% | -36% | -35% |
| 0.05–0.1% | 384 | 0 | 2% | 0% | -100% | -94% | -96% |
| 0.1–0.2% | 649 | 1 | 4% | 2% | -80% | -91% | -92% |
| 0.2–0.5% | 920 | 2 | 6% | 3% | -76% | -88% | -89% |
| Over 0.5% | 447 | 4 | 7% | 2% | -7% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1143 | 6 | 4% | 2% | -40% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,201 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 9:44:15 AM | SILVER | UP | 44 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:43:58 AM | PALLADIUM | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:43:42 AM | PLATINUM | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:43:11 AM | NATGAS | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:42:22 AM | XRP | UP | 2.6 min | -0.457% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:42:05 AM | HYPE | UP | 2.9 min | -0.437% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:42:05 AM | DOGE | UP | 2.9 min | -0.593% | 0¢ | ❌ Lost | $0.00 |
| 10/1 9:42:05 AM | BTC | UP | 2.9 min | -0.264% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:42:05 AM | SOL | UP | 2.9 min | -0.418% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:42:05 AM | ZEC | UP | 2.9 min | -0.550% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:42:05 AM | COPPER | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:41:01 AM | ETH | UP | 4.0 min | -0.408% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:41:01 AM | BNB | UP | 4.0 min | -0.270% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:34:43 AM | GBPUSD | UP | 10.3 min | — | 11¢ | ❌ Lost | -$0.15 |
| 10/1 9:34:28 AM | EURUSD | UP | 10.5 min | — | 22¢ | ❌ Lost | -$0.15 |
| 10/1 9:29:43 AM | HYPE | UP | 17 sec | -0.052% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:29:43 AM | EURUSD | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:29:43 AM | SILVER | DOWN | 17 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:29:43 AM | GBPUSD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:29:12 AM | NEAR | DOWN | 47 sec | +0.156% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:28:40 AM | ZEC | DOWN | 79 sec | +0.191% | 2¢ | ❌ Lost | -$0.15 |
| 10/1 9:28:24 AM | ETH | DOWN | 1.6 min | +0.097% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:28:24 AM | USDJPY | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:28:08 AM | NATGAS | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:28:08 AM | PALLADIUM | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:27:48 AM | BTC | DOWN | 2.2 min | +0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 9:27:48 AM | XRP | DOWN | 2.2 min | +0.330% | 0¢ | ❌ Lost | $0.00 |
| 10/1 9:27:48 AM | PLATINUM | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:27:48 AM | SOL | DOWN | 2.2 min | +0.243% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 9:27:48 AM | COPPER | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
