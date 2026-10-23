# 15-Minute 1¢ Study

*Updated Thu Oct 22, 9:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2423 finished bets | 1% | $75.65 | +28% | +3.12¢ | $36.30 / $39.35 |

*Expect about **97 buys a day** (~$14.62/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2233 | $46.65 | +19% |
| Volatility model ≥ 2%, hold to the close | 4476 | -$2.70 | -0% |
| Momentum model ≥ 2%, hold to the close | 3731 | -$33.20 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 29045 | 29037 | 110 (0%) | 1.07% | -$2,000.60 (-57%) | Hold to the close: -$2,000.60 (-57%) |

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
| Volatility model | 18516 | 4.7% | 0.4% (79) | -643% | ❌ Worse |
| Momentum model | 18516 | 4.6% | 0.4% (79) | -668% | ❌ Worse |
| Mean-reversion model | 18516 | 7.9% | 0.4% (79) | -776% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18516 | 79 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4476 | 39 | -0% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2423 | 25 | +28% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1376 | 16 | +63% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3731 | 29 | -8% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2233 | 21 | +19% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1470 | 14 | +31% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7419 | 52 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5193 | 43 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3456 | 30 | -2% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18715 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6990 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3332 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 29037 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 110 | 0% | -$2,000.60 | -57% | — |
| Sell at 2¢ | 1078 | 4% | -$3,120.32 | -88% | 47 sec |
| Sell at 3¢ | 735 | 3% | -$3,113.95 | -88% | 48 sec |
| Sell at 5¢ | 517 | 2% | -$3,064.55 | -87% | 61 sec |
| Sell at 10¢ | 317 | 1% | -$2,957.33 | -84% | 64 sec |
| Sell at 25¢ | 176 | 1% | -$2,720.04 | -77% | 86 sec |
| Sell at 50¢ | 115 | 0% | -$2,456.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1225 | 7 | 11% | 4% | -45% | -80% | -82% |
| 2–5 min | 9344 | 52 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7375 | 28 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 11089 | 23 | 1% | 0% | -70% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2098 | 12 | 5% | 2% | -28% | -89% | -89% |
| BNB | 2091 | 12 | 5% | 3% | -29% | -83% | -82% |
| HYPE | 2089 | 8 | 5% | 3% | -53% | -88% | -87% |
| ETH | 2080 | 10 | 6% | 3% | -42% | -86% | -85% |
| SOL | 2080 | 3 | 4% | 1% | -82% | -92% | -92% |
| DOGE | 2076 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2070 | 8 | 3% | 1% | -52% | -88% | -88% |
| NEAR | 2067 | 12 | 6% | 3% | -25% | -80% | -80% |
| BTC | 2064 | 12 | 5% | 2% | -22% | -88% | -90% |
| GOLD | 1141 | 3 | 4% | 1% | -69% | -81% | -83% |
| SILVER | 1103 | 5 | 3% | 1% | -48% | -82% | -82% |
| WTI | 1081 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 962 | 0 | 1% | 1% | -100% | -99% | -98% |
| COPPER | 948 | 3 | 1% | 1% | -70% | -78% | -78% |
| EURUSD | 890 | 3 | 2% | 1% | -69% | -86% | -86% |
| NATGAS | 884 | 5 | 2% | 1% | -47% | -86% | -85% |
| PALLADIUM | 858 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 838 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 810 | 4 | 1% | 1% | -54% | -99% | -98% |
| AUDUSD | 383 | 0 | 1% | 1% | -100% | -99% | -98% |
| USDCAD | 343 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14638 | 59 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 14399 | 51 | 4% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3102 | 15 | 2% | 1% | -19% | -79% | -78% |
| 0.05–0.1% | 3211 | 11 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4809 | 17 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 5479 | 28 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2110 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7952 | 26 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,679 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 8:59:51 PM | NATGAS | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:59:51 PM | AUDUSD | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:59:51 PM | USDCAD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:59:51 PM | EURUSD | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:59:35 PM | GBPUSD | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:59:35 PM | PLATINUM | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:59:19 PM | COPPER | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:59:19 PM | WTI | UP | 41 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 8:59:04 PM | SOL | DOWN | 56 sec | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:58:48 PM | HYPE | DOWN | 72 sec | +0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/22 8:58:48 PM | PALLADIUM | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:58:16 PM | SILVER | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:58:16 PM | XRP | DOWN | 1.7 min | +0.197% | 0¢ | ❌ Lost | $0.00 |
| 10/22 8:58:16 PM | DOGE | DOWN | 1.7 min | +0.211% | 0¢ | ❌ Lost | $0.00 |
| 10/22 8:58:01 PM | BTC | DOWN | 2.0 min | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:58:01 PM | ETH | DOWN | 2.0 min | +0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:57:36 PM | NEAR | DOWN | 2.4 min | +0.281% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:56:48 PM | ZEC | DOWN | 3.2 min | +0.430% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:55:43 PM | BNB | DOWN | 4.3 min | +0.114% | 2¢ | ❌ Lost | -$0.15 |
| 10/22 8:44:45 PM | USDCAD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:44:45 PM | GBPUSD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:44:45 PM | EURUSD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:44:29 PM | NATGAS | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:44:29 PM | XRP | DOWN | 31 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/22 8:44:13 PM | PLATINUM | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:44:13 PM | PALLADIUM | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:43:56 PM | GOLD | DOWN | 64 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:43:40 PM | SILVER | DOWN | 80 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:43:40 PM | DOGE | DOWN | 80 sec | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:43:40 PM | WTI | UP | 80 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
