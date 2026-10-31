# 15-Minute 1¢ Study

*Updated Fri Oct 30, 6:27 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3207 finished bets | 1% | $89.95 | +25% | +2.80¢ | $74.10 / $15.85 |

*Expect about **98 buys a day** (~$14.69/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2974 | $39.70 | +12% |
| Volatility model ≥ 2%, hold to the close | 5950 | $7.25 | +1% |
| Momentum model ≥ 2%, hold to the close | 4908 | -$63.90 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 40105 | 40090 | 149 (0%) | 1.07% | -$2,810.30 (-57%) | Hold to the close: -$2,810.30 (-57%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 24499 | 4.7% | 0.4% (96) | -682% | ❌ Worse |
| Momentum model | 24499 | 4.5% | 0.4% (96) | -704% | ❌ Worse |
| Mean-reversion model | 24499 | 8.1% | 0.4% (96) | -829% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24499 | 96 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5950 | 52 | +1% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3207 | 32 | +25% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1812 | 19 | +50% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 4908 | 36 | -11% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2974 | 26 | +12% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1936 | 17 | +22% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10068 | 67 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7046 | 57 | -10% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4702 | 39 | -6% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24700 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9703 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 40090 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 149 | 0% | -$2,810.30 | -57% | — |
| Sell at 2¢ | 1549 | 4% | -$4,269.56 | -87% | 47 sec |
| Sell at 3¢ | 1065 | 3% | -$4,256.95 | -87% | 49 sec |
| Sell at 5¢ | 742 | 2% | -$4,176.00 | -85% | 63 sec |
| Sell at 10¢ | 446 | 1% | -$4,004.04 | -82% | 65 sec |
| Sell at 25¢ | 233 | 1% | -$3,705.07 | -76% | 83 sec |
| Sell at 50¢ | 152 | 0% | -$3,366.30 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1871 | 9 | 11% | 4% | -54% | -80% | -81% |
| 2–5 min | 12779 | 70 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10152 | 35 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15277 | 35 | 1% | 0% | -68% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2764 | 13 | 5% | 3% | -40% | -88% | -88% |
| HYPE | 2757 | 8 | 5% | 3% | -64% | -89% | -87% |
| BNB | 2756 | 16 | 5% | 3% | -27% | -84% | -83% |
| SOL | 2752 | 7 | 4% | 2% | -68% | -91% | -91% |
| DOGE | 2745 | 6 | 4% | 2% | -73% | -90% | -89% |
| ETH | 2743 | 11 | 6% | 3% | -51% | -85% | -85% |
| NEAR | 2728 | 13 | 5% | 2% | -38% | -83% | -83% |
| BTC | 2728 | 13 | 5% | 2% | -36% | -88% | -89% |
| XRP | 2727 | 11 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1515 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1481 | 7 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1469 | 4 | 3% | 1% | -67% | -93% | -93% |
| PLATINUM | 1314 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1253 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1249 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1210 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1185 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1178 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1171 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 705 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 685 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 283 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20355 | 81 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19735 | 68 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3938 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4191 | 14 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 6336 | 22 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 7383 | 32 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2848 | 11 | 7% | 3% | -60% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9916 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10122 | 46 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9463 | 33 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 10589 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,466 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 6:27:07 PM | BNB | DOWN | 2.9 min | +0.359% | — | In play | — |
| 10/30 6:27:07 PM | ZEC | DOWN | 2.9 min | +0.493% | — | In play | — |
| 10/30 6:24:56 PM | NEAR | DOWN | 5.1 min | +0.674% | — | In play | — |
| 10/30 6:24:56 PM | HYPE | DOWN | 5.1 min | +0.552% | — | In play | — |
| 10/30 6:24:21 PM | DOGE | DOWN | 5.7 min | +0.346% | — | In play | — |
| 10/30 6:14:38 PM | BTC | UP | 22 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/30 6:14:38 PM | SOL | UP | 22 sec | -0.107% | 0¢ | ❌ Lost | $0.00 |
| 10/30 6:14:23 PM | ETH | DOWN | 36 sec | +0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 6:13:50 PM | NEAR | DOWN | 69 sec | +0.284% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 6:13:34 PM | DOGE | DOWN | 85 sec | +0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 6:12:43 PM | ZEC | DOWN | 2.3 min | +0.485% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 6:11:53 PM | XRP | DOWN | 3.1 min | +0.159% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 6:11:07 PM | HYPE | UP | 3.9 min | -0.515% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 6:08:21 PM | BNB | DOWN | 6.6 min | +0.368% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 5:59:54 PM | BTC | DOWN | 6 sec | -0.007% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 5:59:54 PM | XRP | DOWN | 6 sec | -0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/30 5:59:22 PM | HYPE | DOWN | 37 sec | +0.004% | 1¢ | ❌ Lost | $0.00 |
| 10/30 5:59:22 PM | BNB | UP | 37 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 5:59:22 PM | DOGE | UP | 37 sec | -0.066% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 5:58:49 PM | ETH | UP | 70 sec | -0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 5:58:49 PM | NEAR | UP | 70 sec | -0.270% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 5:58:49 PM | WTI | DOWN | 70 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 5:58:33 PM | ZEC | DOWN | 86 sec | +0.411% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 5:58:33 PM | SOL | DOWN | 86 sec | +0.048% | 1¢ | ❌ Lost | $0.00 |
| 10/30 5:44:35 PM | WTI | UP | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 5:44:00 PM | BRENT | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 5:44:00 PM | NEAR | UP | 60 sec | -0.387% | 0¢ | ❌ Lost | $0.00 |
| 10/30 5:42:39 PM | ETH | DOWN | 2.4 min | +0.091% | 4¢ | ❌ Lost | -$0.15 |
| 10/30 5:42:39 PM | HYPE | DOWN | 2.4 min | +0.267% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 5:42:39 PM | BNB | DOWN | 2.4 min | +0.090% | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
