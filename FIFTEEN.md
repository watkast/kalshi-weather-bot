# 15-Minute 1¢ Study

*Updated Thu Oct 1, 12:10 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 142 finished bets | 1% | $7.15 | +34% | +5.04¢ | $17.35 / -$10.20 |

*Expect about **39 buys a day** (~$5.84/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 276 | -$2.45 | -8% |
| Volatility model ≥ 5%, sell at 25¢ | 266 | -$5.47 | -19% |
| Volatility model ≥ 5%, sell at 10¢ | 266 | -$6.23 | -21% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4563 | 4555 | 15 (0%) | 1.07% | -$349.95 (-62%) | Hold to the close: -$349.95 (-62%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 2597 | 3.5% | 0.2% (6) | -673% | ❌ Worse |
| Momentum model | 2597 | 3.7% | 0.2% (6) | -729% | ❌ Worse |
| Mean-reversion model | 2597 | 6.6% | 0.2% (6) | -857% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2597 | 6 | -71% | -85% | -87% | -84% |
| Volatility model ≥ 2% | 528 | 3 | -35% | -63% | -65% | -61% |
| Volatility model ≥ 5% | 266 | 1 | -52% | -34% | -35% | -30% |
| Volatility model ≥ 10% | 152 | 1 | -4% | +14% | +12% | +19% |
| Momentum model ≥ 2% | 472 | 2 | -50% | -59% | -63% | -60% |
| Momentum model ≥ 5% | 276 | 2 | -8% | -40% | -42% | -37% |
| Momentum model ≥ 10% | 184 | 1 | -23% | -13% | -12% | -9% |
| Mean-reversion model ≥ 2% | 978 | 3 | -67% | -86% | -88% | -84% |
| Mean-reversion model ≥ 5% | 648 | 3 | -50% | -83% | -85% | -79% |
| Mean-reversion model ≥ 10% | 411 | 2 | -46% | -78% | -81% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2793 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1356 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 406 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 4555 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 15 | 0% | -$349.95 | -62% | — |
| Sell at 2¢ | 168 | 4% | -$502.27 | -90% | 46 sec |
| Sell at 3¢ | 100 | 2% | -$506.95 | -91% | 50 sec |
| Sell at 5¢ | 74 | 2% | -$497.85 | -89% | 66 sec |
| Sell at 10¢ | 53 | 1% | -$462.52 | -83% | 81 sec |
| Sell at 25¢ | 24 | 1% | -$438.51 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$408.95 | -73% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 139 | 2 | 13% | 3% | +37% | -77% | -89% |
| 2–5 min | 1515 | 7 | 7% | 3% | -55% | -88% | -89% |
| 1–2 min | 1179 | 4 | 3% | 2% | -64% | -94% | -93% |
| Under 1 min | 1719 | 2 | 1% | 0% | -83% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 316 | 1 | 4% | 1% | -59% | -90% | -92% |
| ETH | 313 | 2 | 5% | 3% | -22% | -89% | -87% |
| NEAR | 310 | 0 | 5% | 1% | -100% | -88% | -92% |
| ZEC | 310 | 1 | 5% | 2% | -62% | -89% | -94% |
| HYPE | 310 | 1 | 5% | 3% | -61% | -90% | -88% |
| BNB | 310 | 0 | 4% | 1% | -100% | -92% | -95% |
| BTC | 309 | 0 | 7% | 3% | -100% | -84% | -88% |
| XRP | 308 | 3 | 2% | 1% | +26% | -54% | -53% |
| SOL | 307 | 0 | 3% | 1% | -100% | -92% | -91% |
| GOLD | 233 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 217 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 206 | 1 | 3% | 1% | -50% | -94% | -96% |
| COPPER | 192 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 177 | 1 | 4% | 2% | -47% | -93% | -91% |
| PLATINUM | 168 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 163 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 145 | 1 | 5% | 2% | -36% | -92% | -93% |
| EURUSD | 141 | 1 | 4% | 1% | -34% | -94% | -94% |
| USDJPY | 120 | 3 | 3% | 2% | +133% | -94% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2329 | 9 | 4% | 2% | -56% | -92% | -92% |
| DOWN (bought NO) | 2226 | 6 | 4% | 1% | -69% | -87% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 322 | 1 | 1% | 1% | -43% | -38% | -38% |
| 0.05–0.1% | 389 | 0 | 2% | 0% | -100% | -94% | -96% |
| 0.1–0.2% | 662 | 1 | 4% | 2% | -80% | -91% | -92% |
| 0.2–0.5% | 953 | 2 | 6% | 3% | -77% | -89% | -89% |
| Over 0.5% | 466 | 4 | 7% | 2% | -11% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,194 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 12:10:58 PM | BNB | UP | 4.0 min | -0.163% | — | In play | — |
| 10/1 12:10:58 PM | ZEC | UP | 4.0 min | -0.679% | — | In play | — |
| 10/1 11:59:49 AM | NATGAS | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:58:58 AM | EURUSD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:58:26 AM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:58:26 AM | GOLD | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:58:11 AM | ZEC | UP | 1.8 min | -0.534% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:58:11 AM | PALLADIUM | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:57:37 AM | XRP | UP | 2.4 min | -0.359% | 2¢ | ❌ Lost | -$0.15 |
| 10/1 11:57:37 AM | BNB | UP | 2.4 min | -0.212% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:57:37 AM | GBPUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:57:21 AM | BTC | UP | 2.6 min | -0.276% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:57:21 AM | SILVER | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:57:21 AM | PLATINUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:57:06 AM | DOGE | UP | 2.9 min | -0.376% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:56:49 AM | ETH | UP | 3.2 min | -0.336% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:56:49 AM | USDJPY | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:56:49 AM | SOL | UP | 3.2 min | -0.555% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:56:49 AM | WTI | DOWN | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:55:44 AM | NEAR | UP | 4.3 min | -0.999% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:55:44 AM | HYPE | UP | 4.3 min | -0.565% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:44:48 AM | HYPE | DOWN | 11 sec | -0.009% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:44:32 AM | ETH | DOWN | 27 sec | +0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/1 11:44:32 AM | SILVER | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:44:32 AM | WTI | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:44:16 AM | COPPER | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:44:16 AM | GOLD | DOWN | 44 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 11:44:16 AM | XRP | DOWN | 44 sec | +0.140% | 0¢ | ❌ Lost | $0.00 |
| 10/1 11:44:16 AM | BNB | UP | 44 sec | -0.085% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 11:43:59 AM | DOGE | DOWN | 60 sec | +0.117% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
