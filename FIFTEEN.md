# 15-Minute 1¢ Study

*Updated Fri Oct 2, 4:34 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 337 finished bets | 1% | $5.70 | +16% | +1.69¢ | -$4.90 / $10.60 |

*Expect about **81 buys a day** (~$12.15/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 163 | $4.00 | +17% |
| Momentum model ≥ 5%, sell at 50¢ | 337 | -$1.55 | -4% |
| Volatility model ≥ 5%, hold to the close | 329 | -$7.70 | -22% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5427 | 5421 | 19 (0%) | 1.07% | -$393.25 (-60%) | Hold to the close: -$393.25 (-60%) |

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
| Volatility model | 3130 | 3.6% | 0.3% (9) | -609% | ❌ Worse |
| Momentum model | 3130 | 3.8% | 0.3% (9) | -659% | ❌ Worse |
| Mean-reversion model | 3130 | 6.7% | 0.3% (9) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3130 | 9 | -63% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 667 | 4 | -31% | -67% | -68% | -65% |
| Volatility model ≥ 5% | 329 | 2 | -22% | -41% | -42% | -39% |
| Volatility model ≥ 10% | 185 | 2 | +62% | -1% | -3% | +4% |
| Momentum model ≥ 2% | 581 | 3 | -38% | -64% | -68% | -65% |
| Momentum model ≥ 5% | 337 | 3 | +16% | -46% | -50% | -45% |
| Momentum model ≥ 10% | 224 | 2 | +29% | -24% | -25% | -21% |
| Mean-reversion model ≥ 2% | 1202 | 6 | -46% | -86% | -88% | -84% |
| Mean-reversion model ≥ 5% | 792 | 6 | -18% | -82% | -84% | -79% |
| Mean-reversion model ≥ 10% | 504 | 4 | -10% | -78% | -82% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3326 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1601 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 494 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5421 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 19 | 0% | -$393.25 | -60% | — |
| Sell at 2¢ | 197 | 4% | -$594.03 | -90% | 46 sec |
| Sell at 3¢ | 116 | 2% | -$600.01 | -91% | 50 sec |
| Sell at 5¢ | 84 | 2% | -$590.65 | -90% | 66 sec |
| Sell at 10¢ | 61 | 1% | -$551.34 | -84% | 81 sec |
| Sell at 25¢ | 31 | 1% | -$514.64 | -78% | 1.6 min |
| Sell at 50¢ | 16 | 0% | -$467.25 | -71% | 2.3 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 160 | 2 | 12% | 2% | +19% | -79% | -90% |
| 2–5 min | 1769 | 9 | 7% | 3% | -50% | -88% | -89% |
| 1–2 min | 1425 | 5 | 3% | 2% | -62% | -94% | -93% |
| Under 1 min | 2064 | 3 | 1% | 0% | -79% | -91% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 377 | 2 | 4% | 1% | -32% | -91% | -91% |
| BNB | 372 | 0 | 3% | 1% | -100% | -92% | -95% |
| ETH | 371 | 2 | 5% | 3% | -33% | -88% | -86% |
| ZEC | 371 | 1 | 5% | 2% | -68% | -90% | -94% |
| BTC | 370 | 0 | 6% | 2% | -100% | -84% | -89% |
| HYPE | 368 | 2 | 4% | 3% | -33% | -90% | -88% |
| XRP | 367 | 3 | 1% | 1% | +5% | -62% | -61% |
| NEAR | 366 | 1 | 6% | 2% | -63% | -86% | -90% |
| SOL | 364 | 0 | 3% | 1% | -100% | -93% | -93% |
| GOLD | 277 | 0 | 5% | 1% | -100% | -89% | -93% |
| SILVER | 257 | 0 | 2% | 1% | -100% | -97% | -96% |
| WTI | 243 | 1 | 3% | 1% | -56% | -94% | -96% |
| COPPER | 231 | 0 | 1% | 0% | -100% | -98% | -99% |
| PLATINUM | 201 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 199 | 1 | 4% | 2% | -53% | -94% | -92% |
| PALLADIUM | 193 | 1 | 3% | 1% | -52% | -96% | -97% |
| GBPUSD | 175 | 1 | 4% | 2% | -47% | -93% | -94% |
| EURUSD | 173 | 1 | 4% | 2% | -46% | -93% | -92% |
| USDJPY | 146 | 3 | 3% | 2% | +92% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2748 | 12 | 4% | 2% | -50% | -92% | -93% |
| DOWN (bought NO) | 2673 | 7 | 4% | 1% | -70% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 399 | 2 | 1% | 1% | -5% | -48% | -47% |
| 0.05–0.1% | 468 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 810 | 1 | 3% | 1% | -84% | -92% | -93% |
| 0.2–0.5% | 1126 | 4 | 6% | 3% | -60% | -88% | -89% |
| Over 0.5% | 522 | 4 | 7% | 2% | -21% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1389 | 4 | 4% | 1% | -67% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,140 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 4:29:54 AM | DOGE | DOWN | 6 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:29:54 AM | SILVER | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:29:54 AM | COPPER | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:29:54 AM | GOLD | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:29:38 AM | ETH | DOWN | 22 sec | +0.025% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:29:22 AM | BTC | DOWN | 38 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:29:07 AM | SOL | DOWN | 52 sec | +0.110% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:29:07 AM | NEAR | DOWN | 52 sec | +0.301% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:28:51 AM | BNB | DOWN | 69 sec | +0.062% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:28:19 AM | XRP | DOWN | 1.7 min | +0.351% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:28:19 AM | ZEC | DOWN | 1.7 min | +0.552% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:27:14 AM | PALLADIUM | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:27:14 AM | EURUSD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:26:42 AM | WTI | DOWN | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:26:10 AM | DOGE | UP | 3.8 min | -0.342% | 100¢ | ✅ Won | $13.85 |
| 10/2 4:25:05 AM | HYPE | DOWN | 4.9 min | +0.541% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:14:58 AM | ZEC | DOWN | 1 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:14:42 AM | BTC | UP | 17 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:14:10 AM | GBPUSD | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:14:10 AM | WTI | DOWN | 50 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:13:53 AM | SOL | UP | 66 sec | -0.132% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:13:53 AM | ETH | UP | 66 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:13:53 AM | XRP | UP | 66 sec | -0.175% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:13:37 AM | BNB | UP | 82 sec | -0.113% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:13:37 AM | NEAR | DOWN | 82 sec | +0.314% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:13:37 AM | DOGE | UP | 82 sec | -0.160% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:13:21 AM | NATGAS | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:13:21 AM | PALLADIUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:12:48 AM | COPPER | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:12:32 AM | HYPE | DOWN | 2.5 min | +0.284% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
