# 15-Minute 1¢ Study

*Updated Wed Sep 30, 3:36 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 92 finished bets | 2% | $14.35 | +105% | +15.60¢ | $21.10 / -$6.75 |

*Expect about **40 buys a day** (~$6.03/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 92 | -$0.15 | -1% |
| Momentum model ≥ 5%, hold to the close | 155 | -$3.25 | -19% |
| Volatility model ≥ 5%, sell at 25¢ | 142 | -$5.07 | -34% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2967 | 2961 | 13 (0%) | 1.07% | -$180.40 (-50%) | Hold to the close: -$180.40 (-50%) |

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
| Volatility model | 1648 | 2.8% | 0.3% (5) | -461% | ❌ Worse |
| Momentum model | 1648 | 2.9% | 0.3% (5) | -506% | ❌ Worse |
| Mean-reversion model | 1648 | 5.8% | 0.3% (5) | -582% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1648 | 5 | -62% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 308 | 2 | -25% | -86% | -87% | -84% |
| Volatility model ≥ 5% | 142 | 0 | -100% | -77% | -77% | -70% |
| Volatility model ≥ 10% | 78 | 0 | -100% | -74% | -72% | -63% |
| Momentum model ≥ 2% | 274 | 1 | -57% | -86% | -89% | -88% |
| Momentum model ≥ 5% | 155 | 1 | -19% | -82% | -86% | -81% |
| Momentum model ≥ 10% | 97 | 0 | -100% | -86% | -83% | -79% |
| Mean-reversion model ≥ 2% | 606 | 3 | -47% | -87% | -87% | -83% |
| Mean-reversion model ≥ 5% | 392 | 3 | -18% | -84% | -83% | -76% |
| Mean-reversion model ≥ 10% | 241 | 2 | -7% | -78% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1844 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 899 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 218 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 2961 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$180.40 | -50% | — |
| Sell at 2¢ | 108 | 4% | -$334.32 | -92% | 47 sec |
| Sell at 3¢ | 68 | 2% | -$335.88 | -93% | 48 sec |
| Sell at 5¢ | 49 | 2% | -$330.55 | -91% | 64 sec |
| Sell at 10¢ | 40 | 1% | -$296.00 | -82% | 82 sec |
| Sell at 25¢ | 20 | 1% | -$282.20 | -78% | 1.7 min |
| Sell at 50¢ | 11 | 0% | -$246.15 | -68% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 92 | 2 | 10% | 2% | +105% | -83% | -89% |
| 2–5 min | 988 | 6 | 6% | 3% | -41% | -89% | -90% |
| 1–2 min | 792 | 4 | 4% | 2% | -46% | -93% | -92% |
| Under 1 min | 1089 | 1 | 1% | 0% | -86% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 208 | 1 | 4% | 1% | -38% | -91% | -91% |
| ZEC | 207 | 1 | 5% | 3% | -42% | -88% | -90% |
| ETH | 206 | 2 | 5% | 3% | +16% | -89% | -87% |
| NEAR | 205 | 0 | 5% | 1% | -100% | -88% | -91% |
| XRP | 205 | 2 | 2% | 2% | +25% | -94% | -93% |
| SOL | 205 | 0 | 3% | 1% | -100% | -93% | -91% |
| BTC | 203 | 0 | 6% | 2% | -100% | -86% | -91% |
| BNB | 203 | 0 | 2% | 0% | -100% | -96% | -97% |
| HYPE | 202 | 1 | 5% | 3% | -38% | -89% | -86% |
| GOLD | 160 | 0 | 6% | 1% | -100% | -87% | -92% |
| SILVER | 141 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 139 | 1 | 4% | 1% | -23% | -93% | -94% |
| COPPER | 131 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 122 | 1 | 3% | 2% | -23% | -94% | -91% |
| PLATINUM | 104 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 102 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 79 | 1 | 5% | 3% | +18% | -91% | -90% |
| EURUSD | 73 | 1 | 4% | 1% | +28% | -93% | -96% |
| USDJPY | 66 | 2 | 3% | 3% | +183% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1547 | 8 | 4% | 2% | -41% | -92% | -92% |
| DOWN (bought NO) | 1414 | 5 | 4% | 2% | -59% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 186 | 0 | 2% | 2% | -100% | -92% | -91% |
| 0.05–0.1% | 247 | 0 | 1% | 0% | -100% | -96% | -98% |
| 0.1–0.2% | 442 | 1 | 3% | 1% | -70% | -92% | -93% |
| 0.2–0.5% | 678 | 2 | 6% | 3% | -68% | -89% | -89% |
| Over 0.5% | 290 | 4 | 6% | 2% | +44% | -89% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 767 | 2 | 4% | 1% | -70% | -92% | -95% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,600 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 3:29:57 AM | NATGAS | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:29:57 AM | ZEC | UP | 3 sec | -0.086% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:29:24 AM | HYPE | DOWN | 36 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:29:08 AM | NEAR | UP | 52 sec | -0.504% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:28:21 AM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:27:49 AM | DOGE | DOWN | 2.2 min | +0.207% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:27:32 AM | SOL | DOWN | 2.5 min | +0.267% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:27:16 AM | BTC | DOWN | 2.7 min | +0.162% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:27:16 AM | ETH | DOWN | 2.7 min | +0.202% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:26:45 AM | XRP | DOWN | 3.2 min | +0.333% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:26:45 AM | SILVER | UP | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:26:30 AM | BNB | DOWN | 3.5 min | +0.160% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:26:30 AM | GOLD | UP | 3.5 min | — | 2¢ | ❌ Lost | -$0.15 |
| 9/30 3:14:16 AM | NEAR | DOWN | 44 sec | +0.145% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:14:01 AM | ZEC | DOWN | 58 sec | +0.193% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:13:46 AM | GOLD | UP | 74 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:13:14 AM | USDJPY | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:13:14 AM | PLATINUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:12:57 AM | NATGAS | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:12:57 AM | WTI | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:12:57 AM | PALLADIUM | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:12:42 AM | XRP | DOWN | 2.3 min | +0.200% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:12:42 AM | DOGE | DOWN | 2.3 min | +0.277% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:11:54 AM | BNB | DOWN | 3.1 min | +0.138% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:11:54 AM | SOL | DOWN | 3.1 min | +0.304% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:11:06 AM | GBPUSD | UP | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:11:06 AM | ETH | DOWN | 3.9 min | +0.267% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:10:49 AM | BTC | DOWN | 4.2 min | +0.203% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:09:46 AM | EURUSD | UP | 5.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:59:58 AM | NATGAS | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
