# 15-Minute 1¢ Study

*Updated Tue Oct 6, 3:06 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 642 finished bets | 1% | $29.15 | +42% | +4.54¢ | -$7.10 / $36.25 |

*Expect about **79 buys a day** (~$11.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 640 | $15.90 | +23% |
| Volatility model ≥ 2%, hold to the close | 1189 | $10.90 | +8% |
| 5+ min left, hold to the close | 242 | $6.15 | +17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9346 | 9340 | 40 (0%) | 1.07% | -$564.10 (-50%) | Hold to the close: -$564.10 (-50%) |

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
| Volatility model | 6112 | 4.0% | 0.5% (28) | -570% | ❌ Worse |
| Momentum model | 6112 | 4.1% | 0.5% (28) | -593% | ❌ Worse |
| Mean-reversion model | 6112 | 6.7% | 0.5% (28) | -669% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6112 | 28 | -42% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1189 | 11 | +8% | -71% | -71% | -67% |
| Volatility model ≥ 5% | 642 | 7 | +42% | -59% | -58% | -54% |
| Volatility model ≥ 10% | 396 | 5 | +89% | -40% | -41% | -36% |
| Momentum model ≥ 2% | 1052 | 9 | +4% | -72% | -73% | -71% |
| Momentum model ≥ 5% | 640 | 6 | +23% | -63% | -66% | -63% |
| Momentum model ≥ 10% | 443 | 5 | +62% | -51% | -52% | -50% |
| Mean-reversion model ≥ 2% | 2095 | 15 | -22% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1409 | 13 | +3% | -80% | -80% | -73% |
| Mean-reversion model ≥ 10% | 932 | 9 | +12% | -78% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6309 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2291 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 740 | 3% | 3% | 2% | 1% | 1% | 0% |
| **All** | 9340 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 40 | 0% | -$564.10 | -50% | — |
| Sell at 2¢ | 344 | 4% | -$1,006.66 | -90% | 33 sec |
| Sell at 3¢ | 225 | 2% | -$1,008.35 | -90% | 47 sec |
| Sell at 5¢ | 166 | 2% | -$988.20 | -88% | 56 sec |
| Sell at 10¢ | 112 | 1% | -$935.38 | -83% | 66 sec |
| Sell at 25¢ | 62 | 1% | -$848.88 | -76% | 82 sec |
| Sell at 50¢ | 39 | 0% | -$748.85 | -67% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 239 | 3 | 10% | 3% | +19% | -82% | -89% |
| 2–5 min | 3010 | 21 | 7% | 3% | -32% | -87% | -87% |
| 1–2 min | 2458 | 11 | 3% | 2% | -51% | -94% | -93% |
| Under 1 min | 3630 | 5 | 1% | 0% | -79% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 714 | 5 | 5% | 3% | -16% | -89% | -89% |
| HYPE | 705 | 3 | 5% | 3% | -47% | -89% | -86% |
| DOGE | 704 | 2 | 4% | 1% | -63% | -91% | -91% |
| ETH | 702 | 7 | 6% | 3% | +25% | -87% | -86% |
| BNB | 699 | 2 | 4% | 2% | -65% | -91% | -92% |
| XRP | 697 | 4 | 1% | 1% | -27% | -78% | -79% |
| SOL | 697 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 696 | 3 | 5% | 2% | -44% | -87% | -90% |
| NEAR | 695 | 4 | 6% | 3% | -25% | -66% | -67% |
| GOLD | 386 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 369 | 0 | 2% | 1% | -100% | -96% | -97% |
| WTI | 350 | 2 | 3% | 1% | -38% | -95% | -97% |
| COPPER | 327 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 293 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 286 | 2 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 280 | 1 | 2% | 1% | -67% | -97% | -98% |
| EURUSD | 268 | 1 | 4% | 3% | -65% | -93% | -91% |
| GBPUSD | 254 | 1 | 4% | 2% | -63% | -94% | -94% |
| USDJPY | 218 | 3 | 2% | 1% | +28% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4716 | 22 | 4% | 2% | -45% | -89% | -88% |
| DOWN (bought NO) | 4624 | 18 | 4% | 2% | -55% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1041 | 7 | 2% | 1% | +15% | -61% | -61% |
| 0.05–0.1% | 1085 | 4 | 3% | 1% | -45% | -91% | -92% |
| 0.1–0.2% | 1579 | 6 | 4% | 2% | -52% | -91% | -91% |
| 0.2–0.5% | 1848 | 9 | 6% | 3% | -46% | -88% | -87% |
| Over 0.5% | 754 | 4 | 7% | 3% | -45% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2400 | 10 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,059 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 2:59:56 AM | ZEC | DOWN | 4 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/6 2:59:56 AM | DOGE | UP | 4 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/6 2:59:40 AM | GOLD | DOWN | 20 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:40 AM | XRP | UP | 20 sec | -0.067% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:40 AM | COPPER | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:24 AM | ETH | DOWN | 36 sec | +0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:24 AM | EURUSD | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:24 AM | NEAR | DOWN | 36 sec | +0.141% | 0¢ | ❌ Lost | $0.00 |
| 10/6 2:59:09 AM | SOL | UP | 50 sec | -0.082% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:58:37 AM | BTC | DOWN | 83 sec | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:58:21 AM | PLATINUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:58:21 AM | BNB | DOWN | 1.6 min | +0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/6 2:57:46 AM | HYPE | DOWN | 2.2 min | +0.234% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:56:39 AM | SILVER | UP | 3.3 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/6 2:54:49 AM | PALLADIUM | UP | 5.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:44:35 AM | SOL | DOWN | 24 sec | +0.024% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:44:35 AM | DOGE | DOWN | 24 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/6 2:44:35 AM | HYPE | UP | 24 sec | -0.113% | 0¢ | ❌ Lost | $0.00 |
| 10/6 2:44:35 AM | NEAR | UP | 24 sec | -0.211% | 0¢ | ❌ Lost | $0.00 |
| 10/6 2:44:19 AM | XRP | DOWN | 40 sec | +0.020% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:44:05 AM | BTC | DOWN | 54 sec | +0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:43:49 AM | COPPER | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:43:33 AM | BNB | DOWN | 87 sec | +0.003% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:43:17 AM | PLATINUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:43:01 AM | SILVER | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:42:45 AM | ZEC | DOWN | 2.2 min | +0.301% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:42:45 AM | WTI | UP | 2.2 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/6 2:42:29 AM | GOLD | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:42:13 AM | GBPUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:42:13 AM | PALLADIUM | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
