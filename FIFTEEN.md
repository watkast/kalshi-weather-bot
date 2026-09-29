# 15-Minute 1¢ Study

*Updated Tue Sep 29, 6:55 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 65 finished bets | 3% | $18.25 | +187% | +28.08¢ | $23.20 / -$4.95 |

*Expect about **46 buys a day** (~$6.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 235 | $11.55 | +38% |
| 5+ min left, sell at 50¢ | 65 | $3.75 | +38% |
| Volatility model ≥ 5%, sell at 25¢ | 85 | $1.08 | +12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1840 | 1834 | 8 (0%) | 1.07% | -$109.55 (-49%) | Hold to the close: -$109.55 (-49%) |

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
| Volatility model | 967 | 2.8% | 0.4% (4) | -408% | ❌ Worse |
| Momentum model | 967 | 2.9% | 0.4% (4) | -476% | ❌ Worse |
| Mean-reversion model | 967 | 6.0% | 0.4% (4) | -494% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 967 | 4 | -47% | -90% | -92% | -88% |
| Volatility model ≥ 2% | 190 | 1 | -39% | -86% | -88% | -83% |
| Volatility model ≥ 5% | 85 | 0 | -100% | -74% | -74% | -63% |
| Volatility model ≥ 10% | 44 | 0 | -100% | -73% | -70% | -50% |
| Momentum model ≥ 2% | 155 | 0 | -100% | -87% | -91% | -89% |
| Momentum model ≥ 5% | 89 | 0 | -100% | -84% | -92% | -86% |
| Momentum model ≥ 10% | 57 | 0 | -100% | -90% | -85% | -75% |
| Mean-reversion model ≥ 2% | 362 | 3 | -10% | -86% | -88% | -82% |
| Mean-reversion model ≥ 5% | 235 | 3 | +38% | -84% | -85% | -77% |
| Mean-reversion model ≥ 10% | 149 | 2 | +52% | -79% | -81% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1162 | 4% | 2% | 2% | 2% | 1% | 1% |
| Commodities | 565 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 107 | 4% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1834 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$109.55 | -49% | — |
| Sell at 2¢ | 61 | 3% | -$205.69 | -93% | 47 sec |
| Sell at 3¢ | 35 | 2% | -$207.90 | -94% | 47 sec |
| Sell at 5¢ | 25 | 1% | -$205.30 | -93% | 81 sec |
| Sell at 10¢ | 23 | 1% | -$191.42 | -86% | 1.9 min |
| Sell at 25¢ | 13 | 1% | -$178.52 | -81% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$160.80 | -73% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 65 | 2 | 9% | 3% | +187% | -84% | -88% |
| 2–5 min | 616 | 5 | 6% | 3% | -21% | -89% | -90% |
| 1–2 min | 503 | 1 | 2% | 1% | -79% | -96% | -96% |
| Under 1 min | 650 | 0 | 1% | 0% | -100% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 133 | 2 | 5% | 3% | +87% | -90% | -87% |
| ZEC | 131 | 1 | 5% | 2% | -7% | -88% | -95% |
| NEAR | 130 | 0 | 5% | 2% | -100% | -88% | -94% |
| DOGE | 130 | 1 | 5% | 2% | -5% | -89% | -87% |
| XRP | 130 | 2 | 3% | 2% | +94% | -93% | -92% |
| BTC | 129 | 0 | 8% | 2% | -100% | -81% | -88% |
| SOL | 128 | 0 | 2% | 2% | -100% | -94% | -91% |
| BNB | 126 | 0 | 2% | 1% | -100% | -95% | -95% |
| HYPE | 125 | 0 | 2% | 2% | -100% | -95% | -95% |
| GOLD | 97 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 89 | 0 | 1% | 0% | -100% | -98% | -100% |
| SILVER | 89 | 0 | 2% | 0% | -100% | -95% | -96% |
| COPPER | 82 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 77 | 0 | 4% | 1% | -100% | -93% | -90% |
| PLATINUM | 72 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 59 | 0 | 2% | 0% | -100% | -97% | -100% |
| GBPUSD | 40 | 0 | 2% | 0% | -100% | -96% | -94% |
| USDJPY | 34 | 2 | 6% | 6% | +449% | -90% | -85% |
| EURUSD | 33 | 0 | 3% | 0% | -100% | -95% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 964 | 5 | 4% | 2% | -39% | -92% | -92% |
| DOWN (bought NO) | 870 | 3 | 3% | 1% | -60% | -94% | -96% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 116 | 0 | 3% | 2% | -100% | -90% | -90% |
| 0.05–0.1% | 138 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 270 | 0 | 4% | 1% | -100% | -90% | -91% |
| 0.2–0.5% | 442 | 2 | 5% | 2% | -50% | -91% | -92% |
| Over 0.5% | 196 | 4 | 7% | 4% | +115% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,787 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 4:59:52 AM | ZEC | DOWN | 7 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:59:36 AM | COPPER | DOWN | 23 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:59:20 AM | BTC | DOWN | 39 sec | +0.019% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:59:04 AM | DOGE | DOWN | 56 sec | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:58:31 AM | GOLD | DOWN | 88 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:58:31 AM | ETH | DOWN | 88 sec | +0.121% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:58:31 AM | NATGAS | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:58:15 AM | SOL | DOWN | 1.7 min | +0.111% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:57:27 AM | WTI | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:57:11 AM | BNB | DOWN | 2.8 min | +0.054% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:57:11 AM | USDJPY | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:56:54 AM | HYPE | DOWN | 3.1 min | +0.213% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:56:20 AM | XRP | DOWN | 3.6 min | +0.326% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:56:20 AM | NEAR | DOWN | 3.6 min | +0.415% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:53:09 AM | EURUSD | DOWN | 6.8 min | — | 2¢ | ❌ Lost | -$0.15 |
| 9/29 4:44:28 AM | COPPER | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:44:12 AM | ZEC | UP | 48 sec | -0.195% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:43:22 AM | BNB | UP | 1.6 min | -0.123% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 4:43:22 AM | ETH | UP | 1.6 min | -0.155% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:43:22 AM | HYPE | UP | 1.6 min | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:43:07 AM | XRP | UP | 1.9 min | -0.226% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:42:49 AM | BTC | UP | 2.2 min | -0.109% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:42:02 AM | SOL | UP | 3.0 min | -0.303% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:42:02 AM | DOGE | UP | 3.0 min | -0.314% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:39:37 AM | NEAR | UP | 5.4 min | -1.133% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:29:22 AM | NATGAS | DOWN | 38 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:29:06 AM | SILVER | UP | 54 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 9/29 4:28:33 AM | BTC | UP | 86 sec | -0.103% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:28:33 AM | ETH | UP | 86 sec | -0.107% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:28:33 AM | SOL | UP | 86 sec | -0.170% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
