# 15-Minute 1¢ Study

*Updated Tue Oct 27, 1:17 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2811 finished bets | 1% | $74.30 | +23% | +2.64¢ | $54.90 / $19.40 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2621 | $47.25 | +16% |
| Volatility model ≥ 2%, hold to the close | 5229 | -$23.15 | -4% |
| Momentum model ≥ 2%, hold to the close | 4349 | -$46.05 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34106 | 34098 | 126 (0%) | 1.07% | -$2,383.05 (-57%) | Hold to the close: -$2,383.05 (-57%) |

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
| Volatility model | 21688 | 4.6% | 0.4% (86) | -672% | ❌ Worse |
| Momentum model | 21688 | 4.6% | 0.4% (86) | -697% | ❌ Worse |
| Mean-reversion model | 21688 | 7.9% | 0.4% (86) | -815% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21688 | 86 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5229 | 44 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2811 | 28 | +23% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1597 | 18 | +58% | -67% | -65% | -63% |
| Momentum model ≥ 2% | 4349 | 33 | -9% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2621 | 24 | +16% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1713 | 16 | +29% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8779 | 57 | -29% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6148 | 47 | -16% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4096 | 33 | -9% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21888 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8027 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4183 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34098 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 126 | 0% | -$2,383.05 | -57% | — |
| Sell at 2¢ | 1279 | 4% | -$3,646.51 | -88% | 47 sec |
| Sell at 3¢ | 876 | 3% | -$3,637.41 | -88% | 48 sec |
| Sell at 5¢ | 606 | 2% | -$3,585.15 | -86% | 62 sec |
| Sell at 10¢ | 373 | 1% | -$3,434.42 | -83% | 65 sec |
| Sell at 25¢ | 199 | 1% | -$3,180.36 | -77% | 83 sec |
| Sell at 50¢ | 129 | 0% | -$2,884.30 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1488 | 8 | 11% | 4% | -49% | -80% | -82% |
| 2–5 min | 10941 | 58 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8639 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13026 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2452 | 12 | 5% | 2% | -38% | -89% | -88% |
| HYPE | 2444 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2442 | 13 | 5% | 2% | -33% | -84% | -83% |
| SOL | 2438 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2432 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2427 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2420 | 12 | 5% | 2% | -36% | -82% | -82% |
| XRP | 2419 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2414 | 12 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1287 | 5 | 4% | 2% | -54% | -81% | -83% |
| SILVER | 1251 | 6 | 4% | 2% | -44% | -82% | -82% |
| WTI | 1231 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1101 | 0 | 2% | 1% | -100% | -97% | -97% |
| COPPER | 1063 | 4 | 1% | 1% | -65% | -71% | -71% |
| EURUSD | 1032 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1020 | 5 | 2% | 1% | -54% | -87% | -87% |
| PALLADIUM | 981 | 2 | 1% | 0% | -81% | -89% | -89% |
| GBPUSD | 972 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 957 | 5 | 1% | 1% | -51% | -98% | -97% |
| AUDUSD | 516 | 2 | 1% | 1% | -64% | -98% | -96% |
| USDCAD | 475 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 93 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 64 | 0 | 3% | 0% | -100% | -95% | -96% |
| 2YRRATE | 58 | 1 | 3% | 0% | +61% | +67% | +65% |
| 30YRRATE | 58 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 51 | 1 | 4% | 4% | +83% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17309 | 69 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16789 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3612 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3752 | 12 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5671 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6439 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2410 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8412 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,712 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 1:14:55 AM | USDCAD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:14:55 AM | EURUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:14:55 AM | 2YRRATE | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:14:55 AM | 30YRRATE | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:14:55 AM | 10YRRATE | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:14:39 AM | BNB | UP | 20 sec | -0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/27 1:14:23 AM | NATGAS | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:14:23 AM | NEAR | UP | 36 sec | -0.208% | 0¢ | ❌ Lost | $0.00 |
| 10/27 1:14:23 AM | DOGE | UP | 36 sec | -0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:14:08 AM | 5YRRATE | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:14:08 AM | BTC | UP | 51 sec | -0.063% | 0¢ | ❌ Lost | $0.00 |
| 10/27 1:14:08 AM | ETH | UP | 51 sec | -0.086% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:14:08 AM | XRP | DOWN | 51 sec | +0.023% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:14:08 AM | BRENT | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:13:36 AM | WTI | DOWN | 84 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 1:13:20 AM | HYPE | DOWN | 1.7 min | +0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:13:20 AM | GOLD | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:13:20 AM | PALLADIUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:10:38 AM | ZEC | DOWN | 4.4 min | +0.415% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:09:25 AM | GBPUSD | UP | 5.6 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/27 1:07:02 AM | AUDUSD | UP | 8.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:59:46 AM | ZEC | DOWN | 13 sec | +0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/27 12:59:46 AM | HYPE | UP | 13 sec | -0.019% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 12:59:46 AM | BNB | UP | 13 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/27 12:59:30 AM | USDCAD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:59:30 AM | AUDUSD | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:59:14 AM | GBPUSD | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:59:14 AM | SILVER | DOWN | 46 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 12:58:58 AM | COPPER | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:58:42 AM | EURUSD | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
