# 15-Minute 1¢ Study

*Updated Sat Oct 3, 12:49 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 453 finished bets | 1% | $8.90 | +19% | +1.96¢ | $3.40 / $5.50 |

*Expect about **82 buys a day** (~$12.34/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 175 | $2.20 | +9% |
| Momentum model ≥ 5%, sell at 50¢ | 453 | -$5.60 | -12% |
| Volatility model ≥ 5%, hold to the close | 452 | -$5.85 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6716 | 6710 | 29 (0%) | 1.07% | -$401.75 (-50%) | Hold to the close: -$401.75 (-50%) |

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
| Volatility model | 4174 | 4.1% | 0.4% (17) | -634% | ❌ Worse |
| Momentum model | 4174 | 4.2% | 0.4% (17) | -667% | ❌ Worse |
| Mean-reversion model | 4174 | 7.0% | 0.4% (17) | -762% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4174 | 17 | -48% | -83% | -84% | -80% |
| Volatility model ≥ 2% | 866 | 6 | -19% | -67% | -68% | -63% |
| Volatility model ≥ 5% | 452 | 3 | -12% | -49% | -50% | -46% |
| Volatility model ≥ 10% | 273 | 3 | +70% | -20% | -25% | -17% |
| Momentum model ≥ 2% | 754 | 5 | -19% | -66% | -70% | -66% |
| Momentum model ≥ 5% | 453 | 4 | +19% | -54% | -58% | -52% |
| Momentum model ≥ 10% | 308 | 3 | +44% | -37% | -40% | -34% |
| Mean-reversion model ≥ 2% | 1535 | 8 | -43% | -83% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1032 | 7 | -25% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 676 | 5 | -14% | -77% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4371 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6710 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 29 | 0% | -$401.75 | -50% | — |
| Sell at 2¢ | 267 | 4% | -$710.33 | -88% | 34 sec |
| Sell at 3¢ | 169 | 3% | -$713.84 | -88% | 48 sec |
| Sell at 5¢ | 127 | 2% | -$697.20 | -86% | 61 sec |
| Sell at 10¢ | 86 | 1% | -$653.09 | -81% | 80 sec |
| Sell at 25¢ | 47 | 1% | -$596.18 | -74% | 1.6 min |
| Sell at 50¢ | 27 | 0% | -$527.50 | -65% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 172 | 2 | 12% | 3% | +10% | -79% | -89% |
| 2–5 min | 2191 | 14 | 8% | 4% | -38% | -86% | -87% |
| 1–2 min | 1736 | 8 | 3% | 2% | -50% | -94% | -93% |
| Under 1 min | 2608 | 5 | 1% | 0% | -71% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 492 | 2 | 4% | 1% | -47% | -90% | -91% |
| ETH | 491 | 4 | 6% | 3% | +3% | -85% | -85% |
| ZEC | 490 | 3 | 5% | 3% | -27% | -89% | -91% |
| HYPE | 489 | 2 | 5% | 3% | -50% | -88% | -85% |
| BNB | 484 | 1 | 4% | 2% | -75% | -90% | -92% |
| XRP | 483 | 4 | 2% | 1% | +7% | -69% | -69% |
| BTC | 481 | 1 | 6% | 2% | -73% | -85% | -89% |
| SOL | 481 | 0 | 3% | 1% | -100% | -93% | -93% |
| NEAR | 480 | 2 | 6% | 2% | -44% | -56% | -59% |
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
| UP (bought YES) | 3390 | 17 | 4% | 2% | -41% | -88% | -87% |
| DOWN (bought NO) | 3320 | 12 | 4% | 2% | -58% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 630 | 5 | 2% | 1% | +44% | -37% | -37% |
| 0.05–0.1% | 689 | 0 | 3% | 1% | -100% | -92% | -93% |
| 0.1–0.2% | 1074 | 4 | 4% | 2% | -51% | -90% | -90% |
| 0.2–0.5% | 1374 | 6 | 6% | 3% | -52% | -88% | -87% |
| Over 0.5% | 602 | 4 | 7% | 3% | -31% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1330 | 3 | 3% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,518 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 12:44:54 PM | XRP | DOWN | 5 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/3 12:44:22 PM | SOL | DOWN | 37 sec | +0.053% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 12:44:22 PM | HYPE | DOWN | 37 sec | +0.036% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 12:44:06 PM | ZEC | DOWN | 54 sec | +0.270% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 12:43:34 PM | ETH | UP | 86 sec | -0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 12:43:18 PM | DOGE | DOWN | 1.7 min | +0.126% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 12:43:01 PM | BTC | UP | 2.0 min | -0.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 12:42:45 PM | NEAR | DOWN | 2.2 min | +0.412% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 12:29:55 PM | SOL | UP | 4 sec | -0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/3 12:29:55 PM | BNB | DOWN | 4 sec | -0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 12:29:39 PM | ETH | UP | 20 sec | -0.014% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 12:29:39 PM | XRP | DOWN | 20 sec | +0.054% | 0¢ | ❌ Lost | $0.00 |
| 10/3 12:29:23 PM | DOGE | UP | 36 sec | -0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/3 12:26:58 PM | HYPE | UP | 3.0 min | -0.279% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 12:26:42 PM | ZEC | UP | 3.3 min | -0.458% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 12:25:06 PM | NEAR | UP | 4.9 min | -0.776% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 12:14:57 PM | BNB | DOWN | 2 sec | +0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/3 12:14:25 PM | XRP | UP | 34 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 10/3 12:14:25 PM | BTC | UP | 34 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/3 12:14:09 PM | SOL | UP | 50 sec | -0.063% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 12:14:09 PM | DOGE | UP | 50 sec | -0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 12:13:53 PM | NEAR | UP | 66 sec | -0.316% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 12:13:53 PM | ZEC | UP | 66 sec | -0.144% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 12:13:05 PM | ETH | UP | 1.9 min | -0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 12:12:49 PM | HYPE | DOWN | 2.2 min | +0.239% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:59:52 AM | XRP | DOWN | 7 sec | +0.027% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 11:59:52 AM | SOL | UP | 7 sec | -0.033% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 11:59:52 AM | DOGE | DOWN | 7 sec | +0.002% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 11:59:36 AM | ZEC | DOWN | 23 sec | +0.171% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:59:04 AM | HYPE | DOWN | 56 sec | +0.073% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
