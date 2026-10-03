# 15-Minute 1¢ Study

*Updated Sat Oct 3, 8:18 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 172 finished bets | 1% | $2.65 | +10% | +1.54¢ | $15.25 / -$12.60 |

*Expect about **31 buys a day** (~$4.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 438 | -$4.05 | -9% |
| Momentum model ≥ 5%, sell at 50¢ | 438 | -$11.30 | -25% |
| 5+ min left, sell at 50¢ | 172 | -$11.85 | -47% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6562 | 6556 | 28 (0%) | 1.07% | -$398.20 (-50%) | Hold to the close: -$398.20 (-50%) |

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
| Volatility model | 4020 | 4.1% | 0.4% (16) | -646% | ❌ Worse |
| Momentum model | 4020 | 4.2% | 0.4% (16) | -682% | ❌ Worse |
| Mean-reversion model | 4020 | 7.1% | 0.4% (16) | -773% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4020 | 16 | -49% | -82% | -83% | -80% |
| Volatility model ≥ 2% | 845 | 5 | -31% | -67% | -68% | -63% |
| Volatility model ≥ 5% | 441 | 2 | -41% | -49% | -50% | -47% |
| Volatility model ≥ 10% | 265 | 2 | +15% | -20% | -25% | -19% |
| Momentum model ≥ 2% | 738 | 4 | -34% | -66% | -70% | -67% |
| Momentum model ≥ 5% | 438 | 3 | -9% | -53% | -58% | -53% |
| Momentum model ≥ 10% | 299 | 2 | -2% | -36% | -40% | -35% |
| Mean-reversion model ≥ 2% | 1498 | 7 | -49% | -83% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1012 | 6 | -35% | -79% | -81% | -74% |
| Mean-reversion model ≥ 10% | 662 | 4 | -30% | -77% | -80% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4217 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6556 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 28 | 0% | -$398.20 | -50% | — |
| Sell at 2¢ | 265 | 4% | -$693.30 | -88% | 34 sec |
| Sell at 3¢ | 168 | 3% | -$696.68 | -88% | 48 sec |
| Sell at 5¢ | 126 | 2% | -$680.30 | -86% | 62 sec |
| Sell at 10¢ | 85 | 1% | -$636.85 | -81% | 81 sec |
| Sell at 25¢ | 46 | 1% | -$581.94 | -74% | 1.6 min |
| Sell at 50¢ | 26 | 0% | -$516.70 | -65% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 169 | 2 | 12% | 3% | +12% | -79% | -89% |
| 2–5 min | 2147 | 14 | 8% | 4% | -36% | -86% | -86% |
| 1–2 min | 1701 | 8 | 3% | 2% | -49% | -93% | -93% |
| Under 1 min | 2536 | 4 | 1% | 0% | -76% | -86% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 474 | 2 | 4% | 1% | -44% | -90% | -91% |
| ETH | 473 | 3 | 6% | 3% | -20% | -85% | -85% |
| ZEC | 473 | 3 | 5% | 3% | -25% | -89% | -90% |
| HYPE | 471 | 2 | 5% | 4% | -48% | -88% | -85% |
| BNB | 468 | 1 | 4% | 2% | -74% | -90% | -91% |
| SOL | 466 | 0 | 3% | 1% | -100% | -93% | -93% |
| BTC | 465 | 1 | 6% | 3% | -72% | -85% | -88% |
| XRP | 465 | 4 | 2% | 1% | +11% | -68% | -68% |
| NEAR | 462 | 2 | 6% | 3% | -41% | -54% | -57% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 274 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 225 | 2 | 4% | 2% | -17% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3323 | 16 | 4% | 2% | -44% | -88% | -87% |
| DOWN (bought NO) | 3233 | 12 | 4% | 2% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 590 | 4 | 2% | 1% | +24% | -32% | -33% |
| 0.05–0.1% | 650 | 0 | 3% | 1% | -100% | -91% | -92% |
| 0.1–0.2% | 1034 | 4 | 4% | 2% | -49% | -90% | -90% |
| 0.2–0.5% | 1347 | 6 | 6% | 3% | -51% | -87% | -87% |
| Over 0.5% | 594 | 4 | 7% | 3% | -30% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1720 | 12 | 5% | 3% | -21% | -89% | -88% |
| Afternoon (12–6pm) | 1305 | 3 | 4% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,408 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 8:14:06 AM | BNB | DOWN | 54 sec | +0.068% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 8:12:47 AM | HYPE | UP | 2.2 min | -0.294% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:12:32 AM | NEAR | UP | 2.5 min | -0.455% | 3¢ | ❌ Lost | -$0.15 |
| 10/3 8:12:32 AM | XRP | UP | 2.5 min | -0.242% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:12:32 AM | BTC | UP | 2.5 min | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/3 8:12:16 AM | DOGE | UP | 2.7 min | -0.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:11:44 AM | SOL | UP | 3.3 min | -0.186% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:11:29 AM | ETH | UP | 3.5 min | -0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:11:29 AM | ZEC | UP | 3.5 min | -0.398% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:59:49 AM | NEAR | DOWN | 11 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/3 7:59:49 AM | SOL | DOWN | 11 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/3 7:59:49 AM | ZEC | DOWN | 11 sec | +0.147% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 7:58:46 AM | BNB | DOWN | 74 sec | +0.041% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 7:58:31 AM | BTC | DOWN | 89 sec | +0.039% | 2¢ | ❌ Lost | -$0.15 |
| 10/3 7:58:31 AM | ETH | DOWN | 89 sec | +0.030% | 2¢ | ❌ Lost | -$0.15 |
| 10/3 7:57:43 AM | XRP | DOWN | 2.3 min | +0.175% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:57:28 AM | DOGE | DOWN | 2.5 min | +0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:44:36 AM | HYPE | UP | 24 sec | -0.165% | 0¢ | ❌ Lost | $0.00 |
| 10/3 7:44:36 AM | SOL | UP | 24 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/3 7:44:36 AM | XRP | UP | 24 sec | -0.081% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 7:43:47 AM | NEAR | UP | 72 sec | -0.273% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:43:15 AM | XRP | DOWN | 1.8 min | +0.101% | 100¢ | ✅ Won | $13.85 |
| 10/3 7:42:44 AM | ZEC | DOWN | 2.2 min | +0.351% | 99¢ | ✅ Won | $13.85 |
| 10/3 7:42:12 AM | DOGE | DOWN | 2.8 min | +0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:41:09 AM | BTC | DOWN | 3.9 min | +0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:40:38 AM | ETH | DOWN | 4.3 min | +0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:40:23 AM | BNB | DOWN | 4.6 min | +0.131% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:29:21 AM | HYPE | DOWN | 39 sec | +0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/3 7:29:05 AM | SOL | UP | 55 sec | -0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:28:32 AM | XRP | UP | 88 sec | -0.088% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
