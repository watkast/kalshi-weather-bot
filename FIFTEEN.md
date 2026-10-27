# 15-Minute 1¢ Study

*Updated Tue Oct 27, 11:16 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2865 finished bets | 1% | $82.30 | +25% | +2.87¢ | $79.75 / $2.55 |

*Expect about **97 buys a day** (~$14.60/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2674 | $41.40 | +14% |
| Volatility model ≥ 2%, hold to the close | 5320 | -$6.40 | -1% |
| Momentum model ≥ 2%, hold to the close | 4421 | -$54.00 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34898 | 34890 | 132 (0%) | 1.07% | -$2,401.80 (-57%) | Hold to the close: -$2,401.80 (-57%) |

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
| Volatility model | 22031 | 4.6% | 0.4% (88) | -672% | ❌ Worse |
| Momentum model | 22031 | 4.6% | 0.4% (88) | -697% | ❌ Worse |
| Mean-reversion model | 22031 | 8.0% | 0.4% (88) | -816% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22031 | 88 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5320 | 46 | -1% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2865 | 29 | +25% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1626 | 18 | +56% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4421 | 33 | -10% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2674 | 24 | +14% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1747 | 16 | +26% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8940 | 59 | -28% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6258 | 49 | -14% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4175 | 35 | -5% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22231 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8243 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4416 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34890 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 132 | 0% | -$2,401.80 | -57% | — |
| Sell at 2¢ | 1318 | 4% | -$3,711.12 | -87% | 47 sec |
| Sell at 3¢ | 898 | 3% | -$3,703.58 | -87% | 48 sec |
| Sell at 5¢ | 621 | 2% | -$3,650.15 | -86% | 62 sec |
| Sell at 10¢ | 383 | 1% | -$3,496.07 | -82% | 65 sec |
| Sell at 25¢ | 207 | 1% | -$3,228.63 | -76% | 1.5 min |
| Sell at 50¢ | 137 | 0% | -$2,905.05 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1550 | 8 | 11% | 4% | -51% | -81% | -82% |
| 2–5 min | 11183 | 62 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 8847 | 31 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 13306 | 31 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2490 | 12 | 5% | 2% | -39% | -89% | -89% |
| HYPE | 2481 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2481 | 15 | 5% | 2% | -24% | -84% | -83% |
| SOL | 2477 | 6 | 4% | 2% | -70% | -92% | -92% |
| ETH | 2471 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2466 | 5 | 4% | 2% | -75% | -91% | -90% |
| NEAR | 2459 | 12 | 5% | 2% | -37% | -82% | -82% |
| XRP | 2455 | 9 | 3% | 1% | -55% | -89% | -89% |
| BTC | 2451 | 12 | 5% | 2% | -34% | -88% | -89% |
| GOLD | 1313 | 5 | 4% | 2% | -55% | -81% | -83% |
| SILVER | 1282 | 6 | 4% | 2% | -45% | -82% | -82% |
| WTI | 1263 | 4 | 3% | 1% | -62% | -93% | -94% |
| PLATINUM | 1135 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1086 | 4 | 1% | 1% | -66% | -72% | -72% |
| EURUSD | 1057 | 3 | 2% | 1% | -74% | -87% | -87% |
| NATGAS | 1045 | 6 | 2% | 1% | -46% | -79% | -78% |
| PALLADIUM | 1002 | 2 | 1% | 0% | -81% | -89% | -89% |
| GBPUSD | 997 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 983 | 5 | 1% | 1% | -53% | -98% | -97% |
| AUDUSD | 542 | 3 | 1% | 1% | -48% | -81% | -79% |
| USDCAD | 502 | 0 | 1% | 0% | -100% | -98% | -98% |
| BRENT | 117 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 92 | 0 | 4% | 0% | -100% | -92% | -92% |
| 30YRRATE | 82 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 81 | 1 | 4% | 1% | +15% | +22% | +22% |
| 5YRRATE | 80 | 1 | 5% | 2% | +17% | -91% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17652 | 73 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 17238 | 59 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3651 | 18 | 2% | 1% | -16% | -81% | -80% |
| 0.05–0.1% | 3802 | 13 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 5773 | 20 | 5% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 6555 | 29 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2446 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8688 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,646 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 11:14:46 AM | SILVER | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:14:46 AM | BTC | UP | 13 sec | -0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:14:46 AM | 10YRRATE | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:14:46 AM | SOL | UP | 13 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/27 11:14:46 AM | ETH | UP | 13 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 10/27 11:14:30 AM | 30YRRATE | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:14:30 AM | BNB | DOWN | 29 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/27 11:14:14 AM | ZEC | UP | 45 sec | -0.210% | 0¢ | ❌ Lost | $0.00 |
| 10/27 11:13:58 AM | NEAR | UP | 61 sec | -0.347% | 0¢ | ❌ Lost | $0.00 |
| 10/27 11:13:58 AM | XRP | UP | 61 sec | -0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:13:58 AM | PALLADIUM | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:13:27 AM | DOGE | UP | 1.6 min | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 11:13:27 AM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:13:27 AM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:12:39 AM | HYPE | DOWN | 2.3 min | +0.313% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 11:12:07 AM | GBPUSD | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 10:59:57 AM | 2YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:59:57 AM | 30YRRATE | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:59:57 AM | GBPUSD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:59:57 AM | BNB | DOWN | 3 sec | -0.007% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:59:57 AM | ZEC | UP | 3 sec | -0.265% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:59:57 AM | HYPE | DOWN | 3 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/27 10:59:57 AM | PALLADIUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:59:57 AM | COPPER | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:59:41 AM | USDJPY | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:59:41 AM | GOLD | UP | 19 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 10:59:25 AM | NEAR | DOWN | 35 sec | +0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/27 10:59:25 AM | BRENT | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:59:09 AM | NATGAS | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 10:59:09 AM | SOL | DOWN | 51 sec | +0.147% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
