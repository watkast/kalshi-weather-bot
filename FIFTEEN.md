# 15-Minute 1¢ Study

*Updated Fri Oct 23, 6:24 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2462 finished bets | 1% | $85.75 | +31% | +3.48¢ | $47.60 / $38.15 |

*Expect about **98 buys a day** (~$14.63/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2270 | $57.20 | +23% |
| Volatility model ≥ 2%, hold to the close | 4552 | $2.60 | +0% |
| Momentum model ≥ 2%, hold to the close | 3790 | -$25.50 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 29683 | 29673 | 113 (0%) | 1.07% | -$2,038.70 (-56%) | Hold to the close: -$2,038.70 (-56%) |

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
| Volatility model | 18831 | 4.7% | 0.4% (80) | -645% | ❌ Worse |
| Momentum model | 18831 | 4.6% | 0.4% (80) | -670% | ❌ Worse |
| Mean-reversion model | 18831 | 7.9% | 0.4% (80) | -777% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18831 | 80 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4552 | 40 | +0% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2462 | 26 | +31% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1403 | 17 | +71% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3790 | 30 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2270 | 22 | +23% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1497 | 15 | +38% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7552 | 53 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5286 | 44 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3520 | 31 | -0% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19030 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7163 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3480 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 29673 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 113 | 0% | -$2,038.70 | -56% | — |
| Sell at 2¢ | 1100 | 4% | -$3,180.70 | -88% | 47 sec |
| Sell at 3¢ | 753 | 3% | -$3,173.03 | -88% | 48 sec |
| Sell at 5¢ | 530 | 2% | -$3,122.20 | -86% | 61 sec |
| Sell at 10¢ | 323 | 1% | -$3,015.57 | -83% | 64 sec |
| Sell at 25¢ | 180 | 1% | -$2,772.90 | -77% | 82 sec |
| Sell at 50¢ | 116 | 0% | -$2,501.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1252 | 7 | 11% | 4% | -47% | -80% | -82% |
| 2–5 min | 9515 | 52 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7578 | 28 | 3% | 2% | -60% | -93% | -93% |
| Under 1 min | 11324 | 26 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2133 | 12 | 5% | 2% | -29% | -89% | -89% |
| BNB | 2126 | 12 | 5% | 3% | -30% | -83% | -82% |
| HYPE | 2123 | 8 | 5% | 3% | -54% | -88% | -87% |
| ETH | 2115 | 10 | 6% | 3% | -43% | -86% | -86% |
| SOL | 2115 | 4 | 3% | 2% | -77% | -92% | -92% |
| DOGE | 2111 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2105 | 8 | 3% | 1% | -53% | -88% | -88% |
| NEAR | 2102 | 12 | 6% | 3% | -26% | -80% | -80% |
| BTC | 2100 | 12 | 5% | 2% | -24% | -88% | -89% |
| GOLD | 1166 | 3 | 4% | 1% | -69% | -82% | -83% |
| SILVER | 1131 | 5 | 4% | 1% | -49% | -82% | -82% |
| WTI | 1103 | 3 | 3% | 1% | -68% | -94% | -95% |
| PLATINUM | 988 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 969 | 4 | 1% | 1% | -61% | -69% | -68% |
| EURUSD | 914 | 3 | 2% | 1% | -69% | -86% | -86% |
| NATGAS | 909 | 5 | 2% | 1% | -49% | -86% | -86% |
| PALLADIUM | 878 | 2 | 1% | 0% | -79% | -87% | -88% |
| GBPUSD | 858 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 840 | 5 | 1% | 1% | -44% | -98% | -98% |
| AUDUSD | 406 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 361 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 27 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 26 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 19 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14970 | 61 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 14703 | 52 | 4% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3149 | 16 | 2% | 1% | -15% | -79% | -78% |
| 0.05–0.1% | 3271 | 11 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4909 | 17 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5567 | 28 | 6% | 3% | -45% | -87% | -87% |
| Over 0.5% | 2130 | 10 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7532 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7024 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,627 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 6:24:35 AM | USDCAD | UP | 5.4 min | — | — | In play | — |
| 10/23 6:23:47 AM | NEAR | DOWN | 6.2 min | +0.795% | — | In play | — |
| 10/23 6:14:47 AM | GOLD | UP | 13 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 6:14:47 AM | USDCAD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:14:31 AM | EURUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:14:03 AM | BNB | UP | 56 sec | -0.098% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:14:03 AM | GBPUSD | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:14:03 AM | 10YRRATE | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:13:16 AM | 2YRRATE | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:13:16 AM | 5YRRATE | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:13:16 AM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:13:16 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:12:45 AM | USDJPY | UP | 2.2 min | — | 7¢ | ❌ Lost | -$0.15 |
| 10/23 6:11:41 AM | PALLADIUM | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:11:25 AM | BTC | UP | 3.6 min | -0.210% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:11:25 AM | PLATINUM | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:11:09 AM | SOL | UP | 3.9 min | -0.279% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:11:09 AM | DOGE | UP | 3.9 min | -0.254% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:11:09 AM | XRP | UP | 3.9 min | -0.258% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:10:21 AM | ZEC | UP | 4.6 min | -0.667% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:10:05 AM | HYPE | UP | 4.9 min | -0.375% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:09:34 AM | ETH | UP | 5.4 min | -0.266% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:09:34 AM | NEAR | UP | 5.4 min | -0.742% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:08:15 AM | WTI | DOWN | 6.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:59:52 AM | WTI | DOWN | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 5:59:52 AM | COPPER | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 5:59:52 AM | BTC | DOWN | 8 sec | +0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/23 5:59:36 AM | HYPE | DOWN | 24 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/23 5:59:36 AM | PALLADIUM | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 5:59:36 AM | SILVER | UP | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
