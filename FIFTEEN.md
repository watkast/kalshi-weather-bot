# 15-Minute 1¢ Study

*Updated Fri Oct 9, 11:49 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 874 finished bets | 1% | $31.05 | +33% | +3.55¢ | -$18.65 / $49.70 |

*Expect about **76 buys a day** (~$11.44/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 852 | $20.50 | +22% |
| 5+ min left, hold to the close | 379 | $0.05 | +0% |
| Volatility model ≥ 5%, sell at 50¢ | 874 | -$6.20 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13047 | 13040 | 52 (0%) | 1.07% | -$854.20 (-54%) | Hold to the close: -$854.20 (-54%) |

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
| Volatility model | 8290 | 4.0% | 0.4% (35) | -580% | ❌ Worse |
| Momentum model | 8290 | 4.1% | 0.4% (35) | -614% | ❌ Worse |
| Mean-reversion model | 8290 | 6.7% | 0.4% (35) | -678% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8290 | 35 | -47% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 1595 | 13 | -6% | -75% | -75% | -72% |
| Volatility model ≥ 5% | 874 | 9 | +33% | -67% | -66% | -63% |
| Volatility model ≥ 10% | 534 | 7 | +93% | -52% | -52% | -47% |
| Momentum model ≥ 2% | 1410 | 11 | -6% | -76% | -78% | -75% |
| Momentum model ≥ 5% | 852 | 8 | +22% | -70% | -71% | -68% |
| Momentum model ≥ 10% | 584 | 6 | +47% | -61% | -62% | -58% |
| Mean-reversion model ≥ 2% | 2891 | 20 | -25% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1957 | 16 | -10% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1285 | 12 | +7% | -81% | -81% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8487 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3367 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1186 | 2% | 2% | 1% | 1% | 1% | 0% |
| **All** | 13040 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 52 | 0% | -$854.20 | -54% | — |
| Sell at 2¢ | 440 | 3% | -$1,425.80 | -90% | 33 sec |
| Sell at 3¢ | 292 | 2% | -$1,426.32 | -90% | 47 sec |
| Sell at 5¢ | 214 | 2% | -$1,401.10 | -89% | 60 sec |
| Sell at 10¢ | 141 | 1% | -$1,327.49 | -84% | 64 sec |
| Sell at 25¢ | 81 | 1% | -$1,216.09 | -77% | 81 sec |
| Sell at 50¢ | 53 | 0% | -$1,084.45 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 375 | 4 | 10% | 3% | +1% | -82% | -86% |
| 2–5 min | 4217 | 26 | 6% | 3% | -40% | -89% | -89% |
| 1–2 min | 3412 | 13 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 5032 | 9 | 1% | 0% | -74% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 949 | 6 | 4% | 3% | -24% | -90% | -90% |
| HYPE | 949 | 3 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 947 | 2 | 3% | 1% | -73% | -92% | -92% |
| BNB | 946 | 4 | 4% | 2% | -49% | -91% | -92% |
| ETH | 943 | 7 | 5% | 2% | -9% | -89% | -88% |
| NEAR | 939 | 5 | 6% | 2% | -30% | -72% | -73% |
| BTC | 939 | 4 | 5% | 2% | -44% | -88% | -90% |
| SOL | 938 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 937 | 6 | 2% | 1% | -20% | -82% | -83% |
| GOLD | 560 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 545 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 515 | 3 | 3% | 1% | -34% | -94% | -96% |
| COPPER | 483 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 441 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 413 | 3 | 3% | 2% | -32% | -95% | -93% |
| PALLADIUM | 410 | 1 | 1% | 0% | -77% | -98% | -99% |
| EURUSD | 406 | 3 | 3% | 2% | -31% | -72% | -71% |
| GBPUSD | 385 | 1 | 3% | 2% | -76% | -95% | -95% |
| USDJPY | 346 | 3 | 1% | 1% | -19% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6572 | 27 | 3% | 2% | -53% | -89% | -89% |
| DOWN (bought NO) | 6468 | 25 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1368 | 8 | 2% | 1% | +1% | -69% | -68% |
| 0.05–0.1% | 1430 | 4 | 3% | 1% | -59% | -92% | -92% |
| 0.1–0.2% | 2163 | 7 | 4% | 2% | -59% | -92% | -92% |
| 0.2–0.5% | 2483 | 13 | 5% | 3% | -42% | -89% | -88% |
| Over 0.5% | 1041 | 5 | 6% | 2% | -51% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3343 | 18 | 4% | 2% | -38% | -85% | -85% |
| Morning (6am–12pm) | 3223 | 17 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 2853 | 8 | 3% | 1% | -67% | -89% | -90% |
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
| 10/9 11:44:59 AM | NEAR | UP | 0 sec | -0.145% | 0¢ | ❌ Lost | $0.00 |
| 10/9 11:44:59 AM | PALLADIUM | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 11:44:43 AM | DOGE | UP | 16 sec | -0.054% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 11:44:43 AM | WTI | DOWN | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 11:44:27 AM | SOL | UP | 32 sec | -0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 11:44:27 AM | BTC | DOWN | 32 sec | +0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 11:44:27 AM | HYPE | UP | 32 sec | -0.047% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 11:44:12 AM | NATGAS | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 11:44:12 AM | ETH | UP | 48 sec | -0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/9 11:44:12 AM | COPPER | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 11:44:12 AM | ZEC | DOWN | 48 sec | +0.078% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 11:43:38 AM | PLATINUM | DOWN | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 11:43:38 AM | GOLD | DOWN | 82 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/9 11:43:06 AM | BNB | DOWN | 1.9 min | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 11:42:33 AM | XRP | DOWN | 2.5 min | +0.253% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 11:14:51 AM | PALLADIUM | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 11:14:51 AM | COPPER | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 11:14:51 AM | XRP | UP | 8 sec | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/9 11:14:35 AM | PLATINUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 11:14:19 AM | USDJPY | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 11:14:19 AM | GBPUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 11:14:19 AM | DOGE | UP | 40 sec | -0.124% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 11:14:19 AM | WTI | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 11:14:03 AM | SOL | UP | 57 sec | -0.109% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 11:13:46 AM | BNB | UP | 73 sec | -0.099% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 11:13:30 AM | BTC | UP | 89 sec | -0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 11:13:14 AM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 11:12:44 AM | ETH | UP | 2.2 min | -0.119% | 2¢ | ❌ Lost | -$0.15 |
| 10/9 11:12:28 AM | NEAR | UP | 2.5 min | -0.570% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 11:11:08 AM | ZEC | UP | 3.9 min | -0.447% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
