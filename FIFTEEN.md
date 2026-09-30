# 15-Minute 1¢ Study

*Updated Wed Sep 30, 4:16 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 92 finished bets | 2% | $14.35 | +105% | +15.60¢ | $21.10 / -$6.75 |

*Expect about **40 buys a day** (~$5.96/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 92 | -$0.15 | -1% |
| Momentum model ≥ 5%, hold to the close | 163 | -$4.30 | -23% |
| Volatility model ≥ 5%, sell at 25¢ | 145 | -$5.37 | -35% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3000 | 2994 | 13 (0%) | 1.07% | -$184.30 (-50%) | Hold to the close: -$184.30 (-50%) |

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
| Volatility model | 1675 | 2.9% | 0.3% (5) | -475% | ❌ Worse |
| Momentum model | 1675 | 3.1% | 0.3% (5) | -532% | ❌ Worse |
| Mean-reversion model | 1675 | 5.8% | 0.3% (5) | -590% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1675 | 5 | -63% | -91% | -91% | -88% |
| Volatility model ≥ 2% | 319 | 2 | -28% | -87% | -88% | -85% |
| Volatility model ≥ 5% | 145 | 0 | -100% | -78% | -77% | -70% |
| Volatility model ≥ 10% | 80 | 0 | -100% | -75% | -73% | -64% |
| Momentum model ≥ 2% | 287 | 1 | -59% | -87% | -90% | -89% |
| Momentum model ≥ 5% | 163 | 1 | -23% | -83% | -87% | -82% |
| Momentum model ≥ 10% | 102 | 0 | -100% | -87% | -84% | -80% |
| Mean-reversion model ≥ 2% | 618 | 3 | -48% | -87% | -87% | -83% |
| Mean-reversion model ≥ 5% | 398 | 3 | -19% | -84% | -83% | -76% |
| Mean-reversion model ≥ 10% | 245 | 2 | -8% | -79% | -80% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1871 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 905 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 218 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 2994 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$184.30 | -50% | — |
| Sell at 2¢ | 108 | 4% | -$338.22 | -92% | 47 sec |
| Sell at 3¢ | 68 | 2% | -$339.78 | -93% | 48 sec |
| Sell at 5¢ | 49 | 2% | -$334.45 | -91% | 64 sec |
| Sell at 10¢ | 40 | 1% | -$299.90 | -82% | 82 sec |
| Sell at 25¢ | 20 | 1% | -$286.10 | -78% | 1.7 min |
| Sell at 50¢ | 11 | 0% | -$250.05 | -68% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 92 | 2 | 10% | 2% | +105% | -83% | -89% |
| 2–5 min | 1000 | 6 | 6% | 3% | -42% | -89% | -90% |
| 1–2 min | 800 | 4 | 4% | 2% | -47% | -93% | -92% |
| Under 1 min | 1102 | 1 | 1% | 0% | -86% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 211 | 1 | 4% | 1% | -39% | -91% | -92% |
| ZEC | 210 | 1 | 5% | 3% | -43% | -88% | -90% |
| ETH | 209 | 2 | 5% | 3% | +15% | -89% | -87% |
| NEAR | 208 | 0 | 5% | 1% | -100% | -88% | -91% |
| XRP | 208 | 2 | 2% | 2% | +24% | -94% | -93% |
| SOL | 208 | 0 | 3% | 1% | -100% | -93% | -91% |
| BTC | 206 | 0 | 6% | 2% | -100% | -86% | -92% |
| BNB | 206 | 0 | 2% | 0% | -100% | -96% | -97% |
| HYPE | 205 | 1 | 5% | 3% | -39% | -89% | -86% |
| GOLD | 161 | 0 | 6% | 1% | -100% | -87% | -92% |
| SILVER | 141 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 139 | 1 | 4% | 1% | -23% | -93% | -94% |
| COPPER | 132 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 124 | 1 | 3% | 2% | -25% | -94% | -92% |
| PLATINUM | 104 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 104 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 79 | 1 | 5% | 3% | +18% | -91% | -90% |
| EURUSD | 73 | 1 | 4% | 1% | +28% | -93% | -96% |
| USDJPY | 66 | 2 | 3% | 3% | +183% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1558 | 8 | 4% | 2% | -41% | -92% | -92% |
| DOWN (bought NO) | 1436 | 5 | 4% | 2% | -60% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 190 | 0 | 2% | 2% | -100% | -92% | -91% |
| 0.05–0.1% | 251 | 0 | 1% | 0% | -100% | -96% | -98% |
| 0.1–0.2% | 453 | 1 | 3% | 1% | -71% | -92% | -94% |
| 0.2–0.5% | 683 | 2 | 6% | 3% | -68% | -89% | -89% |
| Over 0.5% | 293 | 4 | 6% | 2% | +42% | -89% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 800 | 2 | 4% | 1% | -72% | -92% | -95% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,550 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 4:14:48 AM | ZEC | DOWN | 12 sec | -0.012% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:14:32 AM | SOL | DOWN | 28 sec | +0.064% | 0¢ | ❌ Lost | $0.00 |
| 9/30 4:14:32 AM | PALLADIUM | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:14:16 AM | XRP | UP | 44 sec | -0.073% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:14:16 AM | COPPER | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:13:44 AM | DOGE | DOWN | 75 sec | +0.193% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:13:44 AM | ETH | DOWN | 75 sec | +0.105% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:13:28 AM | HYPE | UP | 1.5 min | -0.142% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:12:07 AM | BTC | DOWN | 2.9 min | +0.138% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:11:21 AM | NATGAS | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:10:33 AM | NEAR | DOWN | 4.4 min | +0.653% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:10:01 AM | BNB | DOWN | 5.0 min | +0.248% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:59:56 AM | XRP | UP | 3 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:59:41 AM | ETH | UP | 19 sec | -0.036% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:59:25 AM | DOGE | UP | 35 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:58:05 AM | BTC | DOWN | 1.9 min | +0.109% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:58:05 AM | HYPE | DOWN | 1.9 min | +0.126% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:58:05 AM | SOL | DOWN | 1.9 min | +0.191% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:57:49 AM | ZEC | DOWN | 2.2 min | +0.301% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:57:32 AM | BNB | UP | 2.5 min | -0.155% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:57:32 AM | NEAR | UP | 2.5 min | -0.656% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:44:29 AM | HYPE | DOWN | 31 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:44:29 AM | ZEC | UP | 31 sec | -0.287% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:44:13 AM | NATGAS | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:44:13 AM | ETH | DOWN | 47 sec | +0.091% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:44:13 AM | GOLD | DOWN | 47 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:43:27 AM | SOL | DOWN | 1.5 min | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:43:27 AM | PALLADIUM | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:42:55 AM | XRP | DOWN | 2.1 min | +0.212% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:42:55 AM | NEAR | DOWN | 2.1 min | +0.506% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
