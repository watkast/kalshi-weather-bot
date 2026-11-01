# 15-Minute 1¢ Study

*Updated Sat Oct 31, 6:34 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3333 finished bets | 1% | $103.40 | +28% | +3.10¢ | $80.90 / $22.50 |

*Expect about **99 buys a day** (~$14.82/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3085 | $55.70 | +17% |
| Volatility model ≥ 2%, hold to the close | 6158 | $10.35 | +1% |
| Momentum model ≥ 2%, hold to the close | 5083 | -$55.85 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 40910 | 40900 | 151 (0%) | 1.07% | -$2,867.65 (-58%) | Hold to the close: -$2,867.65 (-58%) |

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
| Volatility model | 25299 | 4.7% | 0.4% (98) | -697% | ❌ Worse |
| Momentum model | 25299 | 4.6% | 0.4% (98) | -719% | ❌ Worse |
| Mean-reversion model | 25299 | 8.1% | 0.4% (98) | -847% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 25299 | 98 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6158 | 54 | +1% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3333 | 34 | +28% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1889 | 21 | +59% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 5083 | 38 | -10% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3085 | 28 | +17% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 2015 | 19 | +31% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10409 | 69 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7293 | 59 | -10% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4876 | 41 | -4% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 25501 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 40900 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 151 | 0% | -$2,867.65 | -58% | — |
| Sell at 2¢ | 1589 | 4% | -$4,344.51 | -87% | 47 sec |
| Sell at 3¢ | 1095 | 3% | -$4,330.60 | -87% | 48 sec |
| Sell at 5¢ | 757 | 2% | -$4,251.60 | -85% | 63 sec |
| Sell at 10¢ | 454 | 1% | -$4,078.91 | -82% | 65 sec |
| Sell at 25¢ | 238 | 1% | -$3,773.87 | -76% | 82 sec |
| Sell at 50¢ | 155 | 0% | -$3,431.40 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1913 | 9 | 11% | 4% | -55% | -80% | -81% |
| 2–5 min | 13047 | 70 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 10355 | 35 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 15574 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2856 | 13 | 5% | 3% | -42% | -88% | -88% |
| HYPE | 2846 | 8 | 5% | 2% | -65% | -89% | -87% |
| SOL | 2844 | 9 | 4% | 2% | -60% | -91% | -91% |
| BNB | 2843 | 16 | 5% | 2% | -30% | -85% | -84% |
| DOGE | 2835 | 6 | 4% | 2% | -73% | -90% | -89% |
| ETH | 2833 | 11 | 6% | 3% | -53% | -85% | -85% |
| NEAR | 2815 | 13 | 5% | 2% | -40% | -83% | -83% |
| BTC | 2815 | 13 | 5% | 2% | -38% | -88% | -89% |
| XRP | 2814 | 11 | 3% | 1% | -52% | -89% | -89% |
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
| UP (bought YES) | 20755 | 82 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 20145 | 69 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4138 | 21 | 2% | 1% | -12% | -82% | -81% |
| 0.05–0.1% | 4357 | 14 | 3% | 2% | -52% | -92% | -91% |
| 0.1–0.2% | 6564 | 22 | 4% | 2% | -58% | -90% | -89% |
| 0.2–0.5% | 7552 | 32 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2885 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10116 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10310 | 46 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 9655 | 34 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 10819 | 35 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,629 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/31 6:28:47 PM | ETH | DOWN | 72 sec | +0.048% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 6:28:31 PM | DOGE | DOWN | 88 sec | +0.091% | 0¢ | ❌ Lost | $0.00 |
| 10/31 6:28:15 PM | XRP | DOWN | 1.8 min | +0.064% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 6:27:25 PM | SOL | DOWN | 2.6 min | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 6:27:10 PM | HYPE | DOWN | 2.8 min | +0.224% | 4¢ | ❌ Lost | -$0.15 |
| 10/31 6:26:19 PM | ZEC | DOWN | 3.7 min | +0.423% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 6:26:04 PM | BTC | DOWN | 3.9 min | +0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 6:26:04 PM | BNB | DOWN | 3.9 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 6:25:46 PM | NEAR | DOWN | 4.2 min | +0.464% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 6:14:36 PM | DOGE | UP | 24 sec | -0.146% | 0¢ | ❌ Lost | $0.00 |
| 10/31 6:14:36 PM | ZEC | UP | 24 sec | -0.068% | 0¢ | ❌ Lost | $0.00 |
| 10/31 6:14:36 PM | XRP | DOWN | 24 sec | -0.024% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 6:13:55 PM | ETH | UP | 64 sec | -0.043% | 5¢ | ❌ Lost | -$0.15 |
| 10/31 6:13:39 PM | BNB | UP | 80 sec | -0.114% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 6:13:23 PM | NEAR | UP | 1.6 min | -0.348% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 6:13:07 PM | SOL | UP | 1.9 min | -0.137% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 6:12:18 PM | BTC | UP | 2.7 min | -0.089% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 5:59:27 PM | DOGE | DOWN | 32 sec | -0.017% | 0¢ | ❌ Lost | $0.00 |
| 10/31 5:58:38 PM | HYPE | DOWN | 81 sec | +0.103% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 5:58:22 PM | BNB | DOWN | 1.6 min | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/31 5:58:22 PM | ETH | DOWN | 1.6 min | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 10/31 5:58:06 PM | BTC | DOWN | 1.9 min | +0.045% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 5:57:01 PM | ZEC | UP | 3.0 min | -0.430% | 0¢ | ❌ Lost | $0.00 |
| 10/31 5:56:44 PM | SOL | DOWN | 3.2 min | +0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 5:44:25 PM | XRP | DOWN | 35 sec | +0.024% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 5:44:08 PM | BTC | UP | 51 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/31 5:43:52 PM | BNB | DOWN | 67 sec | +0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 5:43:52 PM | SOL | UP | 67 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/31 5:43:20 PM | DOGE | DOWN | 1.7 min | +0.075% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 5:42:45 PM | ZEC | DOWN | 2.2 min | +0.250% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
