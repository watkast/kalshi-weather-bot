# 15-Minute 1¢ Study

*Updated Wed Nov 25, 6:12 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4900 finished bets | 1% | $208.15 | +39% | +4.25¢ | $86.95 / $121.20 |

*Expect about **83 buys a day** (~$12.51/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4642 | $107.45 | +22% |
| Volatility model ≥ 2%, hold to the close | 9133 | $45.90 | +4% |
| Momentum model ≥ 2%, hold to the close | 7595 | -$36.35 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 67813 | 67775 | 256 (0%) | 1.07% | -$4,622.95 (-56%) | Hold to the close: -$4,622.95 (-56%) |

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
| Volatility model | 40157 | 4.5% | 0.4% (165) | -646% | ❌ Worse |
| Momentum model | 40157 | 4.4% | 0.4% (165) | -669% | ❌ Worse |
| Mean-reversion model | 40157 | 7.9% | 0.4% (165) | -786% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40157 | 165 | -47% | -87% | -86% | -85% |
| Volatility model ≥ 2% | 9133 | 81 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4900 | 53 | +39% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2834 | 32 | +67% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 7595 | 59 | -4% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4642 | 43 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3024 | 28 | +34% | -68% | -68% | -63% |
| Mean-reversion model ≥ 2% | 16355 | 113 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11390 | 93 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7558 | 66 | -0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40363 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16134 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11278 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 67775 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 256 | 0% | -$4,622.95 | -56% | — |
| Sell at 2¢ | 2777 | 4% | -$7,190.93 | -88% | 47 sec |
| Sell at 3¢ | 1865 | 3% | -$7,185.60 | -88% | 48 sec |
| Sell at 5¢ | 1261 | 2% | -$7,065.30 | -86% | 62 sec |
| Sell at 10¢ | 770 | 1% | -$6,792.25 | -83% | 65 sec |
| Sell at 25¢ | 416 | 1% | -$6,269.99 | -76% | 80 sec |
| Sell at 50¢ | 266 | 0% | -$5,669.45 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3503 | 17 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 21978 | 116 | 7% | 3% | -48% | -86% | -86% |
| 1–2 min | 16903 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25378 | 65 | 1% | 0% | -63% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4514 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4507 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4500 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4494 | 22 | 5% | 2% | -38% | -86% | -85% |
| DOGE | 4491 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4485 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4464 | 24 | 6% | 2% | -26% | -86% | -87% |
| NEAR | 4460 | 18 | 5% | 2% | -47% | -86% | -86% |
| XRP | 4448 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2386 | 8 | 5% | 2% | -59% | -83% | -84% |
| WTI | 2373 | 8 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2328 | 9 | 5% | 2% | -54% | -83% | -84% |
| PLATINUM | 2113 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2066 | 7 | 3% | 1% | -68% | -91% | -90% |
| GBPUSD | 2008 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 2003 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1966 | 6 | 2% | 1% | -72% | -96% | -96% |
| NATGAS | 1962 | 10 | 2% | 1% | -52% | -77% | -77% |
| PALLADIUM | 1900 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1531 | 7 | 2% | 1% | -57% | -90% | -90% |
| USDCAD | 1439 | 1 | 3% | 1% | -94% | -96% | -96% |
| BRENT | 1069 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 557 | 2 | 3% | 1% | -66% | -78% | -76% |
| 30YRRATE | 518 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 515 | 4 | 4% | 2% | -28% | -57% | -57% |
| 5YRRATE | 506 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 139 | 1 | 2% | 1% | -33% | -96% | -96% |
| USDMXN | 33 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34640 | 132 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33135 | 124 | 4% | 2% | -57% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5855 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6405 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 10005 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12724 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5365 | 24 | 7% | 3% | -53% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16330 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16129 | 82 | 4% | 2% | -42% | -86% | -85% |
| Afternoon (12–6pm) | 16751 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18565 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,090 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/25 6:11:54 PM | XRP | DOWN | 3.1 min | +0.351% | — | In play | — |
| 11/25 6:11:38 PM | NEAR | DOWN | 3.4 min | +0.594% | — | In play | — |
| 11/25 6:10:48 PM | PALLADIUM | DOWN | 4.2 min | — | — | In play | — |
| 11/25 6:09:41 PM | BRENT | DOWN | 5.3 min | — | — | In play | — |
| 11/25 5:59:49 PM | XRP | UP | 10 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 11/25 5:59:49 PM | ETH | DOWN | 10 sec | +0.018% | 0¢ | ❌ Lost | $0.00 |
| 11/25 5:59:49 PM | USDCAD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 5:59:30 PM | DOGE | DOWN | 29 sec | +0.044% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 5:58:42 PM | HYPE | UP | 78 sec | -0.276% | 0¢ | ❌ Lost | $0.00 |
| 11/25 5:58:21 PM | NATGAS | UP | 1.6 min | — | 4¢ | ❌ Lost | -$0.15 |
| 11/25 5:58:04 PM | PALLADIUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 5:58:04 PM | PLATINUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 5:57:48 PM | EURUSD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 5:57:34 PM | USDJPY | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 5:57:34 PM | BTC | UP | 2.4 min | -0.230% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 5:57:15 PM | NEAR | DOWN | 2.7 min | +0.565% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 5:56:43 PM | SILVER | UP | 3.3 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/25 5:56:43 PM | GBPUSD | DOWN | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 5:56:27 PM | GOLD | UP | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 5:56:07 PM | ZEC | UP | 3.9 min | -0.779% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 5:55:19 PM | AUDUSD | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 5:44:34 PM | GBPUSD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 5:44:34 PM | PLATINUM | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 5:44:02 PM | ZEC | UP | 58 sec | -0.548% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 5:43:46 PM | SILVER | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 5:43:26 PM | NATGAS | DOWN | 1.6 min | — | 43¢ | ❌ Lost | -$0.15 |
| 11/25 5:43:26 PM | USDCAD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 5:42:38 PM | NEAR | UP | 2.4 min | -0.784% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 5:42:38 PM | DOGE | UP | 2.4 min | -0.423% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 5:42:38 PM | COPPER | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
