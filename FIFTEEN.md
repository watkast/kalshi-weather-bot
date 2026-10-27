# 15-Minute 1¢ Study

*Updated Tue Oct 27, 5:02 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2832 finished bets | 1% | $71.45 | +22% | +2.52¢ | $81.85 / -$10.40 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2643 | $44.25 | +15% |
| Volatility model ≥ 2%, hold to the close | 5262 | -$27.65 | -4% |
| Momentum model ≥ 2%, hold to the close | 4378 | -$49.95 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34398 | 34390 | 127 (0%) | 1.07% | -$2,407.30 (-58%) | Hold to the close: -$2,407.30 (-58%) |

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
| Volatility model | 21811 | 4.6% | 0.4% (86) | -675% | ❌ Worse |
| Momentum model | 21811 | 4.6% | 0.4% (86) | -700% | ❌ Worse |
| Mean-reversion model | 21811 | 8.0% | 0.4% (86) | -819% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21811 | 86 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5262 | 44 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2832 | 28 | +22% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1608 | 18 | +57% | -67% | -66% | -63% |
| Momentum model ≥ 2% | 4378 | 33 | -10% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2643 | 24 | +15% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1726 | 16 | +27% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8833 | 57 | -30% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6182 | 47 | -16% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4119 | 33 | -10% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22011 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8108 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4271 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34390 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 127 | 0% | -$2,407.30 | -58% | — |
| Sell at 2¢ | 1287 | 4% | -$3,682.68 | -88% | 47 sec |
| Sell at 3¢ | 879 | 3% | -$3,674.49 | -88% | 48 sec |
| Sell at 5¢ | 609 | 2% | -$3,621.45 | -87% | 62 sec |
| Sell at 10¢ | 376 | 1% | -$3,468.74 | -83% | 65 sec |
| Sell at 25¢ | 202 | 1% | -$3,208.68 | -77% | 86 sec |
| Sell at 50¢ | 132 | 0% | -$2,902.30 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1515 | 8 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 11037 | 59 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8717 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13117 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2465 | 12 | 5% | 2% | -38% | -89% | -88% |
| HYPE | 2458 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2456 | 13 | 5% | 2% | -34% | -84% | -83% |
| SOL | 2452 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2446 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2441 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2434 | 12 | 5% | 2% | -36% | -82% | -82% |
| XRP | 2432 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2427 | 12 | 5% | 2% | -34% | -88% | -89% |
| GOLD | 1296 | 5 | 4% | 2% | -54% | -82% | -83% |
| SILVER | 1262 | 6 | 4% | 2% | -45% | -82% | -82% |
| WTI | 1242 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1112 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1074 | 4 | 1% | 1% | -65% | -72% | -72% |
| EURUSD | 1043 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1031 | 5 | 2% | 1% | -55% | -87% | -87% |
| PALLADIUM | 988 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 983 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 969 | 5 | 1% | 1% | -52% | -98% | -97% |
| AUDUSD | 525 | 2 | 1% | 1% | -64% | -98% | -97% |
| USDCAD | 484 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 103 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 73 | 0 | 3% | 0% | -100% | -95% | -96% |
| 30YRRATE | 67 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 65 | 1 | 3% | 0% | +44% | +49% | +48% |
| 5YRRATE | 62 | 1 | 3% | 3% | +51% | -94% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17445 | 70 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16945 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3623 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3773 | 12 | 3% | 2% | -53% | -92% | -92% |
| 0.1–0.2% | 5708 | 20 | 5% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 6485 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2418 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8704 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,682 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 4:59:50 AM | USDJPY | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:59:50 AM | 10YRRATE | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:59:50 AM | SOL | DOWN | 10 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:59:50 AM | 30YRRATE | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:59:34 AM | NATGAS | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:58:48 AM | COPPER | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:58:32 AM | PLATINUM | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:58:32 AM | ETH | DOWN | 87 sec | +0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:58:16 AM | HYPE | DOWN | 1.7 min | +0.123% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:58:00 AM | DOGE | DOWN | 2.0 min | +0.204% | 0¢ | ❌ Lost | $0.00 |
| 10/27 4:57:45 AM | EURUSD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:57:45 AM | ZEC | DOWN | 2.2 min | +0.487% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 4:57:13 AM | BTC | DOWN | 2.8 min | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:56:40 AM | BNB | DOWN | 3.3 min | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:56:40 AM | NEAR | DOWN | 3.3 min | +0.702% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 4:56:40 AM | XRP | DOWN | 3.3 min | +0.270% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
