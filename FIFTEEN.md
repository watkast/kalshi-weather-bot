# 15-Minute 1¢ Study

*Updated Mon Sep 28, 11:48 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 52 finished bets | 4% | $20.20 | +259% | +38.85¢ | $24.10 / -$3.90 |

*Expect about **46 buys a day** (~$6.90/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 191 | $17.10 | +69% |
| 5+ min left, sell at 50¢ | 52 | $5.70 | +73% |
| Mean-reversion model ≥ 2%, hold to the close | 291 | $4.65 | +12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1558 | 1552 | 8 (1%) | 1.07% | -$74.60 (-40%) | Hold to the close: -$74.60 (-40%) |

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
| Volatility model | 783 | 2.8% | 0.5% (4) | -328% | ❌ Worse |
| Momentum model | 783 | 3.0% | 0.5% (4) | -405% | ❌ Worse |
| Mean-reversion model | 783 | 5.7% | 0.5% (4) | -383% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 783 | 4 | -34% | -89% | -90% | -85% |
| Volatility model ≥ 2% | 151 | 1 | -23% | -84% | -85% | -79% |
| Volatility model ≥ 5% | 69 | 0 | -100% | -72% | -69% | -57% |
| Volatility model ≥ 10% | 36 | 0 | -100% | -70% | -66% | -43% |
| Momentum model ≥ 2% | 127 | 0 | -100% | -84% | -89% | -87% |
| Momentum model ≥ 5% | 76 | 0 | -100% | -81% | -91% | -85% |
| Momentum model ≥ 10% | 51 | 0 | -100% | -89% | -84% | -74% |
| Mean-reversion model ≥ 2% | 291 | 3 | +12% | -85% | -84% | -77% |
| Mean-reversion model ≥ 5% | 191 | 3 | +69% | -82% | -81% | -71% |
| Mean-reversion model ≥ 10% | 119 | 2 | +89% | -77% | -76% | -65% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 978 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 481 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 93 | 3% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1552 | 3% | 2% | 2% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 1% | -$74.60 | -40% | — |
| Sell at 2¢ | 53 | 3% | -$172.82 | -93% | 47 sec |
| Sell at 3¢ | 34 | 2% | -$173.34 | -93% | 47 sec |
| Sell at 5¢ | 25 | 2% | -$170.35 | -91% | 81 sec |
| Sell at 10¢ | 23 | 1% | -$156.47 | -84% | 1.9 min |
| Sell at 25¢ | 13 | 1% | -$143.57 | -77% | 2.1 min |
| Sell at 50¢ | 9 | 1% | -$125.85 | -67% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 52 | 2 | 6% | 4% | +259% | -90% | -85% |
| 2–5 min | 518 | 5 | 7% | 3% | -6% | -87% | -89% |
| 1–2 min | 441 | 1 | 2% | 1% | -75% | -95% | -96% |
| Under 1 min | 541 | 0 | 1% | 0% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 112 | 2 | 5% | 4% | +122% | -88% | -85% |
| ZEC | 111 | 1 | 6% | 2% | +10% | -86% | -94% |
| DOGE | 110 | 1 | 5% | 3% | +11% | -90% | -85% |
| NEAR | 109 | 0 | 5% | 2% | -100% | -88% | -93% |
| BTC | 109 | 0 | 8% | 3% | -100% | -79% | -86% |
| XRP | 109 | 2 | 4% | 3% | +136% | -91% | -90% |
| SOL | 108 | 0 | 3% | 2% | -100% | -92% | -89% |
| BNB | 106 | 0 | 2% | 1% | -100% | -96% | -94% |
| HYPE | 104 | 0 | 3% | 2% | -100% | -94% | -94% |
| GOLD | 85 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 76 | 0 | 1% | 0% | -100% | -97% | -100% |
| SILVER | 75 | 0 | 1% | 0% | -100% | -97% | -96% |
| NATGAS | 67 | 0 | 3% | 1% | -100% | -95% | -92% |
| COPPER | 66 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 64 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 48 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 35 | 0 | 3% | 0% | -100% | -95% | -93% |
| EURUSD | 30 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 28 | 2 | 7% | 7% | +567% | -88% | -81% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 837 | 5 | 4% | 2% | -30% | -91% | -91% |
| DOWN (bought NO) | 715 | 3 | 3% | 1% | -51% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 98 | 0 | 3% | 2% | -100% | -88% | -88% |
| 0.05–0.1% | 111 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 220 | 0 | 4% | 1% | -100% | -90% | -89% |
| 0.2–0.5% | 372 | 2 | 5% | 3% | -40% | -89% | -91% |
| Over 0.5% | 177 | 4 | 7% | 4% | +139% | -86% | -85% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 576 | 2 | 4% | 2% | -59% | -91% | -90% |

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
| 9/28 11:44:56 PM | XRP | UP | 4 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 9/28 11:44:56 PM | GBPUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:44:56 PM | BTC | UP | 4 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 9/28 11:44:40 PM | BNB | UP | 20 sec | -0.042% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:44:40 PM | SOL | UP | 20 sec | -0.140% | 0¢ | ❌ Lost | $0.00 |
| 9/28 11:43:51 PM | PALLADIUM | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:43:51 PM | GOLD | DOWN | 68 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:43:19 PM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:43:05 PM | SILVER | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:42:17 PM | ZEC | UP | 2.7 min | -0.524% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:42:17 PM | DOGE | UP | 2.7 min | -0.427% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:41:12 PM | ETH | UP | 3.8 min | -0.380% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:40:22 PM | NEAR | UP | 4.6 min | -1.019% | 56¢ | ❌ Lost | -$0.15 |
| 9/28 11:39:03 PM | HYPE | UP | 5.9 min | -0.802% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
