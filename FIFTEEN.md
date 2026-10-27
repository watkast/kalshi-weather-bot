# 15-Minute 1¢ Study

*Updated Tue Oct 27, 4:17 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2882 finished bets | 1% | $94.80 | +29% | +3.29¢ | $92.55 / $2.25 |

*Expect about **97 buys a day** (~$14.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2688 | $54.20 | +18% |
| Volatility model ≥ 2%, hold to the close | 5353 | $18.00 | +3% |
| Momentum model ≥ 2%, hold to the close | 4439 | -$41.80 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 35237 | 35229 | 135 (0%) | 1.07% | -$2,401.95 (-56%) | Hold to the close: -$2,401.95 (-56%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 22202 | 4.7% | 0.4% (91) | -662% | ❌ Worse |
| Momentum model | 22202 | 4.6% | 0.4% (91) | -687% | ❌ Worse |
| Mean-reversion model | 22202 | 8.0% | 0.4% (91) | -803% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22202 | 91 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5353 | 48 | +3% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2882 | 30 | +29% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1638 | 19 | +64% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4439 | 34 | -8% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2688 | 25 | +18% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1759 | 17 | +33% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 9021 | 62 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6321 | 52 | -9% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4218 | 37 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22402 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8328 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4499 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 35229 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 135 | 0% | -$2,401.95 | -56% | — |
| Sell at 2¢ | 1333 | 4% | -$3,749.37 | -87% | 47 sec |
| Sell at 3¢ | 909 | 3% | -$3,741.44 | -87% | 48 sec |
| Sell at 5¢ | 629 | 2% | -$3,687.10 | -86% | 62 sec |
| Sell at 10¢ | 386 | 1% | -$3,534.29 | -82% | 65 sec |
| Sell at 25¢ | 209 | 1% | -$3,250.16 | -76% | 1.5 min |
| Sell at 50¢ | 139 | 0% | -$2,919.70 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1571 | 8 | 11% | 4% | -51% | -81% | -82% |
| 2–5 min | 11282 | 64 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 8936 | 31 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 13436 | 32 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2508 | 12 | 5% | 2% | -39% | -89% | -88% |
| HYPE | 2501 | 8 | 5% | 3% | -61% | -89% | -87% |
| BNB | 2500 | 15 | 5% | 2% | -25% | -84% | -83% |
| SOL | 2497 | 7 | 4% | 2% | -65% | -92% | -91% |
| ETH | 2489 | 11 | 6% | 3% | -47% | -86% | -85% |
| DOGE | 2486 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2476 | 10 | 3% | 1% | -50% | -89% | -89% |
| NEAR | 2475 | 12 | 5% | 2% | -37% | -82% | -82% |
| BTC | 2470 | 13 | 5% | 2% | -29% | -88% | -89% |
| GOLD | 1323 | 5 | 4% | 2% | -55% | -81% | -83% |
| SILVER | 1292 | 6 | 4% | 2% | -46% | -82% | -82% |
| WTI | 1275 | 4 | 3% | 1% | -63% | -93% | -95% |
| PLATINUM | 1146 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1097 | 4 | 1% | 1% | -66% | -72% | -72% |
| EURUSD | 1069 | 3 | 2% | 1% | -74% | -87% | -87% |
| NATGAS | 1057 | 6 | 2% | 1% | -47% | -79% | -78% |
| PALLADIUM | 1012 | 2 | 1% | 0% | -82% | -89% | -89% |
| GBPUSD | 1007 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 994 | 5 | 1% | 1% | -53% | -98% | -97% |
| AUDUSD | 549 | 3 | 1% | 1% | -49% | -81% | -80% |
| USDCAD | 510 | 0 | 1% | 0% | -100% | -98% | -98% |
| BRENT | 126 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 101 | 0 | 4% | 0% | -100% | -93% | -92% |
| 30YRRATE | 92 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 89 | 1 | 3% | 1% | +5% | +11% | +11% |
| 5YRRATE | 88 | 1 | 5% | 2% | +6% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17821 | 75 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 17408 | 60 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3668 | 19 | 2% | 1% | -12% | -81% | -80% |
| 0.05–0.1% | 3850 | 14 | 3% | 2% | -46% | -92% | -91% |
| 0.1–0.2% | 5825 | 21 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6597 | 29 | 7% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2458 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8305 | 28 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,640 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 4:14:35 PM | NATGAS | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:14:35 PM | ETH | UP | 25 sec | -0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:14:35 PM | NEAR | UP | 25 sec | -0.269% | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:14:35 PM | HYPE | UP | 25 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:14:19 PM | USDJPY | DOWN | 41 sec | — | 7¢ | ❌ Lost | -$0.15 |
| 10/27 4:14:19 PM | DOGE | UP | 41 sec | -0.108% | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:14:19 PM | XRP | DOWN | 41 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:14:04 PM | BRENT | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:14:04 PM | EURUSD | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:13:48 PM | WTI | UP | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:13:48 PM | ZEC | UP | 72 sec | -0.235% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:13:32 PM | SOL | UP | 88 sec | -0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:12:43 PM | BNB | UP | 2.3 min | -0.111% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 3:59:48 PM | BRENT | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:59:48 PM | EURUSD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:59:32 PM | XRP | DOWN | 27 sec | +0.030% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 3:59:16 PM | ETH | UP | 44 sec | -0.096% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:59:16 PM | DOGE | UP | 44 sec | -0.089% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 3:58:58 PM | GBPUSD | DOWN | 62 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 3:58:58 PM | BTC | UP | 62 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/27 3:58:42 PM | SOL | UP | 78 sec | -0.135% | 0¢ | ❌ Lost | $0.00 |
| 10/27 3:57:22 PM | HYPE | UP | 2.6 min | -0.264% | 0¢ | ❌ Lost | $0.00 |
| 10/27 3:57:05 PM | BNB | UP | 2.9 min | -0.150% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 3:44:36 PM | GBPUSD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:44:20 PM | WTI | DOWN | 39 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 3:43:32 PM | USDJPY | DOWN | 87 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 3:43:16 PM | AUDUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:39:47 PM | DOGE | DOWN | 5.2 min | +0.525% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 3:38:26 PM | XRP | DOWN | 6.5 min | +0.836% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 3:38:26 PM | BTC | DOWN | 6.5 min | +0.646% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
