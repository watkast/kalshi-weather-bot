# 15-Minute 1¢ Study

*Updated Tue Oct 13, 10:06 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1267 finished bets | 1% | $43.10 | +31% | +3.40¢ | $30.05 / $13.05 |

*Expect about **82 buys a day** (~$12.35/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1211 | $23.50 | +18% |
| 5+ min left, hold to the close | 471 | -$13.75 | -20% |
| Volatility model ≥ 5%, sell at 50¢ | 1267 | -$15.90 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16629 | 16622 | 63 (0%) | 1.07% | -$1,131.60 (-56%) | Hold to the close: -$1,131.60 (-56%) |

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
| Volatility model | 10957 | 4.4% | 0.4% (46) | -657% | ❌ Worse |
| Momentum model | 10957 | 4.4% | 0.4% (46) | -684% | ❌ Worse |
| Mean-reversion model | 10957 | 7.2% | 0.4% (46) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10957 | 46 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2257 | 18 | -7% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1267 | 13 | +31% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 782 | 9 | +65% | -63% | -63% | -60% |
| Momentum model ≥ 2% | 1982 | 15 | -8% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1211 | 11 | +18% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 824 | 8 | +37% | -69% | -69% | -65% |
| Mean-reversion model ≥ 2% | 3925 | 27 | -25% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2681 | 20 | -17% | -83% | -83% | -79% |
| Mean-reversion model ≥ 10% | 1766 | 14 | -8% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11155 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4006 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1461 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 16622 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,131.60 | -56% | — |
| Sell at 2¢ | 566 | 3% | -$1,824.44 | -91% | 33 sec |
| Sell at 3¢ | 374 | 2% | -$1,825.74 | -91% | 46 sec |
| Sell at 5¢ | 269 | 2% | -$1,796.75 | -89% | 49 sec |
| Sell at 10¢ | 174 | 1% | -$1,715.66 | -85% | 63 sec |
| Sell at 25¢ | 99 | 1% | -$1,587.91 | -79% | 79 sec |
| Sell at 50¢ | 64 | 0% | -$1,427.60 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 467 | 4 | 11% | 3% | -19% | -80% | -86% |
| 2–5 min | 5373 | 32 | 6% | 3% | -41% | -88% | -89% |
| 1–2 min | 4385 | 16 | 3% | 2% | -60% | -94% | -94% |
| Under 1 min | 6393 | 11 | 1% | 0% | -75% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1252 | 7 | 4% | 2% | -31% | -90% | -90% |
| HYPE | 1249 | 4 | 4% | 2% | -61% | -90% | -89% |
| DOGE | 1243 | 2 | 4% | 2% | -80% | -91% | -90% |
| ETH | 1241 | 8 | 5% | 2% | -21% | -90% | -89% |
| BNB | 1241 | 5 | 4% | 2% | -51% | -91% | -91% |
| SOL | 1240 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1233 | 6 | 5% | 2% | -35% | -88% | -91% |
| NEAR | 1228 | 7 | 5% | 2% | -26% | -77% | -78% |
| XRP | 1228 | 7 | 2% | 1% | -29% | -85% | -85% |
| GOLD | 658 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 640 | 1 | 3% | 1% | -82% | -94% | -94% |
| WTI | 613 | 3 | 3% | 1% | -44% | -94% | -96% |
| COPPER | 571 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 532 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 500 | 1 | 1% | 0% | -81% | -98% | -98% |
| NATGAS | 492 | 3 | 3% | 2% | -43% | -95% | -94% |
| EURUSD | 479 | 3 | 3% | 2% | -42% | -76% | -75% |
| GBPUSD | 453 | 1 | 2% | 1% | -79% | -96% | -96% |
| USDJPY | 415 | 3 | 1% | 1% | -33% | -98% | -97% |
| AUDUSD | 59 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 55 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8390 | 34 | 3% | 2% | -53% | -90% | -90% |
| DOWN (bought NO) | 8232 | 29 | 3% | 2% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1959 | 10 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 1975 | 6 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 2837 | 9 | 4% | 2% | -61% | -91% | -92% |
| 0.2–0.5% | 3148 | 18 | 5% | 3% | -37% | -89% | -89% |
| Over 0.5% | 1233 | 5 | 6% | 2% | -58% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3810 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3818 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4650 | 14 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,480 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 9:59:39 AM | AUDUSD | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:59:39 AM | PLATINUM | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:59:39 AM | DOGE | DOWN | 20 sec | +0.090% | 0¢ | ❌ Lost | $0.00 |
| 10/13 9:59:24 AM | BNB | DOWN | 36 sec | +0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/13 9:59:24 AM | HYPE | DOWN | 36 sec | +0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:59:08 AM | USDJPY | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:59:08 AM | ZEC | DOWN | 52 sec | +0.295% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:59:08 AM | XRP | DOWN | 52 sec | +0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:58:52 AM | BTC | DOWN | 68 sec | +0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:58:52 AM | SOL | DOWN | 68 sec | +0.199% | 0¢ | ❌ Lost | $0.00 |
| 10/13 9:58:04 AM | GBPUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:58:04 AM | ETH | DOWN | 1.9 min | +0.199% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:57:48 AM | EURUSD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:56:59 AM | NEAR | UP | 3.0 min | -1.596% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:14:40 AM | SOL | UP | 20 sec | -0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:14:40 AM | BNB | UP | 20 sec | -0.023% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:14:24 AM | NEAR | UP | 36 sec | -0.298% | 0¢ | ❌ Lost | $0.00 |
| 10/13 6:14:24 AM | PLATINUM | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:14:24 AM | DOGE | UP | 36 sec | -0.103% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:14:08 AM | USDJPY | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:14:08 AM | XRP | DOWN | 52 sec | +0.096% | 0¢ | ❌ Lost | $0.00 |
| 10/13 6:13:52 AM | BTC | UP | 68 sec | -0.080% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:13:52 AM | ETH | UP | 68 sec | -0.089% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:13:52 AM | NATGAS | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:13:36 AM | PALLADIUM | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:13:36 AM | GOLD | DOWN | 83 sec | — | 7¢ | ❌ Lost | -$0.15 |
| 10/13 6:13:20 AM | WTI | UP | 1.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 6:12:33 AM | ZEC | UP | 2.4 min | -0.601% | 0¢ | ❌ Lost | $0.00 |
| 10/13 6:11:14 AM | COPPER | UP | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:09:35 AM | HYPE | UP | 5.4 min | -0.585% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
