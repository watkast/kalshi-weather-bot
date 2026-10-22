# 15-Minute 1¢ Study

*Updated Thu Oct 22, 9:23 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2364 finished bets | 1% | $69.30 | +26% | +2.93¢ | $39.75 / $29.55 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2184 | $52.05 | +22% |
| Volatility model ≥ 2%, hold to the close | 4345 | $0.40 | +0% |
| Momentum model ≥ 2%, hold to the close | 3643 | -$36.70 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28223 | 28215 | 107 (0%) | 1.07% | -$1,939.10 (-56%) | Hold to the close: -$1,939.10 (-56%) |

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
| Volatility model | 18100 | 4.7% | 0.4% (77) | -650% | ❌ Worse |
| Momentum model | 18100 | 4.6% | 0.4% (77) | -675% | ❌ Worse |
| Mean-reversion model | 18100 | 7.9% | 0.4% (77) | -782% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18100 | 77 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4345 | 38 | +0% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2364 | 24 | +26% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1352 | 16 | +66% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 3643 | 28 | -9% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2184 | 21 | +22% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1433 | 14 | +34% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7219 | 51 | -23% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5041 | 42 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3355 | 29 | -2% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18299 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6778 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3138 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28215 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 107 | 0% | -$1,939.10 | -56% | — |
| Sell at 2¢ | 1027 | 4% | -$3,030.08 | -88% | 47 sec |
| Sell at 3¢ | 702 | 2% | -$3,023.32 | -88% | 48 sec |
| Sell at 5¢ | 495 | 2% | -$2,975.35 | -87% | 61 sec |
| Sell at 10¢ | 305 | 1% | -$2,869.55 | -83% | 64 sec |
| Sell at 25¢ | 169 | 1% | -$2,639.71 | -77% | 83 sec |
| Sell at 50¢ | 111 | 0% | -$2,379.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1171 | 7 | 11% | 4% | -43% | -81% | -84% |
| 2–5 min | 9075 | 50 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7176 | 27 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 10789 | 23 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2051 | 11 | 5% | 2% | -33% | -89% | -89% |
| BNB | 2046 | 12 | 5% | 2% | -28% | -83% | -82% |
| HYPE | 2043 | 8 | 5% | 3% | -52% | -89% | -87% |
| ETH | 2033 | 10 | 6% | 3% | -41% | -86% | -86% |
| SOL | 2033 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2030 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2023 | 7 | 3% | 1% | -57% | -88% | -88% |
| NEAR | 2021 | 12 | 6% | 3% | -23% | -80% | -80% |
| BTC | 2019 | 12 | 5% | 2% | -20% | -88% | -89% |
| GOLD | 1108 | 3 | 4% | 1% | -68% | -82% | -84% |
| SILVER | 1072 | 4 | 3% | 1% | -57% | -83% | -83% |
| WTI | 1045 | 3 | 3% | 1% | -66% | -94% | -95% |
| PLATINUM | 930 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 921 | 3 | 1% | 1% | -70% | -77% | -77% |
| NATGAS | 860 | 5 | 2% | 1% | -46% | -86% | -85% |
| EURUSD | 858 | 3 | 2% | 1% | -67% | -85% | -85% |
| PALLADIUM | 834 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 805 | 1 | 2% | 1% | -88% | -97% | -96% |
| USDJPY | 774 | 4 | 1% | 1% | -52% | -99% | -98% |
| AUDUSD | 363 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 316 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 9 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14245 | 57 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 13970 | 50 | 3% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3042 | 15 | 2% | 1% | -17% | -78% | -78% |
| 0.05–0.1% | 3154 | 11 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4677 | 17 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5354 | 27 | 6% | 3% | -45% | -87% | -87% |
| Over 0.5% | 2068 | 9 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 6805 | 32 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,687 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 9:14:45 AM | NATGAS | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 9:14:13 AM | USDCAD | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 9:14:13 AM | GOLD | UP | 47 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 9:14:13 AM | AUDUSD | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 9:13:57 AM | SILVER | UP | 63 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 9:13:41 AM | COPPER | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 9:13:25 AM | GBPUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 9:12:27 AM | USDJPY | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 9:12:11 AM | PALLADIUM | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 9:11:55 AM | XRP | UP | 3.1 min | -0.393% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 9:11:40 AM | SOL | UP | 3.3 min | -0.351% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 9:10:52 AM | NEAR | UP | 4.1 min | -0.824% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 9:10:52 AM | ZEC | UP | 4.1 min | -0.635% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 9:10:21 AM | EURUSD | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 9:09:49 AM | BTC | UP | 5.2 min | -0.355% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 9:09:49 AM | BNB | UP | 5.2 min | -0.177% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 9:09:33 AM | DOGE | UP | 5.4 min | -0.513% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 9:09:33 AM | HYPE | UP | 5.4 min | -0.693% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 9:09:17 AM | ETH | UP | 5.7 min | -0.501% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:59:55 AM | NATGAS | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:59:39 AM | USDJPY | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:59:39 AM | USDCAD | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:59:39 AM | COPPER | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:59:39 AM | PLATINUM | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:59:39 AM | SILVER | UP | 21 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:59:23 AM | WTI | DOWN | 37 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 8:58:53 AM | EURUSD | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:58:53 AM | AUDUSD | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:58:21 AM | GBPUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:57:50 AM | BTC | UP | 2.2 min | -0.173% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
