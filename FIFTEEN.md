# 15-Minute 1¢ Study

*Updated Fri Oct 2, 5:25 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 340 finished bets | 1% | $5.40 | +15% | +1.59¢ | -$5.05 / $10.45 |

*Expect about **81 buys a day** (~$12.15/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 165 | $3.70 | +15% |
| Momentum model ≥ 5%, sell at 50¢ | 340 | -$1.85 | -5% |
| Volatility model ≥ 5%, hold to the close | 332 | -$8.15 | -23% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5468 | 5462 | 20 (0%) | 1.07% | -$384.65 (-58%) | Hold to the close: -$384.65 (-58%) |

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
| Volatility model | 3157 | 3.6% | 0.3% (9) | -608% | ❌ Worse |
| Momentum model | 3157 | 3.7% | 0.3% (9) | -657% | ❌ Worse |
| Mean-reversion model | 3157 | 6.7% | 0.3% (9) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3157 | 9 | -64% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 672 | 4 | -32% | -67% | -69% | -66% |
| Volatility model ≥ 5% | 332 | 2 | -23% | -42% | -43% | -40% |
| Volatility model ≥ 10% | 186 | 2 | +61% | -2% | -4% | +3% |
| Momentum model ≥ 2% | 588 | 3 | -39% | -64% | -68% | -65% |
| Momentum model ≥ 5% | 340 | 3 | +15% | -46% | -50% | -46% |
| Momentum model ≥ 10% | 226 | 2 | +28% | -24% | -25% | -21% |
| Mean-reversion model ≥ 2% | 1214 | 6 | -47% | -86% | -88% | -84% |
| Mean-reversion model ≥ 5% | 801 | 6 | -19% | -82% | -85% | -79% |
| Mean-reversion model ≥ 10% | 512 | 4 | -12% | -78% | -82% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3353 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1613 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 496 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5462 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 20 | 0% | -$384.65 | -58% | — |
| Sell at 2¢ | 198 | 4% | -$599.17 | -90% | 46 sec |
| Sell at 3¢ | 117 | 2% | -$605.02 | -91% | 49 sec |
| Sell at 5¢ | 85 | 2% | -$595.40 | -90% | 66 sec |
| Sell at 10¢ | 62 | 1% | -$555.43 | -84% | 81 sec |
| Sell at 25¢ | 32 | 1% | -$516.73 | -78% | 1.6 min |
| Sell at 50¢ | 17 | 0% | -$465.90 | -70% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 162 | 2 | 12% | 2% | +17% | -79% | -90% |
| 2–5 min | 1782 | 9 | 7% | 3% | -51% | -88% | -90% |
| 1–2 min | 1434 | 6 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 2081 | 3 | 1% | 0% | -79% | -91% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 380 | 2 | 4% | 1% | -32% | -91% | -92% |
| BNB | 375 | 0 | 3% | 1% | -100% | -92% | -95% |
| ETH | 374 | 2 | 5% | 3% | -34% | -88% | -86% |
| ZEC | 374 | 1 | 5% | 2% | -68% | -90% | -94% |
| BTC | 373 | 0 | 6% | 2% | -100% | -85% | -89% |
| HYPE | 371 | 2 | 4% | 3% | -33% | -90% | -88% |
| XRP | 370 | 3 | 1% | 1% | +4% | -62% | -61% |
| NEAR | 369 | 1 | 6% | 2% | -63% | -86% | -90% |
| SOL | 367 | 0 | 3% | 1% | -100% | -93% | -93% |
| GOLD | 279 | 0 | 5% | 1% | -100% | -90% | -93% |
| SILVER | 258 | 0 | 2% | 1% | -100% | -97% | -96% |
| WTI | 244 | 1 | 3% | 1% | -57% | -94% | -96% |
| COPPER | 233 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 202 | 2 | 4% | 2% | -8% | -93% | -91% |
| PLATINUM | 202 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 195 | 1 | 3% | 1% | -52% | -96% | -97% |
| GBPUSD | 175 | 1 | 4% | 2% | -47% | -93% | -94% |
| EURUSD | 174 | 1 | 4% | 2% | -46% | -93% | -93% |
| USDJPY | 147 | 3 | 3% | 2% | +90% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2767 | 13 | 4% | 2% | -46% | -92% | -92% |
| DOWN (bought NO) | 2695 | 7 | 4% | 1% | -70% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 403 | 2 | 1% | 1% | -7% | -49% | -48% |
| 0.05–0.1% | 469 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 820 | 1 | 3% | 1% | -84% | -92% | -93% |
| 0.2–0.5% | 1135 | 4 | 6% | 3% | -61% | -89% | -89% |
| Over 0.5% | 525 | 4 | 7% | 2% | -21% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1430 | 5 | 4% | 1% | -60% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,152 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 5:14:42 AM | USDJPY | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 5:14:42 AM | GOLD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 5:14:10 AM | NEAR | UP | 50 sec | -0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:14:10 AM | PALLADIUM | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 5:13:37 AM | NATGAS | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 5:13:37 AM | XRP | DOWN | 82 sec | +0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:12:00 AM | DOGE | DOWN | 3.0 min | +0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:11:10 AM | SOL | DOWN | 3.8 min | +0.326% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:11:10 AM | ZEC | DOWN | 3.8 min | +0.553% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:10:55 AM | BTC | DOWN | 4.1 min | +0.228% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:10:55 AM | HYPE | DOWN | 4.1 min | +0.420% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 5:10:06 AM | ETH | DOWN | 4.9 min | +0.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:09:50 AM | BNB | DOWN | 5.2 min | +0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:59:55 AM | PALLADIUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:59:39 AM | COPPER | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:59:23 AM | HYPE | UP | 36 sec | -0.112% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:58:33 AM | SOL | UP | 87 sec | -0.177% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:58:02 AM | DOGE | UP | 1.9 min | -0.238% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:57:30 AM | BTC | UP | 2.5 min | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:57:14 AM | BNB | UP | 2.8 min | -0.134% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:56:58 AM | NATGAS | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:56:25 AM | ETH | UP | 3.6 min | -0.225% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:56:09 AM | XRP | UP | 3.9 min | -0.369% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:55:53 AM | NEAR | UP | 4.1 min | -0.749% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:54:31 AM | ZEC | UP | 5.5 min | -0.766% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:44:52 AM | WTI | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:44:36 AM | SILVER | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:44:36 AM | COPPER | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:44:36 AM | EURUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:44:36 AM | XRP | DOWN | 24 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
