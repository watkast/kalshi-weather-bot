# 15-Minute 1¢ Study

*Updated Fri Oct 2, 10:07 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 171 finished bets | 1% | $2.80 | +11% | +1.64¢ | $15.40 / -$12.60 |

*Expect about **34 buys a day** (~$5.07/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 399 | -$0.00 | -0% |
| Momentum model ≥ 5%, sell at 50¢ | 399 | -$7.25 | -17% |
| 5+ min left, sell at 50¢ | 171 | -$11.70 | -46% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6216 | 6210 | 23 (0%) | 1.07% | -$429.65 (-57%) | Hold to the close: -$429.65 (-57%) |

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
| Volatility model | 3674 | 3.9% | 0.3% (11) | -697% | ❌ Worse |
| Momentum model | 3674 | 4.0% | 0.3% (11) | -740% | ❌ Worse |
| Mean-reversion model | 3674 | 7.0% | 0.3% (11) | -853% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3674 | 11 | -62% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 779 | 5 | -26% | -66% | -66% | -61% |
| Volatility model ≥ 5% | 398 | 2 | -34% | -45% | -46% | -41% |
| Volatility model ≥ 10% | 234 | 2 | +31% | -12% | -14% | -7% |
| Momentum model ≥ 2% | 686 | 4 | -29% | -65% | -68% | -64% |
| Momentum model ≥ 5% | 399 | 3 | -0% | -51% | -54% | -48% |
| Momentum model ≥ 10% | 270 | 2 | +9% | -32% | -33% | -28% |
| Mean-reversion model ≥ 2% | 1387 | 7 | -45% | -84% | -86% | -81% |
| Mean-reversion model ≥ 5% | 929 | 6 | -29% | -80% | -82% | -75% |
| Mean-reversion model ≥ 10% | 602 | 4 | -23% | -77% | -81% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3871 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6210 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 23 | 0% | -$429.65 | -57% | — |
| Sell at 2¢ | 244 | 4% | -$674.21 | -90% | 43 sec |
| Sell at 3¢ | 152 | 2% | -$678.37 | -90% | 48 sec |
| Sell at 5¢ | 113 | 2% | -$664.20 | -88% | 64 sec |
| Sell at 10¢ | 74 | 1% | -$626.71 | -83% | 81 sec |
| Sell at 25¢ | 39 | 1% | -$580.56 | -77% | 1.6 min |
| Sell at 50¢ | 21 | 0% | -$525.90 | -70% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 2025 | 12 | 8% | 3% | -42% | -86% | -87% |
| 1–2 min | 1612 | 6 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 2402 | 3 | 1% | 0% | -82% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 437 | 2 | 4% | 1% | -39% | -90% | -91% |
| ZEC | 434 | 2 | 5% | 3% | -45% | -88% | -90% |
| HYPE | 432 | 2 | 5% | 4% | -43% | -88% | -85% |
| ETH | 431 | 2 | 6% | 3% | -43% | -86% | -86% |
| BNB | 431 | 0 | 4% | 1% | -100% | -91% | -93% |
| BTC | 429 | 1 | 7% | 3% | -70% | -84% | -88% |
| XRP | 427 | 3 | 2% | 1% | -8% | -65% | -66% |
| SOL | 426 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 424 | 1 | 6% | 2% | -68% | -86% | -88% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 274 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 225 | 2 | 4% | 2% | -17% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3158 | 14 | 4% | 2% | -48% | -91% | -91% |
| DOWN (bought NO) | 3052 | 9 | 4% | 2% | -66% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 491 | 2 | 1% | 1% | -23% | -58% | -57% |
| 0.05–0.1% | 563 | 0 | 3% | 1% | -100% | -91% | -94% |
| 0.1–0.2% | 948 | 2 | 4% | 1% | -72% | -90% | -91% |
| 0.2–0.5% | 1280 | 5 | 6% | 3% | -56% | -88% | -87% |
| Over 0.5% | 587 | 4 | 7% | 3% | -29% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1640 | 9 | 5% | 3% | -38% | -90% | -88% |
| Afternoon (12–6pm) | 1305 | 3 | 4% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1791 | 6 | 3% | 2% | -61% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,194 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 9:59:47 PM | ZEC | UP | 13 sec | +0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:59:47 PM | NATGAS | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:59:00 PM | BNB | DOWN | 59 sec | -0.004% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:58:44 PM | SOL | DOWN | 75 sec | +0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:58:28 PM | ETH | DOWN | 1.5 min | +0.026% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:58:12 PM | BTC | DOWN | 1.8 min | +0.053% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:57:56 PM | HYPE | DOWN | 2.1 min | +0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:57:39 PM | NEAR | DOWN | 2.3 min | +0.160% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:57:23 PM | DOGE | DOWN | 2.6 min | +0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:56:03 PM | XRP | DOWN | 3.9 min | +0.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:44:34 PM | BNB | UP | 25 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:44:34 PM | ZEC | UP | 25 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:44:34 PM | NEAR | DOWN | 25 sec | -0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:44:18 PM | HYPE | UP | 41 sec | -0.092% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:44:02 PM | NATGAS | UP | 58 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:44:02 PM | XRP | DOWN | 58 sec | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:43:11 PM | SOL | DOWN | 1.8 min | +0.130% | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:43:11 PM | DOGE | DOWN | 1.8 min | +0.096% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:43:11 PM | BTC | DOWN | 1.8 min | +0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:29:50 PM | XRP | DOWN | 9 sec | +0.000% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:29:34 PM | ZEC | DOWN | 25 sec | +0.068% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:29:18 PM | HYPE | UP | 41 sec | -0.137% | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:29:02 PM | NEAR | UP | 57 sec | -0.368% | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:27:08 PM | BTC | DOWN | 2.9 min | +0.079% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:26:36 PM | SOL | DOWN | 3.4 min | +0.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:26:36 PM | DOGE | DOWN | 3.4 min | +0.248% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:26:04 PM | ETH | DOWN | 3.9 min | +0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:25:14 PM | BNB | DOWN | 4.8 min | +0.072% | 2¢ | ❌ Lost | -$0.15 |
| 10/2 9:14:46 PM | ETH | UP | 14 sec | -0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:14:46 PM | WTI | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
