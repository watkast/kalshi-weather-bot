# 15-Minute 1¢ Study

*Updated Thu Oct 1, 11:40 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 142 finished bets | 1% | $7.15 | +34% | +5.04¢ | $17.35 / -$10.20 |

*Expect about **39 buys a day** (~$5.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 274 | -$2.30 | -8% |
| Volatility model ≥ 5%, sell at 25¢ | 265 | -$5.32 | -18% |
| Volatility model ≥ 5%, sell at 10¢ | 265 | -$6.08 | -21% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4526 | 4520 | 15 (0%) | 1.07% | -$345.30 (-62%) | Hold to the close: -$345.30 (-62%) |

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
| Volatility model | 2579 | 3.5% | 0.2% (6) | -669% | ❌ Worse |
| Momentum model | 2579 | 3.7% | 0.2% (6) | -730% | ❌ Worse |
| Mean-reversion model | 2579 | 6.6% | 0.2% (6) | -845% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2579 | 6 | -71% | -85% | -86% | -84% |
| Volatility model ≥ 2% | 525 | 3 | -35% | -63% | -65% | -60% |
| Volatility model ≥ 5% | 265 | 1 | -52% | -33% | -35% | -30% |
| Volatility model ≥ 10% | 151 | 1 | -3% | +15% | +13% | +20% |
| Momentum model ≥ 2% | 470 | 2 | -50% | -59% | -63% | -60% |
| Momentum model ≥ 5% | 274 | 2 | -8% | -39% | -42% | -37% |
| Momentum model ≥ 10% | 182 | 1 | -22% | -12% | -11% | -8% |
| Mean-reversion model ≥ 2% | 971 | 3 | -67% | -86% | -88% | -84% |
| Mean-reversion model ≥ 5% | 643 | 3 | -50% | -83% | -85% | -78% |
| Mean-reversion model ≥ 10% | 410 | 2 | -46% | -78% | -81% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2775 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1343 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 402 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 4520 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 15 | 0% | -$345.30 | -62% | — |
| Sell at 2¢ | 168 | 4% | -$497.62 | -90% | 46 sec |
| Sell at 3¢ | 100 | 2% | -$502.30 | -90% | 50 sec |
| Sell at 5¢ | 74 | 2% | -$493.20 | -89% | 66 sec |
| Sell at 10¢ | 53 | 1% | -$457.87 | -82% | 81 sec |
| Sell at 25¢ | 24 | 1% | -$433.86 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$404.30 | -73% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 139 | 2 | 13% | 3% | +37% | -77% | -89% |
| 2–5 min | 1500 | 7 | 7% | 3% | -55% | -88% | -89% |
| 1–2 min | 1168 | 4 | 3% | 2% | -64% | -94% | -93% |
| Under 1 min | 1710 | 2 | 1% | 0% | -83% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 314 | 1 | 4% | 1% | -59% | -90% | -92% |
| ETH | 311 | 2 | 5% | 3% | -21% | -89% | -87% |
| NEAR | 308 | 0 | 5% | 1% | -100% | -88% | -92% |
| ZEC | 308 | 1 | 5% | 2% | -61% | -89% | -94% |
| HYPE | 308 | 1 | 5% | 3% | -61% | -90% | -88% |
| BNB | 308 | 0 | 4% | 1% | -100% | -92% | -95% |
| BTC | 307 | 0 | 7% | 3% | -100% | -84% | -87% |
| XRP | 306 | 3 | 2% | 1% | +26% | -54% | -53% |
| SOL | 305 | 0 | 3% | 1% | -100% | -92% | -91% |
| GOLD | 231 | 0 | 4% | 1% | -100% | -90% | -93% |
| SILVER | 215 | 0 | 2% | 1% | -100% | -96% | -95% |
| WTI | 204 | 1 | 3% | 1% | -49% | -94% | -96% |
| COPPER | 190 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 176 | 1 | 4% | 2% | -47% | -93% | -91% |
| PLATINUM | 166 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 161 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 144 | 1 | 5% | 2% | -35% | -92% | -93% |
| EURUSD | 139 | 1 | 4% | 1% | -33% | -94% | -94% |
| USDJPY | 119 | 3 | 3% | 3% | +135% | -94% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2312 | 9 | 4% | 2% | -55% | -92% | -92% |
| DOWN (bought NO) | 2208 | 6 | 4% | 1% | -69% | -87% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 321 | 1 | 1% | 1% | -42% | -38% | -38% |
| 0.05–0.1% | 388 | 0 | 2% | 0% | -100% | -94% | -96% |
| 0.1–0.2% | 657 | 1 | 4% | 2% | -80% | -91% | -92% |
| 0.2–0.5% | 947 | 2 | 6% | 3% | -77% | -89% | -89% |
| Over 0.5% | 461 | 4 | 7% | 2% | -10% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1250 | 7 | 4% | 2% | -37% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,198 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 11:27:52 AM | COPPER | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:27:20 AM | USDJPY | UP | 2.7 min | — | 12¢ | ✅ Won | $13.85 |
| 10/1 11:27:20 AM | PLATINUM | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:26:31 AM | ZEC | DOWN | 3.5 min | +0.633% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:26:31 AM | PALLADIUM | DOWN | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:25:59 AM | XRP | DOWN | 4.0 min | +0.530% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:25:26 AM | BNB | DOWN | 4.5 min | +0.278% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:25:26 AM | EURUSD | DOWN | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:25:10 AM | ETH | DOWN | 4.8 min | +0.371% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:25:10 AM | BTC | DOWN | 4.8 min | +0.392% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:25:10 AM | DOGE | DOWN | 4.8 min | +0.624% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:25:10 AM | GBPUSD | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:25:10 AM | NEAR | DOWN | 4.8 min | +1.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:25:10 AM | HYPE | DOWN | 4.8 min | +0.576% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:24:54 AM | SOL | DOWN | 5.1 min | +0.555% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:24:54 AM | WTI | UP | 5.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:14:50 AM | NATGAS | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:14:34 AM | NEAR | UP | 26 sec | -0.217% | 0¢ | ❌ Lost | $0.00 |
| 10/1 11:13:29 AM | USDJPY | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:13:12 AM | ZEC | DOWN | 1.8 min | +0.435% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:13:12 AM | PLATINUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:12:23 AM | COPPER | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:12:07 AM | GOLD | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:11:32 AM | XRP | DOWN | 3.5 min | +0.425% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:11:32 AM | DOGE | DOWN | 3.5 min | +0.439% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:11:32 AM | PALLADIUM | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:11:01 AM | ETH | DOWN | 4.0 min | +0.311% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:10:44 AM | SILVER | DOWN | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:10:44 AM | SOL | DOWN | 4.2 min | +0.394% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:10:28 AM | BTC | DOWN | 4.5 min | +0.296% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
