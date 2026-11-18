# 15-Minute 1¢ Study

*Updated Wed Nov 18, 2:04 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4531 finished bets | 1% | $214.05 | +43% | +4.72¢ | $80.10 / $133.95 |

*Expect about **88 buys a day** (~$13.17/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4262 | $115.15 | +25% |
| Volatility model ≥ 2%, hold to the close | 8455 | $75.45 | +7% |
| Momentum model ≥ 2%, hold to the close | 7005 | -$5.25 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 61103 | 61069 | 237 (0%) | 1.07% | -$4,114.80 (-55%) | Hold to the close: -$4,114.80 (-55%) |

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
| Volatility model | 36436 | 4.5% | 0.4% (154) | -629% | ❌ Worse |
| Momentum model | 36436 | 4.4% | 0.4% (154) | -654% | ❌ Worse |
| Mean-reversion model | 36436 | 7.9% | 0.4% (154) | -765% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36436 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8455 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4531 | 51 | +43% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2605 | 30 | +68% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7005 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4262 | 41 | +25% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2778 | 26 | +33% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14935 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10394 | 89 | -5% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6908 | 64 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36642 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14569 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9858 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 61069 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,114.80 | -55% | — |
| Sell at 2¢ | 2465 | 4% | -$6,497.90 | -87% | 47 sec |
| Sell at 3¢ | 1664 | 3% | -$6,489.84 | -87% | 48 sec |
| Sell at 5¢ | 1134 | 2% | -$6,373.70 | -86% | 63 sec |
| Sell at 10¢ | 691 | 1% | -$6,121.59 | -82% | 65 sec |
| Sell at 25¢ | 369 | 1% | -$5,665.41 | -76% | 80 sec |
| Sell at 50¢ | 244 | 0% | -$5,113.80 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3114 | 17 | 10% | 4% | -48% | -82% | -83% |
| 2–5 min | 19802 | 108 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 15295 | 51 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 22845 | 61 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4097 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4094 | 19 | 4% | 2% | -41% | -86% | -87% |
| HYPE | 4089 | 12 | 4% | 2% | -63% | -89% | -88% |
| DOGE | 4077 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4077 | 21 | 5% | 2% | -35% | -85% | -85% |
| ETH | 4070 | 19 | 7% | 3% | -42% | -82% | -82% |
| BTC | 4052 | 21 | 5% | 2% | -30% | -86% | -88% |
| NEAR | 4051 | 18 | 5% | 2% | -42% | -85% | -86% |
| XRP | 4035 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2177 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2155 | 7 | 4% | 1% | -61% | -91% | -92% |
| SILVER | 2114 | 9 | 5% | 2% | -49% | -83% | -83% |
| PLATINUM | 1926 | 4 | 3% | 1% | -81% | -95% | -95% |
| EURUSD | 1878 | 7 | 3% | 1% | -65% | -91% | -90% |
| COPPER | 1811 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1805 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1774 | 10 | 2% | 1% | -47% | -75% | -75% |
| USDJPY | 1764 | 6 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1728 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1315 | 6 | 2% | 1% | -57% | -89% | -90% |
| USDCAD | 1258 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 884 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 463 | 2 | 3% | 1% | -60% | -74% | -73% |
| 2YRRATE | 442 | 4 | 4% | 2% | -16% | -51% | -50% |
| 30YRRATE | 425 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 416 | 2 | 4% | 1% | -55% | -94% | -96% |
| INX | 92 | 1 | 2% | 1% | +1% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31134 | 121 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 29935 | 116 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5498 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5959 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9169 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11378 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4629 | 23 | 7% | 3% | -48% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14961 | 45 | 4% | 2% | -66% | -88% | -88% |
| Morning (6am–12pm) | 14575 | 78 | 4% | 2% | -39% | -85% | -85% |
| Afternoon (12–6pm) | 14975 | 65 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16558 | 49 | 4% | 2% | -66% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,029 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/18 1:59:29 PM | BTC | DOWN | 31 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 11/18 1:59:14 PM | GBPUSD | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:58:56 PM | EURUSD | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:58:56 PM | ZEC | UP | 64 sec | -0.317% | 0¢ | ❌ Lost | $0.00 |
| 11/18 1:58:40 PM | SILVER | UP | 80 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:58:40 PM | SOL | DOWN | 80 sec | +0.161% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:58:09 PM | XRP | DOWN | 1.8 min | +0.176% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:58:09 PM | GOLD | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:58:09 PM | PLATINUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:58:09 PM | BRENT | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:57:18 PM | WTI | UP | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:57:18 PM | USDCAD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:57:18 PM | HYPE | DOWN | 2.7 min | +0.351% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:57:18 PM | ETH | DOWN | 2.7 min | +0.220% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:57:18 PM | DOGE | DOWN | 2.7 min | +0.359% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:56:47 PM | NEAR | DOWN | 3.2 min | +0.267% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:44:44 PM | 10YRRATE | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:44:29 PM | XRP | DOWN | 30 sec | +0.062% | 0¢ | ❌ Lost | $0.00 |
| 11/18 1:44:29 PM | HYPE | DOWN | 30 sec | +0.036% | 0¢ | ❌ Lost | $0.00 |
| 11/18 1:44:29 PM | BNB | UP | 30 sec | -0.068% | 0¢ | ❌ Lost | $0.00 |
| 11/18 1:44:29 PM | 5YRRATE | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:44:29 PM | ETH | UP | 30 sec | -0.090% | 0¢ | ❌ Lost | $0.00 |
| 11/18 1:44:29 PM | BRENT | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:44:29 PM | DOGE | UP | 30 sec | -0.113% | 0¢ | ❌ Lost | $0.00 |
| 11/18 1:43:58 PM | PALLADIUM | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:43:42 PM | INX | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:43:26 PM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:43:10 PM | BTC | UP | 1.8 min | -0.144% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:43:10 PM | AUDUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:43:10 PM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
