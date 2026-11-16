# 15-Minute 1¢ Study

*Updated Mon Nov 16, 12:32 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4431 finished bets | 1% | $223.50 | +46% | +5.04¢ | $85.80 / $137.70 |

*Expect about **89 buys a day** (~$13.42/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4183 | $121.75 | +27% |
| Volatility model ≥ 2%, hold to the close | 8245 | $86.05 | +9% |
| Momentum model ≥ 2%, hold to the close | 6857 | $10.95 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 58755 | 58721 | 227 (0%) | 1.07% | -$3,963.35 (-55%) | Hold to the close: -$3,963.35 (-55%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 35376 | 4.6% | 0.4% (148) | -634% | ❌ Worse |
| Momentum model | 35376 | 4.5% | 0.4% (148) | -659% | ❌ Worse |
| Mean-reversion model | 35376 | 7.9% | 0.4% (148) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35376 | 148 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8245 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4431 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2549 | 30 | +70% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6857 | 57 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4183 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2723 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14482 | 103 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10077 | 85 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6684 | 61 | +4% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35582 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13910 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9229 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 58721 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$3,963.35 | -55% | — |
| Sell at 2¢ | 2359 | 4% | -$6,234.01 | -87% | 47 sec |
| Sell at 3¢ | 1589 | 3% | -$6,227.64 | -87% | 48 sec |
| Sell at 5¢ | 1088 | 2% | -$6,112.15 | -86% | 62 sec |
| Sell at 10¢ | 665 | 1% | -$5,864.20 | -82% | 65 sec |
| Sell at 25¢ | 351 | 1% | -$5,447.54 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,903.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2933 | 13 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 18995 | 104 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14794 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 21986 | 59 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3982 | 19 | 5% | 2% | -38% | -88% | -87% |
| SOL | 3977 | 18 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 3970 | 12 | 4% | 2% | -62% | -89% | -88% |
| DOGE | 3962 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 3959 | 20 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3950 | 17 | 6% | 3% | -46% | -82% | -82% |
| BTC | 3933 | 21 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 3931 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3918 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2081 | 5 | 5% | 2% | -71% | -82% | -84% |
| WTI | 2065 | 7 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2024 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1846 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1794 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1728 | 6 | 2% | 1% | -68% | -75% | -75% |
| GBPUSD | 1718 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1702 | 9 | 2% | 1% | -51% | -75% | -74% |
| USDJPY | 1680 | 6 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1656 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1239 | 6 | 2% | 1% | -55% | -89% | -89% |
| USDCAD | 1186 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 808 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 410 | 2 | 4% | 1% | -54% | -71% | -69% |
| 2YRRATE | 395 | 4 | 4% | 2% | -5% | -46% | -45% |
| 30YRRATE | 382 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 367 | 2 | 4% | 2% | -49% | -93% | -95% |
| INX | 58 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29870 | 113 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28851 | 114 | 4% | 2% | -55% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5403 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5843 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8938 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10974 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4415 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14411 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13940 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14313 | 63 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16057 | 49 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,080 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/16 12:29:48 PM | SOL | DOWN | 11 sec | +0.003% | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:29:32 PM | XRP | DOWN | 27 sec | +0.011% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:29:17 PM | PALLADIUM | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:29:17 PM | NEAR | DOWN | 42 sec | +0.108% | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:29:17 PM | WTI | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:29:17 PM | BNB | DOWN | 42 sec | +0.020% | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:29:17 PM | BTC | DOWN | 42 sec | +0.094% | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:29:17 PM | DOGE | DOWN | 42 sec | +0.133% | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:29:01 PM | USDJPY | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:28:45 PM | ETH | DOWN | 74 sec | +0.112% | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:27:40 PM | INX | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:27:24 PM | HYPE | DOWN | 2.6 min | +0.352% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:27:08 PM | USDCAD | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:27:08 PM | AUDUSD | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:26:18 PM | PLATINUM | DOWN | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:26:03 PM | GBPUSD | DOWN | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:25:46 PM | EURUSD | DOWN | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:25:14 PM | SILVER | DOWN | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:24:26 PM | GOLD | DOWN | 5.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:59 PM | 10YRRATE | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:59 PM | NATGAS | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:59 PM | USDJPY | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:43 PM | EURUSD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:43 PM | AUDUSD | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:43 PM | 5YRRATE | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:27 PM | GBPUSD | DOWN | 33 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:27 PM | HYPE | UP | 33 sec | -0.125% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:27 PM | COPPER | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:27 PM | 30YRRATE | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:11 PM | GOLD | DOWN | 49 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
