# 15-Minute 1¢ Study

*Updated Thu Nov 19, 8:06 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4567 finished bets | 1% | $211.05 | +42% | +4.62¢ | $77.70 / $133.35 |

*Expect about **87 buys a day** (~$13.09/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4302 | $111.55 | +24% |
| Volatility model ≥ 2%, hold to the close | 8518 | $68.85 | +7% |
| Momentum model ≥ 2%, hold to the close | 7060 | -$10.65 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 62017 | 61983 | 239 (0%) | 1.07% | -$4,193.75 (-56%) | Hold to the close: -$4,193.75 (-56%) |

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
| Volatility model | 36843 | 4.5% | 0.4% (154) | -635% | ❌ Worse |
| Momentum model | 36843 | 4.4% | 0.4% (154) | -661% | ❌ Worse |
| Mean-reversion model | 36843 | 7.9% | 0.4% (154) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36843 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8518 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4567 | 51 | +42% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2626 | 30 | +67% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7060 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4302 | 41 | +24% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2805 | 26 | +32% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 15063 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10484 | 89 | -6% | -79% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6972 | 64 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37049 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14840 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10094 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 61983 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 239 | 0% | -$4,193.75 | -56% | — |
| Sell at 2¢ | 2513 | 4% | -$6,592.37 | -87% | 47 sec |
| Sell at 3¢ | 1695 | 3% | -$6,584.70 | -87% | 48 sec |
| Sell at 5¢ | 1157 | 2% | -$6,465.70 | -86% | 63 sec |
| Sell at 10¢ | 707 | 1% | -$6,207.58 | -82% | 65 sec |
| Sell at 25¢ | 378 | 1% | -$5,742.57 | -76% | 80 sec |
| Sell at 50¢ | 246 | 0% | -$5,193.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3147 | 17 | 10% | 4% | -49% | -82% | -83% |
| 2–5 min | 20111 | 108 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 15503 | 52 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 23209 | 62 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4143 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4140 | 19 | 4% | 2% | -41% | -86% | -86% |
| HYPE | 4132 | 12 | 4% | 2% | -63% | -89% | -88% |
| DOGE | 4122 | 11 | 4% | 2% | -66% | -89% | -89% |
| BNB | 4121 | 21 | 5% | 2% | -35% | -85% | -85% |
| ETH | 4117 | 19 | 7% | 3% | -42% | -82% | -82% |
| BTC | 4098 | 21 | 5% | 2% | -30% | -86% | -88% |
| NEAR | 4096 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4080 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2212 | 6 | 5% | 2% | -67% | -82% | -84% |
| WTI | 2191 | 7 | 4% | 1% | -61% | -91% | -92% |
| SILVER | 2152 | 9 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1959 | 4 | 3% | 1% | -81% | -95% | -95% |
| EURUSD | 1918 | 7 | 3% | 1% | -66% | -91% | -90% |
| GBPUSD | 1846 | 8 | 2% | 1% | -60% | -96% | -95% |
| COPPER | 1844 | 6 | 2% | 1% | -70% | -76% | -76% |
| NATGAS | 1803 | 10 | 2% | 1% | -48% | -76% | -75% |
| USDJPY | 1802 | 6 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1763 | 4 | 1% | 0% | -79% | -93% | -93% |
| AUDUSD | 1355 | 6 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1294 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 916 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 474 | 2 | 3% | 1% | -61% | -75% | -73% |
| 2YRRATE | 450 | 4 | 4% | 2% | -17% | -52% | -51% |
| 30YRRATE | 436 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 426 | 2 | 4% | 1% | -56% | -94% | -96% |
| INX | 93 | 1 | 2% | 1% | +0% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31585 | 123 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30398 | 116 | 4% | 2% | -56% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5539 | 25 | 2% | 1% | -18% | -78% | -78% |
| 0.05–0.1% | 6022 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9284 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11516 | 50 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4679 | 23 | 7% | 3% | -49% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15189 | 47 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14737 | 78 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15130 | 65 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16927 | 49 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,001 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/19 7:59:56 AM | USDJPY | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:59:40 AM | NATGAS | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:59:24 AM | EURUSD | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:58:52 AM | SILVER | UP | 67 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 7:58:04 AM | AUDUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:57:49 AM | GOLD | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 7:57:33 AM | HYPE | UP | 2.5 min | -0.508% | 20¢ | ❌ Lost | -$0.15 |
| 11/19 7:57:00 AM | GBPUSD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:57:00 AM | INX | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:57:00 AM | SOL | UP | 3.0 min | -0.610% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:56:26 AM | XRP | UP | 3.6 min | -0.625% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:56:26 AM | DOGE | UP | 3.6 min | -0.520% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 7:55:54 AM | BTC | UP | 4.1 min | -0.529% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 7:55:38 AM | BNB | UP | 4.3 min | -0.365% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 7:55:38 AM | NEAR | UP | 4.3 min | -1.141% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 7:55:22 AM | ZEC | UP | 4.6 min | -0.955% | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:55:22 AM | ETH | UP | 4.6 min | -0.538% | 2¢ | ❌ Lost | -$0.15 |
| 11/19 7:44:59 AM | XRP | DOWN | 1 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:44:59 AM | WTI | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:44:59 AM | PALLADIUM | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:44:59 AM | PLATINUM | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:44:59 AM | BRENT | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:44:43 AM | COPPER | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:44:43 AM | BTC | UP | 17 sec | -0.038% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 7:44:27 AM | 5YRRATE | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:44:27 AM | USDJPY | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:44:27 AM | 2YRRATE | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:44:11 AM | ETH | UP | 49 sec | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 7:43:55 AM | 10YRRATE | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:43:55 AM | ZEC | DOWN | 65 sec | +0.527% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
