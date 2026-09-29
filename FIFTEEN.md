# 15-Minute 1¢ Study

*Updated Mon Sep 28, 9:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 51 finished bets | 4% | $20.35 | +266% | +39.90¢ | $24.25 / -$3.90 |

*Expect about **50 buys a day** (~$7.44/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 177 | $19.20 | +84% |
| Mean-reversion model ≥ 2%, hold to the close | 271 | $7.50 | +22% |
| 5+ min left, sell at 50¢ | 51 | $5.85 | +76% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1436 | 1430 | 8 (1%) | 1.07% | -$59.75 (-35%) | Hold to the close: -$59.75 (-35%) |

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
| Volatility model | 712 | 3.0% | 0.6% (4) | -338% | ❌ Worse |
| Momentum model | 712 | 3.1% | 0.6% (4) | -412% | ❌ Worse |
| Mean-reversion model | 712 | 5.9% | 0.6% (4) | -383% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 712 | 4 | -27% | -88% | -89% | -84% |
| Volatility model ≥ 2% | 137 | 1 | -14% | -84% | -83% | -76% |
| Volatility model ≥ 5% | 68 | 0 | -100% | -72% | -69% | -57% |
| Volatility model ≥ 10% | 36 | 0 | -100% | -70% | -66% | -43% |
| Momentum model ≥ 2% | 116 | 0 | -100% | -84% | -88% | -85% |
| Momentum model ≥ 5% | 68 | 0 | -100% | -82% | -89% | -82% |
| Momentum model ≥ 10% | 46 | 0 | -100% | -88% | -82% | -70% |
| Mean-reversion model ≥ 2% | 271 | 3 | +22% | -84% | -84% | -77% |
| Mean-reversion model ≥ 5% | 177 | 3 | +84% | -82% | -81% | -71% |
| Mean-reversion model ≥ 10% | 111 | 2 | +105% | -77% | -77% | -67% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 907 | 5% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 443 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 80 | 4% | 4% | 2% | 2% | 2% | 2% |
| **All** | 1430 | 4% | 2% | 2% | 2% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 1% | -$59.75 | -35% | — |
| Sell at 2¢ | 51 | 4% | -$158.49 | -92% | 47 sec |
| Sell at 3¢ | 33 | 2% | -$158.88 | -93% | 47 sec |
| Sell at 5¢ | 24 | 2% | -$156.15 | -91% | 80 sec |
| Sell at 10¢ | 22 | 2% | -$142.93 | -83% | 1.7 min |
| Sell at 25¢ | 12 | 1% | -$132.03 | -77% | 1.9 min |
| Sell at 50¢ | 8 | 1% | -$117.75 | -69% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 51 | 2 | 6% | 4% | +266% | -90% | -85% |
| 2–5 min | 484 | 5 | 7% | 3% | +1% | -87% | -88% |
| 1–2 min | 403 | 1 | 2% | 1% | -73% | -95% | -95% |
| Under 1 min | 492 | 0 | 1% | 0% | -100% | -98% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 104 | 2 | 6% | 4% | +139% | -87% | -83% |
| ZEC | 103 | 1 | 7% | 2% | +20% | -84% | -93% |
| DOGE | 102 | 1 | 5% | 3% | +18% | -89% | -84% |
| NEAR | 101 | 0 | 3% | 1% | -100% | -92% | -96% |
| BTC | 101 | 0 | 9% | 3% | -100% | -77% | -85% |
| XRP | 101 | 2 | 4% | 3% | +149% | -91% | -90% |
| SOL | 100 | 0 | 3% | 2% | -100% | -92% | -88% |
| BNB | 99 | 0 | 2% | 1% | -100% | -96% | -93% |
| HYPE | 96 | 0 | 3% | 2% | -100% | -93% | -93% |
| GOLD | 78 | 0 | 3% | 0% | -100% | -94% | -100% |
| WTI | 72 | 0 | 1% | 0% | -100% | -97% | -100% |
| SILVER | 68 | 0 | 1% | 0% | -100% | -97% | -95% |
| NATGAS | 63 | 0 | 3% | 2% | -100% | -94% | -92% |
| COPPER | 60 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 58 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 44 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 30 | 0 | 3% | 0% | -100% | -94% | -91% |
| EURUSD | 26 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 24 | 2 | 8% | 8% | +678% | -86% | -78% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 771 | 5 | 4% | 2% | -24% | -91% | -91% |
| DOWN (bought NO) | 659 | 3 | 3% | 1% | -47% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 89 | 0 | 3% | 2% | -100% | -87% | -87% |
| 0.05–0.1% | 98 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 198 | 0 | 4% | 2% | -100% | -89% | -88% |
| 0.2–0.5% | 355 | 2 | 5% | 3% | -37% | -90% | -90% |
| Over 0.5% | 167 | 4 | 7% | 4% | +156% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 454 | 2 | 5% | 2% | -48% | -90% | -88% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,964 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
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
| 9/28 9:12:01 PM | NEAR | UP | 3.0 min | -0.854% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:59:49 PM | SOL | DOWN | 10 sec | +0.018% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:59:34 PM | COPPER | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:59:34 PM | DOGE | UP | 26 sec | -0.078% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:59:34 PM | BNB | DOWN | 26 sec | +0.034% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:59:18 PM | BTC | UP | 42 sec | -0.054% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:59:18 PM | ETH | UP | 42 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:59:18 PM | NEAR | UP | 42 sec | -0.185% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:59:18 PM | NATGAS | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:59:18 PM | GBPUSD | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:59:18 PM | XRP | UP | 42 sec | -0.074% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:59:02 PM | HYPE | DOWN | 58 sec | +0.232% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:57:59 PM | USDJPY | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:57:43 PM | ZEC | UP | 2.3 min | -0.544% | 3¢ | ❌ Lost | -$0.15 |
| 9/28 8:44:52 PM | PLATINUM | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:44:37 PM | NEAR | UP | 22 sec | -0.150% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:44:21 PM | BTC | DOWN | 38 sec | +0.052% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
