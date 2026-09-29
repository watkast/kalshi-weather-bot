# 15-Minute 1¢ Study

*Updated Mon Sep 28, 9:41 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 51 finished bets | 4% | $20.35 | +266% | +39.90¢ | $24.25 / -$3.90 |

*Expect about **49 buys a day** (~$7.34/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 182 | $18.45 | +78% |
| Mean-reversion model ≥ 2%, hold to the close | 277 | $6.60 | +19% |
| 5+ min left, sell at 50¢ | 51 | $5.85 | +76% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1453 | 1447 | 8 (1%) | 1.07% | -$62.30 (-36%) | Hold to the close: -$62.30 (-36%) |

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
| Volatility model | 721 | 2.9% | 0.6% (4) | -336% | ❌ Worse |
| Momentum model | 721 | 3.1% | 0.6% (4) | -411% | ❌ Worse |
| Mean-reversion model | 721 | 5.9% | 0.6% (4) | -385% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 721 | 4 | -28% | -89% | -90% | -84% |
| Volatility model ≥ 2% | 138 | 1 | -14% | -84% | -83% | -76% |
| Volatility model ≥ 5% | 68 | 0 | -100% | -72% | -69% | -57% |
| Volatility model ≥ 10% | 36 | 0 | -100% | -70% | -66% | -43% |
| Momentum model ≥ 2% | 116 | 0 | -100% | -84% | -88% | -85% |
| Momentum model ≥ 5% | 68 | 0 | -100% | -82% | -89% | -82% |
| Momentum model ≥ 10% | 46 | 0 | -100% | -88% | -82% | -70% |
| Mean-reversion model ≥ 2% | 277 | 3 | +19% | -85% | -85% | -78% |
| Mean-reversion model ≥ 5% | 182 | 3 | +78% | -82% | -82% | -72% |
| Mean-reversion model ≥ 10% | 114 | 2 | +99% | -78% | -78% | -68% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 916 | 5% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 449 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 82 | 4% | 4% | 2% | 2% | 2% | 2% |
| **All** | 1447 | 4% | 2% | 2% | 2% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 1% | -$62.30 | -36% | — |
| Sell at 2¢ | 51 | 4% | -$161.04 | -92% | 47 sec |
| Sell at 3¢ | 33 | 2% | -$161.43 | -93% | 47 sec |
| Sell at 5¢ | 24 | 2% | -$158.70 | -91% | 80 sec |
| Sell at 10¢ | 22 | 2% | -$145.48 | -83% | 1.7 min |
| Sell at 25¢ | 12 | 1% | -$134.58 | -77% | 1.9 min |
| Sell at 50¢ | 8 | 1% | -$120.30 | -69% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 51 | 2 | 6% | 4% | +266% | -90% | -85% |
| 2–5 min | 494 | 5 | 7% | 3% | -2% | -87% | -88% |
| 1–2 min | 407 | 1 | 2% | 1% | -73% | -96% | -96% |
| Under 1 min | 495 | 0 | 1% | 0% | -100% | -98% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 105 | 2 | 6% | 4% | +136% | -87% | -84% |
| ZEC | 104 | 1 | 7% | 2% | +18% | -85% | -93% |
| DOGE | 103 | 1 | 5% | 3% | +17% | -89% | -84% |
| NEAR | 102 | 0 | 3% | 1% | -100% | -92% | -96% |
| BTC | 102 | 0 | 9% | 3% | -100% | -77% | -85% |
| XRP | 102 | 2 | 4% | 3% | +146% | -91% | -90% |
| SOL | 101 | 0 | 3% | 2% | -100% | -92% | -88% |
| BNB | 100 | 0 | 2% | 1% | -100% | -96% | -94% |
| HYPE | 97 | 0 | 3% | 2% | -100% | -93% | -93% |
| GOLD | 79 | 0 | 3% | 0% | -100% | -94% | -100% |
| WTI | 72 | 0 | 1% | 0% | -100% | -97% | -100% |
| SILVER | 69 | 0 | 1% | 0% | -100% | -97% | -95% |
| NATGAS | 64 | 0 | 3% | 2% | -100% | -95% | -92% |
| COPPER | 61 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 59 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 45 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 31 | 0 | 3% | 0% | -100% | -94% | -92% |
| EURUSD | 27 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 24 | 2 | 8% | 8% | +678% | -86% | -78% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 771 | 5 | 4% | 2% | -24% | -91% | -91% |
| DOWN (bought NO) | 676 | 3 | 3% | 1% | -49% | -94% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 89 | 0 | 3% | 2% | -100% | -87% | -87% |
| 0.05–0.1% | 98 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 198 | 0 | 4% | 2% | -100% | -89% | -88% |
| 0.2–0.5% | 359 | 2 | 5% | 3% | -38% | -90% | -91% |
| Over 0.5% | 172 | 4 | 7% | 3% | +147% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 471 | 2 | 4% | 2% | -51% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,974 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 9:29:55 PM | NATGAS | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:29:24 PM | PALLADIUM | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:29:08 PM | GBPUSD | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:28:51 PM | PLATINUM | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:28:51 PM | EURUSD | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:28:37 PM | COPPER | DOWN | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:28:37 PM | GOLD | DOWN | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:27:02 PM | ZEC | DOWN | 3.0 min | +0.553% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:27:02 PM | XRP | DOWN | 3.0 min | +0.840% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:26:46 PM | HYPE | DOWN | 3.2 min | +0.406% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:26:31 PM | SILVER | DOWN | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:25:59 PM | ETH | DOWN | 4.0 min | +0.264% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:25:43 PM | BNB | DOWN | 4.3 min | +0.292% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:25:28 PM | BTC | DOWN | 4.5 min | +0.289% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:25:28 PM | SOL | DOWN | 4.5 min | +0.652% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:25:28 PM | DOGE | DOWN | 4.5 min | +1.087% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 9:25:12 PM | NEAR | DOWN | 4.8 min | +1.694% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:14:50 PM | PLATINUM | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:14:50 PM | XRP | DOWN | 10 sec | +0.075% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:14:35 PM | PALLADIUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:14:19 PM | BTC | UP | 40 sec | -0.074% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:14:19 PM | SOL | DOWN | 40 sec | +0.113% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:14:19 PM | COPPER | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:14:19 PM | ZEC | UP | 40 sec | -0.114% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:14:19 PM | GOLD | UP | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:14:19 PM | BNB | DOWN | 40 sec | +0.001% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:14:03 PM | NATGAS | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:13:47 PM | WTI | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:13:47 PM | ETH | DOWN | 73 sec | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:13:16 PM | HYPE | UP | 1.7 min | -0.187% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
