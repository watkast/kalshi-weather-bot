# 15-Minute 1¢ Study

*Updated Fri Nov 6, 1:07 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3753 finished bets | 1% | $129.30 | +31% | +3.45¢ | $85.35 / $43.95 |

*Expect about **96 buys a day** (~$14.41/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3499 | $56.15 | +15% |
| Volatility model ≥ 2%, hold to the close | 6943 | $32.20 | +4% |
| Momentum model ≥ 2%, hold to the close | 5735 | -$42.80 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 47560 | 47543 | 173 (0%) | 1.07% | -$3,375.35 (-58%) | Hold to the close: -$3,375.35 (-58%) |

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
| Volatility model | 28745 | 4.7% | 0.4% (111) | -686% | ❌ Worse |
| Momentum model | 28745 | 4.6% | 0.4% (111) | -713% | ❌ Worse |
| Mean-reversion model | 28745 | 8.1% | 0.4% (111) | -835% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28745 | 111 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6943 | 62 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3753 | 39 | +31% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2147 | 24 | +61% | -71% | -70% | -66% |
| Momentum model ≥ 2% | 5735 | 44 | -6% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3499 | 31 | +15% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 2290 | 20 | +23% | -75% | -75% | -71% |
| Mean-reversion model ≥ 2% | 11876 | 80 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8319 | 69 | -8% | -81% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5569 | 49 | +0% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28950 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11436 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7157 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 47543 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 173 | 0% | -$3,375.35 | -58% | — |
| Sell at 2¢ | 1862 | 4% | -$5,061.23 | -87% | 47 sec |
| Sell at 3¢ | 1271 | 3% | -$5,049.66 | -87% | 49 sec |
| Sell at 5¢ | 879 | 2% | -$4,946.00 | -85% | 63 sec |
| Sell at 10¢ | 530 | 1% | -$4,739.05 | -82% | 65 sec |
| Sell at 25¢ | 277 | 1% | -$4,404.48 | -76% | 83 sec |
| Sell at 50¢ | 178 | 0% | -$4,021.85 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2345 | 10 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 15306 | 81 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 11973 | 40 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17907 | 42 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3244 | 13 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3237 | 12 | 4% | 2% | -53% | -90% | -90% |
| BNB | 3232 | 17 | 5% | 2% | -34% | -85% | -84% |
| HYPE | 3230 | 10 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 3217 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3214 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3195 | 16 | 5% | 2% | -35% | -84% | -84% |
| BTC | 3194 | 15 | 5% | 2% | -36% | -88% | -89% |
| XRP | 3187 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1760 | 5 | 5% | 2% | -65% | -81% | -82% |
| WTI | 1708 | 5 | 4% | 1% | -65% | -92% | -93% |
| SILVER | 1707 | 8 | 5% | 2% | -45% | -82% | -82% |
| PLATINUM | 1539 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1477 | 3 | 2% | 1% | -81% | -90% | -89% |
| COPPER | 1452 | 6 | 2% | 1% | -61% | -71% | -71% |
| GBPUSD | 1406 | 4 | 2% | 1% | -73% | -96% | -96% |
| NATGAS | 1397 | 8 | 2% | 1% | -47% | -76% | -76% |
| USDJPY | 1384 | 5 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1383 | 3 | 1% | 1% | -80% | -91% | -92% |
| AUDUSD | 935 | 4 | 2% | 1% | -60% | -87% | -87% |
| USDCAD | 906 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 490 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 280 | 1 | 4% | 1% | -67% | -59% | -57% |
| 30YRRATE | 266 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 262 | 3 | 4% | 1% | +7% | -22% | -21% |
| 5YRRATE | 240 | 1 | 5% | 2% | -61% | -92% | -95% |
| INX | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24145 | 92 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23398 | 81 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4627 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4903 | 18 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 7442 | 26 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8678 | 34 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3292 | 13 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11583 | 40 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 11661 | 51 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 11352 | 41 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12947 | 41 | 3% | 2% | -64% | -90% | -90% |

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
| 11/6 12:59:52 AM | ZEC | DOWN | 7 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 11/6 12:59:52 AM | 30YRRATE | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 12:59:52 AM | SOL | DOWN | 7 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 11/6 12:59:36 AM | 2YRRATE | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 12:59:20 AM | NATGAS | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 12:59:20 AM | BNB | DOWN | 39 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 11/6 12:59:20 AM | WTI | UP | 39 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/6 12:59:20 AM | BRENT | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 12:59:04 AM | HYPE | DOWN | 56 sec | +0.092% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 12:58:48 AM | NEAR | DOWN | 71 sec | +0.214% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 12:58:32 AM | XRP | DOWN | 87 sec | +0.186% | 0¢ | ❌ Lost | $0.00 |
| 11/6 12:58:16 AM | AUDUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 12:58:16 AM | PALLADIUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 12:58:16 AM | ETH | UP | 1.7 min | -0.196% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 12:57:42 AM | BTC | UP | 2.3 min | -0.237% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 12:57:42 AM | USDJPY | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 12:57:26 AM | DOGE | DOWN | 2.6 min | +0.208% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 12:57:26 AM | EURUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 12:55:37 AM | GOLD | DOWN | 4.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 12:55:21 AM | PLATINUM | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 12:55:05 AM | SILVER | DOWN | 4.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 12:44:34 AM | GOLD | DOWN | 26 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/6 12:44:18 AM | GBPUSD | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 12:44:18 AM | HYPE | DOWN | 42 sec | +0.135% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 12:44:18 AM | XRP | DOWN | 42 sec | +0.102% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 12:44:18 AM | EURUSD | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 12:43:15 AM | SILVER | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 12:42:25 AM | COPPER | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 12:42:25 AM | PLATINUM | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 12:41:38 AM | DOGE | DOWN | 3.4 min | +0.368% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
