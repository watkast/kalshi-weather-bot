# 15-Minute 1¢ Study

*Updated Wed Oct 28, 10:53 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2991 finished bets | 1% | $83.70 | +25% | +2.80¢ | $86.70 / -$3.00 |

*Expect about **98 buys a day** (~$14.75/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2777 | $45.20 | +15% |
| Volatility model ≥ 2%, hold to the close | 5538 | $11.60 | +2% |
| Momentum model ≥ 2%, hold to the close | 4581 | -$56.80 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 36603 | 36595 | 138 (0%) | 1.07% | -$2,531.40 (-57%) | Hold to the close: -$2,531.40 (-57%) |

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
| Volatility model | 22837 | 4.7% | 0.4% (92) | -672% | ❌ Worse |
| Momentum model | 22837 | 4.6% | 0.4% (92) | -696% | ❌ Worse |
| Mean-reversion model | 22837 | 8.1% | 0.4% (92) | -816% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22837 | 92 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5538 | 49 | +2% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 2991 | 30 | +25% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1697 | 19 | +59% | -68% | -66% | -64% |
| Momentum model ≥ 2% | 4581 | 34 | -11% | -81% | -80% | -78% |
| Momentum model ≥ 5% | 2777 | 25 | +15% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1821 | 17 | +29% | -72% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9318 | 63 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6538 | 53 | -10% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4370 | 38 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23037 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8725 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4833 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 36595 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,531.40 | -57% | — |
| Sell at 2¢ | 1390 | 4% | -$3,906.00 | -88% | 47 sec |
| Sell at 3¢ | 953 | 3% | -$3,895.73 | -87% | 48 sec |
| Sell at 5¢ | 662 | 2% | -$3,837.10 | -86% | 62 sec |
| Sell at 10¢ | 404 | 1% | -$3,682.16 | -82% | 65 sec |
| Sell at 25¢ | 217 | 1% | -$3,395.13 | -76% | 83 sec |
| Sell at 50¢ | 143 | 0% | -$3,064.15 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1635 | 8 | 11% | 4% | -53% | -80% | -81% |
| 2–5 min | 11684 | 66 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 9280 | 32 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 13992 | 32 | 1% | 0% | -67% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2580 | 12 | 5% | 2% | -41% | -88% | -88% |
| HYPE | 2573 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2571 | 15 | 5% | 2% | -27% | -85% | -84% |
| SOL | 2565 | 7 | 3% | 2% | -66% | -92% | -92% |
| ETH | 2559 | 11 | 6% | 3% | -48% | -85% | -85% |
| DOGE | 2557 | 5 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2548 | 11 | 3% | 1% | -47% | -89% | -89% |
| NEAR | 2542 | 12 | 5% | 2% | -39% | -82% | -82% |
| BTC | 2542 | 13 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1379 | 5 | 4% | 2% | -56% | -81% | -83% |
| SILVER | 1350 | 6 | 4% | 2% | -48% | -82% | -81% |
| WTI | 1329 | 4 | 3% | 1% | -64% | -93% | -94% |
| PLATINUM | 1197 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1140 | 4 | 1% | 1% | -67% | -73% | -73% |
| EURUSD | 1119 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1100 | 6 | 2% | 1% | -49% | -79% | -79% |
| GBPUSD | 1062 | 2 | 2% | 1% | -82% | -96% | -96% |
| PALLADIUM | 1060 | 2 | 1% | 0% | -82% | -89% | -89% |
| USDJPY | 1038 | 5 | 2% | 1% | -55% | -97% | -96% |
| AUDUSD | 598 | 4 | 1% | 1% | -38% | -82% | -81% |
| USDCAD | 565 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 170 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 121 | 0 | 3% | 0% | -100% | -94% | -94% |
| 30YRRATE | 115 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 110 | 1 | 3% | 1% | -15% | -10% | -10% |
| 5YRRATE | 105 | 1 | 5% | 2% | -11% | -92% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18518 | 77 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 18077 | 61 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3801 | 19 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3970 | 14 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 5996 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6766 | 29 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2500 | 10 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9134 | 42 | 4% | 2% | -48% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,577 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 10:44:59 AM | GBPUSD | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 10:44:59 AM | HYPE | UP | 0 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/28 10:44:59 AM | COPPER | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 10:44:59 AM | SILVER | DOWN | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 10:44:43 AM | EURUSD | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 10:44:43 AM | USDCAD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 10:44:11 AM | AUDUSD | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 10:43:55 AM | XRP | UP | 65 sec | -0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 10:43:55 AM | BTC | UP | 65 sec | -0.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 10:43:33 AM | SOL | UP | 87 sec | -0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 10:43:17 AM | PALLADIUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 10:43:17 AM | ETH | UP | 1.7 min | -0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 10:42:44 AM | BNB | UP | 2.2 min | -0.175% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 10:42:12 AM | DOGE | UP | 2.8 min | -0.224% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 10:41:56 AM | PLATINUM | UP | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 10:41:39 AM | ZEC | UP | 3.3 min | -0.343% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 10:41:23 AM | NEAR | UP | 3.6 min | -0.558% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 10:29:54 AM | WTI | UP | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 10:29:38 AM | BNB | UP | 22 sec | -0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/28 10:29:38 AM | DOGE | UP | 22 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/28 10:29:38 AM | USDJPY | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 10:29:38 AM | HYPE | DOWN | 22 sec | +0.011% | 0¢ | ❌ Lost | $0.00 |
| 10/28 10:29:38 AM | PALLADIUM | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 10:29:38 AM | GBPUSD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 10:29:22 AM | NEAR | UP | 38 sec | -0.156% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 10:29:22 AM | ETH | UP | 38 sec | -0.059% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 10:29:22 AM | USDCAD | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 10:29:22 AM | ZEC | UP | 38 sec | -0.137% | 0¢ | ❌ Lost | $0.00 |
| 10/28 10:29:06 AM | PLATINUM | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 10:28:51 AM | BRENT | UP | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
