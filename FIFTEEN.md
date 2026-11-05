# 15-Minute 1¢ Study

*Updated Thu Nov 5, 1:36 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3718 finished bets | 1% | $132.90 | +32% | +3.57¢ | $87.45 / $45.45 |

*Expect about **96 buys a day** (~$14.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3458 | $60.05 | +16% |
| Volatility model ≥ 2%, hold to the close | 6878 | $39.25 | +5% |
| Momentum model ≥ 2%, hold to the close | 5676 | -$36.65 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 46898 | 46887 | 172 (0%) | 1.07% | -$3,311.20 (-58%) | Hold to the close: -$3,311.20 (-58%) |

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
| Volatility model | 28423 | 4.7% | 0.4% (111) | -686% | ❌ Worse |
| Momentum model | 28423 | 4.6% | 0.4% (111) | -712% | ❌ Worse |
| Mean-reversion model | 28423 | 8.1% | 0.4% (111) | -833% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28423 | 111 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6878 | 62 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3718 | 39 | +32% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2126 | 24 | +62% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5676 | 44 | -6% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3458 | 31 | +16% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2260 | 20 | +24% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11756 | 80 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8248 | 69 | -7% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5526 | 49 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28628 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11238 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7021 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 46887 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 172 | 0% | -$3,311.20 | -58% | — |
| Sell at 2¢ | 1835 | 4% | -$4,990.10 | -87% | 47 sec |
| Sell at 3¢ | 1252 | 3% | -$4,978.92 | -87% | 48 sec |
| Sell at 5¢ | 865 | 2% | -$4,876.95 | -85% | 63 sec |
| Sell at 10¢ | 524 | 1% | -$4,668.76 | -82% | 65 sec |
| Sell at 25¢ | 272 | 1% | -$4,342.88 | -76% | 82 sec |
| Sell at 50¢ | 175 | 0% | -$3,963.95 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2320 | 10 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 15100 | 80 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 11789 | 40 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17666 | 42 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3206 | 13 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3200 | 12 | 4% | 2% | -52% | -90% | -90% |
| HYPE | 3196 | 10 | 5% | 2% | -61% | -89% | -87% |
| BNB | 3196 | 17 | 5% | 2% | -33% | -85% | -84% |
| DOGE | 3181 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3178 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3161 | 16 | 5% | 2% | -34% | -84% | -84% |
| BTC | 3160 | 15 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3150 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1734 | 5 | 5% | 2% | -65% | -81% | -83% |
| WTI | 1683 | 5 | 4% | 1% | -64% | -92% | -92% |
| SILVER | 1680 | 8 | 5% | 2% | -44% | -82% | -81% |
| PLATINUM | 1515 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1452 | 3 | 2% | 1% | -81% | -89% | -89% |
| COPPER | 1429 | 6 | 2% | 1% | -61% | -71% | -71% |
| GBPUSD | 1382 | 4 | 2% | 1% | -73% | -96% | -96% |
| NATGAS | 1368 | 8 | 2% | 1% | -45% | -76% | -75% |
| PALLADIUM | 1361 | 3 | 1% | 1% | -79% | -91% | -91% |
| USDJPY | 1359 | 5 | 2% | 1% | -66% | -97% | -97% |
| AUDUSD | 905 | 4 | 2% | 1% | -59% | -86% | -87% |
| USDCAD | 886 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 468 | 0 | 1% | 1% | -100% | -97% | -97% |
| 10YRRATE | 277 | 1 | 4% | 1% | -66% | -59% | -57% |
| 30YRRATE | 263 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 258 | 2 | 3% | 1% | -28% | -22% | -21% |
| 5YRRATE | 238 | 1 | 5% | 2% | -61% | -92% | -95% |
| INX | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23785 | 91 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23102 | 81 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4593 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4866 | 18 | 3% | 2% | -44% | -91% | -90% |
| 0.1–0.2% | 7375 | 26 | 5% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8542 | 34 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3244 | 13 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11506 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11661 | 51 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 11094 | 40 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12626 | 41 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,647 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/5 1:29:51 PM | EURUSD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:29:51 PM | PALLADIUM | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:29:51 PM | BNB | DOWN | 8 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 11/5 1:29:35 PM | PLATINUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:29:35 PM | SOL | DOWN | 24 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 11/5 1:29:35 PM | COPPER | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:29:35 PM | USDCAD | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:29:35 PM | XRP | UP | 24 sec | -0.153% | 0¢ | ❌ Lost | $0.00 |
| 11/5 1:29:19 PM | ETH | UP | 40 sec | -0.190% | 0¢ | ❌ Lost | $0.00 |
| 11/5 1:29:19 PM | AUDUSD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:29:19 PM | GOLD | UP | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 1:29:19 PM | BTC | UP | 40 sec | -0.095% | 0¢ | ❌ Lost | $0.00 |
| 11/5 1:29:03 PM | BRENT | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:29:03 PM | GBPUSD | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:28:48 PM | SILVER | UP | 72 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/5 1:28:48 PM | 2YRRATE | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:28:32 PM | 30YRRATE | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:28:16 PM | 5YRRATE | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:28:16 PM | 10YRRATE | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:28:16 PM | WTI | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 1:28:00 PM | ZEC | DOWN | 2.0 min | +0.619% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 1:27:45 PM | DOGE | DOWN | 2.2 min | +0.167% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:27:45 PM | NEAR | DOWN | 2.2 min | +0.514% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:27:45 PM | HYPE | DOWN | 2.2 min | +0.319% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 1:14:57 PM | NATGAS | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:14:57 PM | 10YRRATE | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:14:57 PM | USDJPY | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:14:42 PM | 30YRRATE | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:14:42 PM | 5YRRATE | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 1:13:23 PM | BRENT | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
