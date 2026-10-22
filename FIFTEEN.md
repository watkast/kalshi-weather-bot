# 15-Minute 1¢ Study

*Updated Thu Oct 22, 10:25 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2374 finished bets | 1% | $82.10 | +31% | +3.46¢ | $39.30 / $42.80 |

*Expect about **97 buys a day** (~$14.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2190 | $51.45 | +21% |
| Volatility model ≥ 2%, hold to the close | 4364 | $12.00 | +2% |
| Momentum model ≥ 2%, hold to the close | 3655 | -$24.20 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28291 | 28283 | 108 (0%) | 1.07% | -$1,933.95 (-56%) | Hold to the close: -$1,933.95 (-56%) |

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
| Volatility model | 18135 | 4.7% | 0.4% (78) | -645% | ❌ Worse |
| Momentum model | 18135 | 4.6% | 0.4% (78) | -670% | ❌ Worse |
| Mean-reversion model | 18135 | 7.9% | 0.4% (78) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18135 | 78 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4364 | 39 | +2% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2374 | 25 | +31% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1356 | 16 | +66% | -63% | -61% | -59% |
| Momentum model ≥ 2% | 3655 | 29 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2190 | 21 | +21% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1439 | 14 | +33% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7239 | 52 | -22% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5057 | 43 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3365 | 30 | +1% | -78% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18334 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6794 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3155 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28283 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 108 | 0% | -$1,933.95 | -56% | — |
| Sell at 2¢ | 1032 | 4% | -$3,037.63 | -88% | 47 sec |
| Sell at 3¢ | 706 | 2% | -$3,030.61 | -88% | 48 sec |
| Sell at 5¢ | 496 | 2% | -$2,983.55 | -87% | 61 sec |
| Sell at 10¢ | 306 | 1% | -$2,877.09 | -83% | 64 sec |
| Sell at 25¢ | 170 | 1% | -$2,645.25 | -77% | 86 sec |
| Sell at 50¢ | 112 | 0% | -$2,381.95 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1174 | 7 | 11% | 4% | -43% | -81% | -83% |
| 2–5 min | 9099 | 51 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7190 | 27 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 10816 | 23 | 1% | 0% | -70% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2055 | 12 | 5% | 2% | -27% | -89% | -89% |
| BNB | 2050 | 12 | 5% | 2% | -28% | -83% | -82% |
| HYPE | 2047 | 8 | 5% | 3% | -52% | -89% | -87% |
| ETH | 2037 | 10 | 6% | 3% | -41% | -86% | -86% |
| SOL | 2037 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2034 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2027 | 7 | 3% | 1% | -58% | -88% | -88% |
| NEAR | 2024 | 12 | 6% | 3% | -23% | -80% | -80% |
| BTC | 2023 | 12 | 5% | 2% | -21% | -88% | -89% |
| GOLD | 1110 | 3 | 4% | 1% | -68% | -82% | -84% |
| SILVER | 1074 | 4 | 3% | 1% | -57% | -82% | -82% |
| WTI | 1049 | 3 | 3% | 1% | -66% | -94% | -95% |
| PLATINUM | 934 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 924 | 3 | 1% | 1% | -70% | -77% | -77% |
| EURUSD | 862 | 3 | 2% | 1% | -68% | -85% | -85% |
| NATGAS | 861 | 5 | 2% | 1% | -46% | -86% | -85% |
| PALLADIUM | 834 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 809 | 1 | 2% | 1% | -88% | -97% | -96% |
| USDJPY | 777 | 4 | 1% | 1% | -52% | -99% | -98% |
| AUDUSD | 366 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 319 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 9 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14272 | 57 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 14011 | 51 | 3% | 1% | -58% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3048 | 15 | 2% | 1% | -17% | -78% | -78% |
| 0.05–0.1% | 3157 | 11 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4688 | 17 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5366 | 27 | 6% | 3% | -45% | -87% | -87% |
| Over 0.5% | 2071 | 10 | 7% | 3% | -50% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 6873 | 33 | 4% | 2% | -45% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,686 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 10:14:52 AM | COPPER | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:14:52 AM | NEAR | UP | 7 sec | -0.156% | 0¢ | ❌ Lost | $0.00 |
| 10/22 10:14:52 AM | HYPE | UP | 7 sec | +0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/22 10:14:35 AM | DOGE | UP | 25 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/22 10:14:19 AM | XRP | DOWN | 41 sec | +0.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 10:14:19 AM | BNB | UP | 41 sec | -0.051% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:14:19 AM | NATGAS | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:14:19 AM | USDJPY | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:14:03 AM | SOL | UP | 57 sec | -0.157% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:13:48 AM | BTC | UP | 71 sec | -0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 10:13:48 AM | ETH | UP | 71 sec | -0.080% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 10:13:17 AM | EURUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:13:17 AM | SILVER | UP | 1.7 min | — | 2¢ | ❌ Lost | $0.00 |
| 10/22 10:13:01 AM | GOLD | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 10:13:01 AM | PLATINUM | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:12:12 AM | WTI | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 10:10:21 AM | GBPUSD | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 10:10:05 AM | ZEC | DOWN | 4.9 min | +0.656% | 84¢ | ✅ Won | $13.85 |
| 10/22 9:59:51 AM | USDCAD | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 9:59:03 AM | BNB | DOWN | 57 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/22 9:58:31 AM | WTI | DOWN | 88 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 9:58:31 AM | PLATINUM | DOWN | 88 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 10/22 9:58:15 AM | XRP | DOWN | 1.7 min | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 9:57:44 AM | ZEC | DOWN | 2.3 min | +0.440% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 9:57:44 AM | DOGE | DOWN | 2.3 min | +0.210% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 9:57:28 AM | EURUSD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 9:57:12 AM | GBPUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 9:57:12 AM | SOL | DOWN | 2.8 min | +0.250% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 9:56:56 AM | AUDUSD | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 9:56:56 AM | ETH | DOWN | 3.1 min | +0.168% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
