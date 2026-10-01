# 15-Minute 1¢ Study

*Updated Thu Oct 1, 8:27 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 136 finished bets | 1% | $8.05 | +40% | +5.92¢ | $17.80 / -$9.75 |

*Expect about **39 buys a day** (~$5.84/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 256 | -$0.20 | -1% |
| Volatility model ≥ 5%, sell at 25¢ | 249 | -$3.52 | -13% |
| Volatility model ≥ 5%, sell at 10¢ | 249 | -$4.28 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4326 | 4316 | 14 (0%) | 1.07% | -$333.65 (-63%) | Hold to the close: -$333.65 (-63%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 2468 | 3.4% | 0.2% (6) | -623% | ❌ Worse |
| Momentum model | 2468 | 3.6% | 0.2% (6) | -674% | ❌ Worse |
| Mean-reversion model | 2468 | 6.5% | 0.2% (6) | -792% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2468 | 6 | -70% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 502 | 3 | -32% | -62% | -64% | -60% |
| Volatility model ≥ 5% | 249 | 1 | -49% | -29% | -31% | -25% |
| Volatility model ≥ 10% | 144 | 1 | +0% | +19% | +17% | +24% |
| Momentum model ≥ 2% | 444 | 2 | -46% | -57% | -61% | -58% |
| Momentum model ≥ 5% | 256 | 2 | -1% | -36% | -39% | -34% |
| Momentum model ≥ 10% | 168 | 1 | -15% | -4% | -3% | +1% |
| Mean-reversion model ≥ 2% | 929 | 3 | -66% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 610 | 3 | -47% | -82% | -85% | -78% |
| Mean-reversion model ≥ 10% | 390 | 2 | -43% | -78% | -81% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2664 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1280 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 372 | 3% | 2% | 1% | 1% | 1% | 1% |
| **All** | 4316 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$333.65 | -63% | — |
| Sell at 2¢ | 158 | 4% | -$474.57 | -90% | 46 sec |
| Sell at 3¢ | 91 | 2% | -$480.16 | -91% | 49 sec |
| Sell at 5¢ | 68 | 2% | -$471.45 | -89% | 66 sec |
| Sell at 10¢ | 49 | 1% | -$437.46 | -83% | 78 sec |
| Sell at 25¢ | 24 | 1% | -$422.21 | -80% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$392.65 | -74% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 136 | 2 | 13% | 3% | +40% | -77% | -88% |
| 2–5 min | 1407 | 6 | 7% | 3% | -59% | -88% | -90% |
| 1–2 min | 1124 | 4 | 3% | 2% | -62% | -94% | -93% |
| Under 1 min | 1649 | 2 | 1% | 0% | -82% | -89% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 301 | 1 | 4% | 1% | -57% | -90% | -92% |
| ETH | 298 | 2 | 5% | 3% | -17% | -89% | -87% |
| NEAR | 297 | 0 | 5% | 1% | -100% | -88% | -91% |
| ZEC | 297 | 1 | 5% | 2% | -60% | -89% | -93% |
| XRP | 295 | 3 | 2% | 1% | +30% | -53% | -52% |
| HYPE | 295 | 1 | 4% | 3% | -59% | -90% | -89% |
| BNB | 295 | 0 | 4% | 1% | -100% | -91% | -95% |
| BTC | 294 | 0 | 7% | 3% | -100% | -83% | -87% |
| SOL | 292 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 222 | 0 | 5% | 1% | -100% | -90% | -93% |
| SILVER | 206 | 0 | 1% | 0% | -100% | -97% | -97% |
| WTI | 197 | 1 | 3% | 1% | -47% | -94% | -96% |
| COPPER | 180 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 167 | 1 | 4% | 2% | -44% | -93% | -91% |
| PLATINUM | 157 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 151 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 135 | 1 | 4% | 1% | -31% | -94% | -94% |
| EURUSD | 129 | 1 | 2% | 1% | -28% | -96% | -98% |
| USDJPY | 108 | 2 | 2% | 2% | +73% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2206 | 8 | 3% | 2% | -58% | -93% | -93% |
| DOWN (bought NO) | 2110 | 6 | 4% | 1% | -68% | -87% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 311 | 1 | 1% | 1% | -40% | -36% | -35% |
| 0.05–0.1% | 378 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 638 | 1 | 4% | 2% | -80% | -91% | -92% |
| 0.2–0.5% | 897 | 2 | 6% | 3% | -75% | -89% | -89% |
| Over 0.5% | 439 | 4 | 7% | 3% | -6% | -86% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1046 | 6 | 4% | 2% | -35% | -91% | -91% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,202 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 8:27:02 AM | GOLD | DOWN | 3.0 min | — | — | In play | — |
| 10/1 8:27:02 AM | ETH | DOWN | 3.0 min | +0.421% | — | In play | — |
| 10/1 8:27:02 AM | USDJPY | UP | 3.0 min | — | — | In play | — |
| 10/1 8:26:13 AM | BTC | DOWN | 3.8 min | +0.346% | — | In play | — |
| 10/1 8:14:27 AM | NEAR | UP | 33 sec | -0.338% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:14:12 AM | BNB | UP | 48 sec | -0.139% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:14:12 AM | PLATINUM | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:14:12 AM | BTC | UP | 48 sec | -0.207% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:13:40 AM | WTI | DOWN | 80 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:13:24 AM | SOL | UP | 1.6 min | -0.326% | 2¢ | ❌ Lost | -$0.15 |
| 10/1 8:13:24 AM | ETH | UP | 1.6 min | -0.379% | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:13:24 AM | PALLADIUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:13:07 AM | COPPER | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:13:07 AM | GOLD | UP | 1.9 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 8:13:07 AM | EURUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:12:51 AM | XRP | UP | 2.1 min | -0.497% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:12:51 AM | ZEC | UP | 2.1 min | -0.621% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:12:51 AM | USDJPY | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:12:51 AM | SILVER | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:12:35 AM | HYPE | UP | 2.4 min | -0.361% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:12:35 AM | NATGAS | DOWN | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 8:12:35 AM | GBPUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 8:12:19 AM | DOGE | UP | 2.7 min | -0.585% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:59:59 AM | USDJPY | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:59:59 AM | BNB | UP | 1 sec | +0.035% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:59:59 AM | HYPE | UP | 1 sec | +0.006% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:59:59 AM | GOLD | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 7:59:43 AM | SOL | DOWN | 17 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/1 7:59:43 AM | WTI | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:59:43 AM | ETH | UP | 17 sec | -0.025% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
