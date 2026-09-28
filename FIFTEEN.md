# 15-Minute 1¢ Study

*Updated Mon Sep 28, 2:50 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 123 finished bets | 2% | $26.25 | +167% | +21.34¢ | $6.05 / $20.20 |

*Expect **123 buys in the first 14 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 45 | $21.25 | +315% |
| Mean-reversion model ≥ 2%, hold to the close | 191 | $17.70 | +73% |
| 2–5 min left, hold to the close | 368 | $17.35 | +33% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1094 | 1088 | 7 (1%) | 1.07% | -$33.40 (-25%) | Hold to the close: -$33.40 (-25%) |

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
| Volatility model | 490 | 3.1% | 0.8% (4) | -281% | ❌ Worse |
| Momentum model | 490 | 3.2% | 0.8% (4) | -360% | ❌ Worse |
| Mean-reversion model | 490 | 6.3% | 0.8% (4) | -306% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 490 | 4 | +5% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 93 | 1 | +28% | -86% | -82% | -76% |
| Volatility model ≥ 5% | 45 | 0 | -100% | -74% | -68% | -61% |
| Volatility model ≥ 10% | 22 | 0 | -100% | -75% | -63% | -38% |
| Momentum model ≥ 2% | 83 | 0 | -100% | -86% | -88% | -86% |
| Momentum model ≥ 5% | 47 | 0 | -100% | -80% | -85% | -75% |
| Momentum model ≥ 10% | 31 | 0 | -100% | -83% | -74% | -57% |
| Mean-reversion model ≥ 2% | 191 | 3 | +73% | -85% | -86% | -81% |
| Mean-reversion model ≥ 5% | 123 | 3 | +167% | -82% | -80% | -71% |
| Mean-reversion model ≥ 10% | 81 | 2 | +179% | -79% | -77% | -68% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 685 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 347 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 56 | 2% | 2% | 2% | 2% | 2% | 2% |
| **All** | 1088 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 7 | 1% | -$33.40 | -25% | — |
| Sell at 2¢ | 34 | 3% | -$122.56 | -93% | 62 sec |
| Sell at 3¢ | 21 | 2% | -$123.21 | -94% | 67 sec |
| Sell at 5¢ | 14 | 1% | -$122.30 | -93% | 89 sec |
| Sell at 10¢ | 13 | 1% | -$114.37 | -87% | 1.9 min |
| Sell at 25¢ | 10 | 1% | -$98.30 | -75% | 2.1 min |
| Sell at 50¢ | 7 | 1% | -$84.15 | -64% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 45 | 2 | 7% | 4% | +315% | -88% | -83% |
| 2–5 min | 368 | 5 | 7% | 2% | +33% | -88% | -90% |
| 1–2 min | 329 | 0 | 2% | 0% | -100% | -97% | -97% |
| Under 1 min | 346 | 0 | 1% | 1% | -100% | -98% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 78 | 2 | 4% | 3% | +222% | -91% | -87% |
| DOGE | 78 | 1 | 5% | 3% | +44% | -89% | -84% |
| ZEC | 78 | 1 | 5% | 1% | +61% | -88% | -96% |
| XRP | 77 | 2 | 4% | 3% | +222% | -91% | -91% |
| NEAR | 76 | 0 | 1% | 0% | -100% | -96% | -100% |
| BTC | 76 | 0 | 9% | 3% | -100% | -76% | -85% |
| SOL | 76 | 0 | 4% | 3% | -100% | -90% | -84% |
| BNB | 75 | 0 | 1% | 0% | -100% | -97% | -96% |
| HYPE | 71 | 0 | 3% | 1% | -100% | -94% | -95% |
| GOLD | 62 | 0 | 3% | 0% | -100% | -93% | -100% |
| WTI | 58 | 0 | 2% | 0% | -100% | -97% | -100% |
| SILVER | 55 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 47 | 0 | 4% | 2% | -100% | -93% | -89% |
| COPPER | 45 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 44 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 36 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 15 | 1 | 7% | 7% | +522% | -88% | -83% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 590 | 5 | 3% | 1% | -0% | -93% | -93% |
| DOWN (bought NO) | 498 | 2 | 3% | 1% | -54% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 59 | 0 | 3% | 3% | -100% | -87% | -80% |
| 0.05–0.1% | 67 | 0 | 1% | 0% | -100% | -95% | -100% |
| 0.1–0.2% | 147 | 0 | 3% | 0% | -100% | -90% | -91% |
| 0.2–0.5% | 279 | 2 | 4% | 2% | -22% | -92% | -93% |
| Over 0.5% | 133 | 4 | 7% | 4% | +230% | -86% | -84% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 166 | 0 | 2% | 1% | -100% | -96% | -98% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,813 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 48 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 2:44:53 PM | COPPER | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:44:53 PM | WTI | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:44:53 PM | XRP | UP | 6 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:44:53 PM | PLATINUM | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:44:38 PM | SILVER | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:44:22 PM | ETH | UP | 37 sec | -0.037% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:44:22 PM | NEAR | UP | 37 sec | -0.472% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:44:22 PM | SOL | UP | 37 sec | -0.056% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:44:22 PM | BTC | UP | 37 sec | -0.043% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:44:22 PM | BNB | UP | 37 sec | -0.068% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:44:06 PM | NATGAS | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:43:50 PM | GOLD | UP | 69 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:43:50 PM | GBPUSD | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:43:18 PM | DOGE | UP | 1.7 min | -0.234% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:43:02 PM | HYPE | UP | 2.0 min | -0.286% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:42:46 PM | ZEC | UP | 2.2 min | -0.801% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:29:53 PM | USDJPY | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:29:38 PM | COPPER | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:29:38 PM | HYPE | DOWN | 22 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:29:38 PM | SOL | UP | 22 sec | -0.050% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:29:38 PM | GBPUSD | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:29:22 PM | NEAR | DOWN | 38 sec | +0.232% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:29:22 PM | XRP | DOWN | 38 sec | +0.141% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:29:22 PM | BTC | UP | 38 sec | -0.036% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 2:29:22 PM | PLATINUM | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:29:22 PM | BNB | DOWN | 38 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:29:06 PM | ZEC | DOWN | 54 sec | +0.252% | 0¢ | ❌ Lost | $0.00 |
| 9/28 2:28:35 PM | PALLADIUM | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:28:19 PM | WTI | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 2:28:19 PM | DOGE | DOWN | 1.7 min | +0.224% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
