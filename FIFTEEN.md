# 15-Minute 1¢ Study

*Updated Mon Oct 5, 9:18 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 625 finished bets | 1% | $30.80 | +46% | +4.93¢ | -$6.35 / $37.15 |

*Expect about **80 buys a day** (~$11.93/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 625 | $17.40 | +26% |
| Volatility model ≥ 2%, hold to the close | 1163 | $13.90 | +10% |
| Mean-reversion model ≥ 5%, hold to the close | 1383 | $8.15 | +5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9130 | 9124 | 39 (0%) | 1.07% | -$552.15 (-50%) | Hold to the close: -$552.15 (-50%) |

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
| Volatility model | 5984 | 4.1% | 0.5% (27) | -580% | ❌ Worse |
| Momentum model | 5984 | 4.1% | 0.5% (27) | -605% | ❌ Worse |
| Mean-reversion model | 5984 | 6.7% | 0.5% (27) | -679% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5984 | 27 | -43% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 1163 | 11 | +10% | -70% | -70% | -66% |
| Volatility model ≥ 5% | 625 | 7 | +46% | -57% | -57% | -53% |
| Volatility model ≥ 10% | 385 | 5 | +94% | -38% | -40% | -34% |
| Momentum model ≥ 2% | 1029 | 9 | +6% | -71% | -73% | -71% |
| Momentum model ≥ 5% | 625 | 6 | +26% | -63% | -65% | -62% |
| Momentum model ≥ 10% | 431 | 5 | +67% | -50% | -51% | -48% |
| Mean-reversion model ≥ 2% | 2057 | 15 | -20% | -83% | -83% | -79% |
| Mean-reversion model ≥ 5% | 1383 | 13 | +5% | -80% | -79% | -73% |
| Mean-reversion model ≥ 10% | 912 | 9 | +14% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6181 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2227 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 716 | 3% | 3% | 2% | 2% | 1% | 0% |
| **All** | 9124 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 39 | 0% | -$552.15 | -50% | — |
| Sell at 2¢ | 342 | 4% | -$981.23 | -89% | 33 sec |
| Sell at 3¢ | 224 | 2% | -$982.79 | -89% | 47 sec |
| Sell at 5¢ | 165 | 2% | -$962.90 | -88% | 61 sec |
| Sell at 10¢ | 111 | 1% | -$910.74 | -83% | 66 sec |
| Sell at 25¢ | 61 | 1% | -$826.24 | -75% | 83 sec |
| Sell at 50¢ | 38 | 0% | -$729.65 | -66% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 233 | 3 | 10% | 3% | +22% | -82% | -89% |
| 2–5 min | 2945 | 21 | 7% | 3% | -30% | -87% | -87% |
| 1–2 min | 2406 | 10 | 3% | 2% | -55% | -93% | -93% |
| Under 1 min | 3537 | 5 | 1% | 0% | -79% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 699 | 5 | 5% | 3% | -15% | -89% | -89% |
| DOGE | 690 | 2 | 4% | 1% | -63% | -91% | -91% |
| HYPE | 690 | 3 | 5% | 3% | -47% | -88% | -86% |
| ETH | 689 | 6 | 6% | 3% | +10% | -87% | -86% |
| BNB | 686 | 2 | 4% | 2% | -65% | -91% | -92% |
| XRP | 683 | 4 | 1% | 1% | -25% | -78% | -78% |
| BTC | 682 | 3 | 5% | 2% | -42% | -87% | -90% |
| SOL | 682 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 680 | 4 | 6% | 3% | -23% | -66% | -66% |
| GOLD | 374 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 359 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 341 | 2 | 3% | 1% | -37% | -95% | -96% |
| COPPER | 317 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 284 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 279 | 2 | 3% | 2% | -33% | -94% | -93% |
| PALLADIUM | 273 | 1 | 2% | 1% | -66% | -97% | -98% |
| EURUSD | 259 | 1 | 4% | 3% | -64% | -93% | -91% |
| GBPUSD | 245 | 1 | 4% | 2% | -62% | -94% | -94% |
| USDJPY | 212 | 3 | 2% | 1% | +32% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4630 | 21 | 4% | 2% | -47% | -89% | -88% |
| DOWN (bought NO) | 4494 | 18 | 4% | 2% | -54% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1018 | 7 | 2% | 1% | +18% | -61% | -60% |
| 0.05–0.1% | 1056 | 3 | 3% | 1% | -58% | -91% | -92% |
| 0.1–0.2% | 1548 | 6 | 4% | 2% | -51% | -91% | -91% |
| 0.2–0.5% | 1812 | 9 | 6% | 3% | -45% | -88% | -87% |
| Over 0.5% | 745 | 4 | 7% | 3% | -45% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2592 | 7 | 3% | 1% | -69% | -94% | -94% |

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
| 10/5 9:14:49 PM | DOGE | UP | 11 sec | -0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:14:33 PM | SOL | UP | 27 sec | -0.042% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:14:17 PM | ZEC | UP | 43 sec | -0.151% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:14:17 PM | XRP | DOWN | 43 sec | +0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:14:01 PM | USDJPY | DOWN | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:13:45 PM | GBPUSD | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:13:45 PM | ETH | UP | 74 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:13:29 PM | NEAR | UP | 1.5 min | -0.390% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:13:29 PM | EURUSD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:13:13 PM | BNB | DOWN | 1.8 min | +0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:13:13 PM | COPPER | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:12:41 PM | HYPE | UP | 2.3 min | -0.217% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
