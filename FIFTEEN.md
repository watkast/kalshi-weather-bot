# 15-Minute 1¢ Study

*Updated Tue Oct 27, 4:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2830 finished bets | 1% | $71.75 | +22% | +2.54¢ | $81.85 / -$10.10 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2639 | $44.85 | +15% |
| Volatility model ≥ 2%, hold to the close | 5259 | -$27.20 | -4% |
| Momentum model ≥ 2%, hold to the close | 4373 | -$49.20 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34382 | 34374 | 127 (0%) | 1.07% | -$2,405.20 (-57%) | Hold to the close: -$2,405.20 (-57%) |

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
| Volatility model | 21802 | 4.6% | 0.4% (86) | -675% | ❌ Worse |
| Momentum model | 21802 | 4.6% | 0.4% (86) | -700% | ❌ Worse |
| Mean-reversion model | 21802 | 8.0% | 0.4% (86) | -819% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21802 | 86 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5259 | 44 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2830 | 28 | +22% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1608 | 18 | +57% | -67% | -66% | -63% |
| Momentum model ≥ 2% | 4373 | 33 | -10% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2639 | 24 | +15% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1723 | 16 | +28% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8830 | 57 | -30% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6181 | 47 | -16% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4118 | 33 | -10% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22002 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8105 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4267 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34374 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 127 | 0% | -$2,405.20 | -57% | — |
| Sell at 2¢ | 1287 | 4% | -$3,680.58 | -88% | 47 sec |
| Sell at 3¢ | 879 | 3% | -$3,672.39 | -88% | 48 sec |
| Sell at 5¢ | 609 | 2% | -$3,619.35 | -87% | 62 sec |
| Sell at 10¢ | 376 | 1% | -$3,466.64 | -83% | 65 sec |
| Sell at 25¢ | 202 | 1% | -$3,206.58 | -77% | 86 sec |
| Sell at 50¢ | 132 | 0% | -$2,900.20 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1515 | 8 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 11030 | 59 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8713 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13112 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2464 | 12 | 5% | 2% | -38% | -89% | -88% |
| HYPE | 2457 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2455 | 13 | 5% | 2% | -34% | -84% | -83% |
| SOL | 2451 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2445 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2440 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2433 | 12 | 5% | 2% | -36% | -82% | -82% |
| XRP | 2431 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2426 | 12 | 5% | 2% | -34% | -88% | -89% |
| GOLD | 1296 | 5 | 4% | 2% | -54% | -82% | -83% |
| SILVER | 1262 | 6 | 4% | 2% | -45% | -82% | -82% |
| WTI | 1242 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1111 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1073 | 4 | 1% | 1% | -65% | -72% | -71% |
| EURUSD | 1042 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1030 | 5 | 2% | 1% | -55% | -87% | -87% |
| PALLADIUM | 988 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 983 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 968 | 5 | 1% | 1% | -52% | -98% | -97% |
| AUDUSD | 525 | 2 | 1% | 1% | -64% | -98% | -97% |
| USDCAD | 484 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 103 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 72 | 0 | 3% | 0% | -100% | -95% | -96% |
| 30YRRATE | 66 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 65 | 1 | 3% | 0% | +44% | +49% | +48% |
| 5YRRATE | 62 | 1 | 3% | 3% | +51% | -94% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17444 | 70 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16930 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3622 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3772 | 12 | 3% | 2% | -53% | -92% | -92% |
| 0.1–0.2% | 5705 | 20 | 5% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 6482 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2417 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8688 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,683 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 4:44:45 AM | NATGAS | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:44:29 AM | 2YRRATE | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:44:13 AM | SILVER | DOWN | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:43:41 AM | BRENT | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:42:53 AM | ZEC | DOWN | 2.1 min | +0.446% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:42:22 AM | EURUSD | DOWN | 2.6 min | — | 53¢ | ❌ Lost | -$0.15 |
| 10/27 4:42:22 AM | WTI | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:41:53 AM | HYPE | DOWN | 3.1 min | +0.299% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:41:22 AM | DOGE | DOWN | 3.6 min | +0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:41:06 AM | NEAR | DOWN | 3.9 min | +0.638% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:40:18 AM | USDJPY | UP | 4.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:40:02 AM | ETH | DOWN | 5.0 min | +0.390% | 2¢ | ❌ Lost | -$0.15 |
| 10/27 4:40:02 AM | XRP | DOWN | 5.0 min | +0.410% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:40:02 AM | SOL | DOWN | 5.0 min | +0.411% | 2¢ | ❌ Lost | -$0.15 |
| 10/27 4:40:02 AM | 30YRRATE | UP | 5.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:39:46 AM | 10YRRATE | UP | 5.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:39:46 AM | BTC | DOWN | 5.2 min | +0.253% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:39:46 AM | BNB | DOWN | 5.2 min | +0.253% | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:39:46 AM | GOLD | DOWN | 5.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:39:46 AM | 5YRRATE | UP | 5.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:38:58 AM | AUDUSD | DOWN | 6.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:29:57 AM | GOLD | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:29:42 AM | ZEC | DOWN | 17 sec | +0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:29:42 AM | GBPUSD | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:29:42 AM | NATGAS | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:29:26 AM | COPPER | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:29:10 AM | HYPE | DOWN | 49 sec | +0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:28:54 AM | 2YRRATE | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:28:54 AM | AUDUSD | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:28:39 AM | BRENT | UP | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
