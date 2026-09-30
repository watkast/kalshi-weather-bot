# 15-Minute 1¢ Study

*Updated Wed Sep 30, 4:47 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 119 finished bets | 2% | $10.45 | +60% | +8.78¢ | $19.15 / -$8.70 |

*Expect about **42 buys a day** (~$6.29/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 119 | -$4.05 | -23% |
| 5+ min left, sell at 25¢ | 119 | -$7.62 | -43% |
| Momentum model ≥ 5%, hold to the close | 198 | -$7.75 | -36% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3590 | 3584 | 13 (0%) | 1.07% | -$256.60 (-59%) | Hold to the close: -$256.60 (-59%) |

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
| Volatility model | 2049 | 3.2% | 0.2% (5) | -580% | ❌ Worse |
| Momentum model | 2049 | 3.2% | 0.2% (5) | -629% | ❌ Worse |
| Mean-reversion model | 2049 | 6.3% | 0.2% (5) | -743% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2049 | 5 | -69% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 405 | 2 | -44% | -85% | -86% | -82% |
| Volatility model ≥ 5% | 196 | 0 | -100% | -79% | -78% | -73% |
| Volatility model ≥ 10% | 107 | 0 | -100% | -82% | -80% | -74% |
| Momentum model ≥ 2% | 355 | 1 | -67% | -85% | -86% | -83% |
| Momentum model ≥ 5% | 198 | 1 | -36% | -84% | -87% | -82% |
| Momentum model ≥ 10% | 129 | 0 | -100% | -89% | -87% | -84% |
| Mean-reversion model ≥ 2% | 779 | 3 | -59% | -86% | -87% | -83% |
| Mean-reversion model ≥ 5% | 514 | 3 | -38% | -83% | -84% | -78% |
| Mean-reversion model ≥ 10% | 325 | 2 | -32% | -78% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2245 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 1066 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 273 | 4% | 2% | 2% | 1% | 1% | 1% |
| **All** | 3584 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$256.60 | -59% | — |
| Sell at 2¢ | 138 | 4% | -$402.72 | -92% | 47 sec |
| Sell at 3¢ | 85 | 2% | -$405.45 | -92% | 50 sec |
| Sell at 5¢ | 63 | 2% | -$397.65 | -91% | 64 sec |
| Sell at 10¢ | 48 | 1% | -$361.72 | -82% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$345.16 | -79% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$315.60 | -72% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 119 | 2 | 12% | 3% | +60% | -79% | -87% |
| 2–5 min | 1191 | 6 | 7% | 3% | -51% | -88% | -89% |
| 1–2 min | 922 | 4 | 3% | 2% | -53% | -93% | -92% |
| Under 1 min | 1352 | 1 | 1% | 0% | -89% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 254 | 1 | 4% | 2% | -50% | -91% | -90% |
| ZEC | 252 | 1 | 6% | 2% | -53% | -88% | -92% |
| NEAR | 250 | 0 | 5% | 2% | -100% | -87% | -90% |
| ETH | 250 | 2 | 5% | 4% | -3% | -88% | -85% |
| XRP | 249 | 2 | 2% | 2% | +5% | -95% | -94% |
| BNB | 249 | 0 | 3% | 1% | -100% | -93% | -95% |
| HYPE | 248 | 1 | 4% | 3% | -51% | -90% | -88% |
| BTC | 247 | 0 | 6% | 3% | -100% | -85% | -89% |
| SOL | 246 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 185 | 0 | 5% | 2% | -100% | -88% | -91% |
| SILVER | 168 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 164 | 1 | 4% | 1% | -35% | -93% | -95% |
| COPPER | 151 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 147 | 1 | 4% | 3% | -37% | -93% | -89% |
| PLATINUM | 129 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 122 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 99 | 1 | 5% | 2% | -6% | -91% | -92% |
| EURUSD | 91 | 1 | 3% | 1% | +3% | -94% | -97% |
| USDJPY | 83 | 2 | 2% | 2% | +125% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1850 | 8 | 4% | 2% | -50% | -92% | -92% |
| DOWN (bought NO) | 1734 | 5 | 4% | 2% | -67% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 240 | 0 | 2% | 1% | -100% | -94% | -93% |
| 0.05–0.1% | 293 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 527 | 1 | 4% | 1% | -75% | -91% | -92% |
| 0.2–0.5% | 791 | 2 | 6% | 3% | -72% | -88% | -88% |
| Over 0.5% | 393 | 4 | 7% | 3% | +5% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 772 | 1 | 3% | 1% | -85% | -93% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,388 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 4:44:51 PM | SILVER | UP | 9 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:44:51 PM | BTC | UP | 9 sec | -0.015% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:44:04 PM | GOLD | UP | 55 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:43:48 PM | WTI | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:43:33 PM | HYPE | DOWN | 86 sec | +0.143% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:43:33 PM | NEAR | DOWN | 86 sec | +0.324% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:42:45 PM | ETH | DOWN | 2.2 min | +0.086% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:42:45 PM | ZEC | DOWN | 2.2 min | +0.441% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:42:30 PM | SOL | DOWN | 2.5 min | +0.165% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:41:11 PM | DOGE | DOWN | 3.8 min | +0.322% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:41:11 PM | XRP | DOWN | 3.8 min | +0.195% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:40:24 PM | BNB | DOWN | 4.6 min | +0.102% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:29:50 PM | PALLADIUM | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:29:03 PM | WTI | UP | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:28:31 PM | PLATINUM | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:27:43 PM | BTC | DOWN | 2.3 min | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:27:12 PM | DOGE | DOWN | 2.8 min | +0.253% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:26:54 PM | XRP | DOWN | 3.1 min | +0.229% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:26:23 PM | SOL | DOWN | 3.6 min | +0.294% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:25:35 PM | HYPE | DOWN | 4.4 min | +0.515% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:25:20 PM | BNB | DOWN | 4.7 min | +0.115% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:24:32 PM | ETH | DOWN | 5.5 min | +0.157% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:23:11 PM | NEAR | DOWN | 6.8 min | +1.395% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 4:22:55 PM | ZEC | DOWN | 7.1 min | +0.788% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:14:46 PM | SILVER | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:14:36 PM | USDJPY | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:14:36 PM | WTI | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:14:20 PM | XRP | UP | 40 sec | -0.054% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:14:04 PM | BTC | UP | 56 sec | -0.070% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:14:04 PM | DOGE | UP | 56 sec | -0.165% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
