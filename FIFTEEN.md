# 15-Minute 1¢ Study

*Updated Thu Oct 1, 4:02 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 142 finished bets | 1% | $7.15 | +34% | +5.04¢ | $17.35 / -$10.20 |

*Expect about **37 buys a day** (~$5.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 289 | -$3.80 | -12% |
| Volatility model ≥ 5%, sell at 25¢ | 279 | -$6.82 | -22% |
| 5+ min left, sell at 50¢ | 142 | -$7.35 | -35% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4715 | 4709 | 15 (0%) | 1.07% | -$367.20 (-64%) | Hold to the close: -$367.20 (-64%) |

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
| Volatility model | 2700 | 3.5% | 0.2% (6) | -680% | ❌ Worse |
| Momentum model | 2700 | 3.7% | 0.2% (6) | -736% | ❌ Worse |
| Mean-reversion model | 2700 | 6.6% | 0.2% (6) | -864% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2700 | 6 | -72% | -85% | -86% | -84% |
| Volatility model ≥ 2% | 554 | 3 | -38% | -63% | -65% | -61% |
| Volatility model ≥ 5% | 279 | 1 | -54% | -35% | -35% | -33% |
| Volatility model ≥ 10% | 157 | 1 | -7% | +11% | +9% | +15% |
| Momentum model ≥ 2% | 497 | 2 | -52% | -61% | -64% | -62% |
| Momentum model ≥ 5% | 289 | 2 | -12% | -41% | -44% | -40% |
| Momentum model ≥ 10% | 192 | 1 | -27% | -17% | -16% | -13% |
| Mean-reversion model ≥ 2% | 1022 | 3 | -69% | -85% | -87% | -84% |
| Mean-reversion model ≥ 5% | 671 | 3 | -52% | -82% | -84% | -79% |
| Mean-reversion model ≥ 10% | 424 | 2 | -47% | -78% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2896 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1389 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 424 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 4709 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 15 | 0% | -$367.20 | -64% | — |
| Sell at 2¢ | 175 | 4% | -$517.70 | -90% | 46 sec |
| Sell at 3¢ | 106 | 2% | -$521.86 | -90% | 49 sec |
| Sell at 5¢ | 77 | 2% | -$513.15 | -89% | 66 sec |
| Sell at 10¢ | 56 | 1% | -$475.84 | -82% | 81 sec |
| Sell at 25¢ | 26 | 1% | -$449.14 | -78% | 1.6 min |
| Sell at 50¢ | 13 | 0% | -$419.45 | -73% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 139 | 2 | 13% | 3% | +37% | -77% | -89% |
| 2–5 min | 1558 | 7 | 7% | 3% | -56% | -88% | -89% |
| 1–2 min | 1225 | 4 | 3% | 2% | -65% | -94% | -93% |
| Under 1 min | 1784 | 2 | 1% | 0% | -84% | -90% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 328 | 1 | 4% | 1% | -61% | -90% | -92% |
| ETH | 324 | 2 | 5% | 3% | -24% | -88% | -85% |
| ZEC | 322 | 1 | 5% | 2% | -63% | -89% | -94% |
| BNB | 322 | 0 | 4% | 1% | -100% | -91% | -94% |
| HYPE | 321 | 1 | 5% | 3% | -63% | -90% | -87% |
| NEAR | 320 | 0 | 5% | 2% | -100% | -88% | -91% |
| BTC | 320 | 0 | 7% | 3% | -100% | -84% | -88% |
| XRP | 320 | 3 | 2% | 1% | +22% | -56% | -55% |
| SOL | 319 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 238 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 221 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 213 | 1 | 3% | 1% | -51% | -95% | -96% |
| COPPER | 197 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 182 | 1 | 4% | 2% | -49% | -93% | -91% |
| PLATINUM | 173 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 165 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 151 | 1 | 5% | 2% | -38% | -92% | -93% |
| EURUSD | 149 | 1 | 4% | 2% | -37% | -93% | -93% |
| USDJPY | 124 | 3 | 3% | 2% | +126% | -94% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2405 | 9 | 4% | 2% | -57% | -92% | -92% |
| DOWN (bought NO) | 2304 | 6 | 4% | 1% | -70% | -87% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 336 | 1 | 1% | 1% | -45% | -41% | -40% |
| 0.05–0.1% | 407 | 0 | 2% | 0% | -100% | -93% | -95% |
| 0.1–0.2% | 700 | 1 | 4% | 1% | -81% | -91% | -92% |
| 0.2–0.5% | 977 | 2 | 6% | 3% | -77% | -88% | -89% |
| Over 0.5% | 475 | 4 | 7% | 2% | -13% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 995 | 2 | 3% | 1% | -77% | -82% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,190 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 3:59:39 PM | ZEC | DOWN | 21 sec | +0.215% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:59:04 PM | WTI | DOWN | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:59:04 PM | NEAR | DOWN | 56 sec | +0.148% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:58:56 PM | SOL | DOWN | 64 sec | +0.181% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:58:54 PM | BTC | DOWN | 66 sec | +0.063% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:58:50 PM | GBPUSD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:58:12 PM | HYPE | UP | 1.8 min | -0.306% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:58:10 PM | XRP | DOWN | 1.8 min | +0.168% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:57:07 PM | ETH | DOWN | 2.9 min | +0.068% | 4¢ | ❌ Lost | -$0.15 |
| 10/1 3:56:54 PM | DOGE | DOWN | 3.1 min | +0.226% | 2¢ | ❌ Lost | -$0.15 |
| 10/1 3:56:41 PM | BNB | DOWN | 3.3 min | +0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:44:57 PM | EURUSD | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:44:51 PM | GBPUSD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:44:15 PM | NATGAS | UP | 44 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:43:37 PM | BNB | UP | 83 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:42:59 PM | XRP | UP | 2.0 min | -0.288% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:42:59 PM | NEAR | UP | 2.0 min | -0.671% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:42:23 PM | SOL | UP | 2.6 min | -0.266% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:42:23 PM | BTC | UP | 2.6 min | -0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:42:19 PM | ETH | UP | 2.7 min | -0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:41:31 PM | DOGE | UP | 3.5 min | -0.406% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:40:36 PM | HYPE | UP | 4.4 min | -0.466% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:40:26 PM | ZEC | UP | 4.5 min | -0.652% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 3:29:48 PM | SOL | UP | 11 sec | -0.107% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:29:44 PM | BNB | DOWN | 15 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:29:24 PM | BTC | UP | 35 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:29:14 PM | XRP | UP | 45 sec | -0.167% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:29:05 PM | ETH | UP | 54 sec | -0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 3:28:48 PM | HYPE | UP | 72 sec | -0.311% | 0¢ | ❌ Lost | $0.00 |
| 10/1 3:28:26 PM | DOGE | UP | 1.6 min | -0.142% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
