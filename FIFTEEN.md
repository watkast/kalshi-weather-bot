# 15-Minute 1¢ Study

*Updated Sun Oct 4, 10:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 570 finished bets | 1% | $22.65 | +37% | +3.97¢ | -$17.35 / $40.00 |

*Expect about **82 buys a day** (~$12.35/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1048 | $13.85 | +11% |
| 5+ min left, hold to the close | 195 | $13.20 | +46% |
| Momentum model ≥ 5%, hold to the close | 574 | $8.95 | +15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8025 | 8019 | 36 (0%) | 1.07% | -$457.80 (-48%) | Hold to the close: -$457.80 (-48%) |

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
| Volatility model | 5327 | 4.2% | 0.5% (24) | -612% | ❌ Worse |
| Momentum model | 5327 | 4.3% | 0.5% (24) | -643% | ❌ Worse |
| Mean-reversion model | 5327 | 6.9% | 0.5% (24) | -709% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5327 | 24 | -43% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1048 | 10 | +11% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 570 | 6 | +37% | -55% | -54% | -50% |
| Volatility model ≥ 10% | 355 | 4 | +66% | -36% | -38% | -32% |
| Momentum model ≥ 2% | 925 | 7 | -8% | -69% | -72% | -69% |
| Momentum model ≥ 5% | 574 | 5 | +15% | -61% | -64% | -60% |
| Momentum model ≥ 10% | 398 | 4 | +44% | -48% | -49% | -46% |
| Mean-reversion model ≥ 2% | 1849 | 13 | -23% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1242 | 11 | -2% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 821 | 8 | +13% | -77% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5524 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1893 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 602 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8019 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 36 | 0% | -$457.80 | -48% | — |
| Sell at 2¢ | 318 | 4% | -$851.12 | -88% | 33 sec |
| Sell at 3¢ | 206 | 3% | -$853.46 | -89% | 47 sec |
| Sell at 5¢ | 152 | 2% | -$835.00 | -87% | 61 sec |
| Sell at 10¢ | 104 | 1% | -$783.56 | -81% | 72 sec |
| Sell at 25¢ | 57 | 1% | -$703.13 | -73% | 1.6 min |
| Sell at 50¢ | 35 | 0% | -$613.55 | -64% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 192 | 3 | 12% | 3% | +48% | -79% | -88% |
| 2–5 min | 2581 | 19 | 8% | 4% | -28% | -86% | -86% |
| 1–2 min | 2127 | 9 | 3% | 2% | -54% | -93% | -93% |
| Under 1 min | 3116 | 5 | 1% | 0% | -76% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 624 | 5 | 5% | 3% | -5% | -89% | -89% |
| DOGE | 618 | 2 | 4% | 1% | -58% | -91% | -91% |
| ETH | 617 | 5 | 6% | 3% | +2% | -86% | -86% |
| HYPE | 615 | 3 | 5% | 3% | -40% | -88% | -86% |
| BNB | 613 | 2 | 4% | 2% | -61% | -91% | -92% |
| SOL | 612 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 610 | 3 | 6% | 2% | -35% | -86% | -89% |
| XRP | 610 | 4 | 2% | 1% | -16% | -75% | -76% |
| NEAR | 605 | 2 | 6% | 3% | -56% | -63% | -64% |
| GOLD | 320 | 0 | 4% | 1% | -100% | -90% | -93% |
| SILVER | 306 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 293 | 2 | 3% | 1% | -28% | -95% | -96% |
| COPPER | 271 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 238 | 2 | 3% | 2% | -22% | -94% | -92% |
| PLATINUM | 236 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 229 | 1 | 2% | 1% | -59% | -96% | -98% |
| EURUSD | 216 | 1 | 5% | 3% | -57% | -92% | -90% |
| GBPUSD | 207 | 1 | 4% | 2% | -55% | -93% | -94% |
| USDJPY | 179 | 3 | 2% | 2% | +56% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4056 | 20 | 4% | 2% | -42% | -88% | -88% |
| DOWN (bought NO) | 3963 | 16 | 4% | 2% | -53% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 925 | 7 | 2% | 1% | +28% | -57% | -57% |
| 0.05–0.1% | 937 | 2 | 4% | 1% | -69% | -90% | -92% |
| 0.1–0.2% | 1365 | 5 | 4% | 2% | -53% | -90% | -91% |
| 0.2–0.5% | 1623 | 8 | 6% | 3% | -45% | -87% | -87% |
| Over 0.5% | 672 | 4 | 7% | 3% | -39% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2328 | 7 | 3% | 2% | -65% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,170 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 10:44:36 PM | BNB | DOWN | 24 sec | +0.005% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:44:04 PM | COPPER | DOWN | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:43:46 PM | SOL | UP | 74 sec | -0.203% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:43:46 PM | PALLADIUM | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:43:14 PM | XRP | UP | 1.8 min | -0.298% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:42:59 PM | DOGE | UP | 2.0 min | -0.510% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:42:59 PM | WTI | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:42:41 PM | SILVER | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:42:10 PM | HYPE | DOWN | 2.8 min | +0.386% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:42:10 PM | ZEC | UP | 2.8 min | -0.639% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:41:54 PM | GBPUSD | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:41:37 PM | BTC | UP | 3.4 min | -0.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:41:21 PM | GOLD | DOWN | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:40:32 PM | EURUSD | DOWN | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:40:16 PM | ETH | UP | 4.7 min | -0.293% | 2¢ | ❌ Lost | -$0.15 |
| 10/4 10:29:50 PM | GBPUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:29:34 PM | SOL | DOWN | 26 sec | +0.099% | 0¢ | ❌ Lost | $0.00 |
| 10/4 10:29:03 PM | NEAR | UP | 57 sec | -0.461% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:29:03 PM | XRP | UP | 57 sec | -0.205% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:29:03 PM | WTI | UP | 57 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:29:03 PM | ETH | UP | 57 sec | -0.153% | 0¢ | ❌ Lost | $0.00 |
| 10/4 10:29:03 PM | EURUSD | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:28:47 PM | DOGE | UP | 72 sec | -0.195% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:28:47 PM | BNB | UP | 72 sec | -0.139% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:28:47 PM | PLATINUM | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:28:15 PM | GOLD | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:28:15 PM | PALLADIUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:28:15 PM | BTC | UP | 1.7 min | -0.155% | 0¢ | ❌ Lost | $0.00 |
| 10/4 10:28:15 PM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:28:15 PM | SILVER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
