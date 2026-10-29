# 15-Minute 1¢ Study

*Updated Wed Oct 28, 10:04 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3057 finished bets | 1% | $90.95 | +27% | +2.98¢ | $82.80 / $8.15 |

*Expect about **99 buys a day** (~$14.84/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2834 | $39.95 | +13% |
| Volatility model ≥ 2%, hold to the close | 5655 | $12.70 | +2% |
| Volatility model ≥ 5%, sell at 50¢ | 3057 | -$63.30 | -18% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 37447 | 37439 | 140 (0%) | 1.07% | -$2,610.35 (-57%) | Hold to the close: -$2,610.35 (-57%) |

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
| Volatility model | 23229 | 4.7% | 0.4% (93) | -676% | ❌ Worse |
| Momentum model | 23229 | 4.6% | 0.4% (93) | -700% | ❌ Worse |
| Mean-reversion model | 23229 | 8.1% | 0.4% (93) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23229 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5655 | 50 | +2% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3057 | 31 | +27% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1732 | 19 | +56% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4669 | 34 | -12% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2834 | 25 | +13% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1854 | 17 | +27% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9495 | 64 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6661 | 54 | -10% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4446 | 39 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23429 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8967 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5043 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 37439 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 140 | 0% | -$2,610.35 | -57% | — |
| Sell at 2¢ | 1422 | 4% | -$4,004.63 | -88% | 47 sec |
| Sell at 3¢ | 977 | 3% | -$3,993.32 | -87% | 48 sec |
| Sell at 5¢ | 678 | 2% | -$3,933.65 | -86% | 62 sec |
| Sell at 10¢ | 412 | 1% | -$3,778.63 | -83% | 64 sec |
| Sell at 25¢ | 220 | 1% | -$3,492.15 | -76% | 82 sec |
| Sell at 50¢ | 145 | 0% | -$3,157.60 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1690 | 8 | 11% | 4% | -55% | -80% | -82% |
| 2–5 min | 11954 | 67 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9475 | 32 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14316 | 33 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2622 | 12 | 5% | 2% | -41% | -88% | -88% |
| HYPE | 2616 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2616 | 15 | 5% | 2% | -28% | -85% | -84% |
| SOL | 2609 | 7 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2604 | 11 | 6% | 3% | -49% | -86% | -85% |
| DOGE | 2603 | 6 | 4% | 2% | -71% | -90% | -90% |
| XRP | 2588 | 11 | 3% | 1% | -48% | -89% | -89% |
| NEAR | 2586 | 12 | 5% | 2% | -40% | -82% | -82% |
| BTC | 2585 | 13 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1411 | 5 | 4% | 2% | -57% | -82% | -83% |
| SILVER | 1383 | 6 | 4% | 2% | -49% | -82% | -82% |
| WTI | 1366 | 4 | 3% | 1% | -65% | -93% | -94% |
| PLATINUM | 1227 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1163 | 4 | 1% | 1% | -68% | -74% | -73% |
| EURUSD | 1153 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1130 | 7 | 2% | 1% | -42% | -80% | -79% |
| GBPUSD | 1095 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1090 | 2 | 1% | 0% | -83% | -89% | -90% |
| USDJPY | 1074 | 5 | 2% | 1% | -57% | -97% | -96% |
| AUDUSD | 628 | 4 | 1% | 1% | -41% | -83% | -82% |
| USDCAD | 594 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 197 | 0 | 1% | 1% | -100% | -99% | -99% |
| 10YRRATE | 133 | 0 | 5% | 1% | -100% | -92% | -90% |
| 30YRRATE | 125 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 124 | 1 | 4% | 1% | -25% | -18% | -16% |
| 5YRRATE | 117 | 1 | 6% | 3% | -20% | -90% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18980 | 77 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 18459 | 63 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3846 | 19 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 4038 | 14 | 3% | 2% | -48% | -92% | -92% |
| 0.1–0.2% | 6085 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6908 | 30 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2548 | 10 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9232 | 42 | 4% | 2% | -48% | -86% | -85% |
| Afternoon (12–6pm) | 8852 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 10126 | 34 | 3% | 2% | -61% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,549 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 9:59:58 PM | BRENT | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:59:58 PM | SILVER | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:59:58 PM | ETH | DOWN | 2 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:59:58 PM | BNB | DOWN | 2 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:59:58 PM | SOL | UP | 2 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:59:43 PM | USDCAD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:59:43 PM | DOGE | DOWN | 16 sec | +0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:59:43 PM | EURUSD | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:59:27 PM | COPPER | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:59:27 PM | XRP | UP | 32 sec | -0.116% | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:59:27 PM | USDJPY | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:59:27 PM | WTI | UP | 32 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 9:59:11 PM | NEAR | DOWN | 48 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:59:11 PM | PLATINUM | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:58:55 PM | PALLADIUM | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:58:39 PM | BTC | UP | 81 sec | -0.074% | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:57:35 PM | AUDUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:57:04 PM | ZEC | DOWN | 2.9 min | +0.379% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 9:56:32 PM | GOLD | UP | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 9:44:50 PM | WTI | DOWN | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:44:09 PM | NEAR | DOWN | 50 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:44:09 PM | BTC | DOWN | 50 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:44:09 PM | SOL | DOWN | 50 sec | +0.087% | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:43:53 PM | XRP | DOWN | 66 sec | +0.078% | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:43:53 PM | AUDUSD | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:43:53 PM | PLATINUM | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 9:43:37 PM | GOLD | DOWN | 82 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 9:43:37 PM | ETH | DOWN | 82 sec | +0.160% | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:43:37 PM | BNB | DOWN | 82 sec | +0.109% | 0¢ | ❌ Lost | $0.00 |
| 10/28 9:43:37 PM | NATGAS | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
