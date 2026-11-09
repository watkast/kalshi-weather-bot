# 15-Minute 1¢ Study

*Updated Mon Nov 9, 4:39 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4117 finished bets | 1% | $186.35 | +41% | +4.53¢ | $91.15 / $95.20 |

*Expect about **96 buys a day** (~$14.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3825 | $104.00 | +25% |
| Volatility model ≥ 2%, hold to the close | 7533 | $73.40 | +8% |
| Momentum model ≥ 2%, hold to the close | 6231 | -$1.35 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51336 | 51319 | 195 (0%) | 1.07% | -$3,517.05 (-56%) | Hold to the close: -$3,517.05 (-56%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31232 | 4.8% | 0.4% (124) | -687% | ❌ Worse |
| Momentum model | 31232 | 4.6% | 0.4% (124) | -712% | ❌ Worse |
| Mean-reversion model | 31232 | 8.1% | 0.4% (124) | -831% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31232 | 124 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7533 | 70 | +8% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4117 | 46 | +41% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2370 | 28 | +69% | -61% | -60% | -56% |
| Momentum model ≥ 2% | 6231 | 51 | -0% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3825 | 37 | +25% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 2510 | 25 | +40% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 12918 | 90 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9062 | 77 | -6% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6054 | 56 | +5% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31437 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12124 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7758 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51319 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 195 | 0% | -$3,517.05 | -56% | — |
| Sell at 2¢ | 2035 | 4% | -$5,437.95 | -87% | 47 sec |
| Sell at 3¢ | 1384 | 3% | -$5,427.29 | -87% | 48 sec |
| Sell at 5¢ | 969 | 2% | -$5,309.20 | -85% | 62 sec |
| Sell at 10¢ | 587 | 1% | -$5,086.08 | -81% | 65 sec |
| Sell at 25¢ | 308 | 1% | -$4,723.57 | -76% | 83 sec |
| Sell at 50¢ | 201 | 0% | -$4,288.30 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2543 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16559 | 89 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12978 | 44 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 19227 | 50 | 1% | 0% | -63% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3522 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3516 | 15 | 4% | 2% | -46% | -87% | -87% |
| HYPE | 3507 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3501 | 19 | 5% | 2% | -32% | -86% | -85% |
| DOGE | 3498 | 7 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3492 | 14 | 7% | 3% | -51% | -81% | -81% |
| NEAR | 3471 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3470 | 16 | 5% | 2% | -37% | -87% | -89% |
| XRP | 3460 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1843 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1815 | 6 | 4% | 2% | -60% | -91% | -92% |
| SILVER | 1792 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1625 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1558 | 5 | 2% | 1% | -70% | -90% | -89% |
| COPPER | 1521 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1483 | 8 | 2% | 1% | -50% | -77% | -77% |
| GBPUSD | 1480 | 5 | 2% | 1% | -68% | -96% | -96% |
| PALLADIUM | 1461 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1459 | 6 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 1019 | 5 | 2% | 1% | -54% | -87% | -88% |
| USDCAD | 986 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 584 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 331 | 2 | 5% | 2% | -44% | -64% | -62% |
| 2YRRATE | 314 | 4 | 4% | 2% | +19% | -33% | -31% |
| 30YRRATE | 309 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 291 | 2 | 4% | 2% | -36% | -92% | -95% |
| INX | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26008 | 100 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 25311 | 95 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5070 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5373 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8078 | 27 | 5% | 2% | -58% | -89% | -89% |
| 0.2–0.5% | 9383 | 40 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 3525 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12671 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12425 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12421 | 53 | 4% | 2% | -50% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,908 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 4:29:50 PM | XRP | DOWN | 10 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:29:50 PM | ZEC | DOWN | 10 sec | +0.077% | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:29:34 PM | PALLADIUM | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:29:34 PM | HYPE | DOWN | 26 sec | +0.083% | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:29:34 PM | GBPUSD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:29:19 PM | BRENT | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:29:19 PM | NEAR | DOWN | 40 sec | +0.097% | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:29:19 PM | DOGE | DOWN | 40 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:28:55 PM | SILVER | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:28:55 PM | SOL | DOWN | 65 sec | +0.099% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:28:39 PM | WTI | DOWN | 81 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:28:39 PM | BNB | DOWN | 81 sec | +0.007% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:28:39 PM | NATGAS | UP | 81 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:28:39 PM | GOLD | UP | 81 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:28:23 PM | PLATINUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:28:08 PM | COPPER | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:27:50 PM | ETH | DOWN | 2.2 min | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:27:03 PM | BTC | DOWN | 2.9 min | +0.151% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:14:17 PM | WTI | UP | 43 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:13:59 PM | BRENT | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:13:59 PM | GBPUSD | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:13:12 PM | DOGE | UP | 1.8 min | -0.167% | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:12:22 PM | EURUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:11:01 PM | HYPE | UP | 4.0 min | -0.499% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:11:01 PM | ETH | UP | 4.0 min | -0.272% | 2¢ | ❌ Lost | -$0.15 |
| 11/9 4:10:27 PM | BTC | UP | 4.5 min | -0.231% | 2¢ | ❌ Lost | -$0.15 |
| 11/9 4:10:27 PM | XRP | UP | 4.5 min | -0.425% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:10:11 PM | NEAR | UP | 4.8 min | -0.912% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:10:11 PM | SOL | UP | 4.8 min | -0.398% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:09:56 PM | BNB | UP | 5.0 min | -0.155% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
