# 15-Minute 1¢ Study

*Updated Fri Oct 9, 6:58 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 906 finished bets | 1% | $41.45 | +42% | +4.58¢ | -$5.85 / $47.30 |

*Expect about **77 buys a day** (~$11.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 883 | $17.20 | +18% |
| 5+ min left, hold to the close | 385 | -$0.85 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 906 | -$3.05 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13382 | 13374 | 53 (0%) | 1.07% | -$880.55 (-54%) | Hold to the close: -$880.55 (-54%) |

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
| Volatility model | 8537 | 4.0% | 0.4% (36) | -582% | ❌ Worse |
| Momentum model | 8537 | 4.1% | 0.4% (36) | -615% | ❌ Worse |
| Mean-reversion model | 8537 | 6.7% | 0.4% (36) | -681% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8537 | 36 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1648 | 14 | -2% | -75% | -75% | -72% |
| Volatility model ≥ 5% | 906 | 10 | +42% | -68% | -66% | -63% |
| Volatility model ≥ 10% | 557 | 8 | +110% | -52% | -53% | -48% |
| Momentum model ≥ 2% | 1460 | 11 | -9% | -77% | -78% | -76% |
| Momentum model ≥ 5% | 883 | 8 | +18% | -71% | -72% | -69% |
| Momentum model ≥ 10% | 603 | 6 | +42% | -62% | -63% | -60% |
| Mean-reversion model ≥ 2% | 2977 | 21 | -23% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2009 | 17 | -7% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1319 | 13 | +13% | -81% | -81% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8735 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3436 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 13374 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 53 | 0% | -$880.55 | -54% | — |
| Sell at 2¢ | 448 | 3% | -$1,464.07 | -90% | 33 sec |
| Sell at 3¢ | 299 | 2% | -$1,463.94 | -90% | 47 sec |
| Sell at 5¢ | 219 | 2% | -$1,438.20 | -89% | 51 sec |
| Sell at 10¢ | 144 | 1% | -$1,363.91 | -84% | 64 sec |
| Sell at 25¢ | 82 | 1% | -$1,253.13 | -77% | 82 sec |
| Sell at 50¢ | 54 | 0% | -$1,118.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 381 | 4 | 10% | 3% | -0% | -82% | -86% |
| 2–5 min | 4321 | 27 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 3492 | 13 | 3% | 2% | -60% | -94% | -94% |
| Under 1 min | 5176 | 9 | 1% | 0% | -75% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 977 | 6 | 4% | 3% | -25% | -90% | -90% |
| HYPE | 976 | 3 | 5% | 2% | -62% | -90% | -88% |
| DOGE | 975 | 2 | 3% | 2% | -74% | -92% | -92% |
| BNB | 975 | 5 | 4% | 2% | -38% | -90% | -91% |
| ETH | 970 | 7 | 5% | 2% | -11% | -89% | -89% |
| NEAR | 967 | 5 | 5% | 2% | -32% | -73% | -74% |
| SOL | 966 | 0 | 2% | 1% | -100% | -94% | -93% |
| BTC | 965 | 4 | 5% | 2% | -46% | -88% | -91% |
| XRP | 964 | 6 | 2% | 1% | -22% | -82% | -82% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 526 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 426 | 3 | 3% | 2% | -34% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6728 | 27 | 3% | 2% | -54% | -89% | -89% |
| DOWN (bought NO) | 6646 | 26 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1427 | 8 | 2% | 1% | -3% | -70% | -69% |
| 0.05–0.1% | 1486 | 5 | 3% | 1% | -51% | -92% | -92% |
| 0.1–0.2% | 2231 | 7 | 4% | 2% | -61% | -92% | -92% |
| 0.2–0.5% | 2534 | 13 | 5% | 3% | -44% | -89% | -88% |
| Over 0.5% | 1054 | 5 | 6% | 2% | -51% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3343 | 18 | 4% | 2% | -38% | -85% | -85% |
| Morning (6am–12pm) | 3238 | 17 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3143 | 9 | 3% | 1% | -66% | -90% | -90% |
| Evening (6pm–12am) | 3650 | 9 | 3% | 1% | -72% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,058 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/9 6:58:07 PM | NEAR | DOWN | 1.9 min | +0.277% | — | In play | — |
| 10/9 6:44:41 PM | NATGAS | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:44:41 PM | ZEC | DOWN | 18 sec | +0.095% | 0¢ | ❌ Lost | $0.00 |
| 10/9 6:44:41 PM | DOGE | DOWN | 18 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/9 6:44:25 PM | ETH | UP | 34 sec | -0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:44:25 PM | XRP | DOWN | 34 sec | +0.036% | 13¢ | ❌ Lost | -$0.15 |
| 10/9 6:43:35 PM | BTC | UP | 85 sec | -0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 6:43:35 PM | BNB | UP | 85 sec | -0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 6:43:04 PM | SOL | DOWN | 1.9 min | +0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 6:43:04 PM | NEAR | UP | 1.9 min | -0.539% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 6:42:47 PM | HYPE | UP | 2.2 min | -0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 6:29:42 PM | NATGAS | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:29:26 PM | BTC | UP | 33 sec | -0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 6:29:10 PM | HYPE | DOWN | 50 sec | +0.043% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:29:10 PM | SOL | DOWN | 50 sec | +0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 6:29:10 PM | NEAR | DOWN | 50 sec | +0.089% | 0¢ | ❌ Lost | $0.00 |
| 10/9 6:28:21 PM | XRP | DOWN | 1.6 min | +0.150% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:28:21 PM | DOGE | DOWN | 1.6 min | +0.168% | 0¢ | ❌ Lost | $0.00 |
| 10/9 6:28:21 PM | ETH | DOWN | 1.6 min | +0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 6:27:33 PM | ZEC | DOWN | 2.4 min | +0.271% | 4¢ | ❌ Lost | -$0.15 |
| 10/9 6:27:33 PM | BNB | DOWN | 2.4 min | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/9 6:14:31 PM | SOL | DOWN | 28 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/9 6:14:15 PM | NATGAS | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:13:59 PM | ETH | DOWN | 61 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/9 6:13:43 PM | BNB | DOWN | 77 sec | +0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/9 6:13:27 PM | HYPE | DOWN | 1.6 min | +0.119% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:13:27 PM | DOGE | DOWN | 1.6 min | +0.216% | 0¢ | ❌ Lost | $0.00 |
| 10/9 6:13:10 PM | NEAR | DOWN | 1.8 min | +0.483% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 6:12:37 PM | ZEC | DOWN | 2.4 min | +0.184% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:12:05 PM | XRP | DOWN | 2.9 min | +0.136% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
