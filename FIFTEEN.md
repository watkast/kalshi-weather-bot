# 15-Minute 1¢ Study

*Updated Sun Nov 1, 7:57 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3457 finished bets | 1% | $131.90 | +34% | +3.82¢ | $74.45 / $57.45 |

*Expect about **99 buys a day** (~$14.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3188 | $59.35 | +17% |
| Volatility model ≥ 2%, hold to the close | 6382 | $53.35 | +7% |
| Momentum model ≥ 2%, hold to the close | 5261 | -$34.10 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41881 | 41864 | 158 (0%) | 1.07% | -$2,882.60 (-57%) | Hold to the close: -$2,882.60 (-57%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 26147 | 4.7% | 0.4% (105) | -677% | ❌ Worse |
| Momentum model | 26147 | 4.6% | 0.4% (105) | -699% | ❌ Worse |
| Mean-reversion model | 26147 | 8.1% | 0.4% (105) | -825% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26147 | 105 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6382 | 59 | +7% | -79% | -78% | -73% |
| Volatility model ≥ 5% | 3457 | 37 | +34% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1960 | 22 | +60% | -70% | -68% | -64% |
| Momentum model ≥ 2% | 5261 | 41 | -6% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3188 | 29 | +17% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 2081 | 19 | +28% | -73% | -73% | -68% |
| Mean-reversion model ≥ 2% | 10810 | 75 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7578 | 64 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5069 | 46 | +3% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26349 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 9783 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5732 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41864 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 158 | 0% | -$2,882.60 | -57% | — |
| Sell at 2¢ | 1640 | 4% | -$4,444.20 | -87% | 47 sec |
| Sell at 3¢ | 1127 | 3% | -$4,431.07 | -87% | 48 sec |
| Sell at 5¢ | 784 | 2% | -$4,333.00 | -85% | 63 sec |
| Sell at 10¢ | 471 | 1% | -$4,155.59 | -82% | 65 sec |
| Sell at 25¢ | 250 | 1% | -$3,833.10 | -75% | 83 sec |
| Sell at 50¢ | 163 | 0% | -$3,476.35 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1989 | 9 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 13430 | 75 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 10591 | 37 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15843 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2952 | 13 | 5% | 3% | -43% | -88% | -88% |
| SOL | 2942 | 11 | 4% | 2% | -53% | -91% | -90% |
| BNB | 2939 | 17 | 5% | 2% | -28% | -85% | -84% |
| HYPE | 2938 | 9 | 5% | 3% | -62% | -89% | -87% |
| ETH | 2927 | 11 | 6% | 3% | -54% | -85% | -85% |
| DOGE | 2927 | 6 | 4% | 2% | -74% | -90% | -90% |
| BTC | 2909 | 14 | 5% | 2% | -35% | -88% | -89% |
| XRP | 2908 | 11 | 3% | 1% | -53% | -89% | -89% |
| NEAR | 2907 | 15 | 5% | 2% | -33% | -83% | -83% |
| GOLD | 1526 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1491 | 7 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1486 | 4 | 3% | 1% | -68% | -93% | -93% |
| PLATINUM | 1321 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1261 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1258 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1218 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1192 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1186 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1181 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 714 | 4 | 2% | 1% | -48% | -84% | -83% |
| USDCAD | 695 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 294 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21244 | 87 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20620 | 71 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4307 | 21 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 4534 | 17 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 6817 | 24 | 4% | 2% | -56% | -90% | -90% |
| 0.2–0.5% | 7762 | 33 | 7% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2924 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10303 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9923 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11125 | 37 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,806 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 7:56:47 PM | PLATINUM | UP | 3.2 min | — | — | In play | — |
| 11/1 7:56:31 PM | NATGAS | UP | 3.5 min | — | — | In play | — |
| 11/1 7:56:00 PM | GOLD | UP | 4.0 min | — | — | In play | — |
| 11/1 7:56:00 PM | XRP | UP | 4.0 min | -0.239% | — | In play | — |
| 11/1 7:55:42 PM | NEAR | UP | 4.3 min | -0.590% | — | In play | — |
| 11/1 7:55:42 PM | COPPER | UP | 4.3 min | — | — | In play | — |
| 11/1 7:54:36 PM | PALLADIUM | UP | 5.4 min | — | — | In play | — |
| 11/1 7:44:54 PM | WTI | UP | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/1 7:44:38 PM | BRENT | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:44:23 PM | BTC | UP | 36 sec | -0.074% | 0¢ | ❌ Lost | $0.00 |
| 11/1 7:44:23 PM | XRP | UP | 36 sec | -0.128% | 0¢ | ❌ Lost | $0.00 |
| 11/1 7:44:04 PM | SILVER | UP | 55 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/1 7:44:04 PM | ZEC | UP | 55 sec | -0.195% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 7:43:48 PM | ETH | UP | 71 sec | -0.114% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:43:48 PM | SOL | UP | 71 sec | -0.153% | 0¢ | ❌ Lost | $0.00 |
| 11/1 7:43:32 PM | GOLD | UP | 87 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/1 7:43:32 PM | USDCAD | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:43:17 PM | DOGE | UP | 1.7 min | -0.156% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:43:17 PM | PLATINUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:43:17 PM | PALLADIUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:43:17 PM | AUDUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:42:42 PM | HYPE | DOWN | 2.3 min | +0.250% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 7:41:54 PM | COPPER | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:41:22 PM | NEAR | UP | 3.6 min | -0.656% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 7:40:33 PM | BNB | UP | 4.4 min | -0.210% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 7:29:49 PM | GOLD | DOWN | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/1 7:29:18 PM | BRENT | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:29:18 PM | WTI | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:28:59 PM | HYPE | DOWN | 60 sec | +0.045% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:28:43 PM | XRP | DOWN | 76 sec | +0.136% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
