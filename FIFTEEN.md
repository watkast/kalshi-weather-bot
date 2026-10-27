# 15-Minute 1¢ Study

*Updated Tue Oct 27, 4:21 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2827 finished bets | 1% | $72.20 | +23% | +2.55¢ | $68.00 / $4.20 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2637 | $45.15 | +16% |
| Volatility model ≥ 2%, hold to the close | 5255 | -$26.60 | -4% |
| Momentum model ≥ 2%, hold to the close | 4371 | -$48.90 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34342 | 34334 | 127 (0%) | 1.07% | -$2,399.80 (-57%) | Hold to the close: -$2,399.80 (-57%) |

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
| Volatility model | 21784 | 4.6% | 0.4% (86) | -675% | ❌ Worse |
| Momentum model | 21784 | 4.6% | 0.4% (86) | -700% | ❌ Worse |
| Mean-reversion model | 21784 | 8.0% | 0.4% (86) | -819% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21784 | 86 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5255 | 44 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2827 | 28 | +23% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1607 | 18 | +57% | -67% | -66% | -63% |
| Momentum model ≥ 2% | 4371 | 33 | -10% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2637 | 24 | +16% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1723 | 16 | +28% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8819 | 57 | -30% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6175 | 47 | -16% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4115 | 33 | -10% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21984 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8094 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4256 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34334 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 127 | 0% | -$2,399.80 | -57% | — |
| Sell at 2¢ | 1286 | 4% | -$3,675.44 | -88% | 47 sec |
| Sell at 3¢ | 878 | 3% | -$3,667.38 | -88% | 48 sec |
| Sell at 5¢ | 608 | 2% | -$3,614.60 | -87% | 62 sec |
| Sell at 10¢ | 375 | 1% | -$3,462.55 | -83% | 65 sec |
| Sell at 25¢ | 201 | 1% | -$3,204.49 | -77% | 83 sec |
| Sell at 50¢ | 131 | 0% | -$2,901.55 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1509 | 8 | 11% | 4% | -49% | -81% | -82% |
| 2–5 min | 11011 | 59 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8707 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13103 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2462 | 12 | 5% | 2% | -38% | -89% | -88% |
| HYPE | 2455 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2453 | 13 | 5% | 2% | -34% | -84% | -83% |
| SOL | 2449 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2443 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2438 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2431 | 12 | 5% | 2% | -36% | -82% | -82% |
| XRP | 2429 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2424 | 12 | 5% | 2% | -34% | -88% | -89% |
| GOLD | 1294 | 5 | 4% | 2% | -54% | -82% | -83% |
| SILVER | 1261 | 6 | 4% | 2% | -45% | -82% | -82% |
| WTI | 1240 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1110 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1072 | 4 | 1% | 1% | -65% | -72% | -71% |
| EURUSD | 1040 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1028 | 5 | 2% | 1% | -55% | -87% | -87% |
| PALLADIUM | 988 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 982 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 967 | 5 | 1% | 1% | -52% | -98% | -97% |
| AUDUSD | 523 | 2 | 1% | 1% | -64% | -98% | -97% |
| USDCAD | 484 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 101 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 71 | 0 | 3% | 0% | -100% | -95% | -96% |
| 30YRRATE | 65 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 63 | 1 | 3% | 0% | +48% | +54% | +52% |
| 5YRRATE | 61 | 1 | 3% | 3% | +53% | -94% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17428 | 70 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16906 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3622 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3768 | 12 | 3% | 2% | -53% | -92% | -92% |
| 0.1–0.2% | 5700 | 20 | 5% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 6474 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2416 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8648 | 34 | 4% | 2% | -55% | -85% | -86% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,685 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 4:14:55 AM | 2YRRATE | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:14:55 AM | PLATINUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:14:55 AM | USDJPY | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:14:55 AM | 30YRRATE | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:14:55 AM | 5YRRATE | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:14:39 AM | GBPUSD | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:14:39 AM | EURUSD | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:13:20 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:13:20 AM | USDCAD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:13:20 AM | NATGAS | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:13:04 AM | AUDUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:12:48 AM | BRENT | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:12:16 AM | PALLADIUM | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:12:16 AM | WTI | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:11:45 AM | GOLD | UP | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:10:34 AM | SILVER | UP | 4.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:10:18 AM | ZEC | UP | 4.7 min | -0.847% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:10:18 AM | XRP | UP | 4.7 min | -0.324% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:10:18 AM | BTC | UP | 4.7 min | -0.268% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:10:02 AM | HYPE | UP | 5.0 min | -0.424% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:09:29 AM | DOGE | UP | 5.5 min | -0.302% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:09:29 AM | SOL | UP | 5.5 min | -0.347% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:09:29 AM | NEAR | UP | 5.5 min | -0.750% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:08:11 AM | ETH | UP | 6.8 min | -0.430% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:07:24 AM | BNB | UP | 7.6 min | -0.281% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 3:59:37 AM | DOGE | DOWN | 23 sec | +0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/27 3:59:37 AM | NEAR | DOWN | 23 sec | +0.054% | 0¢ | ❌ Lost | $0.00 |
| 10/27 3:59:37 AM | 5YRRATE | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:59:21 AM | XRP | DOWN | 39 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/27 3:59:21 AM | 10YRRATE | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
