# 15-Minute 1¢ Study

*Updated Thu Nov 19, 7:25 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4566 finished bets | 1% | $211.05 | +42% | +4.62¢ | $77.70 / $133.35 |

*Expect about **87 buys a day** (~$13.09/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4301 | $111.55 | +24% |
| Volatility model ≥ 2%, hold to the close | 8515 | $69.15 | +7% |
| Momentum model ≥ 2%, hold to the close | 7058 | -$10.50 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 61955 | 61920 | 239 (0%) | 1.07% | -$4,185.95 (-56%) | Hold to the close: -$4,185.95 (-56%) |

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
| Volatility model | 36818 | 4.5% | 0.4% (154) | -635% | ❌ Worse |
| Momentum model | 36818 | 4.4% | 0.4% (154) | -660% | ❌ Worse |
| Mean-reversion model | 36818 | 7.9% | 0.4% (154) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36818 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8515 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4566 | 51 | +42% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2625 | 30 | +67% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7058 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4301 | 41 | +24% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2804 | 26 | +32% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 15055 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10480 | 89 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6968 | 64 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37024 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14824 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10072 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 61920 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 239 | 0% | -$4,185.95 | -56% | — |
| Sell at 2¢ | 2510 | 4% | -$6,585.35 | -87% | 47 sec |
| Sell at 3¢ | 1692 | 3% | -$6,578.07 | -87% | 48 sec |
| Sell at 5¢ | 1154 | 2% | -$6,459.85 | -86% | 63 sec |
| Sell at 10¢ | 705 | 1% | -$6,202.40 | -82% | 65 sec |
| Sell at 25¢ | 377 | 1% | -$5,738.08 | -76% | 80 sec |
| Sell at 50¢ | 246 | 0% | -$5,185.45 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3146 | 17 | 10% | 4% | -49% | -82% | -83% |
| 2–5 min | 20087 | 108 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 15489 | 52 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 23185 | 62 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4140 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4138 | 19 | 4% | 2% | -41% | -86% | -86% |
| HYPE | 4129 | 12 | 4% | 2% | -63% | -90% | -88% |
| DOGE | 4119 | 11 | 4% | 2% | -66% | -89% | -89% |
| BNB | 4119 | 21 | 5% | 2% | -35% | -85% | -85% |
| ETH | 4114 | 19 | 7% | 3% | -42% | -82% | -82% |
| BTC | 4095 | 21 | 5% | 2% | -30% | -86% | -88% |
| NEAR | 4093 | 18 | 5% | 2% | -42% | -85% | -86% |
| XRP | 4077 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2211 | 6 | 5% | 2% | -67% | -82% | -84% |
| WTI | 2189 | 7 | 4% | 1% | -61% | -91% | -92% |
| SILVER | 2149 | 9 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1957 | 4 | 3% | 1% | -81% | -95% | -95% |
| EURUSD | 1915 | 7 | 2% | 1% | -66% | -91% | -90% |
| GBPUSD | 1843 | 8 | 2% | 1% | -59% | -96% | -95% |
| COPPER | 1842 | 6 | 2% | 1% | -70% | -76% | -76% |
| NATGAS | 1801 | 10 | 2% | 1% | -48% | -76% | -75% |
| USDJPY | 1799 | 6 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1761 | 4 | 1% | 0% | -79% | -93% | -93% |
| AUDUSD | 1352 | 6 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1292 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 914 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 473 | 2 | 3% | 1% | -61% | -75% | -73% |
| 2YRRATE | 448 | 4 | 4% | 2% | -17% | -52% | -51% |
| 30YRRATE | 434 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 424 | 2 | 4% | 1% | -56% | -94% | -96% |
| INX | 92 | 1 | 2% | 1% | +1% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31542 | 123 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30378 | 116 | 4% | 2% | -56% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5536 | 25 | 2% | 1% | -18% | -78% | -78% |
| 0.05–0.1% | 6021 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9278 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11511 | 50 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4669 | 23 | 7% | 3% | -48% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15189 | 47 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14674 | 78 | 4% | 2% | -39% | -85% | -85% |
| Afternoon (12–6pm) | 15130 | 65 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16927 | 49 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,006 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/19 7:24:21 AM | COPPER | UP | 5.6 min | — | — | In play | — |
| 11/19 7:14:48 AM | SOL | UP | 11 sec | -0.108% | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:14:32 AM | SILVER | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:14:18 AM | ETH | UP | 41 sec | -0.104% | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:14:02 AM | ZEC | UP | 57 sec | -0.183% | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:14:02 AM | BTC | UP | 57 sec | -0.149% | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:14:02 AM | PALLADIUM | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:14:02 AM | BNB | UP | 57 sec | -0.098% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:13:47 AM | XRP | UP | 72 sec | -0.192% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 7:13:31 AM | HYPE | UP | 88 sec | -0.223% | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:13:31 AM | EURUSD | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:13:15 AM | GOLD | UP | 1.7 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/19 7:13:15 AM | 30YRRATE | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:13:15 AM | DOGE | UP | 1.7 min | -0.228% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 7:13:15 AM | USDJPY | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:12:59 AM | USDCAD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:12:59 AM | 10YRRATE | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:12:28 AM | WTI | DOWN | 2.5 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:12:12 AM | GBPUSD | DOWN | 2.8 min | — | 7¢ | ❌ Lost | -$0.15 |
| 11/19 7:12:12 AM | AUDUSD | DOWN | 2.8 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/19 7:11:24 AM | 5YRRATE | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:10:52 AM | COPPER | DOWN | 4.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:10:37 AM | BRENT | DOWN | 4.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:10:21 AM | 2YRRATE | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:10:05 AM | NEAR | UP | 4.9 min | -0.427% | 10¢ | ❌ Lost | -$0.15 |
| 11/19 6:59:44 AM | AUDUSD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:59:28 AM | SILVER | DOWN | 31 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 6:59:28 AM | NEAR | DOWN | 31 sec | -0.041% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 6:59:28 AM | ZEC | DOWN | 31 sec | +0.096% | 0¢ | ❌ Lost | $0.00 |
| 11/19 6:59:12 AM | HYPE | DOWN | 47 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
