# 15-Minute 1¢ Study

*Updated Sun Oct 4, 7:25 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 562 finished bets | 1% | $23.40 | +39% | +4.16¢ | -$16.90 / $40.30 |

*Expect about **83 buys a day** (~$12.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1039 | $14.75 | +12% |
| 5+ min left, hold to the close | 191 | $13.80 | +49% |
| Momentum model ≥ 5%, hold to the close | 566 | $9.70 | +16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7832 | 7826 | 36 (0%) | 1.07% | -$432.75 (-46%) | Hold to the close: -$432.75 (-46%) |

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
| Volatility model | 5218 | 4.2% | 0.5% (24) | -605% | ❌ Worse |
| Momentum model | 5218 | 4.3% | 0.5% (24) | -636% | ❌ Worse |
| Mean-reversion model | 5218 | 6.9% | 0.5% (24) | -702% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5218 | 24 | -42% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1039 | 10 | +12% | -68% | -69% | -63% |
| Volatility model ≥ 5% | 562 | 6 | +39% | -55% | -54% | -49% |
| Volatility model ≥ 10% | 351 | 4 | +67% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 913 | 7 | -7% | -69% | -71% | -68% |
| Momentum model ≥ 5% | 566 | 5 | +16% | -60% | -63% | -60% |
| Momentum model ≥ 10% | 393 | 4 | +46% | -47% | -48% | -45% |
| Mean-reversion model ≥ 2% | 1832 | 13 | -23% | -82% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1231 | 11 | -1% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 813 | 8 | +14% | -77% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5415 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1838 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 573 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7826 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 36 | 0% | -$432.75 | -46% | — |
| Sell at 2¢ | 316 | 4% | -$826.59 | -88% | 33 sec |
| Sell at 3¢ | 204 | 3% | -$829.19 | -89% | 47 sec |
| Sell at 5¢ | 150 | 2% | -$811.25 | -87% | 61 sec |
| Sell at 10¢ | 104 | 1% | -$758.51 | -81% | 72 sec |
| Sell at 25¢ | 57 | 1% | -$678.08 | -72% | 1.6 min |
| Sell at 50¢ | 35 | 0% | -$588.50 | -63% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 188 | 3 | 12% | 3% | +51% | -78% | -87% |
| 2–5 min | 2520 | 19 | 8% | 4% | -26% | -86% | -86% |
| 1–2 min | 2063 | 9 | 3% | 2% | -52% | -93% | -93% |
| Under 1 min | 3052 | 5 | 1% | 0% | -75% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 611 | 5 | 5% | 3% | -3% | -88% | -89% |
| DOGE | 607 | 2 | 4% | 1% | -57% | -90% | -90% |
| HYPE | 605 | 3 | 5% | 3% | -39% | -88% | -85% |
| ETH | 604 | 5 | 6% | 3% | +4% | -86% | -85% |
| BNB | 600 | 2 | 4% | 2% | -60% | -90% | -92% |
| SOL | 599 | 0 | 3% | 1% | -100% | -93% | -91% |
| BTC | 597 | 3 | 6% | 2% | -34% | -86% | -90% |
| XRP | 597 | 4 | 2% | 1% | -14% | -75% | -75% |
| NEAR | 595 | 2 | 6% | 3% | -55% | -62% | -63% |
| GOLD | 311 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 296 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 284 | 2 | 3% | 1% | -25% | -94% | -96% |
| COPPER | 262 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 233 | 2 | 3% | 2% | -20% | -94% | -92% |
| PLATINUM | 230 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 222 | 1 | 2% | 1% | -58% | -96% | -98% |
| EURUSD | 203 | 1 | 5% | 3% | -54% | -91% | -90% |
| GBPUSD | 200 | 1 | 4% | 2% | -53% | -93% | -94% |
| USDJPY | 170 | 3 | 2% | 2% | +65% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3936 | 20 | 4% | 2% | -40% | -88% | -87% |
| DOWN (bought NO) | 3890 | 16 | 4% | 2% | -52% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 912 | 7 | 2% | 1% | +30% | -57% | -56% |
| 0.05–0.1% | 925 | 2 | 3% | 1% | -68% | -91% | -92% |
| 0.1–0.2% | 1339 | 5 | 4% | 2% | -52% | -90% | -91% |
| 0.2–0.5% | 1576 | 8 | 6% | 4% | -44% | -87% | -86% |
| Over 0.5% | 661 | 4 | 7% | 3% | -38% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2135 | 7 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,130 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 7:14:58 PM | ZEC | UP | 2 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:14:56 PM | COPPER | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:14:56 PM | NATGAS | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:14:56 PM | XRP | DOWN | 4 sec | +0.158% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:14:42 PM | ETH | UP | 18 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:14:42 PM | BNB | DOWN | 18 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:14:40 PM | PALLADIUM | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:14:12 PM | SOL | UP | 48 sec | -0.117% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:14:10 PM | USDJPY | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:13:55 PM | DOGE | DOWN | 64 sec | +0.265% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:13:25 PM | SILVER | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:13:05 PM | NEAR | UP | 1.9 min | -0.370% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:12:25 PM | GBPUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:12:11 PM | EURUSD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:11:41 PM | WTI | DOWN | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:10:57 PM | HYPE | UP | 4.0 min | -0.405% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:59:53 PM | HYPE | DOWN | 6 sec | -0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 6:59:31 PM | NEAR | DOWN | 28 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/4 6:59:29 PM | GOLD | DOWN | 30 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/4 6:59:15 PM | NATGAS | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 6:59:02 PM | BTC | DOWN | 57 sec | +0.104% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:58:43 PM | ZEC | DOWN | 77 sec | +0.237% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:58:41 PM | XRP | DOWN | 79 sec | +0.257% | 0¢ | ❌ Lost | $0.00 |
| 10/4 6:58:39 PM | COPPER | DOWN | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 6:58:31 PM | DOGE | DOWN | 89 sec | +0.231% | 0¢ | ❌ Lost | $0.00 |
| 10/4 6:58:25 PM | ETH | DOWN | 1.6 min | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:58:25 PM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 6:58:25 PM | SILVER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 6:57:58 PM | GBPUSD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 6:56:59 PM | WTI | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
