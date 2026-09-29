# 15-Minute 1¢ Study

*Updated Tue Sep 29, 3:21 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 59 finished bets | 3% | $19.15 | +216% | +32.46¢ | $23.65 / -$4.50 |

*Expect about **46 buys a day** (~$6.92/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 222 | $13.20 | +46% |
| 5+ min left, sell at 50¢ | 59 | $4.65 | +53% |
| Volatility model ≥ 5%, sell at 25¢ | 81 | $1.38 | +16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1746 | 1740 | 8 (0%) | 1.07% | -$97.40 (-47%) | Hold to the close: -$97.40 (-47%) |

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
| Volatility model | 906 | 2.8% | 0.4% (4) | -382% | ❌ Worse |
| Momentum model | 906 | 3.0% | 0.4% (4) | -453% | ❌ Worse |
| Mean-reversion model | 906 | 5.9% | 0.4% (4) | -458% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 906 | 4 | -43% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 175 | 1 | -33% | -85% | -87% | -81% |
| Volatility model ≥ 5% | 81 | 0 | -100% | -73% | -73% | -62% |
| Volatility model ≥ 10% | 41 | 0 | -100% | -71% | -68% | -46% |
| Momentum model ≥ 2% | 144 | 0 | -100% | -86% | -91% | -88% |
| Momentum model ≥ 5% | 84 | 0 | -100% | -83% | -91% | -86% |
| Momentum model ≥ 10% | 56 | 0 | -100% | -90% | -85% | -75% |
| Mean-reversion model ≥ 2% | 338 | 3 | -3% | -86% | -87% | -81% |
| Mean-reversion model ≥ 5% | 222 | 3 | +46% | -84% | -84% | -75% |
| Mean-reversion model ≥ 10% | 140 | 2 | +62% | -79% | -80% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1101 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 537 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 102 | 3% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1740 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$97.40 | -47% | — |
| Sell at 2¢ | 56 | 3% | -$194.84 | -93% | 47 sec |
| Sell at 3¢ | 35 | 2% | -$195.75 | -93% | 47 sec |
| Sell at 5¢ | 25 | 1% | -$193.15 | -92% | 81 sec |
| Sell at 10¢ | 23 | 1% | -$179.27 | -86% | 1.9 min |
| Sell at 25¢ | 13 | 1% | -$166.37 | -79% | 2.1 min |
| Sell at 50¢ | 9 | 1% | -$148.65 | -71% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 59 | 2 | 8% | 3% | +216% | -85% | -87% |
| 2–5 min | 584 | 5 | 6% | 3% | -17% | -89% | -90% |
| 1–2 min | 477 | 1 | 2% | 1% | -77% | -95% | -96% |
| Under 1 min | 620 | 0 | 1% | 0% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 126 | 2 | 5% | 3% | +99% | -89% | -86% |
| ZEC | 124 | 1 | 6% | 2% | -2% | -87% | -95% |
| NEAR | 123 | 0 | 5% | 2% | -100% | -87% | -94% |
| DOGE | 123 | 1 | 4% | 2% | +1% | -91% | -86% |
| XRP | 123 | 2 | 3% | 2% | +107% | -92% | -91% |
| BTC | 122 | 0 | 7% | 2% | -100% | -82% | -88% |
| SOL | 122 | 0 | 2% | 2% | -100% | -93% | -90% |
| BNB | 120 | 0 | 2% | 1% | -100% | -95% | -95% |
| HYPE | 118 | 0 | 3% | 2% | -100% | -94% | -94% |
| GOLD | 93 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 85 | 0 | 1% | 0% | -100% | -98% | -100% |
| SILVER | 84 | 0 | 1% | 0% | -100% | -97% | -96% |
| COPPER | 77 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 74 | 0 | 4% | 1% | -100% | -93% | -89% |
| PLATINUM | 69 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 55 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 38 | 0 | 3% | 0% | -100% | -95% | -93% |
| USDJPY | 33 | 2 | 6% | 6% | +466% | -89% | -84% |
| EURUSD | 31 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 925 | 5 | 4% | 2% | -37% | -92% | -92% |
| DOWN (bought NO) | 815 | 3 | 3% | 1% | -57% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 111 | 0 | 3% | 2% | -100% | -90% | -90% |
| 0.05–0.1% | 131 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 251 | 0 | 4% | 1% | -100% | -91% | -91% |
| 0.2–0.5% | 416 | 2 | 5% | 2% | -47% | -91% | -92% |
| Over 0.5% | 192 | 4 | 7% | 4% | +120% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 483 | 1 | 3% | 1% | -76% | -93% | -95% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,932 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 3:14:34 AM | NEAR | DOWN | 26 sec | +0.109% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:14:18 AM | DOGE | UP | 42 sec | -0.097% | 0¢ | ❌ Lost | $0.00 |
| 9/29 3:14:03 AM | XRP | UP | 56 sec | -0.120% | 0¢ | ❌ Lost | $0.00 |
| 9/29 3:14:03 AM | BNB | UP | 56 sec | -0.090% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:13:47 AM | PALLADIUM | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:13:47 AM | SOL | UP | 72 sec | -0.153% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 3:13:31 AM | ZEC | DOWN | 88 sec | +0.197% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:12:59 AM | BTC | UP | 2.0 min | -0.110% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:12:59 AM | HYPE | UP | 2.0 min | -0.218% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:12:10 AM | ETH | UP | 2.8 min | -0.170% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 3:10:32 AM | NATGAS | UP | 4.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:59:52 AM | COPPER | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:59:52 AM | BTC | UP | 7 sec | -0.004% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:59:36 AM | SOL | DOWN | 23 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 9/29 2:59:36 AM | XRP | DOWN | 23 sec | +0.087% | 0¢ | ❌ Lost | $0.00 |
| 9/29 2:59:20 AM | WTI | UP | 39 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:59:20 AM | HYPE | UP | 39 sec | -0.107% | 0¢ | ❌ Lost | $0.00 |
| 9/29 2:59:04 AM | BNB | UP | 56 sec | -0.086% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:59:04 AM | ZEC | UP | 56 sec | -0.244% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:58:46 AM | PALLADIUM | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:58:30 AM | NATGAS | UP | 1.5 min | — | 3¢ | ❌ Lost | -$0.15 |
| 9/29 2:58:14 AM | ETH | UP | 1.8 min | -0.105% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:57:27 AM | NEAR | DOWN | 2.5 min | +0.389% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:57:11 AM | DOGE | DOWN | 2.8 min | +0.247% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:44:55 AM | SILVER | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:44:07 AM | GOLD | UP | 53 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:42:46 AM | PALLADIUM | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:41:24 AM | SOL | UP | 3.6 min | -0.450% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:41:08 AM | XRP | UP | 3.9 min | -0.689% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:41:08 AM | BTC | UP | 3.9 min | -0.392% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
