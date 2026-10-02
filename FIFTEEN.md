# 15-Minute 1¢ Study

*Updated Fri Oct 2, 1:32 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 322 finished bets | 1% | $7.05 | +20% | +2.19¢ | -$4.00 / $11.05 |

*Expect about **80 buys a day** (~$11.97/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 161 | $4.30 | +18% |
| Momentum model ≥ 5%, sell at 50¢ | 322 | -$0.20 | -1% |
| Volatility model ≥ 5%, hold to the close | 314 | -$6.35 | -18% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5244 | 5238 | 18 (0%) | 1.07% | -$386.70 (-61%) | Hold to the close: -$386.70 (-61%) |

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
| Volatility model | 3023 | 3.6% | 0.3% (8) | -616% | ❌ Worse |
| Momentum model | 3023 | 3.7% | 0.3% (8) | -666% | ❌ Worse |
| Mean-reversion model | 3023 | 6.7% | 0.3% (8) | -789% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3023 | 8 | -66% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 641 | 4 | -29% | -66% | -68% | -65% |
| Volatility model ≥ 5% | 314 | 2 | -18% | -39% | -40% | -37% |
| Volatility model ≥ 10% | 177 | 2 | +67% | +2% | -0% | +7% |
| Momentum model ≥ 2% | 558 | 3 | -35% | -63% | -66% | -63% |
| Momentum model ≥ 5% | 322 | 3 | +20% | -44% | -48% | -43% |
| Momentum model ≥ 10% | 212 | 2 | +36% | -20% | -20% | -16% |
| Mean-reversion model ≥ 2% | 1156 | 5 | -53% | -86% | -88% | -84% |
| Mean-reversion model ≥ 5% | 764 | 5 | -29% | -82% | -85% | -80% |
| Mean-reversion model ≥ 10% | 489 | 4 | -8% | -78% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3219 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1546 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 473 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5238 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 18 | 0% | -$386.70 | -61% | — |
| Sell at 2¢ | 190 | 4% | -$575.30 | -90% | 43 sec |
| Sell at 3¢ | 111 | 2% | -$581.41 | -91% | 49 sec |
| Sell at 5¢ | 82 | 2% | -$571.40 | -89% | 66 sec |
| Sell at 10¢ | 60 | 1% | -$532.10 | -83% | 81 sec |
| Sell at 25¢ | 30 | 1% | -$497.40 | -78% | 1.6 min |
| Sell at 50¢ | 15 | 0% | -$453.45 | -71% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 158 | 2 | 11% | 3% | +20% | -80% | -90% |
| 2–5 min | 1712 | 8 | 7% | 3% | -55% | -88% | -90% |
| 1–2 min | 1383 | 5 | 3% | 2% | -61% | -94% | -93% |
| Under 1 min | 1982 | 3 | 1% | 0% | -78% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 364 | 1 | 4% | 1% | -65% | -91% | -93% |
| BNB | 360 | 0 | 4% | 1% | -100% | -92% | -95% |
| ETH | 359 | 2 | 5% | 3% | -31% | -89% | -87% |
| ZEC | 359 | 1 | 5% | 2% | -67% | -89% | -94% |
| BTC | 358 | 0 | 6% | 3% | -100% | -85% | -89% |
| HYPE | 356 | 2 | 4% | 3% | -31% | -90% | -88% |
| NEAR | 355 | 1 | 6% | 2% | -62% | -86% | -90% |
| XRP | 355 | 3 | 1% | 1% | +9% | -60% | -60% |
| SOL | 353 | 0 | 3% | 1% | -100% | -93% | -93% |
| GOLD | 267 | 0 | 4% | 1% | -100% | -90% | -94% |
| SILVER | 250 | 0 | 2% | 1% | -100% | -97% | -96% |
| WTI | 235 | 1 | 3% | 1% | -55% | -94% | -96% |
| COPPER | 222 | 0 | 1% | 0% | -100% | -98% | -99% |
| PLATINUM | 194 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 192 | 1 | 4% | 2% | -51% | -94% | -92% |
| PALLADIUM | 186 | 1 | 3% | 1% | -50% | -95% | -97% |
| GBPUSD | 168 | 1 | 4% | 2% | -44% | -93% | -94% |
| EURUSD | 165 | 1 | 4% | 2% | -43% | -93% | -92% |
| USDJPY | 140 | 3 | 3% | 2% | +100% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2657 | 11 | 4% | 2% | -52% | -92% | -93% |
| DOWN (bought NO) | 2581 | 7 | 4% | 1% | -69% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 383 | 2 | 1% | 1% | -2% | -47% | -46% |
| 0.05–0.1% | 452 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 781 | 1 | 3% | 1% | -83% | -92% | -93% |
| 0.2–0.5% | 1086 | 3 | 6% | 3% | -69% | -89% | -89% |
| Over 0.5% | 516 | 4 | 6% | 2% | -20% | -88% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1206 | 3 | 4% | 1% | -72% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,198 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 1:29:59 AM | EURUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:43 AM | PLATINUM | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:43 AM | GBPUSD | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:43 AM | PALLADIUM | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:27 AM | BTC | UP | 33 sec | -0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:27 AM | ZEC | UP | 33 sec | -0.132% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:29:27 AM | WTI | UP | 33 sec | — | 1¢ | ❌ Lost | $0.00 |
| 10/2 1:29:27 AM | GOLD | UP | 33 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:11 AM | COPPER | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:28:54 AM | XRP | UP | 65 sec | -0.138% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:28:38 AM | BNB | UP | 81 sec | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:28:22 AM | SOL | UP | 1.6 min | -0.260% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:27:16 AM | DOGE | UP | 2.7 min | -0.227% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:27:01 AM | NEAR | UP | 3.0 min | -0.604% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:27:01 AM | ETH | UP | 3.0 min | -0.132% | 3¢ | ❌ Lost | -$0.15 |
| 10/2 1:25:56 AM | HYPE | UP | 4.1 min | -0.590% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:14:57 AM | ZEC | UP | 3 sec | -0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:14:57 AM | DOGE | DOWN | 3 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:14:41 AM | BTC | UP | 19 sec | -0.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:14:41 AM | SILVER | DOWN | 19 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:14:25 AM | EURUSD | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:14:10 AM | SOL | UP | 50 sec | -0.167% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:14:10 AM | ETH | DOWN | 50 sec | +0.077% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:14:10 AM | GOLD | DOWN | 50 sec | — | 1¢ | ❌ Lost | $0.00 |
| 10/2 1:14:10 AM | XRP | DOWN | 50 sec | +0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:14:10 AM | BNB | UP | 50 sec | -0.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:13:52 AM | COPPER | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:13:52 AM | WTI | UP | 68 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:13:52 AM | PALLADIUM | UP | 68 sec | — | 68¢ | ✅ Won | $13.85 |
| 10/2 1:13:05 AM | NEAR | UP | 1.9 min | -0.555% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
