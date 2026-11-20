# 15-Minute 1¢ Study

*Updated Fri Nov 20, 7:55 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4597 finished bets | 1% | $208.95 | +41% | +4.55¢ | $76.50 / $132.45 |

*Expect about **86 buys a day** (~$12.93/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4338 | $108.55 | +23% |
| Volatility model ≥ 2%, hold to the close | 8585 | $62.55 | +6% |
| Momentum model ≥ 2%, hold to the close | 7125 | -$17.25 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 63066 | 63028 | 243 (0%) | 1.07% | -$4,262.10 (-56%) | Hold to the close: -$4,262.10 (-56%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 37329 | 4.5% | 0.4% (156) | -635% | ❌ Worse |
| Momentum model | 37329 | 4.4% | 0.4% (156) | -661% | ❌ Worse |
| Mean-reversion model | 37329 | 7.9% | 0.4% (156) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37329 | 156 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8585 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4597 | 51 | +41% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2646 | 30 | +66% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 7125 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4338 | 41 | +23% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2831 | 26 | +31% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 15241 | 109 | -22% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10601 | 89 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7046 | 64 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37535 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15149 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10344 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 63028 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 243 | 0% | -$4,262.10 | -56% | — |
| Sell at 2¢ | 2559 | 4% | -$6,704.76 | -87% | 47 sec |
| Sell at 3¢ | 1724 | 3% | -$6,697.74 | -87% | 48 sec |
| Sell at 5¢ | 1177 | 2% | -$6,577.05 | -86% | 63 sec |
| Sell at 10¢ | 719 | 1% | -$6,316.21 | -82% | 65 sec |
| Sell at 25¢ | 385 | 1% | -$5,829.75 | -76% | 80 sec |
| Sell at 50¢ | 249 | 0% | -$5,269.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3237 | 17 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 20425 | 109 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 15753 | 54 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 23600 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4196 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4194 | 19 | 4% | 2% | -42% | -86% | -87% |
| HYPE | 4186 | 13 | 4% | 2% | -60% | -89% | -88% |
| DOGE | 4177 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4175 | 21 | 5% | 2% | -36% | -85% | -85% |
| ETH | 4171 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4153 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4149 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4134 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2250 | 7 | 5% | 2% | -62% | -82% | -84% |
| WTI | 2232 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2195 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 1999 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1954 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1889 | 8 | 2% | 1% | -60% | -96% | -95% |
| COPPER | 1882 | 6 | 2% | 1% | -70% | -77% | -77% |
| USDJPY | 1841 | 6 | 2% | 1% | -70% | -96% | -96% |
| NATGAS | 1839 | 10 | 2% | 1% | -49% | -76% | -76% |
| PALLADIUM | 1800 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1392 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1330 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 952 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 488 | 2 | 3% | 1% | -62% | -75% | -73% |
| 2YRRATE | 465 | 4 | 4% | 2% | -20% | -53% | -52% |
| 30YRRATE | 450 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 438 | 2 | 4% | 2% | -57% | -94% | -95% |
| INX | 97 | 1 | 2% | 1% | -4% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32183 | 125 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30845 | 118 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5573 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6074 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9390 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11688 | 52 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4801 | 23 | 7% | 3% | -50% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15327 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 14961 | 79 | 5% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15444 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17296 | 50 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,983 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/20 7:55:01 AM | NATGAS | DOWN | 5.0 min | — | — | In play | — |
| 11/20 7:55:01 AM | 10YRRATE | DOWN | 5.0 min | — | — | In play | — |
| 11/20 7:55:01 AM | 5YRRATE | DOWN | 5.0 min | — | — | In play | — |
| 11/20 7:54:45 AM | 30YRRATE | DOWN | 5.2 min | — | — | In play | — |
| 11/20 7:44:54 AM | PALLADIUM | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:44:38 AM | GBPUSD | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:44:38 AM | EURUSD | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:44:22 AM | SILVER | UP | 37 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/20 7:44:22 AM | USDJPY | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:44:22 AM | COPPER | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:44:06 AM | PLATINUM | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:43:48 AM | USDCAD | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:42:29 AM | 2YRRATE | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:42:13 AM | AUDUSD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:41:57 AM | NATGAS | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 7:41:41 AM | WTI | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 7:41:41 AM | BRENT | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:41:25 AM | 5YRRATE | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:41:09 AM | 30YRRATE | UP | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:41:09 AM | 10YRRATE | UP | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:40:53 AM | HYPE | UP | 4.1 min | -1.233% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 7:40:38 AM | NEAR | UP | 4.3 min | -1.504% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 7:40:38 AM | ETH | UP | 4.3 min | -0.914% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 7:40:38 AM | BNB | UP | 4.3 min | -0.658% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 7:40:22 AM | DOGE | UP | 4.6 min | -0.907% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 7:40:22 AM | BTC | UP | 4.6 min | -0.672% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 7:40:22 AM | SOL | UP | 4.6 min | -0.857% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 7:40:06 AM | XRP | UP | 4.9 min | -0.926% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 7:40:06 AM | ZEC | UP | 4.9 min | -1.782% | 0¢ | ❌ Lost | $0.00 |
| 11/20 7:29:53 AM | NATGAS | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
