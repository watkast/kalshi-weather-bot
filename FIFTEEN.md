# 15-Minute 1¢ Study

*Updated Tue Oct 27, 1:23 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2874 finished bets | 1% | $81.70 | +25% | +2.84¢ | $93.00 / -$11.30 |

*Expect about **97 buys a day** (~$14.60/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2682 | $40.80 | +14% |
| Volatility model ≥ 2%, hold to the close | 5334 | -$7.60 | -1% |
| Momentum model ≥ 2%, hold to the close | 4431 | -$54.90 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 35051 | 35043 | 132 (0%) | 1.07% | -$2,421.15 (-57%) | Hold to the close: -$2,421.15 (-57%) |

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
| Volatility model | 22098 | 4.7% | 0.4% (88) | -676% | ❌ Worse |
| Momentum model | 22098 | 4.6% | 0.4% (88) | -702% | ❌ Worse |
| Mean-reversion model | 22098 | 8.0% | 0.4% (88) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22098 | 88 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5334 | 46 | -1% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2874 | 29 | +25% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1634 | 18 | +55% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4431 | 33 | -11% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2682 | 24 | +14% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1754 | 16 | +26% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8972 | 59 | -28% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6284 | 49 | -14% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4194 | 35 | -6% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22298 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8288 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4457 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 35043 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 132 | 0% | -$2,421.15 | -57% | — |
| Sell at 2¢ | 1326 | 4% | -$3,728.39 | -87% | 47 sec |
| Sell at 3¢ | 903 | 3% | -$3,720.98 | -87% | 48 sec |
| Sell at 5¢ | 624 | 2% | -$3,667.55 | -86% | 62 sec |
| Sell at 10¢ | 383 | 1% | -$3,515.42 | -82% | 65 sec |
| Sell at 25¢ | 207 | 1% | -$3,247.98 | -76% | 1.5 min |
| Sell at 50¢ | 137 | 0% | -$2,924.40 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1559 | 8 | 11% | 4% | -51% | -81% | -82% |
| 2–5 min | 11233 | 62 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 8886 | 31 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 13361 | 31 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2498 | 12 | 5% | 2% | -39% | -89% | -88% |
| HYPE | 2489 | 8 | 5% | 3% | -60% | -89% | -86% |
| BNB | 2488 | 15 | 5% | 2% | -25% | -84% | -83% |
| SOL | 2485 | 6 | 4% | 2% | -70% | -92% | -92% |
| ETH | 2477 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2474 | 5 | 4% | 2% | -75% | -90% | -90% |
| NEAR | 2465 | 12 | 5% | 2% | -37% | -82% | -82% |
| XRP | 2463 | 9 | 3% | 1% | -55% | -89% | -89% |
| BTC | 2459 | 12 | 5% | 2% | -35% | -88% | -89% |
| GOLD | 1320 | 5 | 4% | 2% | -55% | -81% | -83% |
| SILVER | 1288 | 6 | 4% | 2% | -46% | -82% | -82% |
| WTI | 1268 | 4 | 3% | 1% | -63% | -93% | -95% |
| PLATINUM | 1140 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1092 | 4 | 1% | 1% | -66% | -72% | -72% |
| EURUSD | 1061 | 3 | 2% | 1% | -74% | -87% | -87% |
| NATGAS | 1051 | 6 | 2% | 1% | -47% | -79% | -78% |
| PALLADIUM | 1008 | 2 | 1% | 0% | -81% | -89% | -89% |
| GBPUSD | 1001 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 989 | 5 | 1% | 1% | -53% | -98% | -97% |
| AUDUSD | 546 | 3 | 1% | 1% | -49% | -81% | -80% |
| USDCAD | 505 | 0 | 1% | 0% | -100% | -98% | -98% |
| BRENT | 121 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 98 | 0 | 4% | 0% | -100% | -93% | -92% |
| 30YRRATE | 88 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 85 | 1 | 4% | 1% | +10% | +16% | +16% |
| 5YRRATE | 84 | 1 | 5% | 2% | +11% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17725 | 73 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 17318 | 59 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3657 | 18 | 2% | 1% | -16% | -81% | -80% |
| 0.05–0.1% | 3822 | 13 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 5789 | 20 | 5% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 6578 | 29 | 7% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2448 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8119 | 25 | 4% | 2% | -64% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,639 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 1:14:13 PM | COPPER | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:14:13 PM | ZEC | UP | 47 sec | -0.226% | 0¢ | ❌ Lost | $0.00 |
| 10/27 1:14:13 PM | USDCAD | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:13:57 PM | 2YRRATE | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:13:57 PM | AUDUSD | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:13:41 PM | PALLADIUM | DOWN | 79 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:13:23 PM | EURUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:13:23 PM | BNB | UP | 1.6 min | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:12:19 PM | BRENT | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:12:19 PM | GBPUSD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:12:03 PM | NATGAS | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:11:47 PM | 5YRRATE | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:11:47 PM | USDJPY | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:11:31 PM | BTC | DOWN | 3.5 min | +0.120% | 5¢ | ❌ Lost | -$0.15 |
| 10/27 1:11:31 PM | 10YRRATE | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:11:31 PM | WTI | UP | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:10:42 PM | HYPE | DOWN | 4.3 min | +0.416% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:10:42 PM | 30YRRATE | UP | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:10:42 PM | SILVER | DOWN | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:10:10 PM | GOLD | DOWN | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:10:10 PM | XRP | DOWN | 4.8 min | +0.250% | 4¢ | ❌ Lost | -$0.15 |
| 10/27 1:10:10 PM | SOL | DOWN | 4.8 min | +0.352% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:09:54 PM | DOGE | DOWN | 5.1 min | +0.224% | 7¢ | ❌ Lost | -$0.15 |
| 10/27 1:08:31 PM | PLATINUM | DOWN | 6.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:59:49 PM | 10YRRATE | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:59:49 PM | AUDUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:59:33 PM | 30YRRATE | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:59:33 PM | GOLD | DOWN | 26 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 12:59:15 PM | HYPE | DOWN | 45 sec | +0.005% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:59:15 PM | DOGE | UP | 45 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
