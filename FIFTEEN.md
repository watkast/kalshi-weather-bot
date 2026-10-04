# 15-Minute 1¢ Study

*Updated Sun Oct 4, 3:32 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 510 finished bets | 1% | $2.30 | +4% | +0.45¢ | -$0.05 / $2.35 |

*Expect about **83 buys a day** (~$12.50/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 179 | $1.60 | +6% |
| Volatility model ≥ 5%, hold to the close | 504 | -$11.55 | -22% |
| Volatility model ≥ 5%, sell at 50¢ | 504 | -$12.05 | -23% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7223 | 7217 | 30 (0%) | 1.07% | -$447.00 (-52%) | Hold to the close: -$447.00 (-52%) |

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
| Volatility model | 4681 | 4.2% | 0.4% (18) | -688% | ❌ Worse |
| Momentum model | 4681 | 4.3% | 0.4% (18) | -725% | ❌ Worse |
| Mean-reversion model | 4681 | 7.0% | 0.4% (18) | -805% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4681 | 18 | -51% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 949 | 6 | -26% | -68% | -69% | -64% |
| Volatility model ≥ 5% | 504 | 3 | -22% | -53% | -53% | -51% |
| Volatility model ≥ 10% | 310 | 3 | +47% | -29% | -32% | -28% |
| Momentum model ≥ 2% | 831 | 5 | -27% | -68% | -71% | -68% |
| Momentum model ≥ 5% | 510 | 4 | +4% | -58% | -62% | -58% |
| Momentum model ≥ 10% | 347 | 3 | +26% | -43% | -45% | -42% |
| Mean-reversion model ≥ 2% | 1673 | 9 | -41% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1131 | 8 | -21% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 743 | 6 | -6% | -78% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4878 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7217 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 30 | 0% | -$447.00 | -52% | — |
| Sell at 2¢ | 279 | 4% | -$766.46 | -88% | 34 sec |
| Sell at 3¢ | 177 | 2% | -$769.97 | -89% | 48 sec |
| Sell at 5¢ | 132 | 2% | -$753.20 | -87% | 62 sec |
| Sell at 10¢ | 88 | 1% | -$709.72 | -82% | 80 sec |
| Sell at 25¢ | 49 | 1% | -$648.81 | -75% | 1.6 min |
| Sell at 50¢ | 29 | 0% | -$573.25 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 176 | 2 | 11% | 3% | +8% | -80% | -89% |
| 2–5 min | 2342 | 15 | 8% | 4% | -38% | -86% | -87% |
| 1–2 min | 1879 | 8 | 3% | 2% | -54% | -94% | -93% |
| Under 1 min | 2817 | 5 | 1% | 0% | -73% | -87% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 549 | 4 | 5% | 3% | -14% | -89% | -89% |
| DOGE | 548 | 2 | 4% | 1% | -53% | -91% | -91% |
| HYPE | 547 | 2 | 5% | 3% | -56% | -89% | -86% |
| ETH | 544 | 4 | 6% | 3% | -7% | -87% | -86% |
| SOL | 540 | 0 | 3% | 1% | -100% | -93% | -92% |
| BNB | 540 | 1 | 4% | 2% | -78% | -91% | -93% |
| BTC | 538 | 1 | 5% | 2% | -76% | -87% | -90% |
| XRP | 538 | 4 | 2% | 1% | -4% | -72% | -72% |
| NEAR | 534 | 2 | 6% | 2% | -50% | -60% | -63% |
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
| UP (bought YES) | 3639 | 17 | 4% | 2% | -45% | -88% | -88% |
| DOWN (bought NO) | 3578 | 13 | 4% | 2% | -58% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 793 | 5 | 2% | 1% | +8% | -52% | -52% |
| 0.05–0.1% | 809 | 0 | 3% | 1% | -100% | -93% | -94% |
| 0.1–0.2% | 1196 | 4 | 4% | 2% | -57% | -90% | -91% |
| 0.2–0.5% | 1451 | 7 | 6% | 3% | -47% | -88% | -87% |
| Over 0.5% | 627 | 4 | 7% | 3% | -34% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1797 | 8 | 4% | 2% | -48% | -84% | -86% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,902 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 3:29:09 AM | NEAR | DOWN | 51 sec | +0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:28:04 AM | ZEC | DOWN | 1.9 min | +0.274% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 3:27:14 AM | HYPE | DOWN | 2.8 min | +0.169% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 3:27:00 AM | BTC | DOWN | 3.0 min | +0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:27:00 AM | XRP | DOWN | 3.0 min | +0.328% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:26:21 AM | BNB | DOWN | 3.6 min | +0.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:25:50 AM | DOGE | DOWN | 4.2 min | +0.241% | 3¢ | ❌ Lost | -$0.15 |
| 10/4 3:25:17 AM | SOL | DOWN | 4.7 min | +0.232% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:25:17 AM | ETH | DOWN | 4.7 min | +0.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:14:19 AM | SOL | UP | 40 sec | -0.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:14:19 AM | ZEC | UP | 40 sec | -0.122% | 0¢ | ❌ Lost | $0.00 |
| 10/4 3:14:19 AM | XRP | DOWN | 40 sec | +0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 3:14:03 AM | BTC | DOWN | 57 sec | +0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:13:47 AM | NEAR | UP | 73 sec | -0.273% | 0¢ | ❌ Lost | $0.00 |
| 10/4 3:13:31 AM | ETH | UP | 89 sec | -0.030% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:12:59 AM | DOGE | DOWN | 2.0 min | +0.156% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:11:53 AM | HYPE | UP | 3.1 min | -0.199% | 2¢ | ❌ Lost | -$0.15 |
| 10/4 3:11:53 AM | BNB | DOWN | 3.1 min | +0.292% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:59:47 AM | DOGE | DOWN | 13 sec | -0.007% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:59:15 AM | NEAR | DOWN | 45 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:59:15 AM | SOL | DOWN | 45 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:59:15 AM | BTC | DOWN | 45 sec | +0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:59:00 AM | ETH | DOWN | 59 sec | +0.041% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:58:12 AM | XRP | UP | 1.8 min | -0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:57:08 AM | HYPE | UP | 2.9 min | -0.248% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:57:08 AM | BNB | DOWN | 2.9 min | +0.091% | 2¢ | ❌ Lost | -$0.15 |
| 10/4 2:56:36 AM | ZEC | UP | 3.4 min | -0.438% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:44:50 AM | BNB | UP | 9 sec | -0.077% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:44:34 AM | XRP | UP | 25 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:43:32 AM | ETH | UP | 87 sec | -0.087% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
