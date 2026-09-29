# 15-Minute 1¢ Study

*Updated Mon Sep 28, 11:02 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 51 finished bets | 4% | $20.35 | +266% | +39.90¢ | $24.25 / -$3.90 |

*Expect about **46 buys a day** (~$6.96/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 187 | $17.70 | +73% |
| 5+ min left, sell at 50¢ | 51 | $5.85 | +76% |
| Mean-reversion model ≥ 2%, hold to the close | 287 | $5.25 | +14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1544 | 1538 | 8 (1%) | 1.07% | -$72.95 (-39%) | Hold to the close: -$72.95 (-39%) |

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
| Volatility model | 774 | 2.8% | 0.5% (4) | -330% | ❌ Worse |
| Momentum model | 774 | 3.0% | 0.5% (4) | -406% | ❌ Worse |
| Mean-reversion model | 774 | 5.7% | 0.5% (4) | -381% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 774 | 4 | -33% | -89% | -90% | -85% |
| Volatility model ≥ 2% | 150 | 1 | -22% | -84% | -85% | -78% |
| Volatility model ≥ 5% | 69 | 0 | -100% | -72% | -69% | -57% |
| Volatility model ≥ 10% | 36 | 0 | -100% | -70% | -66% | -43% |
| Momentum model ≥ 2% | 127 | 0 | -100% | -84% | -89% | -87% |
| Momentum model ≥ 5% | 76 | 0 | -100% | -81% | -91% | -85% |
| Momentum model ≥ 10% | 51 | 0 | -100% | -89% | -84% | -74% |
| Mean-reversion model ≥ 2% | 287 | 3 | +14% | -85% | -85% | -79% |
| Mean-reversion model ≥ 5% | 187 | 3 | +73% | -83% | -82% | -73% |
| Mean-reversion model ≥ 10% | 116 | 2 | +94% | -78% | -78% | -68% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 969 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 477 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 92 | 3% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1538 | 3% | 2% | 2% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 1% | -$72.95 | -39% | — |
| Sell at 2¢ | 52 | 3% | -$171.43 | -93% | 40 sec |
| Sell at 3¢ | 33 | 2% | -$172.08 | -93% | 47 sec |
| Sell at 5¢ | 24 | 2% | -$169.35 | -92% | 80 sec |
| Sell at 10¢ | 22 | 1% | -$156.13 | -84% | 1.7 min |
| Sell at 25¢ | 12 | 1% | -$145.23 | -79% | 1.9 min |
| Sell at 50¢ | 8 | 1% | -$130.95 | -71% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 51 | 2 | 6% | 4% | +266% | -90% | -85% |
| 2–5 min | 514 | 5 | 7% | 3% | -6% | -88% | -89% |
| 1–2 min | 437 | 1 | 2% | 1% | -75% | -95% | -96% |
| Under 1 min | 536 | 0 | 1% | 0% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 111 | 2 | 5% | 4% | +125% | -87% | -84% |
| ZEC | 110 | 1 | 6% | 2% | +11% | -86% | -94% |
| DOGE | 109 | 1 | 5% | 3% | +12% | -90% | -84% |
| NEAR | 108 | 0 | 4% | 1% | -100% | -90% | -96% |
| BTC | 108 | 0 | 8% | 3% | -100% | -79% | -86% |
| XRP | 108 | 2 | 4% | 3% | +136% | -91% | -90% |
| SOL | 107 | 0 | 3% | 2% | -100% | -92% | -89% |
| BNB | 105 | 0 | 2% | 1% | -100% | -96% | -94% |
| HYPE | 103 | 0 | 3% | 2% | -100% | -94% | -94% |
| GOLD | 84 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 76 | 0 | 1% | 0% | -100% | -97% | -100% |
| SILVER | 74 | 0 | 1% | 0% | -100% | -97% | -95% |
| NATGAS | 67 | 0 | 3% | 1% | -100% | -95% | -92% |
| COPPER | 65 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 64 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 47 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 34 | 0 | 3% | 0% | -100% | -95% | -92% |
| EURUSD | 30 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 28 | 2 | 7% | 7% | +567% | -88% | -81% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 827 | 5 | 4% | 2% | -29% | -92% | -92% |
| DOWN (bought NO) | 711 | 3 | 3% | 1% | -51% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 96 | 0 | 3% | 2% | -100% | -88% | -88% |
| 0.05–0.1% | 110 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 219 | 0 | 4% | 1% | -100% | -90% | -89% |
| 0.2–0.5% | 370 | 2 | 5% | 3% | -40% | -89% | -91% |
| Over 0.5% | 174 | 4 | 7% | 3% | +144% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 562 | 2 | 4% | 2% | -58% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,912 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 10:59:56 PM | SILVER | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:59:56 PM | COPPER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:59:40 PM | WTI | DOWN | 20 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:59:40 PM | SOL | DOWN | 20 sec | +0.077% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:59:40 PM | NEAR | UP | 20 sec | -0.204% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:59:40 PM | DOGE | DOWN | 20 sec | +0.069% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:59:40 PM | XRP | DOWN | 20 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:59:08 PM | NATGAS | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:58:52 PM | ETH | DOWN | 68 sec | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:58:52 PM | BTC | DOWN | 68 sec | +0.038% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:57:49 PM | HYPE | UP | 2.2 min | -0.180% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:57:49 PM | BNB | UP | 2.2 min | -0.173% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:57:16 PM | ZEC | UP | 2.7 min | -0.665% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:57:16 PM | GBPUSD | UP | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:44:51 PM | WTI | DOWN | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:44:51 PM | PLATINUM | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:44:20 PM | EURUSD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:44:20 PM | COPPER | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:44:04 PM | GOLD | UP | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:43:48 PM | GBPUSD | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:43:33 PM | BTC | UP | 87 sec | -0.076% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:43:33 PM | XRP | UP | 87 sec | -0.188% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:43:17 PM | SOL | UP | 1.7 min | -0.224% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:43:17 PM | NEAR | UP | 1.7 min | -0.354% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 10:43:17 PM | DOGE | UP | 1.7 min | -0.285% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:43:01 PM | ETH | UP | 2.0 min | -0.157% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:42:44 PM | HYPE | UP | 2.2 min | -0.311% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:42:28 PM | BNB | UP | 2.5 min | -0.136% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:42:12 PM | ZEC | UP | 2.8 min | -0.377% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:41:56 PM | USDJPY | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
