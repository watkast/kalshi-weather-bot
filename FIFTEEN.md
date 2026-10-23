# 15-Minute 1¢ Study

*Updated Fri Oct 23, 9:05 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2464 finished bets | 1% | $85.45 | +31% | +3.47¢ | $47.45 / $38.00 |

*Expect about **97 buys a day** (~$14.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2277 | $56.30 | +22% |
| Volatility model ≥ 2%, hold to the close | 4561 | $1.40 | +0% |
| Momentum model ≥ 2%, hold to the close | 3803 | -$27.15 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 29861 | 29853 | 114 (0%) | 1.07% | -$2,048.40 (-56%) | Hold to the close: -$2,048.40 (-56%) |

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
| Volatility model | 18912 | 4.7% | 0.4% (80) | -644% | ❌ Worse |
| Momentum model | 18912 | 4.6% | 0.4% (80) | -669% | ❌ Worse |
| Mean-reversion model | 18912 | 7.9% | 0.4% (80) | -776% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18912 | 80 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4561 | 40 | +0% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2464 | 26 | +31% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1404 | 17 | +71% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3803 | 30 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2277 | 22 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1500 | 15 | +38% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7585 | 53 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5311 | 44 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3537 | 31 | -1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19111 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7211 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3531 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 29853 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 114 | 0% | -$2,048.40 | -56% | — |
| Sell at 2¢ | 1115 | 4% | -$3,200.50 | -88% | 47 sec |
| Sell at 3¢ | 764 | 3% | -$3,192.44 | -88% | 48 sec |
| Sell at 5¢ | 537 | 2% | -$3,141.35 | -86% | 61 sec |
| Sell at 10¢ | 327 | 1% | -$3,020.03 | -83% | 64 sec |
| Sell at 25¢ | 181 | 1% | -$2,779.29 | -76% | 82 sec |
| Sell at 50¢ | 116 | 0% | -$2,511.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1267 | 7 | 11% | 4% | -47% | -80% | -82% |
| 2–5 min | 9577 | 52 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7613 | 28 | 3% | 2% | -60% | -93% | -93% |
| Under 1 min | 11392 | 27 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2142 | 12 | 5% | 2% | -30% | -89% | -89% |
| BNB | 2135 | 12 | 5% | 3% | -31% | -83% | -82% |
| HYPE | 2132 | 8 | 5% | 3% | -54% | -88% | -86% |
| ETH | 2124 | 10 | 6% | 3% | -44% | -86% | -85% |
| SOL | 2124 | 4 | 4% | 2% | -77% | -92% | -92% |
| DOGE | 2120 | 4 | 4% | 2% | -77% | -90% | -89% |
| XRP | 2114 | 8 | 3% | 1% | -53% | -88% | -88% |
| NEAR | 2111 | 12 | 6% | 3% | -26% | -80% | -80% |
| BTC | 2109 | 12 | 5% | 2% | -24% | -88% | -89% |
| GOLD | 1172 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1137 | 5 | 4% | 1% | -49% | -82% | -82% |
| WTI | 1109 | 3 | 3% | 1% | -68% | -94% | -95% |
| PLATINUM | 996 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 974 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 920 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 915 | 5 | 2% | 1% | -49% | -86% | -86% |
| PALLADIUM | 886 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 865 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 847 | 5 | 1% | 1% | -45% | -98% | -98% |
| AUDUSD | 415 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 368 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 33 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 33 | 0 | 3% | 0% | -100% | -95% | -100% |
| 30YRRATE | 29 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 22 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15048 | 62 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 14805 | 52 | 4% | 2% | -60% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3154 | 16 | 2% | 1% | -15% | -79% | -78% |
| 0.05–0.1% | 3279 | 11 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4922 | 17 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5602 | 28 | 6% | 3% | -45% | -87% | -86% |
| Over 0.5% | 2150 | 10 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7532 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7204 | 34 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,610 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 8:59:55 AM | PLATINUM | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 8:59:55 AM | PALLADIUM | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 8:59:55 AM | NATGAS | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 8:59:39 AM | COPPER | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 8:59:39 AM | ETH | UP | 21 sec | -0.071% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 8:59:23 AM | BTC | UP | 37 sec | -0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/23 8:59:23 AM | SOL | DOWN | 37 sec | +0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/23 8:59:23 AM | NEAR | UP | 37 sec | -0.288% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 8:59:23 AM | DOGE | DOWN | 37 sec | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/23 8:59:08 AM | XRP | UP | 51 sec | -0.221% | 0¢ | ❌ Lost | $0.00 |
| 10/23 8:59:08 AM | BNB | UP | 51 sec | -0.108% | 0¢ | ❌ Lost | $0.00 |
| 10/23 8:58:52 AM | USDCAD | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 8:58:52 AM | ZEC | UP | 67 sec | -0.441% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 8:57:14 AM | USDJPY | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 8:56:43 AM | GBPUSD | DOWN | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 8:54:49 AM | HYPE | DOWN | 5.2 min | +0.456% | 8¢ | ❌ Lost | -$0.15 |
| 10/23 8:44:49 AM | 2YRRATE | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 8:44:24 AM | GBPUSD | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 8:44:08 AM | BRENT | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 8:44:08 AM | USDJPY | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 8:43:50 AM | WTI | DOWN | 70 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 8:43:18 AM | USDCAD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 8:43:18 AM | EURUSD | DOWN | 1.7 min | — | 44¢ | ❌ Lost | -$0.15 |
| 10/23 8:42:31 AM | NATGAS | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 8:41:08 AM | AUDUSD | DOWN | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 8:40:53 AM | XRP | DOWN | 4.1 min | +0.474% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 8:40:53 AM | PALLADIUM | DOWN | 4.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 8:40:37 AM | SOL | DOWN | 4.4 min | +0.629% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 8:40:37 AM | NEAR | DOWN | 4.4 min | +0.951% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 8:40:37 AM | HYPE | DOWN | 4.4 min | +0.679% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
