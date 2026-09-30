# 15-Minute 1¢ Study

*Updated Wed Sep 30, 11:22 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 112 finished bets | 2% | $11.35 | +68% | +10.13¢ | $19.60 / -$8.25 |

*Expect about **43 buys a day** (~$6.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 112 | -$3.15 | -19% |
| 5+ min left, sell at 25¢ | 112 | -$6.72 | -40% |
| Momentum model ≥ 5%, hold to the close | 187 | -$6.85 | -33% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3375 | 3369 | 13 (0%) | 1.07% | -$230.50 (-56%) | Hold to the close: -$230.50 (-56%) |

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
| Volatility model | 1901 | 3.1% | 0.3% (5) | -548% | ❌ Worse |
| Momentum model | 1901 | 3.2% | 0.3% (5) | -607% | ❌ Worse |
| Mean-reversion model | 1901 | 6.1% | 0.3% (5) | -682% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1901 | 5 | -67% | -90% | -90% | -87% |
| Volatility model ≥ 2% | 377 | 2 | -40% | -85% | -86% | -82% |
| Volatility model ≥ 5% | 177 | 0 | -100% | -77% | -76% | -70% |
| Volatility model ≥ 10% | 94 | 0 | -100% | -79% | -78% | -70% |
| Momentum model ≥ 2% | 338 | 1 | -65% | -84% | -85% | -82% |
| Momentum model ≥ 5% | 187 | 1 | -33% | -84% | -87% | -81% |
| Momentum model ≥ 10% | 120 | 0 | -100% | -89% | -87% | -83% |
| Mean-reversion model ≥ 2% | 722 | 3 | -56% | -86% | -87% | -82% |
| Mean-reversion model ≥ 5% | 470 | 3 | -32% | -84% | -84% | -77% |
| Mean-reversion model ≥ 10% | 289 | 2 | -23% | -78% | -79% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2097 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 1018 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 254 | 4% | 2% | 2% | 2% | 1% | 1% |
| **All** | 3369 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$230.50 | -56% | — |
| Sell at 2¢ | 128 | 4% | -$379.22 | -92% | 47 sec |
| Sell at 3¢ | 82 | 2% | -$380.52 | -92% | 49 sec |
| Sell at 5¢ | 61 | 2% | -$372.85 | -90% | 64 sec |
| Sell at 10¢ | 48 | 1% | -$335.62 | -81% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$319.06 | -77% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$289.50 | -70% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 112 | 2 | 11% | 4% | +68% | -81% | -86% |
| 2–5 min | 1117 | 6 | 7% | 3% | -48% | -88% | -89% |
| 1–2 min | 894 | 4 | 4% | 2% | -52% | -93% | -92% |
| Under 1 min | 1246 | 1 | 1% | 0% | -88% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 237 | 1 | 4% | 2% | -46% | -90% | -90% |
| ZEC | 235 | 1 | 5% | 3% | -49% | -89% | -91% |
| NEAR | 234 | 0 | 5% | 1% | -100% | -88% | -91% |
| ETH | 233 | 2 | 5% | 4% | +3% | -89% | -86% |
| XRP | 233 | 2 | 2% | 2% | +12% | -95% | -94% |
| BNB | 232 | 0 | 3% | 1% | -100% | -94% | -95% |
| BTC | 231 | 0 | 6% | 3% | -100% | -85% | -88% |
| SOL | 231 | 0 | 3% | 1% | -100% | -92% | -92% |
| HYPE | 231 | 1 | 5% | 3% | -47% | -89% | -87% |
| GOLD | 178 | 0 | 6% | 2% | -100% | -88% | -91% |
| SILVER | 159 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 157 | 1 | 4% | 1% | -32% | -92% | -94% |
| COPPER | 145 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 139 | 1 | 4% | 2% | -33% | -94% | -91% |
| PLATINUM | 121 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 119 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 94 | 1 | 5% | 2% | -1% | -91% | -92% |
| EURUSD | 83 | 1 | 4% | 1% | +12% | -94% | -97% |
| USDJPY | 77 | 2 | 3% | 3% | +142% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1730 | 8 | 4% | 2% | -47% | -92% | -92% |
| DOWN (bought NO) | 1639 | 5 | 4% | 2% | -65% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 215 | 0 | 2% | 1% | -100% | -93% | -92% |
| 0.05–0.1% | 274 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 495 | 1 | 4% | 1% | -73% | -91% | -92% |
| 0.2–0.5% | 748 | 2 | 6% | 3% | -71% | -88% | -88% |
| Over 0.5% | 364 | 4 | 6% | 3% | +14% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 934 | 6 | 4% | 2% | -27% | -91% | -91% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,407 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 11:14:45 AM | WTI | UP | 14 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 11:14:45 AM | SOL | DOWN | 14 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 9/30 11:14:45 AM | BNB | DOWN | 14 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 9/30 11:14:29 AM | PLATINUM | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 11:14:29 AM | GOLD | UP | 30 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 11:14:29 AM | DOGE | UP | 30 sec | -0.103% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 11:14:29 AM | XRP | UP | 30 sec | -0.046% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 11:14:29 AM | GBPUSD | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 11:14:12 AM | ZEC | UP | 47 sec | -0.152% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 11:14:12 AM | PALLADIUM | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 11:14:12 AM | ETH | UP | 47 sec | -0.089% | 0¢ | ❌ Lost | $0.00 |
| 9/30 11:13:23 AM | NEAR | UP | 1.6 min | -1.089% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 11:12:18 AM | SILVER | UP | 2.7 min | — | 2¢ | ❌ Lost | -$0.15 |
| 9/30 11:11:13 AM | HYPE | DOWN | 3.8 min | +1.339% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:59:45 AM | NEAR | UP | 14 sec | -0.431% | 0¢ | ❌ Lost | $0.00 |
| 9/30 10:59:29 AM | BTC | UP | 30 sec | -0.028% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:59:29 AM | DOGE | UP | 30 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |
| 9/30 10:59:29 AM | NATGAS | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:59:13 AM | GOLD | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:59:13 AM | BNB | UP | 47 sec | -0.116% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:58:56 AM | SILVER | UP | 64 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:58:40 AM | ZEC | DOWN | 80 sec | +0.294% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:58:24 AM | WTI | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:58:24 AM | ETH | DOWN | 1.6 min | +0.144% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:58:07 AM | SOL | DOWN | 1.9 min | +0.212% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 10:54:53 AM | HYPE | DOWN | 5.1 min | +0.827% | 48¢ | ❌ Lost | -$0.15 |
| 9/30 10:44:56 AM | PLATINUM | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:44:40 AM | SILVER | DOWN | 20 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 10:44:40 AM | COPPER | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 10:44:40 AM | DOGE | DOWN | 20 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
