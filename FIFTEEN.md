# 15-Minute 1¢ Study

*Updated Thu Oct 1, 11:23 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 314 finished bets | 1% | $7.65 | +22% | +2.44¢ | -$3.55 / $11.20 |

*Expect about **80 buys a day** (~$11.94/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 156 | $5.05 | +22% |
| Momentum model ≥ 5%, sell at 50¢ | 314 | $0.40 | +1% |
| Volatility model ≥ 5%, hold to the close | 306 | -$5.75 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5116 | 5110 | 16 (0%) | 1.07% | -$400.30 (-64%) | Hold to the close: -$400.30 (-64%) |

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
| Volatility model | 2945 | 3.5% | 0.2% (7) | -637% | ❌ Worse |
| Momentum model | 2945 | 3.7% | 0.2% (7) | -685% | ❌ Worse |
| Mean-reversion model | 2945 | 6.6% | 0.2% (7) | -824% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2945 | 7 | -70% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 618 | 4 | -26% | -65% | -67% | -64% |
| Volatility model ≥ 5% | 306 | 2 | -17% | -38% | -39% | -35% |
| Volatility model ≥ 10% | 172 | 2 | +71% | +5% | +2% | +9% |
| Momentum model ≥ 2% | 546 | 3 | -34% | -63% | -66% | -63% |
| Momentum model ≥ 5% | 314 | 3 | +22% | -44% | -47% | -42% |
| Momentum model ≥ 10% | 207 | 2 | +38% | -21% | -19% | -15% |
| Mean-reversion model ≥ 2% | 1127 | 4 | -62% | -86% | -88% | -85% |
| Mean-reversion model ≥ 5% | 745 | 4 | -42% | -82% | -85% | -80% |
| Mean-reversion model ≥ 10% | 474 | 3 | -29% | -78% | -82% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3141 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1511 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 458 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5110 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 16 | 0% | -$400.30 | -64% | — |
| Sell at 2¢ | 186 | 4% | -$561.94 | -90% | 44 sec |
| Sell at 3¢ | 109 | 2% | -$567.79 | -91% | 49 sec |
| Sell at 5¢ | 80 | 2% | -$558.30 | -89% | 66 sec |
| Sell at 10¢ | 58 | 1% | -$520.32 | -83% | 81 sec |
| Sell at 25¢ | 28 | 1% | -$489.62 | -78% | 1.6 min |
| Sell at 50¢ | 13 | 0% | -$452.55 | -72% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 153 | 2 | 12% | 3% | +24% | -79% | -90% |
| 2–5 min | 1677 | 7 | 7% | 3% | -59% | -88% | -90% |
| 1–2 min | 1351 | 4 | 3% | 2% | -68% | -94% | -94% |
| Under 1 min | 1926 | 3 | 1% | 0% | -77% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 355 | 1 | 4% | 1% | -64% | -91% | -93% |
| ZEC | 351 | 1 | 5% | 2% | -66% | -89% | -93% |
| BNB | 351 | 0 | 4% | 1% | -100% | -92% | -94% |
| ETH | 350 | 2 | 5% | 3% | -30% | -89% | -86% |
| BTC | 349 | 0 | 7% | 3% | -100% | -84% | -89% |
| HYPE | 348 | 1 | 4% | 3% | -65% | -90% | -88% |
| NEAR | 347 | 1 | 6% | 2% | -61% | -86% | -90% |
| XRP | 346 | 3 | 1% | 1% | +12% | -59% | -59% |
| SOL | 344 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 262 | 0 | 5% | 1% | -100% | -90% | -94% |
| SILVER | 244 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 229 | 1 | 3% | 1% | -54% | -94% | -96% |
| COPPER | 217 | 0 | 1% | 0% | -100% | -98% | -99% |
| NATGAS | 190 | 1 | 4% | 2% | -51% | -94% | -92% |
| PLATINUM | 189 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 180 | 0 | 2% | 1% | -100% | -97% | -99% |
| GBPUSD | 163 | 1 | 4% | 2% | -43% | -93% | -94% |
| EURUSD | 160 | 1 | 4% | 2% | -42% | -92% | -92% |
| USDJPY | 135 | 3 | 3% | 2% | +107% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2573 | 9 | 4% | 2% | -60% | -92% | -93% |
| DOWN (bought NO) | 2537 | 7 | 4% | 1% | -68% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 372 | 2 | 1% | 1% | +1% | -45% | -44% |
| 0.05–0.1% | 442 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 762 | 1 | 3% | 1% | -83% | -92% | -92% |
| 0.2–0.5% | 1061 | 2 | 6% | 3% | -79% | -88% | -89% |
| Over 0.5% | 503 | 4 | 7% | 2% | -18% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1612 | 5 | 3% | 2% | -64% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,212 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 11:14:11 PM | BTC | UP | 48 sec | -0.053% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:13:26 PM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:13:26 PM | XRP | UP | 1.6 min | -0.320% | 0¢ | ❌ Lost | $0.00 |
| 10/1 11:13:26 PM | ZEC | UP | 1.6 min | -0.485% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:12:44 PM | GOLD | DOWN | 2.3 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/1 11:12:44 PM | SILVER | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:12:28 PM | DOGE | UP | 2.5 min | -0.332% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:12:12 PM | NATGAS | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:11:56 PM | PALLADIUM | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:11:39 PM | WTI | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:10:51 PM | NEAR | UP | 4.2 min | -0.947% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:10:19 PM | ETH | UP | 4.7 min | -0.328% | 2¢ | ❌ Lost | -$0.15 |
| 10/1 11:10:19 PM | BNB | UP | 4.7 min | -0.240% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:59:57 PM | GOLD | DOWN | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:59:57 PM | ETH | DOWN | 3 sec | +0.107% | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:59:57 PM | PLATINUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:59:57 PM | PALLADIUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:59:41 PM | WTI | UP | 19 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:59:41 PM | COPPER | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:59:08 PM | NEAR | UP | 51 sec | -0.354% | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:58:37 PM | BNB | UP | 83 sec | -0.110% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:58:37 PM | BTC | DOWN | 83 sec | +0.089% | 3¢ | ❌ Lost | -$0.15 |
| 10/1 10:58:37 PM | USDJPY | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:58:21 PM | ZEC | DOWN | 1.6 min | +0.400% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:58:04 PM | HYPE | UP | 1.9 min | -0.332% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:57:31 PM | DOGE | DOWN | 2.5 min | +0.460% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:57:31 PM | SOL | DOWN | 2.5 min | +0.570% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:57:15 PM | XRP | DOWN | 2.8 min | +0.440% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:44:55 PM | WTI | DOWN | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:44:39 PM | DOGE | UP | 21 sec | -0.091% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
