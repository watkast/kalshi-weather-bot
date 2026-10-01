# 15-Minute 1¢ Study

*Updated Thu Oct 1, 2:20 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 142 finished bets | 1% | $7.15 | +34% | +5.04¢ | $17.35 / -$10.20 |

*Expect about **38 buys a day** (~$5.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 283 | -$3.05 | -10% |
| Volatility model ≥ 5%, sell at 25¢ | 272 | -$6.07 | -20% |
| Volatility model ≥ 5%, sell at 10¢ | 272 | -$6.83 | -23% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4631 | 4625 | 15 (0%) | 1.07% | -$358.05 (-63%) | Hold to the close: -$358.05 (-63%) |

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
| Volatility model | 2641 | 3.5% | 0.2% (6) | -670% | ❌ Worse |
| Momentum model | 2641 | 3.7% | 0.2% (6) | -727% | ❌ Worse |
| Mean-reversion model | 2641 | 6.6% | 0.2% (6) | -854% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2641 | 6 | -71% | -85% | -86% | -84% |
| Volatility model ≥ 2% | 539 | 3 | -37% | -63% | -64% | -60% |
| Volatility model ≥ 5% | 272 | 1 | -53% | -34% | -35% | -32% |
| Volatility model ≥ 10% | 156 | 1 | -6% | +12% | +10% | +16% |
| Momentum model ≥ 2% | 484 | 2 | -51% | -60% | -64% | -61% |
| Momentum model ≥ 5% | 283 | 2 | -10% | -41% | -44% | -38% |
| Momentum model ≥ 10% | 189 | 1 | -25% | -15% | -14% | -11% |
| Mean-reversion model ≥ 2% | 1000 | 3 | -68% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 660 | 3 | -51% | -82% | -85% | -79% |
| Mean-reversion model ≥ 10% | 419 | 2 | -47% | -78% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2837 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1374 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 414 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 4625 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 15 | 0% | -$358.05 | -63% | — |
| Sell at 2¢ | 172 | 4% | -$509.33 | -90% | 46 sec |
| Sell at 3¢ | 103 | 2% | -$513.88 | -90% | 49 sec |
| Sell at 5¢ | 75 | 2% | -$505.30 | -89% | 66 sec |
| Sell at 10¢ | 54 | 1% | -$469.31 | -83% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$446.61 | -79% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$417.05 | -73% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 139 | 2 | 13% | 3% | +37% | -77% | -89% |
| 2–5 min | 1528 | 7 | 7% | 3% | -56% | -88% | -89% |
| 1–2 min | 1204 | 4 | 3% | 2% | -65% | -94% | -93% |
| Under 1 min | 1751 | 2 | 1% | 0% | -83% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 321 | 1 | 4% | 1% | -60% | -90% | -92% |
| ETH | 318 | 2 | 5% | 3% | -23% | -88% | -86% |
| NEAR | 315 | 0 | 5% | 2% | -100% | -88% | -91% |
| ZEC | 315 | 1 | 5% | 2% | -62% | -89% | -94% |
| BNB | 315 | 0 | 4% | 1% | -100% | -91% | -94% |
| BTC | 314 | 0 | 7% | 3% | -100% | -84% | -88% |
| HYPE | 314 | 1 | 4% | 3% | -62% | -90% | -88% |
| XRP | 313 | 3 | 2% | 1% | +23% | -55% | -55% |
| SOL | 312 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 235 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 219 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 209 | 1 | 3% | 1% | -50% | -94% | -96% |
| COPPER | 195 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 181 | 1 | 4% | 2% | -48% | -93% | -91% |
| PLATINUM | 171 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 164 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 146 | 1 | 5% | 2% | -36% | -92% | -93% |
| EURUSD | 146 | 1 | 3% | 1% | -36% | -94% | -95% |
| USDJPY | 122 | 3 | 3% | 2% | +130% | -94% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2349 | 9 | 4% | 2% | -56% | -92% | -92% |
| DOWN (bought NO) | 2276 | 6 | 4% | 1% | -70% | -87% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 329 | 1 | 1% | 1% | -43% | -39% | -39% |
| 0.05–0.1% | 397 | 0 | 2% | 0% | -100% | -94% | -96% |
| 0.1–0.2% | 677 | 1 | 4% | 1% | -81% | -91% | -91% |
| 0.2–0.5% | 963 | 2 | 6% | 3% | -77% | -89% | -89% |
| Over 0.5% | 470 | 4 | 7% | 2% | -12% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 911 | 2 | 3% | 1% | -75% | -81% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,188 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 2:14:49 PM | GOLD | DOWN | 10 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 2:14:33 PM | SILVER | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:14:33 PM | HYPE | DOWN | 26 sec | +0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:14:17 PM | ETH | DOWN | 42 sec | +0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/1 2:14:17 PM | PLATINUM | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:14:01 PM | NATGAS | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:13:45 PM | XRP | DOWN | 74 sec | +0.167% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:13:45 PM | DOGE | DOWN | 74 sec | +0.067% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 2:13:29 PM | ZEC | DOWN | 1.5 min | +0.463% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:13:29 PM | SOL | DOWN | 1.5 min | +0.155% | 0¢ | ❌ Lost | $0.00 |
| 10/1 2:13:13 PM | WTI | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:13:13 PM | NEAR | UP | 1.8 min | -0.473% | 14¢ | ❌ Lost | -$0.15 |
| 10/1 2:12:41 PM | BNB | DOWN | 2.3 min | +0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 2:12:25 PM | EURUSD | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 2:12:25 PM | BTC | DOWN | 2.6 min | +0.127% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
