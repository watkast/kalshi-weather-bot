# 15-Minute 1¢ Study

*Updated Fri Oct 23, 1:25 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2477 finished bets | 1% | $83.80 | +30% | +3.38¢ | $46.70 / $37.10 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2296 | $53.90 | +21% |
| Volatility model ≥ 2%, hold to the close | 4598 | -$3.40 | -1% |
| Momentum model ≥ 2%, hold to the close | 3835 | -$31.05 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30177 | 30169 | 114 (0%) | 1.07% | -$2,087.70 (-57%) | Hold to the close: -$2,087.70 (-57%) |

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
| Volatility model | 19062 | 4.6% | 0.4% (80) | -643% | ❌ Worse |
| Momentum model | 19062 | 4.5% | 0.4% (80) | -668% | ❌ Worse |
| Mean-reversion model | 19062 | 7.9% | 0.4% (80) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19062 | 80 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4598 | 40 | -1% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2477 | 26 | +30% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1410 | 17 | +70% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3835 | 30 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2296 | 22 | +21% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1504 | 15 | +37% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7657 | 53 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5344 | 44 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3553 | 31 | -1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19262 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7292 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3615 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30169 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 114 | 0% | -$2,087.70 | -57% | — |
| Sell at 2¢ | 1127 | 4% | -$3,236.68 | -88% | 47 sec |
| Sell at 3¢ | 771 | 3% | -$3,229.01 | -88% | 48 sec |
| Sell at 5¢ | 539 | 2% | -$3,179.35 | -86% | 61 sec |
| Sell at 10¢ | 328 | 1% | -$3,058.02 | -83% | 64 sec |
| Sell at 25¢ | 182 | 1% | -$2,815.28 | -76% | 82 sec |
| Sell at 50¢ | 116 | 0% | -$2,550.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1275 | 7 | 11% | 4% | -48% | -80% | -82% |
| 2–5 min | 9678 | 52 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 7695 | 28 | 3% | 1% | -60% | -93% | -93% |
| Under 1 min | 11517 | 27 | 1% | 0% | -67% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2159 | 12 | 5% | 2% | -30% | -89% | -89% |
| BNB | 2152 | 12 | 5% | 3% | -31% | -83% | -82% |
| HYPE | 2149 | 8 | 5% | 3% | -54% | -88% | -86% |
| ETH | 2141 | 10 | 6% | 3% | -44% | -86% | -85% |
| SOL | 2141 | 4 | 4% | 1% | -77% | -92% | -92% |
| DOGE | 2137 | 4 | 4% | 2% | -77% | -90% | -89% |
| XRP | 2130 | 8 | 3% | 1% | -54% | -88% | -88% |
| NEAR | 2127 | 12 | 6% | 3% | -27% | -81% | -80% |
| BTC | 2126 | 12 | 5% | 2% | -25% | -88% | -89% |
| GOLD | 1184 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1150 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1121 | 3 | 3% | 1% | -68% | -94% | -95% |
| PLATINUM | 1007 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 984 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 934 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 924 | 5 | 2% | 1% | -49% | -86% | -86% |
| PALLADIUM | 895 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 879 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 860 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 425 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 381 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 38 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 38 | 0 | 3% | 0% | -100% | -95% | -100% |
| 30YRRATE | 35 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 27 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 25 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15235 | 62 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 14934 | 52 | 4% | 2% | -60% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3161 | 16 | 2% | 1% | -15% | -79% | -78% |
| 0.05–0.1% | 3302 | 11 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4974 | 17 | 5% | 2% | -58% | -89% | -89% |
| 0.2–0.5% | 5656 | 28 | 6% | 3% | -46% | -87% | -86% |
| Over 0.5% | 2165 | 10 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7532 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7425 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7050 | 21 | 4% | 2% | -65% | -89% | -89% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,582 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 1:14:45 PM | PLATINUM | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:14:29 PM | WTI | DOWN | 31 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 1:14:29 PM | GOLD | UP | 31 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 1:13:24 PM | SOL | UP | 1.6 min | -0.222% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 1:13:24 PM | ETH | UP | 1.6 min | -0.236% | 0¢ | ❌ Lost | $0.00 |
| 10/23 1:13:24 PM | GBPUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:13:08 PM | BTC | UP | 1.9 min | -0.153% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 1:12:50 PM | EURUSD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:12:34 PM | HYPE | UP | 2.4 min | -0.312% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 1:12:18 PM | USDCAD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:12:03 PM | XRP | UP | 2.9 min | -0.268% | 0¢ | ❌ Lost | $0.00 |
| 10/23 1:12:03 PM | BNB | UP | 2.9 min | -0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 1:11:47 PM | 10YRRATE | DOWN | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 1:11:47 PM | NEAR | UP | 3.2 min | -0.658% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 1:11:31 PM | AUDUSD | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:11:15 PM | ZEC | UP | 3.7 min | -0.626% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 1:11:15 PM | DOGE | UP | 3.7 min | -0.239% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 1:08:50 PM | 30YRRATE | DOWN | 6.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 12:59:55 PM | SILVER | DOWN | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 12:59:55 PM | EURUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:59:55 PM | PLATINUM | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:59:55 PM | GOLD | DOWN | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 12:59:40 PM | BNB | UP | 19 sec | -0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/23 12:59:40 PM | WTI | DOWN | 19 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 12:59:24 PM | BTC | UP | 35 sec | -0.075% | 0¢ | ❌ Lost | $0.00 |
| 10/23 12:59:24 PM | ETH | UP | 35 sec | -0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/23 12:59:24 PM | DOGE | UP | 35 sec | -0.088% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:59:08 PM | NATGAS | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:59:08 PM | SOL | UP | 51 sec | -0.075% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:59:08 PM | XRP | UP | 51 sec | -0.084% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
