# 15-Minute 1¢ Study

*Updated Thu Nov 19, 1:42 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4567 finished bets | 1% | $211.05 | +42% | +4.62¢ | $77.70 / $133.35 |

*Expect about **87 buys a day** (~$13.03/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4304 | $111.25 | +24% |
| Volatility model ≥ 2%, hold to the close | 8518 | $68.85 | +7% |
| Momentum model ≥ 2%, hold to the close | 7063 | -$11.10 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 62087 | 62052 | 240 (0%) | 1.07% | -$4,189.05 (-55%) | Hold to the close: -$4,189.05 (-55%) |

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
| Volatility model | 36870 | 4.5% | 0.4% (154) | -635% | ❌ Worse |
| Momentum model | 36870 | 4.4% | 0.4% (154) | -660% | ❌ Worse |
| Mean-reversion model | 36870 | 7.9% | 0.4% (154) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36870 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8518 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4567 | 51 | +42% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2626 | 30 | +67% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7063 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4304 | 41 | +24% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2805 | 26 | +32% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 15067 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10486 | 89 | -6% | -79% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6972 | 64 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37076 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14858 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10118 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 62052 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 240 | 0% | -$4,189.05 | -55% | — |
| Sell at 2¢ | 2523 | 4% | -$6,599.07 | -87% | 47 sec |
| Sell at 3¢ | 1704 | 3% | -$6,590.49 | -87% | 48 sec |
| Sell at 5¢ | 1165 | 2% | -$6,469.80 | -86% | 63 sec |
| Sell at 10¢ | 713 | 1% | -$6,209.02 | -82% | 65 sec |
| Sell at 25¢ | 381 | 1% | -$5,727.94 | -76% | 80 sec |
| Sell at 50¢ | 247 | 0% | -$5,181.80 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3167 | 17 | 11% | 4% | -49% | -81% | -82% |
| 2–5 min | 20129 | 108 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 15525 | 52 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 23218 | 63 | 1% | 0% | -61% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4146 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4143 | 19 | 4% | 2% | -41% | -86% | -86% |
| HYPE | 4135 | 12 | 4% | 2% | -63% | -89% | -88% |
| DOGE | 4125 | 11 | 4% | 2% | -66% | -89% | -89% |
| BNB | 4124 | 21 | 5% | 2% | -35% | -85% | -85% |
| ETH | 4120 | 19 | 7% | 3% | -42% | -82% | -82% |
| BTC | 4101 | 21 | 5% | 2% | -30% | -86% | -88% |
| NEAR | 4099 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4083 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2215 | 6 | 5% | 2% | -67% | -82% | -84% |
| WTI | 2194 | 7 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 2155 | 9 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1962 | 5 | 3% | 1% | -76% | -95% | -95% |
| EURUSD | 1921 | 7 | 3% | 1% | -66% | -91% | -90% |
| GBPUSD | 1849 | 8 | 2% | 1% | -60% | -96% | -95% |
| COPPER | 1845 | 6 | 2% | 1% | -70% | -76% | -76% |
| USDJPY | 1805 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1804 | 10 | 2% | 1% | -48% | -76% | -75% |
| PALLADIUM | 1765 | 4 | 1% | 0% | -79% | -93% | -93% |
| AUDUSD | 1358 | 6 | 2% | 1% | -59% | -90% | -89% |
| USDCAD | 1295 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 918 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 476 | 2 | 3% | 1% | -61% | -75% | -73% |
| 2YRRATE | 452 | 4 | 4% | 2% | -17% | -52% | -51% |
| 30YRRATE | 438 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 428 | 2 | 4% | 2% | -56% | -94% | -95% |
| INX | 96 | 1 | 2% | 1% | -3% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31637 | 123 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30415 | 117 | 4% | 2% | -56% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5539 | 25 | 2% | 1% | -18% | -78% | -78% |
| 0.05–0.1% | 6022 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9288 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11526 | 50 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4692 | 23 | 7% | 3% | -49% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15189 | 47 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14806 | 79 | 5% | 2% | -39% | -85% | -84% |
| Afternoon (12–6pm) | 15130 | 65 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16927 | 49 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,000 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/19 1:40:15 PM | BRENT | DOWN | 4.8 min | — | — | In play | — |
| 11/19 8:44:13 AM | SILVER | DOWN | 47 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/19 8:43:56 AM | GBPUSD | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:43:41 AM | GOLD | DOWN | 78 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/19 8:43:41 AM | AUDUSD | UP | 78 sec | — | 29¢ | ❌ Lost | -$0.15 |
| 11/19 8:43:41 AM | EURUSD | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:43:09 AM | PALLADIUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:43:09 AM | PLATINUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:41:18 AM | USDJPY | UP | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:39:58 AM | BRENT | UP | 5.0 min | — | 5¢ | ❌ Lost | -$0.15 |
| 11/19 8:39:58 AM | WTI | UP | 5.0 min | — | 8¢ | ❌ Lost | -$0.15 |
| 11/19 8:39:25 AM | 30YRRATE | UP | 5.6 min | — | 4¢ | ❌ Lost | -$0.15 |
| 11/19 8:39:25 AM | INX | UP | 5.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:39:25 AM | BTC | UP | 5.6 min | -0.885% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:39:25 AM | HYPE | UP | 5.6 min | -1.071% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:39:25 AM | ZEC | UP | 5.6 min | -1.539% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:39:09 AM | ETH | UP | 5.8 min | -1.190% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:39:09 AM | 5YRRATE | UP | 5.8 min | — | 35¢ | ❌ Lost | -$0.15 |
| 11/19 8:39:09 AM | 2YRRATE | UP | 5.8 min | — | 65¢ | ❌ Lost | -$0.15 |
| 11/19 8:38:53 AM | 10YRRATE | UP | 6.1 min | — | 10¢ | ❌ Lost | -$0.15 |
| 11/19 8:38:53 AM | NEAR | UP | 6.1 min | -1.322% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:38:38 AM | DOGE | UP | 6.3 min | -1.059% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:38:38 AM | BNB | UP | 6.3 min | -0.583% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:38:38 AM | SOL | UP | 6.3 min | -1.248% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:38:07 AM | XRP | UP | 6.9 min | -1.180% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:29:15 AM | COPPER | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:28:59 AM | SOL | UP | 61 sec | -0.313% | 0¢ | ❌ Lost | $0.00 |
| 11/19 8:28:43 AM | XRP | UP | 77 sec | -0.243% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:28:43 AM | BTC | UP | 77 sec | -0.196% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:28:43 AM | HYPE | UP | 77 sec | -0.383% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
