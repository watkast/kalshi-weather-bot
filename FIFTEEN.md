# 15-Minute 1¢ Study

*Updated Wed Sep 30, 8:50 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 105 finished bets | 2% | $12.40 | +79% | +11.81¢ | $20.20 / -$7.80 |

*Expect about **42 buys a day** (~$6.28/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 105 | -$2.10 | -13% |
| Momentum model ≥ 5%, hold to the close | 177 | -$5.80 | -29% |
| Volatility model ≥ 5%, sell at 25¢ | 166 | -$8.22 | -45% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3235 | 3229 | 13 (0%) | 1.07% | -$213.10 (-54%) | Hold to the close: -$213.10 (-54%) |

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
| Volatility model | 1815 | 3.0% | 0.3% (5) | -530% | ❌ Worse |
| Momentum model | 1815 | 3.2% | 0.3% (5) | -587% | ❌ Worse |
| Mean-reversion model | 1815 | 6.1% | 0.3% (5) | -662% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1815 | 5 | -65% | -90% | -90% | -87% |
| Volatility model ≥ 2% | 352 | 2 | -36% | -85% | -86% | -81% |
| Volatility model ≥ 5% | 166 | 0 | -100% | -77% | -76% | -68% |
| Volatility model ≥ 10% | 89 | 0 | -100% | -78% | -76% | -68% |
| Momentum model ≥ 2% | 315 | 1 | -63% | -85% | -87% | -83% |
| Momentum model ≥ 5% | 177 | 1 | -29% | -83% | -86% | -80% |
| Momentum model ≥ 10% | 112 | 0 | -100% | -88% | -86% | -82% |
| Mean-reversion model ≥ 2% | 686 | 3 | -53% | -86% | -87% | -82% |
| Mean-reversion model ≥ 5% | 447 | 3 | -29% | -84% | -83% | -76% |
| Mean-reversion model ≥ 10% | 276 | 2 | -20% | -78% | -79% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2011 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 978 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 240 | 4% | 2% | 2% | 2% | 1% | 1% |
| **All** | 3229 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$213.10 | -54% | — |
| Sell at 2¢ | 122 | 4% | -$363.38 | -92% | 47 sec |
| Sell at 3¢ | 78 | 2% | -$364.68 | -92% | 50 sec |
| Sell at 5¢ | 58 | 2% | -$357.40 | -90% | 64 sec |
| Sell at 10¢ | 46 | 1% | -$320.84 | -81% | 80 sec |
| Sell at 25¢ | 23 | 1% | -$304.97 | -77% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$272.10 | -69% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 105 | 2 | 10% | 3% | +79% | -82% | -88% |
| 2–5 min | 1076 | 6 | 7% | 3% | -46% | -88% | -89% |
| 1–2 min | 858 | 4 | 4% | 2% | -50% | -93% | -92% |
| Under 1 min | 1190 | 1 | 1% | 0% | -88% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 227 | 1 | 4% | 1% | -44% | -91% | -91% |
| ZEC | 225 | 1 | 5% | 3% | -46% | -88% | -91% |
| NEAR | 224 | 0 | 5% | 1% | -100% | -88% | -90% |
| ETH | 224 | 2 | 5% | 4% | +7% | -88% | -85% |
| XRP | 224 | 2 | 2% | 2% | +17% | -95% | -93% |
| BTC | 222 | 0 | 7% | 3% | -100% | -84% | -87% |
| SOL | 222 | 0 | 3% | 1% | -100% | -92% | -92% |
| BNB | 222 | 0 | 3% | 1% | -100% | -94% | -96% |
| HYPE | 221 | 1 | 5% | 3% | -43% | -89% | -87% |
| GOLD | 173 | 0 | 6% | 2% | -100% | -87% | -90% |
| WTI | 151 | 1 | 3% | 1% | -29% | -93% | -94% |
| SILVER | 151 | 0 | 2% | 1% | -100% | -96% | -96% |
| COPPER | 140 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 134 | 1 | 4% | 2% | -30% | -94% | -90% |
| PLATINUM | 115 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 114 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 87 | 1 | 6% | 2% | +7% | -90% | -91% |
| EURUSD | 79 | 1 | 4% | 1% | +18% | -93% | -97% |
| USDJPY | 74 | 2 | 3% | 3% | +152% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1671 | 8 | 4% | 2% | -45% | -92% | -92% |
| DOWN (bought NO) | 1558 | 5 | 4% | 2% | -63% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 205 | 0 | 2% | 1% | -100% | -93% | -92% |
| 0.05–0.1% | 263 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 483 | 1 | 4% | 1% | -72% | -91% | -92% |
| 0.2–0.5% | 721 | 2 | 6% | 3% | -70% | -88% | -88% |
| Over 0.5% | 338 | 4 | 6% | 2% | +23% | -89% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 794 | 6 | 4% | 2% | -13% | -91% | -91% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,394 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 8:44:53 AM | XRP | UP | 6 sec | -0.180% | 0¢ | ❌ Lost | $0.00 |
| 9/30 8:44:53 AM | BNB | DOWN | 6 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 9/30 8:44:21 AM | HYPE | DOWN | 38 sec | +0.084% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:44:21 AM | DOGE | UP | 38 sec | -0.199% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:44:21 AM | BTC | UP | 38 sec | -0.145% | 0¢ | ❌ Lost | $0.00 |
| 9/30 8:44:21 AM | NATGAS | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:44:21 AM | ETH | UP | 38 sec | -0.146% | 0¢ | ❌ Lost | $0.00 |
| 9/30 8:43:31 AM | COPPER | UP | 89 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:43:15 AM | GBPUSD | DOWN | 1.8 min | — | 2¢ | ❌ Lost | -$0.15 |
| 9/30 8:43:15 AM | NEAR | DOWN | 1.8 min | +0.612% | 6¢ | ❌ Lost | -$0.15 |
| 9/30 8:29:50 AM | EURUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:29:50 AM | NATGAS | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:29:18 AM | GBPUSD | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:29:18 AM | PALLADIUM | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:29:18 AM | USDJPY | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:28:47 AM | PLATINUM | UP | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:27:58 AM | COPPER | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:27:42 AM | GOLD | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:27:42 AM | SILVER | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:27:26 AM | BNB | UP | 2.5 min | -0.542% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:27:10 AM | WTI | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:27:10 AM | DOGE | UP | 2.8 min | -1.108% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:26:54 AM | XRP | UP | 3.1 min | -0.931% | 0¢ | ❌ Lost | $0.00 |
| 9/30 8:26:54 AM | NEAR | UP | 3.1 min | -1.675% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:25:49 AM | SOL | UP | 4.2 min | -1.167% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:25:49 AM | ETH | UP | 4.2 min | -0.637% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:25:14 AM | HYPE | UP | 4.8 min | -0.844% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:24:58 AM | BTC | UP | 5.0 min | -0.578% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 8:23:06 AM | ZEC | UP | 6.9 min | -2.483% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:14:54 AM | EURUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
