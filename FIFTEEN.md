# 15-Minute 1¢ Study

*Updated Fri Oct 16, 1:36 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1595 finished bets | 1% | $74.70 | +42% | +4.68¢ | $39.90 / $34.80 |

*Expect about **88 buys a day** (~$13.26/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1485 | $48.90 | +30% |
| Momentum model ≥ 2%, hold to the close | 2494 | -$9.50 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 1595 | -$20.55 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20406 | 20399 | 79 (0%) | 1.07% | -$1,375.60 (-55%) | Hold to the close: -$1,375.60 (-55%) |

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
| Volatility model | 13082 | 4.4% | 0.4% (53) | -641% | ❌ Worse |
| Momentum model | 13082 | 4.4% | 0.4% (53) | -665% | ❌ Worse |
| Mean-reversion model | 13082 | 7.4% | 0.4% (53) | -767% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13082 | 53 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2905 | 23 | -8% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1595 | 18 | +42% | -74% | -73% | -68% |
| Volatility model ≥ 10% | 936 | 11 | +67% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2494 | 20 | -3% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1485 | 15 | +30% | -77% | -77% | -74% |
| Momentum model ≥ 10% | 992 | 10 | +41% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4911 | 33 | -27% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3376 | 26 | -15% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2210 | 15 | -22% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13280 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5047 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2072 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20399 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 79 | 0% | -$1,375.60 | -55% | — |
| Sell at 2¢ | 719 | 4% | -$2,196.66 | -89% | 42 sec |
| Sell at 3¢ | 482 | 2% | -$2,195.62 | -88% | 47 sec |
| Sell at 5¢ | 351 | 2% | -$2,155.45 | -87% | 50 sec |
| Sell at 10¢ | 216 | 1% | -$2,072.64 | -84% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,899.85 | -77% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,690.10 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 660 | 5 | 11% | 3% | -28% | -81% | -86% |
| 2–5 min | 6618 | 36 | 7% | 3% | -46% | -88% | -88% |
| 1–2 min | 5308 | 20 | 3% | 2% | -59% | -92% | -92% |
| Under 1 min | 7809 | 18 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1490 | 11 | 5% | 3% | -8% | -89% | -90% |
| HYPE | 1486 | 5 | 4% | 2% | -59% | -90% | -89% |
| ETH | 1480 | 8 | 5% | 3% | -34% | -88% | -87% |
| BNB | 1478 | 5 | 4% | 2% | -58% | -90% | -90% |
| DOGE | 1477 | 2 | 4% | 2% | -83% | -91% | -90% |
| SOL | 1473 | 2 | 3% | 2% | -83% | -92% | -91% |
| XRP | 1468 | 7 | 3% | 1% | -41% | -86% | -86% |
| BTC | 1466 | 7 | 5% | 2% | -36% | -88% | -91% |
| NEAR | 1462 | 8 | 5% | 3% | -28% | -78% | -79% |
| GOLD | 823 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 801 | 4 | 3% | 1% | -42% | -79% | -80% |
| WTI | 771 | 3 | 3% | 1% | -55% | -94% | -96% |
| COPPER | 705 | 2 | 2% | 1% | -74% | -84% | -83% |
| PLATINUM | 684 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 632 | 2 | 1% | 0% | -70% | -83% | -84% |
| NATGAS | 631 | 5 | 2% | 2% | -26% | -81% | -80% |
| EURUSD | 624 | 3 | 3% | 1% | -55% | -80% | -80% |
| GBPUSD | 583 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 549 | 3 | 1% | 1% | -49% | -99% | -98% |
| AUDUSD | 169 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 147 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10269 | 39 | 4% | 2% | -56% | -89% | -89% |
| DOWN (bought NO) | 10130 | 40 | 4% | 2% | -54% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2206 | 11 | 2% | 1% | -16% | -79% | -78% |
| 0.05–0.1% | 2296 | 7 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 3362 | 10 | 4% | 2% | -63% | -90% | -90% |
| 0.2–0.5% | 3881 | 21 | 6% | 3% | -40% | -88% | -88% |
| Over 0.5% | 1532 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5074 | 20 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,459 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 1:29:52 AM | BNB | DOWN | 8 sec | -0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:29:52 AM | NATGAS | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:29:52 AM | WTI | DOWN | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:29:36 AM | XRP | DOWN | 24 sec | +0.030% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:29:36 AM | BTC | DOWN | 24 sec | +0.052% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:29:20 AM | PLATINUM | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:29:20 AM | NEAR | DOWN | 40 sec | +0.179% | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:29:20 AM | ETH | DOWN | 40 sec | +0.119% | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:29:05 AM | SOL | UP | 54 sec | -0.067% | 7¢ | ❌ Lost | $0.00 |
| 10/16 1:28:49 AM | GOLD | DOWN | 70 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:28:17 AM | USDJPY | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:28:17 AM | HYPE | UP | 1.7 min | -0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:28:17 AM | DOGE | UP | 1.7 min | -0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:26:23 AM | EURUSD | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:25:51 AM | GBPUSD | DOWN | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:14:53 AM | ZEC | UP | 7 sec | -0.101% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:14:53 AM | SILVER | DOWN | 7 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:14:21 AM | USDJPY | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:14:06 AM | BTC | DOWN | 53 sec | +0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:13:50 AM | SOL | DOWN | 69 sec | +0.167% | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:13:50 AM | XRP | DOWN | 69 sec | +0.134% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:13:50 AM | DOGE | DOWN | 69 sec | +0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:13:18 AM | GBPUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:13:18 AM | AUDUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:13:18 AM | BNB | DOWN | 1.7 min | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:13:18 AM | HYPE | DOWN | 1.7 min | +0.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:12:44 AM | ETH | DOWN | 2.3 min | +0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:12:44 AM | USDCAD | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:12:12 AM | PALLADIUM | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:10:52 AM | PLATINUM | DOWN | 4.1 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
