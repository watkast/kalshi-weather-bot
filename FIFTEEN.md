# 15-Minute 1¢ Study

*Updated Fri Oct 2, 1:12 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 321 finished bets | 1% | $7.20 | +21% | +2.24¢ | -$3.85 / $11.05 |

*Expect about **80 buys a day** (~$11.98/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 161 | $4.30 | +18% |
| Momentum model ≥ 5%, sell at 50¢ | 321 | -$0.05 | -0% |
| Volatility model ≥ 5%, hold to the close | 314 | -$6.35 | -18% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5214 | 5208 | 17 (0%) | 1.07% | -$397.85 (-63%) | Hold to the close: -$397.85 (-63%) |

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
| Volatility model | 3006 | 3.6% | 0.3% (8) | -618% | ❌ Worse |
| Momentum model | 3006 | 3.7% | 0.3% (8) | -668% | ❌ Worse |
| Mean-reversion model | 3006 | 6.7% | 0.3% (8) | -791% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3006 | 8 | -66% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 639 | 4 | -28% | -66% | -68% | -65% |
| Volatility model ≥ 5% | 314 | 2 | -18% | -39% | -40% | -37% |
| Volatility model ≥ 10% | 177 | 2 | +67% | +2% | -0% | +7% |
| Momentum model ≥ 2% | 557 | 3 | -35% | -63% | -66% | -63% |
| Momentum model ≥ 5% | 321 | 3 | +21% | -45% | -47% | -43% |
| Momentum model ≥ 10% | 211 | 2 | +37% | -21% | -20% | -15% |
| Mean-reversion model ≥ 2% | 1154 | 5 | -53% | -86% | -88% | -84% |
| Mean-reversion model ≥ 5% | 764 | 5 | -29% | -82% | -85% | -80% |
| Mean-reversion model ≥ 10% | 489 | 4 | -8% | -78% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3202 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1536 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 470 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5208 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 17 | 0% | -$397.85 | -63% | — |
| Sell at 2¢ | 188 | 4% | -$572.97 | -90% | 44 sec |
| Sell at 3¢ | 110 | 2% | -$578.95 | -91% | 50 sec |
| Sell at 5¢ | 81 | 2% | -$569.20 | -90% | 67 sec |
| Sell at 10¢ | 59 | 1% | -$530.56 | -83% | 81 sec |
| Sell at 25¢ | 29 | 1% | -$497.86 | -78% | 1.6 min |
| Sell at 50¢ | 14 | 0% | -$457.35 | -72% | 2.3 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 158 | 2 | 11% | 3% | +20% | -80% | -90% |
| 2–5 min | 1708 | 8 | 7% | 3% | -54% | -88% | -90% |
| 1–2 min | 1376 | 4 | 3% | 2% | -69% | -94% | -94% |
| Under 1 min | 1963 | 3 | 1% | 0% | -78% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 362 | 1 | 4% | 1% | -65% | -91% | -93% |
| BNB | 358 | 0 | 4% | 1% | -100% | -92% | -94% |
| ETH | 357 | 2 | 5% | 3% | -31% | -89% | -87% |
| ZEC | 357 | 1 | 5% | 2% | -67% | -89% | -94% |
| BTC | 356 | 0 | 6% | 3% | -100% | -85% | -89% |
| HYPE | 355 | 2 | 5% | 3% | -31% | -90% | -87% |
| NEAR | 353 | 1 | 6% | 2% | -62% | -86% | -90% |
| XRP | 353 | 3 | 1% | 1% | +9% | -60% | -59% |
| SOL | 351 | 0 | 3% | 1% | -100% | -93% | -93% |
| GOLD | 265 | 0 | 5% | 1% | -100% | -90% | -94% |
| SILVER | 249 | 0 | 2% | 1% | -100% | -97% | -96% |
| WTI | 233 | 1 | 3% | 1% | -55% | -94% | -96% |
| COPPER | 220 | 0 | 1% | 0% | -100% | -98% | -99% |
| PLATINUM | 193 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 192 | 1 | 4% | 2% | -51% | -94% | -92% |
| PALLADIUM | 184 | 0 | 2% | 1% | -100% | -96% | -99% |
| GBPUSD | 167 | 1 | 4% | 2% | -44% | -93% | -94% |
| EURUSD | 163 | 1 | 4% | 2% | -43% | -93% | -92% |
| USDJPY | 140 | 3 | 3% | 2% | +100% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2636 | 10 | 4% | 2% | -56% | -92% | -93% |
| DOWN (bought NO) | 2572 | 7 | 4% | 1% | -69% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 380 | 2 | 1% | 1% | -1% | -46% | -45% |
| 0.05–0.1% | 450 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 774 | 1 | 3% | 1% | -83% | -92% | -93% |
| 0.2–0.5% | 1084 | 3 | 6% | 3% | -69% | -89% | -89% |
| Over 0.5% | 513 | 4 | 6% | 2% | -20% | -88% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1176 | 2 | 4% | 1% | -81% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,202 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 12:59:57 AM | PLATINUM | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 12:59:57 AM | BTC | DOWN | 2 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/2 12:59:57 AM | WTI | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 12:59:41 AM | ETH | UP | 18 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/2 12:59:41 AM | XRP | UP | 18 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/2 12:59:41 AM | BNB | UP | 18 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/2 12:59:25 AM | SOL | UP | 34 sec | -0.126% | 0¢ | ❌ Lost | $0.00 |
| 10/2 12:58:53 AM | NEAR | UP | 67 sec | -0.366% | 0¢ | ❌ Lost | $0.00 |
| 10/2 12:58:53 AM | ZEC | UP | 67 sec | -0.284% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 12:58:53 AM | HYPE | UP | 67 sec | -0.211% | 0¢ | ❌ Lost | $0.00 |
| 10/2 12:58:37 AM | USDJPY | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 12:58:37 AM | DOGE | UP | 83 sec | -0.227% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 12:44:57 AM | GBPUSD | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 12:44:41 AM | SOL | UP | 19 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/2 12:44:41 AM | ETH | DOWN | 19 sec | +0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/2 12:44:25 AM | PLATINUM | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 12:44:25 AM | ZEC | UP | 35 sec | -0.113% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 12:44:25 AM | DOGE | UP | 35 sec | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 12:44:25 AM | XRP | UP | 35 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/2 12:43:53 AM | USDJPY | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 12:43:53 AM | BNB | UP | 67 sec | -0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 12:43:36 AM | BTC | UP | 83 sec | -0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 12:43:20 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 12:43:20 AM | WTI | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 12:43:04 AM | HYPE | UP | 1.9 min | -0.264% | 0¢ | ❌ Lost | $0.00 |
| 10/2 12:42:31 AM | NEAR | UP | 2.5 min | -0.653% | 0¢ | ❌ Lost | $0.00 |
| 10/2 12:42:13 AM | GOLD | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 12:41:57 AM | PALLADIUM | UP | 3.0 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/2 12:41:25 AM | SILVER | UP | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 12:29:51 AM | SILVER | UP | 8 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
