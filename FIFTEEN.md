# 15-Minute 1¢ Study

*Updated Sat Oct 3, 9:39 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 173 finished bets | 1% | $2.50 | +10% | +1.45¢ | $15.25 / -$12.75 |

*Expect about **31 buys a day** (~$4.68/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 441 | -$4.20 | -9% |
| Momentum model ≥ 5%, sell at 50¢ | 441 | -$11.45 | -25% |
| 5+ min left, sell at 50¢ | 173 | -$12.00 | -47% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6605 | 6599 | 28 (0%) | 1.07% | -$403.45 (-51%) | Hold to the close: -$403.45 (-51%) |

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
| Volatility model | 4063 | 4.1% | 0.4% (16) | -644% | ❌ Worse |
| Momentum model | 4063 | 4.2% | 0.4% (16) | -680% | ❌ Worse |
| Mean-reversion model | 4063 | 7.1% | 0.4% (16) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4063 | 16 | -50% | -82% | -83% | -80% |
| Volatility model ≥ 2% | 849 | 5 | -32% | -67% | -68% | -63% |
| Volatility model ≥ 5% | 444 | 2 | -41% | -49% | -51% | -47% |
| Volatility model ≥ 10% | 267 | 2 | +15% | -20% | -25% | -19% |
| Momentum model ≥ 2% | 741 | 4 | -34% | -66% | -70% | -67% |
| Momentum model ≥ 5% | 441 | 3 | -9% | -53% | -58% | -53% |
| Momentum model ≥ 10% | 302 | 2 | -2% | -37% | -40% | -35% |
| Mean-reversion model ≥ 2% | 1509 | 7 | -50% | -83% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1019 | 6 | -35% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 666 | 4 | -31% | -77% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4260 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6599 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 28 | 0% | -$403.45 | -51% | — |
| Sell at 2¢ | 265 | 4% | -$698.55 | -88% | 34 sec |
| Sell at 3¢ | 168 | 3% | -$701.93 | -88% | 48 sec |
| Sell at 5¢ | 126 | 2% | -$685.55 | -86% | 62 sec |
| Sell at 10¢ | 85 | 1% | -$642.10 | -81% | 81 sec |
| Sell at 25¢ | 46 | 1% | -$587.19 | -74% | 1.6 min |
| Sell at 50¢ | 26 | 0% | -$521.95 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 170 | 2 | 12% | 3% | +12% | -79% | -89% |
| 2–5 min | 2169 | 14 | 8% | 4% | -37% | -86% | -87% |
| 1–2 min | 1708 | 8 | 3% | 2% | -49% | -94% | -93% |
| Under 1 min | 2549 | 4 | 1% | 0% | -77% | -86% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 479 | 2 | 4% | 1% | -45% | -90% | -91% |
| ETH | 478 | 3 | 6% | 3% | -21% | -85% | -85% |
| ZEC | 478 | 3 | 5% | 3% | -25% | -89% | -90% |
| HYPE | 476 | 2 | 5% | 4% | -48% | -88% | -85% |
| BNB | 473 | 1 | 4% | 2% | -75% | -90% | -91% |
| BTC | 470 | 1 | 6% | 3% | -72% | -85% | -88% |
| XRP | 470 | 4 | 2% | 1% | +9% | -68% | -68% |
| SOL | 469 | 0 | 3% | 1% | -100% | -93% | -93% |
| NEAR | 467 | 2 | 6% | 3% | -42% | -55% | -57% |
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
| UP (bought YES) | 3338 | 16 | 4% | 2% | -44% | -88% | -87% |
| DOWN (bought NO) | 3261 | 12 | 4% | 2% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 597 | 4 | 2% | 1% | +22% | -33% | -34% |
| 0.05–0.1% | 659 | 0 | 3% | 1% | -100% | -91% | -93% |
| 0.1–0.2% | 1048 | 4 | 4% | 2% | -50% | -90% | -90% |
| 0.2–0.5% | 1357 | 6 | 6% | 3% | -51% | -88% | -87% |
| Over 0.5% | 597 | 4 | 7% | 3% | -31% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1763 | 12 | 5% | 3% | -22% | -90% | -88% |
| Afternoon (12–6pm) | 1305 | 3 | 4% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,433 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 9:29:37 AM | ETH | DOWN | 22 sec | +0.002% | 0¢ | ❌ Lost | $0.00 |
| 10/3 9:29:37 AM | BTC | DOWN | 22 sec | +0.010% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:29:21 AM | HYPE | DOWN | 38 sec | +0.051% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 9:29:05 AM | ZEC | UP | 54 sec | -0.221% | 0¢ | ❌ Lost | $0.00 |
| 10/3 9:29:05 AM | BNB | UP | 54 sec | -0.116% | 0¢ | ❌ Lost | $0.00 |
| 10/3 9:28:18 AM | NEAR | UP | 1.7 min | -0.284% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:28:18 AM | DOGE | DOWN | 1.7 min | +0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:27:30 AM | XRP | DOWN | 2.5 min | +0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:14:55 AM | BTC | UP | 5 sec | -0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/3 9:14:24 AM | BNB | UP | 36 sec | -0.188% | 0¢ | ❌ Lost | $0.00 |
| 10/3 9:13:21 AM | XRP | UP | 1.6 min | -0.148% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:13:05 AM | NEAR | UP | 1.9 min | -0.439% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:12:48 AM | SOL | UP | 2.2 min | -0.191% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 9:12:32 AM | ZEC | UP | 2.5 min | -0.319% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:12:32 AM | DOGE | UP | 2.5 min | -0.229% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:12:16 AM | HYPE | UP | 2.7 min | -0.232% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 9:12:00 AM | ETH | UP | 3.0 min | -0.088% | 2¢ | ❌ Lost | -$0.15 |
| 10/3 8:57:26 AM | ETH | DOWN | 2.5 min | +0.080% | 2¢ | ❌ Lost | -$0.15 |
| 10/3 8:57:26 AM | DOGE | DOWN | 2.5 min | +0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:56:54 AM | BNB | DOWN | 3.1 min | +0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:56:38 AM | XRP | DOWN | 3.4 min | +0.269% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:56:23 AM | BTC | DOWN | 3.6 min | +0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:56:23 AM | SOL | DOWN | 3.6 min | +0.277% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:55:20 AM | ZEC | DOWN | 4.7 min | +0.685% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:55:20 AM | NEAR | DOWN | 4.7 min | +0.594% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:52:42 AM | HYPE | DOWN | 7.3 min | +0.694% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:44:33 AM | NEAR | DOWN | 26 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/3 8:44:33 AM | XRP | DOWN | 26 sec | +0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 8:44:33 AM | HYPE | UP | 26 sec | -0.069% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 8:44:17 AM | BNB | DOWN | 42 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
