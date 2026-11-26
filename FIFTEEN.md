# 15-Minute 1¢ Study

*Updated Thu Nov 26, 6:17 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4940 finished bets | 1% | $204.40 | +38% | +4.14¢ | $84.70 / $119.70 |

*Expect about **83 buys a day** (~$12.50/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4682 | $104.00 | +21% |
| Volatility model ≥ 2%, hold to the close | 9201 | $39.15 | +4% |
| Momentum model ≥ 2%, hold to the close | 7658 | -$42.20 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 68357 | 68323 | 257 (0%) | 1.07% | -$4,674.20 (-57%) | Hold to the close: -$4,674.20 (-57%) |

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
| Volatility model | 40409 | 4.5% | 0.4% (165) | -652% | ❌ Worse |
| Momentum model | 40409 | 4.4% | 0.4% (165) | -676% | ❌ Worse |
| Mean-reversion model | 40409 | 7.9% | 0.4% (165) | -792% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40409 | 165 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9201 | 81 | +4% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 4940 | 53 | +38% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2860 | 32 | +66% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 7658 | 59 | -5% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4682 | 43 | +21% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3052 | 28 | +33% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16466 | 113 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11463 | 93 | -10% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 7610 | 66 | -1% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40615 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16313 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11395 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 68323 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 257 | 0% | -$4,674.20 | -57% | — |
| Sell at 2¢ | 2799 | 4% | -$7,236.46 | -87% | 47 sec |
| Sell at 3¢ | 1878 | 3% | -$7,231.78 | -87% | 48 sec |
| Sell at 5¢ | 1270 | 2% | -$7,110.70 | -86% | 62 sec |
| Sell at 10¢ | 778 | 1% | -$6,833.02 | -83% | 65 sec |
| Sell at 25¢ | 421 | 1% | -$6,304.69 | -76% | 80 sec |
| Sell at 50¢ | 268 | 0% | -$5,707.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3526 | 17 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 22158 | 116 | 7% | 3% | -48% | -86% | -86% |
| 1–2 min | 17041 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25585 | 66 | 1% | 0% | -63% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4542 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4535 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4529 | 20 | 4% | 2% | -43% | -86% | -86% |
| BNB | 4521 | 22 | 5% | 2% | -38% | -85% | -85% |
| DOGE | 4519 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4513 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4493 | 24 | 6% | 2% | -26% | -86% | -87% |
| NEAR | 4486 | 18 | 5% | 2% | -47% | -86% | -86% |
| XRP | 4477 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2410 | 8 | 5% | 2% | -59% | -83% | -84% |
| WTI | 2393 | 9 | 4% | 2% | -54% | -86% | -87% |
| SILVER | 2355 | 9 | 5% | 2% | -54% | -83% | -84% |
| PLATINUM | 2138 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2088 | 7 | 2% | 1% | -69% | -91% | -90% |
| GBPUSD | 2032 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 2024 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1984 | 6 | 2% | 1% | -72% | -97% | -96% |
| NATGAS | 1981 | 10 | 2% | 1% | -53% | -77% | -77% |
| PALLADIUM | 1924 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1553 | 7 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1459 | 1 | 3% | 1% | -94% | -95% | -96% |
| BRENT | 1088 | 1 | 2% | 1% | -91% | -96% | -96% |
| 10YRRATE | 557 | 2 | 3% | 1% | -66% | -78% | -76% |
| 30YRRATE | 518 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 515 | 4 | 4% | 2% | -28% | -57% | -57% |
| 5YRRATE | 506 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 139 | 1 | 2% | 1% | -33% | -96% | -96% |
| USDMXN | 44 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34878 | 133 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33445 | 124 | 4% | 2% | -57% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5895 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6453 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 10067 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12802 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5389 | 24 | 7% | 3% | -53% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16499 | 51 | 4% | 2% | -65% | -87% | -88% |
| Morning (6am–12pm) | 16148 | 82 | 4% | 2% | -42% | -86% | -85% |
| Afternoon (12–6pm) | 16751 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18925 | 51 | 4% | 2% | -69% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,080 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/26 6:14:45 AM | WTI | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:14:45 AM | NEAR | DOWN | 15 sec | +0.003% | 0¢ | ❌ Lost | $0.00 |
| 11/26 6:14:29 AM | HYPE | UP | 31 sec | -0.115% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:14:29 AM | SOL | DOWN | 31 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 11/26 6:14:29 AM | BTC | UP | 31 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 11/26 6:14:14 AM | ETH | UP | 45 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 11/26 6:13:57 AM | PALLADIUM | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:13:57 AM | AUDUSD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:13:57 AM | GOLD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:13:57 AM | XRP | UP | 62 sec | -0.210% | 0¢ | ❌ Lost | $0.00 |
| 11/26 6:13:25 AM | BNB | DOWN | 1.6 min | +0.071% | 3¢ | ❌ Lost | -$0.15 |
| 11/26 6:13:09 AM | DOGE | DOWN | 1.9 min | +0.180% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:13:09 AM | ZEC | UP | 1.9 min | -0.289% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 6:12:36 AM | EURUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:12:36 AM | USDCAD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:12:36 AM | GBPUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:12:04 AM | PLATINUM | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:10:30 AM | COPPER | UP | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:10:14 AM | SILVER | UP | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/26 5:59:56 AM | PALLADIUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 5:59:56 AM | SILVER | DOWN | 3 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/26 5:59:56 AM | WTI | DOWN | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/26 5:59:40 AM | NATGAS | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 5:59:40 AM | EURUSD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 5:59:40 AM | BRENT | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 5:59:40 AM | USDJPY | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 5:59:24 AM | BNB | UP | 36 sec | -0.058% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 5:59:24 AM | ETH | UP | 36 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 11/26 5:59:24 AM | SOL | UP | 36 sec | -0.078% | 0¢ | ❌ Lost | $0.00 |
| 11/26 5:59:05 AM | USDCAD | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
