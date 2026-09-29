# 15-Minute 1¢ Study

*Updated Tue Sep 29, 12:00 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 69 finished bets | 3% | $17.65 | +171% | +25.58¢ | $22.90 / -$5.25 |

*Expect about **43 buys a day** (~$6.40/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 286 | $4.50 | +12% |
| 5+ min left, sell at 50¢ | 69 | $3.15 | +30% |
| Volatility model ≥ 5%, sell at 25¢ | 103 | -$0.87 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2149 | 2133 | 10 (0%) | 1.07% | -$117.70 (-46%) | Hold to the close: -$117.70 (-46%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 1143 | 2.8% | 0.3% (4) | -443% | ❌ Worse |
| Momentum model | 1143 | 3.0% | 0.3% (4) | -518% | ❌ Worse |
| Mean-reversion model | 1143 | 5.9% | 0.3% (4) | -530% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1143 | 4 | -55% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 227 | 1 | -49% | -85% | -86% | -83% |
| Volatility model ≥ 5% | 103 | 0 | -100% | -74% | -71% | -64% |
| Volatility model ≥ 10% | 52 | 0 | -100% | -72% | -66% | -58% |
| Momentum model ≥ 2% | 187 | 0 | -100% | -86% | -88% | -88% |
| Momentum model ≥ 5% | 108 | 0 | -100% | -83% | -87% | -84% |
| Momentum model ≥ 10% | 67 | 0 | -100% | -88% | -81% | -79% |
| Mean-reversion model ≥ 2% | 438 | 3 | -27% | -86% | -86% | -83% |
| Mean-reversion model ≥ 5% | 286 | 3 | +12% | -83% | -83% | -77% |
| Mean-reversion model ≥ 10% | 175 | 2 | +28% | -77% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1338 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 661 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 134 | 4% | 4% | 3% | 2% | 2% | 1% |
| **All** | 2133 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$117.70 | -46% | — |
| Sell at 2¢ | 76 | 4% | -$237.94 | -92% | 47 sec |
| Sell at 3¢ | 47 | 2% | -$239.37 | -93% | 47 sec |
| Sell at 5¢ | 34 | 2% | -$235.60 | -91% | 72 sec |
| Sell at 10¢ | 29 | 1% | -$205.71 | -80% | 1.6 min |
| Sell at 25¢ | 15 | 1% | -$194.05 | -75% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$168.95 | -66% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 69 | 2 | 10% | 3% | +171% | -82% | -89% |
| 2–5 min | 714 | 5 | 6% | 3% | -32% | -89% | -89% |
| 1–2 min | 577 | 2 | 3% | 1% | -63% | -94% | -94% |
| Under 1 min | 773 | 1 | 1% | 0% | -80% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 153 | 2 | 5% | 4% | +61% | -88% | -84% |
| ZEC | 151 | 1 | 5% | 2% | -18% | -88% | -93% |
| DOGE | 150 | 1 | 4% | 2% | -15% | -91% | -88% |
| XRP | 150 | 2 | 3% | 2% | +70% | -94% | -93% |
| BTC | 149 | 0 | 8% | 3% | -100% | -80% | -88% |
| NEAR | 147 | 0 | 5% | 1% | -100% | -88% | -92% |
| SOL | 147 | 0 | 4% | 2% | -100% | -89% | -86% |
| BNB | 146 | 0 | 2% | 1% | -100% | -96% | -96% |
| HYPE | 145 | 0 | 3% | 1% | -100% | -94% | -93% |
| GOLD | 115 | 0 | 2% | 0% | -100% | -96% | -100% |
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
| UP (bought YES) | 1133 | 7 | 4% | 2% | -29% | -92% | -92% |
| DOWN (bought NO) | 1000 | 3 | 4% | 2% | -65% | -92% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 130 | 0 | 2% | 2% | -100% | -91% | -91% |
| 0.05–0.1% | 161 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 304 | 0 | 4% | 1% | -100% | -90% | -92% |
| 0.2–0.5% | 507 | 2 | 5% | 3% | -57% | -89% | -90% |
| Over 0.5% | 236 | 4 | 6% | 3% | +79% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 637 | 6 | 4% | 2% | +9% | -92% | -91% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,752 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 11:59:24 AM | EURUSD | UP | 35 sec | — | 0¢ | In play | — |
| 9/29 11:59:08 AM | ZEC | UP | 52 sec | -0.087% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:58:51 AM | WTI | UP | 68 sec | — | 1¢ | In play | — |
| 9/29 11:58:35 AM | GOLD | UP | 84 sec | — | 4¢ | In play | — |
| 9/29 11:58:19 AM | COPPER | UP | 1.7 min | — | 0¢ | In play | — |
| 9/29 11:58:19 AM | DOGE | UP | 1.7 min | -0.293% | 0¢ | In play | — |
| 9/29 11:58:19 AM | XRP | UP | 1.7 min | -0.324% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:58:19 AM | GBPUSD | UP | 1.7 min | — | 0¢ | In play | — |
| 9/29 11:58:03 AM | ETH | UP | 1.9 min | -0.174% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:57:30 AM | BTC | UP | 2.5 min | -0.164% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:56:58 AM | SOL | UP | 3.0 min | -0.330% | 1¢ | In play | — |
| 9/29 11:56:25 AM | BNB | UP | 3.6 min | -0.276% | 1¢ | In play | — |
| 9/29 11:55:53 AM | HYPE | UP | 4.1 min | -0.478% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:55:53 AM | USDJPY | DOWN | 4.1 min | — | 0¢ | In play | — |
| 9/29 11:52:07 AM | NEAR | UP | 7.9 min | -2.440% | 3¢ | In play | — |
| 9/29 11:44:58 AM | BTC | DOWN | 2 sec | +0.016% | 0¢ | ❌ Lost | $0.00 |
| 9/29 11:44:58 AM | SOL | DOWN | 2 sec | -0.030% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:44:42 AM | ETH | UP | 18 sec | -0.041% | 0¢ | ❌ Lost | $0.00 |
| 9/29 11:44:42 AM | BNB | UP | 18 sec | -0.053% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:44:26 AM | XRP | UP | 34 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 9/29 11:44:11 AM | HYPE | UP | 48 sec | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:44:11 AM | DOGE | DOWN | 48 sec | +0.117% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:43:39 AM | GOLD | UP | 81 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:42:48 AM | NEAR | DOWN | 2.2 min | +0.617% | 4¢ | ❌ Lost | $0.00 |
| 9/29 11:42:01 AM | ZEC | DOWN | 3.0 min | +0.412% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:29:55 AM | NATGAS | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:29:55 AM | PALLADIUM | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:29:39 AM | PLATINUM | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:29:39 AM | WTI | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:29:23 AM | GBPUSD | UP | 36 sec | — | 6¢ | ✅ Won | $13.85 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
