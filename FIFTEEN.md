# 15-Minute 1¢ Study

*Updated Tue Oct 27, 9:02 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2854 finished bets | 1% | $69.50 | +22% | +2.44¢ | $80.35 / -$10.85 |

*Expect about **97 buys a day** (~$14.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2663 | $42.60 | +15% |
| Volatility model ≥ 2%, hold to the close | 5302 | -$18.30 | -3% |
| Momentum model ≥ 2%, hold to the close | 4407 | -$52.50 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34721 | 34713 | 129 (0%) | 1.07% | -$2,421.75 (-57%) | Hold to the close: -$2,421.75 (-57%) |

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
| Volatility model | 21950 | 4.6% | 0.4% (87) | -675% | ❌ Worse |
| Momentum model | 21950 | 4.6% | 0.4% (87) | -700% | ❌ Worse |
| Mean-reversion model | 21950 | 8.0% | 0.4% (87) | -819% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21950 | 87 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5302 | 45 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2854 | 28 | +22% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1619 | 18 | +56% | -67% | -66% | -63% |
| Momentum model ≥ 2% | 4407 | 33 | -10% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2663 | 24 | +15% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1740 | 16 | +27% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8908 | 58 | -29% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6234 | 48 | -15% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4156 | 34 | -8% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22150 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8198 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4365 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34713 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 129 | 0% | -$2,421.75 | -57% | — |
| Sell at 2¢ | 1309 | 4% | -$3,705.41 | -88% | 47 sec |
| Sell at 3¢ | 892 | 3% | -$3,697.87 | -87% | 48 sec |
| Sell at 5¢ | 616 | 2% | -$3,645.35 | -86% | 62 sec |
| Sell at 10¢ | 380 | 1% | -$3,491.95 | -83% | 65 sec |
| Sell at 25¢ | 205 | 1% | -$3,227.20 | -76% | 1.5 min |
| Sell at 50¢ | 135 | 0% | -$2,910.50 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1539 | 8 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 11146 | 60 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8801 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13223 | 30 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2481 | 12 | 5% | 2% | -38% | -89% | -89% |
| HYPE | 2472 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2471 | 14 | 5% | 2% | -29% | -84% | -83% |
| SOL | 2468 | 6 | 4% | 2% | -70% | -92% | -92% |
| ETH | 2462 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2457 | 5 | 4% | 2% | -75% | -90% | -90% |
| NEAR | 2450 | 12 | 5% | 2% | -36% | -82% | -82% |
| XRP | 2447 | 9 | 3% | 1% | -55% | -89% | -89% |
| BTC | 2442 | 12 | 5% | 2% | -34% | -88% | -89% |
| GOLD | 1306 | 5 | 4% | 2% | -54% | -81% | -83% |
| SILVER | 1276 | 6 | 4% | 2% | -45% | -82% | -82% |
| WTI | 1256 | 3 | 3% | 1% | -72% | -94% | -95% |
| PLATINUM | 1127 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1083 | 4 | 1% | 1% | -66% | -72% | -72% |
| EURUSD | 1052 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1040 | 6 | 2% | 1% | -46% | -79% | -78% |
| PALLADIUM | 997 | 2 | 1% | 0% | -81% | -89% | -89% |
| GBPUSD | 990 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 978 | 5 | 1% | 1% | -52% | -98% | -97% |
| AUDUSD | 537 | 2 | 1% | 1% | -65% | -98% | -97% |
| USDCAD | 498 | 0 | 1% | 0% | -100% | -98% | -98% |
| BRENT | 113 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 86 | 0 | 5% | 0% | -100% | -92% | -91% |
| 30YRRATE | 76 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 74 | 1 | 4% | 1% | +26% | +33% | +33% |
| 5YRRATE | 74 | 1 | 5% | 3% | +26% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17572 | 71 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 17141 | 58 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3639 | 18 | 2% | 1% | -16% | -81% | -80% |
| 0.05–0.1% | 3788 | 12 | 3% | 2% | -53% | -92% | -92% |
| 0.1–0.2% | 5743 | 20 | 5% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 6543 | 29 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2433 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8511 | 39 | 4% | 2% | -48% | -87% | -86% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,656 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 8:59:54 AM | EURUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:59:54 AM | AUDUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:59:38 AM | PLATINUM | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:59:38 AM | NATGAS | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:59:38 AM | USDCAD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:59:38 AM | DOGE | DOWN | 22 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:59:22 AM | 2YRRATE | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:59:22 AM | XRP | DOWN | 38 sec | +0.030% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:59:05 AM | NEAR | UP | 54 sec | -0.390% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:59:05 AM | BRENT | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:59:05 AM | 5YRRATE | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:59:05 AM | WTI | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:58:50 AM | BTC | DOWN | 69 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:58:50 AM | BNB | DOWN | 69 sec | +0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:58:50 AM | SOL | DOWN | 69 sec | +0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:58:34 AM | ZEC | UP | 85 sec | -0.411% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:58:34 AM | HYPE | UP | 85 sec | -0.209% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:58:18 AM | GOLD | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:57:47 AM | 10YRRATE | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:56:59 AM | 30YRRATE | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:56:43 AM | ETH | DOWN | 3.3 min | +0.232% | 2¢ | ❌ Lost | -$0.15 |
| 10/27 8:56:27 AM | COPPER | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:56:11 AM | SILVER | DOWN | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:56:11 AM | PALLADIUM | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:54 AM | NEAR | DOWN | 5 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:44:54 AM | 2YRRATE | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:54 AM | USDJPY | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:54 AM | HYPE | DOWN | 5 sec | -0.013% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:54 AM | 10YRRATE | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:54 AM | WTI | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
