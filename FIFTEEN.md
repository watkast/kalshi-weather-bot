# 15-Minute 1¢ Study

*Updated Sun Oct 4, 10:12 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 568 finished bets | 1% | $22.95 | +38% | +4.04¢ | -$17.20 / $40.15 |

*Expect about **82 buys a day** (~$12.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1046 | $14.15 | +11% |
| 5+ min left, hold to the close | 195 | $13.20 | +46% |
| Momentum model ≥ 5%, hold to the close | 572 | $9.25 | +15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7981 | 7975 | 36 (0%) | 1.07% | -$451.95 (-47%) | Hold to the close: -$451.95 (-47%) |

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
| Volatility model | 5303 | 4.2% | 0.5% (24) | -613% | ❌ Worse |
| Momentum model | 5303 | 4.3% | 0.5% (24) | -643% | ❌ Worse |
| Mean-reversion model | 5303 | 6.9% | 0.5% (24) | -710% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5303 | 24 | -43% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1046 | 10 | +11% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 568 | 6 | +38% | -55% | -54% | -49% |
| Volatility model ≥ 10% | 354 | 4 | +67% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 922 | 7 | -8% | -69% | -71% | -69% |
| Momentum model ≥ 5% | 572 | 5 | +15% | -61% | -63% | -60% |
| Momentum model ≥ 10% | 396 | 4 | +45% | -47% | -49% | -45% |
| Mean-reversion model ≥ 2% | 1848 | 13 | -23% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1241 | 11 | -1% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 820 | 8 | +13% | -77% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5500 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1879 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 596 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7975 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 36 | 0% | -$451.95 | -47% | — |
| Sell at 2¢ | 318 | 4% | -$845.27 | -88% | 33 sec |
| Sell at 3¢ | 206 | 3% | -$847.61 | -89% | 47 sec |
| Sell at 5¢ | 152 | 2% | -$829.15 | -87% | 61 sec |
| Sell at 10¢ | 104 | 1% | -$777.71 | -81% | 72 sec |
| Sell at 25¢ | 57 | 1% | -$697.28 | -73% | 1.6 min |
| Sell at 50¢ | 35 | 0% | -$607.70 | -64% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 192 | 3 | 12% | 3% | +48% | -79% | -88% |
| 2–5 min | 2570 | 19 | 8% | 4% | -28% | -86% | -86% |
| 1–2 min | 2111 | 9 | 3% | 2% | -54% | -93% | -93% |
| Under 1 min | 3099 | 5 | 1% | 0% | -76% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 621 | 5 | 5% | 3% | -5% | -89% | -89% |
| DOGE | 615 | 2 | 4% | 1% | -58% | -91% | -91% |
| ETH | 614 | 5 | 6% | 3% | +3% | -86% | -86% |
| HYPE | 614 | 3 | 5% | 3% | -40% | -88% | -86% |
| BNB | 610 | 2 | 4% | 2% | -61% | -91% | -92% |
| SOL | 609 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 607 | 3 | 6% | 2% | -35% | -86% | -89% |
| XRP | 607 | 4 | 2% | 1% | -16% | -75% | -75% |
| NEAR | 603 | 2 | 6% | 3% | -56% | -63% | -64% |
| GOLD | 317 | 0 | 4% | 1% | -100% | -90% | -93% |
| SILVER | 303 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 291 | 2 | 3% | 1% | -27% | -95% | -96% |
| COPPER | 269 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 238 | 2 | 3% | 2% | -22% | -94% | -92% |
| PLATINUM | 235 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 226 | 1 | 2% | 1% | -59% | -96% | -98% |
| EURUSD | 213 | 1 | 5% | 3% | -56% | -92% | -90% |
| GBPUSD | 204 | 1 | 4% | 2% | -54% | -93% | -94% |
| USDJPY | 179 | 3 | 2% | 2% | +56% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4027 | 20 | 4% | 2% | -42% | -88% | -87% |
| DOWN (bought NO) | 3948 | 16 | 4% | 2% | -53% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 922 | 7 | 2% | 1% | +29% | -57% | -57% |
| 0.05–0.1% | 935 | 2 | 4% | 1% | -69% | -90% | -92% |
| 0.1–0.2% | 1358 | 5 | 4% | 2% | -53% | -90% | -91% |
| 0.2–0.5% | 1613 | 8 | 6% | 3% | -45% | -87% | -87% |
| Over 0.5% | 670 | 4 | 7% | 3% | -39% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2284 | 7 | 3% | 2% | -64% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,164 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 9:59:53 PM | NEAR | UP | 6 sec | -0.295% | 0¢ | ❌ Lost | $0.00 |
| 10/4 9:59:53 PM | ZEC | DOWN | 6 sec | +0.037% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:59:53 PM | USDJPY | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:59:21 PM | WTI | UP | 38 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:59:21 PM | PLATINUM | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:59:05 PM | PALLADIUM | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:58:33 PM | SOL | UP | 86 sec | -0.223% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:58:33 PM | BTC | UP | 86 sec | -0.213% | 0¢ | ❌ Lost | $0.00 |
| 10/4 9:58:17 PM | BNB | UP | 1.7 min | -0.292% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:58:17 PM | ETH | UP | 1.7 min | -0.160% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:58:01 PM | XRP | UP | 2.0 min | -0.304% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:58:01 PM | EURUSD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:57:13 PM | DOGE | UP | 2.8 min | -0.315% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:57:13 PM | HYPE | UP | 2.8 min | -0.289% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:44:49 PM | HYPE | UP | 10 sec | -0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:44:49 PM | SILVER | DOWN | 10 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/4 9:44:33 PM | PALLADIUM | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:44:33 PM | PLATINUM | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:43:43 PM | XRP | UP | 77 sec | -0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:43:43 PM | COPPER | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:43:27 PM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:43:27 PM | GBPUSD | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:43:11 PM | ZEC | UP | 1.8 min | -0.334% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:43:11 PM | NATGAS | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:42:56 PM | SOL | UP | 2.0 min | -0.206% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:42:38 PM | BNB | UP | 2.4 min | -0.253% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:41:51 PM | BTC | UP | 3.1 min | -0.189% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:41:51 PM | ETH | UP | 3.1 min | -0.159% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:41:35 PM | EURUSD | UP | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:29:48 PM | DOGE | DOWN | 11 sec | +0.020% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
