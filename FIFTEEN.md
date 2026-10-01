# 15-Minute 1¢ Study

*Updated Thu Oct 1, 3:57 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 124 finished bets | 2% | $9.70 | +53% | +7.82¢ | $18.70 / -$9.00 |

*Expect about **38 buys a day** (~$5.67/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 235 | $2.20 | +9% |
| Volatility model ≥ 5%, sell at 25¢ | 233 | -$1.87 | -7% |
| Volatility model ≥ 5%, sell at 10¢ | 233 | -$2.63 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4121 | 4105 | 14 (0%) | 1.07% | -$306.35 (-61%) | Hold to the close: -$306.35 (-61%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 2355 | 3.3% | 0.3% (6) | -576% | ❌ Worse |
| Momentum model | 2355 | 3.4% | 0.3% (6) | -621% | ❌ Worse |
| Mean-reversion model | 2355 | 6.4% | 0.3% (6) | -742% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2355 | 6 | -68% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 471 | 3 | -28% | -60% | -62% | -57% |
| Volatility model ≥ 5% | 233 | 1 | -46% | -25% | -26% | -21% |
| Volatility model ≥ 10% | 136 | 1 | +6% | +26% | +24% | +31% |
| Momentum model ≥ 2% | 412 | 2 | -42% | -54% | -58% | -55% |
| Momentum model ≥ 5% | 235 | 2 | +9% | -30% | -34% | -28% |
| Momentum model ≥ 10% | 154 | 1 | -6% | +7% | +7% | +12% |
| Mean-reversion model ≥ 2% | 883 | 3 | -64% | -85% | -88% | -83% |
| Mean-reversion model ≥ 5% | 584 | 3 | -45% | -83% | -85% | -78% |
| Mean-reversion model ≥ 10% | 370 | 2 | -40% | -78% | -81% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2551 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1207 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 347 | 3% | 2% | 1% | 1% | 1% | 1% |
| **All** | 4105 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$306.35 | -61% | — |
| Sell at 2¢ | 150 | 4% | -$449.35 | -89% | 46 sec |
| Sell at 3¢ | 90 | 2% | -$453.25 | -90% | 49 sec |
| Sell at 5¢ | 67 | 2% | -$444.80 | -89% | 66 sec |
| Sell at 10¢ | 48 | 1% | -$411.47 | -82% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$394.91 | -79% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$365.35 | -73% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 124 | 2 | 11% | 3% | +53% | -80% | -87% |
| 2–5 min | 1333 | 6 | 7% | 3% | -56% | -88% | -89% |
| 1–2 min | 1062 | 4 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 1586 | 2 | 1% | 0% | -82% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 288 | 1 | 3% | 1% | -55% | -92% | -91% |
| NEAR | 285 | 0 | 5% | 1% | -100% | -89% | -91% |
| ETH | 285 | 2 | 5% | 3% | -14% | -89% | -87% |
| ZEC | 284 | 1 | 5% | 2% | -58% | -88% | -93% |
| XRP | 283 | 3 | 2% | 1% | +36% | -50% | -50% |
| HYPE | 283 | 1 | 5% | 3% | -57% | -90% | -88% |
| BTC | 282 | 0 | 7% | 3% | -100% | -84% | -88% |
| BNB | 282 | 0 | 4% | 1% | -100% | -91% | -94% |
| SOL | 279 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 209 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 195 | 0 | 2% | 1% | -100% | -97% | -97% |
| WTI | 186 | 1 | 3% | 1% | -43% | -94% | -95% |
| COPPER | 169 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 156 | 1 | 4% | 3% | -40% | -93% | -90% |
| PLATINUM | 148 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 144 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 124 | 1 | 4% | 2% | -25% | -93% | -94% |
| EURUSD | 121 | 1 | 2% | 1% | -23% | -96% | -98% |
| USDJPY | 102 | 2 | 2% | 2% | +83% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2086 | 8 | 3% | 2% | -56% | -93% | -92% |
| DOWN (bought NO) | 2019 | 6 | 4% | 2% | -66% | -86% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 299 | 1 | 1% | 1% | -37% | -33% | -32% |
| 0.05–0.1% | 366 | 0 | 2% | 0% | -100% | -94% | -98% |
| 0.1–0.2% | 610 | 1 | 4% | 2% | -79% | -91% | -92% |
| 0.2–0.5% | 862 | 2 | 6% | 3% | -74% | -89% | -89% |
| Over 0.5% | 413 | 4 | 7% | 3% | +0% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 991 | 2 | 4% | 2% | -77% | -92% | -94% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,261 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 3:57:45 AM | GBPUSD | UP | 2.2 min | — | — | In play | — |
| 10/1 3:56:42 AM | DOGE | UP | 3.3 min | -0.337% | — | In play | — |
| 10/1 3:56:42 AM | EURUSD | UP | 3.3 min | — | — | In play | — |
| 10/1 3:56:26 AM | NEAR | UP | 3.5 min | -0.693% | — | In play | — |
| 10/1 3:56:26 AM | HYPE | UP | 3.5 min | -0.327% | — | In play | — |
| 10/1 3:56:26 AM | BTC | UP | 3.5 min | -0.160% | — | In play | — |
| 10/1 3:56:26 AM | XRP | UP | 3.5 min | -0.261% | — | In play | — |
| 10/1 3:55:38 AM | ETH | UP | 4.3 min | -0.216% | — | In play | — |
| 10/1 3:55:22 AM | SOL | UP | 4.6 min | -0.342% | — | In play | — |
| 10/1 3:53:29 AM | ZEC | UP | 6.5 min | -0.744% | — | In play | — |
| 10/1 3:44:43 AM | DOGE | DOWN | 17 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:44:43 AM | HYPE | UP | 17 sec | -0.085% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:44:27 AM | SOL | DOWN | 33 sec | +0.042% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:44:27 AM | GBPUSD | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:44:27 AM | NEAR | UP | 33 sec | -0.260% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:44:11 AM | EURUSD | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:43:56 AM | SILVER | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:43:56 AM | XRP | DOWN | 63 sec | +0.087% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:43:39 AM | ETH | DOWN | 81 sec | +0.072% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:42:52 AM | ZEC | UP | 2.1 min | -0.427% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:42:35 AM | BTC | DOWN | 2.4 min | +0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:42:03 AM | BNB | DOWN | 3.0 min | +0.053% | 2¢ | ❌ Lost | -$0.15 |
| 10/1 3:29:51 AM | SILVER | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:29:35 AM | ZEC | UP | 25 sec | -0.125% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:29:35 AM | PALLADIUM | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:29:35 AM | NEAR | UP | 25 sec | -0.395% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:29:35 AM | XRP | UP | 25 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:29:19 AM | SOL | DOWN | 41 sec | +0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:29:04 AM | GBPUSD | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:28:49 AM | ETH | DOWN | 71 sec | +0.110% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
