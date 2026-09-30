# 15-Minute 1¢ Study

*Updated Wed Sep 30, 10:21 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 111 finished bets | 2% | $11.50 | +70% | +10.36¢ | $19.75 / -$8.25 |

*Expect about **43 buys a day** (~$6.48/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 111 | -$3.00 | -18% |
| Momentum model ≥ 5%, hold to the close | 184 | -$6.55 | -32% |
| Volatility model ≥ 5%, sell at 25¢ | 174 | -$9.12 | -48% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3324 | 3318 | 13 (0%) | 1.07% | -$224.95 (-55%) | Hold to the close: -$224.95 (-55%) |

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
| Volatility model | 1868 | 3.1% | 0.3% (5) | -530% | ❌ Worse |
| Momentum model | 1868 | 3.2% | 0.3% (5) | -590% | ❌ Worse |
| Mean-reversion model | 1868 | 6.1% | 0.3% (5) | -662% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1868 | 5 | -67% | -90% | -90% | -87% |
| Volatility model ≥ 2% | 371 | 2 | -39% | -85% | -86% | -82% |
| Volatility model ≥ 5% | 174 | 0 | -100% | -77% | -75% | -69% |
| Volatility model ≥ 10% | 92 | 0 | -100% | -79% | -77% | -70% |
| Momentum model ≥ 2% | 333 | 1 | -65% | -84% | -85% | -82% |
| Momentum model ≥ 5% | 184 | 1 | -32% | -84% | -87% | -81% |
| Momentum model ≥ 10% | 117 | 0 | -100% | -89% | -86% | -83% |
| Mean-reversion model ≥ 2% | 714 | 3 | -55% | -86% | -87% | -83% |
| Mean-reversion model ≥ 5% | 465 | 3 | -32% | -83% | -83% | -77% |
| Mean-reversion model ≥ 10% | 286 | 2 | -23% | -78% | -79% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2064 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 1002 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 252 | 4% | 2% | 2% | 2% | 1% | 1% |
| **All** | 3318 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$224.95 | -55% | — |
| Sell at 2¢ | 127 | 4% | -$373.93 | -92% | 47 sec |
| Sell at 3¢ | 81 | 2% | -$375.36 | -92% | 49 sec |
| Sell at 5¢ | 60 | 2% | -$367.95 | -90% | 64 sec |
| Sell at 10¢ | 47 | 1% | -$331.38 | -81% | 78 sec |
| Sell at 25¢ | 23 | 1% | -$316.82 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$283.95 | -70% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 111 | 2 | 10% | 3% | +70% | -83% | -88% |
| 2–5 min | 1110 | 6 | 7% | 3% | -48% | -88% | -89% |
| 1–2 min | 882 | 4 | 4% | 2% | -51% | -93% | -92% |
| Under 1 min | 1215 | 1 | 1% | 0% | -88% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 233 | 1 | 4% | 2% | -46% | -90% | -89% |
| ZEC | 231 | 1 | 5% | 3% | -48% | -88% | -91% |
| NEAR | 230 | 0 | 5% | 1% | -100% | -88% | -91% |
| ETH | 230 | 2 | 5% | 4% | +4% | -88% | -85% |
| XRP | 230 | 2 | 2% | 2% | +14% | -95% | -94% |
| BTC | 228 | 0 | 7% | 3% | -100% | -85% | -88% |
| BNB | 228 | 0 | 3% | 1% | -100% | -94% | -94% |
| SOL | 227 | 0 | 3% | 1% | -100% | -92% | -92% |
| HYPE | 227 | 1 | 4% | 3% | -45% | -90% | -88% |
| GOLD | 176 | 0 | 6% | 2% | -100% | -87% | -91% |
| SILVER | 156 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 154 | 1 | 4% | 1% | -31% | -92% | -94% |
| COPPER | 144 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 136 | 1 | 4% | 2% | -31% | -94% | -90% |
| PLATINUM | 119 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 117 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 92 | 1 | 5% | 2% | +1% | -91% | -92% |
| EURUSD | 83 | 1 | 4% | 1% | +12% | -94% | -97% |
| USDJPY | 77 | 2 | 3% | 3% | +142% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1705 | 8 | 4% | 2% | -47% | -92% | -92% |
| DOWN (bought NO) | 1613 | 5 | 4% | 2% | -65% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 207 | 0 | 2% | 1% | -100% | -93% | -92% |
| 0.05–0.1% | 266 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 491 | 1 | 4% | 1% | -73% | -91% | -92% |
| 0.2–0.5% | 743 | 2 | 6% | 3% | -71% | -88% | -88% |
| Over 0.5% | 356 | 4 | 6% | 3% | +16% | -89% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 883 | 6 | 4% | 2% | -23% | -91% | -91% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,403 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 10:14:59 AM | COPPER | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:14:27 AM | USDJPY | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:14:27 AM | PALLADIUM | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:14:11 AM | PLATINUM | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:14:11 AM | BNB | DOWN | 49 sec | +0.068% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:13:54 AM | GOLD | DOWN | 66 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:13:38 AM | SOL | DOWN | 82 sec | +0.223% | 0¢ | ❌ Lost | $0.00 |
| 9/30 10:13:38 AM | ETH | DOWN | 82 sec | +0.119% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:13:38 AM | DOGE | DOWN | 82 sec | +0.182% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:13:22 AM | SILVER | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:13:06 AM | GBPUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:12:01 AM | EURUSD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:11:28 AM | HYPE | DOWN | 3.5 min | +0.497% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:11:28 AM | WTI | DOWN | 3.5 min | — | 2¢ | ❌ Lost | -$0.15 |
| 9/30 10:11:12 AM | XRP | DOWN | 3.8 min | +0.452% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:10:23 AM | NEAR | DOWN | 4.6 min | +0.845% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 10:10:23 AM | BTC | DOWN | 4.6 min | +0.258% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 10:10:07 AM | ZEC | DOWN | 4.9 min | +0.841% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:59:49 AM | ETH | DOWN | 11 sec | -0.004% | 0¢ | ❌ Lost | $0.00 |
| 9/30 9:59:49 AM | BTC | DOWN | 11 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 9/30 9:59:33 AM | NATGAS | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:59:16 AM | SILVER | UP | 43 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 9:59:16 AM | GBPUSD | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:58:57 AM | PLATINUM | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:58:25 AM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:58:25 AM | DOGE | DOWN | 1.6 min | +0.225% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:58:11 AM | XRP | DOWN | 1.8 min | +0.213% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:57:54 AM | WTI | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:57:38 AM | BNB | DOWN | 2.4 min | +0.117% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:57:22 AM | ZEC | DOWN | 2.6 min | +0.561% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
