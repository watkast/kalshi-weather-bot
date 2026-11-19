# 15-Minute 1¢ Study

*Updated Thu Nov 19, 6:43 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4563 finished bets | 1% | $211.50 | +42% | +4.64¢ | $78.00 / $133.50 |

*Expect about **87 buys a day** (~$13.09/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4299 | $111.85 | +24% |
| Volatility model ≥ 2%, hold to the close | 8509 | $70.05 | +7% |
| Momentum model ≥ 2%, hold to the close | 7056 | -$10.20 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 61901 | 61856 | 239 (0%) | 1.07% | -$4,178.60 (-56%) | Hold to the close: -$4,178.60 (-56%) |

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
| Volatility model | 36792 | 4.5% | 0.4% (154) | -635% | ❌ Worse |
| Momentum model | 36792 | 4.4% | 0.4% (154) | -660% | ❌ Worse |
| Mean-reversion model | 36792 | 7.9% | 0.4% (154) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36792 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8509 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4563 | 51 | +42% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2623 | 30 | +67% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7056 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4299 | 41 | +24% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2802 | 26 | +33% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 15047 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10473 | 89 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6961 | 64 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36998 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14811 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10047 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 61856 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 239 | 0% | -$4,178.60 | -56% | — |
| Sell at 2¢ | 2503 | 4% | -$6,579.82 | -87% | 47 sec |
| Sell at 3¢ | 1689 | 3% | -$6,571.89 | -87% | 48 sec |
| Sell at 5¢ | 1152 | 2% | -$6,453.80 | -86% | 63 sec |
| Sell at 10¢ | 704 | 1% | -$6,196.36 | -82% | 65 sec |
| Sell at 25¢ | 377 | 1% | -$5,730.73 | -76% | 80 sec |
| Sell at 50¢ | 246 | 0% | -$5,178.10 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3145 | 17 | 10% | 4% | -49% | -82% | -83% |
| 2–5 min | 20062 | 108 | 7% | 3% | -47% | -86% | -87% |
| 1–2 min | 15475 | 52 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 23161 | 62 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4137 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4135 | 19 | 4% | 2% | -41% | -86% | -86% |
| HYPE | 4126 | 12 | 4% | 2% | -63% | -90% | -88% |
| DOGE | 4117 | 11 | 4% | 2% | -66% | -89% | -89% |
| BNB | 4116 | 21 | 5% | 2% | -35% | -85% | -85% |
| ETH | 4111 | 19 | 7% | 3% | -42% | -82% | -82% |
| BTC | 4092 | 21 | 5% | 2% | -30% | -86% | -88% |
| NEAR | 4090 | 18 | 5% | 2% | -42% | -85% | -86% |
| XRP | 4074 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2209 | 6 | 5% | 2% | -67% | -82% | -84% |
| WTI | 2187 | 7 | 4% | 1% | -61% | -91% | -92% |
| SILVER | 2146 | 9 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1956 | 4 | 3% | 1% | -81% | -95% | -95% |
| EURUSD | 1912 | 7 | 2% | 1% | -66% | -91% | -90% |
| COPPER | 1841 | 6 | 2% | 1% | -70% | -76% | -76% |
| GBPUSD | 1840 | 8 | 2% | 1% | -59% | -96% | -95% |
| NATGAS | 1800 | 10 | 2% | 1% | -48% | -76% | -75% |
| USDJPY | 1796 | 6 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1759 | 4 | 1% | 0% | -79% | -93% | -93% |
| AUDUSD | 1349 | 6 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1289 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 913 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 471 | 2 | 3% | 1% | -60% | -75% | -73% |
| 2YRRATE | 446 | 4 | 4% | 2% | -16% | -52% | -51% |
| 30YRRATE | 431 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 421 | 2 | 4% | 1% | -56% | -94% | -96% |
| INX | 92 | 1 | 2% | 1% | +1% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31515 | 123 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30341 | 116 | 4% | 2% | -56% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5533 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 6018 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9269 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11500 | 50 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4669 | 23 | 7% | 3% | -48% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15189 | 47 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14610 | 78 | 4% | 2% | -39% | -85% | -85% |
| Afternoon (12–6pm) | 15130 | 65 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16927 | 49 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,010 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/19 6:43:21 AM | BNB | DOWN | 1.6 min | +0.037% | — | In play | — |
| 11/19 6:43:05 AM | SILVER | UP | 1.9 min | — | — | In play | — |
| 11/19 6:42:33 AM | SOL | DOWN | 2.5 min | +0.210% | — | In play | — |
| 11/19 6:42:33 AM | XRP | DOWN | 2.5 min | +0.203% | — | In play | — |
| 11/19 6:42:33 AM | NEAR | UP | 2.5 min | -0.490% | — | In play | — |
| 11/19 6:42:17 AM | GBPUSD | DOWN | 2.7 min | — | — | In play | — |
| 11/19 6:42:17 AM | 2YRRATE | UP | 2.7 min | — | — | In play | — |
| 11/19 6:42:17 AM | 5YRRATE | UP | 2.7 min | — | — | In play | — |
| 11/19 6:42:01 AM | GOLD | UP | 3.0 min | — | — | In play | — |
| 11/19 6:40:43 AM | PALLADIUM | UP | 4.3 min | — | — | In play | — |
| 11/19 6:39:55 AM | PLATINUM | UP | 5.1 min | — | — | In play | — |
| 11/19 6:29:47 AM | DOGE | DOWN | 13 sec | +0.002% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 6:29:47 AM | PLATINUM | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:29:47 AM | AUDUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:29:31 AM | WTI | DOWN | 29 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 6:29:31 AM | XRP | UP | 29 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 11/19 6:29:15 AM | SOL | DOWN | 45 sec | +0.069% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:29:15 AM | GOLD | DOWN | 45 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/19 6:29:15 AM | NEAR | DOWN | 45 sec | +0.274% | 0¢ | ❌ Lost | $0.00 |
| 11/19 6:29:15 AM | NATGAS | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:29:15 AM | USDJPY | DOWN | 45 sec | — | 21¢ | ❌ Lost | -$0.15 |
| 11/19 6:28:27 AM | BTC | UP | 1.5 min | -0.153% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 6:27:40 AM | USDCAD | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:27:08 AM | SILVER | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 6:27:08 AM | COPPER | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:26:21 AM | ETH | UP | 3.6 min | -0.330% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 6:25:17 AM | GBPUSD | UP | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:14:57 AM | AUDUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:14:57 AM | WTI | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/19 6:14:25 AM | ETH | DOWN | 35 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
