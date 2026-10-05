# 15-Minute 1¢ Study

*Updated Mon Oct 5, 10:42 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 599 finished bets | 1% | $33.35 | +52% | +5.57¢ | -$4.70 / $38.05 |

*Expect about **81 buys a day** (~$12.13/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 601 | $19.80 | +31% |
| Volatility model ≥ 2%, hold to the close | 1117 | $19.15 | +14% |
| 5+ min left, hold to the close | 221 | $9.30 | +28% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8647 | 8637 | 37 (0%) | 1.07% | -$520.75 (-50%) | Hold to the close: -$520.75 (-50%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 5695 | 4.1% | 0.4% (25) | -605% | ❌ Worse |
| Momentum model | 5695 | 4.2% | 0.4% (25) | -630% | ❌ Worse |
| Mean-reversion model | 5695 | 6.8% | 0.4% (25) | -707% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5695 | 25 | -45% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1117 | 11 | +14% | -70% | -70% | -65% |
| Volatility model ≥ 5% | 599 | 7 | +52% | -56% | -55% | -51% |
| Volatility model ≥ 10% | 372 | 5 | +98% | -37% | -38% | -33% |
| Momentum model ≥ 2% | 986 | 8 | -2% | -70% | -73% | -70% |
| Momentum model ≥ 5% | 601 | 6 | +31% | -62% | -64% | -61% |
| Momentum model ≥ 10% | 417 | 5 | +71% | -49% | -50% | -47% |
| Mean-reversion model ≥ 2% | 1972 | 14 | -23% | -83% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1322 | 12 | +1% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 872 | 9 | +19% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5892 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2077 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 668 | 3% | 3% | 2% | 1% | 1% | 0% |
| **All** | 8637 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$520.75 | -50% | — |
| Sell at 2¢ | 334 | 4% | -$923.91 | -89% | 33 sec |
| Sell at 3¢ | 217 | 3% | -$926.12 | -89% | 47 sec |
| Sell at 5¢ | 161 | 2% | -$906.10 | -87% | 61 sec |
| Sell at 10¢ | 107 | 1% | -$856.58 | -82% | 66 sec |
| Sell at 25¢ | 59 | 1% | -$773.46 | -74% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$683.75 | -66% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 218 | 3 | 11% | 3% | +30% | -81% | -88% |
| 2–5 min | 2804 | 20 | 7% | 4% | -30% | -87% | -87% |
| 1–2 min | 2276 | 9 | 3% | 2% | -57% | -93% | -93% |
| Under 1 min | 3336 | 5 | 1% | 0% | -77% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 666 | 5 | 5% | 3% | -10% | -89% | -89% |
| DOGE | 658 | 2 | 4% | 2% | -61% | -91% | -90% |
| ETH | 657 | 5 | 6% | 3% | -4% | -87% | -87% |
| HYPE | 657 | 3 | 5% | 3% | -44% | -89% | -87% |
| BNB | 653 | 2 | 4% | 2% | -63% | -90% | -92% |
| XRP | 652 | 4 | 2% | 1% | -22% | -77% | -77% |
| SOL | 652 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 650 | 3 | 6% | 2% | -39% | -86% | -89% |
| NEAR | 647 | 3 | 6% | 3% | -40% | -64% | -65% |
| GOLD | 350 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 336 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 319 | 2 | 3% | 1% | -33% | -94% | -96% |
| COPPER | 295 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 263 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 259 | 2 | 3% | 2% | -28% | -94% | -92% |
| PALLADIUM | 255 | 1 | 2% | 1% | -63% | -97% | -98% |
| EURUSD | 238 | 1 | 5% | 3% | -61% | -92% | -90% |
| GBPUSD | 229 | 1 | 3% | 2% | -59% | -94% | -94% |
| USDJPY | 201 | 3 | 2% | 1% | +39% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4378 | 20 | 4% | 2% | -47% | -89% | -88% |
| DOWN (bought NO) | 4259 | 17 | 4% | 2% | -54% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 971 | 7 | 2% | 1% | +23% | -59% | -58% |
| 0.05–0.1% | 982 | 2 | 3% | 1% | -70% | -91% | -92% |
| 0.1–0.2% | 1469 | 6 | 4% | 2% | -48% | -91% | -91% |
| 0.2–0.5% | 1745 | 8 | 6% | 3% | -50% | -88% | -87% |
| Over 0.5% | 723 | 4 | 7% | 3% | -43% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2264 | 17 | 5% | 3% | -14% | -89% | -88% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,121 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 10:42:11 AM | BNB | DOWN | 2.8 min | +0.154% | — | In play | — |
| 10/5 10:41:55 AM | SOL | DOWN | 3.1 min | +0.185% | — | In play | — |
| 10/5 10:40:18 AM | HYPE | DOWN | 4.7 min | +0.656% | — | In play | — |
| 10/5 10:40:18 AM | NEAR | DOWN | 4.7 min | +1.133% | — | In play | — |
| 10/5 10:29:52 AM | GBPUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:29:52 AM | GOLD | UP | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 10:29:52 AM | COPPER | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:29:36 AM | SILVER | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:29:36 AM | NATGAS | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:29:20 AM | WTI | UP | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 10:29:04 AM | EURUSD | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:28:47 AM | PLATINUM | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:28:31 AM | PALLADIUM | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:28:31 AM | BTC | UP | 88 sec | -0.143% | 0¢ | ❌ Lost | $0.00 |
| 10/5 10:28:31 AM | HYPE | UP | 88 sec | -0.257% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:27:59 AM | NEAR | UP | 2.0 min | -0.491% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 10:27:43 AM | XRP | UP | 2.3 min | -0.388% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 10:27:43 AM | SOL | UP | 2.3 min | -0.298% | 0¢ | ❌ Lost | $0.00 |
| 10/5 10:27:27 AM | ZEC | UP | 2.5 min | -0.498% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 10:27:27 AM | DOGE | UP | 2.5 min | -0.504% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:26:21 AM | BNB | UP | 3.6 min | -0.230% | 5¢ | ❌ Lost | -$0.15 |
| 10/5 10:26:05 AM | ETH | UP | 3.9 min | -0.361% | 2¢ | ❌ Lost | -$0.15 |
| 10/5 10:14:52 AM | ETH | UP | 7 sec | -0.007% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 10:14:52 AM | BNB | DOWN | 7 sec | -0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/5 10:14:52 AM | BTC | UP | 7 sec | -0.024% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 10:14:36 AM | NATGAS | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:14:20 AM | ZEC | UP | 39 sec | -0.165% | 0¢ | ❌ Lost | $0.00 |
| 10/5 10:14:20 AM | SOL | DOWN | 39 sec | +0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/5 10:14:20 AM | HYPE | DOWN | 39 sec | +0.106% | 0¢ | ❌ Lost | $0.00 |
| 10/5 10:14:04 AM | PALLADIUM | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
