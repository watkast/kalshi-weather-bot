# 15-Minute 1¢ Study

*Updated Mon Oct 5, 9:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 624 finished bets | 1% | $30.95 | +46% | +4.96¢ | -$6.35 / $37.30 |

*Expect about **79 buys a day** (~$11.92/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 625 | $17.40 | +26% |
| Volatility model ≥ 2%, hold to the close | 1162 | $14.05 | +10% |
| Mean-reversion model ≥ 5%, hold to the close | 1381 | $8.45 | +5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9118 | 9112 | 39 (0%) | 1.07% | -$550.65 (-50%) | Hold to the close: -$550.65 (-50%) |

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
| Volatility model | 5976 | 4.1% | 0.5% (27) | -580% | ❌ Worse |
| Momentum model | 5976 | 4.1% | 0.5% (27) | -605% | ❌ Worse |
| Mean-reversion model | 5976 | 6.7% | 0.5% (27) | -680% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5976 | 27 | -43% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 1162 | 11 | +10% | -70% | -70% | -66% |
| Volatility model ≥ 5% | 624 | 7 | +46% | -57% | -56% | -53% |
| Volatility model ≥ 10% | 385 | 5 | +94% | -38% | -40% | -34% |
| Momentum model ≥ 2% | 1028 | 9 | +6% | -71% | -73% | -71% |
| Momentum model ≥ 5% | 625 | 6 | +26% | -63% | -65% | -62% |
| Momentum model ≥ 10% | 431 | 5 | +67% | -50% | -51% | -48% |
| Mean-reversion model ≥ 2% | 2055 | 15 | -20% | -83% | -83% | -79% |
| Mean-reversion model ≥ 5% | 1381 | 13 | +5% | -79% | -79% | -73% |
| Mean-reversion model ≥ 10% | 910 | 9 | +14% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6173 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2226 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 713 | 3% | 3% | 2% | 2% | 1% | 0% |
| **All** | 9112 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 39 | 0% | -$550.65 | -50% | — |
| Sell at 2¢ | 342 | 4% | -$979.73 | -89% | 33 sec |
| Sell at 3¢ | 224 | 2% | -$981.29 | -89% | 47 sec |
| Sell at 5¢ | 165 | 2% | -$961.40 | -88% | 61 sec |
| Sell at 10¢ | 111 | 1% | -$909.24 | -83% | 66 sec |
| Sell at 25¢ | 61 | 1% | -$824.74 | -75% | 83 sec |
| Sell at 50¢ | 38 | 0% | -$728.15 | -66% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 233 | 3 | 10% | 3% | +22% | -82% | -89% |
| 2–5 min | 2944 | 21 | 7% | 3% | -30% | -87% | -87% |
| 1–2 min | 2400 | 10 | 3% | 2% | -55% | -93% | -93% |
| Under 1 min | 3532 | 5 | 1% | 0% | -79% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 698 | 5 | 5% | 3% | -14% | -89% | -89% |
| DOGE | 689 | 2 | 4% | 1% | -63% | -91% | -91% |
| HYPE | 689 | 3 | 5% | 3% | -47% | -88% | -86% |
| ETH | 688 | 6 | 6% | 3% | +10% | -87% | -86% |
| BNB | 685 | 2 | 4% | 2% | -65% | -90% | -92% |
| BTC | 682 | 3 | 5% | 2% | -42% | -87% | -90% |
| XRP | 682 | 4 | 1% | 1% | -25% | -78% | -78% |
| SOL | 681 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 679 | 4 | 6% | 3% | -23% | -66% | -66% |
| GOLD | 374 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 359 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 341 | 2 | 3% | 1% | -37% | -95% | -96% |
| COPPER | 316 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 284 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 279 | 2 | 3% | 2% | -33% | -94% | -93% |
| PALLADIUM | 273 | 1 | 2% | 1% | -66% | -97% | -98% |
| EURUSD | 258 | 1 | 4% | 3% | -64% | -93% | -91% |
| GBPUSD | 244 | 1 | 4% | 2% | -62% | -94% | -94% |
| USDJPY | 211 | 3 | 2% | 1% | +33% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4624 | 21 | 4% | 2% | -47% | -89% | -88% |
| DOWN (bought NO) | 4488 | 18 | 4% | 2% | -54% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1015 | 7 | 2% | 1% | +18% | -60% | -60% |
| 0.05–0.1% | 1054 | 3 | 3% | 1% | -58% | -91% | -92% |
| 0.1–0.2% | 1547 | 6 | 4% | 2% | -51% | -91% | -91% |
| 0.2–0.5% | 1810 | 9 | 6% | 3% | -45% | -88% | -87% |
| Over 0.5% | 745 | 4 | 7% | 3% | -45% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2580 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,126 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 8:59:55 PM | EURUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:59:39 PM | HYPE | UP | 20 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/5 8:59:23 PM | ZEC | UP | 36 sec | -0.069% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:59:07 PM | BNB | UP | 52 sec | -0.056% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:59:07 PM | PALLADIUM | DOWN | 52 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:59:07 PM | WTI | DOWN | 52 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:58:17 PM | XRP | UP | 1.7 min | -0.167% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:58:17 PM | ETH | UP | 1.7 min | -0.106% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:57:45 PM | BTC | UP | 2.2 min | -0.112% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:57:13 PM | DOGE | UP | 2.8 min | -0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:56:08 PM | SOL | UP | 3.9 min | -0.216% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:54:50 PM | SILVER | DOWN | 5.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:54:34 PM | NEAR | UP | 5.4 min | -0.709% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:53:30 PM | GOLD | DOWN | 6.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:44:58 PM | NATGAS | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:44:58 PM | SILVER | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 8:44:41 PM | WTI | UP | 19 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 8:44:41 PM | COPPER | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:44:41 PM | BTC | UP | 19 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/5 8:44:41 PM | ZEC | DOWN | 19 sec | +0.061% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:44:41 PM | XRP | UP | 19 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/5 8:44:25 PM | HYPE | UP | 35 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/5 8:44:25 PM | ETH | UP | 35 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/5 8:44:09 PM | GBPUSD | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 8:44:09 PM | DOGE | UP | 51 sec | -0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:43:54 PM | BNB | UP | 65 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/5 8:43:54 PM | GOLD | UP | 65 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:43:37 PM | SOL | UP | 83 sec | -0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:43:37 PM | NEAR | DOWN | 83 sec | +0.261% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 8:42:16 PM | EURUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
