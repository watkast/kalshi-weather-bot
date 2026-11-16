# 15-Minute 1¢ Study

*Updated Mon Nov 16, 1:14 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

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
| Volatility model ≥ 2%, hold to the close | 8246 | $85.90 | +9% |
| Momentum model ≥ 2%, hold to the close | 6857 | $10.95 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 58811 | 58766 | 227 (0%) | 1.07% | -$3,969.35 (-56%) | Hold to the close: -$3,969.35 (-56%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 35392 | 4.6% | 0.4% (148) | -634% | ❌ Worse |
| Momentum model | 35392 | 4.5% | 0.4% (148) | -659% | ❌ Worse |
| Mean-reversion model | 35392 | 7.9% | 0.4% (148) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35392 | 148 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8246 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4431 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2549 | 30 | +70% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6857 | 57 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4183 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2723 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14491 | 103 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10085 | 85 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6689 | 61 | +4% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35598 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13923 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9245 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 58766 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$3,969.35 | -56% | — |
| Sell at 2¢ | 2362 | 4% | -$6,239.23 | -87% | 47 sec |
| Sell at 3¢ | 1592 | 3% | -$6,232.47 | -87% | 48 sec |
| Sell at 5¢ | 1090 | 2% | -$6,116.85 | -86% | 62 sec |
| Sell at 10¢ | 666 | 1% | -$5,868.89 | -82% | 65 sec |
| Sell at 25¢ | 352 | 1% | -$5,450.23 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,909.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2943 | 13 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 19014 | 104 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14801 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 21995 | 59 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3984 | 19 | 5% | 2% | -38% | -88% | -87% |
| SOL | 3979 | 18 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 3971 | 12 | 4% | 2% | -62% | -89% | -88% |
| DOGE | 3963 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 3961 | 20 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3952 | 17 | 6% | 3% | -46% | -82% | -82% |
| BTC | 3935 | 21 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 3933 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3920 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2083 | 5 | 5% | 2% | -71% | -82% | -84% |
| WTI | 2066 | 7 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2026 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1848 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1796 | 6 | 3% | 1% | -69% | -90% | -90% |
| COPPER | 1730 | 6 | 2% | 1% | -68% | -75% | -75% |
| GBPUSD | 1719 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1704 | 9 | 2% | 1% | -51% | -75% | -74% |
| USDJPY | 1682 | 6 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1657 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1240 | 6 | 2% | 1% | -55% | -89% | -89% |
| USDCAD | 1186 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 809 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 412 | 2 | 4% | 1% | -55% | -71% | -69% |
| 2YRRATE | 397 | 4 | 4% | 2% | -6% | -46% | -45% |
| 30YRRATE | 384 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 369 | 2 | 4% | 2% | -49% | -93% | -95% |
| INX | 60 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29893 | 113 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28873 | 114 | 4% | 2% | -55% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5403 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5844 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8940 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10983 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4419 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14411 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13940 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14358 | 63 | 4% | 2% | -48% | -87% | -87% |
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
| 11/16 1:14:12 PM | SOL | DOWN | 47 sec | +0.081% | — | In play | — |
| 11/16 1:14:12 PM | NATGAS | UP | 47 sec | — | — | In play | — |
| 11/16 1:14:12 PM | NEAR | DOWN | 47 sec | -0.031% | — | In play | — |
| 11/16 1:14:12 PM | ZEC | UP | 47 sec | -0.347% | — | In play | — |
| 11/16 1:13:55 PM | DOGE | DOWN | 64 sec | +0.136% | — | In play | — |
| 11/16 1:13:23 PM | 30YRRATE | UP | 1.6 min | — | — | In play | — |
| 11/16 1:13:07 PM | 10YRRATE | UP | 1.9 min | — | — | In play | — |
| 11/16 1:13:07 PM | 2YRRATE | UP | 1.9 min | — | — | In play | — |
| 11/16 1:13:07 PM | 5YRRATE | UP | 1.9 min | — | — | In play | — |
| 11/16 1:11:29 PM | INX | UP | 3.5 min | — | — | In play | — |
| 11/16 1:11:29 PM | HYPE | DOWN | 3.5 min | +0.905% | — | In play | — |
| 11/16 12:59:56 PM | NATGAS | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:59:40 PM | PLATINUM | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:59:40 PM | COPPER | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:57:29 PM | EURUSD | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:56:55 PM | GBPUSD | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:56:08 PM | GOLD | DOWN | 3.9 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/16 12:56:08 PM | 30YRRATE | DOWN | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:56:08 PM | SILVER | DOWN | 3.9 min | — | 5¢ | ❌ Lost | -$0.15 |
| 11/16 12:55:20 PM | 10YRRATE | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:55:20 PM | 5YRRATE | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:55:03 PM | XRP | DOWN | 4.9 min | +0.472% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:55:03 PM | NEAR | DOWN | 4.9 min | +0.447% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:54:45 PM | SOL | DOWN | 5.2 min | +0.518% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:54:45 PM | INX | DOWN | 5.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:54:45 PM | DOGE | DOWN | 5.2 min | +0.441% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:54:45 PM | ETH | DOWN | 5.2 min | +0.384% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:54:29 PM | HYPE | DOWN | 5.5 min | +0.739% | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:54:29 PM | BNB | DOWN | 5.5 min | +0.231% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:54:13 PM | BTC | DOWN | 5.8 min | +0.337% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
