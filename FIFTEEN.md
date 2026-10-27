# 15-Minute 1¢ Study

*Updated Mon Oct 26, 9:20 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2795 finished bets | 1% | $76.10 | +24% | +2.72¢ | $27.80 / $48.30 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2600 | $49.65 | +17% |
| Volatility model ≥ 2%, hold to the close | 5201 | -$19.70 | -3% |
| Momentum model ≥ 2%, hold to the close | 4322 | -$43.05 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33812 | 33804 | 126 (0%) | 1.07% | -$2,346.15 (-57%) | Hold to the close: -$2,346.15 (-57%) |

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
| Volatility model | 21547 | 4.6% | 0.4% (86) | -670% | ❌ Worse |
| Momentum model | 21547 | 4.5% | 0.4% (86) | -694% | ❌ Worse |
| Mean-reversion model | 21547 | 7.9% | 0.4% (86) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21547 | 86 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5201 | 44 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2795 | 28 | +24% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1586 | 18 | +60% | -67% | -65% | -62% |
| Momentum model ≥ 2% | 4322 | 33 | -9% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2600 | 24 | +17% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1697 | 16 | +30% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8723 | 57 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6111 | 47 | -15% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4070 | 33 | -8% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21747 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7933 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4124 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33804 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 126 | 0% | -$2,346.15 | -57% | — |
| Sell at 2¢ | 1273 | 4% | -$3,611.17 | -88% | 47 sec |
| Sell at 3¢ | 872 | 3% | -$3,602.07 | -88% | 48 sec |
| Sell at 5¢ | 605 | 2% | -$3,548.90 | -86% | 61 sec |
| Sell at 10¢ | 373 | 1% | -$3,397.52 | -83% | 65 sec |
| Sell at 25¢ | 199 | 1% | -$3,143.46 | -76% | 83 sec |
| Sell at 50¢ | 129 | 0% | -$2,847.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1481 | 8 | 11% | 4% | -48% | -81% | -82% |
| 2–5 min | 10839 | 58 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8546 | 31 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12934 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2436 | 12 | 5% | 3% | -37% | -88% | -88% |
| HYPE | 2428 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2426 | 13 | 5% | 2% | -33% | -84% | -83% |
| SOL | 2423 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2416 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2411 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2405 | 12 | 5% | 2% | -35% | -82% | -82% |
| XRP | 2404 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2398 | 12 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1273 | 5 | 4% | 2% | -53% | -81% | -83% |
| SILVER | 1239 | 6 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1219 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1086 | 0 | 1% | 1% | -100% | -97% | -98% |
| COPPER | 1052 | 4 | 1% | 1% | -65% | -71% | -71% |
| EURUSD | 1020 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1013 | 5 | 2% | 1% | -54% | -87% | -87% |
| PALLADIUM | 970 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 962 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 946 | 5 | 1% | 1% | -51% | -98% | -97% |
| AUDUSD | 503 | 2 | 1% | 1% | -63% | -98% | -96% |
| USDCAD | 466 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 81 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 63 | 0 | 3% | 0% | -100% | -94% | -96% |
| 2YRRATE | 57 | 1 | 4% | 0% | +64% | +70% | +68% |
| 30YRRATE | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 50 | 1 | 4% | 4% | +87% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17157 | 69 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16647 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3589 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3726 | 12 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5623 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6397 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2408 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9200 | 31 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,720 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 9:14:47 PM | USDCAD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:14:47 PM | GBPUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:14:31 PM | PALLADIUM | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:14:15 PM | COPPER | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:13:43 PM | ZEC | UP | 76 sec | -0.353% | 0¢ | ❌ Lost | $0.00 |
| 10/26 9:13:43 PM | ETH | UP | 76 sec | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 9:13:27 PM | HYPE | UP | 1.5 min | -0.214% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:12:55 PM | BTC | UP | 2.1 min | -0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 9:12:23 PM | EURUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:12:07 PM | XRP | UP | 2.9 min | -0.293% | 4¢ | ❌ Lost | -$0.15 |
| 10/26 9:11:52 PM | SOL | UP | 3.1 min | -0.286% | 2¢ | ❌ Lost | -$0.15 |
| 10/26 9:11:36 PM | BNB | UP | 3.4 min | -0.208% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:11:20 PM | PLATINUM | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:11:20 PM | DOGE | UP | 3.6 min | -0.312% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 9:11:20 PM | NEAR | UP | 3.6 min | -0.824% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:59:46 PM | DOGE | UP | 14 sec | +0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/26 8:59:46 PM | XRP | UP | 14 sec | -0.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:59:30 PM | GBPUSD | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:59:30 PM | EURUSD | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:59:15 PM | ZEC | UP | 44 sec | -0.124% | 0¢ | ❌ Lost | $0.00 |
| 10/26 8:59:15 PM | NEAR | DOWN | 44 sec | +0.090% | 0¢ | ❌ Lost | $0.00 |
| 10/26 8:58:57 PM | SOL | UP | 63 sec | -0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:58:57 PM | GOLD | UP | 63 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:58:41 PM | NATGAS | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:57:52 PM | BNB | UP | 2.1 min | -0.151% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:57:36 PM | SILVER | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:57:36 PM | PALLADIUM | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:57:36 PM | ETH | UP | 2.4 min | -0.232% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:57:20 PM | BTC | UP | 2.7 min | -0.209% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:56:00 PM | PLATINUM | UP | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
