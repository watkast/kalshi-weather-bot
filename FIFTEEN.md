# 15-Minute 1¢ Study

*Updated Sun Nov 1, 1:39 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3430 finished bets | 1% | $120.90 | +32% | +3.52¢ | $75.65 / $45.25 |

*Expect about **99 buys a day** (~$14.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3169 | $47.30 | +14% |
| Volatility model ≥ 2%, hold to the close | 6332 | $45.65 | +6% |
| Momentum model ≥ 2%, hold to the close | 5220 | -$43.30 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41541 | 41530 | 156 (0%) | 1.07% | -$2,868.15 (-57%) | Hold to the close: -$2,868.15 (-57%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 25929 | 4.7% | 0.4% (103) | -685% | ❌ Worse |
| Momentum model | 25929 | 4.6% | 0.4% (103) | -707% | ❌ Worse |
| Mean-reversion model | 25929 | 8.1% | 0.4% (103) | -833% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 25929 | 103 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6332 | 58 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3430 | 36 | +32% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1945 | 21 | +54% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5220 | 40 | -7% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3169 | 28 | +14% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 2070 | 19 | +28% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10691 | 73 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7492 | 63 | -7% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5010 | 45 | +2% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26131 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41530 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 156 | 0% | -$2,868.15 | -57% | — |
| Sell at 2¢ | 1626 | 4% | -$4,405.39 | -87% | 47 sec |
| Sell at 3¢ | 1118 | 3% | -$4,392.13 | -87% | 48 sec |
| Sell at 5¢ | 776 | 2% | -$4,295.75 | -85% | 63 sec |
| Sell at 10¢ | 468 | 1% | -$4,117.07 | -81% | 65 sec |
| Sell at 25¢ | 248 | 1% | -$3,797.27 | -75% | 83 sec |
| Sell at 50¢ | 161 | 0% | -$3,447.40 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1953 | 9 | 11% | 4% | -56% | -80% | -82% |
| 2–5 min | 13306 | 73 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10508 | 37 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 15752 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2927 | 13 | 5% | 3% | -43% | -88% | -88% |
| SOL | 2916 | 10 | 4% | 2% | -57% | -91% | -91% |
| HYPE | 2914 | 9 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2914 | 17 | 5% | 2% | -27% | -85% | -84% |
| DOGE | 2904 | 6 | 4% | 2% | -74% | -90% | -90% |
| ETH | 2903 | 11 | 7% | 3% | -54% | -85% | -84% |
| BTC | 2886 | 14 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 2884 | 14 | 5% | 2% | -37% | -83% | -83% |
| XRP | 2883 | 11 | 3% | 1% | -53% | -89% | -89% |
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
| UP (bought YES) | 21089 | 86 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20441 | 70 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4274 | 21 | 2% | 1% | -15% | -82% | -81% |
| 0.05–0.1% | 4503 | 17 | 3% | 2% | -43% | -91% | -91% |
| 0.1–0.2% | 6759 | 23 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 7698 | 33 | 7% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2892 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10303 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9708 | 35 | 4% | 2% | -58% | -87% | -87% |
| Evening (6pm–12am) | 11006 | 37 | 3% | 2% | -61% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,772 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 1:38:03 PM | ETH | DOWN | 7.0 min | +0.168% | — | In play | — |
| 11/1 1:29:41 PM | BTC | DOWN | 18 sec | +0.025% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:29:41 PM | BNB | DOWN | 18 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 11/1 1:29:25 PM | NEAR | DOWN | 34 sec | +0.035% | 0¢ | ❌ Lost | $0.00 |
| 11/1 1:29:25 PM | HYPE | UP | 34 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 11/1 1:29:11 PM | ETH | UP | 48 sec | -0.056% | 5¢ | ❌ Lost | -$0.15 |
| 11/1 1:28:39 PM | XRP | DOWN | 81 sec | +0.120% | 0¢ | ❌ Lost | $0.00 |
| 11/1 1:28:39 PM | SOL | DOWN | 81 sec | +0.121% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 1:28:24 PM | ZEC | DOWN | 1.6 min | +0.220% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:28:24 PM | DOGE | DOWN | 1.6 min | +0.072% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 1:14:45 PM | HYPE | UP | 14 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 11/1 1:14:29 PM | BTC | UP | 30 sec | -0.029% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:14:17 PM | BNB | UP | 42 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 1:14:17 PM | ETH | UP | 42 sec | -0.043% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:14:17 PM | SOL | UP | 42 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 11/1 1:12:30 PM | DOGE | UP | 2.5 min | -0.203% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:12:00 PM | NEAR | UP | 3.0 min | -0.383% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:11:29 PM | ZEC | UP | 3.5 min | -0.458% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:59:36 PM | BTC | DOWN | 23 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 11/1 12:59:36 PM | BNB | DOWN | 23 sec | +0.007% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 12:59:36 PM | ETH | DOWN | 23 sec | +0.008% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 12:59:36 PM | DOGE | UP | 23 sec | -0.007% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:59:20 PM | XRP | UP | 39 sec | -0.048% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:59:04 PM | SOL | DOWN | 56 sec | +0.075% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 12:58:48 PM | NEAR | DOWN | 72 sec | +0.129% | 0¢ | ❌ Lost | $0.00 |
| 11/1 12:58:18 PM | HYPE | DOWN | 1.7 min | +0.117% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 12:58:07 PM | BTC | UP | 1.9 min | -0.060% | 100¢ | ✅ Won | $13.85 |
| 11/1 12:57:16 PM | ZEC | UP | 2.7 min | -0.280% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:43:33 PM | XRP | UP | 87 sec | -0.088% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:41:58 PM | DOGE | UP | 3.0 min | -0.246% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
