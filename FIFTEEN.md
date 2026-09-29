# 15-Minute 1¢ Study

*Updated Tue Sep 29, 12:10 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 70 finished bets | 3% | $17.50 | +167% | +25.00¢ | $22.75 / -$5.25 |

*Expect about **44 buys a day** (~$6.65/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 286 | $4.50 | +12% |
| 5+ min left, sell at 50¢ | 70 | $3.00 | +29% |
| Volatility model ≥ 5%, sell at 25¢ | 103 | -$0.87 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2157 | 2143 | 10 (0%) | 1.07% | -$119.20 (-46%) | Hold to the close: -$119.20 (-46%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 1147 | 2.8% | 0.3% (4) | -442% | ❌ Worse |
| Momentum model | 1147 | 3.0% | 0.3% (4) | -517% | ❌ Worse |
| Mean-reversion model | 1147 | 5.9% | 0.3% (4) | -530% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1147 | 4 | -55% | -89% | -90% | -87% |
| Volatility model ≥ 2% | 227 | 1 | -49% | -85% | -86% | -83% |
| Volatility model ≥ 5% | 103 | 0 | -100% | -74% | -71% | -64% |
| Volatility model ≥ 10% | 52 | 0 | -100% | -72% | -66% | -58% |
| Momentum model ≥ 2% | 187 | 0 | -100% | -86% | -88% | -88% |
| Momentum model ≥ 5% | 108 | 0 | -100% | -83% | -87% | -84% |
| Momentum model ≥ 10% | 67 | 0 | -100% | -88% | -81% | -79% |
| Mean-reversion model ≥ 2% | 439 | 3 | -27% | -86% | -86% | -83% |
| Mean-reversion model ≥ 5% | 286 | 3 | +12% | -83% | -83% | -77% |
| Mean-reversion model ≥ 10% | 175 | 2 | +28% | -77% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1342 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 664 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 137 | 4% | 4% | 3% | 2% | 2% | 1% |
| **All** | 2143 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$119.20 | -46% | — |
| Sell at 2¢ | 78 | 4% | -$238.92 | -92% | 47 sec |
| Sell at 3¢ | 49 | 2% | -$240.09 | -93% | 47 sec |
| Sell at 5¢ | 34 | 2% | -$237.10 | -91% | 72 sec |
| Sell at 10¢ | 29 | 1% | -$207.21 | -80% | 1.6 min |
| Sell at 25¢ | 15 | 1% | -$195.55 | -75% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$170.45 | -66% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 70 | 2 | 11% | 3% | +167% | -80% | -85% |
| 2–5 min | 717 | 5 | 6% | 3% | -32% | -89% | -89% |
| 1–2 min | 582 | 2 | 3% | 1% | -63% | -94% | -93% |
| Under 1 min | 774 | 1 | 1% | 0% | -80% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 153 | 2 | 5% | 4% | +61% | -88% | -84% |
| DOGE | 151 | 1 | 4% | 2% | -16% | -91% | -88% |
| ZEC | 151 | 1 | 5% | 2% | -18% | -88% | -93% |
| XRP | 150 | 2 | 3% | 2% | +70% | -94% | -93% |
| BTC | 149 | 0 | 8% | 3% | -100% | -80% | -88% |
| NEAR | 148 | 0 | 5% | 1% | -100% | -86% | -89% |
| SOL | 148 | 0 | 4% | 2% | -100% | -89% | -87% |
| BNB | 147 | 0 | 2% | 1% | -100% | -96% | -96% |
| HYPE | 145 | 0 | 3% | 1% | -100% | -94% | -93% |
| GOLD | 116 | 0 | 3% | 0% | -100% | -94% | -97% |
| WTI | 105 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 104 | 0 | 3% | 1% | -100% | -94% | -94% |
| COPPER | 97 | 0 | 1% | 1% | -100% | -98% | -97% |
| NATGAS | 91 | 0 | 3% | 1% | -100% | -94% | -91% |
| PLATINUM | 81 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 70 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 52 | 1 | 4% | 2% | +79% | -93% | -90% |
| EURUSD | 45 | 1 | 4% | 2% | +107% | -92% | -94% |
| USDJPY | 40 | 2 | 5% | 5% | +367% | -91% | -87% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1142 | 7 | 4% | 2% | -29% | -92% | -92% |
| DOWN (bought NO) | 1001 | 3 | 3% | 1% | -65% | -92% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 130 | 0 | 2% | 2% | -100% | -91% | -91% |
| 0.05–0.1% | 161 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 304 | 0 | 4% | 1% | -100% | -90% | -92% |
| 0.2–0.5% | 510 | 2 | 5% | 3% | -57% | -89% | -90% |
| Over 0.5% | 237 | 4 | 7% | 3% | +78% | -87% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,764 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 12:10:37 PM | BTC | DOWN | 4.4 min | +0.311% | — | In play | — |
| 9/29 12:10:37 PM | PALLADIUM | DOWN | 4.4 min | — | — | In play | — |
| 9/29 12:10:37 PM | USDJPY | UP | 4.4 min | — | — | In play | — |
| 9/29 12:10:21 PM | BNB | DOWN | 4.7 min | +0.276% | — | In play | — |
| 9/29 12:10:21 PM | SOL | DOWN | 4.7 min | +0.554% | — | In play | — |
| 9/29 12:09:18 PM | ZEC | DOWN | 5.7 min | +1.000% | — | In play | — |
| 9/29 12:06:19 PM | SILVER | DOWN | 8.7 min | — | — | In play | — |
| 9/29 12:05:13 PM | GBPUSD | DOWN | 9.8 min | — | — | In play | — |
| 9/29 11:59:24 AM | EURUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:59:08 AM | ZEC | UP | 52 sec | -0.087% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:58:51 AM | WTI | UP | 68 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:58:35 AM | GOLD | UP | 84 sec | — | 4¢ | ❌ Lost | -$0.15 |
| 9/29 11:58:19 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:58:19 AM | DOGE | UP | 1.7 min | -0.293% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:58:19 AM | XRP | UP | 1.7 min | -0.324% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:58:19 AM | GBPUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:58:03 AM | ETH | UP | 1.9 min | -0.174% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:57:30 AM | BTC | UP | 2.5 min | -0.164% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:56:58 AM | SOL | UP | 3.0 min | -0.330% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:56:25 AM | BNB | UP | 3.6 min | -0.276% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:55:53 AM | HYPE | UP | 4.1 min | -0.478% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:55:53 AM | USDJPY | DOWN | 4.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:52:07 AM | NEAR | UP | 7.9 min | -2.440% | 3¢ | ❌ Lost | -$0.15 |
| 9/29 11:44:58 AM | BTC | DOWN | 2 sec | +0.016% | 0¢ | ❌ Lost | $0.00 |
| 9/29 11:44:58 AM | SOL | DOWN | 2 sec | -0.030% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:44:42 AM | ETH | UP | 18 sec | -0.041% | 0¢ | ❌ Lost | $0.00 |
| 9/29 11:44:42 AM | BNB | UP | 18 sec | -0.053% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:44:26 AM | XRP | UP | 34 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 9/29 11:44:11 AM | HYPE | UP | 48 sec | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:44:11 AM | DOGE | DOWN | 48 sec | +0.117% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
