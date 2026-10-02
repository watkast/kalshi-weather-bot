# 15-Minute 1¢ Study

*Updated Fri Oct 2, 2:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 171 finished bets | 1% | $2.80 | +11% | +1.64¢ | $15.40 / -$12.60 |

*Expect about **36 buys a day** (~$5.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 370 | $2.55 | +6% |
| Momentum model ≥ 5%, sell at 50¢ | 370 | -$4.70 | -12% |
| Volatility model ≥ 5%, sell at 25¢ | 364 | -$8.75 | -22% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5913 | 5907 | 22 (0%) | 1.07% | -$410.50 (-57%) | Hold to the close: -$410.50 (-57%) |

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
| Volatility model | 3403 | 3.7% | 0.3% (10) | -635% | ❌ Worse |
| Momentum model | 3403 | 3.8% | 0.3% (10) | -677% | ❌ Worse |
| Mean-reversion model | 3403 | 6.8% | 0.3% (10) | -798% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3403 | 10 | -62% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 727 | 5 | -21% | -64% | -65% | -61% |
| Volatility model ≥ 5% | 364 | 2 | -29% | -41% | -42% | -36% |
| Volatility model ≥ 10% | 210 | 2 | +42% | -5% | -7% | +1% |
| Momentum model ≥ 2% | 640 | 4 | -24% | -63% | -66% | -62% |
| Momentum model ≥ 5% | 370 | 3 | +6% | -47% | -51% | -45% |
| Momentum model ≥ 10% | 246 | 2 | +17% | -27% | -28% | -22% |
| Mean-reversion model ≥ 2% | 1307 | 7 | -42% | -84% | -86% | -81% |
| Mean-reversion model ≥ 5% | 869 | 6 | -25% | -80% | -82% | -76% |
| Mean-reversion model ≥ 10% | 559 | 4 | -18% | -77% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3599 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1760 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 548 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5907 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 22 | 0% | -$410.50 | -57% | — |
| Sell at 2¢ | 233 | 4% | -$643.92 | -90% | 43 sec |
| Sell at 3¢ | 145 | 2% | -$647.95 | -90% | 48 sec |
| Sell at 5¢ | 107 | 2% | -$634.95 | -88% | 64 sec |
| Sell at 10¢ | 73 | 1% | -$594.87 | -83% | 81 sec |
| Sell at 25¢ | 38 | 1% | -$550.72 | -77% | 1.6 min |
| Sell at 50¢ | 20 | 0% | -$499.50 | -70% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 1930 | 11 | 8% | 3% | -44% | -86% | -87% |
| 1–2 min | 1533 | 6 | 3% | 2% | -58% | -94% | -93% |
| Under 1 min | 2273 | 3 | 1% | 0% | -81% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 407 | 2 | 4% | 1% | -36% | -89% | -90% |
| ZEC | 402 | 2 | 5% | 3% | -41% | -88% | -90% |
| BNB | 402 | 0 | 4% | 1% | -100% | -91% | -93% |
| ETH | 401 | 2 | 6% | 3% | -38% | -86% | -85% |
| BTC | 400 | 0 | 7% | 3% | -100% | -84% | -88% |
| HYPE | 400 | 2 | 5% | 4% | -38% | -88% | -85% |
| XRP | 397 | 3 | 2% | 1% | -1% | -63% | -63% |
| NEAR | 395 | 1 | 6% | 2% | -66% | -85% | -88% |
| SOL | 395 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 301 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 283 | 0 | 2% | 1% | -100% | -96% | -95% |
| WTI | 265 | 2 | 3% | 1% | -21% | -94% | -96% |
| COPPER | 253 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 223 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 221 | 2 | 4% | 2% | -16% | -94% | -92% |
| PALLADIUM | 214 | 1 | 2% | 1% | -56% | -96% | -98% |
| GBPUSD | 193 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 192 | 1 | 5% | 3% | -51% | -92% | -91% |
| USDJPY | 163 | 3 | 2% | 2% | +72% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3029 | 14 | 4% | 2% | -46% | -91% | -91% |
| DOWN (bought NO) | 2878 | 8 | 4% | 2% | -68% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 431 | 2 | 1% | 1% | -13% | -53% | -52% |
| 0.05–0.1% | 494 | 0 | 3% | 1% | -100% | -90% | -93% |
| 0.1–0.2% | 878 | 1 | 4% | 1% | -85% | -91% | -92% |
| 0.2–0.5% | 1226 | 5 | 6% | 3% | -54% | -87% | -87% |
| Over 0.5% | 569 | 4 | 7% | 3% | -27% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1640 | 9 | 5% | 3% | -38% | -90% | -88% |
| Afternoon (12–6pm) | 1143 | 2 | 3% | 1% | -80% | -83% | -85% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,087 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 1:59:51 PM | COPPER | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:59:35 PM | PALLADIUM | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:59:19 PM | HYPE | UP | 40 sec | -0.071% | 7¢ | ❌ Lost | $0.00 |
| 10/2 1:59:19 PM | SOL | UP | 40 sec | -0.144% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:59:19 PM | DOGE | UP | 40 sec | -0.183% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:59:19 PM | XRP | UP | 40 sec | -0.149% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:59:19 PM | GOLD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:58:47 PM | NATGAS | UP | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:58:31 PM | BNB | DOWN | 88 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:58:31 PM | ETH | DOWN | 88 sec | +0.093% | 2¢ | ❌ Lost | -$0.15 |
| 10/2 1:58:15 PM | PLATINUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:58:15 PM | SILVER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:57:59 PM | BTC | DOWN | 2.0 min | +0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:57:59 PM | NEAR | UP | 2.0 min | -0.515% | 1¢ | ❌ Lost | $0.00 |
| 10/2 1:56:21 PM | ZEC | UP | 3.6 min | -0.740% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:44:33 PM | BTC | DOWN | 27 sec | +0.051% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:44:33 PM | ETH | UP | 27 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:44:17 PM | NEAR | UP | 43 sec | -0.297% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:44:17 PM | SOL | DOWN | 43 sec | +0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:44:17 PM | PALLADIUM | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:44:17 PM | NATGAS | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:43:45 PM | GOLD | UP | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:43:13 PM | XRP | DOWN | 1.8 min | +0.245% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:42:57 PM | SILVER | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:42:39 PM | ZEC | UP | 2.4 min | -0.300% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:42:39 PM | BNB | DOWN | 2.4 min | +0.084% | 7¢ | ❌ Lost | -$0.15 |
| 10/2 1:41:52 PM | HYPE | DOWN | 3.1 min | +0.421% | 4¢ | ❌ Lost | -$0.15 |
| 10/2 1:41:36 PM | WTI | DOWN | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:41:20 PM | DOGE | DOWN | 3.6 min | +0.440% | 1¢ | ❌ Lost | $0.00 |
| 10/2 1:29:56 PM | BTC | DOWN | 3 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
