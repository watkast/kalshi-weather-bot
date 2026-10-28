# 15-Minute 1¢ Study

*Updated Wed Oct 28, 12:47 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2932 finished bets | 1% | $89.40 | +27% | +3.05¢ | $89.40 / -$0.00 |

*Expect about **98 buys a day** (~$14.66/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2726 | $50.30 | +17% |
| Volatility model ≥ 2%, hold to the close | 5440 | $21.80 | +3% |
| Momentum model ≥ 2%, hold to the close | 4503 | -$49.15 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 35819 | 35811 | 137 (0%) | 1.07% | -$2,446.40 (-56%) | Hold to the close: -$2,446.40 (-56%) |

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
| Volatility model | 22496 | 4.7% | 0.4% (92) | -664% | ❌ Worse |
| Momentum model | 22496 | 4.6% | 0.4% (92) | -689% | ❌ Worse |
| Mean-reversion model | 22496 | 8.0% | 0.4% (92) | -806% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22496 | 92 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5440 | 49 | +3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2932 | 30 | +27% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1666 | 19 | +61% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4503 | 34 | -9% | -81% | -80% | -78% |
| Momentum model ≥ 5% | 2726 | 25 | +17% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1792 | 17 | +31% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 9157 | 63 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6425 | 53 | -9% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4293 | 38 | -0% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22696 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8509 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4606 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 35811 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 137 | 0% | -$2,446.40 | -56% | — |
| Sell at 2¢ | 1360 | 4% | -$3,814.80 | -87% | 47 sec |
| Sell at 3¢ | 933 | 3% | -$3,804.53 | -87% | 48 sec |
| Sell at 5¢ | 648 | 2% | -$3,747.20 | -86% | 62 sec |
| Sell at 10¢ | 396 | 1% | -$3,593.64 | -82% | 65 sec |
| Sell at 25¢ | 213 | 1% | -$3,309.37 | -76% | 88 sec |
| Sell at 50¢ | 141 | 0% | -$2,978.65 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1593 | 8 | 11% | 4% | -52% | -81% | -82% |
| 2–5 min | 11449 | 65 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 9083 | 32 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13682 | 32 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2542 | 12 | 5% | 2% | -40% | -89% | -88% |
| HYPE | 2534 | 8 | 5% | 3% | -61% | -89% | -87% |
| BNB | 2533 | 15 | 5% | 2% | -26% | -84% | -83% |
| SOL | 2528 | 7 | 4% | 2% | -65% | -92% | -92% |
| ETH | 2521 | 11 | 6% | 3% | -47% | -85% | -85% |
| DOGE | 2519 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2510 | 11 | 3% | 1% | -46% | -89% | -89% |
| NEAR | 2506 | 12 | 5% | 2% | -38% | -82% | -82% |
| BTC | 2503 | 13 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1348 | 5 | 5% | 2% | -56% | -81% | -83% |
| SILVER | 1319 | 6 | 4% | 2% | -47% | -82% | -81% |
| WTI | 1300 | 4 | 3% | 1% | -63% | -93% | -94% |
| PLATINUM | 1170 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1115 | 4 | 1% | 1% | -67% | -73% | -73% |
| EURUSD | 1093 | 3 | 2% | 1% | -74% | -88% | -88% |
| NATGAS | 1073 | 6 | 2% | 1% | -48% | -79% | -79% |
| PALLADIUM | 1034 | 2 | 1% | 0% | -82% | -89% | -89% |
| GBPUSD | 1029 | 2 | 2% | 1% | -82% | -96% | -96% |
| USDJPY | 1014 | 5 | 2% | 1% | -54% | -97% | -96% |
| AUDUSD | 570 | 3 | 1% | 1% | -51% | -81% | -80% |
| USDCAD | 530 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 150 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 101 | 0 | 4% | 0% | -100% | -93% | -92% |
| 30YRRATE | 92 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 89 | 1 | 3% | 1% | +5% | +11% | +11% |
| 5YRRATE | 88 | 1 | 5% | 2% | +6% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18121 | 76 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 17690 | 61 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3747 | 19 | 2% | 1% | -13% | -81% | -80% |
| 0.05–0.1% | 3905 | 14 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 5901 | 22 | 5% | 2% | -54% | -90% | -89% |
| 0.2–0.5% | 6668 | 29 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2471 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8838 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,637 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 12:44:46 AM | BTC | UP | 13 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/28 12:44:30 AM | ZEC | DOWN | 29 sec | +0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/28 12:44:30 AM | ETH | DOWN | 29 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/28 12:44:30 AM | XRP | DOWN | 29 sec | +0.007% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:44:30 AM | BNB | UP | 29 sec | -0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:44:30 AM | EURUSD | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:44:14 AM | PALLADIUM | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:43:57 AM | BRENT | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:43:41 AM | WTI | UP | 78 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 12:43:41 AM | NATGAS | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:43:41 AM | USDJPY | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:43:09 AM | GBPUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:42:04 AM | HYPE | UP | 2.9 min | -0.210% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:41:15 AM | GOLD | UP | 3.7 min | — | 4¢ | ❌ Lost | -$0.15 |
| 10/28 12:41:15 AM | USDCAD | DOWN | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:41:15 AM | AUDUSD | UP | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:39:54 AM | SILVER | UP | 5.1 min | — | 6¢ | ❌ Lost | -$0.15 |
| 10/28 12:39:19 AM | PLATINUM | UP | 5.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:29:59 AM | COPPER | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:29:43 AM | SOL | UP | 17 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/28 12:29:43 AM | HYPE | UP | 17 sec | -0.063% | 0¢ | ❌ Lost | $0.00 |
| 10/28 12:29:43 AM | BTC | UP | 17 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/28 12:29:43 AM | NEAR | UP | 17 sec | -0.185% | 0¢ | ❌ Lost | $0.00 |
| 10/28 12:29:27 AM | WTI | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:29:12 AM | DOGE | DOWN | 48 sec | +0.049% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:29:12 AM | BRENT | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:29:12 AM | NATGAS | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:29:12 AM | XRP | UP | 48 sec | -0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:28:55 AM | ETH | UP | 64 sec | -0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:28:55 AM | PALLADIUM | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
