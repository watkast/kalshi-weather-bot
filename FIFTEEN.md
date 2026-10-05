# 15-Minute 1¢ Study

*Updated Mon Oct 5, 1:25 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 615 finished bets | 1% | $31.70 | +48% | +5.15¢ | -$5.75 / $37.45 |

*Expect about **82 buys a day** (~$12.25/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 616 | $18.15 | +28% |
| Volatility model ≥ 2%, hold to the close | 1142 | $16.30 | +12% |
| 5+ min left, hold to the close | 224 | $8.85 | +27% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8808 | 8801 | 37 (0%) | 1.07% | -$541.45 (-51%) | Hold to the close: -$541.45 (-51%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 5793 | 4.1% | 0.4% (25) | -609% | ❌ Worse |
| Momentum model | 5793 | 4.2% | 0.4% (25) | -634% | ❌ Worse |
| Mean-reversion model | 5793 | 6.8% | 0.4% (25) | -712% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5793 | 25 | -46% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1142 | 11 | +12% | -70% | -70% | -65% |
| Volatility model ≥ 5% | 615 | 7 | +48% | -57% | -57% | -52% |
| Volatility model ≥ 10% | 380 | 5 | +94% | -38% | -39% | -34% |
| Momentum model ≥ 2% | 1009 | 8 | -4% | -71% | -73% | -71% |
| Momentum model ≥ 5% | 616 | 6 | +28% | -62% | -65% | -62% |
| Momentum model ≥ 10% | 426 | 5 | +68% | -50% | -51% | -48% |
| Mean-reversion model ≥ 2% | 2006 | 14 | -24% | -83% | -83% | -79% |
| Mean-reversion model ≥ 5% | 1348 | 12 | -1% | -79% | -80% | -73% |
| Mean-reversion model ≥ 10% | 891 | 9 | +17% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5990 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2127 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 684 | 3% | 3% | 2% | 1% | 1% | 0% |
| **All** | 8801 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$541.45 | -51% | — |
| Sell at 2¢ | 336 | 4% | -$944.09 | -89% | 33 sec |
| Sell at 3¢ | 219 | 2% | -$946.04 | -89% | 47 sec |
| Sell at 5¢ | 161 | 2% | -$926.80 | -87% | 61 sec |
| Sell at 10¢ | 107 | 1% | -$877.28 | -83% | 66 sec |
| Sell at 25¢ | 59 | 1% | -$794.16 | -75% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$704.45 | -66% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 221 | 3 | 11% | 3% | +28% | -81% | -88% |
| 2–5 min | 2858 | 20 | 7% | 3% | -32% | -87% | -87% |
| 1–2 min | 2320 | 9 | 3% | 2% | -58% | -93% | -93% |
| Under 1 min | 3399 | 5 | 1% | 0% | -78% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 677 | 5 | 5% | 3% | -12% | -89% | -89% |
| DOGE | 669 | 2 | 4% | 1% | -62% | -91% | -90% |
| HYPE | 668 | 3 | 5% | 3% | -45% | -88% | -86% |
| ETH | 667 | 5 | 6% | 3% | -6% | -87% | -87% |
| BNB | 664 | 2 | 4% | 2% | -64% | -90% | -92% |
| XRP | 663 | 4 | 2% | 1% | -23% | -77% | -78% |
| SOL | 663 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 661 | 3 | 5% | 2% | -40% | -87% | -89% |
| NEAR | 658 | 3 | 6% | 3% | -41% | -65% | -66% |
| GOLD | 357 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 342 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 328 | 2 | 3% | 1% | -34% | -95% | -96% |
| COPPER | 301 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 272 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 267 | 2 | 3% | 2% | -30% | -94% | -92% |
| PALLADIUM | 260 | 1 | 2% | 1% | -64% | -97% | -98% |
| EURUSD | 245 | 1 | 4% | 3% | -62% | -92% | -90% |
| GBPUSD | 234 | 1 | 3% | 2% | -60% | -94% | -94% |
| USDJPY | 205 | 3 | 2% | 1% | +37% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4432 | 20 | 4% | 2% | -47% | -89% | -88% |
| DOWN (bought NO) | 4369 | 17 | 4% | 2% | -55% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 991 | 7 | 2% | 1% | +20% | -60% | -59% |
| 0.05–0.1% | 1000 | 2 | 3% | 1% | -70% | -91% | -93% |
| 0.1–0.2% | 1497 | 6 | 4% | 2% | -49% | -91% | -91% |
| 0.2–0.5% | 1769 | 8 | 6% | 3% | -50% | -88% | -87% |
| Over 0.5% | 731 | 4 | 7% | 3% | -44% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1818 | 4 | 3% | 1% | -73% | -86% | -88% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,119 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 1:25:17 PM | NEAR | DOWN | 4.7 min | +0.805% | — | In play | — |
| 10/5 1:14:55 PM | XRP | DOWN | 4 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:14:55 PM | GOLD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 1:14:55 PM | PALLADIUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 1:14:39 PM | BNB | DOWN | 20 sec | -0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:14:23 PM | BTC | DOWN | 36 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:14:23 PM | NATGAS | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 1:14:07 PM | SOL | DOWN | 53 sec | +0.091% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:14:07 PM | NEAR | UP | 53 sec | -0.273% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:13:19 PM | DOGE | UP | 1.7 min | -0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:12:14 PM | ZEC | DOWN | 2.8 min | +0.419% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:12:14 PM | WTI | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:11:58 PM | HYPE | DOWN | 3.0 min | +0.307% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:59:49 PM | COPPER | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:59:49 PM | NEAR | DOWN | 10 sec | +0.124% | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:59:33 PM | XRP | DOWN | 26 sec | +0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:59:33 PM | PALLADIUM | DOWN | 26 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:59:17 PM | ZEC | UP | 42 sec | -0.087% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:59:17 PM | EURUSD | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:59:17 PM | WTI | UP | 42 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:59:03 PM | SOL | DOWN | 57 sec | +0.052% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:59:03 PM | BTC | DOWN | 57 sec | +0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:58:47 PM | NATGAS | UP | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:58:31 PM | GBPUSD | DOWN | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:58:15 PM | USDJPY | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:58:15 PM | BNB | DOWN | 1.8 min | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:58:15 PM | SILVER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:58:15 PM | PLATINUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:57:59 PM | ETH | DOWN | 2.0 min | +0.092% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:57:27 PM | HYPE | UP | 2.5 min | -0.263% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
