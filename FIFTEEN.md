# 15-Minute 1¢ Study

*Updated Mon Nov 16, 4:23 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4424 finished bets | 1% | $223.95 | +46% | +5.06¢ | $86.10 / $137.85 |

*Expect about **90 buys a day** (~$13.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4176 | $122.20 | +27% |
| Volatility model ≥ 2%, hold to the close | 8236 | $86.65 | +9% |
| Momentum model ≥ 2%, hold to the close | 6849 | $11.40 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 58640 | 58619 | 227 (0%) | 1.07% | -$3,950.90 (-55%) | Hold to the close: -$3,950.90 (-55%) |

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
| Volatility model | 35334 | 4.6% | 0.4% (148) | -633% | ❌ Worse |
| Momentum model | 35334 | 4.5% | 0.4% (148) | -658% | ❌ Worse |
| Mean-reversion model | 35334 | 7.9% | 0.4% (148) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35334 | 148 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8236 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4424 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2543 | 30 | +71% | -63% | -61% | -57% |
| Momentum model ≥ 2% | 6849 | 57 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4176 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2719 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14465 | 103 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10062 | 85 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6671 | 61 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35540 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13884 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9195 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 58619 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$3,950.90 | -55% | — |
| Sell at 2¢ | 2355 | 4% | -$6,222.60 | -87% | 47 sec |
| Sell at 3¢ | 1588 | 3% | -$6,215.58 | -87% | 48 sec |
| Sell at 5¢ | 1088 | 2% | -$6,099.70 | -86% | 62 sec |
| Sell at 10¢ | 665 | 1% | -$5,851.75 | -82% | 65 sec |
| Sell at 25¢ | 351 | 1% | -$5,435.09 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,891.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2932 | 13 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 18959 | 104 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14774 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 21941 | 59 | 1% | 0% | -61% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3978 | 19 | 5% | 2% | -37% | -88% | -87% |
| SOL | 3972 | 18 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 3966 | 12 | 4% | 2% | -62% | -89% | -88% |
| DOGE | 3957 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 3954 | 20 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3945 | 17 | 6% | 3% | -46% | -82% | -82% |
| BTC | 3928 | 21 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 3926 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3914 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2076 | 5 | 5% | 2% | -71% | -82% | -84% |
| WTI | 2063 | 7 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2021 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1842 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1789 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1724 | 6 | 2% | 1% | -68% | -75% | -75% |
| GBPUSD | 1713 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1699 | 9 | 2% | 1% | -51% | -75% | -74% |
| USDJPY | 1676 | 6 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1652 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1234 | 6 | 2% | 1% | -55% | -89% | -89% |
| USDCAD | 1184 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 807 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 407 | 2 | 4% | 1% | -54% | -71% | -69% |
| 2YRRATE | 393 | 4 | 4% | 2% | -5% | -46% | -45% |
| 30YRRATE | 380 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 365 | 2 | 4% | 2% | -49% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29827 | 113 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28792 | 114 | 4% | 2% | -54% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5397 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5841 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8923 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10961 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4409 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14387 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13903 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14272 | 63 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16057 | 49 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,084 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/16 4:14:49 AM | 10YRRATE | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:14:49 AM | NATGAS | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:14:49 AM | ETH | DOWN | 10 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 11/16 4:14:49 AM | USDJPY | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:14:33 AM | ZEC | UP | 26 sec | -0.156% | 0¢ | ❌ Lost | $0.00 |
| 11/16 4:14:17 AM | BTC | DOWN | 42 sec | +0.099% | 0¢ | ❌ Lost | $0.00 |
| 11/16 4:14:17 AM | BNB | UP | 42 sec | -0.110% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:14:17 AM | BRENT | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:14:01 AM | 5YRRATE | DOWN | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:14:01 AM | COPPER | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:14:01 AM | WTI | UP | 59 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/16 4:13:44 AM | NEAR | DOWN | 76 sec | +0.222% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:13:44 AM | XRP | DOWN | 76 sec | +0.210% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:13:44 AM | PLATINUM | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 4:08:41 AM | DOGE | DOWN | 6.3 min | +0.569% | 2¢ | ❌ Lost | -$0.15 |
| 11/16 3:59:33 AM | BTC | DOWN | 26 sec | +0.046% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:59:17 AM | NATGAS | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:59:17 AM | ZEC | DOWN | 43 sec | +0.179% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:59:00 AM | SILVER | DOWN | 60 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:58:44 AM | 2YRRATE | DOWN | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:58:28 AM | 30YRRATE | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:58:28 AM | COPPER | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:58:13 AM | 10YRRATE | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:57:58 AM | NEAR | DOWN | 2.0 min | +0.427% | 0¢ | ❌ Lost | $0.00 |
| 11/16 3:57:58 AM | HYPE | DOWN | 2.0 min | +0.318% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:57:42 AM | EURUSD | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:57:42 AM | SOL | DOWN | 2.3 min | +0.335% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:57:42 AM | BNB | DOWN | 2.3 min | +0.127% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:57:42 AM | ETH | DOWN | 2.3 min | +0.258% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:57:42 AM | 5YRRATE | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
