# 15-Minute 1¢ Study

*Updated Fri Oct 2, 1:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 324 finished bets | 1% | $6.75 | +19% | +2.08¢ | -$4.15 / $10.90 |

*Expect about **80 buys a day** (~$12.00/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 161 | $4.30 | +18% |
| Momentum model ≥ 5%, sell at 50¢ | 324 | -$0.50 | -1% |
| Volatility model ≥ 5%, hold to the close | 316 | -$6.65 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5259 | 5253 | 18 (0%) | 1.07% | -$388.65 (-61%) | Hold to the close: -$388.65 (-61%) |

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
| Volatility model | 3032 | 3.6% | 0.3% (8) | -616% | ❌ Worse |
| Momentum model | 3032 | 3.7% | 0.3% (8) | -666% | ❌ Worse |
| Mean-reversion model | 3032 | 6.7% | 0.3% (8) | -790% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3032 | 8 | -67% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 644 | 4 | -29% | -66% | -68% | -65% |
| Volatility model ≥ 5% | 316 | 2 | -19% | -39% | -40% | -37% |
| Volatility model ≥ 10% | 178 | 2 | +65% | +1% | -1% | +6% |
| Momentum model ≥ 2% | 560 | 3 | -36% | -63% | -67% | -64% |
| Momentum model ≥ 5% | 324 | 3 | +19% | -45% | -48% | -44% |
| Momentum model ≥ 10% | 214 | 2 | +34% | -22% | -22% | -17% |
| Mean-reversion model ≥ 2% | 1161 | 5 | -54% | -86% | -88% | -85% |
| Mean-reversion model ≥ 5% | 766 | 5 | -29% | -82% | -85% | -80% |
| Mean-reversion model ≥ 10% | 490 | 4 | -8% | -78% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3228 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1550 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 475 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5253 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 18 | 0% | -$388.65 | -61% | — |
| Sell at 2¢ | 190 | 4% | -$577.25 | -90% | 43 sec |
| Sell at 3¢ | 111 | 2% | -$583.36 | -91% | 49 sec |
| Sell at 5¢ | 82 | 2% | -$573.35 | -89% | 66 sec |
| Sell at 10¢ | 60 | 1% | -$534.05 | -83% | 81 sec |
| Sell at 25¢ | 30 | 1% | -$499.35 | -78% | 1.6 min |
| Sell at 50¢ | 15 | 0% | -$455.40 | -71% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 158 | 2 | 11% | 3% | +20% | -80% | -90% |
| 2–5 min | 1714 | 8 | 7% | 3% | -55% | -88% | -90% |
| 1–2 min | 1387 | 5 | 3% | 2% | -61% | -94% | -94% |
| Under 1 min | 1991 | 3 | 1% | 0% | -78% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 365 | 1 | 4% | 1% | -65% | -91% | -93% |
| BNB | 361 | 0 | 4% | 1% | -100% | -92% | -95% |
| ETH | 360 | 2 | 5% | 3% | -31% | -89% | -87% |
| ZEC | 360 | 1 | 5% | 2% | -67% | -90% | -94% |
| BTC | 359 | 0 | 6% | 3% | -100% | -85% | -89% |
| HYPE | 357 | 2 | 4% | 3% | -31% | -90% | -88% |
| NEAR | 356 | 1 | 6% | 2% | -62% | -86% | -90% |
| XRP | 356 | 3 | 1% | 1% | +9% | -60% | -60% |
| SOL | 354 | 0 | 3% | 1% | -100% | -93% | -93% |
| GOLD | 268 | 0 | 4% | 1% | -100% | -90% | -94% |
| SILVER | 251 | 0 | 2% | 1% | -100% | -97% | -96% |
| WTI | 236 | 1 | 3% | 1% | -55% | -94% | -96% |
| COPPER | 223 | 0 | 1% | 0% | -100% | -98% | -99% |
| PLATINUM | 194 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 192 | 1 | 4% | 2% | -51% | -94% | -92% |
| PALLADIUM | 186 | 1 | 3% | 1% | -50% | -95% | -97% |
| GBPUSD | 168 | 1 | 4% | 2% | -44% | -93% | -94% |
| EURUSD | 166 | 1 | 4% | 2% | -44% | -93% | -92% |
| USDJPY | 141 | 3 | 3% | 2% | +99% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2667 | 11 | 4% | 2% | -53% | -92% | -93% |
| DOWN (bought NO) | 2586 | 7 | 4% | 1% | -69% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 384 | 2 | 1% | 1% | -3% | -47% | -46% |
| 0.05–0.1% | 454 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 785 | 1 | 3% | 1% | -83% | -92% | -93% |
| 0.2–0.5% | 1088 | 3 | 6% | 3% | -69% | -89% | -89% |
| Over 0.5% | 516 | 4 | 6% | 2% | -20% | -88% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1221 | 3 | 4% | 1% | -72% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,198 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 1:44:57 AM | SILVER | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:44:57 AM | COPPER | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:44:41 AM | GOLD | UP | 18 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:44:41 AM | ETH | UP | 18 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:44:25 AM | ZEC | DOWN | 34 sec | -0.005% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:44:25 AM | SOL | UP | 34 sec | -0.151% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:44:09 AM | XRP | DOWN | 51 sec | +0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:44:09 AM | NEAR | DOWN | 51 sec | +0.119% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:44:09 AM | EURUSD | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:43:20 AM | USDJPY | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:43:20 AM | HYPE | DOWN | 1.6 min | +0.182% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:43:04 AM | WTI | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:43:04 AM | DOGE | DOWN | 1.9 min | +0.251% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:41:41 AM | BNB | UP | 3.3 min | -0.260% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:41:25 AM | BTC | UP | 3.6 min | -0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:59 AM | EURUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:43 AM | PLATINUM | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:43 AM | GBPUSD | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:43 AM | PALLADIUM | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:27 AM | BTC | UP | 33 sec | -0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:27 AM | ZEC | UP | 33 sec | -0.132% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:29:27 AM | WTI | UP | 33 sec | — | 1¢ | ❌ Lost | $0.00 |
| 10/2 1:29:27 AM | GOLD | UP | 33 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:11 AM | COPPER | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:28:54 AM | XRP | UP | 65 sec | -0.138% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:28:38 AM | BNB | UP | 81 sec | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:28:22 AM | SOL | UP | 1.6 min | -0.260% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:27:16 AM | DOGE | UP | 2.7 min | -0.227% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:27:01 AM | NEAR | UP | 3.0 min | -0.604% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:27:01 AM | ETH | UP | 3.0 min | -0.132% | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
