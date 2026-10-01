# 15-Minute 1¢ Study

*Updated Thu Oct 1, 4:28 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 127 finished bets | 2% | $9.40 | +51% | +7.40¢ | $18.55 / -$9.15 |

*Expect about **38 buys a day** (~$5.73/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 239 | $1.60 | +6% |
| Volatility model ≥ 5%, sell at 25¢ | 233 | -$1.87 | -7% |
| Volatility model ≥ 5%, sell at 10¢ | 233 | -$2.63 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4149 | 4139 | 14 (0%) | 1.07% | -$311.15 (-61%) | Hold to the close: -$311.15 (-61%) |

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
| Volatility model | 2373 | 3.3% | 0.3% (6) | -574% | ❌ Worse |
| Momentum model | 2373 | 3.4% | 0.3% (6) | -621% | ❌ Worse |
| Mean-reversion model | 2373 | 6.4% | 0.3% (6) | -740% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2373 | 6 | -68% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 471 | 3 | -28% | -60% | -62% | -57% |
| Volatility model ≥ 5% | 233 | 1 | -46% | -25% | -26% | -21% |
| Volatility model ≥ 10% | 136 | 1 | +6% | +26% | +24% | +31% |
| Momentum model ≥ 2% | 416 | 2 | -43% | -55% | -59% | -56% |
| Momentum model ≥ 5% | 239 | 2 | +6% | -31% | -35% | -30% |
| Momentum model ≥ 10% | 157 | 1 | -8% | +3% | +4% | +8% |
| Mean-reversion model ≥ 2% | 889 | 3 | -64% | -86% | -88% | -83% |
| Mean-reversion model ≥ 5% | 587 | 3 | -45% | -83% | -85% | -78% |
| Mean-reversion model ≥ 10% | 372 | 2 | -40% | -78% | -81% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2569 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1219 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 351 | 3% | 2% | 1% | 1% | 1% | 1% |
| **All** | 4139 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$311.15 | -61% | — |
| Sell at 2¢ | 151 | 4% | -$453.89 | -89% | 47 sec |
| Sell at 3¢ | 90 | 2% | -$458.05 | -90% | 49 sec |
| Sell at 5¢ | 67 | 2% | -$449.60 | -89% | 66 sec |
| Sell at 10¢ | 48 | 1% | -$416.27 | -82% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$399.71 | -79% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$370.15 | -73% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 127 | 2 | 12% | 3% | +51% | -79% | -87% |
| 2–5 min | 1346 | 6 | 7% | 3% | -57% | -88% | -89% |
| 1–2 min | 1072 | 4 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 1594 | 2 | 1% | 0% | -82% | -89% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 290 | 1 | 3% | 1% | -56% | -92% | -91% |
| NEAR | 287 | 0 | 5% | 1% | -100% | -88% | -91% |
| ETH | 287 | 2 | 5% | 3% | -14% | -89% | -87% |
| ZEC | 286 | 1 | 5% | 2% | -58% | -88% | -93% |
| XRP | 285 | 3 | 2% | 1% | +35% | -51% | -50% |
| HYPE | 285 | 1 | 5% | 3% | -58% | -90% | -88% |
| BTC | 284 | 0 | 7% | 3% | -100% | -84% | -88% |
| BNB | 284 | 0 | 4% | 1% | -100% | -91% | -94% |
| SOL | 281 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 211 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 197 | 0 | 2% | 1% | -100% | -97% | -97% |
| WTI | 187 | 1 | 3% | 1% | -44% | -94% | -95% |
| COPPER | 171 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 158 | 1 | 4% | 3% | -41% | -93% | -90% |
| PLATINUM | 150 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 145 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 126 | 1 | 4% | 2% | -26% | -93% | -94% |
| EURUSD | 123 | 1 | 2% | 1% | -24% | -96% | -98% |
| USDJPY | 102 | 2 | 2% | 2% | +83% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2112 | 8 | 4% | 2% | -57% | -93% | -93% |
| DOWN (bought NO) | 2027 | 6 | 4% | 2% | -66% | -86% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 300 | 1 | 1% | 1% | -38% | -33% | -33% |
| 0.05–0.1% | 366 | 0 | 2% | 0% | -100% | -94% | -98% |
| 0.1–0.2% | 615 | 1 | 4% | 2% | -79% | -91% | -92% |
| 0.2–0.5% | 868 | 2 | 6% | 3% | -75% | -89% | -89% |
| Over 0.5% | 419 | 4 | 7% | 3% | -1% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1025 | 2 | 4% | 1% | -78% | -92% | -94% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,261 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 4:27:12 AM | EURUSD | DOWN | 2.8 min | — | — | In play | — |
| 10/1 4:27:12 AM | SOL | UP | 2.8 min | -0.294% | — | In play | — |
| 10/1 4:26:40 AM | COPPER | DOWN | 3.3 min | — | — | In play | — |
| 10/1 4:26:24 AM | NEAR | UP | 3.6 min | -1.282% | — | In play | — |
| 10/1 4:14:27 AM | GBPUSD | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:13:56 AM | EURUSD | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:13:56 AM | NATGAS | UP | 63 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:13:41 AM | SOL | UP | 79 sec | -0.165% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:13:41 AM | GOLD | DOWN | 79 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:13:41 AM | SILVER | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:13:25 AM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:13:25 AM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:13:09 AM | HYPE | UP | 1.9 min | -0.341% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:13:09 AM | BTC | UP | 1.9 min | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:12:21 AM | BNB | UP | 2.6 min | -0.156% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:11:48 AM | ETH | UP | 3.2 min | -0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:11:17 AM | XRP | UP | 3.7 min | -0.598% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:10:29 AM | DOGE | UP | 4.5 min | -0.545% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:06:12 AM | NEAR | UP | 8.8 min | -1.645% | 3¢ | ❌ Lost | -$0.15 |
| 10/1 4:05:08 AM | ZEC | UP | 9.9 min | -1.623% | 1¢ | ❌ Lost | $0.00 |
| 10/1 3:59:56 AM | COPPER | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:59:40 AM | PALLADIUM | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:59:40 AM | WTI | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:59:24 AM | NATGAS | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:59:24 AM | PLATINUM | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:59:24 AM | SILVER | UP | 36 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:59:07 AM | BNB | DOWN | 52 sec | +0.031% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:58:36 AM | GOLD | UP | 84 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:57:45 AM | GBPUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:56:42 AM | DOGE | UP | 3.3 min | -0.337% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
