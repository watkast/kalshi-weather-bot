# 15-Minute 1¢ Study

*Updated Tue Sep 29, 8:04 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 79 finished bets | 3% | $16.15 | +136% | +20.44¢ | $22.15 / -$6.00 |

*Expect about **40 buys a day** (~$6.00/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 79 | $1.65 | +14% |
| Mean-reversion model ≥ 5%, hold to the close | 335 | -$1.95 | -4% |
| Volatility model ≥ 5%, sell at 25¢ | 120 | -$2.52 | -20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2526 | 2520 | 10 (0%) | 1.07% | -$166.15 (-54%) | Hold to the close: -$166.15 (-54%) |

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
| Volatility model | 1387 | 2.8% | 0.3% (4) | -472% | ❌ Worse |
| Momentum model | 1387 | 3.0% | 0.3% (4) | -534% | ❌ Worse |
| Mean-reversion model | 1387 | 5.7% | 0.3% (4) | -578% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1387 | 4 | -63% | -91% | -92% | -89% |
| Volatility model ≥ 2% | 268 | 1 | -57% | -86% | -88% | -86% |
| Volatility model ≥ 5% | 120 | 0 | -100% | -75% | -75% | -69% |
| Volatility model ≥ 10% | 65 | 0 | -100% | -73% | -73% | -67% |
| Momentum model ≥ 2% | 231 | 0 | -100% | -87% | -90% | -91% |
| Momentum model ≥ 5% | 132 | 0 | -100% | -84% | -89% | -87% |
| Momentum model ≥ 10% | 84 | 0 | -100% | -87% | -86% | -84% |
| Mean-reversion model ≥ 2% | 512 | 3 | -37% | -86% | -88% | -84% |
| Mean-reversion model ≥ 5% | 335 | 3 | -4% | -84% | -85% | -79% |
| Mean-reversion model ≥ 10% | 207 | 2 | +8% | -79% | -82% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1583 | 4% | 2% | 2% | 2% | 1% | 0% |
| Commodities | 768 | 2% | 1% | 1% | 0% | 0% | 0% |
| Financials | 169 | 5% | 3% | 2% | 2% | 2% | 1% |
| **All** | 2520 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$166.15 | -54% | — |
| Sell at 2¢ | 88 | 3% | -$283.27 | -93% | 34 sec |
| Sell at 3¢ | 53 | 2% | -$285.48 | -93% | 47 sec |
| Sell at 5¢ | 37 | 1% | -$282.10 | -92% | 64 sec |
| Sell at 10¢ | 30 | 1% | -$252.85 | -83% | 1.6 min |
| Sell at 25¢ | 15 | 1% | -$242.50 | -79% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$217.40 | -71% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 79 | 2 | 11% | 3% | +136% | -80% | -87% |
| 2–5 min | 841 | 5 | 6% | 3% | -42% | -89% | -90% |
| 1–2 min | 674 | 2 | 3% | 1% | -68% | -94% | -94% |
| Under 1 min | 926 | 1 | 1% | 0% | -83% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 179 | 1 | 4% | 2% | -27% | -90% | -90% |
| ETH | 178 | 2 | 4% | 3% | +39% | -90% | -86% |
| ZEC | 178 | 1 | 4% | 2% | -33% | -90% | -94% |
| NEAR | 176 | 0 | 6% | 1% | -100% | -86% | -90% |
| XRP | 176 | 2 | 2% | 2% | +47% | -95% | -94% |
| BTC | 175 | 0 | 7% | 2% | -100% | -84% | -90% |
| SOL | 175 | 0 | 3% | 2% | -100% | -91% | -89% |
| HYPE | 173 | 0 | 3% | 2% | -100% | -92% | -92% |
| BNB | 173 | 0 | 2% | 1% | -100% | -96% | -96% |
| GOLD | 138 | 0 | 4% | 1% | -100% | -92% | -95% |
| WTI | 121 | 0 | 2% | 1% | -100% | -95% | -98% |
| SILVER | 121 | 0 | 2% | 1% | -100% | -95% | -95% |
| COPPER | 112 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 104 | 0 | 3% | 1% | -100% | -95% | -92% |
| PLATINUM | 89 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 83 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 64 | 1 | 5% | 2% | +46% | -92% | -92% |
| EURUSD | 56 | 1 | 5% | 2% | +67% | -91% | -95% |
| USDJPY | 49 | 2 | 4% | 4% | +281% | -93% | -89% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1325 | 7 | 4% | 2% | -39% | -92% | -93% |
| DOWN (bought NO) | 1195 | 3 | 3% | 1% | -71% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 167 | 0 | 2% | 1% | -100% | -93% | -93% |
| 0.05–0.1% | 202 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 367 | 0 | 4% | 1% | -100% | -91% | -93% |
| 0.2–0.5% | 581 | 2 | 5% | 3% | -63% | -90% | -91% |
| Over 0.5% | 265 | 4 | 6% | 3% | +57% | -88% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 713 | 2 | 4% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,720 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 7:59:56 PM | GBPUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:59:56 PM | PALLADIUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:59:56 PM | BTC | DOWN | 3 sec | +0.006% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:59:56 PM | USDJPY | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:59:41 PM | SOL | UP | 18 sec | -0.017% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:59:41 PM | NATGAS | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:59:41 PM | XRP | UP | 18 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:59:25 PM | BNB | DOWN | 34 sec | +0.038% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:59:09 PM | HYPE | UP | 50 sec | -0.091% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:59:09 PM | DOGE | UP | 50 sec | -0.111% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:58:53 PM | NEAR | UP | 67 sec | -0.411% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:58:06 PM | GOLD | DOWN | 1.9 min | — | 7¢ | ❌ Lost | -$0.15 |
| 9/29 7:57:33 PM | EURUSD | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:57:01 PM | ZEC | UP | 3.0 min | -0.350% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:44:55 PM | EURUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:44:55 PM | DOGE | UP | 5 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:44:40 PM | XRP | DOWN | 20 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:44:40 PM | BTC | UP | 20 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:44:40 PM | GBPUSD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:44:40 PM | GOLD | DOWN | 20 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:44:24 PM | PLATINUM | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:44:24 PM | ETH | UP | 36 sec | -0.059% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:44:08 PM | SOL | DOWN | 52 sec | +0.162% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:44:08 PM | ZEC | DOWN | 52 sec | +0.220% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:44:08 PM | HYPE | DOWN | 52 sec | +0.090% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:43:35 PM | BNB | UP | 85 sec | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:43:35 PM | COPPER | UP | 85 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:43:03 PM | NATGAS | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:43:03 PM | PALLADIUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:42:48 PM | WTI | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
