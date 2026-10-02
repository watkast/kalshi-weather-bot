# 15-Minute 1¢ Study

*Updated Fri Oct 2, 4:14 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 335 finished bets | 1% | $5.85 | +16% | +1.75¢ | -$4.75 / $10.60 |

*Expect about **81 buys a day** (~$12.12/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 163 | $4.00 | +17% |
| Momentum model ≥ 5%, sell at 50¢ | 335 | -$1.40 | -4% |
| Volatility model ≥ 5%, hold to the close | 328 | -$7.70 | -22% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5409 | 5386 | 18 (0%) | 1.07% | -$403.95 (-62%) | Hold to the close: -$403.95 (-62%) |

*In play or awaiting result: 23. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 3111 | 3.6% | 0.3% (8) | -639% | ❌ Worse |
| Momentum model | 3111 | 3.8% | 0.3% (8) | -688% | ❌ Worse |
| Mean-reversion model | 3111 | 6.7% | 0.3% (8) | -815% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3111 | 8 | -67% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 665 | 4 | -31% | -66% | -68% | -65% |
| Volatility model ≥ 5% | 328 | 2 | -22% | -41% | -42% | -39% |
| Volatility model ≥ 10% | 184 | 2 | +62% | -1% | -3% | +4% |
| Momentum model ≥ 2% | 579 | 3 | -38% | -64% | -68% | -65% |
| Momentum model ≥ 5% | 335 | 3 | +16% | -45% | -49% | -45% |
| Momentum model ≥ 10% | 222 | 2 | +30% | -23% | -24% | -20% |
| Mean-reversion model ≥ 2% | 1199 | 5 | -55% | -86% | -88% | -85% |
| Mean-reversion model ≥ 5% | 790 | 5 | -31% | -82% | -85% | -80% |
| Mean-reversion model ≥ 10% | 503 | 4 | -10% | -78% | -82% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3307 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1589 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 490 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5386 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 18 | 0% | -$403.95 | -62% | — |
| Sell at 2¢ | 196 | 4% | -$590.99 | -90% | 46 sec |
| Sell at 3¢ | 115 | 2% | -$597.10 | -91% | 49 sec |
| Sell at 5¢ | 83 | 2% | -$588.00 | -90% | 66 sec |
| Sell at 10¢ | 60 | 1% | -$549.35 | -84% | 81 sec |
| Sell at 25¢ | 30 | 1% | -$514.65 | -78% | 1.6 min |
| Sell at 50¢ | 15 | 0% | -$470.70 | -72% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 160 | 2 | 12% | 2% | +19% | -79% | -90% |
| 2–5 min | 1757 | 8 | 7% | 3% | -56% | -88% | -90% |
| 1–2 min | 1414 | 5 | 3% | 2% | -62% | -94% | -93% |
| Under 1 min | 2052 | 3 | 1% | 0% | -79% | -91% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 374 | 1 | 4% | 1% | -66% | -91% | -92% |
| BNB | 370 | 0 | 4% | 1% | -100% | -92% | -95% |
| ETH | 369 | 2 | 5% | 3% | -33% | -87% | -86% |
| ZEC | 369 | 1 | 5% | 2% | -68% | -90% | -94% |
| BTC | 368 | 0 | 7% | 2% | -100% | -84% | -89% |
| HYPE | 366 | 2 | 4% | 3% | -32% | -90% | -88% |
| XRP | 365 | 3 | 1% | 1% | +5% | -62% | -61% |
| NEAR | 364 | 1 | 6% | 2% | -63% | -85% | -90% |
| SOL | 362 | 0 | 3% | 1% | -100% | -93% | -93% |
| GOLD | 275 | 0 | 5% | 1% | -100% | -89% | -93% |
| SILVER | 255 | 0 | 2% | 1% | -100% | -97% | -96% |
| WTI | 241 | 1 | 3% | 1% | -56% | -94% | -96% |
| COPPER | 229 | 0 | 1% | 0% | -100% | -98% | -99% |
| PLATINUM | 200 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 198 | 1 | 4% | 2% | -53% | -94% | -92% |
| PALLADIUM | 191 | 1 | 3% | 1% | -51% | -95% | -97% |
| GBPUSD | 174 | 1 | 4% | 2% | -46% | -93% | -94% |
| EURUSD | 171 | 1 | 4% | 2% | -45% | -93% | -92% |
| USDJPY | 145 | 3 | 3% | 2% | +93% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2733 | 11 | 4% | 2% | -54% | -92% | -93% |
| DOWN (bought NO) | 2653 | 7 | 4% | 1% | -70% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 396 | 2 | 1% | 1% | -5% | -48% | -47% |
| 0.05–0.1% | 464 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 805 | 1 | 3% | 1% | -84% | -92% | -93% |
| 0.2–0.5% | 1121 | 3 | 6% | 3% | -70% | -89% | -89% |
| Over 0.5% | 520 | 4 | 7% | 2% | -21% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1354 | 3 | 4% | 1% | -75% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,166 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 4:14:10 AM | GBPUSD | UP | 50 sec | — | — | In play | — |
| 10/2 4:14:10 AM | WTI | DOWN | 50 sec | — | — | In play | — |
| 10/2 4:13:53 AM | SOL | UP | 66 sec | -0.132% | — | In play | — |
| 10/2 4:13:53 AM | ETH | UP | 66 sec | -0.087% | — | In play | — |
| 10/2 4:13:53 AM | XRP | UP | 66 sec | -0.175% | — | In play | — |
| 10/2 4:13:37 AM | BNB | UP | 82 sec | -0.113% | — | In play | — |
| 10/2 4:13:37 AM | NEAR | DOWN | 82 sec | +0.314% | — | In play | — |
| 10/2 4:13:37 AM | DOGE | UP | 82 sec | -0.160% | — | In play | — |
| 10/2 4:13:21 AM | NATGAS | DOWN | 1.6 min | — | — | In play | — |
| 10/2 4:13:21 AM | PALLADIUM | UP | 1.6 min | — | — | In play | — |
| 10/2 4:12:48 AM | COPPER | UP | 2.2 min | — | — | In play | — |
| 10/2 4:12:32 AM | HYPE | DOWN | 2.5 min | +0.284% | — | In play | — |
| 10/2 4:12:32 AM | EURUSD | UP | 2.5 min | — | — | In play | — |
| 10/2 4:12:00 AM | USDJPY | DOWN | 3.0 min | — | — | In play | — |
| 10/2 4:12:00 AM | GOLD | UP | 3.0 min | — | — | In play | — |
| 10/2 4:10:55 AM | SILVER | UP | 4.1 min | — | — | In play | — |
| 10/2 4:10:39 AM | PLATINUM | UP | 4.3 min | — | — | In play | — |
| 10/2 3:59:53 AM | SOL | UP | 6 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/2 3:59:53 AM | PALLADIUM | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:59:53 AM | BTC | DOWN | 6 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 10/2 3:59:53 AM | ETH | UP | 6 sec | -0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/2 3:59:05 AM | USDJPY | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:58:49 AM | NATGAS | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:58:01 AM | HYPE | DOWN | 2.0 min | +0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:58:01 AM | NEAR | DOWN | 2.0 min | +0.347% | 6¢ | ❌ Lost | -$0.15 |
| 10/2 3:58:01 AM | DOGE | DOWN | 2.0 min | +0.213% | 0¢ | ❌ Lost | $0.00 |
| 10/2 3:57:30 AM | GBPUSD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:56:42 AM | ZEC | DOWN | 3.3 min | +0.373% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 3:56:26 AM | XRP | DOWN | 3.6 min | +0.293% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 3:56:10 AM | BNB | DOWN | 3.8 min | +0.133% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
