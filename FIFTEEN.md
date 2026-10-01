# 15-Minute 1¢ Study

*Updated Thu Oct 1, 2:10 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 142 finished bets | 1% | $7.15 | +34% | +5.04¢ | $17.35 / -$10.20 |

*Expect about **38 buys a day** (~$5.71/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 280 | -$2.60 | -8% |
| Volatility model ≥ 5%, sell at 25¢ | 270 | -$5.77 | -19% |
| Volatility model ≥ 5%, sell at 10¢ | 270 | -$6.53 | -22% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4616 | 4610 | 15 (0%) | 1.07% | -$356.10 (-63%) | Hold to the close: -$356.10 (-63%) |

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
| Volatility model | 2632 | 3.5% | 0.2% (6) | -670% | ❌ Worse |
| Momentum model | 2632 | 3.7% | 0.2% (6) | -726% | ❌ Worse |
| Mean-reversion model | 2632 | 6.6% | 0.2% (6) | -855% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2632 | 6 | -71% | -85% | -86% | -84% |
| Volatility model ≥ 2% | 536 | 3 | -36% | -63% | -65% | -61% |
| Volatility model ≥ 5% | 270 | 1 | -53% | -34% | -34% | -31% |
| Volatility model ≥ 10% | 154 | 1 | -4% | +14% | +12% | +19% |
| Momentum model ≥ 2% | 479 | 2 | -50% | -60% | -63% | -60% |
| Momentum model ≥ 5% | 280 | 2 | -8% | -40% | -43% | -37% |
| Momentum model ≥ 10% | 187 | 1 | -23% | -14% | -13% | -9% |
| Mean-reversion model ≥ 2% | 997 | 3 | -68% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 658 | 3 | -51% | -82% | -85% | -79% |
| Mean-reversion model ≥ 10% | 417 | 2 | -46% | -78% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2828 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1369 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 413 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 4610 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 15 | 0% | -$356.10 | -63% | — |
| Sell at 2¢ | 171 | 4% | -$507.64 | -90% | 47 sec |
| Sell at 3¢ | 102 | 2% | -$512.32 | -90% | 50 sec |
| Sell at 5¢ | 74 | 2% | -$504.00 | -89% | 66 sec |
| Sell at 10¢ | 53 | 1% | -$468.67 | -83% | 81 sec |
| Sell at 25¢ | 24 | 1% | -$444.66 | -79% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$415.10 | -73% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 139 | 2 | 13% | 3% | +37% | -77% | -89% |
| 2–5 min | 1525 | 7 | 7% | 3% | -55% | -88% | -89% |
| 1–2 min | 1198 | 4 | 3% | 2% | -65% | -94% | -93% |
| Under 1 min | 1745 | 2 | 1% | 0% | -83% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 320 | 1 | 4% | 1% | -59% | -90% | -92% |
| ETH | 317 | 2 | 5% | 3% | -23% | -88% | -86% |
| NEAR | 314 | 0 | 5% | 1% | -100% | -88% | -92% |
| ZEC | 314 | 1 | 5% | 2% | -62% | -89% | -94% |
| BNB | 314 | 0 | 4% | 1% | -100% | -91% | -94% |
| BTC | 313 | 0 | 7% | 3% | -100% | -84% | -88% |
| HYPE | 313 | 1 | 4% | 3% | -62% | -90% | -88% |
| XRP | 312 | 3 | 2% | 1% | +23% | -55% | -54% |
| SOL | 311 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 234 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 218 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 208 | 1 | 3% | 1% | -50% | -94% | -96% |
| COPPER | 195 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 180 | 1 | 4% | 2% | -48% | -93% | -91% |
| PLATINUM | 170 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 164 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 146 | 1 | 5% | 2% | -36% | -92% | -93% |
| EURUSD | 145 | 1 | 3% | 1% | -36% | -94% | -95% |
| USDJPY | 122 | 3 | 3% | 2% | +130% | -94% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2346 | 9 | 4% | 2% | -56% | -92% | -92% |
| DOWN (bought NO) | 2264 | 6 | 4% | 1% | -70% | -87% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 327 | 1 | 1% | 1% | -43% | -38% | -38% |
| 0.05–0.1% | 395 | 0 | 2% | 0% | -100% | -94% | -96% |
| 0.1–0.2% | 674 | 1 | 4% | 1% | -81% | -91% | -91% |
| 0.2–0.5% | 961 | 2 | 6% | 3% | -77% | -89% | -89% |
| Over 0.5% | 470 | 4 | 7% | 2% | -12% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 896 | 2 | 3% | 1% | -74% | -81% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,184 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 1:59:46 PM | EURUSD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 1:59:46 PM | BTC | DOWN | 13 sec | +0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/1 1:59:46 PM | PLATINUM | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 1:59:30 PM | ZEC | DOWN | 29 sec | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 1:59:30 PM | COPPER | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 1:59:14 PM | GBPUSD | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 1:59:00 PM | ETH | DOWN | 60 sec | +0.062% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 1:59:00 PM | DOGE | DOWN | 60 sec | +0.220% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 1:58:44 PM | SOL | DOWN | 75 sec | +0.148% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 1:58:44 PM | BNB | DOWN | 75 sec | +0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/1 1:58:44 PM | NATGAS | DOWN | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 1:58:44 PM | XRP | DOWN | 75 sec | +0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 1:58:44 PM | HYPE | DOWN | 75 sec | +0.312% | 0¢ | ❌ Lost | $0.00 |
| 10/1 1:58:44 PM | WTI | DOWN | 75 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 1:58:44 PM | NEAR | DOWN | 75 sec | +0.445% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 1:44:54 PM | EURUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 1:44:54 PM | PALLADIUM | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 1:44:54 PM | NATGAS | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 1:44:54 PM | COPPER | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 1:44:38 PM | BTC | DOWN | 22 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/1 1:44:38 PM | PLATINUM | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 1:43:50 PM | DOGE | DOWN | 70 sec | +0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 1:43:34 PM | BNB | DOWN | 86 sec | +0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/1 1:43:34 PM | XRP | DOWN | 86 sec | +0.161% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 1:43:02 PM | ETH | DOWN | 2.0 min | +0.113% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 1:43:02 PM | NEAR | DOWN | 2.0 min | +0.731% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 1:42:46 PM | SOL | DOWN | 2.2 min | +0.243% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 1:41:42 PM | ZEC | DOWN | 3.3 min | +0.758% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 12:29:59 PM | NEAR | UP | 1 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/1 12:29:59 PM | ETH | UP | 1 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
