# 15-Minute 1¢ Study

*Updated Mon Oct 5, 5:34 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 589 finished bets | 1% | $34.70 | +55% | +5.89¢ | -$18.25 / $52.95 |

*Expect about **82 buys a day** (~$12.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1093 | $22.45 | +17% |
| Momentum model ≥ 5%, hold to the close | 588 | $21.45 | +34% |
| 5+ min left, hold to the close | 211 | $10.80 | +35% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8405 | 8399 | 37 (0%) | 1.07% | -$490.75 (-49%) | Hold to the close: -$490.75 (-49%) |

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
| Volatility model | 5554 | 4.2% | 0.5% (25) | -599% | ❌ Worse |
| Momentum model | 5554 | 4.2% | 0.5% (25) | -624% | ❌ Worse |
| Mean-reversion model | 5554 | 6.9% | 0.5% (25) | -701% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5554 | 25 | -43% | -85% | -85% | -82% |
| Volatility model ≥ 2% | 1093 | 11 | +17% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 589 | 7 | +55% | -56% | -54% | -50% |
| Volatility model ≥ 10% | 366 | 5 | +102% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 959 | 8 | +1% | -70% | -72% | -69% |
| Momentum model ≥ 5% | 588 | 6 | +34% | -61% | -63% | -60% |
| Momentum model ≥ 10% | 409 | 5 | +75% | -48% | -48% | -45% |
| Mean-reversion model ≥ 2% | 1933 | 14 | -21% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1299 | 12 | +3% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 860 | 9 | +21% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5751 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2007 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 641 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8399 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$490.75 | -49% | — |
| Sell at 2¢ | 328 | 4% | -$895.47 | -89% | 33 sec |
| Sell at 3¢ | 213 | 3% | -$897.68 | -89% | 47 sec |
| Sell at 5¢ | 158 | 2% | -$878.05 | -87% | 61 sec |
| Sell at 10¢ | 106 | 1% | -$827.89 | -82% | 66 sec |
| Sell at 25¢ | 59 | 1% | -$743.46 | -74% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$653.75 | -65% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 208 | 3 | 12% | 3% | +37% | -80% | -87% |
| 2–5 min | 2721 | 20 | 7% | 4% | -28% | -86% | -87% |
| 1–2 min | 2212 | 9 | 3% | 2% | -56% | -93% | -93% |
| Under 1 min | 3255 | 5 | 1% | 0% | -77% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 651 | 5 | 5% | 3% | -8% | -89% | -89% |
| ETH | 642 | 5 | 6% | 3% | -2% | -86% | -86% |
| DOGE | 642 | 2 | 4% | 2% | -60% | -90% | -90% |
| HYPE | 641 | 3 | 5% | 3% | -43% | -88% | -86% |
| BNB | 638 | 2 | 4% | 2% | -63% | -91% | -93% |
| XRP | 636 | 4 | 2% | 1% | -20% | -76% | -77% |
| SOL | 636 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 634 | 3 | 6% | 2% | -38% | -87% | -90% |
| NEAR | 631 | 3 | 6% | 3% | -38% | -63% | -64% |
| GOLD | 338 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 326 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 308 | 2 | 3% | 1% | -30% | -95% | -96% |
| COPPER | 285 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 253 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 251 | 2 | 4% | 2% | -26% | -94% | -92% |
| PALLADIUM | 246 | 1 | 2% | 1% | -62% | -96% | -98% |
| EURUSD | 229 | 1 | 5% | 3% | -59% | -92% | -90% |
| GBPUSD | 219 | 1 | 4% | 2% | -57% | -94% | -94% |
| USDJPY | 193 | 3 | 2% | 2% | +45% | -96% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4227 | 20 | 4% | 2% | -45% | -88% | -88% |
| DOWN (bought NO) | 4172 | 17 | 4% | 2% | -53% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 957 | 7 | 2% | 1% | +24% | -58% | -58% |
| 0.05–0.1% | 968 | 2 | 3% | 1% | -69% | -91% | -92% |
| 0.1–0.2% | 1435 | 6 | 4% | 2% | -47% | -90% | -91% |
| 0.2–0.5% | 1691 | 8 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 698 | 4 | 7% | 3% | -41% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2196 | 9 | 4% | 2% | -52% | -86% | -87% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,134 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 5:29:33 AM | GOLD | DOWN | 27 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 5:29:23 AM | COPPER | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:29:17 AM | GBPUSD | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:29:17 AM | NEAR | DOWN | 43 sec | +0.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:28:07 AM | NATGAS | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:27:49 AM | PLATINUM | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:27:47 AM | BNB | DOWN | 2.2 min | +0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/5 5:27:43 AM | DOGE | DOWN | 2.3 min | +0.286% | 0¢ | ❌ Lost | $0.00 |
| 10/5 5:27:43 AM | WTI | UP | 2.3 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 5:27:29 AM | XRP | DOWN | 2.5 min | +0.258% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:27:29 AM | EURUSD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:26:50 AM | BTC | DOWN | 3.1 min | +0.137% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:26:29 AM | SOL | DOWN | 3.5 min | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:26:23 AM | ETH | DOWN | 3.6 min | +0.167% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:26:01 AM | USDJPY | DOWN | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:25:49 AM | PALLADIUM | DOWN | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:25:33 AM | HYPE | DOWN | 4.4 min | +0.292% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:25:29 AM | ZEC | DOWN | 4.5 min | +0.378% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:14:59 AM | WTI | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 5:14:55 AM | ZEC | DOWN | 5 sec | +0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:14:51 AM | USDJPY | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:14:39 AM | SILVER | DOWN | 21 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 5:14:29 AM | COPPER | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:14:16 AM | NEAR | UP | 43 sec | -0.209% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:13:52 AM | HYPE | DOWN | 67 sec | +0.213% | 0¢ | ❌ Lost | $0.00 |
| 10/5 5:13:08 AM | DOGE | UP | 1.9 min | -0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:12:17 AM | SOL | UP | 2.7 min | -0.175% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:10:50 AM | BTC | UP | 4.2 min | -0.193% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:10:29 AM | XRP | UP | 4.5 min | -0.355% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:10:09 AM | ETH | UP | 4.8 min | -0.193% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
