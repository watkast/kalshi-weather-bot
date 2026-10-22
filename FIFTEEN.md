# 15-Minute 1¢ Study

*Updated Thu Oct 22, 8:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2363 finished bets | 1% | $69.45 | +26% | +2.94¢ | $39.75 / $29.70 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2184 | $52.05 | +22% |
| Volatility model ≥ 2%, hold to the close | 4343 | $0.70 | +0% |
| Momentum model ≥ 2%, hold to the close | 3641 | -$36.40 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28185 | 28177 | 107 (0%) | 1.07% | -$1,933.85 (-56%) | Hold to the close: -$1,933.85 (-56%) |

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
| Volatility model | 18082 | 4.7% | 0.4% (77) | -651% | ❌ Worse |
| Momentum model | 18082 | 4.6% | 0.4% (77) | -675% | ❌ Worse |
| Mean-reversion model | 18082 | 7.9% | 0.4% (77) | -782% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18082 | 77 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4343 | 38 | +0% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2363 | 24 | +26% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1352 | 16 | +66% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 3641 | 28 | -8% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2184 | 21 | +22% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1433 | 14 | +34% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7207 | 51 | -23% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5034 | 42 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3352 | 29 | -2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18281 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6768 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3128 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28177 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 107 | 0% | -$1,933.85 | -56% | — |
| Sell at 2¢ | 1027 | 4% | -$3,024.83 | -88% | 47 sec |
| Sell at 3¢ | 702 | 2% | -$3,018.07 | -88% | 48 sec |
| Sell at 5¢ | 495 | 2% | -$2,970.10 | -87% | 61 sec |
| Sell at 10¢ | 305 | 1% | -$2,864.30 | -83% | 64 sec |
| Sell at 25¢ | 169 | 1% | -$2,634.46 | -77% | 83 sec |
| Sell at 50¢ | 111 | 0% | -$2,374.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1165 | 7 | 11% | 4% | -43% | -81% | -84% |
| 2–5 min | 9060 | 50 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7170 | 27 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 10778 | 23 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2049 | 11 | 5% | 2% | -33% | -89% | -89% |
| BNB | 2044 | 12 | 5% | 2% | -28% | -83% | -82% |
| HYPE | 2041 | 8 | 5% | 3% | -52% | -89% | -87% |
| ETH | 2031 | 10 | 6% | 3% | -41% | -86% | -86% |
| SOL | 2031 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2028 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2021 | 7 | 3% | 1% | -57% | -88% | -88% |
| NEAR | 2019 | 12 | 6% | 3% | -23% | -80% | -80% |
| BTC | 2017 | 12 | 5% | 2% | -20% | -88% | -89% |
| GOLD | 1107 | 3 | 4% | 1% | -68% | -82% | -84% |
| SILVER | 1070 | 4 | 3% | 1% | -57% | -83% | -83% |
| WTI | 1044 | 3 | 3% | 1% | -66% | -94% | -95% |
| PLATINUM | 929 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 919 | 3 | 1% | 1% | -70% | -77% | -77% |
| NATGAS | 858 | 5 | 2% | 1% | -46% | -86% | -85% |
| EURUSD | 856 | 3 | 2% | 1% | -67% | -85% | -85% |
| PALLADIUM | 833 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 803 | 1 | 2% | 1% | -88% | -97% | -96% |
| USDJPY | 772 | 4 | 1% | 1% | -52% | -99% | -98% |
| AUDUSD | 361 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 314 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 9 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14216 | 57 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 13961 | 50 | 3% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3042 | 15 | 2% | 1% | -17% | -78% | -78% |
| 0.05–0.1% | 3154 | 11 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4674 | 17 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5347 | 27 | 6% | 3% | -45% | -87% | -87% |
| Over 0.5% | 2060 | 9 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 6767 | 32 | 4% | 2% | -46% | -88% | -87% |
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
| 10/22 8:44:51 AM | PLATINUM | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:44:51 AM | GBPUSD | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:44:35 AM | SOL | DOWN | 25 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/22 8:44:35 AM | HYPE | DOWN | 25 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/22 8:44:19 AM | NEAR | DOWN | 41 sec | +0.288% | 0¢ | ❌ Lost | $0.00 |
| 10/22 8:44:19 AM | WTI | UP | 41 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 8:44:19 AM | SILVER | DOWN | 41 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:44:03 AM | USDJPY | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:43:47 AM | ZEC | DOWN | 72 sec | +0.338% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:43:47 AM | AUDUSD | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:43:31 AM | DOGE | DOWN | 88 sec | +0.179% | 0¢ | ❌ Lost | $0.00 |
| 10/22 8:43:31 AM | XRP | DOWN | 88 sec | +0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:43:15 AM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:42:59 AM | BNB | DOWN | 2.0 min | +0.149% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:42:44 AM | BTC | DOWN | 2.3 min | +0.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:42:44 AM | EURUSD | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:42:28 AM | ETH | DOWN | 2.5 min | +0.219% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:41:17 AM | GOLD | DOWN | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:29:09 AM | SOL | UP | 51 sec | -0.222% | 0¢ | ❌ Lost | $0.00 |
| 10/22 8:28:45 AM | WTI | UP | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:28:37 AM | NATGAS | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:27:38 AM | ZEC | UP | 2.4 min | -0.787% | 0¢ | ❌ Lost | $0.00 |
| 10/22 8:27:38 AM | NEAR | UP | 2.4 min | -1.027% | 0¢ | ❌ Lost | $0.00 |
| 10/22 8:26:55 AM | PLATINUM | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:14:42 AM | SILVER | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:14:30 AM | PALLADIUM | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:14:20 AM | BTC | UP | 39 sec | -0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:14:18 AM | SOL | UP | 41 sec | -0.130% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:14:18 AM | HYPE | UP | 41 sec | -0.397% | 0¢ | ❌ Lost | $0.00 |
| 10/22 8:14:04 AM | NEAR | UP | 55 sec | -0.496% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
