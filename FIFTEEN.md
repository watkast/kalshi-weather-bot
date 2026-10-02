# 15-Minute 1¢ Study

*Updated Fri Oct 2, 8:18 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 347 finished bets | 1% | $4.80 | +13% | +1.38¢ | -$5.35 / $10.15 |

*Expect about **80 buys a day** (~$12.06/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 168 | $3.25 | +13% |
| Momentum model ≥ 5%, sell at 50¢ | 347 | -$2.45 | -7% |
| Volatility model ≥ 5%, hold to the close | 343 | -$9.20 | -25% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5644 | 5638 | 21 (0%) | 1.07% | -$392.10 (-57%) | Hold to the close: -$392.10 (-57%) |

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
| Volatility model | 3255 | 3.6% | 0.3% (9) | -625% | ❌ Worse |
| Momentum model | 3255 | 3.7% | 0.3% (9) | -673% | ❌ Worse |
| Mean-reversion model | 3255 | 6.7% | 0.3% (9) | -791% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3255 | 9 | -65% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 689 | 4 | -33% | -66% | -69% | -65% |
| Volatility model ≥ 5% | 343 | 2 | -25% | -41% | -42% | -38% |
| Volatility model ≥ 10% | 192 | 2 | +57% | +0% | -4% | +4% |
| Momentum model ≥ 2% | 603 | 3 | -40% | -64% | -68% | -65% |
| Momentum model ≥ 5% | 347 | 3 | +13% | -46% | -50% | -45% |
| Momentum model ≥ 10% | 231 | 2 | +26% | -23% | -25% | -19% |
| Mean-reversion model ≥ 2% | 1251 | 6 | -48% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 826 | 6 | -21% | -81% | -84% | -78% |
| Mean-reversion model ≥ 10% | 528 | 4 | -14% | -77% | -82% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3451 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1665 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 522 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5638 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 21 | 0% | -$392.10 | -57% | — |
| Sell at 2¢ | 210 | 4% | -$617.50 | -90% | 46 sec |
| Sell at 3¢ | 124 | 2% | -$623.74 | -91% | 49 sec |
| Sell at 5¢ | 91 | 2% | -$612.95 | -89% | 66 sec |
| Sell at 10¢ | 65 | 1% | -$572.95 | -84% | 81 sec |
| Sell at 25¢ | 34 | 1% | -$531.56 | -77% | 1.6 min |
| Sell at 50¢ | 19 | 0% | -$473.85 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 165 | 2 | 12% | 3% | +15% | -79% | -89% |
| 2–5 min | 1846 | 10 | 7% | 3% | -47% | -87% | -89% |
| 1–2 min | 1466 | 6 | 3% | 2% | -56% | -94% | -93% |
| Under 1 min | 2158 | 3 | 1% | 0% | -80% | -91% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 391 | 2 | 4% | 1% | -34% | -90% | -92% |
| BNB | 386 | 0 | 4% | 1% | -100% | -92% | -95% |
| ETH | 385 | 2 | 5% | 3% | -36% | -87% | -87% |
| ZEC | 385 | 1 | 5% | 3% | -69% | -88% | -91% |
| BTC | 384 | 0 | 7% | 2% | -100% | -84% | -90% |
| HYPE | 382 | 2 | 4% | 3% | -35% | -90% | -88% |
| XRP | 381 | 3 | 1% | 1% | +1% | -63% | -62% |
| NEAR | 379 | 1 | 6% | 2% | -64% | -86% | -90% |
| SOL | 378 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 289 | 0 | 5% | 1% | -100% | -89% | -92% |
| SILVER | 268 | 0 | 1% | 1% | -100% | -97% | -96% |
| WTI | 251 | 2 | 3% | 1% | -16% | -94% | -95% |
| COPPER | 240 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 209 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 208 | 2 | 4% | 2% | -10% | -93% | -91% |
| PALLADIUM | 200 | 1 | 2% | 1% | -53% | -96% | -97% |
| GBPUSD | 184 | 1 | 4% | 2% | -49% | -92% | -93% |
| EURUSD | 183 | 1 | 4% | 2% | -49% | -93% | -93% |
| USDJPY | 155 | 3 | 3% | 2% | +81% | -96% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2861 | 13 | 4% | 2% | -47% | -92% | -92% |
| DOWN (bought NO) | 2777 | 8 | 4% | 1% | -67% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 413 | 2 | 1% | 1% | -9% | -50% | -49% |
| 0.05–0.1% | 478 | 0 | 3% | 0% | -100% | -91% | -95% |
| 0.1–0.2% | 838 | 1 | 3% | 1% | -84% | -92% | -93% |
| 0.2–0.5% | 1176 | 4 | 6% | 3% | -62% | -88% | -89% |
| Over 0.5% | 545 | 4 | 7% | 2% | -24% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1417 | 8 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,110 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 8:14:52 AM | PLATINUM | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:14:52 AM | EURUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:14:36 AM | NATGAS | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:14:20 AM | GOLD | UP | 40 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 10/2 8:14:05 AM | XRP | UP | 55 sec | -0.235% | 0¢ | ❌ Lost | $0.00 |
| 10/2 8:14:05 AM | SOL | UP | 55 sec | -0.232% | 0¢ | ❌ Lost | $0.00 |
| 10/2 8:14:05 AM | DOGE | UP | 55 sec | -0.233% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:13:17 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:13:17 AM | SILVER | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:12:27 AM | BTC | UP | 2.5 min | -0.245% | 2¢ | ❌ Lost | -$0.15 |
| 10/2 8:12:27 AM | ZEC | UP | 2.5 min | -0.416% | 6¢ | ❌ Lost | -$0.15 |
| 10/2 8:12:11 AM | BNB | UP | 2.8 min | -0.293% | 2¢ | ❌ Lost | -$0.15 |
| 10/2 8:12:11 AM | GBPUSD | UP | 2.8 min | — | 21¢ | ❌ Lost | -$0.15 |
| 10/2 8:11:56 AM | HYPE | UP | 3.0 min | -0.624% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:11:56 AM | ETH | UP | 3.0 min | -0.467% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:11:40 AM | USDJPY | DOWN | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:11:24 AM | NEAR | UP | 3.6 min | -1.145% | 1¢ | ❌ Lost | $0.00 |
| 10/2 8:10:36 AM | WTI | UP | 4.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:59:53 AM | GOLD | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:59:21 AM | PLATINUM | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:59:21 AM | COPPER | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:59:21 AM | SILVER | DOWN | 38 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:58:15 AM | GBPUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:57:44 AM | HYPE | UP | 2.3 min | -0.318% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:57:44 AM | XRP | UP | 2.3 min | -0.526% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:57:44 AM | BNB | UP | 2.3 min | -0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:57:44 AM | EURUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:57:12 AM | NEAR | UP | 2.8 min | -1.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:57:12 AM | BTC | UP | 2.8 min | -0.314% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:57:12 AM | ZEC | UP | 2.8 min | -0.715% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
