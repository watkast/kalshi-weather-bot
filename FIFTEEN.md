# 15-Minute 1¢ Study

*Updated Wed Nov 25, 8:48 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4913 finished bets | 1% | $206.95 | +39% | +4.21¢ | $86.20 / $120.75 |

*Expect about **83 buys a day** (~$12.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4655 | $106.40 | +21% |
| Volatility model ≥ 2%, hold to the close | 9156 | $43.95 | +4% |
| Momentum model ≥ 2%, hold to the close | 7614 | -$37.85 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 68026 | 67992 | 256 (0%) | 1.07% | -$4,647.55 (-56%) | Hold to the close: -$4,647.55 (-56%) |

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
| Volatility model | 40254 | 4.5% | 0.4% (165) | -649% | ❌ Worse |
| Momentum model | 40254 | 4.4% | 0.4% (165) | -672% | ❌ Worse |
| Mean-reversion model | 40254 | 7.9% | 0.4% (165) | -788% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40254 | 165 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9156 | 81 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4913 | 53 | +39% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2840 | 32 | +67% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 7614 | 59 | -4% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4655 | 43 | +21% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3032 | 28 | +33% | -68% | -68% | -63% |
| Mean-reversion model ≥ 2% | 16396 | 113 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11413 | 93 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7577 | 66 | -0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40460 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16207 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11325 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 67992 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 256 | 0% | -$4,647.55 | -56% | — |
| Sell at 2¢ | 2786 | 4% | -$7,213.19 | -88% | 47 sec |
| Sell at 3¢ | 1870 | 3% | -$7,208.25 | -88% | 48 sec |
| Sell at 5¢ | 1263 | 2% | -$7,088.60 | -86% | 62 sec |
| Sell at 10¢ | 772 | 1% | -$6,814.23 | -83% | 65 sec |
| Sell at 25¢ | 416 | 1% | -$6,294.59 | -76% | 80 sec |
| Sell at 50¢ | 266 | 0% | -$5,694.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3515 | 17 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 22047 | 116 | 7% | 3% | -48% | -86% | -86% |
| 1–2 min | 16955 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25462 | 65 | 1% | 0% | -63% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4525 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4518 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4511 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4504 | 22 | 5% | 2% | -38% | -86% | -85% |
| DOGE | 4502 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4495 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4475 | 24 | 6% | 2% | -26% | -86% | -87% |
| NEAR | 4471 | 18 | 5% | 2% | -47% | -85% | -86% |
| XRP | 4459 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2396 | 8 | 5% | 2% | -59% | -83% | -84% |
| WTI | 2381 | 8 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2339 | 9 | 5% | 2% | -54% | -83% | -84% |
| PLATINUM | 2123 | 5 | 3% | 1% | -78% | -95% | -94% |
| EURUSD | 2076 | 7 | 3% | 1% | -69% | -91% | -90% |
| GBPUSD | 2018 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 2012 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1971 | 6 | 2% | 1% | -72% | -96% | -96% |
| NATGAS | 1969 | 10 | 2% | 1% | -53% | -77% | -77% |
| PALLADIUM | 1910 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1540 | 7 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1448 | 1 | 3% | 1% | -94% | -95% | -96% |
| BRENT | 1077 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 557 | 2 | 3% | 1% | -66% | -78% | -76% |
| 30YRRATE | 518 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 515 | 4 | 4% | 2% | -28% | -57% | -57% |
| 5YRRATE | 506 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 139 | 1 | 2% | 1% | -33% | -96% | -96% |
| USDMXN | 37 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34735 | 132 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33257 | 124 | 4% | 2% | -57% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5870 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6419 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 10031 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12754 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5377 | 24 | 7% | 3% | -53% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16330 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16129 | 82 | 4% | 2% | -42% | -86% | -85% |
| Afternoon (12–6pm) | 16751 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18782 | 51 | 4% | 2% | -69% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,087 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/25 8:44:46 PM | XRP | DOWN | 14 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:44:46 PM | DOGE | DOWN | 14 sec | -0.030% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:44:46 PM | AUDUSD | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:44:30 PM | BTC | UP | 30 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:44:30 PM | HYPE | UP | 30 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:44:14 PM | ETH | UP | 46 sec | -0.085% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:44:14 PM | SILVER | DOWN | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:44:14 PM | GOLD | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:43:38 PM | SOL | UP | 81 sec | -0.145% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:43:06 PM | NATGAS | DOWN | 1.9 min | — | 15¢ | ❌ Lost | -$0.15 |
| 11/25 8:42:31 PM | PALLADIUM | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:41:22 PM | EURUSD | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:41:06 PM | GBPUSD | UP | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:40:16 PM | NEAR | UP | 4.7 min | -0.681% | 2¢ | ❌ Lost | -$0.15 |
| 11/25 8:40:16 PM | ZEC | UP | 4.7 min | -0.629% | 2¢ | ❌ Lost | -$0.15 |
| 11/25 8:29:50 PM | DOGE | UP | 10 sec | -0.041% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:29:50 PM | SILVER | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:29:34 PM | USDCAD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:29:34 PM | XRP | UP | 26 sec | -0.084% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:29:34 PM | BTC | UP | 26 sec | -0.033% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:29:34 PM | GBPUSD | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:29:18 PM | ETH | UP | 42 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:29:03 PM | NEAR | UP | 56 sec | -0.205% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:29:03 PM | GOLD | UP | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:28:44 PM | USDJPY | DOWN | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:28:28 PM | BNB | UP | 1.5 min | -0.186% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:28:12 PM | SOL | UP | 1.8 min | -0.172% | 3¢ | ❌ Lost | -$0.15 |
| 11/25 8:28:12 PM | HYPE | UP | 1.8 min | -0.294% | 1¢ | ❌ Lost | $0.00 |
| 11/25 8:27:56 PM | BRENT | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:27:56 PM | WTI | DOWN | 2.1 min | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
