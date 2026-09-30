# 15-Minute 1¢ Study

*Updated Wed Sep 30, 5:07 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 119 finished bets | 2% | $10.45 | +60% | +8.78¢ | $19.15 / -$8.70 |

*Expect about **42 buys a day** (~$6.26/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 119 | -$4.05 | -23% |
| 5+ min left, sell at 25¢ | 119 | -$7.62 | -43% |
| Momentum model ≥ 5%, hold to the close | 199 | -$7.90 | -36% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3605 | 3599 | 13 (0%) | 1.07% | -$258.40 (-59%) | Hold to the close: -$258.40 (-59%) |

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
| Volatility model | 2058 | 3.2% | 0.2% (5) | -582% | ❌ Worse |
| Momentum model | 2058 | 3.3% | 0.2% (5) | -629% | ❌ Worse |
| Mean-reversion model | 2058 | 6.4% | 0.2% (5) | -746% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2058 | 5 | -70% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 406 | 2 | -44% | -85% | -86% | -82% |
| Volatility model ≥ 5% | 197 | 0 | -100% | -80% | -78% | -73% |
| Volatility model ≥ 10% | 108 | 0 | -100% | -82% | -81% | -74% |
| Momentum model ≥ 2% | 356 | 1 | -67% | -85% | -86% | -83% |
| Momentum model ≥ 5% | 199 | 1 | -36% | -85% | -88% | -82% |
| Momentum model ≥ 10% | 130 | 0 | -100% | -90% | -87% | -84% |
| Mean-reversion model ≥ 2% | 780 | 3 | -59% | -86% | -87% | -83% |
| Mean-reversion model ≥ 5% | 515 | 3 | -38% | -84% | -84% | -78% |
| Mean-reversion model ≥ 10% | 326 | 2 | -32% | -78% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2254 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 1070 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 275 | 4% | 2% | 2% | 1% | 1% | 1% |
| **All** | 3599 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$258.40 | -59% | — |
| Sell at 2¢ | 138 | 4% | -$404.52 | -92% | 47 sec |
| Sell at 3¢ | 85 | 2% | -$407.25 | -92% | 50 sec |
| Sell at 5¢ | 63 | 2% | -$399.45 | -91% | 64 sec |
| Sell at 10¢ | 48 | 1% | -$363.52 | -83% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$346.96 | -79% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$317.40 | -72% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 119 | 2 | 12% | 3% | +60% | -79% | -87% |
| 2–5 min | 1194 | 6 | 7% | 3% | -51% | -88% | -89% |
| 1–2 min | 928 | 4 | 3% | 2% | -54% | -93% | -92% |
| Under 1 min | 1358 | 1 | 1% | 0% | -89% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 255 | 1 | 4% | 2% | -50% | -91% | -90% |
| ZEC | 253 | 1 | 6% | 2% | -53% | -88% | -92% |
| NEAR | 251 | 0 | 5% | 2% | -100% | -88% | -90% |
| ETH | 251 | 2 | 5% | 4% | -3% | -88% | -85% |
| XRP | 250 | 2 | 2% | 2% | +5% | -95% | -94% |
| BNB | 250 | 0 | 3% | 1% | -100% | -93% | -95% |
| HYPE | 249 | 1 | 4% | 3% | -51% | -90% | -88% |
| BTC | 248 | 0 | 6% | 3% | -100% | -85% | -89% |
| SOL | 247 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 185 | 0 | 5% | 2% | -100% | -88% | -91% |
| SILVER | 169 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 165 | 1 | 4% | 1% | -36% | -93% | -95% |
| COPPER | 152 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 147 | 1 | 4% | 3% | -37% | -93% | -89% |
| PLATINUM | 130 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 122 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 100 | 1 | 5% | 2% | -7% | -91% | -92% |
| EURUSD | 92 | 1 | 3% | 1% | +1% | -94% | -97% |
| USDJPY | 83 | 2 | 2% | 2% | +125% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1863 | 8 | 4% | 2% | -51% | -92% | -92% |
| DOWN (bought NO) | 1736 | 5 | 4% | 2% | -67% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 241 | 0 | 2% | 1% | -100% | -94% | -93% |
| 0.05–0.1% | 294 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 531 | 1 | 4% | 1% | -75% | -91% | -92% |
| 0.2–0.5% | 793 | 2 | 6% | 3% | -72% | -88% | -88% |
| Over 0.5% | 394 | 4 | 7% | 3% | +5% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 787 | 1 | 3% | 1% | -86% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,387 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 4:59:50 PM | WTI | DOWN | 10 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:59:35 PM | GBPUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:59:35 PM | HYPE | UP | 24 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 9/30 4:59:35 PM | EURUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:59:19 PM | ZEC | UP | 40 sec | -0.156% | 0¢ | ❌ Lost | $0.00 |
| 9/30 4:59:19 PM | BNB | DOWN | 40 sec | -0.005% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:58:47 PM | SILVER | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:58:32 PM | PLATINUM | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:58:16 PM | DOGE | UP | 1.7 min | -0.149% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:58:16 PM | ETH | UP | 1.7 min | -0.131% | 0¢ | ❌ Lost | $0.00 |
| 9/30 4:58:16 PM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:58:00 PM | SOL | UP | 2.0 min | -0.230% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:57:44 PM | BTC | UP | 2.3 min | -0.122% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:57:44 PM | XRP | UP | 2.3 min | -0.228% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:57:13 PM | NEAR | UP | 2.8 min | -0.584% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
