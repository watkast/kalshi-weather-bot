# 15-Minute 1¢ Study

*Updated Fri Oct 9, 12:50 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 878 finished bets | 1% | $30.60 | +32% | +3.49¢ | -$18.95 / $49.55 |

*Expect about **76 buys a day** (~$11.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 855 | $20.05 | +22% |
| 5+ min left, hold to the close | 382 | -$0.40 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 878 | -$6.65 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13108 | 13101 | 52 (0%) | 1.07% | -$862.15 (-54%) | Hold to the close: -$862.15 (-54%) |

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
| Volatility model | 8325 | 4.0% | 0.4% (35) | -579% | ❌ Worse |
| Momentum model | 8325 | 4.1% | 0.4% (35) | -613% | ❌ Worse |
| Mean-reversion model | 8325 | 6.7% | 0.4% (35) | -677% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8325 | 35 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1603 | 13 | -6% | -75% | -75% | -72% |
| Volatility model ≥ 5% | 878 | 9 | +32% | -67% | -66% | -63% |
| Volatility model ≥ 10% | 536 | 7 | +92% | -52% | -52% | -47% |
| Momentum model ≥ 2% | 1416 | 11 | -6% | -76% | -78% | -75% |
| Momentum model ≥ 5% | 855 | 8 | +22% | -70% | -72% | -69% |
| Momentum model ≥ 10% | 586 | 6 | +46% | -61% | -62% | -59% |
| Mean-reversion model ≥ 2% | 2906 | 20 | -25% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1966 | 16 | -10% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1289 | 12 | +7% | -81% | -81% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8522 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3386 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1193 | 2% | 2% | 1% | 1% | 1% | 0% |
| **All** | 13101 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 52 | 0% | -$862.15 | -54% | — |
| Sell at 2¢ | 440 | 3% | -$1,433.75 | -90% | 33 sec |
| Sell at 3¢ | 292 | 2% | -$1,434.27 | -90% | 47 sec |
| Sell at 5¢ | 214 | 2% | -$1,409.05 | -89% | 60 sec |
| Sell at 10¢ | 141 | 1% | -$1,335.44 | -84% | 64 sec |
| Sell at 25¢ | 81 | 1% | -$1,224.04 | -77% | 81 sec |
| Sell at 50¢ | 53 | 0% | -$1,092.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 378 | 4 | 10% | 3% | +0% | -82% | -86% |
| 2–5 min | 4235 | 26 | 6% | 3% | -40% | -89% | -89% |
| 1–2 min | 3431 | 13 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 5053 | 9 | 1% | 0% | -74% | -90% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 953 | 6 | 4% | 3% | -24% | -90% | -90% |
| HYPE | 953 | 3 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 951 | 2 | 3% | 1% | -73% | -92% | -92% |
| BNB | 950 | 4 | 4% | 2% | -49% | -91% | -92% |
| ETH | 947 | 7 | 5% | 2% | -9% | -89% | -88% |
| NEAR | 943 | 5 | 6% | 2% | -30% | -73% | -74% |
| BTC | 943 | 4 | 5% | 2% | -44% | -88% | -90% |
| SOL | 942 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 940 | 6 | 2% | 1% | -20% | -82% | -83% |
| GOLD | 563 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 549 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 516 | 3 | 3% | 1% | -34% | -94% | -96% |
| COPPER | 484 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 444 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 416 | 3 | 3% | 2% | -33% | -95% | -93% |
| PALLADIUM | 414 | 1 | 1% | 0% | -77% | -98% | -99% |
| EURUSD | 409 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 387 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 348 | 3 | 1% | 1% | -20% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6609 | 27 | 3% | 2% | -53% | -89% | -89% |
| DOWN (bought NO) | 6492 | 25 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1370 | 8 | 2% | 1% | +1% | -69% | -68% |
| 0.05–0.1% | 1439 | 4 | 3% | 1% | -59% | -92% | -92% |
| 0.1–0.2% | 2173 | 7 | 4% | 2% | -60% | -92% | -92% |
| 0.2–0.5% | 2494 | 13 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 1044 | 5 | 6% | 2% | -51% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3343 | 18 | 4% | 2% | -38% | -85% | -85% |
| Morning (6am–12pm) | 3238 | 17 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 2899 | 8 | 3% | 1% | -67% | -89% | -90% |
| Evening (6pm–12am) | 3621 | 9 | 3% | 1% | -72% | -95% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,030 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/9 12:44:33 PM | PALLADIUM | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:44:33 PM | NATGAS | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:44:17 PM | SILVER | DOWN | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:44:02 PM | PLATINUM | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:44:02 PM | USDJPY | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:43:44 PM | ETH | UP | 75 sec | -0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:43:12 PM | ZEC | UP | 1.8 min | -0.334% | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:43:12 PM | DOGE | UP | 1.8 min | -0.202% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:43:12 PM | XRP | UP | 1.8 min | -0.216% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:42:58 PM | BTC | UP | 2.0 min | -0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:42:26 PM | NEAR | UP | 2.5 min | -0.646% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:42:26 PM | WTI | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:42:10 PM | SOL | UP | 2.8 min | -0.256% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:42:10 PM | BNB | UP | 2.8 min | -0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:40:17 PM | HYPE | UP | 4.7 min | -0.378% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:29:19 PM | EURUSD | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:29:19 PM | XRP | UP | 41 sec | -0.108% | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:29:03 PM | PALLADIUM | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:28:47 PM | USDJPY | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:28:31 PM | SILVER | UP | 89 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:28:31 PM | GOLD | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:28:15 PM | PLATINUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:28:15 PM | SOL | UP | 1.8 min | -0.138% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:27:10 PM | NEAR | UP | 2.8 min | -0.566% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:27:10 PM | ETH | UP | 2.8 min | -0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:26:22 PM | DOGE | UP | 3.6 min | -0.273% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:26:06 PM | BTC | UP | 3.9 min | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:26:06 PM | ZEC | UP | 3.9 min | -0.432% | 2¢ | ❌ Lost | -$0.15 |
| 10/9 12:26:06 PM | BNB | UP | 3.9 min | -0.210% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:24:13 PM | HYPE | UP | 5.8 min | -0.505% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
