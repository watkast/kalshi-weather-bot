# 15-Minute 1¢ Study

*Updated Sat Oct 3, 9:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 483 finished bets | 1% | $5.60 | +11% | +1.16¢ | $1.60 / $4.00 |

*Expect about **82 buys a day** (~$12.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 178 | $1.75 | +7% |
| Volatility model ≥ 5%, hold to the close | 480 | -$8.70 | -17% |
| Momentum model ≥ 5%, sell at 50¢ | 483 | -$8.90 | -18% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7006 | 7000 | 29 (0%) | 1.07% | -$434.90 (-52%) | Hold to the close: -$434.90 (-52%) |

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
| Volatility model | 4464 | 4.2% | 0.4% (17) | -688% | ❌ Worse |
| Momentum model | 4464 | 4.2% | 0.4% (17) | -722% | ❌ Worse |
| Mean-reversion model | 4464 | 7.0% | 0.4% (17) | -813% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4464 | 17 | -51% | -84% | -84% | -81% |
| Volatility model ≥ 2% | 913 | 6 | -23% | -68% | -68% | -63% |
| Volatility model ≥ 5% | 480 | 3 | -17% | -51% | -52% | -48% |
| Volatility model ≥ 10% | 292 | 3 | +57% | -25% | -29% | -23% |
| Momentum model ≥ 2% | 797 | 5 | -23% | -67% | -70% | -67% |
| Momentum model ≥ 5% | 483 | 4 | +11% | -56% | -60% | -55% |
| Momentum model ≥ 10% | 330 | 3 | +34% | -40% | -43% | -39% |
| Mean-reversion model ≥ 2% | 1614 | 8 | -46% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1089 | 7 | -29% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 716 | 5 | -19% | -78% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4661 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7000 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 29 | 0% | -$434.90 | -52% | — |
| Sell at 2¢ | 273 | 4% | -$741.92 | -88% | 34 sec |
| Sell at 3¢ | 173 | 2% | -$745.43 | -89% | 48 sec |
| Sell at 5¢ | 130 | 2% | -$728.40 | -87% | 61 sec |
| Sell at 10¢ | 87 | 1% | -$684.93 | -81% | 78 sec |
| Sell at 25¢ | 48 | 1% | -$626.02 | -74% | 1.6 min |
| Sell at 50¢ | 28 | 0% | -$553.90 | -66% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 175 | 2 | 11% | 3% | +9% | -80% | -89% |
| 2–5 min | 2269 | 14 | 8% | 4% | -40% | -86% | -87% |
| 1–2 min | 1822 | 8 | 3% | 2% | -52% | -94% | -93% |
| Under 1 min | 2731 | 5 | 1% | 0% | -73% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 525 | 2 | 4% | 1% | -51% | -91% | -92% |
| ZEC | 523 | 3 | 5% | 3% | -32% | -89% | -90% |
| HYPE | 523 | 2 | 5% | 3% | -54% | -89% | -86% |
| ETH | 520 | 4 | 6% | 3% | -2% | -86% | -86% |
| BNB | 518 | 1 | 4% | 2% | -77% | -91% | -92% |
| SOL | 515 | 0 | 3% | 1% | -100% | -93% | -93% |
| BTC | 513 | 1 | 6% | 2% | -74% | -86% | -89% |
| XRP | 513 | 4 | 2% | 1% | +1% | -71% | -71% |
| NEAR | 511 | 2 | 6% | 2% | -47% | -58% | -61% |
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
| UP (bought YES) | 3539 | 17 | 4% | 2% | -44% | -88% | -88% |
| DOWN (bought NO) | 3461 | 12 | 4% | 2% | -60% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 730 | 5 | 2% | 1% | +20% | -47% | -47% |
| 0.05–0.1% | 753 | 0 | 3% | 1% | -100% | -92% | -94% |
| 0.1–0.2% | 1141 | 4 | 4% | 2% | -54% | -90% | -90% |
| 0.2–0.5% | 1416 | 6 | 6% | 3% | -53% | -88% | -88% |
| Over 0.5% | 619 | 4 | 7% | 3% | -33% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 1965 | 6 | 3% | 2% | -64% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,764 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 9:14:49 PM | BTC | DOWN | 11 sec | +0.004% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:14:49 PM | XRP | DOWN | 11 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/3 9:14:49 PM | ZEC | UP | 11 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/3 9:14:49 PM | ETH | DOWN | 11 sec | +0.004% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:14:18 PM | BNB | UP | 42 sec | -0.017% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 9:14:18 PM | SOL | UP | 42 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 10/3 9:14:18 PM | HYPE | DOWN | 42 sec | +0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 9:12:43 PM | DOGE | UP | 2.3 min | -0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:12:12 PM | NEAR | UP | 2.8 min | -0.517% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:59:48 PM | NEAR | DOWN | 11 sec | -0.064% | 0¢ | ❌ Lost | $0.00 |
| 10/3 8:59:48 PM | XRP | UP | 11 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/3 8:59:48 PM | HYPE | DOWN | 11 sec | -0.009% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 8:58:45 PM | ZEC | DOWN | 75 sec | +0.131% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:57:42 PM | SOL | DOWN | 2.3 min | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:57:42 PM | DOGE | UP | 2.3 min | -0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:56:39 PM | BNB | UP | 3.4 min | -0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:44:48 PM | HYPE | DOWN | 11 sec | +0.001% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 8:44:32 PM | SOL | DOWN | 28 sec | +0.024% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 8:44:16 PM | XRP | DOWN | 44 sec | +0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:44:16 PM | NEAR | UP | 44 sec | -0.362% | 0¢ | ❌ Lost | $0.00 |
| 10/3 8:44:00 PM | ETH | UP | 60 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/3 8:43:45 PM | DOGE | DOWN | 74 sec | +0.072% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:43:45 PM | BTC | UP | 74 sec | -0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:42:42 PM | ZEC | DOWN | 2.3 min | +0.194% | 5¢ | ❌ Lost | -$0.15 |
| 10/3 8:41:39 PM | BNB | DOWN | 3.4 min | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 8:29:50 PM | DOGE | DOWN | 9 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/3 8:29:50 PM | HYPE | DOWN | 9 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/3 8:29:50 PM | BTC | DOWN | 9 sec | +0.010% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 8:29:19 PM | BNB | UP | 40 sec | -0.079% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 8:29:19 PM | SOL | UP | 40 sec | -0.063% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
