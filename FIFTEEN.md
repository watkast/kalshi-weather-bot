# 15-Minute 1¢ Study

*Updated Thu Nov 5, 6:04 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3700 finished bets | 1% | $133.95 | +33% | +3.62¢ | $88.35 / $45.60 |

*Expect about **97 buys a day** (~$14.50/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3440 | $61.40 | +16% |
| Volatility model ≥ 2%, hold to the close | 6848 | $41.95 | +5% |
| Momentum model ≥ 2%, hold to the close | 5652 | -$34.55 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 46525 | 46514 | 170 (0%) | 1.07% | -$3,291.95 (-58%) | Hold to the close: -$3,291.95 (-58%) |

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
| Volatility model | 28276 | 4.7% | 0.4% (110) | -686% | ❌ Worse |
| Momentum model | 28276 | 4.6% | 0.4% (110) | -713% | ❌ Worse |
| Mean-reversion model | 28276 | 8.1% | 0.4% (110) | -834% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28276 | 110 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6848 | 62 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3700 | 39 | +33% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2112 | 24 | +63% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5652 | 44 | -5% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3440 | 31 | +16% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2248 | 20 | +25% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11694 | 80 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8206 | 69 | -7% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5497 | 49 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28481 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11129 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6904 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 46514 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 170 | 0% | -$3,291.95 | -58% | — |
| Sell at 2¢ | 1820 | 4% | -$4,946.75 | -87% | 47 sec |
| Sell at 3¢ | 1244 | 3% | -$4,934.79 | -87% | 48 sec |
| Sell at 5¢ | 860 | 2% | -$4,832.95 | -85% | 63 sec |
| Sell at 10¢ | 520 | 1% | -$4,626.75 | -82% | 65 sec |
| Sell at 25¢ | 269 | 1% | -$4,305.56 | -76% | 83 sec |
| Sell at 50¢ | 173 | 0% | -$3,930.20 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2308 | 10 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 14969 | 79 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 11697 | 39 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17528 | 42 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3190 | 13 | 5% | 2% | -47% | -88% | -88% |
| SOL | 3183 | 12 | 4% | 2% | -52% | -90% | -90% |
| HYPE | 3179 | 9 | 5% | 2% | -65% | -89% | -88% |
| BNB | 3179 | 17 | 5% | 2% | -33% | -85% | -85% |
| DOGE | 3166 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3160 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3144 | 16 | 5% | 2% | -34% | -84% | -84% |
| BTC | 3144 | 15 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3136 | 12 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1720 | 5 | 5% | 2% | -65% | -81% | -83% |
| SILVER | 1670 | 8 | 5% | 2% | -44% | -82% | -81% |
| WTI | 1668 | 5 | 4% | 1% | -64% | -92% | -93% |
| PLATINUM | 1499 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1437 | 3 | 2% | 1% | -81% | -89% | -89% |
| COPPER | 1414 | 6 | 2% | 1% | -60% | -71% | -70% |
| GBPUSD | 1367 | 3 | 2% | 1% | -80% | -96% | -96% |
| NATGAS | 1355 | 8 | 2% | 1% | -45% | -76% | -75% |
| PALLADIUM | 1348 | 3 | 1% | 1% | -79% | -91% | -91% |
| USDJPY | 1347 | 5 | 2% | 1% | -65% | -97% | -97% |
| AUDUSD | 892 | 4 | 2% | 1% | -58% | -86% | -86% |
| USDCAD | 870 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 455 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 266 | 1 | 5% | 2% | -65% | -57% | -55% |
| 30YRRATE | 250 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 248 | 2 | 3% | 0% | -25% | -19% | -18% |
| 5YRRATE | 227 | 1 | 4% | 2% | -59% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23596 | 90 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 22918 | 80 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4573 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4856 | 18 | 3% | 2% | -44% | -91% | -90% |
| 0.1–0.2% | 7341 | 26 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8493 | 33 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3210 | 13 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11506 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11422 | 50 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 10960 | 39 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12626 | 41 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,671 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/5 5:59:53 AM | WTI | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:59:53 AM | GBPUSD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:59:53 AM | 30YRRATE | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:59:37 AM | BRENT | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:59:37 AM | BNB | DOWN | 23 sec | +0.003% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:59:37 AM | XRP | DOWN | 23 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 11/5 5:59:37 AM | DOGE | DOWN | 23 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 11/5 5:59:21 AM | AUDUSD | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:59:21 AM | SOL | DOWN | 39 sec | +0.070% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:59:21 AM | ETH | UP | 39 sec | -0.068% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:59:06 AM | NEAR | UP | 53 sec | -0.327% | 0¢ | ❌ Lost | $0.00 |
| 11/5 5:59:06 AM | USDJPY | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:58:51 AM | BTC | UP | 68 sec | -0.133% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:58:51 AM | HYPE | UP | 68 sec | -0.154% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:58:35 AM | ZEC | DOWN | 84 sec | +0.396% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:58:35 AM | EURUSD | DOWN | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:58:19 AM | USDCAD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:57:16 AM | NATGAS | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:56:13 AM | SILVER | DOWN | 3.8 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/5 5:55:56 AM | PLATINUM | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:54:22 AM | PALLADIUM | DOWN | 5.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:44:58 AM | GBPUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:44:58 AM | HYPE | UP | 1 sec | -0.165% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:44:27 AM | BRENT | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:44:27 AM | PALLADIUM | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:43:38 AM | GOLD | UP | 81 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:42:19 AM | USDJPY | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:41:16 AM | USDCAD | DOWN | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:40:44 AM | BNB | UP | 4.3 min | -0.352% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:40:12 AM | AUDUSD | UP | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
