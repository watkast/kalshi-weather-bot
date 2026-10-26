# 15-Minute 1¢ Study

*Updated Mon Oct 26, 12:29 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2762 finished bets | 1% | $78.80 | +25% | +2.85¢ | $30.05 / $48.75 |

*Expect about **97 buys a day** (~$14.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2570 | $52.05 | +18% |
| Volatility model ≥ 2%, hold to the close | 5141 | -$27.40 | -4% |
| Momentum model ≥ 2%, hold to the close | 4274 | -$38.55 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33200 | 33182 | 123 (0%) | 1.07% | -$2,313.00 (-57%) | Hold to the close: -$2,313.00 (-57%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 21233 | 4.6% | 0.4% (85) | -664% | ❌ Worse |
| Momentum model | 21233 | 4.5% | 0.4% (85) | -689% | ❌ Worse |
| Mean-reversion model | 21233 | 7.9% | 0.4% (85) | -807% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21233 | 85 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5141 | 43 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2762 | 28 | +25% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1562 | 18 | +61% | -67% | -65% | -62% |
| Momentum model ≥ 2% | 4274 | 33 | -8% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2570 | 24 | +18% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1674 | 16 | +31% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8596 | 56 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6022 | 47 | -14% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4009 | 33 | -7% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21433 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7760 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3989 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33182 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 123 | 0% | -$2,313.00 | -57% | — |
| Sell at 2¢ | 1251 | 4% | -$3,541.74 | -88% | 47 sec |
| Sell at 3¢ | 855 | 3% | -$3,533.55 | -88% | 48 sec |
| Sell at 5¢ | 593 | 2% | -$3,481.55 | -86% | 62 sec |
| Sell at 10¢ | 367 | 1% | -$3,344.23 | -83% | 65 sec |
| Sell at 25¢ | 195 | 1% | -$3,095.55 | -77% | 83 sec |
| Sell at 50¢ | 126 | 0% | -$2,806.50 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1466 | 8 | 11% | 4% | -48% | -81% | -82% |
| 2–5 min | 10656 | 57 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8406 | 30 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 12650 | 28 | 1% | 0% | -68% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2401 | 12 | 5% | 2% | -36% | -88% | -88% |
| HYPE | 2394 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2391 | 13 | 5% | 3% | -32% | -84% | -83% |
| SOL | 2388 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2382 | 11 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2374 | 4 | 4% | 2% | -79% | -91% | -90% |
| XRP | 2371 | 9 | 3% | 1% | -53% | -89% | -89% |
| NEAR | 2369 | 12 | 5% | 2% | -34% | -82% | -82% |
| BTC | 2363 | 12 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1248 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1215 | 6 | 4% | 2% | -42% | -82% | -82% |
| WTI | 1193 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1063 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1035 | 4 | 1% | 1% | -64% | -71% | -70% |
| EURUSD | 996 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 989 | 5 | 2% | 1% | -53% | -87% | -86% |
| PALLADIUM | 952 | 2 | 1% | 0% | -80% | -88% | -89% |
| GBPUSD | 940 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 922 | 5 | 1% | 1% | -49% | -98% | -97% |
| AUDUSD | 484 | 1 | 1% | 1% | -81% | -98% | -97% |
| USDCAD | 447 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 65 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 57 | 0 | 2% | 0% | -100% | -97% | -95% |
| 2YRRATE | 51 | 1 | 4% | 0% | +83% | +90% | +88% |
| 30YRRATE | 49 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 43 | 1 | 2% | 2% | +117% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16801 | 68 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 16381 | 55 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3542 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3663 | 11 | 3% | 2% | -56% | -92% | -92% |
| 0.1–0.2% | 5541 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6296 | 28 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2387 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 7623 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,740 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 12:29:04 PM | NEAR | UP | 55 sec | -0.306% | — | In play | — |
| 10/26 12:29:04 PM | WTI | UP | 55 sec | — | — | In play | — |
| 10/26 12:28:48 PM | EURUSD | UP | 71 sec | — | — | In play | — |
| 10/26 12:28:16 PM | USDCAD | DOWN | 1.7 min | — | — | In play | — |
| 10/26 12:28:00 PM | SILVER | UP | 2.0 min | — | — | In play | — |
| 10/26 12:27:44 PM | GOLD | UP | 2.3 min | — | — | In play | — |
| 10/26 12:27:44 PM | ZEC | UP | 2.3 min | -0.401% | — | In play | — |
| 10/26 12:27:12 PM | DOGE | UP | 2.8 min | -0.232% | — | In play | — |
| 10/26 12:27:12 PM | BTC | UP | 2.8 min | -0.115% | — | In play | — |
| 10/26 12:26:56 PM | SOL | UP | 3.1 min | -0.283% | — | In play | — |
| 10/26 12:14:53 PM | 10YRRATE | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:14:53 PM | USDCAD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:14:37 PM | NEAR | DOWN | 22 sec | +0.115% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:14:21 PM | XRP | DOWN | 38 sec | +0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:14:05 PM | BNB | UP | 54 sec | -0.136% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:14:05 PM | SILVER | UP | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:14:05 PM | ETH | UP | 54 sec | -0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:14:05 PM | WTI | DOWN | 54 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 10/26 12:13:49 PM | DOGE | UP | 70 sec | -0.130% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:13:49 PM | PLATINUM | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:13:33 PM | EURUSD | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:13:33 PM | BTC | UP | 86 sec | -0.097% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:13:17 PM | NATGAS | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:13:17 PM | SOL | UP | 1.7 min | -0.217% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:11:40 PM | HYPE | UP | 3.3 min | -0.574% | 4¢ | ❌ Lost | -$0.15 |
| 10/26 12:11:40 PM | ZEC | UP | 3.3 min | -0.550% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 11:59:49 AM | PLATINUM | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:59:49 AM | USDJPY | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:59:49 AM | ZEC | UP | 10 sec | -0.174% | 0¢ | ❌ Lost | $0.00 |
| 10/26 11:59:49 AM | 2YRRATE | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
