# 15-Minute 1¢ Study

*Updated Sun Nov 1, 4:45 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3445 finished bets | 1% | $132.95 | +35% | +3.86¢ | $74.90 / $58.05 |

*Expect about **99 buys a day** (~$14.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3181 | $59.80 | +17% |
| Volatility model ≥ 2%, hold to the close | 6361 | $55.60 | +7% |
| Momentum model ≥ 2%, hold to the close | 5245 | -$32.60 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41681 | 41655 | 157 (0%) | 1.07% | -$2,871.10 (-57%) | Hold to the close: -$2,871.10 (-57%) |

*In play or awaiting result: 25. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 26041 | 4.7% | 0.4% (104) | -680% | ❌ Worse |
| Momentum model | 26041 | 4.6% | 0.4% (104) | -702% | ❌ Worse |
| Mean-reversion model | 26041 | 8.1% | 0.4% (104) | -828% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26041 | 104 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6361 | 59 | +7% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3445 | 37 | +35% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1954 | 22 | +61% | -70% | -68% | -64% |
| Momentum model ≥ 2% | 5245 | 41 | -5% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3181 | 29 | +17% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 2076 | 19 | +28% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10753 | 74 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7532 | 64 | -6% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5041 | 46 | +4% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26243 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9717 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5695 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41655 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 157 | 0% | -$2,871.10 | -57% | — |
| Sell at 2¢ | 1633 | 4% | -$4,420.52 | -87% | 47 sec |
| Sell at 3¢ | 1123 | 3% | -$4,407.13 | -87% | 48 sec |
| Sell at 5¢ | 781 | 2% | -$4,309.45 | -85% | 63 sec |
| Sell at 10¢ | 470 | 1% | -$4,131.40 | -82% | 65 sec |
| Sell at 25¢ | 249 | 1% | -$3,810.91 | -75% | 83 sec |
| Sell at 50¢ | 162 | 0% | -$3,457.60 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1970 | 9 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 13366 | 74 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 10531 | 37 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 15777 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2939 | 13 | 5% | 3% | -43% | -88% | -87% |
| SOL | 2929 | 11 | 4% | 2% | -53% | -91% | -91% |
| HYPE | 2927 | 9 | 5% | 2% | -62% | -89% | -87% |
| BNB | 2926 | 17 | 5% | 2% | -27% | -85% | -84% |
| ETH | 2916 | 11 | 6% | 3% | -54% | -85% | -85% |
| DOGE | 2915 | 6 | 4% | 2% | -74% | -90% | -90% |
| BTC | 2899 | 14 | 5% | 2% | -35% | -87% | -89% |
| NEAR | 2896 | 14 | 5% | 2% | -37% | -83% | -83% |
| XRP | 2896 | 11 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1516 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1482 | 7 | 5% | 2% | -44% | -82% | -81% |
| WTI | 1477 | 4 | 3% | 1% | -67% | -93% | -93% |
| PLATINUM | 1314 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1253 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1251 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1212 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1185 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1178 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1172 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 708 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 687 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 285 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21138 | 86 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20517 | 71 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4293 | 21 | 2% | 1% | -15% | -82% | -81% |
| 0.05–0.1% | 4517 | 17 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 6792 | 24 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7729 | 33 | 7% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2907 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10303 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9833 | 36 | 4% | 2% | -57% | -87% | -87% |
| Evening (6pm–12am) | 11006 | 37 | 3% | 2% | -61% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,801 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 4:44:58 PM | USDCAD | DOWN | 1 sec | — | 0¢ | In play | — |
| 11/1 4:44:58 PM | PLATINUM | DOWN | 1 sec | — | 0¢ | In play | — |
| 11/1 4:44:58 PM | NATGAS | DOWN | 1 sec | — | 0¢ | In play | — |
| 11/1 4:44:25 PM | EURUSD | UP | 34 sec | — | 0¢ | In play | — |
| 11/1 4:44:25 PM | GBPUSD | UP | 34 sec | — | 0¢ | In play | — |
| 11/1 4:44:09 PM | USDJPY | DOWN | 50 sec | — | 0¢ | In play | — |
| 11/1 4:44:09 PM | BRENT | UP | 50 sec | — | 0¢ | In play | — |
| 11/1 4:43:37 PM | PALLADIUM | DOWN | 82 sec | — | 0¢ | In play | — |
| 11/1 4:43:37 PM | GOLD | DOWN | 82 sec | — | 2¢ | In play | — |
| 11/1 4:43:21 PM | WTI | UP | 1.6 min | — | 1¢ | In play | — |
| 11/1 4:43:06 PM | AUDUSD | DOWN | 1.9 min | — | 0¢ | In play | — |
| 11/1 4:42:50 PM | SILVER | DOWN | 2.1 min | — | 1¢ | In play | — |
| 11/1 4:42:18 PM | XRP | DOWN | 2.7 min | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:39:50 PM | BTC | DOWN | 5.2 min | +0.316% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:39:34 PM | HYPE | DOWN | 5.4 min | +0.568% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:39:18 PM | DOGE | DOWN | 5.7 min | +0.403% | 1¢ | In play | — |
| 11/1 4:39:18 PM | ETH | DOWN | 5.7 min | +0.446% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:39:03 PM | ZEC | DOWN | 6.0 min | +0.709% | 1¢ | In play | — |
| 11/1 4:38:44 PM | BNB | DOWN | 6.2 min | +0.226% | 1¢ | In play | — |
| 11/1 4:38:44 PM | SOL | DOWN | 6.2 min | +0.402% | 1¢ | In play | — |
| 11/1 4:38:44 PM | NEAR | DOWN | 6.2 min | +0.685% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:29:59 PM | EURUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 4:29:27 PM | AUDUSD | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 4:28:55 PM | SILVER | DOWN | 65 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/1 4:28:55 PM | XRP | UP | 65 sec | -0.104% | 0¢ | ❌ Lost | $0.00 |
| 11/1 4:28:55 PM | WTI | DOWN | 65 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:28:55 PM | BTC | UP | 65 sec | -0.106% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:28:39 PM | ZEC | UP | 81 sec | -0.213% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:28:25 PM | BRENT | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 4:28:09 PM | HYPE | UP | 1.9 min | -0.188% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
