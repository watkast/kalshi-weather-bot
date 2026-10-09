# 15-Minute 1¢ Study

*Updated Fri Oct 9, 1:11 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 880 finished bets | 1% | $30.45 | +32% | +3.46¢ | -$19.10 / $49.55 |

*Expect about **76 buys a day** (~$11.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 859 | $19.75 | +21% |
| 5+ min left, hold to the close | 382 | -$0.40 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 880 | -$6.80 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13123 | 13116 | 52 (0%) | 1.07% | -$863.35 (-54%) | Hold to the close: -$863.35 (-54%) |

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
| Volatility model | 8334 | 4.0% | 0.4% (35) | -579% | ❌ Worse |
| Momentum model | 8334 | 4.1% | 0.4% (35) | -614% | ❌ Worse |
| Mean-reversion model | 8334 | 6.7% | 0.4% (35) | -677% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8334 | 35 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1605 | 13 | -6% | -75% | -75% | -72% |
| Volatility model ≥ 5% | 880 | 9 | +32% | -67% | -66% | -63% |
| Volatility model ≥ 10% | 538 | 7 | +91% | -52% | -52% | -47% |
| Momentum model ≥ 2% | 1420 | 11 | -6% | -76% | -78% | -75% |
| Momentum model ≥ 5% | 859 | 8 | +21% | -70% | -72% | -69% |
| Momentum model ≥ 10% | 590 | 6 | +45% | -61% | -62% | -59% |
| Mean-reversion model ≥ 2% | 2908 | 20 | -25% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1968 | 16 | -10% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1290 | 12 | +7% | -81% | -81% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8531 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3391 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1194 | 2% | 2% | 1% | 1% | 1% | 0% |
| **All** | 13116 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 52 | 0% | -$863.35 | -54% | — |
| Sell at 2¢ | 440 | 3% | -$1,434.95 | -90% | 33 sec |
| Sell at 3¢ | 292 | 2% | -$1,435.47 | -90% | 47 sec |
| Sell at 5¢ | 214 | 2% | -$1,410.25 | -89% | 60 sec |
| Sell at 10¢ | 141 | 1% | -$1,336.64 | -84% | 64 sec |
| Sell at 25¢ | 81 | 1% | -$1,225.24 | -77% | 81 sec |
| Sell at 50¢ | 53 | 0% | -$1,093.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 378 | 4 | 10% | 3% | +0% | -82% | -86% |
| 2–5 min | 4235 | 26 | 6% | 3% | -40% | -89% | -89% |
| 1–2 min | 3435 | 13 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 5064 | 9 | 1% | 0% | -74% | -90% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 954 | 6 | 4% | 3% | -24% | -90% | -90% |
| HYPE | 954 | 3 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 952 | 2 | 3% | 1% | -73% | -92% | -92% |
| BNB | 951 | 4 | 4% | 2% | -49% | -91% | -92% |
| ETH | 948 | 7 | 5% | 2% | -9% | -89% | -88% |
| NEAR | 944 | 5 | 6% | 2% | -30% | -73% | -74% |
| BTC | 944 | 4 | 5% | 2% | -44% | -88% | -90% |
| SOL | 943 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 941 | 6 | 2% | 1% | -20% | -82% | -83% |
| GOLD | 563 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 550 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 517 | 3 | 3% | 1% | -34% | -94% | -96% |
| COPPER | 485 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 445 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 417 | 3 | 3% | 2% | -33% | -95% | -93% |
| PALLADIUM | 414 | 1 | 1% | 0% | -77% | -98% | -99% |
| EURUSD | 410 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 387 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 348 | 3 | 1% | 1% | -20% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6612 | 27 | 3% | 2% | -53% | -89% | -89% |
| DOWN (bought NO) | 6504 | 25 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1374 | 8 | 2% | 1% | +1% | -69% | -68% |
| 0.05–0.1% | 1442 | 4 | 3% | 1% | -59% | -92% | -92% |
| 0.1–0.2% | 2174 | 7 | 4% | 2% | -60% | -92% | -92% |
| 0.2–0.5% | 2495 | 13 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 1044 | 5 | 6% | 2% | -51% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3343 | 18 | 4% | 2% | -38% | -85% | -85% |
| Morning (6am–12pm) | 3238 | 17 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 2914 | 8 | 3% | 1% | -68% | -89% | -90% |
| Evening (6pm–12am) | 3621 | 9 | 3% | 1% | -72% | -95% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,020 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/9 12:59:54 PM | SILVER | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:59:54 PM | ZEC | DOWN | 6 sec | +0.090% | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:59:38 PM | BTC | UP | 22 sec | -0.014% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:59:38 PM | ETH | DOWN | 22 sec | +0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:59:22 PM | COPPER | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:59:06 PM | HYPE | DOWN | 54 sec | +0.146% | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:59:06 PM | SOL | DOWN | 54 sec | +0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:59:06 PM | BNB | DOWN | 54 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:59:06 PM | DOGE | DOWN | 54 sec | +0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:59:06 PM | NATGAS | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:59:06 PM | XRP | DOWN | 54 sec | +0.094% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:58:51 PM | NEAR | DOWN | 69 sec | +0.300% | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:58:35 PM | PLATINUM | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:58:35 PM | WTI | UP | 85 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:58:03 PM | EURUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:44:33 PM | PALLADIUM | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:44:33 PM | NATGAS | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:44:17 PM | SILVER | DOWN | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:44:02 PM | PLATINUM | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:44:02 PM | USDJPY | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:43:44 PM | ETH | UP | 75 sec | -0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:43:12 PM | ZEC | UP | 1.8 min | -0.334% | 0¢ | ❌ Lost | $0.00 |
| 10/9 12:43:12 PM | DOGE | UP | 1.8 min | -0.202% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:43:12 PM | XRP | UP | 1.8 min | -0.216% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 12:42:58 PM | BTC | UP | 2.0 min | -0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:42:26 PM | NEAR | UP | 2.5 min | -0.646% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:42:26 PM | WTI | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:42:10 PM | SOL | UP | 2.8 min | -0.256% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:42:10 PM | BNB | UP | 2.8 min | -0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 12:40:17 PM | HYPE | UP | 4.7 min | -0.378% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
