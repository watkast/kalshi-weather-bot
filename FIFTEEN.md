# 15-Minute 1¢ Study

*Updated Sat Oct 31, 1:48 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3250 finished bets | 1% | $98.70 | +27% | +3.04¢ | $85.70 / $13.00 |

*Expect about **98 buys a day** (~$14.75/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3016 | $48.60 | +15% |
| Volatility model ≥ 2%, hold to the close | 6021 | $12.55 | +2% |
| Momentum model ≥ 2%, hold to the close | 4972 | -$57.70 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 40375 | 40365 | 150 (0%) | 1.07% | -$2,825.70 (-57%) | Hold to the close: -$2,825.70 (-57%) |

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
| Volatility model | 24765 | 4.7% | 0.4% (97) | -686% | ❌ Worse |
| Momentum model | 24765 | 4.6% | 0.4% (97) | -709% | ❌ Worse |
| Mean-reversion model | 24765 | 8.1% | 0.4% (97) | -833% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24765 | 97 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6021 | 53 | +2% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3250 | 33 | +27% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1838 | 20 | +55% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 4972 | 37 | -10% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3016 | 27 | +15% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1965 | 18 | +27% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10179 | 68 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7123 | 58 | -10% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4755 | 40 | -4% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24966 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 40365 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 150 | 0% | -$2,825.70 | -57% | — |
| Sell at 2¢ | 1559 | 4% | -$4,296.36 | -87% | 47 sec |
| Sell at 3¢ | 1071 | 3% | -$4,284.01 | -87% | 48 sec |
| Sell at 5¢ | 746 | 2% | -$4,202.80 | -85% | 63 sec |
| Sell at 10¢ | 448 | 1% | -$4,030.82 | -82% | 65 sec |
| Sell at 25¢ | 235 | 1% | -$3,727.85 | -76% | 83 sec |
| Sell at 50¢ | 154 | 0% | -$3,382.20 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1886 | 9 | 11% | 4% | -55% | -80% | -81% |
| 2–5 min | 12872 | 70 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10222 | 35 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15374 | 36 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2794 | 13 | 5% | 3% | -41% | -88% | -88% |
| HYPE | 2787 | 8 | 5% | 2% | -64% | -89% | -87% |
| BNB | 2785 | 16 | 5% | 3% | -28% | -85% | -84% |
| SOL | 2782 | 8 | 4% | 2% | -64% | -91% | -91% |
| DOGE | 2775 | 6 | 4% | 2% | -73% | -90% | -89% |
| ETH | 2773 | 11 | 6% | 3% | -52% | -85% | -85% |
| NEAR | 2758 | 13 | 5% | 2% | -39% | -83% | -83% |
| BTC | 2757 | 13 | 5% | 2% | -37% | -88% | -89% |
| XRP | 2755 | 11 | 3% | 1% | -51% | -89% | -89% |
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
| UP (bought YES) | 20495 | 82 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19870 | 68 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3992 | 20 | 2% | 1% | -13% | -81% | -81% |
| 0.05–0.1% | 4233 | 14 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 6417 | 22 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 7460 | 32 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2860 | 11 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9978 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10122 | 46 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9463 | 33 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 10802 | 35 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,521 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/31 1:42:16 AM | BTC | UP | 2.7 min | -0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:42:16 AM | ZEC | UP | 2.7 min | -0.417% | 0¢ | ❌ Lost | $0.00 |
| 10/31 1:42:16 AM | ETH | UP | 2.7 min | -0.140% | 0¢ | ❌ Lost | $0.00 |
| 10/31 1:40:07 AM | DOGE | UP | 4.9 min | -0.297% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:40:07 AM | HYPE | UP | 4.9 min | -0.466% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:39:51 AM | BNB | UP | 5.2 min | -0.257% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:39:33 AM | NEAR | UP | 5.5 min | -0.977% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:38:46 AM | SOL | UP | 6.2 min | -0.346% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:38:46 AM | XRP | UP | 6.2 min | -0.289% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:29:59 AM | XRP | DOWN | 0 sec | -0.008% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 1:29:59 AM | BNB | DOWN | 0 sec | -0.071% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 1:29:43 AM | BTC | DOWN | 16 sec | -0.009% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:29:27 AM | DOGE | UP | 32 sec | -0.103% | 0¢ | ❌ Lost | $0.00 |
| 10/31 1:28:39 AM | NEAR | UP | 80 sec | -0.381% | 0¢ | ❌ Lost | $0.00 |
| 10/31 1:28:23 AM | SOL | DOWN | 1.6 min | +0.078% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:28:23 AM | ETH | DOWN | 1.6 min | +0.067% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 1:26:38 AM | HYPE | DOWN | 3.4 min | +0.224% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:26:06 AM | ZEC | DOWN | 3.9 min | +0.452% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:14:46 AM | BTC | DOWN | 13 sec | +0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/31 1:14:15 AM | DOGE | UP | 44 sec | -0.096% | 0¢ | ❌ Lost | $0.00 |
| 10/31 1:13:59 AM | ETH | UP | 60 sec | -0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:13:59 AM | NEAR | DOWN | 60 sec | +0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:13:43 AM | BNB | UP | 76 sec | -0.164% | 0¢ | ❌ Lost | $0.00 |
| 10/31 1:13:27 AM | ZEC | DOWN | 1.5 min | +0.272% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 1:12:06 AM | SOL | UP | 2.9 min | -0.239% | 2¢ | ❌ Lost | -$0.15 |
| 10/31 1:11:49 AM | XRP | UP | 3.2 min | -0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:09:42 AM | HYPE | UP | 5.3 min | -0.545% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 12:59:15 AM | ETH | DOWN | 44 sec | +0.009% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 12:58:59 AM | XRP | DOWN | 61 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/31 12:58:59 AM | SOL | UP | 61 sec | -0.111% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
