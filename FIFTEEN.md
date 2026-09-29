# 15-Minute 1¢ Study

*Updated Tue Sep 29, 3:51 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 59 finished bets | 3% | $19.15 | +216% | +32.46¢ | $23.65 / -$4.50 |

*Expect about **45 buys a day** (~$6.81/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 227 | $12.60 | +43% |
| 5+ min left, sell at 50¢ | 59 | $4.65 | +53% |
| Volatility model ≥ 5%, sell at 25¢ | 83 | $1.23 | +14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1774 | 1768 | 8 (0%) | 1.07% | -$100.85 (-47%) | Hold to the close: -$100.85 (-47%) |

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
| Volatility model | 923 | 2.8% | 0.4% (4) | -380% | ❌ Worse |
| Momentum model | 923 | 2.9% | 0.4% (4) | -451% | ❌ Worse |
| Mean-reversion model | 923 | 5.9% | 0.4% (4) | -460% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 923 | 4 | -44% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 181 | 1 | -35% | -86% | -87% | -82% |
| Volatility model ≥ 5% | 83 | 0 | -100% | -73% | -73% | -63% |
| Volatility model ≥ 10% | 42 | 0 | -100% | -72% | -69% | -48% |
| Momentum model ≥ 2% | 148 | 0 | -100% | -86% | -91% | -89% |
| Momentum model ≥ 5% | 86 | 0 | -100% | -83% | -92% | -86% |
| Momentum model ≥ 10% | 56 | 0 | -100% | -90% | -85% | -75% |
| Mean-reversion model ≥ 2% | 345 | 3 | -5% | -86% | -87% | -81% |
| Mean-reversion model ≥ 5% | 227 | 3 | +43% | -84% | -84% | -76% |
| Mean-reversion model ≥ 10% | 143 | 2 | +58% | -79% | -80% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1118 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 548 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 102 | 3% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1768 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$100.85 | -47% | — |
| Sell at 2¢ | 58 | 3% | -$197.77 | -93% | 40 sec |
| Sell at 3¢ | 35 | 2% | -$199.20 | -94% | 47 sec |
| Sell at 5¢ | 25 | 1% | -$196.60 | -92% | 81 sec |
| Sell at 10¢ | 23 | 1% | -$182.72 | -86% | 1.9 min |
| Sell at 25¢ | 13 | 1% | -$169.82 | -80% | 2.1 min |
| Sell at 50¢ | 9 | 1% | -$152.10 | -71% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 59 | 2 | 8% | 3% | +216% | -85% | -87% |
| 2–5 min | 596 | 5 | 6% | 3% | -19% | -89% | -90% |
| 1–2 min | 485 | 1 | 2% | 1% | -78% | -95% | -96% |
| Under 1 min | 628 | 0 | 1% | 0% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 128 | 2 | 5% | 3% | +96% | -89% | -86% |
| ZEC | 126 | 1 | 6% | 2% | -4% | -87% | -95% |
| NEAR | 125 | 0 | 5% | 2% | -100% | -87% | -94% |
| DOGE | 125 | 1 | 4% | 2% | -1% | -91% | -86% |
| XRP | 125 | 2 | 3% | 2% | +103% | -92% | -92% |
| BTC | 124 | 0 | 8% | 2% | -100% | -80% | -88% |
| SOL | 124 | 0 | 2% | 2% | -100% | -93% | -90% |
| BNB | 121 | 0 | 2% | 1% | -100% | -95% | -95% |
| HYPE | 120 | 0 | 2% | 2% | -100% | -94% | -94% |
| GOLD | 95 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 86 | 0 | 1% | 0% | -100% | -98% | -100% |
| SILVER | 86 | 0 | 1% | 0% | -100% | -97% | -96% |
| COPPER | 79 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 75 | 0 | 4% | 1% | -100% | -93% | -90% |
| PLATINUM | 70 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 57 | 0 | 2% | 0% | -100% | -97% | -100% |
| GBPUSD | 38 | 0 | 3% | 0% | -100% | -95% | -93% |
| USDJPY | 33 | 2 | 6% | 6% | +466% | -89% | -84% |
| EURUSD | 31 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 931 | 5 | 4% | 2% | -37% | -92% | -92% |
| DOWN (bought NO) | 837 | 3 | 3% | 1% | -59% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 113 | 0 | 3% | 2% | -100% | -90% | -90% |
| 0.05–0.1% | 132 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 256 | 0 | 4% | 1% | -100% | -90% | -91% |
| 0.2–0.5% | 424 | 2 | 4% | 2% | -48% | -91% | -92% |
| Over 0.5% | 193 | 4 | 7% | 4% | +118% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 511 | 1 | 3% | 1% | -77% | -93% | -95% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,854 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 3:44:19 AM | PALLADIUM | DOWN | 40 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 9/29 3:44:03 AM | HYPE | DOWN | 57 sec | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 9/29 3:44:03 AM | NATGAS | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:43:29 AM | PLATINUM | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:43:29 AM | SILVER | DOWN | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:43:29 AM | GOLD | DOWN | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:43:13 AM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:42:58 AM | BNB | DOWN | 2.0 min | +0.034% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:42:42 AM | XRP | DOWN | 2.3 min | +0.320% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:42:26 AM | ZEC | DOWN | 2.5 min | +0.359% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:41:54 AM | ETH | DOWN | 3.1 min | +0.177% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:41:54 AM | WTI | UP | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:41:37 AM | BTC | DOWN | 3.4 min | +0.116% | 2¢ | ❌ Lost | -$0.15 |
| 9/29 3:41:37 AM | SOL | DOWN | 3.4 min | +0.269% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:40:32 AM | DOGE | DOWN | 4.5 min | +0.314% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:40:32 AM | NEAR | DOWN | 4.5 min | +0.567% | 2¢ | ❌ Lost | -$0.15 |
| 9/29 3:29:57 AM | SILVER | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 3:29:57 AM | GOLD | DOWN | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 3:29:41 AM | ETH | DOWN | 18 sec | +0.008% | 0¢ | ❌ Lost | $0.00 |
| 9/29 3:29:25 AM | PALLADIUM | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:29:25 AM | NEAR | UP | 34 sec | -0.207% | 0¢ | ❌ Lost | $0.00 |
| 9/29 3:28:33 AM | BTC | DOWN | 87 sec | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:28:18 AM | DOGE | DOWN | 1.7 min | +0.182% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:28:18 AM | COPPER | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:28:03 AM | HYPE | DOWN | 1.9 min | +0.175% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:27:47 AM | ZEC | DOWN | 2.2 min | +0.424% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:27:15 AM | XRP | DOWN | 2.7 min | +0.234% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:26:59 AM | SOL | DOWN | 3.0 min | +0.242% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:14:34 AM | NEAR | DOWN | 26 sec | +0.109% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:14:18 AM | DOGE | UP | 42 sec | -0.097% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
