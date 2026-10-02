# 15-Minute 1¢ Study

*Updated Fri Oct 2, 12:14 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 315 finished bets | 1% | $7.50 | +22% | +2.38¢ | -$3.55 / $11.05 |

*Expect about **79 buys a day** (~$11.91/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 160 | $4.45 | +19% |
| Momentum model ≥ 5%, sell at 50¢ | 315 | $0.25 | +1% |
| Volatility model ≥ 5%, hold to the close | 308 | -$5.90 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5168 | 5148 | 17 (0%) | 1.07% | -$391.40 (-62%) | Hold to the close: -$391.40 (-62%) |

*In play or awaiting result: 20. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 2971 | 3.5% | 0.3% (8) | -592% | ❌ Worse |
| Momentum model | 2971 | 3.7% | 0.3% (8) | -642% | ❌ Worse |
| Mean-reversion model | 2971 | 6.7% | 0.3% (8) | -766% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2971 | 8 | -66% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 627 | 4 | -27% | -66% | -68% | -64% |
| Volatility model ≥ 5% | 308 | 2 | -17% | -38% | -39% | -36% |
| Volatility model ≥ 10% | 173 | 2 | +70% | +4% | +1% | +8% |
| Momentum model ≥ 2% | 549 | 3 | -35% | -63% | -66% | -63% |
| Momentum model ≥ 5% | 315 | 3 | +22% | -44% | -47% | -42% |
| Momentum model ≥ 10% | 207 | 2 | +38% | -21% | -19% | -15% |
| Mean-reversion model ≥ 2% | 1141 | 5 | -53% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 756 | 5 | -28% | -82% | -85% | -79% |
| Mean-reversion model ≥ 10% | 481 | 4 | -6% | -77% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3167 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1517 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 464 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5148 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 17 | 0% | -$391.40 | -62% | — |
| Sell at 2¢ | 187 | 4% | -$566.78 | -90% | 45 sec |
| Sell at 3¢ | 110 | 2% | -$572.50 | -91% | 50 sec |
| Sell at 5¢ | 81 | 2% | -$562.75 | -89% | 67 sec |
| Sell at 10¢ | 59 | 1% | -$524.11 | -83% | 81 sec |
| Sell at 25¢ | 29 | 1% | -$491.41 | -78% | 1.6 min |
| Sell at 50¢ | 14 | 0% | -$450.90 | -72% | 2.3 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 157 | 2 | 11% | 3% | +21% | -80% | -90% |
| 2–5 min | 1693 | 8 | 7% | 3% | -54% | -88% | -89% |
| 1–2 min | 1358 | 4 | 3% | 2% | -68% | -94% | -94% |
| Under 1 min | 1937 | 3 | 1% | 0% | -77% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 358 | 1 | 4% | 1% | -64% | -91% | -93% |
| ZEC | 354 | 1 | 5% | 2% | -66% | -89% | -93% |
| BNB | 354 | 0 | 4% | 1% | -100% | -92% | -94% |
| ETH | 353 | 2 | 5% | 3% | -30% | -89% | -86% |
| BTC | 352 | 0 | 7% | 3% | -100% | -84% | -89% |
| HYPE | 351 | 2 | 5% | 3% | -31% | -90% | -87% |
| NEAR | 349 | 1 | 6% | 2% | -61% | -86% | -90% |
| XRP | 349 | 3 | 1% | 1% | +10% | -60% | -59% |
| SOL | 347 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 262 | 0 | 5% | 1% | -100% | -90% | -94% |
| SILVER | 246 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 230 | 1 | 3% | 1% | -54% | -94% | -96% |
| COPPER | 218 | 0 | 1% | 0% | -100% | -98% | -99% |
| NATGAS | 190 | 1 | 4% | 2% | -51% | -94% | -92% |
| PLATINUM | 190 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 181 | 0 | 2% | 1% | -100% | -97% | -99% |
| GBPUSD | 165 | 1 | 4% | 2% | -43% | -93% | -94% |
| EURUSD | 162 | 1 | 4% | 2% | -42% | -93% | -92% |
| USDJPY | 137 | 3 | 3% | 2% | +104% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2602 | 10 | 4% | 2% | -56% | -92% | -93% |
| DOWN (bought NO) | 2546 | 7 | 4% | 1% | -68% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 375 | 2 | 1% | 1% | -0% | -45% | -45% |
| 0.05–0.1% | 442 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 766 | 1 | 3% | 1% | -83% | -92% | -92% |
| 0.2–0.5% | 1074 | 3 | 6% | 3% | -69% | -88% | -89% |
| Over 0.5% | 509 | 4 | 6% | 2% | -19% | -88% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,216 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 12:14:10 AM | USDJPY | UP | 50 sec | — | — | In play | — |
| 10/2 12:14:10 AM | BNB | DOWN | 50 sec | +0.030% | — | In play | — |
| 10/2 12:13:42 AM | ZEC | DOWN | 78 sec | +0.308% | — | In play | — |
| 10/2 12:12:55 AM | GBPUSD | DOWN | 2.1 min | — | — | In play | — |
| 10/2 12:12:55 AM | SOL | UP | 2.1 min | -0.320% | — | In play | — |
| 10/2 12:12:39 AM | PALLADIUM | DOWN | 2.3 min | — | — | In play | — |
| 10/2 12:12:23 AM | WTI | UP | 2.6 min | — | — | In play | — |
| 10/2 12:12:23 AM | SILVER | DOWN | 2.6 min | — | — | In play | — |
| 10/2 12:12:23 AM | GOLD | DOWN | 2.6 min | — | — | In play | — |
| 10/2 12:11:51 AM | NEAR | DOWN | 3.1 min | +0.949% | — | In play | — |
| 10/2 12:11:51 AM | ETH | DOWN | 3.1 min | +0.258% | — | In play | — |
| 10/2 12:11:19 AM | HYPE | DOWN | 3.7 min | +0.661% | — | In play | — |
| 10/2 12:11:03 AM | XRP | DOWN | 4.0 min | +0.560% | — | In play | — |
| 10/2 12:06:55 AM | EURUSD | DOWN | 8.1 min | — | — | In play | — |
| 10/1 11:59:52 PM | ETH | DOWN | 7 sec | +0.019% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:59:20 PM | XRP | UP | 39 sec | -0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:59:04 PM | NEAR | DOWN | 56 sec | +0.195% | 0¢ | ❌ Lost | $0.00 |
| 10/1 11:59:04 PM | GBPUSD | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:58:48 PM | EURUSD | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:58:16 PM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:58:16 PM | SILVER | UP | 1.7 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 11:57:42 PM | BNB | UP | 2.3 min | -0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/1 11:57:42 PM | SOL | UP | 2.3 min | -0.264% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:57:42 PM | DOGE | UP | 2.3 min | -0.220% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:57:10 PM | ZEC | UP | 2.8 min | -0.545% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:56:55 PM | BTC | UP | 3.1 min | -0.150% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:54:48 PM | HYPE | DOWN | 5.2 min | +0.793% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:44:28 PM | PLATINUM | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:44:12 PM | USDJPY | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:44:12 PM | GBPUSD | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
