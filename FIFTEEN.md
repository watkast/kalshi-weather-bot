# 15-Minute 1¢ Study

*Updated Fri Oct 9, 5:36 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 901 finished bets | 1% | $41.75 | +42% | +4.63¢ | -$5.70 / $47.45 |

*Expect about **77 buys a day** (~$11.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 878 | $17.50 | +19% |
| 5+ min left, hold to the close | 385 | -$0.85 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 901 | -$2.75 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13333 | 13326 | 53 (0%) | 1.07% | -$875.45 (-54%) | Hold to the close: -$875.45 (-54%) |

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
| Volatility model | 8493 | 4.0% | 0.4% (36) | -582% | ❌ Worse |
| Momentum model | 8493 | 4.1% | 0.4% (36) | -616% | ❌ Worse |
| Mean-reversion model | 8493 | 6.7% | 0.4% (36) | -680% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8493 | 36 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1640 | 14 | -1% | -75% | -75% | -72% |
| Volatility model ≥ 5% | 901 | 10 | +42% | -67% | -66% | -63% |
| Volatility model ≥ 10% | 553 | 8 | +111% | -52% | -52% | -48% |
| Momentum model ≥ 2% | 1454 | 11 | -9% | -77% | -78% | -76% |
| Momentum model ≥ 5% | 878 | 8 | +19% | -71% | -72% | -69% |
| Momentum model ≥ 10% | 601 | 6 | +43% | -62% | -63% | -60% |
| Mean-reversion model ≥ 2% | 2960 | 21 | -23% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1998 | 17 | -6% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1313 | 13 | +14% | -81% | -81% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8691 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3432 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 13326 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 53 | 0% | -$875.45 | -54% | — |
| Sell at 2¢ | 446 | 3% | -$1,459.49 | -90% | 33 sec |
| Sell at 3¢ | 297 | 2% | -$1,459.62 | -90% | 47 sec |
| Sell at 5¢ | 218 | 2% | -$1,433.75 | -89% | 56 sec |
| Sell at 10¢ | 143 | 1% | -$1,360.12 | -84% | 64 sec |
| Sell at 25¢ | 82 | 1% | -$1,248.03 | -77% | 82 sec |
| Sell at 50¢ | 54 | 0% | -$1,112.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 381 | 4 | 10% | 3% | -0% | -82% | -86% |
| 2–5 min | 4312 | 27 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 3474 | 13 | 3% | 2% | -60% | -94% | -94% |
| Under 1 min | 5155 | 9 | 1% | 0% | -74% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 972 | 6 | 4% | 3% | -25% | -90% | -90% |
| HYPE | 971 | 3 | 5% | 2% | -62% | -90% | -88% |
| DOGE | 970 | 2 | 3% | 2% | -74% | -92% | -92% |
| BNB | 970 | 5 | 4% | 2% | -38% | -90% | -91% |
| ETH | 965 | 7 | 5% | 2% | -11% | -89% | -89% |
| NEAR | 962 | 5 | 6% | 2% | -32% | -73% | -74% |
| BTC | 961 | 4 | 5% | 2% | -45% | -88% | -91% |
| SOL | 961 | 0 | 2% | 1% | -100% | -94% | -93% |
| XRP | 959 | 6 | 2% | 1% | -22% | -83% | -83% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 526 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 422 | 3 | 3% | 2% | -34% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6711 | 27 | 3% | 2% | -54% | -89% | -89% |
| DOWN (bought NO) | 6615 | 26 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1408 | 8 | 2% | 1% | -2% | -70% | -69% |
| 0.05–0.1% | 1476 | 5 | 3% | 1% | -50% | -92% | -92% |
| 0.1–0.2% | 2222 | 7 | 4% | 2% | -61% | -92% | -92% |
| 0.2–0.5% | 2530 | 13 | 5% | 3% | -44% | -89% | -88% |
| Over 0.5% | 1052 | 5 | 6% | 2% | -51% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3343 | 18 | 4% | 2% | -38% | -85% | -85% |
| Morning (6am–12pm) | 3238 | 17 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3124 | 9 | 3% | 1% | -66% | -90% | -90% |
| Evening (6pm–12am) | 3621 | 9 | 3% | 1% | -72% | -95% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,048 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/9 5:29:59 PM | BTC | UP | 0 sec | -0.009% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:29:59 PM | WTI | DOWN | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 5:29:59 PM | HYPE | DOWN | 0 sec | -0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/9 5:29:11 PM | ZEC | DOWN | 49 sec | +0.089% | 0¢ | ❌ Lost | $0.00 |
| 10/9 5:28:53 PM | XRP | DOWN | 67 sec | +0.036% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:28:53 PM | DOGE | DOWN | 67 sec | +0.008% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:28:37 PM | SOL | DOWN | 83 sec | +0.088% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:28:06 PM | ETH | DOWN | 1.9 min | +0.055% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:26:44 PM | BNB | DOWN | 3.2 min | +0.042% | 3¢ | ❌ Lost | -$0.15 |
| 10/9 5:25:56 PM | NEAR | UP | 4.1 min | -1.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:14:47 PM | BTC | UP | 13 sec | -0.019% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:14:47 PM | BNB | DOWN | 13 sec | -0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:14:31 PM | HYPE | UP | 29 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/9 5:14:15 PM | XRP | UP | 45 sec | -0.093% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:13:58 PM | SOL | UP | 61 sec | -0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:13:42 PM | NEAR | DOWN | 77 sec | +0.564% | 0¢ | ❌ Lost | $0.00 |
| 10/9 5:13:42 PM | ZEC | UP | 77 sec | -0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:13:10 PM | ETH | UP | 1.8 min | -0.074% | 1¢ | ❌ Lost | $0.00 |
| 10/9 5:11:33 PM | DOGE | UP | 3.4 min | -0.193% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:59:44 PM | NEAR | UP | 15 sec | -0.166% | 0¢ | ❌ Lost | $0.00 |
| 10/9 4:59:28 PM | DOGE | UP | 31 sec | -0.067% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:59:28 PM | ETH | UP | 31 sec | -0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 4:59:28 PM | ZEC | UP | 31 sec | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/9 4:59:12 PM | XRP | DOWN | 47 sec | +0.036% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:58:40 PM | SOL | UP | 80 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/9 4:57:19 PM | BNB | DOWN | 2.7 min | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:43:36 PM | XRP | DOWN | 84 sec | +0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/9 4:41:59 PM | DOGE | DOWN | 3.0 min | +0.171% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:41:59 PM | BNB | DOWN | 3.0 min | +0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 4:41:59 PM | HYPE | DOWN | 3.0 min | +0.121% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
