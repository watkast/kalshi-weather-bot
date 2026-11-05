# 15-Minute 1¢ Study

*Updated Thu Nov 5, 11:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3711 finished bets | 1% | $133.20 | +32% | +3.59¢ | $87.90 / $45.30 |

*Expect about **96 buys a day** (~$14.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3451 | $60.50 | +16% |
| Volatility model ≥ 2%, hold to the close | 6867 | $40.15 | +5% |
| Momentum model ≥ 2%, hold to the close | 5668 | -$36.05 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 46747 | 46736 | 171 (0%) | 1.07% | -$3,306.30 (-58%) | Hold to the close: -$3,306.30 (-58%) |

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
| Volatility model | 28363 | 4.7% | 0.4% (110) | -688% | ❌ Worse |
| Momentum model | 28363 | 4.6% | 0.4% (110) | -715% | ❌ Worse |
| Mean-reversion model | 28363 | 8.1% | 0.4% (110) | -836% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28363 | 110 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6867 | 62 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3711 | 39 | +32% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2121 | 24 | +63% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5668 | 44 | -6% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3451 | 31 | +16% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2255 | 20 | +25% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11731 | 80 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8228 | 69 | -7% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5516 | 49 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28568 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11192 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6976 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 46736 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 171 | 0% | -$3,306.30 | -58% | — |
| Sell at 2¢ | 1826 | 4% | -$4,973.54 | -87% | 47 sec |
| Sell at 3¢ | 1247 | 3% | -$4,961.97 | -87% | 48 sec |
| Sell at 5¢ | 861 | 2% | -$4,860.65 | -85% | 63 sec |
| Sell at 10¢ | 521 | 1% | -$4,653.79 | -82% | 65 sec |
| Sell at 25¢ | 270 | 1% | -$4,330.60 | -76% | 83 sec |
| Sell at 50¢ | 174 | 0% | -$3,951.80 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2317 | 10 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 15043 | 80 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 11757 | 39 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17607 | 42 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3201 | 13 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3193 | 12 | 4% | 2% | -52% | -90% | -90% |
| HYPE | 3189 | 9 | 5% | 2% | -65% | -89% | -88% |
| BNB | 3189 | 17 | 5% | 2% | -33% | -85% | -85% |
| DOGE | 3174 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3171 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3154 | 16 | 5% | 2% | -34% | -84% | -84% |
| BTC | 3153 | 15 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3144 | 12 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1728 | 5 | 5% | 2% | -65% | -81% | -83% |
| WTI | 1676 | 5 | 4% | 1% | -64% | -92% | -93% |
| SILVER | 1675 | 8 | 5% | 2% | -44% | -82% | -81% |
| PLATINUM | 1508 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1447 | 3 | 2% | 1% | -81% | -89% | -89% |
| COPPER | 1423 | 6 | 2% | 1% | -61% | -71% | -71% |
| GBPUSD | 1377 | 4 | 2% | 1% | -73% | -96% | -96% |
| NATGAS | 1363 | 8 | 2% | 1% | -45% | -76% | -75% |
| PALLADIUM | 1355 | 3 | 1% | 1% | -79% | -91% | -91% |
| USDJPY | 1354 | 5 | 2% | 1% | -66% | -97% | -97% |
| AUDUSD | 900 | 4 | 2% | 1% | -59% | -87% | -86% |
| USDCAD | 881 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 464 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 273 | 1 | 4% | 1% | -66% | -58% | -56% |
| 30YRRATE | 257 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 253 | 2 | 3% | 0% | -26% | -21% | -20% |
| 5YRRATE | 234 | 1 | 4% | 2% | -60% | -93% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23704 | 90 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23032 | 81 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4586 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4859 | 18 | 3% | 2% | -44% | -91% | -90% |
| 0.1–0.2% | 7363 | 26 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8519 | 33 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3233 | 13 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11506 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11644 | 51 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 10960 | 39 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12626 | 41 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,650 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/5 11:44:59 AM | GOLD | UP | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/5 11:44:59 AM | 2YRRATE | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:44:59 AM | BTC | DOWN | 0 sec | +0.026% | 0¢ | ❌ Lost | $0.00 |
| 11/5 11:44:43 AM | BNB | DOWN | 17 sec | +0.048% | 0¢ | ❌ Lost | $0.00 |
| 11/5 11:44:43 AM | SILVER | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:44:43 AM | BRENT | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:44:27 AM | DOGE | DOWN | 33 sec | +0.132% | 0¢ | ❌ Lost | $0.00 |
| 11/5 11:44:11 AM | ETH | UP | 49 sec | -0.175% | 0¢ | ❌ Lost | $0.00 |
| 11/5 11:43:56 AM | NEAR | DOWN | 63 sec | +0.261% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:43:56 AM | HYPE | UP | 63 sec | -0.232% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:43:56 AM | USDJPY | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:43:25 AM | WTI | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:43:09 AM | NATGAS | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:42:36 AM | EURUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:42:36 AM | SOL | UP | 2.4 min | -0.347% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 11:41:50 AM | ZEC | UP | 3.2 min | -0.997% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 11:41:19 AM | AUDUSD | UP | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:41:03 AM | GBPUSD | UP | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:41:03 AM | USDCAD | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:29:48 AM | PALLADIUM | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:29:33 AM | ZEC | DOWN | 27 sec | +0.249% | 0¢ | ❌ Lost | $0.00 |
| 11/5 11:29:33 AM | HYPE | DOWN | 27 sec | +0.140% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 11:29:33 AM | BNB | UP | 27 sec | -0.075% | 0¢ | ❌ Lost | $0.00 |
| 11/5 11:29:33 AM | SOL | UP | 27 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 11/5 11:29:33 AM | AUDUSD | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:29:17 AM | PLATINUM | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:29:17 AM | DOGE | DOWN | 43 sec | +0.155% | 0¢ | ❌ Lost | $0.00 |
| 11/5 11:29:17 AM | NATGAS | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:29:01 AM | USDCAD | DOWN | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 11:28:45 AM | ETH | UP | 75 sec | -0.212% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
