# 15-Minute 1¢ Study

*Updated Tue Sep 29, 4:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 64 finished bets | 3% | $18.40 | +192% | +28.75¢ | $23.20 / -$4.80 |

*Expect about **48 buys a day** (~$7.15/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 230 | $12.15 | +41% |
| 5+ min left, sell at 50¢ | 64 | $3.90 | +41% |
| Volatility model ≥ 5%, sell at 25¢ | 83 | $1.23 | +14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1825 | 1819 | 8 (0%) | 1.07% | -$107.45 (-49%) | Hold to the close: -$107.45 (-49%) |

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
| Volatility model | 958 | 2.7% | 0.4% (4) | -375% | ❌ Worse |
| Momentum model | 958 | 2.8% | 0.4% (4) | -445% | ❌ Worse |
| Mean-reversion model | 958 | 5.8% | 0.4% (4) | -461% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 958 | 4 | -46% | -90% | -92% | -88% |
| Volatility model ≥ 2% | 184 | 1 | -37% | -86% | -88% | -82% |
| Volatility model ≥ 5% | 83 | 0 | -100% | -73% | -73% | -63% |
| Volatility model ≥ 10% | 42 | 0 | -100% | -72% | -69% | -48% |
| Momentum model ≥ 2% | 151 | 0 | -100% | -87% | -91% | -89% |
| Momentum model ≥ 5% | 86 | 0 | -100% | -83% | -92% | -86% |
| Momentum model ≥ 10% | 56 | 0 | -100% | -90% | -85% | -75% |
| Mean-reversion model ≥ 2% | 355 | 3 | -8% | -86% | -87% | -82% |
| Mean-reversion model ≥ 5% | 230 | 3 | +41% | -83% | -84% | -76% |
| Mean-reversion model ≥ 10% | 146 | 2 | +54% | -79% | -81% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1153 | 4% | 2% | 2% | 2% | 1% | 1% |
| Commodities | 561 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 105 | 3% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1819 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$107.45 | -49% | — |
| Sell at 2¢ | 60 | 3% | -$203.85 | -93% | 40 sec |
| Sell at 3¢ | 35 | 2% | -$205.80 | -94% | 47 sec |
| Sell at 5¢ | 25 | 1% | -$203.20 | -93% | 81 sec |
| Sell at 10¢ | 23 | 1% | -$189.32 | -86% | 1.9 min |
| Sell at 25¢ | 13 | 1% | -$176.42 | -80% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$158.70 | -72% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 64 | 2 | 8% | 3% | +192% | -86% | -88% |
| 2–5 min | 610 | 5 | 6% | 3% | -21% | -89% | -90% |
| 1–2 min | 499 | 1 | 2% | 1% | -78% | -96% | -96% |
| Under 1 min | 646 | 0 | 1% | 0% | -100% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 132 | 2 | 5% | 3% | +89% | -89% | -87% |
| ZEC | 130 | 1 | 5% | 2% | -7% | -88% | -95% |
| NEAR | 129 | 0 | 5% | 2% | -100% | -88% | -94% |
| DOGE | 129 | 1 | 5% | 2% | -4% | -89% | -87% |
| XRP | 129 | 2 | 3% | 2% | +96% | -93% | -92% |
| BTC | 128 | 0 | 8% | 2% | -100% | -81% | -88% |
| SOL | 127 | 0 | 2% | 2% | -100% | -94% | -90% |
| BNB | 125 | 0 | 2% | 1% | -100% | -95% | -95% |
| HYPE | 124 | 0 | 2% | 2% | -100% | -95% | -95% |
| GOLD | 96 | 0 | 2% | 0% | -100% | -95% | -100% |
| SILVER | 89 | 0 | 2% | 0% | -100% | -95% | -96% |
| WTI | 88 | 0 | 1% | 0% | -100% | -98% | -100% |
| COPPER | 81 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 76 | 0 | 4% | 1% | -100% | -93% | -90% |
| PLATINUM | 72 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 59 | 0 | 2% | 0% | -100% | -97% | -100% |
| GBPUSD | 40 | 0 | 2% | 0% | -100% | -96% | -94% |
| USDJPY | 33 | 2 | 6% | 6% | +466% | -89% | -84% |
| EURUSD | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 962 | 5 | 4% | 2% | -39% | -92% | -92% |
| DOWN (bought NO) | 857 | 3 | 3% | 1% | -60% | -94% | -96% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 114 | 0 | 3% | 2% | -100% | -90% | -90% |
| 0.05–0.1% | 136 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 268 | 0 | 4% | 1% | -100% | -90% | -91% |
| 0.2–0.5% | 439 | 2 | 5% | 2% | -50% | -91% | -92% |
| Over 0.5% | 196 | 4 | 7% | 4% | +115% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 562 | 1 | 3% | 1% | -79% | -93% | -95% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,808 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 4:44:28 AM | COPPER | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:44:12 AM | ZEC | UP | 48 sec | -0.195% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:43:22 AM | BNB | UP | 1.6 min | -0.123% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:43:22 AM | ETH | UP | 1.6 min | -0.155% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:43:22 AM | HYPE | UP | 1.6 min | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:43:07 AM | XRP | UP | 1.9 min | -0.226% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:42:49 AM | BTC | UP | 2.2 min | -0.109% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:42:02 AM | SOL | UP | 3.0 min | -0.303% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:42:02 AM | DOGE | UP | 3.0 min | -0.314% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:39:37 AM | NEAR | UP | 5.4 min | -1.133% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:29:22 AM | NATGAS | DOWN | 38 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:29:06 AM | SILVER | UP | 54 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 9/29 4:28:33 AM | BTC | UP | 86 sec | -0.103% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:28:33 AM | ETH | UP | 86 sec | -0.107% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:28:33 AM | SOL | UP | 86 sec | -0.170% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:28:33 AM | NEAR | DOWN | 86 sec | +0.295% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:28:01 AM | XRP | UP | 2.0 min | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:26:24 AM | DOGE | UP | 3.6 min | -0.267% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:25:19 AM | HYPE | UP | 4.7 min | -0.369% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:25:03 AM | ZEC | UP | 4.9 min | -0.531% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:25:03 AM | BNB | UP | 4.9 min | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:14:51 AM | BTC | UP | 9 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:14:51 AM | XRP | UP | 9 sec | -0.113% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:14:51 AM | GBPUSD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:14:35 AM | ETH | UP | 25 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:14:35 AM | NEAR | UP | 25 sec | -0.247% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:14:35 AM | BNB | UP | 25 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:14:19 AM | EURUSD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:14:19 AM | PLATINUM | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:14:19 AM | DOGE | UP | 41 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
