# 15-Minute 1¢ Study

*Updated Fri Oct 30, 9:16 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3217 finished bets | 1% | $89.05 | +25% | +2.77¢ | $73.65 / $15.40 |

*Expect about **98 buys a day** (~$14.69/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2983 | $38.80 | +12% |
| Volatility model ≥ 2%, hold to the close | 5967 | $5.60 | +1% |
| Momentum model ≥ 2%, hold to the close | 4921 | -$65.25 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 40216 | 40206 | 149 (0%) | 1.07% | -$2,821.40 (-57%) | Hold to the close: -$2,821.40 (-57%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 24606 | 4.7% | 0.4% (96) | -683% | ❌ Worse |
| Momentum model | 24606 | 4.5% | 0.4% (96) | -706% | ❌ Worse |
| Mean-reversion model | 24606 | 8.0% | 0.4% (96) | -831% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24606 | 96 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5967 | 52 | +1% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 3217 | 32 | +25% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1820 | 19 | +49% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 4921 | 36 | -11% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2983 | 26 | +12% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 1944 | 17 | +22% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10107 | 67 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7071 | 57 | -11% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4716 | 39 | -6% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24807 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 40206 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 149 | 0% | -$2,821.40 | -57% | — |
| Sell at 2¢ | 1552 | 4% | -$4,279.88 | -87% | 47 sec |
| Sell at 3¢ | 1067 | 3% | -$4,267.27 | -87% | 48 sec |
| Sell at 5¢ | 744 | 2% | -$4,185.80 | -85% | 63 sec |
| Sell at 10¢ | 447 | 1% | -$4,013.83 | -82% | 65 sec |
| Sell at 25¢ | 234 | 1% | -$3,712.86 | -76% | 83 sec |
| Sell at 50¢ | 153 | 0% | -$3,370.65 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1875 | 9 | 11% | 4% | -54% | -80% | -81% |
| 2–5 min | 12815 | 70 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10178 | 35 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15327 | 35 | 1% | 0% | -68% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2776 | 13 | 5% | 3% | -40% | -88% | -88% |
| HYPE | 2769 | 8 | 5% | 2% | -64% | -89% | -87% |
| BNB | 2768 | 16 | 5% | 3% | -27% | -85% | -83% |
| SOL | 2763 | 7 | 4% | 2% | -68% | -91% | -91% |
| DOGE | 2757 | 6 | 4% | 2% | -73% | -90% | -89% |
| ETH | 2755 | 11 | 6% | 3% | -51% | -85% | -85% |
| NEAR | 2740 | 13 | 5% | 2% | -38% | -83% | -83% |
| BTC | 2740 | 13 | 5% | 2% | -36% | -88% | -89% |
| XRP | 2739 | 11 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1515 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1481 | 7 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1476 | 4 | 3% | 1% | -67% | -93% | -93% |
| PLATINUM | 1314 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1253 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1249 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1212 | 7 | 2% | 1% | -46% | -81% | -80% |
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
| UP (bought YES) | 20418 | 81 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19788 | 68 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3956 | 19 | 2% | 1% | -17% | -81% | -81% |
| 0.05–0.1% | 4207 | 14 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 6375 | 22 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 7410 | 32 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2855 | 11 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9916 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10122 | 46 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9463 | 33 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 10705 | 34 | 3% | 2% | -64% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,486 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 9:14:58 PM | WTI | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 9:14:42 PM | BNB | UP | 18 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/30 9:13:20 PM | ZEC | UP | 1.7 min | -0.194% | 0¢ | ❌ Lost | $0.00 |
| 10/30 9:13:05 PM | SOL | UP | 1.9 min | -0.152% | 1¢ | ❌ Lost | $0.00 |
| 10/30 9:12:48 PM | XRP | UP | 2.2 min | -0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 9:12:32 PM | NEAR | UP | 2.5 min | -0.485% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 9:12:16 PM | BTC | UP | 2.7 min | -0.177% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 9:12:16 PM | DOGE | UP | 2.7 min | -0.261% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:12:00 PM | HYPE | UP | 3.0 min | -0.379% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:10:23 PM | ETH | UP | 4.6 min | -0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:59:59 PM | BTC | UP | 1 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/30 8:59:43 PM | ETH | DOWN | 17 sec | -0.011% | 0¢ | ❌ Lost | $0.00 |
| 10/30 8:59:27 PM | ZEC | UP | 33 sec | +0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/30 8:58:55 PM | XRP | DOWN | 64 sec | +0.072% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:58:08 PM | SOL | UP | 1.9 min | -0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:58:08 PM | DOGE | UP | 1.9 min | -0.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:57:36 PM | NEAR | UP | 2.4 min | -0.444% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:56:48 PM | HYPE | UP | 3.2 min | -0.367% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:56:32 PM | BNB | DOWN | 3.5 min | +0.111% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:44:45 PM | NEAR | UP | 14 sec | -0.193% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:44:29 PM | BNB | DOWN | 30 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/30 8:44:13 PM | ZEC | DOWN | 47 sec | +0.282% | 0¢ | ❌ Lost | $0.00 |
| 10/30 8:43:40 PM | ETH | DOWN | 79 sec | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:43:24 PM | XRP | DOWN | 1.6 min | +0.112% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:42:51 PM | HYPE | DOWN | 2.1 min | +0.330% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:42:51 PM | DOGE | DOWN | 2.1 min | +0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:42:51 PM | BTC | DOWN | 2.1 min | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:42:19 PM | SOL | DOWN | 2.7 min | +0.192% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:29:42 PM | SOL | DOWN | 17 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/30 8:29:26 PM | XRP | UP | 33 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
