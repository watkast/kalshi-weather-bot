# 15-Minute 1¢ Study

*Updated Tue Oct 6, 3:38 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 676 finished bets | 1% | $39.70 | +55% | +5.87¢ | -$8.75 / $48.45 |

*Expect about **78 buys a day** (~$11.76/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 677 | $26.30 | +37% |
| Mean-reversion model ≥ 5%, hold to the close | 1488 | $22.95 | +12% |
| 5+ min left, hold to the close | 251 | $18.80 | +51% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9867 | 9861 | 46 (0%) | 1.07% | -$545.35 (-46%) | Hold to the close: -$545.35 (-46%) |

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
| Volatility model | 6428 | 4.1% | 0.5% (33) | -541% | ❌ Worse |
| Momentum model | 6428 | 4.2% | 0.5% (33) | -568% | ❌ Worse |
| Mean-reversion model | 6428 | 6.7% | 0.5% (33) | -624% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6428 | 33 | -35% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1250 | 12 | +12% | -72% | -72% | -67% |
| Volatility model ≥ 5% | 676 | 8 | +55% | -60% | -59% | -55% |
| Volatility model ≥ 10% | 417 | 6 | +116% | -42% | -43% | -37% |
| Momentum model ≥ 2% | 1115 | 10 | +9% | -73% | -74% | -72% |
| Momentum model ≥ 5% | 677 | 7 | +37% | -65% | -67% | -64% |
| Momentum model ≥ 10% | 468 | 6 | +86% | -53% | -53% | -50% |
| Mean-reversion model ≥ 2% | 2204 | 19 | -6% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1488 | 15 | +12% | -80% | -80% | -74% |
| Mean-reversion model ≥ 10% | 979 | 11 | +30% | -79% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6625 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2447 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 789 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 9861 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 46 | 0% | -$545.35 | -46% | — |
| Sell at 2¢ | 359 | 4% | -$1,068.01 | -90% | 33 sec |
| Sell at 3¢ | 237 | 2% | -$1,068.92 | -90% | 47 sec |
| Sell at 5¢ | 177 | 2% | -$1,046.30 | -88% | 50 sec |
| Sell at 10¢ | 121 | 1% | -$988.84 | -83% | 65 sec |
| Sell at 25¢ | 70 | 1% | -$887.65 | -75% | 82 sec |
| Sell at 50¢ | 46 | 0% | -$766.85 | -64% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 248 | 4 | 10% | 4% | +52% | -82% | -87% |
| 2–5 min | 3176 | 24 | 7% | 3% | -26% | -87% | -87% |
| 1–2 min | 2602 | 11 | 3% | 2% | -54% | -94% | -93% |
| Under 1 min | 3832 | 7 | 1% | 0% | -73% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 751 | 6 | 5% | 3% | -4% | -89% | -89% |
| HYPE | 741 | 3 | 5% | 3% | -50% | -89% | -87% |
| DOGE | 740 | 2 | 4% | 1% | -65% | -92% | -91% |
| ETH | 737 | 7 | 5% | 3% | +19% | -87% | -87% |
| BNB | 734 | 3 | 4% | 2% | -51% | -91% | -92% |
| NEAR | 731 | 5 | 6% | 3% | -10% | -67% | -68% |
| SOL | 731 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 730 | 4 | 5% | 3% | -28% | -87% | -89% |
| XRP | 730 | 5 | 2% | 1% | -13% | -79% | -79% |
| GOLD | 411 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 395 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 375 | 2 | 3% | 1% | -42% | -95% | -97% |
| COPPER | 353 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 312 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 303 | 3 | 3% | 2% | -8% | -94% | -92% |
| PALLADIUM | 298 | 1 | 2% | 1% | -69% | -97% | -98% |
| EURUSD | 285 | 1 | 4% | 2% | -67% | -93% | -92% |
| GBPUSD | 273 | 1 | 3% | 2% | -66% | -94% | -94% |
| USDJPY | 231 | 3 | 2% | 1% | +21% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4972 | 24 | 4% | 2% | -44% | -89% | -89% |
| DOWN (bought NO) | 4889 | 22 | 3% | 2% | -48% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1092 | 8 | 2% | 1% | +26% | -63% | -62% |
| 0.05–0.1% | 1134 | 4 | 3% | 1% | -48% | -91% | -92% |
| 0.1–0.2% | 1675 | 6 | 4% | 2% | -55% | -91% | -92% |
| 0.2–0.5% | 1944 | 12 | 6% | 3% | -32% | -88% | -87% |
| Over 0.5% | 778 | 5 | 7% | 3% | -34% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2119 | 7 | 3% | 1% | -61% | -87% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,045 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 3:29:49 PM | NATGAS | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:29:33 PM | BNB | DOWN | 26 sec | -0.019% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:29:33 PM | XRP | DOWN | 26 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/6 3:29:17 PM | ZEC | DOWN | 43 sec | +0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:29:17 PM | ETH | UP | 43 sec | -0.016% | 0¢ | ❌ Lost | $0.00 |
| 10/6 3:29:02 PM | HYPE | UP | 57 sec | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:29:02 PM | NEAR | UP | 57 sec | -0.359% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:29:02 PM | DOGE | UP | 57 sec | -0.136% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:28:30 PM | WTI | UP | 89 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:14:45 PM | USDJPY | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:14:45 PM | NATGAS | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:14:29 PM | XRP | UP | 31 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/6 3:14:29 PM | NEAR | UP | 31 sec | -0.174% | 0¢ | ❌ Lost | $0.00 |
| 10/6 3:14:12 PM | ETH | UP | 47 sec | -0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:13:39 PM | SOL | UP | 81 sec | -0.132% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:13:39 PM | DOGE | DOWN | 81 sec | +0.121% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:13:39 PM | BTC | UP | 81 sec | -0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:13:08 PM | WTI | UP | 1.9 min | — | 2¢ | ❌ Lost | $0.00 |
| 10/6 3:11:00 PM | ZEC | UP | 4.0 min | -0.408% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:10:12 PM | HYPE | UP | 4.8 min | -0.352% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:44 PM | GOLD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:44 PM | HYPE | UP | 15 sec | -0.041% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:27 PM | WTI | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:27 PM | BNB | DOWN | 33 sec | +0.013% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:27 PM | XRP | UP | 33 sec | -0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:27 PM | ETH | DOWN | 33 sec | +0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:27 PM | BTC | UP | 33 sec | -0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:11 PM | GBPUSD | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:11 PM | EURUSD | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:59:11 PM | NATGAS | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
