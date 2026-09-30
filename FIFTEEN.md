# 15-Minute 1¢ Study

*Updated Wed Sep 30, 9:51 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 109 finished bets | 2% | $11.80 | +73% | +10.83¢ | $19.90 / -$8.10 |

*Expect about **43 buys a day** (~$6.41/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 109 | -$2.70 | -17% |
| Momentum model ≥ 5%, hold to the close | 180 | -$6.25 | -31% |
| Volatility model ≥ 5%, sell at 25¢ | 169 | -$8.67 | -47% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3291 | 3285 | 13 (0%) | 1.07% | -$220.60 (-55%) | Hold to the close: -$220.60 (-55%) |

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
| Volatility model | 1850 | 3.0% | 0.3% (5) | -526% | ❌ Worse |
| Momentum model | 1850 | 3.1% | 0.3% (5) | -583% | ❌ Worse |
| Mean-reversion model | 1850 | 6.0% | 0.3% (5) | -659% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1850 | 5 | -66% | -90% | -90% | -87% |
| Volatility model ≥ 2% | 361 | 2 | -37% | -85% | -85% | -81% |
| Volatility model ≥ 5% | 169 | 0 | -100% | -76% | -75% | -69% |
| Volatility model ≥ 10% | 90 | 0 | -100% | -78% | -77% | -69% |
| Momentum model ≥ 2% | 325 | 1 | -64% | -84% | -85% | -82% |
| Momentum model ≥ 5% | 180 | 1 | -31% | -83% | -87% | -81% |
| Momentum model ≥ 10% | 114 | 0 | -100% | -88% | -86% | -83% |
| Mean-reversion model ≥ 2% | 701 | 3 | -54% | -86% | -87% | -82% |
| Mean-reversion model ≥ 5% | 455 | 3 | -30% | -84% | -83% | -76% |
| Mean-reversion model ≥ 10% | 280 | 2 | -21% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2046 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 992 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 247 | 4% | 2% | 2% | 2% | 1% | 1% |
| **All** | 3285 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$220.60 | -55% | — |
| Sell at 2¢ | 125 | 4% | -$370.10 | -92% | 47 sec |
| Sell at 3¢ | 81 | 2% | -$371.01 | -92% | 49 sec |
| Sell at 5¢ | 60 | 2% | -$363.60 | -90% | 64 sec |
| Sell at 10¢ | 47 | 1% | -$327.03 | -81% | 78 sec |
| Sell at 25¢ | 23 | 1% | -$312.47 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$279.60 | -69% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 109 | 2 | 10% | 3% | +73% | -82% | -88% |
| 2–5 min | 1099 | 6 | 7% | 3% | -47% | -88% | -89% |
| 1–2 min | 872 | 4 | 4% | 2% | -51% | -93% | -91% |
| Under 1 min | 1205 | 1 | 1% | 0% | -88% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 231 | 1 | 4% | 2% | -45% | -90% | -89% |
| ZEC | 229 | 1 | 5% | 3% | -47% | -88% | -91% |
| NEAR | 228 | 0 | 5% | 1% | -100% | -89% | -91% |
| ETH | 228 | 2 | 5% | 4% | +5% | -88% | -85% |
| XRP | 228 | 2 | 2% | 2% | +15% | -95% | -94% |
| BTC | 226 | 0 | 7% | 3% | -100% | -85% | -88% |
| BNB | 226 | 0 | 3% | 1% | -100% | -94% | -94% |
| SOL | 225 | 0 | 3% | 1% | -100% | -92% | -92% |
| HYPE | 225 | 1 | 4% | 3% | -45% | -90% | -88% |
| GOLD | 175 | 0 | 6% | 2% | -100% | -87% | -90% |
| SILVER | 154 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 152 | 1 | 3% | 1% | -30% | -93% | -94% |
| COPPER | 143 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 135 | 1 | 4% | 2% | -31% | -94% | -90% |
| PLATINUM | 117 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 116 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 90 | 1 | 6% | 2% | +4% | -90% | -91% |
| EURUSD | 81 | 1 | 4% | 1% | +15% | -94% | -97% |
| USDJPY | 76 | 2 | 3% | 3% | +146% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1697 | 8 | 4% | 2% | -46% | -92% | -92% |
| DOWN (bought NO) | 1588 | 5 | 4% | 2% | -64% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 205 | 0 | 2% | 1% | -100% | -93% | -92% |
| 0.05–0.1% | 265 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 488 | 1 | 4% | 1% | -73% | -91% | -92% |
| 0.2–0.5% | 736 | 2 | 6% | 3% | -70% | -88% | -88% |
| Over 0.5% | 351 | 4 | 6% | 3% | +18% | -89% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 850 | 6 | 4% | 2% | -20% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,399 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 9:44:30 AM | COPPER | UP | 30 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:44:30 AM | USDJPY | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:44:15 AM | GBPUSD | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:43:42 AM | EURUSD | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:43:42 AM | NATGAS | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:42:21 AM | XRP | DOWN | 2.6 min | +0.408% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:41:32 AM | SOL | DOWN | 3.5 min | +0.405% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:41:32 AM | BNB | DOWN | 3.5 min | +0.291% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:41:15 AM | DOGE | DOWN | 3.7 min | +0.755% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:40:26 AM | ETH | DOWN | 4.5 min | +0.388% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:39:54 AM | NEAR | DOWN | 5.1 min | +1.042% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:39:37 AM | BTC | DOWN | 5.4 min | +0.409% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:39:21 AM | HYPE | DOWN | 5.7 min | +1.168% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:39:21 AM | ZEC | DOWN | 5.7 min | +1.119% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:28:52 AM | PALLADIUM | UP | 68 sec | — | 14¢ | ❌ Lost | -$0.15 |
| 9/30 9:28:36 AM | GBPUSD | UP | 84 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:27:15 AM | BTC | UP | 2.8 min | -0.337% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:27:15 AM | XRP | UP | 2.8 min | -0.713% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:27:00 AM | DOGE | UP | 3.0 min | -0.718% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:27:00 AM | SOL | UP | 3.0 min | -0.627% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:27:00 AM | GOLD | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:27:00 AM | BNB | UP | 3.0 min | -0.279% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:26:26 AM | HYPE | UP | 3.6 min | -0.990% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:26:26 AM | SILVER | UP | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:26:26 AM | ETH | UP | 3.6 min | -0.358% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:25:55 AM | NEAR | UP | 4.1 min | -1.434% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:25:37 AM | ZEC | UP | 4.4 min | -1.267% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:14:53 AM | SILVER | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 9:14:53 AM | PLATINUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:14:37 AM | GBPUSD | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
