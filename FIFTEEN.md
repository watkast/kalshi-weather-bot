# 15-Minute 1¢ Study

*Updated Sun Nov 1, 3:43 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3438 finished bets | 1% | $119.85 | +31% | +3.49¢ | $75.35 / $44.50 |

*Expect about **99 buys a day** (~$14.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3176 | $46.40 | +13% |
| Volatility model ≥ 2%, hold to the close | 6345 | $43.85 | +6% |
| Momentum model ≥ 2%, hold to the close | 5235 | -$45.25 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41616 | 41601 | 156 (0%) | 1.07% | -$2,877.60 (-57%) | Hold to the close: -$2,877.60 (-57%) |

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
| Volatility model | 26000 | 4.7% | 0.4% (103) | -685% | ❌ Worse |
| Momentum model | 26000 | 4.6% | 0.4% (103) | -707% | ❌ Worse |
| Mean-reversion model | 26000 | 8.1% | 0.4% (103) | -833% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26000 | 103 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6345 | 58 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3438 | 36 | +31% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 1950 | 21 | +54% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5235 | 40 | -7% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3176 | 28 | +13% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 2074 | 19 | +28% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10728 | 73 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7517 | 63 | -7% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5029 | 45 | +2% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26202 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41601 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 156 | 0% | -$2,877.60 | -57% | — |
| Sell at 2¢ | 1628 | 4% | -$4,414.32 | -87% | 47 sec |
| Sell at 3¢ | 1119 | 3% | -$4,401.19 | -87% | 48 sec |
| Sell at 5¢ | 777 | 2% | -$4,304.55 | -85% | 63 sec |
| Sell at 10¢ | 468 | 1% | -$4,126.52 | -82% | 65 sec |
| Sell at 25¢ | 248 | 1% | -$3,806.72 | -75% | 83 sec |
| Sell at 50¢ | 161 | 0% | -$3,456.85 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1965 | 9 | 11% | 4% | -56% | -80% | -82% |
| 2–5 min | 13336 | 73 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10520 | 37 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 15769 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2935 | 13 | 5% | 3% | -43% | -88% | -88% |
| SOL | 2924 | 10 | 4% | 2% | -57% | -91% | -91% |
| HYPE | 2922 | 9 | 5% | 2% | -62% | -89% | -87% |
| BNB | 2922 | 17 | 5% | 2% | -27% | -85% | -84% |
| ETH | 2911 | 11 | 6% | 3% | -54% | -85% | -85% |
| DOGE | 2911 | 6 | 4% | 2% | -74% | -90% | -90% |
| BTC | 2894 | 14 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 2892 | 14 | 5% | 2% | -37% | -83% | -83% |
| XRP | 2891 | 11 | 3% | 1% | -53% | -89% | -89% |
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
| UP (bought YES) | 21124 | 86 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20477 | 70 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4291 | 21 | 2% | 1% | -15% | -82% | -81% |
| 0.05–0.1% | 4514 | 17 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 6776 | 23 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 7714 | 33 | 7% | 3% | -53% | -86% | -86% |
| Over 0.5% | 2902 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10303 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9779 | 35 | 4% | 2% | -58% | -87% | -87% |
| Evening (6pm–12am) | 11006 | 37 | 3% | 2% | -61% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,794 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 3:43:19 PM | DOGE | DOWN | 1.7 min | +0.107% | — | In play | — |
| 11/1 3:43:19 PM | BNB | DOWN | 1.7 min | +0.034% | — | In play | — |
| 11/1 3:42:03 PM | ETH | DOWN | 3.0 min | +0.153% | — | In play | — |
| 11/1 3:42:03 PM | BTC | DOWN | 3.0 min | +0.158% | — | In play | — |
| 11/1 3:40:35 PM | SOL | DOWN | 4.4 min | +0.220% | — | In play | — |
| 11/1 3:26:39 PM | ZEC | UP | 3.4 min | -0.615% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:26:23 PM | HYPE | UP | 3.6 min | -0.407% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:25:36 PM | BTC | UP | 4.4 min | -0.202% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:25:20 PM | NEAR | UP | 4.7 min | -0.622% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:24:48 PM | BNB | UP | 5.2 min | -0.266% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 3:24:31 PM | DOGE | UP | 5.5 min | -0.591% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:23:43 PM | ETH | UP | 6.3 min | -0.391% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:23:26 PM | SOL | UP | 6.5 min | -0.784% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:21:05 PM | XRP | UP | 8.9 min | -0.489% | 2¢ | ❌ Lost | -$0.15 |
| 11/1 3:13:21 PM | ETH | UP | 1.6 min | -0.125% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:13:21 PM | BTC | UP | 1.6 min | -0.091% | 0¢ | ❌ Lost | $0.00 |
| 11/1 3:12:19 PM | DOGE | UP | 2.7 min | -0.172% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:12:19 PM | XRP | UP | 2.7 min | -0.168% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:11:31 PM | NEAR | UP | 3.5 min | -0.377% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:11:31 PM | BNB | UP | 3.5 min | -0.195% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:10:44 PM | SOL | UP | 4.2 min | -0.301% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:10:20 PM | HYPE | UP | 4.7 min | -0.545% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 3:10:03 PM | ZEC | UP | 4.9 min | -0.841% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:59:17 PM | ETH | UP | 42 sec | -0.071% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:59:11 PM | BTC | UP | 48 sec | -0.078% | 0¢ | ❌ Lost | $0.00 |
| 11/1 2:59:11 PM | HYPE | UP | 48 sec | -0.110% | 0¢ | ❌ Lost | $0.00 |
| 11/1 2:57:11 PM | NEAR | UP | 2.8 min | -0.351% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:56:59 PM | SOL | UP | 3.0 min | -0.166% | 2¢ | ❌ Lost | -$0.15 |
| 11/1 2:56:59 PM | XRP | UP | 3.0 min | -0.136% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:56:46 PM | DOGE | UP | 3.2 min | -0.182% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
