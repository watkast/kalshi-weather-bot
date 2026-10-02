# 15-Minute 1¢ Study

*Updated Fri Oct 2, 5:55 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 343 finished bets | 1% | $5.10 | +14% | +1.49¢ | -$5.20 / $10.30 |

*Expect about **81 buys a day** (~$12.20/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 165 | $3.70 | +15% |
| Momentum model ≥ 5%, sell at 50¢ | 343 | -$2.15 | -6% |
| Volatility model ≥ 5%, hold to the close | 336 | -$8.60 | -23% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5495 | 5489 | 20 (0%) | 1.07% | -$387.65 (-58%) | Hold to the close: -$387.65 (-58%) |

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
| Volatility model | 3174 | 3.6% | 0.3% (9) | -607% | ❌ Worse |
| Momentum model | 3174 | 3.7% | 0.3% (9) | -655% | ❌ Worse |
| Mean-reversion model | 3174 | 6.7% | 0.3% (9) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3174 | 9 | -64% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 676 | 4 | -32% | -66% | -69% | -66% |
| Volatility model ≥ 5% | 336 | 2 | -23% | -41% | -44% | -40% |
| Volatility model ≥ 10% | 189 | 2 | +58% | -0% | -5% | +1% |
| Momentum model ≥ 2% | 592 | 3 | -39% | -64% | -68% | -66% |
| Momentum model ≥ 5% | 343 | 3 | +14% | -46% | -50% | -46% |
| Momentum model ≥ 10% | 228 | 2 | +27% | -24% | -26% | -22% |
| Mean-reversion model ≥ 2% | 1219 | 6 | -47% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 806 | 6 | -19% | -82% | -85% | -79% |
| Mean-reversion model ≥ 10% | 516 | 4 | -12% | -78% | -82% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3370 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1618 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 501 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5489 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 20 | 0% | -$387.65 | -58% | — |
| Sell at 2¢ | 201 | 4% | -$601.39 | -90% | 43 sec |
| Sell at 3¢ | 118 | 2% | -$607.63 | -91% | 49 sec |
| Sell at 5¢ | 86 | 2% | -$597.75 | -90% | 66 sec |
| Sell at 10¢ | 63 | 1% | -$557.12 | -83% | 81 sec |
| Sell at 25¢ | 33 | 1% | -$516.42 | -77% | 1.6 min |
| Sell at 50¢ | 18 | 0% | -$462.15 | -69% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 162 | 2 | 12% | 2% | +17% | -79% | -90% |
| 2–5 min | 1787 | 9 | 7% | 3% | -51% | -88% | -90% |
| 1–2 min | 1441 | 6 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 2096 | 3 | 1% | 0% | -79% | -91% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 382 | 2 | 4% | 1% | -32% | -91% | -92% |
| BNB | 377 | 0 | 4% | 1% | -100% | -92% | -95% |
| ETH | 376 | 2 | 6% | 3% | -34% | -87% | -86% |
| ZEC | 376 | 1 | 5% | 2% | -68% | -90% | -94% |
| BTC | 375 | 0 | 6% | 2% | -100% | -85% | -89% |
| HYPE | 373 | 2 | 4% | 3% | -34% | -90% | -88% |
| XRP | 372 | 3 | 1% | 1% | +4% | -62% | -61% |
| NEAR | 370 | 1 | 6% | 2% | -64% | -86% | -90% |
| SOL | 369 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 280 | 0 | 5% | 1% | -100% | -90% | -93% |
| SILVER | 259 | 0 | 2% | 1% | -100% | -97% | -96% |
| WTI | 244 | 1 | 3% | 1% | -57% | -94% | -96% |
| COPPER | 234 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 203 | 2 | 4% | 2% | -8% | -93% | -91% |
| PLATINUM | 202 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 196 | 1 | 3% | 1% | -52% | -96% | -97% |
| GBPUSD | 176 | 1 | 4% | 2% | -47% | -93% | -94% |
| EURUSD | 176 | 1 | 4% | 2% | -47% | -93% | -93% |
| USDJPY | 149 | 3 | 3% | 2% | +88% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2783 | 13 | 4% | 2% | -46% | -92% | -92% |
| DOWN (bought NO) | 2706 | 7 | 4% | 1% | -70% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 407 | 2 | 1% | 1% | -7% | -49% | -48% |
| 0.05–0.1% | 473 | 0 | 3% | 0% | -100% | -91% | -95% |
| 0.1–0.2% | 823 | 1 | 3% | 1% | -84% | -92% | -93% |
| 0.2–0.5% | 1141 | 4 | 6% | 3% | -61% | -89% | -89% |
| Over 0.5% | 525 | 4 | 7% | 2% | -21% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1457 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,134 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 5:44:43 AM | GBPUSD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 5:44:43 AM | COPPER | UP | 17 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:44:43 AM | SOL | UP | 17 sec | -0.067% | 52¢ | ❌ Lost | $0.00 |
| 10/2 5:44:43 AM | EURUSD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 5:44:27 AM | XRP | UP | 33 sec | -0.176% | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:44:27 AM | ZEC | UP | 33 sec | -0.262% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:44:27 AM | DOGE | UP | 33 sec | -0.165% | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:44:27 AM | PALLADIUM | UP | 33 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:44:12 AM | NATGAS | DOWN | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:44:12 AM | USDJPY | UP | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:43:56 AM | BTC | DOWN | 64 sec | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:42:35 AM | ETH | DOWN | 2.4 min | +0.065% | 3¢ | ❌ Lost | -$0.15 |
| 10/2 5:42:03 AM | BNB | DOWN | 2.9 min | +0.053% | 3¢ | ❌ Lost | -$0.15 |
| 10/2 5:40:58 AM | HYPE | DOWN | 4.0 min | +0.234% | 2¢ | ❌ Lost | -$0.15 |
| 10/2 5:29:52 AM | DOGE | DOWN | 7 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:29:52 AM | BTC | UP | 7 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:29:52 AM | USDJPY | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 5:29:36 AM | SILVER | UP | 23 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:29:06 AM | NEAR | UP | 53 sec | -0.207% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:28:50 AM | EURUSD | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 5:28:34 AM | SOL | UP | 85 sec | -0.158% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 5:28:34 AM | GOLD | UP | 85 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:28:18 AM | ETH | UP | 1.7 min | -0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:28:18 AM | ZEC | UP | 1.7 min | -0.337% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:28:02 AM | BNB | DOWN | 2.0 min | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:27:15 AM | HYPE | UP | 2.7 min | -0.369% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:27:15 AM | XRP | UP | 2.7 min | -0.299% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 5:14:42 AM | USDJPY | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 5:14:42 AM | GOLD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 5:14:10 AM | NEAR | UP | 50 sec | -0.168% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
