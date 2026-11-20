# 15-Minute 1¢ Study

*Updated Fri Nov 20, 8:36 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4597 finished bets | 1% | $208.95 | +41% | +4.55¢ | $76.50 / $132.45 |

*Expect about **86 buys a day** (~$12.92/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4338 | $108.55 | +23% |
| Volatility model ≥ 2%, hold to the close | 8585 | $62.55 | +6% |
| Momentum model ≥ 2%, hold to the close | 7126 | -$17.40 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 63137 | 63103 | 243 (0%) | 1.07% | -$4,273.05 (-56%) | Hold to the close: -$4,273.05 (-56%) |

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
| Volatility model | 37356 | 4.5% | 0.4% (156) | -635% | ❌ Worse |
| Momentum model | 37356 | 4.4% | 0.4% (156) | -661% | ❌ Worse |
| Mean-reversion model | 37356 | 7.9% | 0.4% (156) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37356 | 156 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8585 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4597 | 51 | +41% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2646 | 30 | +66% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 7126 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4338 | 41 | +23% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2831 | 26 | +31% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 15257 | 109 | -22% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10607 | 89 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7051 | 64 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37562 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15171 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10370 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 63103 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 243 | 0% | -$4,273.05 | -56% | — |
| Sell at 2¢ | 2560 | 4% | -$6,715.45 | -87% | 47 sec |
| Sell at 3¢ | 1725 | 3% | -$6,708.30 | -87% | 48 sec |
| Sell at 5¢ | 1178 | 2% | -$6,587.35 | -86% | 63 sec |
| Sell at 10¢ | 719 | 1% | -$6,327.16 | -82% | 65 sec |
| Sell at 25¢ | 385 | 1% | -$5,840.70 | -76% | 80 sec |
| Sell at 50¢ | 249 | 0% | -$5,280.30 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3256 | 17 | 10% | 4% | -50% | -82% | -83% |
| 2–5 min | 20465 | 109 | 7% | 3% | -47% | -86% | -87% |
| 1–2 min | 15762 | 54 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 23607 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4199 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4197 | 19 | 4% | 2% | -42% | -86% | -87% |
| HYPE | 4189 | 13 | 4% | 2% | -60% | -89% | -88% |
| DOGE | 4180 | 11 | 4% | 2% | -67% | -90% | -89% |
| BNB | 4178 | 21 | 5% | 2% | -36% | -86% | -85% |
| ETH | 4174 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4156 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4152 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4137 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2253 | 7 | 5% | 2% | -62% | -82% | -84% |
| WTI | 2234 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2198 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2002 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1956 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1891 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1885 | 6 | 2% | 1% | -70% | -77% | -77% |
| USDJPY | 1844 | 6 | 2% | 1% | -70% | -96% | -96% |
| NATGAS | 1842 | 10 | 2% | 1% | -49% | -76% | -76% |
| PALLADIUM | 1803 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1395 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1331 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 954 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 491 | 2 | 3% | 1% | -62% | -75% | -74% |
| 2YRRATE | 468 | 4 | 4% | 2% | -20% | -53% | -52% |
| 30YRRATE | 453 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 441 | 2 | 4% | 2% | -58% | -94% | -95% |
| INX | 100 | 1 | 2% | 1% | -7% | -97% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32231 | 125 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30872 | 118 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5573 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6074 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9390 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11694 | 52 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4822 | 23 | 7% | 3% | -50% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15327 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15036 | 79 | 5% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15444 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17296 | 50 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,980 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/20 8:29:28 AM | NATGAS | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:29:12 AM | EURUSD | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:28:08 AM | USDJPY | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:28:08 AM | AUDUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:27:37 AM | PALLADIUM | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:27:05 AM | GBPUSD | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:26:21 AM | BRENT | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:26:05 AM | WTI | UP | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:25:17 AM | INX | UP | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:25:01 AM | NEAR | UP | 5.0 min | -2.009% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:25:01 AM | 2YRRATE | UP | 5.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:25:01 AM | 30YRRATE | UP | 5.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:24:27 AM | COPPER | UP | 5.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:24:27 AM | 10YRRATE | UP | 5.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:24:27 AM | 5YRRATE | UP | 5.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:24:27 AM | SILVER | UP | 5.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:24:27 AM | GOLD | UP | 5.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:24:11 AM | PLATINUM | UP | 5.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:24:11 AM | XRP | UP | 5.8 min | -1.889% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:23:55 AM | HYPE | UP | 6.1 min | -1.334% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:23:40 AM | ZEC | UP | 6.3 min | -2.990% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:23:24 AM | DOGE | UP | 6.6 min | -1.885% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:23:08 AM | SOL | UP | 6.8 min | -1.639% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:22:20 AM | BTC | UP | 7.7 min | -1.226% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:21:32 AM | BNB | UP | 8.5 min | -1.551% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:20:29 AM | ETH | UP | 9.5 min | -2.075% | 2¢ | ❌ Lost | -$0.15 |
| 11/20 8:14:54 AM | PALLADIUM | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:14:06 AM | GBPUSD | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:14:06 AM | EURUSD | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:13:34 AM | USDJPY | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
