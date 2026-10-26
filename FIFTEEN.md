# 15-Minute 1¢ Study

*Updated Mon Oct 26, 12:49 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2765 finished bets | 1% | $78.65 | +25% | +2.84¢ | $29.90 / $48.75 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2573 | $51.90 | +18% |
| Volatility model ≥ 2%, hold to the close | 5145 | -$27.70 | -4% |
| Momentum model ≥ 2%, hold to the close | 4279 | -$39.00 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33234 | 33226 | 123 (0%) | 1.07% | -$2,318.55 (-57%) | Hold to the close: -$2,318.55 (-57%) |

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
| Volatility model | 21251 | 4.6% | 0.4% (85) | -667% | ❌ Worse |
| Momentum model | 21251 | 4.5% | 0.4% (85) | -692% | ❌ Worse |
| Mean-reversion model | 21251 | 7.9% | 0.4% (85) | -810% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21251 | 85 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5145 | 43 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2765 | 28 | +25% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1564 | 18 | +61% | -67% | -65% | -62% |
| Momentum model ≥ 2% | 4279 | 33 | -8% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2573 | 24 | +18% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1677 | 16 | +31% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8603 | 56 | -29% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 6026 | 47 | -14% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4013 | 33 | -7% | -78% | -77% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21451 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7773 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4002 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33226 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 123 | 0% | -$2,318.55 | -57% | — |
| Sell at 2¢ | 1256 | 4% | -$3,545.99 | -88% | 47 sec |
| Sell at 3¢ | 859 | 3% | -$3,537.54 | -88% | 48 sec |
| Sell at 5¢ | 596 | 2% | -$3,485.15 | -86% | 61 sec |
| Sell at 10¢ | 368 | 1% | -$3,348.47 | -83% | 65 sec |
| Sell at 25¢ | 195 | 1% | -$3,101.10 | -77% | 83 sec |
| Sell at 50¢ | 126 | 0% | -$2,812.05 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1466 | 8 | 11% | 4% | -48% | -81% | -82% |
| 2–5 min | 10671 | 57 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8413 | 30 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 12672 | 28 | 1% | 0% | -68% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2403 | 12 | 5% | 2% | -36% | -88% | -88% |
| HYPE | 2396 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2393 | 13 | 5% | 3% | -32% | -84% | -83% |
| SOL | 2390 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2384 | 11 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2376 | 4 | 4% | 2% | -79% | -91% | -90% |
| XRP | 2373 | 9 | 3% | 1% | -53% | -89% | -89% |
| NEAR | 2371 | 12 | 5% | 2% | -34% | -82% | -82% |
| BTC | 2365 | 12 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1250 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1217 | 6 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1195 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1065 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1036 | 4 | 1% | 1% | -64% | -71% | -70% |
| EURUSD | 998 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 991 | 5 | 2% | 1% | -53% | -87% | -86% |
| PALLADIUM | 954 | 2 | 1% | 0% | -80% | -88% | -89% |
| GBPUSD | 942 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 924 | 5 | 1% | 1% | -49% | -98% | -97% |
| AUDUSD | 485 | 1 | 1% | 1% | -81% | -98% | -97% |
| USDCAD | 449 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 65 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 58 | 0 | 2% | 0% | -100% | -97% | -96% |
| 2YRRATE | 51 | 1 | 4% | 0% | +83% | +90% | +88% |
| 30YRRATE | 51 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 44 | 1 | 2% | 2% | +112% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16833 | 68 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 16393 | 55 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3546 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3665 | 11 | 3% | 2% | -56% | -92% | -92% |
| 0.1–0.2% | 5544 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6304 | 28 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2388 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 7667 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,738 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 12:44:59 PM | 30YRRATE | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:44:43 PM | NATGAS | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:44:43 PM | 5YRRATE | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:44:27 PM | 10YRRATE | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:44:27 PM | AUDUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:44:27 PM | ZEC | UP | 32 sec | -0.324% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:44:11 PM | BNB | UP | 48 sec | -0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:44:11 PM | USDJPY | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:44:11 PM | GBPUSD | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:44:11 PM | BTC | UP | 48 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:43:39 PM | ETH | UP | 81 sec | -0.120% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:43:23 PM | PALLADIUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:43:23 PM | SOL | UP | 1.6 min | -0.241% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:43:23 PM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:43:07 PM | XRP | UP | 1.9 min | -0.162% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:42:50 PM | WTI | DOWN | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:42:18 PM | NEAR | UP | 2.7 min | -0.635% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:42:02 PM | SILVER | UP | 3.0 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/26 12:42:02 PM | PLATINUM | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:42:02 PM | HYPE | UP | 3.0 min | -0.381% | 3¢ | ❌ Lost | -$0.15 |
| 10/26 12:41:48 PM | EURUSD | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:41:48 PM | DOGE | UP | 3.2 min | -0.207% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:41:00 PM | USDCAD | DOWN | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:40:44 PM | GOLD | UP | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:29:57 PM | HYPE | DOWN | 2 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:29:41 PM | BNB | DOWN | 18 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:29:41 PM | NATGAS | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:29:41 PM | USDJPY | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:29:41 PM | ETH | UP | 18 sec | -0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:29:25 PM | PALLADIUM | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
