# 15-Minute 1¢ Study

*Updated Mon Oct 5, 6:37 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 620 finished bets | 1% | $31.10 | +46% | +5.02¢ | -$6.05 / $37.15 |

*Expect about **80 buys a day** (~$12.00/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 620 | $17.70 | +27% |
| Volatility model ≥ 2%, hold to the close | 1154 | $14.80 | +11% |
| Mean-reversion model ≥ 5%, hold to the close | 1368 | $9.80 | +6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8958 | 8952 | 39 (0%) | 1.07% | -$530.55 (-49%) | Hold to the close: -$530.55 (-49%) |

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
| Volatility model | 5888 | 4.1% | 0.5% (27) | -578% | ❌ Worse |
| Momentum model | 5888 | 4.1% | 0.5% (27) | -603% | ❌ Worse |
| Mean-reversion model | 5888 | 6.7% | 0.5% (27) | -677% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5888 | 27 | -42% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1154 | 11 | +11% | -70% | -70% | -66% |
| Volatility model ≥ 5% | 620 | 7 | +46% | -57% | -56% | -53% |
| Volatility model ≥ 10% | 381 | 5 | +94% | -38% | -39% | -34% |
| Momentum model ≥ 2% | 1018 | 9 | +7% | -71% | -73% | -70% |
| Momentum model ≥ 5% | 620 | 6 | +27% | -62% | -65% | -62% |
| Momentum model ≥ 10% | 427 | 5 | +68% | -50% | -51% | -48% |
| Mean-reversion model ≥ 2% | 2035 | 15 | -20% | -83% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1368 | 13 | +6% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 900 | 9 | +16% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6085 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2172 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 695 | 3% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8952 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 39 | 0% | -$530.55 | -49% | — |
| Sell at 2¢ | 342 | 4% | -$959.63 | -89% | 33 sec |
| Sell at 3¢ | 224 | 3% | -$961.19 | -89% | 47 sec |
| Sell at 5¢ | 165 | 2% | -$941.30 | -87% | 61 sec |
| Sell at 10¢ | 111 | 1% | -$889.14 | -83% | 66 sec |
| Sell at 25¢ | 61 | 1% | -$804.64 | -75% | 83 sec |
| Sell at 50¢ | 38 | 0% | -$708.05 | -66% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 223 | 3 | 11% | 3% | +27% | -81% | -88% |
| 2–5 min | 2901 | 21 | 7% | 3% | -29% | -87% | -87% |
| 1–2 min | 2357 | 10 | 3% | 2% | -54% | -93% | -93% |
| Under 1 min | 3468 | 5 | 1% | 0% | -78% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 688 | 5 | 5% | 3% | -13% | -89% | -89% |
| DOGE | 679 | 2 | 4% | 1% | -62% | -91% | -91% |
| HYPE | 679 | 3 | 5% | 3% | -46% | -88% | -86% |
| ETH | 678 | 6 | 6% | 3% | +11% | -87% | -86% |
| BNB | 675 | 2 | 4% | 2% | -64% | -90% | -92% |
| BTC | 672 | 3 | 5% | 2% | -41% | -87% | -90% |
| XRP | 672 | 4 | 1% | 1% | -24% | -78% | -78% |
| SOL | 672 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 670 | 4 | 6% | 3% | -22% | -65% | -66% |
| GOLD | 366 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 350 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 333 | 2 | 3% | 1% | -35% | -95% | -96% |
| COPPER | 309 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 277 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 271 | 2 | 3% | 2% | -31% | -94% | -92% |
| PALLADIUM | 266 | 1 | 2% | 1% | -65% | -97% | -98% |
| EURUSD | 248 | 1 | 4% | 3% | -62% | -92% | -91% |
| GBPUSD | 239 | 1 | 4% | 2% | -61% | -93% | -93% |
| USDJPY | 208 | 3 | 2% | 1% | +35% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4524 | 21 | 4% | 2% | -46% | -89% | -88% |
| DOWN (bought NO) | 4428 | 18 | 4% | 2% | -53% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1008 | 7 | 2% | 1% | +19% | -60% | -60% |
| 0.05–0.1% | 1028 | 3 | 3% | 1% | -57% | -91% | -92% |
| 0.1–0.2% | 1523 | 6 | 4% | 2% | -50% | -91% | -91% |
| 0.2–0.5% | 1784 | 9 | 6% | 3% | -44% | -88% | -87% |
| Over 0.5% | 740 | 4 | 7% | 3% | -45% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2420 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,128 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 6:29:48 PM | BTC | UP | 11 sec | -0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/5 6:29:48 PM | SOL | UP | 11 sec | -0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/5 6:29:32 PM | ETH | UP | 27 sec | -0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:29:32 PM | BNB | UP | 27 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/5 6:29:16 PM | WTI | DOWN | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:28:46 PM | PALLADIUM | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 6:28:46 PM | DOGE | UP | 73 sec | -0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:28:46 PM | COPPER | DOWN | 73 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:28:14 PM | HYPE | DOWN | 1.8 min | +0.218% | 0¢ | ❌ Lost | $0.00 |
| 10/5 6:28:14 PM | NEAR | DOWN | 1.8 min | +0.624% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:28:14 PM | PLATINUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 6:27:58 PM | SILVER | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 6:27:40 PM | GOLD | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:26:37 PM | ZEC | DOWN | 3.4 min | +0.463% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:14:52 PM | ZEC | UP | 8 sec | -0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/5 6:14:52 PM | GOLD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 6:14:52 PM | DOGE | UP | 8 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/5 6:14:20 PM | NEAR | DOWN | 40 sec | +0.270% | 0¢ | ❌ Lost | $0.00 |
| 10/5 6:14:20 PM | XRP | DOWN | 40 sec | +0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 6:14:20 PM | BNB | DOWN | 40 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/5 6:14:04 PM | BTC | DOWN | 56 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/5 6:13:30 PM | SOL | DOWN | 1.5 min | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:13:14 PM | USDJPY | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:13:14 PM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 6:12:09 PM | HYPE | DOWN | 2.8 min | +0.254% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:11:07 PM | ETH | DOWN | 3.9 min | +0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:59:51 PM | COPPER | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:59:35 PM | WTI | DOWN | 25 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:59:19 PM | BTC | UP | 41 sec | -0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:59:03 PM | DOGE | UP | 57 sec | -0.095% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
