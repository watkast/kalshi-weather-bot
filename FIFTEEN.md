# 15-Minute 1¢ Study

*Updated Thu Oct 1, 11:50 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 142 finished bets | 1% | $7.15 | +34% | +5.04¢ | $17.35 / -$10.20 |

*Expect about **39 buys a day** (~$5.86/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 276 | -$2.45 | -8% |
| Volatility model ≥ 5%, sell at 25¢ | 266 | -$5.47 | -19% |
| Volatility model ≥ 5%, sell at 10¢ | 266 | -$6.23 | -21% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4542 | 4536 | 15 (0%) | 1.07% | -$347.10 (-62%) | Hold to the close: -$347.10 (-62%) |

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
| Volatility model | 2588 | 3.6% | 0.2% (6) | -674% | ❌ Worse |
| Momentum model | 2588 | 3.7% | 0.2% (6) | -731% | ❌ Worse |
| Mean-reversion model | 2588 | 6.6% | 0.2% (6) | -859% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2588 | 6 | -71% | -85% | -87% | -84% |
| Volatility model ≥ 2% | 528 | 3 | -35% | -63% | -65% | -61% |
| Volatility model ≥ 5% | 266 | 1 | -52% | -34% | -35% | -30% |
| Volatility model ≥ 10% | 152 | 1 | -4% | +14% | +12% | +19% |
| Momentum model ≥ 2% | 472 | 2 | -50% | -59% | -63% | -60% |
| Momentum model ≥ 5% | 276 | 2 | -8% | -40% | -42% | -37% |
| Momentum model ≥ 10% | 184 | 1 | -23% | -13% | -12% | -9% |
| Mean-reversion model ≥ 2% | 976 | 3 | -67% | -86% | -88% | -84% |
| Mean-reversion model ≥ 5% | 647 | 3 | -50% | -83% | -85% | -78% |
| Mean-reversion model ≥ 10% | 411 | 2 | -46% | -78% | -81% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2784 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1349 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 403 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 4536 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 15 | 0% | -$347.10 | -62% | — |
| Sell at 2¢ | 168 | 4% | -$499.42 | -90% | 46 sec |
| Sell at 3¢ | 100 | 2% | -$504.10 | -90% | 50 sec |
| Sell at 5¢ | 74 | 2% | -$495.00 | -89% | 66 sec |
| Sell at 10¢ | 53 | 1% | -$459.67 | -83% | 81 sec |
| Sell at 25¢ | 24 | 1% | -$435.66 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$406.10 | -73% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 139 | 2 | 13% | 3% | +37% | -77% | -89% |
| 2–5 min | 1502 | 7 | 7% | 3% | -55% | -88% | -89% |
| 1–2 min | 1174 | 4 | 3% | 2% | -64% | -94% | -93% |
| Under 1 min | 1718 | 2 | 1% | 0% | -83% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 315 | 1 | 4% | 1% | -59% | -90% | -92% |
| ETH | 312 | 2 | 5% | 3% | -21% | -89% | -87% |
| NEAR | 309 | 0 | 5% | 1% | -100% | -88% | -92% |
| ZEC | 309 | 1 | 5% | 2% | -61% | -89% | -94% |
| HYPE | 309 | 1 | 5% | 3% | -61% | -90% | -88% |
| BNB | 309 | 0 | 4% | 1% | -100% | -92% | -95% |
| BTC | 308 | 0 | 7% | 3% | -100% | -84% | -88% |
| XRP | 307 | 3 | 2% | 1% | +26% | -54% | -53% |
| SOL | 306 | 0 | 3% | 1% | -100% | -92% | -91% |
| GOLD | 232 | 0 | 4% | 1% | -100% | -90% | -93% |
| SILVER | 216 | 0 | 2% | 1% | -100% | -96% | -95% |
| WTI | 205 | 1 | 3% | 1% | -49% | -94% | -96% |
| COPPER | 191 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 176 | 1 | 4% | 2% | -47% | -93% | -91% |
| PLATINUM | 167 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 162 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 144 | 1 | 5% | 2% | -35% | -92% | -93% |
| EURUSD | 140 | 1 | 4% | 1% | -33% | -94% | -94% |
| USDJPY | 119 | 3 | 3% | 3% | +135% | -94% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2313 | 9 | 4% | 2% | -56% | -92% | -92% |
| DOWN (bought NO) | 2223 | 6 | 4% | 1% | -69% | -87% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 322 | 1 | 1% | 1% | -43% | -38% | -38% |
| 0.05–0.1% | 389 | 0 | 2% | 0% | -100% | -94% | -96% |
| 0.1–0.2% | 662 | 1 | 4% | 2% | -80% | -91% | -92% |
| 0.2–0.5% | 948 | 2 | 6% | 3% | -77% | -89% | -89% |
| Over 0.5% | 462 | 4 | 7% | 2% | -10% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1266 | 7 | 4% | 2% | -37% | -91% | -91% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,194 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 11:44:48 AM | HYPE | DOWN | 11 sec | -0.009% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:44:32 AM | ETH | DOWN | 27 sec | +0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/1 11:44:32 AM | SILVER | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:44:32 AM | WTI | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:44:16 AM | COPPER | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:44:16 AM | GOLD | DOWN | 44 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:44:16 AM | XRP | DOWN | 44 sec | +0.140% | 0¢ | ❌ Lost | $0.00 |
| 10/1 11:44:16 AM | BNB | UP | 44 sec | -0.085% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:43:59 AM | DOGE | DOWN | 60 sec | +0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/1 11:43:59 AM | PALLADIUM | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:43:59 AM | PLATINUM | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:43:43 AM | EURUSD | DOWN | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:43:43 AM | SOL | DOWN | 76 sec | +0.186% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:43:11 AM | BTC | DOWN | 1.8 min | +0.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:42:36 AM | ZEC | DOWN | 2.4 min | +0.393% | 0¢ | ❌ Lost | $0.00 |
| 10/1 11:41:32 AM | NEAR | DOWN | 3.5 min | +0.974% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
