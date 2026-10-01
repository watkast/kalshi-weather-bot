# 15-Minute 1¢ Study

*Updated Thu Oct 1, 3:31 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 142 finished bets | 1% | $7.15 | +34% | +5.04¢ | $17.35 / -$10.20 |

*Expect about **38 buys a day** (~$5.63/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 287 | -$3.50 | -11% |
| Volatility model ≥ 5%, sell at 25¢ | 278 | -$6.67 | -22% |
| 5+ min left, sell at 50¢ | 142 | -$7.35 | -35% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4692 | 4686 | 15 (0%) | 1.07% | -$364.50 (-63%) | Hold to the close: -$364.50 (-63%) |

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
| Volatility model | 2682 | 3.5% | 0.2% (6) | -682% | ❌ Worse |
| Momentum model | 2682 | 3.7% | 0.2% (6) | -738% | ❌ Worse |
| Mean-reversion model | 2682 | 6.6% | 0.2% (6) | -866% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2682 | 6 | -72% | -85% | -86% | -84% |
| Volatility model ≥ 2% | 551 | 3 | -38% | -64% | -65% | -61% |
| Volatility model ≥ 5% | 278 | 1 | -54% | -36% | -36% | -33% |
| Volatility model ≥ 10% | 157 | 1 | -7% | +11% | +9% | +15% |
| Momentum model ≥ 2% | 495 | 2 | -52% | -61% | -65% | -62% |
| Momentum model ≥ 5% | 287 | 2 | -11% | -42% | -44% | -39% |
| Momentum model ≥ 10% | 192 | 1 | -27% | -17% | -16% | -13% |
| Mean-reversion model ≥ 2% | 1017 | 3 | -68% | -86% | -88% | -84% |
| Mean-reversion model ≥ 5% | 669 | 3 | -52% | -83% | -85% | -79% |
| Mean-reversion model ≥ 10% | 423 | 2 | -47% | -78% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2878 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1387 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 421 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 4686 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 15 | 0% | -$364.50 | -63% | — |
| Sell at 2¢ | 174 | 4% | -$515.26 | -90% | 46 sec |
| Sell at 3¢ | 105 | 2% | -$519.55 | -90% | 49 sec |
| Sell at 5¢ | 77 | 2% | -$510.45 | -89% | 66 sec |
| Sell at 10¢ | 56 | 1% | -$473.14 | -82% | 81 sec |
| Sell at 25¢ | 26 | 1% | -$446.44 | -78% | 1.6 min |
| Sell at 50¢ | 13 | 0% | -$416.75 | -73% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 139 | 2 | 13% | 3% | +37% | -77% | -89% |
| 2–5 min | 1547 | 7 | 7% | 3% | -56% | -88% | -89% |
| 1–2 min | 1219 | 4 | 3% | 2% | -65% | -94% | -93% |
| Under 1 min | 1778 | 2 | 1% | 0% | -84% | -90% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 326 | 1 | 4% | 1% | -60% | -90% | -92% |
| ETH | 322 | 2 | 5% | 3% | -24% | -89% | -86% |
| ZEC | 320 | 1 | 5% | 2% | -63% | -89% | -94% |
| BNB | 320 | 0 | 4% | 1% | -100% | -91% | -94% |
| HYPE | 319 | 1 | 5% | 3% | -62% | -89% | -87% |
| NEAR | 318 | 0 | 5% | 2% | -100% | -88% | -91% |
| BTC | 318 | 0 | 7% | 3% | -100% | -84% | -88% |
| XRP | 318 | 3 | 2% | 1% | +22% | -55% | -55% |
| SOL | 317 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 238 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 221 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 212 | 1 | 3% | 1% | -51% | -94% | -96% |
| COPPER | 197 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 181 | 1 | 4% | 2% | -48% | -93% | -91% |
| PLATINUM | 173 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 165 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 149 | 1 | 5% | 2% | -37% | -92% | -93% |
| EURUSD | 148 | 1 | 4% | 2% | -37% | -93% | -93% |
| USDJPY | 124 | 3 | 3% | 2% | +126% | -94% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2391 | 9 | 4% | 2% | -57% | -92% | -92% |
| DOWN (bought NO) | 2295 | 6 | 4% | 1% | -70% | -87% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 336 | 1 | 1% | 1% | -45% | -41% | -40% |
| 0.05–0.1% | 404 | 0 | 2% | 0% | -100% | -94% | -97% |
| 0.1–0.2% | 694 | 1 | 4% | 1% | -81% | -91% | -92% |
| 0.2–0.5% | 970 | 2 | 6% | 3% | -77% | -88% | -89% |
| Over 0.5% | 473 | 4 | 7% | 2% | -13% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 972 | 2 | 3% | 1% | -76% | -81% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,176 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 3:29:48 PM | SOL | UP | 11 sec | -0.107% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:29:44 PM | BNB | DOWN | 15 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:29:24 PM | BTC | UP | 35 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:29:14 PM | XRP | UP | 45 sec | -0.167% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:29:05 PM | ETH | UP | 54 sec | -0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:28:48 PM | HYPE | UP | 72 sec | -0.311% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:28:26 PM | DOGE | UP | 1.6 min | -0.142% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:28:14 PM | ZEC | UP | 1.8 min | -0.322% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:14:59 PM | BNB | DOWN | 1 sec | -0.019% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:14:57 PM | WTI | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:13:46 PM | DOGE | UP | 73 sec | -0.146% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:13:40 PM | XRP | UP | 79 sec | -0.194% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:13:40 PM | ZEC | UP | 79 sec | -0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:13:38 PM | HYPE | UP | 81 sec | -0.141% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:12:59 PM | ETH | UP | 2.0 min | -0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:12:46 PM | SOL | UP | 2.2 min | -0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:12:40 PM | NEAR | UP | 2.3 min | -0.672% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:59:52 PM | BTC | DOWN | 8 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/1 2:59:50 PM | XRP | UP | 10 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/1 2:59:28 PM | DOGE | UP | 32 sec | -0.080% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:59:22 PM | SILVER | DOWN | 38 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 2:59:10 PM | ETH | DOWN | 50 sec | +0.027% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 2:59:08 PM | PALLADIUM | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:58:27 PM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:58:25 PM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 2:58:09 PM | ZEC | DOWN | 1.9 min | +0.444% | 0¢ | ❌ Lost | $0.00 |
| 10/1 2:57:59 PM | BNB | DOWN | 2.0 min | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/1 2:57:40 PM | SOL | DOWN | 2.3 min | +0.119% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 2:57:16 PM | USDJPY | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:56:54 PM | EURUSD | UP | 3.1 min | — | 83¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
