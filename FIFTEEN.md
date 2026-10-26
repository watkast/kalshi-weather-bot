# 15-Minute 1¢ Study

*Updated Mon Oct 26, 7:49 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2746 finished bets | 1% | $80.30 | +26% | +2.92¢ | $31.10 / $49.20 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2551 | $53.70 | +19% |
| Volatility model ≥ 2%, hold to the close | 5093 | -$21.70 | -3% |
| Momentum model ≥ 2%, hold to the close | 4240 | -$35.10 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32827 | 32819 | 122 (0%) | 1.07% | -$2,280.95 (-57%) | Hold to the close: -$2,280.95 (-57%) |

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
| Volatility model | 21073 | 4.6% | 0.4% (85) | -663% | ❌ Worse |
| Momentum model | 21073 | 4.5% | 0.4% (85) | -687% | ❌ Worse |
| Mean-reversion model | 21073 | 7.9% | 0.4% (85) | -804% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21073 | 85 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5093 | 43 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2746 | 28 | +26% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1554 | 18 | +62% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 4240 | 33 | -7% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2551 | 24 | +19% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1661 | 16 | +32% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8513 | 56 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5958 | 47 | -13% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3968 | 33 | -6% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21273 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7664 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3882 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32819 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 122 | 0% | -$2,280.95 | -57% | — |
| Sell at 2¢ | 1232 | 4% | -$3,500.63 | -88% | 47 sec |
| Sell at 3¢ | 843 | 3% | -$3,492.18 | -88% | 48 sec |
| Sell at 5¢ | 588 | 2% | -$3,438.75 | -86% | 61 sec |
| Sell at 10¢ | 364 | 1% | -$3,302.11 | -83% | 65 sec |
| Sell at 25¢ | 195 | 1% | -$3,063.50 | -77% | 83 sec |
| Sell at 50¢ | 126 | 0% | -$2,774.45 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1451 | 8 | 11% | 4% | -47% | -81% | -82% |
| 2–5 min | 10523 | 56 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8320 | 30 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 12521 | 28 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2384 | 12 | 5% | 2% | -36% | -89% | -89% |
| HYPE | 2376 | 8 | 5% | 3% | -58% | -88% | -87% |
| BNB | 2373 | 13 | 5% | 3% | -32% | -84% | -83% |
| SOL | 2370 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2364 | 11 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2356 | 4 | 4% | 2% | -79% | -91% | -90% |
| XRP | 2353 | 9 | 3% | 1% | -53% | -89% | -89% |
| NEAR | 2352 | 12 | 5% | 2% | -34% | -82% | -81% |
| BTC | 2345 | 12 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1237 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1204 | 6 | 4% | 2% | -42% | -82% | -81% |
| WTI | 1179 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1051 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1024 | 4 | 1% | 1% | -64% | -70% | -70% |
| EURUSD | 982 | 3 | 2% | 1% | -71% | -87% | -87% |
| NATGAS | 974 | 5 | 2% | 1% | -52% | -87% | -86% |
| PALLADIUM | 940 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 929 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 909 | 5 | 1% | 1% | -49% | -98% | -97% |
| AUDUSD | 471 | 1 | 1% | 1% | -80% | -98% | -97% |
| USDCAD | 433 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 55 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 45 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 41 | 1 | 2% | 0% | +128% | +132% | +128% |
| 30YRRATE | 41 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 31 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16636 | 67 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16183 | 55 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3533 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3649 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5500 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6230 | 28 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2357 | 10 | 7% | 3% | -56% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 7921 | 36 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,782 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 7:44:58 AM | 2YRRATE | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:44:58 AM | USDJPY | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:44:58 AM | GBPUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:44:58 AM | WTI | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 7:44:42 AM | COPPER | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:44:27 AM | 5YRRATE | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:44:10 AM | USDCAD | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:43:54 AM | DOGE | UP | 65 sec | -0.289% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:43:54 AM | 10YRRATE | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:43:54 AM | 30YRRATE | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:43:54 AM | SOL | UP | 65 sec | -0.302% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:43:54 AM | ETH | UP | 65 sec | -0.370% | 0¢ | ❌ Lost | $0.00 |
| 10/26 7:43:38 AM | SILVER | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:43:38 AM | XRP | UP | 81 sec | -0.318% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:43:38 AM | PLATINUM | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:43:38 AM | HYPE | UP | 81 sec | -0.326% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:43:22 AM | GOLD | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:43:22 AM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:43:22 AM | BTC | UP | 1.6 min | -0.275% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:43:22 AM | BNB | UP | 1.6 min | -0.299% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:43:22 AM | PALLADIUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:43:03 AM | ZEC | DOWN | 1.9 min | +0.590% | 3¢ | ❌ Lost | -$0.15 |
| 10/26 7:40:06 AM | NEAR | DOWN | 4.9 min | +1.189% | 13¢ | ❌ Lost | -$0.15 |
| 10/26 7:29:47 AM | PLATINUM | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:29:47 AM | EURUSD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:29:15 AM | BRENT | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:29:15 AM | 10YRRATE | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:29:00 AM | WTI | UP | 59 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 7:28:44 AM | NATGAS | UP | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:28:44 AM | 30YRRATE | UP | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
