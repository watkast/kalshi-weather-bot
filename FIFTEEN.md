# 15-Minute 1¢ Study

*Updated Mon Oct 5, 11:02 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 603 finished bets | 1% | $32.90 | +51% | +5.46¢ | -$5.00 / $37.90 |

*Expect about **81 buys a day** (~$12.17/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 604 | $19.50 | +30% |
| Volatility model ≥ 2%, hold to the close | 1124 | $18.25 | +13% |
| 5+ min left, hold to the close | 223 | $9.00 | +27% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8673 | 8667 | 37 (0%) | 1.07% | -$524.80 (-50%) | Hold to the close: -$524.80 (-50%) |

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
| Volatility model | 5713 | 4.1% | 0.4% (25) | -605% | ❌ Worse |
| Momentum model | 5713 | 4.2% | 0.4% (25) | -630% | ❌ Worse |
| Mean-reversion model | 5713 | 6.8% | 0.4% (25) | -708% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5713 | 25 | -45% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1124 | 11 | +13% | -70% | -70% | -65% |
| Volatility model ≥ 5% | 603 | 7 | +51% | -57% | -56% | -52% |
| Volatility model ≥ 10% | 374 | 5 | +97% | -37% | -39% | -33% |
| Momentum model ≥ 2% | 992 | 8 | -3% | -71% | -73% | -70% |
| Momentum model ≥ 5% | 604 | 6 | +30% | -62% | -64% | -61% |
| Momentum model ≥ 10% | 419 | 5 | +70% | -49% | -50% | -47% |
| Mean-reversion model ≥ 2% | 1984 | 14 | -23% | -83% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1332 | 12 | -0% | -79% | -80% | -73% |
| Mean-reversion model ≥ 10% | 879 | 9 | +18% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5910 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2086 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 671 | 3% | 3% | 2% | 1% | 1% | 0% |
| **All** | 8667 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$524.80 | -50% | — |
| Sell at 2¢ | 334 | 4% | -$927.96 | -89% | 33 sec |
| Sell at 3¢ | 217 | 3% | -$930.17 | -89% | 47 sec |
| Sell at 5¢ | 161 | 2% | -$910.15 | -87% | 61 sec |
| Sell at 10¢ | 107 | 1% | -$860.63 | -83% | 66 sec |
| Sell at 25¢ | 59 | 1% | -$777.51 | -75% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$687.80 | -66% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 220 | 3 | 11% | 3% | +29% | -81% | -88% |
| 2–5 min | 2813 | 20 | 7% | 4% | -31% | -87% | -87% |
| 1–2 min | 2284 | 9 | 3% | 2% | -57% | -93% | -93% |
| Under 1 min | 3347 | 5 | 1% | 0% | -78% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 668 | 5 | 5% | 3% | -10% | -89% | -89% |
| DOGE | 660 | 2 | 4% | 2% | -61% | -91% | -90% |
| ETH | 659 | 5 | 6% | 3% | -4% | -87% | -87% |
| HYPE | 659 | 3 | 5% | 3% | -44% | -89% | -87% |
| BNB | 655 | 2 | 4% | 2% | -64% | -90% | -92% |
| XRP | 654 | 4 | 2% | 1% | -22% | -77% | -77% |
| SOL | 654 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 652 | 3 | 6% | 2% | -40% | -87% | -89% |
| NEAR | 649 | 3 | 6% | 3% | -40% | -64% | -65% |
| GOLD | 351 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 337 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 320 | 2 | 3% | 1% | -33% | -94% | -96% |
| COPPER | 296 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 265 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 261 | 2 | 3% | 2% | -28% | -94% | -92% |
| PALLADIUM | 256 | 1 | 2% | 1% | -64% | -97% | -98% |
| EURUSD | 239 | 1 | 5% | 3% | -61% | -92% | -90% |
| GBPUSD | 230 | 1 | 3% | 2% | -59% | -94% | -94% |
| USDJPY | 202 | 3 | 2% | 1% | +39% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4381 | 20 | 4% | 2% | -47% | -89% | -88% |
| DOWN (bought NO) | 4286 | 17 | 4% | 2% | -54% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 973 | 7 | 2% | 1% | +22% | -59% | -58% |
| 0.05–0.1% | 984 | 2 | 3% | 1% | -70% | -91% | -92% |
| 0.1–0.2% | 1474 | 6 | 4% | 2% | -48% | -91% | -91% |
| 0.2–0.5% | 1750 | 8 | 6% | 3% | -50% | -88% | -87% |
| Over 0.5% | 727 | 4 | 7% | 3% | -44% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2294 | 17 | 5% | 3% | -15% | -89% | -88% |
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
| 10/5 10:59:35 AM | WTI | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:59:35 AM | USDJPY | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:59:04 AM | PLATINUM | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:59:04 AM | NEAR | DOWN | 55 sec | +0.110% | 0¢ | ❌ Lost | $0.00 |
| 10/5 10:58:48 AM | NATGAS | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:58:16 AM | BNB | DOWN | 1.7 min | +0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 10:57:44 AM | XRP | DOWN | 2.3 min | +0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 10:56:39 AM | BTC | DOWN | 3.3 min | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 10:56:39 AM | DOGE | DOWN | 3.3 min | +0.288% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 10:56:23 AM | ZEC | DOWN | 3.6 min | +0.814% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:55:33 AM | SOL | DOWN | 4.4 min | +0.248% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 10:54:47 AM | HYPE | DOWN | 5.2 min | +0.769% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 10:54:47 AM | ETH | DOWN | 5.2 min | +0.262% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 10:44:52 AM | COPPER | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:44:36 AM | XRP | UP | 23 sec | -0.054% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:44:36 AM | NATGAS | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:44:36 AM | BTC | DOWN | 23 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/5 10:44:20 AM | SILVER | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:44:20 AM | ETH | DOWN | 39 sec | +0.055% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:44:04 AM | GOLD | DOWN | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 10:43:32 AM | DOGE | DOWN | 88 sec | +0.211% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 10:43:32 AM | PLATINUM | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:43:32 AM | EURUSD | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:43:16 AM | ZEC | DOWN | 1.7 min | +0.344% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 10:43:16 AM | PALLADIUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:43:16 AM | GBPUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:42:11 AM | BNB | DOWN | 2.8 min | +0.154% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 10:41:55 AM | SOL | DOWN | 3.1 min | +0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 10:40:18 AM | HYPE | DOWN | 4.7 min | +0.656% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 10:40:18 AM | NEAR | DOWN | 4.7 min | +1.133% | 1¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
