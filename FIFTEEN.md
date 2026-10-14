# 15-Minute 1¢ Study

*Updated Wed Oct 14, 5:27 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1370 finished bets | 1% | $31.55 | +21% | +2.30¢ | $38.65 / -$7.10 |

*Expect about **85 buys a day** (~$12.69/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1293 | $14.80 | +11% |
| 5+ min left, hold to the close | 543 | -$23.95 | -30% |
| Volatility model ≥ 5%, sell at 50¢ | 1370 | -$27.45 | -18% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17721 | 17714 | 65 (0%) | 1.07% | -$1,235.15 (-58%) | Hold to the close: -$1,235.15 (-58%) |

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
| Volatility model | 11611 | 4.5% | 0.4% (46) | -683% | ❌ Worse |
| Momentum model | 11611 | 4.5% | 0.4% (46) | -709% | ❌ Worse |
| Mean-reversion model | 11611 | 7.3% | 0.4% (46) | -806% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11611 | 46 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2432 | 18 | -14% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1370 | 13 | +21% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 837 | 9 | +54% | -64% | -63% | -60% |
| Momentum model ≥ 2% | 2129 | 15 | -15% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1293 | 11 | +11% | -77% | -76% | -74% |
| Momentum model ≥ 10% | 882 | 8 | +28% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4216 | 27 | -30% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2878 | 20 | -23% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1897 | 14 | -15% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11809 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4312 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1593 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17714 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 65 | 0% | -$1,235.15 | -58% | — |
| Sell at 2¢ | 609 | 3% | -$1,944.81 | -91% | 33 sec |
| Sell at 3¢ | 407 | 2% | -$1,944.42 | -91% | 46 sec |
| Sell at 5¢ | 295 | 2% | -$1,911.40 | -89% | 48 sec |
| Sell at 10¢ | 186 | 1% | -$1,831.49 | -85% | 63 sec |
| Sell at 25¢ | 103 | 1% | -$1,706.22 | -80% | 67 sec |
| Sell at 50¢ | 66 | 0% | -$1,531.65 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 539 | 4 | 10% | 2% | -29% | -82% | -88% |
| 2–5 min | 5694 | 32 | 6% | 3% | -45% | -88% | -88% |
| 1–2 min | 4654 | 17 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 6823 | 12 | 1% | 0% | -74% | -92% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1323 | 7 | 4% | 2% | -34% | -90% | -90% |
| HYPE | 1320 | 4 | 4% | 2% | -62% | -90% | -89% |
| ETH | 1317 | 8 | 5% | 3% | -26% | -89% | -88% |
| BNB | 1317 | 5 | 4% | 2% | -54% | -90% | -90% |
| DOGE | 1315 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1311 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1303 | 6 | 5% | 2% | -39% | -88% | -91% |
| XRP | 1302 | 7 | 2% | 1% | -33% | -86% | -86% |
| NEAR | 1301 | 7 | 5% | 2% | -30% | -77% | -78% |
| GOLD | 701 | 1 | 4% | 1% | -83% | -91% | -93% |
| SILVER | 689 | 2 | 3% | 1% | -66% | -94% | -93% |
| WTI | 660 | 3 | 3% | 1% | -47% | -94% | -96% |
| COPPER | 608 | 0 | 1% | 1% | -100% | -97% | -97% |
| PLATINUM | 581 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 539 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 534 | 3 | 2% | 2% | -48% | -96% | -95% |
| EURUSD | 514 | 3 | 3% | 2% | -46% | -77% | -76% |
| GBPUSD | 483 | 1 | 2% | 1% | -81% | -96% | -96% |
| USDJPY | 442 | 3 | 1% | 1% | -37% | -98% | -98% |
| AUDUSD | 83 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 71 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8908 | 35 | 3% | 2% | -55% | -90% | -90% |
| DOWN (bought NO) | 8806 | 30 | 3% | 2% | -61% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2063 | 10 | 2% | 1% | -19% | -78% | -77% |
| 0.05–0.1% | 2104 | 6 | 3% | 1% | -59% | -92% | -91% |
| 0.1–0.2% | 3021 | 9 | 4% | 2% | -63% | -91% | -91% |
| 0.2–0.5% | 3330 | 18 | 5% | 3% | -41% | -89% | -89% |
| Over 0.5% | 1288 | 5 | 6% | 2% | -60% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4674 | 20 | 4% | 2% | -51% | -87% | -88% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,515 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 5:14:45 AM | HYPE | DOWN | 14 sec | -0.018% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:14:45 AM | XRP | UP | 14 sec | -0.044% | 0¢ | ❌ Lost | $0.00 |
| 10/14 5:14:29 AM | USDJPY | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:14:13 AM | SILVER | DOWN | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:14:13 AM | PALLADIUM | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:13:56 AM | COPPER | DOWN | 63 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:13:24 AM | AUDUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:13:24 AM | USDCAD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:12:34 AM | NATGAS | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:10:26 AM | ETH | UP | 4.6 min | -0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:10:10 AM | WTI | DOWN | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:10:10 AM | NEAR | UP | 4.8 min | -0.698% | 5¢ | ❌ Lost | -$0.15 |
| 10/14 5:10:10 AM | ZEC | UP | 4.8 min | -0.579% | 0¢ | ❌ Lost | $0.00 |
| 10/14 5:10:10 AM | BNB | UP | 4.8 min | -0.132% | 7¢ | ❌ Lost | -$0.15 |
| 10/14 5:09:53 AM | SOL | UP | 5.1 min | -0.335% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:08:48 AM | DOGE | UP | 6.2 min | -0.287% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:59:45 AM | PALLADIUM | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:59:29 AM | SILVER | UP | 31 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 4:59:29 AM | USDCAD | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:59:29 AM | COPPER | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:58:38 AM | NEAR | DOWN | 82 sec | +0.051% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:58:38 AM | PLATINUM | DOWN | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:58:22 AM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:58:22 AM | BTC | DOWN | 1.6 min | +0.053% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:58:22 AM | HYPE | DOWN | 1.6 min | +0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:58:22 AM | ETH | DOWN | 1.6 min | +0.128% | 0¢ | ❌ Lost | $0.00 |
| 10/14 4:58:22 AM | GOLD | UP | 1.6 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/14 4:58:07 AM | BNB | DOWN | 1.9 min | +0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/14 4:56:29 AM | SOL | DOWN | 3.5 min | +0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:55:57 AM | XRP | DOWN | 4.0 min | +0.190% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
