# 15-Minute 1¢ Study

*Updated Mon Sep 28, 10:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 51 finished bets | 4% | $20.35 | +266% | +39.90¢ | $24.25 / -$3.90 |

*Expect about **48 buys a day** (~$7.14/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 185 | $18.00 | +75% |
| 5+ min left, sell at 50¢ | 51 | $5.85 | +76% |
| Mean-reversion model ≥ 2%, hold to the close | 282 | $5.85 | +16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1499 | 1493 | 8 (1%) | 1.07% | -$67.55 (-38%) | Hold to the close: -$67.55 (-38%) |

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
| Volatility model | 747 | 2.9% | 0.5% (4) | -333% | ❌ Worse |
| Momentum model | 747 | 3.0% | 0.5% (4) | -407% | ❌ Worse |
| Mean-reversion model | 747 | 5.8% | 0.5% (4) | -383% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 747 | 4 | -30% | -89% | -90% | -85% |
| Volatility model ≥ 2% | 143 | 1 | -17% | -85% | -84% | -77% |
| Volatility model ≥ 5% | 69 | 0 | -100% | -72% | -69% | -57% |
| Volatility model ≥ 10% | 36 | 0 | -100% | -70% | -66% | -43% |
| Momentum model ≥ 2% | 118 | 0 | -100% | -84% | -88% | -85% |
| Momentum model ≥ 5% | 69 | 0 | -100% | -82% | -89% | -82% |
| Momentum model ≥ 10% | 47 | 0 | -100% | -88% | -82% | -70% |
| Mean-reversion model ≥ 2% | 282 | 3 | +16% | -85% | -85% | -78% |
| Mean-reversion model ≥ 5% | 185 | 3 | +75% | -83% | -82% | -73% |
| Mean-reversion model ≥ 10% | 115 | 2 | +96% | -78% | -78% | -68% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 942 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 465 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 86 | 3% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1493 | 3% | 2% | 2% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 1% | -$67.55 | -38% | — |
| Sell at 2¢ | 51 | 3% | -$166.29 | -93% | 47 sec |
| Sell at 3¢ | 33 | 2% | -$166.68 | -93% | 47 sec |
| Sell at 5¢ | 24 | 2% | -$163.95 | -91% | 80 sec |
| Sell at 10¢ | 22 | 1% | -$150.73 | -84% | 1.7 min |
| Sell at 25¢ | 12 | 1% | -$139.83 | -78% | 1.9 min |
| Sell at 50¢ | 8 | 1% | -$125.55 | -70% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 51 | 2 | 6% | 4% | +266% | -90% | -85% |
| 2–5 min | 502 | 5 | 7% | 3% | -3% | -87% | -89% |
| 1–2 min | 423 | 1 | 2% | 1% | -74% | -96% | -96% |
| Under 1 min | 517 | 0 | 1% | 0% | -100% | -98% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 108 | 2 | 6% | 4% | +133% | -87% | -84% |
| ZEC | 107 | 1 | 7% | 2% | +15% | -85% | -94% |
| DOGE | 106 | 1 | 5% | 3% | +15% | -89% | -84% |
| NEAR | 105 | 0 | 3% | 1% | -100% | -92% | -96% |
| BTC | 105 | 0 | 9% | 3% | -100% | -78% | -85% |
| XRP | 105 | 2 | 4% | 3% | +142% | -91% | -90% |
| SOL | 104 | 0 | 3% | 2% | -100% | -92% | -89% |
| BNB | 102 | 0 | 2% | 1% | -100% | -96% | -94% |
| HYPE | 100 | 0 | 3% | 2% | -100% | -93% | -93% |
| GOLD | 82 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 74 | 0 | 1% | 0% | -100% | -97% | -100% |
| SILVER | 72 | 0 | 1% | 0% | -100% | -97% | -95% |
| NATGAS | 65 | 0 | 3% | 2% | -100% | -95% | -92% |
| COPPER | 63 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 62 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 47 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 32 | 0 | 3% | 0% | -100% | -95% | -92% |
| EURUSD | 28 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 26 | 2 | 8% | 8% | +618% | -87% | -80% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 803 | 5 | 4% | 2% | -27% | -92% | -91% |
| DOWN (bought NO) | 690 | 3 | 3% | 1% | -50% | -94% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 95 | 0 | 3% | 2% | -100% | -88% | -88% |
| 0.05–0.1% | 104 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 209 | 0 | 4% | 1% | -100% | -90% | -88% |
| 0.2–0.5% | 362 | 2 | 5% | 3% | -39% | -90% | -91% |
| Over 0.5% | 172 | 4 | 7% | 3% | +147% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 517 | 2 | 4% | 2% | -55% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,958 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 10:14:47 PM | PLATINUM | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:14:47 PM | COPPER | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:14:47 PM | DOGE | UP | 12 sec | -0.112% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:14:47 PM | SOL | UP | 12 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:14:31 PM | EURUSD | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:14:31 PM | XRP | UP | 28 sec | -0.141% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:14:15 PM | GOLD | UP | 44 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:14:15 PM | NEAR | UP | 44 sec | -0.334% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:13:59 PM | NATGAS | UP | 60 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:13:59 PM | HYPE | DOWN | 60 sec | +0.161% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:13:26 PM | ETH | DOWN | 1.6 min | +0.069% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:13:10 PM | BTC | DOWN | 1.8 min | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:12:40 PM | ZEC | DOWN | 2.3 min | +0.438% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:12:24 PM | WTI | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:12:08 PM | SILVER | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:59:54 PM | HYPE | DOWN | 6 sec | +0.021% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:59:23 PM | ZEC | UP | 37 sec | -0.113% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:59:07 PM | GBPUSD | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:59:07 PM | XRP | UP | 53 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:58:51 PM | ETH | UP | 69 sec | -0.110% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:58:36 PM | WTI | DOWN | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:58:36 PM | DOGE | UP | 83 sec | -0.157% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:58:36 PM | NEAR | UP | 83 sec | -0.416% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:58:20 PM | SOL | UP | 1.6 min | -0.134% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:58:20 PM | GOLD | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:58:20 PM | BTC | UP | 1.6 min | -0.104% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:58:20 PM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:58:04 PM | BNB | UP | 1.9 min | -0.134% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:57:33 PM | COPPER | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:57:17 PM | SILVER | UP | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
