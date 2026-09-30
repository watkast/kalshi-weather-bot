# 15-Minute 1¢ Study

*Updated Wed Sep 30, 5:37 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 93 finished bets | 2% | $14.20 | +103% | +15.27¢ | $21.10 / -$6.90 |

*Expect about **39 buys a day** (~$5.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 93 | -$0.30 | -2% |
| Momentum model ≥ 5%, hold to the close | 167 | -$4.75 | -25% |
| Volatility model ≥ 5%, sell at 25¢ | 154 | -$6.57 | -40% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3071 | 3065 | 13 (0%) | 1.07% | -$192.70 (-51%) | Hold to the close: -$192.70 (-51%) |

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
| Volatility model | 1720 | 3.0% | 0.3% (5) | -494% | ❌ Worse |
| Momentum model | 1720 | 3.1% | 0.3% (5) | -553% | ❌ Worse |
| Mean-reversion model | 1720 | 5.9% | 0.3% (5) | -614% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1720 | 5 | -64% | -90% | -90% | -87% |
| Volatility model ≥ 2% | 330 | 2 | -31% | -85% | -86% | -82% |
| Volatility model ≥ 5% | 154 | 0 | -100% | -75% | -74% | -65% |
| Volatility model ≥ 10% | 83 | 0 | -100% | -76% | -74% | -65% |
| Momentum model ≥ 2% | 297 | 1 | -61% | -85% | -88% | -85% |
| Momentum model ≥ 5% | 167 | 1 | -25% | -83% | -88% | -83% |
| Momentum model ≥ 10% | 106 | 0 | -100% | -87% | -85% | -81% |
| Mean-reversion model ≥ 2% | 638 | 3 | -50% | -86% | -86% | -81% |
| Mean-reversion model ≥ 5% | 411 | 3 | -22% | -83% | -83% | -75% |
| Mean-reversion model ≥ 10% | 255 | 2 | -13% | -78% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1916 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 926 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 223 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 3065 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$192.70 | -51% | — |
| Sell at 2¢ | 116 | 4% | -$344.54 | -92% | 47 sec |
| Sell at 3¢ | 74 | 2% | -$345.84 | -92% | 50 sec |
| Sell at 5¢ | 54 | 2% | -$339.60 | -91% | 64 sec |
| Sell at 10¢ | 44 | 1% | -$303.06 | -81% | 72 sec |
| Sell at 25¢ | 22 | 1% | -$287.88 | -77% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$251.70 | -67% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 93 | 2 | 10% | 2% | +103% | -83% | -89% |
| 2–5 min | 1028 | 6 | 7% | 3% | -43% | -88% | -89% |
| 1–2 min | 819 | 4 | 4% | 2% | -48% | -93% | -92% |
| Under 1 min | 1125 | 1 | 1% | 0% | -87% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 216 | 1 | 4% | 1% | -41% | -90% | -90% |
| ZEC | 215 | 1 | 5% | 3% | -44% | -89% | -91% |
| ETH | 214 | 2 | 5% | 4% | +11% | -89% | -86% |
| NEAR | 213 | 0 | 5% | 1% | -100% | -89% | -92% |
| XRP | 213 | 2 | 2% | 2% | +22% | -94% | -93% |
| SOL | 213 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 211 | 0 | 7% | 3% | -100% | -85% | -88% |
| BNB | 211 | 0 | 3% | 1% | -100% | -94% | -96% |
| HYPE | 210 | 1 | 5% | 3% | -39% | -89% | -86% |
| GOLD | 164 | 0 | 5% | 1% | -100% | -88% | -92% |
| WTI | 144 | 1 | 3% | 1% | -26% | -93% | -94% |
| SILVER | 144 | 0 | 2% | 1% | -100% | -95% | -95% |
| COPPER | 134 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 127 | 1 | 4% | 2% | -27% | -93% | -90% |
| PLATINUM | 107 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 106 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 81 | 1 | 5% | 2% | +15% | -91% | -90% |
| EURUSD | 75 | 1 | 4% | 1% | +24% | -93% | -97% |
| USDJPY | 67 | 2 | 3% | 3% | +179% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1584 | 8 | 4% | 2% | -42% | -92% | -92% |
| DOWN (bought NO) | 1481 | 5 | 4% | 2% | -61% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 197 | 0 | 2% | 2% | -100% | -93% | -92% |
| 0.05–0.1% | 257 | 0 | 1% | 0% | -100% | -96% | -98% |
| 0.1–0.2% | 465 | 1 | 4% | 2% | -72% | -91% | -92% |
| 0.2–0.5% | 695 | 2 | 6% | 3% | -69% | -88% | -88% |
| Over 0.5% | 301 | 4 | 6% | 2% | +39% | -89% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 871 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,516 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 5:29:48 AM | WTI | UP | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 5:29:48 AM | ZEC | DOWN | 11 sec | -0.048% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:29:16 AM | BNB | UP | 43 sec | -0.066% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:29:16 AM | SILVER | DOWN | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:29:16 AM | SOL | DOWN | 43 sec | +0.101% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:29:16 AM | BTC | DOWN | 43 sec | +0.031% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:29:00 AM | GOLD | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:29:00 AM | HYPE | DOWN | 60 sec | +0.121% | 0¢ | ❌ Lost | $0.00 |
| 9/30 5:28:44 AM | ETH | DOWN | 75 sec | +0.052% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:28:44 AM | DOGE | DOWN | 75 sec | +0.142% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:28:28 AM | NEAR | UP | 1.5 min | -0.303% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 5:28:12 AM | XRP | DOWN | 1.8 min | +0.199% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:14:41 AM | HYPE | UP | 18 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 9/30 5:13:53 AM | WTI | DOWN | 67 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:13:53 AM | PLATINUM | UP | 67 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:13:53 AM | NEAR | DOWN | 67 sec | +0.799% | 0¢ | ❌ Lost | $0.00 |
| 9/30 5:13:53 AM | PALLADIUM | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:13:53 AM | NATGAS | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:13:21 AM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:12:32 AM | GOLD | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:12:16 AM | BNB | UP | 2.7 min | -0.213% | 26¢ | ❌ Lost | -$0.15 |
| 9/30 5:12:00 AM | DOGE | UP | 3.0 min | -0.350% | 4¢ | ❌ Lost | -$0.15 |
| 9/30 5:11:45 AM | XRP | UP | 3.2 min | -0.298% | 1¢ | ❌ Lost | $0.00 |
| 9/30 5:11:45 AM | GBPUSD | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:11:45 AM | COPPER | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:11:14 AM | ZEC | UP | 3.8 min | -0.595% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:10:58 AM | SILVER | UP | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:10:42 AM | ETH | UP | 4.3 min | -0.257% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:10:25 AM | BTC | UP | 4.6 min | -0.240% | 6¢ | ❌ Lost | -$0.15 |
| 9/30 5:10:09 AM | SOL | UP | 4.8 min | -0.500% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
