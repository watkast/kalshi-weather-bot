# 15-Minute 1¢ Study

*Updated Thu Nov 26, 3:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4953 finished bets | 1% | $203.20 | +38% | +4.10¢ | $83.95 / $119.25 |

*Expect about **83 buys a day** (~$12.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4700 | $102.20 | +20% |
| Volatility model ≥ 2%, hold to the close | 9232 | $35.55 | +3% |
| Momentum model ≥ 2%, hold to the close | 7691 | -$45.80 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 68596 | 68562 | 257 (0%) | 1.07% | -$4,702.70 (-57%) | Hold to the close: -$4,702.70 (-57%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 40535 | 4.5% | 0.4% (165) | -655% | ❌ Worse |
| Momentum model | 40535 | 4.4% | 0.4% (165) | -678% | ❌ Worse |
| Mean-reversion model | 40535 | 7.9% | 0.4% (165) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40535 | 165 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9232 | 81 | +3% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 4953 | 53 | +38% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2870 | 32 | +65% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 7691 | 59 | -5% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4700 | 43 | +20% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 3061 | 28 | +32% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16520 | 113 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11502 | 93 | -10% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 7633 | 66 | -1% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40741 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16380 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11441 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 68562 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 257 | 0% | -$4,702.70 | -57% | — |
| Sell at 2¢ | 2803 | 4% | -$7,263.92 | -88% | 47 sec |
| Sell at 3¢ | 1880 | 3% | -$7,259.50 | -87% | 48 sec |
| Sell at 5¢ | 1272 | 2% | -$7,137.90 | -86% | 62 sec |
| Sell at 10¢ | 780 | 1% | -$6,858.90 | -83% | 65 sec |
| Sell at 25¢ | 422 | 1% | -$6,329.88 | -76% | 80 sec |
| Sell at 50¢ | 269 | 0% | -$5,728.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3547 | 17 | 11% | 4% | -55% | -81% | -83% |
| 2–5 min | 22231 | 116 | 7% | 3% | -49% | -86% | -87% |
| 1–2 min | 17079 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25692 | 66 | 1% | 0% | -63% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4557 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4550 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4542 | 20 | 4% | 2% | -43% | -86% | -86% |
| BNB | 4535 | 22 | 5% | 2% | -38% | -86% | -85% |
| DOGE | 4533 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4526 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4506 | 24 | 6% | 2% | -27% | -86% | -87% |
| NEAR | 4501 | 18 | 5% | 2% | -47% | -86% | -86% |
| XRP | 4491 | 16 | 4% | 2% | -54% | -89% | -89% |
| GOLD | 2420 | 8 | 5% | 2% | -59% | -83% | -84% |
| WTI | 2404 | 9 | 4% | 2% | -54% | -86% | -87% |
| SILVER | 2365 | 9 | 5% | 2% | -54% | -83% | -83% |
| PLATINUM | 2145 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2094 | 7 | 2% | 1% | -69% | -91% | -90% |
| GBPUSD | 2042 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 2031 | 6 | 2% | 1% | -72% | -79% | -79% |
| USDJPY | 1991 | 6 | 2% | 1% | -72% | -97% | -96% |
| NATGAS | 1985 | 10 | 2% | 1% | -53% | -77% | -77% |
| PALLADIUM | 1931 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1561 | 7 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1469 | 1 | 3% | 1% | -94% | -96% | -96% |
| BRENT | 1099 | 1 | 2% | 1% | -92% | -96% | -96% |
| 10YRRATE | 557 | 2 | 3% | 1% | -66% | -78% | -76% |
| 30YRRATE | 518 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 515 | 4 | 4% | 2% | -28% | -57% | -57% |
| 5YRRATE | 506 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 139 | 1 | 2% | 1% | -33% | -96% | -96% |
| USDMXN | 49 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34986 | 133 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33576 | 124 | 4% | 2% | -57% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5904 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6475 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 10090 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12847 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5416 | 24 | 7% | 3% | -53% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16499 | 51 | 4% | 2% | -65% | -87% | -88% |
| Morning (6am–12pm) | 16354 | 82 | 4% | 2% | -43% | -86% | -85% |
| Afternoon (12–6pm) | 16784 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18925 | 51 | 4% | 2% | -69% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,078 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/26 3:10:22 PM | NEAR | UP | 4.6 min | -0.729% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:10:22 PM | ZEC | UP | 4.6 min | -0.975% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:10:06 PM | XRP | UP | 4.9 min | -0.367% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:09:32 PM | ETH | UP | 5.5 min | -0.379% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:09:32 PM | DOGE | UP | 5.5 min | -0.476% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:09:32 PM | HYPE | UP | 5.5 min | -0.697% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:09:16 PM | BTC | UP | 5.7 min | -0.359% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:08:45 PM | BNB | UP | 6.2 min | -0.338% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:08:12 PM | SOL | UP | 6.8 min | -0.545% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 2:59:47 PM | DOGE | UP | 13 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 11/26 2:59:31 PM | SOL | UP | 29 sec | -0.066% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 2:59:31 PM | XRP | UP | 29 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |
| 11/26 2:59:31 PM | WTI | UP | 29 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/26 2:59:15 PM | BNB | UP | 45 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 11/26 2:58:27 PM | BTC | UP | 1.6 min | -0.077% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 2:58:11 PM | HYPE | UP | 1.8 min | -0.315% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 2:57:39 PM | ETH | UP | 2.4 min | -0.121% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 2:57:39 PM | NEAR | UP | 2.4 min | -0.400% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 2:54:59 PM | ZEC | UP | 5.0 min | -0.879% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 2:44:50 PM | BTC | UP | 9 sec | -0.008% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 2:44:50 PM | USDJPY | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 2:44:50 PM | WTI | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/26 2:44:34 PM | DOGE | DOWN | 25 sec | +0.047% | 0¢ | ❌ Lost | $0.00 |
| 11/26 2:44:34 PM | HYPE | UP | 25 sec | -0.128% | 0¢ | ❌ Lost | $0.00 |
| 11/26 2:44:34 PM | GBPUSD | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 2:44:18 PM | BRENT | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 2:44:18 PM | USDCAD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 2:42:42 PM | BNB | DOWN | 2.3 min | +0.095% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 2:42:42 PM | NEAR | DOWN | 2.3 min | +0.220% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 2:42:26 PM | ZEC | DOWN | 2.5 min | +0.442% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
