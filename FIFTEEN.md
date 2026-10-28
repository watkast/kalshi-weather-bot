# 15-Minute 1¢ Study

*Updated Wed Oct 28, 9:31 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2984 finished bets | 1% | $84.15 | +25% | +2.82¢ | $86.85 / -$2.70 |

*Expect about **98 buys a day** (~$14.74/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2770 | $45.80 | +15% |
| Volatility model ≥ 2%, hold to the close | 5530 | $12.20 | +2% |
| Momentum model ≥ 2%, hold to the close | 4572 | -$56.05 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 36497 | 36489 | 138 (0%) | 1.07% | -$2,518.20 (-57%) | Hold to the close: -$2,518.20 (-57%) |

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
| Volatility model | 22794 | 4.7% | 0.4% (92) | -668% | ❌ Worse |
| Momentum model | 22794 | 4.6% | 0.4% (92) | -691% | ❌ Worse |
| Mean-reversion model | 22794 | 8.0% | 0.4% (92) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22794 | 92 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5530 | 49 | +2% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 2984 | 30 | +25% | -76% | -74% | -72% |
| Volatility model ≥ 10% | 1692 | 19 | +59% | -68% | -66% | -64% |
| Momentum model ≥ 2% | 4572 | 34 | -11% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 2770 | 25 | +15% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1816 | 17 | +29% | -72% | -71% | -68% |
| Mean-reversion model ≥ 2% | 9302 | 63 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6528 | 53 | -10% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4363 | 38 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22994 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8696 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4799 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 36489 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,518.20 | -57% | — |
| Sell at 2¢ | 1387 | 4% | -$3,893.58 | -87% | 47 sec |
| Sell at 3¢ | 951 | 3% | -$3,883.31 | -87% | 48 sec |
| Sell at 5¢ | 661 | 2% | -$3,824.55 | -86% | 62 sec |
| Sell at 10¢ | 403 | 1% | -$3,670.27 | -82% | 65 sec |
| Sell at 25¢ | 216 | 1% | -$3,385.24 | -76% | 83 sec |
| Sell at 50¢ | 142 | 0% | -$3,057.70 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1633 | 8 | 11% | 4% | -53% | -80% | -81% |
| 2–5 min | 11657 | 66 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 9250 | 32 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 13945 | 32 | 1% | 0% | -67% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2575 | 12 | 5% | 2% | -40% | -88% | -88% |
| HYPE | 2568 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2566 | 15 | 5% | 2% | -27% | -85% | -83% |
| SOL | 2561 | 7 | 3% | 2% | -66% | -92% | -92% |
| ETH | 2555 | 11 | 6% | 3% | -48% | -85% | -85% |
| DOGE | 2552 | 5 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2543 | 11 | 3% | 1% | -47% | -89% | -89% |
| NEAR | 2537 | 12 | 5% | 2% | -39% | -82% | -82% |
| BTC | 2537 | 13 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1375 | 5 | 4% | 2% | -56% | -81% | -83% |
| SILVER | 1345 | 6 | 4% | 2% | -47% | -82% | -81% |
| WTI | 1325 | 4 | 3% | 1% | -64% | -93% | -94% |
| PLATINUM | 1194 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1135 | 4 | 1% | 1% | -67% | -73% | -73% |
| EURUSD | 1114 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1099 | 6 | 2% | 1% | -49% | -79% | -79% |
| GBPUSD | 1059 | 2 | 2% | 1% | -82% | -96% | -96% |
| PALLADIUM | 1056 | 2 | 1% | 0% | -82% | -89% | -89% |
| USDJPY | 1037 | 5 | 2% | 1% | -55% | -97% | -96% |
| AUDUSD | 593 | 4 | 1% | 1% | -37% | -82% | -81% |
| USDCAD | 560 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 167 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 117 | 0 | 3% | 0% | -100% | -94% | -93% |
| 30YRRATE | 111 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 107 | 1 | 3% | 1% | -13% | -8% | -8% |
| 5YRRATE | 101 | 1 | 4% | 2% | -8% | -93% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18464 | 77 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 18025 | 61 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3794 | 19 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3957 | 14 | 3% | 2% | -47% | -92% | -92% |
| 0.1–0.2% | 5981 | 22 | 4% | 2% | -54% | -90% | -89% |
| 0.2–0.5% | 6760 | 29 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2498 | 10 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9028 | 42 | 4% | 2% | -47% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,586 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 9:29:49 AM | GBPUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:29:49 AM | 30YRRATE | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:29:49 AM | 5YRRATE | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:29:33 AM | BNB | DOWN | 26 sec | +0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:29:33 AM | 2YRRATE | UP | 26 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 9:29:33 AM | PALLADIUM | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:29:33 AM | USDCAD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:29:17 AM | PLATINUM | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:29:17 AM | DOGE | DOWN | 42 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:29:17 AM | XRP | DOWN | 42 sec | +0.030% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:29:17 AM | ZEC | UP | 42 sec | -0.136% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:29:17 AM | 10YRRATE | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:28:43 AM | WTI | DOWN | 77 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 9:28:43 AM | ETH | DOWN | 77 sec | +0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:28:43 AM | BTC | DOWN | 77 sec | +0.054% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:28:27 AM | HYPE | DOWN | 1.6 min | +0.137% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:28:27 AM | NEAR | DOWN | 1.6 min | +0.201% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:28:11 AM | SOL | DOWN | 1.8 min | +0.142% | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:23:08 AM | NATGAS | UP | 6.8 min | — | 3¢ | ❌ Lost | -$0.15 |
| 10/28 9:14:57 AM | SILVER | DOWN | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:14:57 AM | PALLADIUM | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:14:25 AM | ZEC | DOWN | 34 sec | +0.061% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:14:25 AM | NATGAS | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:14:09 AM | HYPE | DOWN | 51 sec | +0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 9:13:53 AM | GBPUSD | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:13:53 AM | GOLD | DOWN | 66 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 9:13:37 AM | BNB | DOWN | 82 sec | +0.090% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:13:37 AM | XRP | DOWN | 82 sec | +0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 9:13:37 AM | SOL | DOWN | 82 sec | +0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 9:13:37 AM | BTC | DOWN | 82 sec | +0.099% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
