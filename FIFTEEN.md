# 15-Minute 1¢ Study

*Updated Tue Sep 29, 8:24 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 79 finished bets | 3% | $16.15 | +136% | +20.44¢ | $22.15 / -$6.00 |

*Expect about **40 buys a day** (~$5.96/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 79 | $1.65 | +14% |
| Mean-reversion model ≥ 5%, hold to the close | 337 | -$2.25 | -5% |
| Volatility model ≥ 5%, sell at 25¢ | 121 | -$2.67 | -21% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2544 | 2538 | 10 (0%) | 1.07% | -$168.55 (-55%) | Hold to the close: -$168.55 (-55%) |

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
| Volatility model | 1395 | 2.8% | 0.3% (4) | -471% | ❌ Worse |
| Momentum model | 1395 | 3.0% | 0.3% (4) | -533% | ❌ Worse |
| Mean-reversion model | 1395 | 5.7% | 0.3% (4) | -578% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1395 | 4 | -64% | -90% | -91% | -89% |
| Volatility model ≥ 2% | 269 | 1 | -57% | -86% | -88% | -86% |
| Volatility model ≥ 5% | 121 | 0 | -100% | -75% | -75% | -69% |
| Volatility model ≥ 10% | 66 | 0 | -100% | -74% | -74% | -68% |
| Momentum model ≥ 2% | 232 | 0 | -100% | -87% | -90% | -91% |
| Momentum model ≥ 5% | 132 | 0 | -100% | -84% | -89% | -87% |
| Momentum model ≥ 10% | 84 | 0 | -100% | -87% | -86% | -84% |
| Mean-reversion model ≥ 2% | 514 | 3 | -38% | -86% | -87% | -84% |
| Mean-reversion model ≥ 5% | 337 | 3 | -5% | -84% | -84% | -78% |
| Mean-reversion model ≥ 10% | 208 | 2 | +7% | -79% | -82% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1591 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 775 | 2% | 1% | 1% | 0% | 0% | 0% |
| Financials | 172 | 5% | 3% | 2% | 2% | 2% | 1% |
| **All** | 2538 | 4% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$168.55 | -55% | — |
| Sell at 2¢ | 90 | 4% | -$285.15 | -92% | 34 sec |
| Sell at 3¢ | 55 | 2% | -$287.10 | -93% | 47 sec |
| Sell at 5¢ | 38 | 1% | -$283.85 | -92% | 65 sec |
| Sell at 10¢ | 31 | 1% | -$253.94 | -82% | 1.6 min |
| Sell at 25¢ | 16 | 1% | -$241.59 | -78% | 1.9 min |
| Sell at 50¢ | 9 | 0% | -$219.80 | -71% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 79 | 2 | 11% | 3% | +136% | -80% | -87% |
| 2–5 min | 846 | 5 | 6% | 3% | -43% | -89% | -90% |
| 1–2 min | 680 | 2 | 3% | 1% | -68% | -94% | -94% |
| Under 1 min | 933 | 1 | 1% | 0% | -84% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 180 | 1 | 4% | 2% | -27% | -91% | -90% |
| ZEC | 179 | 1 | 5% | 2% | -33% | -89% | -93% |
| ETH | 178 | 2 | 4% | 3% | +39% | -90% | -86% |
| NEAR | 177 | 0 | 6% | 1% | -100% | -86% | -90% |
| XRP | 177 | 2 | 2% | 2% | +46% | -95% | -94% |
| BTC | 176 | 0 | 7% | 2% | -100% | -84% | -90% |
| SOL | 176 | 0 | 3% | 2% | -100% | -91% | -89% |
| HYPE | 174 | 0 | 3% | 2% | -100% | -92% | -92% |
| BNB | 174 | 0 | 2% | 1% | -100% | -96% | -96% |
| GOLD | 139 | 0 | 4% | 1% | -100% | -90% | -93% |
| WTI | 122 | 0 | 2% | 1% | -100% | -95% | -98% |
| SILVER | 122 | 0 | 2% | 1% | -100% | -95% | -95% |
| COPPER | 113 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 105 | 0 | 3% | 1% | -100% | -95% | -93% |
| PLATINUM | 90 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 84 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 65 | 1 | 5% | 2% | +44% | -92% | -92% |
| EURUSD | 57 | 1 | 5% | 2% | +64% | -91% | -95% |
| USDJPY | 50 | 2 | 4% | 4% | +273% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1333 | 7 | 4% | 2% | -40% | -92% | -92% |
| DOWN (bought NO) | 1205 | 3 | 3% | 1% | -71% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 167 | 0 | 2% | 1% | -100% | -93% | -93% |
| 0.05–0.1% | 204 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 369 | 0 | 4% | 1% | -100% | -91% | -93% |
| 0.2–0.5% | 584 | 2 | 5% | 3% | -63% | -90% | -91% |
| Over 0.5% | 266 | 4 | 6% | 3% | +56% | -88% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 731 | 2 | 4% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,720 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 8:14:58 PM | EURUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:14:41 PM | COPPER | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:14:41 PM | GBPUSD | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:14:25 PM | SILVER | DOWN | 35 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:14:09 PM | HYPE | UP | 51 sec | -0.185% | 0¢ | ❌ Lost | $0.00 |
| 9/29 8:14:09 PM | PLATINUM | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:14:09 PM | USDJPY | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:13:54 PM | PALLADIUM | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:13:54 PM | BTC | DOWN | 65 sec | +0.086% | 0¢ | ❌ Lost | $0.00 |
| 9/29 8:13:39 PM | DOGE | DOWN | 80 sec | +0.231% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:13:39 PM | WTI | UP | 80 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:13:39 PM | NATGAS | UP | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:13:23 PM | XRP | DOWN | 1.6 min | +0.314% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:12:51 PM | SOL | DOWN | 2.1 min | +0.196% | 2¢ | ❌ Lost | -$0.15 |
| 9/29 8:12:51 PM | NEAR | UP | 2.1 min | -0.694% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:12:51 PM | BNB | DOWN | 2.1 min | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:12:18 PM | ZEC | UP | 2.7 min | -0.344% | 25¢ | ❌ Lost | -$0.15 |
| 9/29 8:12:18 PM | GOLD | DOWN | 2.7 min | — | 3¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
