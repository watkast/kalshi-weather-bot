# 15-Minute 1¢ Study

*Updated Fri Nov 20, 8:47 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

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
| 63162 | 63128 | 243 (0%) | 1.07% | -$4,276.65 (-56%) | Hold to the close: -$4,276.65 (-56%) |

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
| Volatility model | 37365 | 4.5% | 0.4% (156) | -635% | ❌ Worse |
| Momentum model | 37365 | 4.4% | 0.4% (156) | -661% | ❌ Worse |
| Mean-reversion model | 37365 | 7.9% | 0.4% (156) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37365 | 156 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8585 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4597 | 51 | +41% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2646 | 30 | +66% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 7126 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4338 | 41 | +23% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2831 | 26 | +31% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 15260 | 109 | -22% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10610 | 89 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7051 | 64 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37571 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15177 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10380 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 63128 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 243 | 0% | -$4,276.65 | -56% | — |
| Sell at 2¢ | 2560 | 4% | -$6,719.05 | -88% | 47 sec |
| Sell at 3¢ | 1725 | 3% | -$6,711.90 | -87% | 48 sec |
| Sell at 5¢ | 1178 | 2% | -$6,590.95 | -86% | 63 sec |
| Sell at 10¢ | 719 | 1% | -$6,330.76 | -82% | 65 sec |
| Sell at 25¢ | 385 | 1% | -$5,844.30 | -76% | 80 sec |
| Sell at 50¢ | 249 | 0% | -$5,283.90 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3259 | 17 | 10% | 4% | -51% | -82% | -83% |
| 2–5 min | 20477 | 109 | 7% | 3% | -48% | -86% | -87% |
| 1–2 min | 15768 | 54 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 23611 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4200 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4198 | 19 | 4% | 2% | -42% | -86% | -87% |
| HYPE | 4190 | 13 | 4% | 2% | -60% | -89% | -88% |
| DOGE | 4181 | 11 | 4% | 2% | -67% | -90% | -89% |
| BNB | 4179 | 21 | 5% | 2% | -36% | -86% | -85% |
| ETH | 4175 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4157 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4153 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4138 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2254 | 7 | 5% | 2% | -62% | -82% | -84% |
| WTI | 2234 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2199 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2003 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1957 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1892 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1886 | 6 | 2% | 1% | -70% | -77% | -77% |
| USDJPY | 1845 | 6 | 2% | 1% | -70% | -96% | -96% |
| NATGAS | 1843 | 10 | 2% | 1% | -49% | -76% | -76% |
| PALLADIUM | 1804 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1396 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1332 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 954 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 492 | 2 | 3% | 1% | -62% | -75% | -74% |
| 2YRRATE | 469 | 4 | 4% | 2% | -20% | -54% | -52% |
| 30YRRATE | 454 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 442 | 2 | 4% | 2% | -58% | -94% | -95% |
| INX | 101 | 1 | 2% | 1% | -8% | -97% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32247 | 125 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30881 | 118 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5573 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6074 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9390 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11694 | 52 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4831 | 23 | 7% | 3% | -50% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15327 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15061 | 79 | 5% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15444 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17296 | 50 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,978 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/20 8:44:53 AM | PALLADIUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:44:53 AM | NATGAS | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:44:21 AM | COPPER | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:44:21 AM | 30YRRATE | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:43:49 AM | INX | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:43:49 AM | AUDUSD | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:43:17 AM | USDJPY | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:43:17 AM | 2YRRATE | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:43:17 AM | 10YRRATE | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:43:00 AM | 5YRRATE | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:42:46 AM | GBPUSD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:42:46 AM | XRP | UP | 2.2 min | -0.666% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:42:30 AM | NEAR | UP | 2.5 min | -1.623% | 0¢ | ❌ Lost | $0.00 |
| 11/20 8:42:30 AM | DOGE | UP | 2.5 min | -1.044% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:42:14 AM | BTC | UP | 2.8 min | -0.555% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:41:58 AM | USDCAD | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:41:58 AM | BNB | UP | 3.0 min | -0.600% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:41:42 AM | HYPE | UP | 3.3 min | -1.258% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:41:42 AM | SOL | UP | 3.3 min | -0.837% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:41:42 AM | ETH | UP | 3.3 min | -0.788% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:41:26 AM | ZEC | UP | 3.6 min | -1.612% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:40:07 AM | EURUSD | DOWN | 4.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:39:35 AM | PLATINUM | DOWN | 5.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:39:35 AM | SILVER | DOWN | 5.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:37:12 AM | GOLD | DOWN | 7.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:29:28 AM | NATGAS | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:29:12 AM | EURUSD | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:28:08 AM | USDJPY | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 8:28:08 AM | AUDUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 8:27:37 AM | PALLADIUM | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
