# 15-Minute 1¢ Study

*Updated Thu Oct 1, 6:23 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 143 finished bets | 1% | $7.00 | +33% | +4.90¢ | $17.35 / -$10.35 |

*Expect about **37 buys a day** (~$5.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 298 | -$4.55 | -14% |
| 5+ min left, sell at 50¢ | 143 | -$7.50 | -36% |
| Volatility model ≥ 5%, sell at 25¢ | 289 | -$7.87 | -25% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4831 | 4825 | 15 (0%) | 1.07% | -$379.80 (-64%) | Hold to the close: -$379.80 (-64%) |

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
| Volatility model | 2776 | 3.6% | 0.2% (6) | -693% | ❌ Worse |
| Momentum model | 2776 | 3.7% | 0.2% (6) | -749% | ❌ Worse |
| Mean-reversion model | 2776 | 6.6% | 0.2% (6) | -884% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2776 | 6 | -73% | -85% | -87% | -84% |
| Volatility model ≥ 2% | 575 | 3 | -41% | -64% | -66% | -63% |
| Volatility model ≥ 5% | 289 | 1 | -56% | -37% | -38% | -36% |
| Volatility model ≥ 10% | 164 | 1 | -10% | +6% | +5% | +11% |
| Momentum model ≥ 2% | 515 | 2 | -54% | -62% | -65% | -63% |
| Momentum model ≥ 5% | 298 | 2 | -14% | -43% | -45% | -41% |
| Momentum model ≥ 10% | 200 | 1 | -29% | -19% | -19% | -16% |
| Mean-reversion model ≥ 2% | 1053 | 3 | -69% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 693 | 3 | -53% | -82% | -85% | -80% |
| Mean-reversion model ≥ 10% | 440 | 2 | -49% | -78% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2972 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1419 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 434 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 4825 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 15 | 0% | -$379.80 | -64% | — |
| Sell at 2¢ | 177 | 4% | -$529.78 | -90% | 45 sec |
| Sell at 3¢ | 106 | 2% | -$534.46 | -91% | 49 sec |
| Sell at 5¢ | 77 | 2% | -$525.75 | -89% | 66 sec |
| Sell at 10¢ | 56 | 1% | -$488.44 | -83% | 81 sec |
| Sell at 25¢ | 26 | 1% | -$461.74 | -78% | 1.6 min |
| Sell at 50¢ | 13 | 0% | -$432.05 | -73% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 140 | 2 | 13% | 3% | +36% | -77% | -89% |
| 2–5 min | 1588 | 7 | 7% | 3% | -57% | -88% | -89% |
| 1–2 min | 1271 | 4 | 3% | 2% | -66% | -94% | -93% |
| Under 1 min | 1823 | 2 | 1% | 0% | -84% | -90% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 336 | 1 | 4% | 1% | -61% | -91% | -92% |
| ETH | 332 | 2 | 5% | 3% | -26% | -88% | -86% |
| ZEC | 331 | 1 | 5% | 2% | -64% | -89% | -94% |
| BNB | 331 | 0 | 4% | 1% | -100% | -91% | -94% |
| HYPE | 330 | 1 | 5% | 3% | -63% | -90% | -88% |
| BTC | 329 | 0 | 6% | 3% | -100% | -85% | -88% |
| NEAR | 328 | 0 | 5% | 2% | -100% | -86% | -91% |
| XRP | 328 | 3 | 2% | 1% | +19% | -57% | -56% |
| SOL | 327 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 244 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 227 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 218 | 1 | 3% | 1% | -52% | -95% | -96% |
| COPPER | 203 | 0 | 1% | 0% | -100% | -98% | -99% |
| NATGAS | 184 | 1 | 4% | 2% | -49% | -93% | -92% |
| PLATINUM | 177 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 166 | 0 | 2% | 1% | -100% | -97% | -98% |
| EURUSD | 154 | 1 | 4% | 2% | -39% | -93% | -93% |
| GBPUSD | 152 | 1 | 5% | 2% | -39% | -92% | -93% |
| USDJPY | 128 | 3 | 3% | 2% | +119% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2447 | 9 | 4% | 2% | -58% | -92% | -92% |
| DOWN (bought NO) | 2378 | 6 | 4% | 1% | -71% | -87% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 353 | 1 | 1% | 1% | -47% | -43% | -42% |
| 0.05–0.1% | 423 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 719 | 1 | 4% | 1% | -82% | -91% | -92% |
| 0.2–0.5% | 999 | 2 | 6% | 3% | -78% | -88% | -89% |
| Over 0.5% | 477 | 4 | 7% | 2% | -13% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1327 | 4 | 3% | 2% | -65% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,193 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 6:14:54 PM | BTC | DOWN | 6 sec | +0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/1 6:14:52 PM | BNB | DOWN | 8 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 10/1 6:14:40 PM | HYPE | DOWN | 20 sec | +0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/1 6:14:32 PM | DOGE | UP | 28 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/1 6:14:28 PM | XRP | DOWN | 32 sec | +0.074% | 0¢ | ❌ Lost | $0.00 |
| 10/1 6:13:57 PM | NEAR | DOWN | 63 sec | +0.185% | 0¢ | ❌ Lost | $0.00 |
| 10/1 6:13:55 PM | GBPUSD | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:13:39 PM | ZEC | DOWN | 81 sec | +0.319% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:13:32 PM | EURUSD | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:13:18 PM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:12:51 PM | PLATINUM | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:12:49 PM | GOLD | UP | 2.2 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 6:12:07 PM | USDJPY | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 6:11:31 PM | SILVER | UP | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 5:59:45 PM | EURUSD | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:59:35 PM | COPPER | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:59:31 PM | ETH | DOWN | 28 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/1 5:59:29 PM | HYPE | DOWN | 30 sec | +0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/1 5:59:29 PM | NATGAS | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:59:25 PM | SOL | DOWN | 34 sec | +0.032% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:59:23 PM | BTC | DOWN | 36 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/1 5:59:13 PM | XRP | DOWN | 46 sec | +0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/1 5:59:06 PM | DOGE | DOWN | 54 sec | +0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 5:58:58 PM | GOLD | DOWN | 61 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 5:58:44 PM | SILVER | DOWN | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:58:10 PM | ZEC | UP | 1.8 min | -0.407% | 0¢ | ❌ Lost | $0.00 |
| 10/1 5:58:08 PM | PALLADIUM | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:57:11 PM | PLATINUM | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:56:51 PM | BNB | DOWN | 3.1 min | +0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 5:55:14 PM | NEAR | DOWN | 4.8 min | +0.327% | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
