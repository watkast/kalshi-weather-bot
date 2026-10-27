# 15-Minute 1¢ Study

*Updated Tue Oct 27, 6:45 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2840 finished bets | 1% | $70.70 | +22% | +2.49¢ | $81.40 / -$10.70 |

*Expect about **97 buys a day** (~$14.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2652 | $43.20 | +15% |
| Volatility model ≥ 2%, hold to the close | 5280 | -$29.90 | -5% |
| Momentum model ≥ 2%, hold to the close | 4391 | -$51.45 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34533 | 34510 | 128 (0%) | 1.07% | -$2,408.75 (-57%) | Hold to the close: -$2,408.75 (-57%) |

*In play or awaiting result: 22. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 21868 | 4.6% | 0.4% (86) | -676% | ❌ Worse |
| Momentum model | 21868 | 4.6% | 0.4% (86) | -701% | ❌ Worse |
| Mean-reversion model | 21868 | 8.0% | 0.4% (86) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21868 | 86 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5280 | 44 | -5% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2840 | 28 | +22% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1611 | 18 | +57% | -67% | -66% | -63% |
| Momentum model ≥ 2% | 4391 | 33 | -10% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2652 | 24 | +15% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1730 | 16 | +27% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8861 | 57 | -30% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6202 | 47 | -17% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4133 | 33 | -10% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22068 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8139 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4303 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34510 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 128 | 0% | -$2,408.75 | -57% | — |
| Sell at 2¢ | 1293 | 4% | -$3,682.57 | -88% | 47 sec |
| Sell at 3¢ | 882 | 3% | -$3,674.77 | -87% | 48 sec |
| Sell at 5¢ | 611 | 2% | -$3,621.60 | -86% | 62 sec |
| Sell at 10¢ | 376 | 1% | -$3,470.19 | -83% | 65 sec |
| Sell at 25¢ | 202 | 1% | -$3,210.13 | -76% | 86 sec |
| Sell at 50¢ | 132 | 0% | -$2,903.75 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1527 | 8 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 11072 | 59 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8753 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13154 | 30 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2471 | 12 | 5% | 2% | -38% | -89% | -89% |
| HYPE | 2464 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2463 | 13 | 5% | 2% | -34% | -84% | -83% |
| SOL | 2458 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2453 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2447 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2441 | 12 | 5% | 2% | -36% | -82% | -82% |
| XRP | 2438 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2433 | 12 | 5% | 2% | -34% | -88% | -89% |
| GOLD | 1300 | 5 | 4% | 2% | -54% | -81% | -83% |
| SILVER | 1268 | 6 | 4% | 2% | -45% | -82% | -82% |
| WTI | 1247 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1117 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1078 | 4 | 1% | 1% | -65% | -72% | -72% |
| EURUSD | 1045 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1034 | 6 | 2% | 1% | -46% | -78% | -78% |
| PALLADIUM | 990 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 985 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 973 | 5 | 1% | 1% | -52% | -98% | -97% |
| AUDUSD | 529 | 2 | 1% | 1% | -65% | -98% | -97% |
| USDCAD | 489 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 105 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 78 | 0 | 3% | 0% | -100% | -96% | -97% |
| 30YRRATE | 69 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 68 | 1 | 3% | 0% | +37% | +42% | +41% |
| 5YRRATE | 67 | 1 | 3% | 3% | +39% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17490 | 70 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 17020 | 58 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3629 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3783 | 12 | 3% | 2% | -53% | -92% | -92% |
| 0.1–0.2% | 5724 | 20 | 5% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 6504 | 28 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2424 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8308 | 38 | 4% | 2% | -48% | -87% | -86% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,675 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 6:44:14 AM | SILVER | DOWN | 45 sec | — | 1¢ | In play | — |
| 10/27 6:43:59 AM | 30YRRATE | DOWN | 60 sec | — | 0¢ | In play | — |
| 10/27 6:43:11 AM | USDCAD | DOWN | 1.8 min | — | 0¢ | In play | — |
| 10/27 6:43:11 AM | BRENT | DOWN | 1.8 min | — | 0¢ | In play | — |
| 10/27 6:42:56 AM | HYPE | DOWN | 2.1 min | +0.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 6:42:40 AM | BNB | DOWN | 2.3 min | +0.142% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 6:42:40 AM | DOGE | DOWN | 2.3 min | +0.134% | 1¢ | In play | — |
| 10/27 6:42:40 AM | AUDUSD | UP | 2.3 min | — | 0¢ | In play | — |
| 10/27 6:42:24 AM | BTC | DOWN | 2.6 min | +0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 6:42:08 AM | USDJPY | DOWN | 2.9 min | — | 0¢ | In play | — |
| 10/27 6:41:36 AM | NEAR | DOWN | 3.4 min | +0.681% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 6:41:36 AM | COPPER | UP | 3.4 min | — | 0¢ | In play | — |
| 10/27 6:41:20 AM | ETH | DOWN | 3.6 min | +0.300% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 6:41:04 AM | ZEC | DOWN | 3.9 min | +0.871% | 1¢ | In play | — |
| 10/27 6:40:47 AM | SOL | DOWN | 4.2 min | +0.352% | 1¢ | In play | — |
| 10/27 6:39:45 AM | PLATINUM | DOWN | 5.2 min | — | 0¢ | In play | — |
| 10/27 6:39:29 AM | XRP | DOWN | 5.5 min | +0.504% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 6:39:13 AM | WTI | DOWN | 5.8 min | — | 2¢ | In play | — |
| 10/27 6:38:24 AM | 5YRRATE | DOWN | 6.6 min | — | 2¢ | In play | — |
| 10/27 6:38:08 AM | 10YRRATE | DOWN | 6.9 min | — | 3¢ | In play | — |
| 10/27 6:38:08 AM | 2YRRATE | DOWN | 6.9 min | — | 5¢ | In play | — |
| 10/27 6:29:53 AM | PALLADIUM | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 6:29:53 AM | 10YRRATE | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 6:28:49 AM | 5YRRATE | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 6:28:49 AM | PLATINUM | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 6:28:49 AM | COPPER | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 6:28:33 AM | SILVER | DOWN | 86 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 6:28:17 AM | 2YRRATE | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 6:27:46 AM | WTI | UP | 2.2 min | — | 1¢ | ❌ Lost | $0.00 |
| 10/27 6:26:26 AM | GOLD | DOWN | 3.5 min | — | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
