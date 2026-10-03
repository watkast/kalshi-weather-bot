# 15-Minute 1¢ Study

*Updated Fri Oct 2, 11:18 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 171 finished bets | 1% | $2.80 | +11% | +1.64¢ | $15.40 / -$12.60 |

*Expect about **33 buys a day** (~$5.02/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 399 | -$0.00 | -0% |
| Momentum model ≥ 5%, sell at 50¢ | 399 | -$7.25 | -17% |
| 5+ min left, sell at 50¢ | 171 | -$11.70 | -46% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6257 | 6251 | 23 (0%) | 1.07% | -$434.45 (-57%) | Hold to the close: -$434.45 (-57%) |

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
| Volatility model | 3715 | 3.9% | 0.3% (11) | -694% | ❌ Worse |
| Momentum model | 3715 | 4.0% | 0.3% (11) | -737% | ❌ Worse |
| Mean-reversion model | 3715 | 6.9% | 0.3% (11) | -851% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3715 | 11 | -62% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 782 | 5 | -26% | -66% | -66% | -61% |
| Volatility model ≥ 5% | 399 | 2 | -34% | -46% | -46% | -41% |
| Volatility model ≥ 10% | 234 | 2 | +31% | -12% | -14% | -7% |
| Momentum model ≥ 2% | 687 | 4 | -29% | -65% | -68% | -64% |
| Momentum model ≥ 5% | 399 | 3 | -0% | -51% | -54% | -48% |
| Momentum model ≥ 10% | 270 | 2 | +9% | -32% | -33% | -28% |
| Mean-reversion model ≥ 2% | 1401 | 7 | -46% | -84% | -86% | -81% |
| Mean-reversion model ≥ 5% | 938 | 6 | -30% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 610 | 4 | -25% | -77% | -81% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3912 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6251 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 23 | 0% | -$434.45 | -57% | — |
| Sell at 2¢ | 245 | 4% | -$678.75 | -90% | 43 sec |
| Sell at 3¢ | 153 | 2% | -$682.78 | -90% | 48 sec |
| Sell at 5¢ | 114 | 2% | -$668.35 | -88% | 64 sec |
| Sell at 10¢ | 75 | 1% | -$630.20 | -83% | 81 sec |
| Sell at 25¢ | 40 | 1% | -$582.05 | -77% | 1.6 min |
| Sell at 50¢ | 21 | 0% | -$530.70 | -70% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 2042 | 12 | 8% | 3% | -43% | -86% | -87% |
| 1–2 min | 1622 | 6 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 2416 | 3 | 1% | 0% | -82% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 442 | 2 | 4% | 1% | -40% | -90% | -91% |
| ZEC | 438 | 2 | 5% | 3% | -46% | -88% | -90% |
| HYPE | 437 | 2 | 5% | 4% | -44% | -88% | -85% |
| ETH | 436 | 2 | 6% | 3% | -43% | -86% | -86% |
| BTC | 434 | 1 | 6% | 3% | -70% | -84% | -88% |
| BNB | 434 | 0 | 4% | 2% | -100% | -91% | -92% |
| XRP | 432 | 3 | 2% | 1% | -10% | -66% | -67% |
| SOL | 431 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 428 | 1 | 6% | 2% | -68% | -86% | -88% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 274 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 225 | 2 | 4% | 2% | -17% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3182 | 14 | 4% | 2% | -49% | -91% | -91% |
| DOWN (bought NO) | 3069 | 9 | 4% | 2% | -66% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 499 | 2 | 1% | 1% | -24% | -59% | -58% |
| 0.05–0.1% | 574 | 0 | 3% | 1% | -100% | -91% | -94% |
| 0.1–0.2% | 958 | 2 | 4% | 2% | -72% | -90% | -91% |
| 0.2–0.5% | 1289 | 5 | 6% | 3% | -57% | -88% | -87% |
| Over 0.5% | 590 | 4 | 7% | 3% | -30% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1640 | 9 | 5% | 3% | -38% | -90% | -88% |
| Afternoon (12–6pm) | 1305 | 3 | 4% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1832 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,214 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 11:14:04 PM | ETH | UP | 56 sec | -0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:14:04 PM | SOL | DOWN | 56 sec | +0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/2 11:14:04 PM | DOGE | DOWN | 56 sec | +0.104% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:14:04 PM | BTC | UP | 56 sec | -0.023% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:13:46 PM | ZEC | DOWN | 74 sec | +0.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:13:30 PM | XRP | DOWN | 1.5 min | +0.094% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:12:59 PM | HYPE | DOWN | 2.0 min | +0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:10:19 PM | NEAR | DOWN | 4.7 min | +0.814% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:59:49 PM | HYPE | UP | 11 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:59:33 PM | DOGE | DOWN | 27 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:59:02 PM | SOL | DOWN | 57 sec | +0.078% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:58:44 PM | ETH | DOWN | 75 sec | +0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:58:44 PM | BTC | DOWN | 75 sec | +0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:58:28 PM | XRP | DOWN | 1.5 min | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:57:10 PM | BNB | DOWN | 2.8 min | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:44:49 PM | ETH | UP | 10 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:44:17 PM | ZEC | DOWN | 42 sec | +0.141% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:44:17 PM | BTC | DOWN | 42 sec | +0.017% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:44:17 PM | SOL | DOWN | 42 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/2 10:44:17 PM | NEAR | DOWN | 42 sec | +0.067% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:44:01 PM | HYPE | DOWN | 59 sec | +0.121% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:42:56 PM | DOGE | UP | 2.0 min | -0.159% | 2¢ | ❌ Lost | -$0.15 |
| 10/2 10:42:24 PM | XRP | UP | 2.6 min | -0.249% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:40:32 PM | BNB | UP | 4.5 min | -0.149% | 47¢ | ❌ Lost | -$0.15 |
| 10/2 10:28:30 PM | XRP | UP | 89 sec | -0.094% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:28:14 PM | HYPE | UP | 1.8 min | -0.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:27:42 PM | SOL | UP | 2.3 min | -0.216% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:26:54 PM | DOGE | UP | 3.1 min | -0.201% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 10:26:22 PM | ZEC | UP | 3.6 min | -0.333% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 10:26:06 PM | BTC | UP | 3.9 min | -0.102% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
