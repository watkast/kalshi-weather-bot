# 15-Minute 1¢ Study

*Updated Wed Oct 28, 6:34 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2968 finished bets | 1% | $85.50 | +26% | +2.88¢ | $87.60 / -$2.10 |

*Expect about **98 buys a day** (~$14.72/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2751 | $47.90 | +16% |
| Volatility model ≥ 2%, hold to the close | 5496 | $15.95 | +2% |
| Momentum model ≥ 2%, hold to the close | 4548 | -$53.65 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 36254 | 36246 | 138 (0%) | 1.07% | -$2,487.30 (-56%) | Hold to the close: -$2,487.30 (-56%) |

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
| Volatility model | 22686 | 4.7% | 0.4% (92) | -667% | ❌ Worse |
| Momentum model | 22686 | 4.6% | 0.4% (92) | -692% | ❌ Worse |
| Mean-reversion model | 22686 | 8.0% | 0.4% (92) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22686 | 92 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5496 | 49 | +2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2968 | 30 | +26% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1686 | 19 | +59% | -68% | -66% | -64% |
| Momentum model ≥ 2% | 4548 | 34 | -10% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 2751 | 25 | +16% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1808 | 17 | +30% | -72% | -71% | -68% |
| Mean-reversion model ≥ 2% | 9245 | 63 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6493 | 53 | -10% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4343 | 38 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22886 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8633 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4727 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 36246 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,487.30 | -56% | — |
| Sell at 2¢ | 1373 | 4% | -$3,866.32 | -87% | 47 sec |
| Sell at 3¢ | 941 | 3% | -$3,856.31 | -87% | 48 sec |
| Sell at 5¢ | 654 | 2% | -$3,798.20 | -86% | 62 sec |
| Sell at 10¢ | 401 | 1% | -$3,641.99 | -82% | 65 sec |
| Sell at 25¢ | 215 | 1% | -$3,357.65 | -76% | 83 sec |
| Sell at 50¢ | 142 | 0% | -$3,026.80 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1615 | 8 | 11% | 4% | -53% | -81% | -82% |
| 2–5 min | 11582 | 66 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 9197 | 32 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 13848 | 32 | 1% | 0% | -67% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2563 | 12 | 5% | 2% | -40% | -89% | -88% |
| HYPE | 2556 | 8 | 5% | 3% | -61% | -89% | -87% |
| BNB | 2554 | 15 | 5% | 2% | -27% | -85% | -83% |
| SOL | 2549 | 7 | 3% | 2% | -66% | -92% | -92% |
| ETH | 2543 | 11 | 6% | 3% | -48% | -86% | -85% |
| DOGE | 2540 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2531 | 11 | 3% | 1% | -46% | -89% | -89% |
| NEAR | 2525 | 12 | 5% | 2% | -38% | -82% | -82% |
| BTC | 2525 | 13 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1368 | 5 | 4% | 2% | -56% | -81% | -83% |
| SILVER | 1335 | 6 | 4% | 2% | -47% | -82% | -81% |
| WTI | 1318 | 4 | 3% | 1% | -64% | -93% | -94% |
| PLATINUM | 1184 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1130 | 4 | 1% | 1% | -67% | -73% | -73% |
| EURUSD | 1107 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1088 | 6 | 2% | 1% | -49% | -79% | -79% |
| GBPUSD | 1048 | 2 | 2% | 1% | -82% | -96% | -97% |
| PALLADIUM | 1047 | 2 | 1% | 0% | -82% | -89% | -89% |
| USDJPY | 1031 | 5 | 2% | 1% | -55% | -97% | -96% |
| AUDUSD | 586 | 4 | 1% | 1% | -36% | -82% | -81% |
| USDCAD | 549 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 163 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 110 | 0 | 4% | 0% | -100% | -94% | -93% |
| 30YRRATE | 103 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 99 | 1 | 3% | 1% | -6% | -0% | -0% |
| 5YRRATE | 94 | 1 | 4% | 2% | -1% | -93% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18341 | 77 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 17905 | 61 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3780 | 19 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3942 | 14 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 5956 | 22 | 4% | 2% | -54% | -90% | -89% |
| 0.2–0.5% | 6725 | 29 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2479 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 8785 | 42 | 4% | 2% | -46% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,610 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 6:29:36 AM | SOL | DOWN | 24 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/28 6:29:36 AM | AUDUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:29:36 AM | DOGE | DOWN | 24 sec | +0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/28 6:29:20 AM | BTC | UP | 40 sec | -0.052% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:29:20 AM | WTI | DOWN | 40 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 6:29:20 AM | EURUSD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:29:20 AM | HYPE | DOWN | 40 sec | -0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/28 6:29:20 AM | ETH | DOWN | 40 sec | +0.064% | 0¢ | ❌ Lost | $0.00 |
| 10/28 6:29:05 AM | NEAR | DOWN | 54 sec | +0.197% | 0¢ | ❌ Lost | $0.00 |
| 10/28 6:29:05 AM | USDCAD | UP | 54 sec | — | 21¢ | ❌ Lost | -$0.15 |
| 10/28 6:28:49 AM | ZEC | DOWN | 70 sec | +0.250% | 0¢ | ❌ Lost | $0.00 |
| 10/28 6:28:33 AM | XRP | DOWN | 86 sec | +0.167% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:28:33 AM | GBPUSD | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:27:45 AM | PALLADIUM | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:27:45 AM | COPPER | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:27:13 AM | PLATINUM | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:27:13 AM | USDJPY | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:27:13 AM | SILVER | DOWN | 2.8 min | — | 3¢ | ❌ Lost | -$0.15 |
| 10/28 6:26:24 AM | NATGAS | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:25:52 AM | GOLD | DOWN | 4.1 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/28 6:24:47 AM | 30YRRATE | UP | 5.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:14:47 AM | PLATINUM | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:14:31 AM | SILVER | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:14:15 AM | AUDUSD | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:14:15 AM | USDCAD | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:13:41 AM | BRENT | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:13:41 AM | 2YRRATE | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:13:10 AM | 30YRRATE | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:13:10 AM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 6:13:10 AM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
