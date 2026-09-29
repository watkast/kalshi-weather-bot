# 15-Minute 1¢ Study

*Updated Tue Sep 29, 7:36 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 66 finished bets | 3% | $18.10 | +183% | +27.42¢ | $23.05 / -$4.95 |

*Expect about **45 buys a day** (~$6.80/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 240 | $10.80 | +35% |
| 5+ min left, sell at 50¢ | 66 | $3.60 | +36% |
| Volatility model ≥ 5%, sell at 25¢ | 88 | $0.63 | +7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1884 | 1878 | 8 (0%) | 1.07% | -$114.20 (-50%) | Hold to the close: -$114.20 (-50%) |

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
| Volatility model | 991 | 2.8% | 0.4% (4) | -407% | ❌ Worse |
| Momentum model | 991 | 2.9% | 0.4% (4) | -474% | ❌ Worse |
| Mean-reversion model | 991 | 6.0% | 0.4% (4) | -498% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 991 | 4 | -48% | -90% | -92% | -88% |
| Volatility model ≥ 2% | 195 | 1 | -41% | -86% | -87% | -83% |
| Volatility model ≥ 5% | 88 | 0 | -100% | -72% | -71% | -65% |
| Volatility model ≥ 10% | 46 | 0 | -100% | -69% | -63% | -54% |
| Momentum model ≥ 2% | 159 | 0 | -100% | -86% | -90% | -90% |
| Momentum model ≥ 5% | 93 | 0 | -100% | -82% | -89% | -87% |
| Momentum model ≥ 10% | 59 | 0 | -100% | -86% | -79% | -77% |
| Mean-reversion model ≥ 2% | 369 | 3 | -12% | -86% | -87% | -82% |
| Mean-reversion model ≥ 5% | 240 | 3 | +35% | -83% | -84% | -77% |
| Mean-reversion model ≥ 10% | 153 | 2 | +47% | -78% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1186 | 4% | 2% | 2% | 2% | 1% | 1% |
| Commodities | 581 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 111 | 4% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1878 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$114.20 | -50% | — |
| Sell at 2¢ | 62 | 3% | -$210.08 | -93% | 40 sec |
| Sell at 3¢ | 36 | 2% | -$212.16 | -94% | 40 sec |
| Sell at 5¢ | 25 | 1% | -$209.95 | -93% | 81 sec |
| Sell at 10¢ | 23 | 1% | -$196.07 | -87% | 1.9 min |
| Sell at 25¢ | 13 | 1% | -$183.17 | -81% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$165.45 | -73% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 66 | 2 | 9% | 3% | +183% | -84% | -88% |
| 2–5 min | 624 | 5 | 6% | 3% | -22% | -89% | -90% |
| 1–2 min | 520 | 1 | 2% | 1% | -79% | -95% | -95% |
| Under 1 min | 668 | 0 | 1% | 0% | -100% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 135 | 2 | 4% | 3% | +87% | -90% | -87% |
| ZEC | 134 | 1 | 5% | 1% | -8% | -88% | -95% |
| DOGE | 133 | 1 | 5% | 2% | -6% | -89% | -87% |
| NEAR | 132 | 0 | 5% | 2% | -100% | -88% | -94% |
| BTC | 132 | 0 | 8% | 2% | -100% | -81% | -89% |
| XRP | 132 | 2 | 3% | 2% | +92% | -93% | -92% |
| SOL | 131 | 0 | 2% | 2% | -100% | -94% | -91% |
| BNB | 129 | 0 | 2% | 1% | -100% | -95% | -95% |
| HYPE | 128 | 0 | 3% | 2% | -100% | -93% | -92% |
| GOLD | 100 | 0 | 2% | 0% | -100% | -96% | -100% |
| WTI | 91 | 0 | 1% | 0% | -100% | -98% | -100% |
| SILVER | 91 | 0 | 2% | 0% | -100% | -95% | -96% |
| COPPER | 84 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 79 | 0 | 4% | 1% | -100% | -93% | -90% |
| PLATINUM | 74 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 62 | 0 | 2% | 0% | -100% | -97% | -100% |
| GBPUSD | 42 | 0 | 2% | 0% | -100% | -96% | -94% |
| USDJPY | 35 | 2 | 6% | 6% | +433% | -90% | -85% |
| EURUSD | 34 | 0 | 3% | 0% | -100% | -95% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 986 | 5 | 4% | 2% | -41% | -92% | -92% |
| DOWN (bought NO) | 892 | 3 | 3% | 1% | -61% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 119 | 0 | 3% | 2% | -100% | -91% | -91% |
| 0.05–0.1% | 144 | 0 | 1% | 0% | -100% | -95% | -96% |
| 0.1–0.2% | 277 | 0 | 4% | 1% | -100% | -91% | -91% |
| 0.2–0.5% | 448 | 2 | 4% | 2% | -51% | -91% | -92% |
| Over 0.5% | 198 | 4 | 7% | 4% | +113% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 382 | 4 | 3% | 1% | +22% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,695 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 7:29:45 AM | ETH | DOWN | 15 sec | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:29:45 AM | PLATINUM | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:29:29 AM | BTC | UP | 31 sec | -0.045% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:29:29 AM | ZEC | UP | 31 sec | -0.139% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:29:13 AM | GOLD | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:28:57 AM | NATGAS | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:28:57 AM | DOGE | DOWN | 63 sec | +0.114% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:28:41 AM | COPPER | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:28:41 AM | BNB | DOWN | 79 sec | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:28:41 AM | HYPE | DOWN | 79 sec | +0.058% | 3¢ | ❌ Lost | -$0.15 |
| 9/29 7:28:25 AM | SOL | DOWN | 1.6 min | +0.212% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:27:53 AM | NEAR | DOWN | 2.1 min | +0.725% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:24:39 AM | PALLADIUM | UP | 5.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:14:54 AM | PLATINUM | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:14:54 AM | SILVER | DOWN | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:14:38 AM | XRP | UP | 21 sec | -0.090% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:14:22 AM | SOL | DOWN | 37 sec | +0.116% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:14:22 AM | BNB | DOWN | 37 sec | +0.004% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:14:08 AM | DOGE | DOWN | 52 sec | +0.144% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:13:34 AM | ZEC | DOWN | 86 sec | +0.276% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:13:18 AM | BTC | DOWN | 1.7 min | +0.083% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:13:18 AM | WTI | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:13:03 AM | GOLD | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:13:03 AM | NEAR | UP | 1.9 min | -0.484% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:13:03 AM | GBPUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:10:37 AM | PALLADIUM | DOWN | 4.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:10:05 AM | HYPE | DOWN | 4.9 min | +0.618% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:59:55 AM | GBPUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:59:37 AM | WTI | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:59:21 AM | BTC | UP | 39 sec | -0.038% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
