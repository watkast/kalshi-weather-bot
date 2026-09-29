# 15-Minute 1¢ Study

*Updated Mon Sep 28, 10:31 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 51 finished bets | 4% | $20.35 | +266% | +39.90¢ | $24.25 / -$3.90 |

*Expect about **47 buys a day** (~$7.10/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 187 | $17.70 | +73% |
| 5+ min left, sell at 50¢ | 51 | $5.85 | +76% |
| Mean-reversion model ≥ 2%, hold to the close | 285 | $5.55 | +15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1514 | 1508 | 8 (1%) | 1.07% | -$69.65 (-38%) | Hold to the close: -$69.65 (-38%) |

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
| Volatility model | 756 | 2.9% | 0.5% (4) | -332% | ❌ Worse |
| Momentum model | 756 | 3.0% | 0.5% (4) | -407% | ❌ Worse |
| Mean-reversion model | 756 | 5.8% | 0.5% (4) | -384% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 756 | 4 | -31% | -89% | -90% | -85% |
| Volatility model ≥ 2% | 146 | 1 | -20% | -85% | -84% | -78% |
| Volatility model ≥ 5% | 69 | 0 | -100% | -72% | -69% | -57% |
| Volatility model ≥ 10% | 36 | 0 | -100% | -70% | -66% | -43% |
| Momentum model ≥ 2% | 120 | 0 | -100% | -85% | -89% | -86% |
| Momentum model ≥ 5% | 71 | 0 | -100% | -83% | -90% | -83% |
| Momentum model ≥ 10% | 49 | 0 | -100% | -89% | -83% | -72% |
| Mean-reversion model ≥ 2% | 285 | 3 | +15% | -85% | -85% | -79% |
| Mean-reversion model ≥ 5% | 187 | 3 | +73% | -83% | -82% | -73% |
| Mean-reversion model ≥ 10% | 116 | 2 | +94% | -78% | -78% | -68% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 951 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 469 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 88 | 3% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1508 | 3% | 2% | 2% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 1% | -$69.65 | -38% | — |
| Sell at 2¢ | 51 | 3% | -$168.39 | -93% | 47 sec |
| Sell at 3¢ | 33 | 2% | -$168.78 | -93% | 47 sec |
| Sell at 5¢ | 24 | 2% | -$166.05 | -91% | 80 sec |
| Sell at 10¢ | 22 | 1% | -$152.83 | -84% | 1.7 min |
| Sell at 25¢ | 12 | 1% | -$141.93 | -78% | 1.9 min |
| Sell at 50¢ | 8 | 1% | -$127.65 | -70% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 51 | 2 | 6% | 4% | +266% | -90% | -85% |
| 2–5 min | 506 | 5 | 7% | 3% | -4% | -88% | -89% |
| 1–2 min | 428 | 1 | 2% | 1% | -75% | -96% | -96% |
| Under 1 min | 523 | 0 | 1% | 0% | -100% | -98% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 109 | 2 | 6% | 4% | +130% | -87% | -84% |
| ZEC | 108 | 1 | 6% | 2% | +14% | -85% | -94% |
| DOGE | 107 | 1 | 5% | 3% | +14% | -89% | -84% |
| NEAR | 106 | 0 | 3% | 1% | -100% | -92% | -96% |
| BTC | 106 | 0 | 8% | 3% | -100% | -78% | -86% |
| XRP | 106 | 2 | 4% | 3% | +139% | -91% | -90% |
| SOL | 105 | 0 | 3% | 2% | -100% | -92% | -89% |
| BNB | 103 | 0 | 2% | 1% | -100% | -96% | -94% |
| HYPE | 101 | 0 | 3% | 2% | -100% | -93% | -93% |
| GOLD | 83 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 74 | 0 | 1% | 0% | -100% | -97% | -100% |
| SILVER | 73 | 0 | 1% | 0% | -100% | -97% | -95% |
| NATGAS | 66 | 0 | 3% | 2% | -100% | -95% | -92% |
| COPPER | 63 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 63 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 47 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 32 | 0 | 3% | 0% | -100% | -95% | -92% |
| EURUSD | 29 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 27 | 2 | 7% | 7% | +591% | -87% | -81% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 806 | 5 | 4% | 2% | -27% | -92% | -92% |
| DOWN (bought NO) | 702 | 3 | 3% | 1% | -51% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 95 | 0 | 3% | 2% | -100% | -88% | -88% |
| 0.05–0.1% | 105 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 214 | 0 | 4% | 1% | -100% | -90% | -89% |
| 0.2–0.5% | 364 | 2 | 5% | 3% | -39% | -90% | -91% |
| Over 0.5% | 173 | 4 | 7% | 3% | +146% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 532 | 2 | 4% | 2% | -56% | -91% | -90% |

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
| 9/28 10:29:53 PM | EURUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:29:53 PM | PLATINUM | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:29:53 PM | NATGAS | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:29:53 PM | USDJPY | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:29:07 PM | GOLD | UP | 53 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:29:07 PM | ZEC | DOWN | 53 sec | +0.137% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:28:51 PM | SOL | DOWN | 69 sec | +0.120% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:28:36 PM | XRP | DOWN | 84 sec | +0.121% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:28:04 PM | ETH | DOWN | 1.9 min | +0.104% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:28:04 PM | SILVER | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:28:04 PM | BNB | DOWN | 1.9 min | +0.086% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:27:48 PM | BTC | DOWN | 2.2 min | +0.119% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:27:33 PM | DOGE | DOWN | 2.5 min | +0.306% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:26:14 PM | HYPE | DOWN | 3.8 min | +0.480% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:25:58 PM | NEAR | DOWN | 4.0 min | +0.782% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
