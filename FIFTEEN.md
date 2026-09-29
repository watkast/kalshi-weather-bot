# 15-Minute 1¢ Study

*Updated Tue Sep 29, 11:40 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 69 finished bets | 3% | $17.65 | +171% | +25.58¢ | $22.90 / -$5.25 |

*Expect about **42 buys a day** (~$6.37/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 283 | $4.95 | +13% |
| 5+ min left, sell at 50¢ | 69 | $3.15 | +30% |
| Volatility model ≥ 5%, sell at 25¢ | 102 | -$0.72 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2124 | 2118 | 10 (0%) | 1.07% | -$116.05 (-45%) | Hold to the close: -$116.05 (-45%) |

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
| Volatility model | 1129 | 2.8% | 0.4% (4) | -414% | ❌ Worse |
| Momentum model | 1129 | 2.9% | 0.4% (4) | -489% | ❌ Worse |
| Mean-reversion model | 1129 | 5.9% | 0.4% (4) | -502% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1129 | 4 | -55% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 224 | 1 | -48% | -86% | -87% | -83% |
| Volatility model ≥ 5% | 102 | 0 | -100% | -73% | -71% | -63% |
| Volatility model ≥ 10% | 51 | 0 | -100% | -71% | -65% | -57% |
| Momentum model ≥ 2% | 183 | 0 | -100% | -87% | -89% | -88% |
| Momentum model ≥ 5% | 105 | 0 | -100% | -82% | -86% | -83% |
| Momentum model ≥ 10% | 66 | 0 | -100% | -87% | -81% | -79% |
| Mean-reversion model ≥ 2% | 434 | 3 | -26% | -86% | -87% | -83% |
| Mean-reversion model ≥ 5% | 283 | 3 | +13% | -83% | -83% | -77% |
| Mean-reversion model ≥ 10% | 174 | 2 | +29% | -77% | -78% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1324 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 660 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 134 | 4% | 4% | 3% | 2% | 2% | 1% |
| **All** | 2118 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$116.05 | -45% | — |
| Sell at 2¢ | 75 | 4% | -$236.55 | -92% | 47 sec |
| Sell at 3¢ | 46 | 2% | -$238.11 | -93% | 47 sec |
| Sell at 5¢ | 34 | 2% | -$233.95 | -91% | 72 sec |
| Sell at 10¢ | 29 | 1% | -$204.06 | -80% | 1.6 min |
| Sell at 25¢ | 15 | 1% | -$192.40 | -75% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$167.30 | -65% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 69 | 2 | 10% | 3% | +171% | -82% | -89% |
| 2–5 min | 710 | 5 | 6% | 3% | -32% | -89% | -90% |
| 1–2 min | 574 | 2 | 3% | 1% | -63% | -94% | -94% |
| Under 1 min | 765 | 1 | 1% | 0% | -79% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 151 | 2 | 5% | 4% | +62% | -88% | -84% |
| DOGE | 149 | 1 | 4% | 2% | -14% | -90% | -88% |
| ZEC | 149 | 1 | 5% | 2% | -17% | -88% | -93% |
| XRP | 148 | 2 | 3% | 2% | +71% | -94% | -93% |
| BTC | 147 | 0 | 8% | 3% | -100% | -80% | -88% |
| NEAR | 146 | 0 | 4% | 1% | -100% | -89% | -95% |
| SOL | 146 | 0 | 4% | 2% | -100% | -89% | -86% |
| BNB | 145 | 0 | 2% | 1% | -100% | -96% | -96% |
| HYPE | 143 | 0 | 3% | 1% | -100% | -94% | -93% |
| GOLD | 114 | 0 | 2% | 0% | -100% | -96% | -100% |
| WTI | 104 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 104 | 0 | 3% | 1% | -100% | -94% | -94% |
| COPPER | 96 | 0 | 1% | 1% | -100% | -98% | -97% |
| NATGAS | 91 | 0 | 3% | 1% | -100% | -94% | -91% |
| PLATINUM | 81 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 70 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 51 | 1 | 4% | 2% | +83% | -93% | -90% |
| EURUSD | 44 | 1 | 5% | 2% | +112% | -92% | -94% |
| USDJPY | 39 | 2 | 5% | 5% | +379% | -91% | -87% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1123 | 7 | 4% | 2% | -28% | -92% | -92% |
| DOWN (bought NO) | 995 | 3 | 3% | 2% | -65% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 127 | 0 | 2% | 2% | -100% | -91% | -91% |
| 0.05–0.1% | 158 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 300 | 0 | 4% | 1% | -100% | -90% | -92% |
| 0.2–0.5% | 504 | 2 | 5% | 3% | -56% | -89% | -90% |
| Over 0.5% | 235 | 4 | 6% | 3% | +79% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 622 | 6 | 4% | 2% | +11% | -92% | -91% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,670 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 11:29:55 AM | NATGAS | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:29:55 AM | PALLADIUM | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:29:39 AM | PLATINUM | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:29:39 AM | WTI | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:29:23 AM | GBPUSD | UP | 36 sec | — | 6¢ | ✅ Won | $13.85 |
| 9/29 11:29:07 AM | HYPE | UP | 53 sec | -0.190% | 0¢ | ❌ Lost | $0.00 |
| 9/29 11:28:49 AM | XRP | UP | 71 sec | -0.316% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:28:33 AM | EURUSD | UP | 87 sec | — | 44¢ | ✅ Won | $13.85 |
| 9/29 11:28:33 AM | ETH | UP | 87 sec | -0.149% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:28:02 AM | SOL | UP | 1.9 min | -0.200% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:27:28 AM | DOGE | UP | 2.5 min | -0.459% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:26:25 AM | NEAR | UP | 3.6 min | -0.997% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:25:52 AM | BNB | UP | 4.1 min | -0.278% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:14:57 AM | NATGAS | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:14:57 AM | ZEC | DOWN | 2 sec | +0.064% | 0¢ | ❌ Lost | $0.00 |
| 9/29 11:14:57 AM | SILVER | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:14:41 AM | HYPE | DOWN | 18 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 9/29 11:14:41 AM | SOL | DOWN | 18 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 9/29 11:14:41 AM | GOLD | DOWN | 18 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 11:14:25 AM | XRP | DOWN | 34 sec | +0.115% | 0¢ | ❌ Lost | $0.00 |
| 9/29 11:14:25 AM | BNB | DOWN | 34 sec | +0.044% | 0¢ | ❌ Lost | $0.00 |
| 9/29 11:14:09 AM | PALLADIUM | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:14:09 AM | WTI | UP | 51 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 11:14:09 AM | USDJPY | UP | 51 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:13:52 AM | PLATINUM | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:13:52 AM | BTC | DOWN | 67 sec | +0.079% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:13:52 AM | ETH | DOWN | 67 sec | +0.082% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:13:52 AM | DOGE | DOWN | 67 sec | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:13:20 AM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:59:43 AM | BTC | DOWN | 17 sec | +0.006% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
