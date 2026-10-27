# 15-Minute 1¢ Study

*Updated Tue Oct 27, 2:07 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2815 finished bets | 1% | $73.70 | +23% | +2.62¢ | $68.75 / $4.95 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2623 | $46.95 | +16% |
| Volatility model ≥ 2%, hold to the close | 5235 | -$24.05 | -4% |
| Momentum model ≥ 2%, hold to the close | 4351 | -$46.35 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34150 | 34142 | 126 (0%) | 1.07% | -$2,389.65 (-58%) | Hold to the close: -$2,389.65 (-58%) |

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
| Volatility model | 21706 | 4.6% | 0.4% (86) | -672% | ❌ Worse |
| Momentum model | 21706 | 4.6% | 0.4% (86) | -697% | ❌ Worse |
| Mean-reversion model | 21706 | 8.0% | 0.4% (86) | -816% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21706 | 86 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5235 | 44 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2815 | 28 | +23% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1599 | 18 | +58% | -67% | -66% | -63% |
| Momentum model ≥ 2% | 4351 | 33 | -9% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2623 | 24 | +16% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1715 | 16 | +28% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8792 | 57 | -29% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6158 | 47 | -16% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4104 | 33 | -9% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21906 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8037 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4199 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34142 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 126 | 0% | -$2,389.65 | -58% | — |
| Sell at 2¢ | 1280 | 4% | -$3,652.85 | -88% | 47 sec |
| Sell at 3¢ | 876 | 3% | -$3,644.01 | -88% | 48 sec |
| Sell at 5¢ | 606 | 2% | -$3,591.75 | -86% | 62 sec |
| Sell at 10¢ | 373 | 1% | -$3,441.02 | -83% | 65 sec |
| Sell at 25¢ | 199 | 1% | -$3,186.96 | -77% | 83 sec |
| Sell at 50¢ | 129 | 0% | -$2,890.90 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1498 | 8 | 11% | 4% | -49% | -81% | -82% |
| 2–5 min | 10955 | 58 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8647 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13038 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2454 | 12 | 5% | 2% | -38% | -89% | -88% |
| HYPE | 2446 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2444 | 13 | 5% | 2% | -34% | -84% | -83% |
| SOL | 2440 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2434 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2429 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2422 | 12 | 5% | 2% | -36% | -82% | -82% |
| XRP | 2421 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2416 | 12 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1288 | 5 | 4% | 2% | -54% | -81% | -83% |
| SILVER | 1252 | 6 | 4% | 2% | -44% | -82% | -82% |
| WTI | 1232 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1103 | 0 | 2% | 1% | -100% | -97% | -97% |
| COPPER | 1064 | 4 | 1% | 1% | -65% | -71% | -71% |
| EURUSD | 1034 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1022 | 5 | 2% | 1% | -54% | -87% | -87% |
| PALLADIUM | 982 | 2 | 1% | 0% | -81% | -89% | -89% |
| GBPUSD | 974 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 959 | 5 | 1% | 1% | -51% | -98% | -97% |
| AUDUSD | 518 | 2 | 1% | 1% | -64% | -98% | -96% |
| USDCAD | 476 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 94 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 66 | 0 | 3% | 0% | -100% | -95% | -96% |
| 2YRRATE | 60 | 1 | 3% | 0% | +56% | +61% | +60% |
| 30YRRATE | 59 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 53 | 1 | 4% | 4% | +76% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17321 | 69 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16821 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3613 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3752 | 12 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5675 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6449 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2413 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8456 | 33 | 4% | 2% | -56% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,709 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 1:59:56 AM | GBPUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:59:40 AM | AUDUSD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:59:40 AM | 2YRRATE | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:59:40 AM | NATGAS | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:59:24 AM | 30YRRATE | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:59:24 AM | COPPER | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:58:52 AM | SILVER | UP | 67 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 10/27 1:58:36 AM | BRENT | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:58:20 AM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:58:04 AM | USDCAD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:58:04 AM | PLATINUM | UP | 1.9 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/27 1:57:06 AM | WTI | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:57:06 AM | 5YRRATE | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:56:50 AM | 10YRRATE | DOWN | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:56:50 AM | USDJPY | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:56:35 AM | GOLD | UP | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:56:19 AM | ZEC | DOWN | 3.7 min | +0.507% | 2¢ | ❌ Lost | -$0.15 |
| 10/27 1:55:30 AM | BNB | DOWN | 4.5 min | +0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:55:30 AM | DOGE | DOWN | 4.5 min | +0.258% | 2¢ | ❌ Lost | -$0.15 |
| 10/27 1:55:14 AM | NEAR | DOWN | 4.8 min | +0.733% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:54:58 AM | BTC | DOWN | 5.0 min | +0.244% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:54:28 AM | HYPE | DOWN | 5.5 min | +0.428% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:54:28 AM | XRP | DOWN | 5.5 min | +0.331% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:52:05 AM | ETH | DOWN | 7.9 min | +0.446% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:51:49 AM | SOL | DOWN | 8.2 min | +0.542% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:38:45 AM | 10YRRATE | DOWN | 6.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:29:32 AM | 5YRRATE | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:29:32 AM | NEAR | DOWN | 28 sec | -0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 1:29:32 AM | PLATINUM | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 1:29:16 AM | AUDUSD | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
