# 15-Minute 1¢ Study

*Updated Sun Oct 4, 3:59 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 511 finished bets | 1% | $2.15 | +4% | +0.42¢ | -$0.05 / $2.20 |

*Expect about **83 buys a day** (~$12.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 181 | $1.30 | +5% |
| Volatility model ≥ 5%, hold to the close | 504 | -$11.55 | -22% |
| Volatility model ≥ 5%, sell at 50¢ | 504 | -$12.05 | -23% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7241 | 7226 | 30 (0%) | 1.07% | -$448.20 (-52%) | Hold to the close: -$448.20 (-52%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 4690 | 4.2% | 0.4% (18) | -687% | ❌ Worse |
| Momentum model | 4690 | 4.3% | 0.4% (18) | -724% | ❌ Worse |
| Mean-reversion model | 4690 | 7.0% | 0.4% (18) | -805% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4690 | 18 | -51% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 949 | 6 | -26% | -68% | -69% | -64% |
| Volatility model ≥ 5% | 504 | 3 | -22% | -53% | -53% | -51% |
| Volatility model ≥ 10% | 310 | 3 | +47% | -29% | -32% | -28% |
| Momentum model ≥ 2% | 832 | 5 | -27% | -68% | -71% | -68% |
| Momentum model ≥ 5% | 511 | 4 | +4% | -58% | -62% | -58% |
| Momentum model ≥ 10% | 347 | 3 | +26% | -43% | -45% | -42% |
| Mean-reversion model ≥ 2% | 1675 | 9 | -42% | -83% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1133 | 8 | -22% | -79% | -80% | -74% |
| Mean-reversion model ≥ 10% | 744 | 6 | -6% | -78% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4887 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7226 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 30 | 0% | -$448.20 | -52% | — |
| Sell at 2¢ | 281 | 4% | -$767.14 | -88% | 34 sec |
| Sell at 3¢ | 179 | 2% | -$770.39 | -89% | 48 sec |
| Sell at 5¢ | 133 | 2% | -$753.75 | -87% | 63 sec |
| Sell at 10¢ | 88 | 1% | -$710.92 | -82% | 80 sec |
| Sell at 25¢ | 49 | 1% | -$650.01 | -75% | 1.6 min |
| Sell at 50¢ | 29 | 0% | -$574.45 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 178 | 2 | 12% | 3% | +7% | -79% | -88% |
| 2–5 min | 2343 | 15 | 8% | 4% | -38% | -86% | -87% |
| 1–2 min | 1879 | 8 | 3% | 2% | -54% | -94% | -93% |
| Under 1 min | 2823 | 5 | 1% | 0% | -73% | -87% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 550 | 4 | 5% | 3% | -14% | -88% | -89% |
| DOGE | 549 | 2 | 4% | 1% | -53% | -91% | -91% |
| HYPE | 548 | 2 | 5% | 3% | -56% | -89% | -86% |
| ETH | 545 | 4 | 6% | 3% | -7% | -87% | -86% |
| SOL | 541 | 0 | 3% | 1% | -100% | -93% | -92% |
| BNB | 541 | 1 | 4% | 2% | -78% | -91% | -93% |
| BTC | 539 | 1 | 5% | 2% | -76% | -87% | -90% |
| XRP | 539 | 4 | 2% | 1% | -4% | -72% | -72% |
| NEAR | 535 | 2 | 6% | 2% | -50% | -60% | -62% |
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
| UP (bought YES) | 3644 | 17 | 4% | 2% | -45% | -88% | -88% |
| DOWN (bought NO) | 3582 | 13 | 4% | 2% | -58% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 798 | 5 | 2% | 1% | +6% | -52% | -52% |
| 0.05–0.1% | 809 | 0 | 3% | 1% | -100% | -93% | -94% |
| 0.1–0.2% | 1197 | 4 | 4% | 2% | -57% | -90% | -91% |
| 0.2–0.5% | 1453 | 7 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 628 | 4 | 7% | 3% | -35% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1806 | 8 | 4% | 2% | -48% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,908 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 3:59:08 AM | BTC | UP | 52 sec | -0.056% | — | In play | — |
| 10/4 3:59:08 AM | ETH | UP | 52 sec | -0.044% | — | In play | — |
| 10/4 3:58:52 AM | SOL | DOWN | 68 sec | +0.098% | — | In play | — |
| 10/4 3:58:35 AM | DOGE | UP | 84 sec | -0.057% | — | In play | — |
| 10/4 3:58:18 AM | XRP | UP | 1.7 min | -0.087% | — | In play | — |
| 10/4 3:56:55 AM | NEAR | DOWN | 3.1 min | +0.869% | — | In play | — |
| 10/4 3:56:39 AM | BNB | UP | 3.4 min | -0.239% | — | In play | — |
| 10/4 3:55:35 AM | HYPE | DOWN | 4.4 min | +0.455% | — | In play | — |
| 10/4 3:55:19 AM | ZEC | DOWN | 4.7 min | +0.726% | — | In play | — |
| 10/4 3:44:53 AM | BTC | DOWN | 6 sec | +0.008% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 3:44:37 AM | SOL | DOWN | 22 sec | +0.013% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:44:37 AM | DOGE | DOWN | 22 sec | +0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 3:44:37 AM | ETH | DOWN | 22 sec | +0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:44:21 AM | BNB | UP | 38 sec | -0.126% | 0¢ | ❌ Lost | $0.00 |
| 10/4 3:44:21 AM | XRP | UP | 38 sec | -0.033% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 3:40:51 AM | NEAR | UP | 4.1 min | -0.426% | 8¢ | ❌ Lost | -$0.15 |
| 10/4 3:39:30 AM | HYPE | UP | 5.5 min | -0.302% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:39:14 AM | ZEC | UP | 5.8 min | -0.571% | 3¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
