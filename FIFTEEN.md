# 15-Minute 1¢ Study

*Updated Tue Oct 27, 8:42 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2846 finished bets | 1% | $69.95 | +22% | +2.46¢ | $80.95 / -$11.00 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2655 | $42.90 | +15% |
| Volatility model ≥ 2%, hold to the close | 5292 | -$17.55 | -3% |
| Momentum model ≥ 2%, hold to the close | 4396 | -$51.90 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34676 | 34667 | 129 (0%) | 1.07% | -$2,416.20 (-57%) | Hold to the close: -$2,416.20 (-57%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 21932 | 4.6% | 0.4% (87) | -672% | ❌ Worse |
| Momentum model | 21932 | 4.6% | 0.4% (87) | -697% | ❌ Worse |
| Mean-reversion model | 21932 | 8.0% | 0.4% (87) | -816% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21932 | 87 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5292 | 45 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2846 | 28 | +22% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1614 | 18 | +57% | -67% | -66% | -63% |
| Momentum model ≥ 2% | 4396 | 33 | -10% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2655 | 24 | +15% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1733 | 16 | +27% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8896 | 58 | -29% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6226 | 48 | -15% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4149 | 34 | -8% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22132 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8184 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4351 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34667 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 129 | 0% | -$2,416.20 | -57% | — |
| Sell at 2¢ | 1307 | 4% | -$3,700.38 | -88% | 47 sec |
| Sell at 3¢ | 891 | 3% | -$3,692.71 | -87% | 48 sec |
| Sell at 5¢ | 616 | 2% | -$3,639.80 | -86% | 62 sec |
| Sell at 10¢ | 380 | 1% | -$3,486.40 | -83% | 65 sec |
| Sell at 25¢ | 205 | 1% | -$3,221.65 | -76% | 1.5 min |
| Sell at 50¢ | 135 | 0% | -$2,904.95 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1539 | 8 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 11137 | 60 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8789 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13198 | 30 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2479 | 12 | 5% | 2% | -38% | -89% | -89% |
| HYPE | 2470 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2469 | 14 | 5% | 2% | -29% | -84% | -83% |
| SOL | 2466 | 6 | 4% | 2% | -70% | -92% | -92% |
| ETH | 2460 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2455 | 5 | 4% | 2% | -75% | -90% | -90% |
| NEAR | 2448 | 12 | 5% | 2% | -36% | -82% | -82% |
| XRP | 2445 | 9 | 3% | 1% | -55% | -89% | -89% |
| BTC | 2440 | 12 | 5% | 2% | -34% | -88% | -89% |
| GOLD | 1304 | 5 | 4% | 2% | -54% | -81% | -83% |
| SILVER | 1274 | 6 | 4% | 2% | -45% | -82% | -82% |
| WTI | 1254 | 3 | 3% | 1% | -72% | -94% | -95% |
| PLATINUM | 1125 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1081 | 4 | 1% | 1% | -65% | -72% | -72% |
| EURUSD | 1050 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1038 | 6 | 2% | 1% | -46% | -79% | -78% |
| PALLADIUM | 996 | 2 | 1% | 0% | -81% | -89% | -89% |
| GBPUSD | 989 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 977 | 5 | 1% | 1% | -52% | -98% | -97% |
| AUDUSD | 535 | 2 | 1% | 1% | -65% | -98% | -97% |
| USDCAD | 496 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 112 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 84 | 0 | 5% | 0% | -100% | -92% | -91% |
| 30YRRATE | 75 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 73 | 1 | 5% | 3% | +28% | -91% | -93% |
| 2YRRATE | 72 | 1 | 4% | 1% | +30% | +37% | +37% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17556 | 71 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 17111 | 58 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3633 | 18 | 2% | 1% | -16% | -81% | -80% |
| 0.05–0.1% | 3785 | 12 | 3% | 2% | -53% | -92% | -92% |
| 0.1–0.2% | 5739 | 20 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 6538 | 29 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2433 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8465 | 39 | 4% | 2% | -48% | -87% | -86% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,664 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 8:41:32 AM | NATGAS | DOWN | 3.5 min | — | — | In play | — |
| 10/27 8:29:56 AM | 5YRRATE | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:29:40 AM | AUDUSD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:29:24 AM | USDCAD | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:29:24 AM | DOGE | DOWN | 35 sec | +0.009% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:29:08 AM | USDJPY | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:28:53 AM | PALLADIUM | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:28:53 AM | BTC | DOWN | 66 sec | +0.160% | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:28:53 AM | XRP | DOWN | 66 sec | +0.183% | 1¢ | ❌ Lost | $0.00 |
| 10/27 8:28:53 AM | SOL | DOWN | 66 sec | +0.162% | 22¢ | ❌ Lost | -$0.15 |
| 10/27 8:28:37 AM | NEAR | DOWN | 82 sec | +0.290% | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:28:37 AM | GOLD | DOWN | 82 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:28:21 AM | ZEC | DOWN | 1.6 min | +0.299% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:28:05 AM | SILVER | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:28:05 AM | BRENT | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:27:33 AM | PLATINUM | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:27:17 AM | GBPUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:26:30 AM | ETH | UP | 3.5 min | -0.281% | 91¢ | ❌ Lost | -$0.15 |
| 10/27 8:25:58 AM | WTI | UP | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:25:25 AM | EURUSD | UP | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:25:09 AM | BNB | UP | 4.8 min | -0.210% | 88¢ | ✅ Won | $13.85 |
| 10/27 8:14:29 AM | 2YRRATE | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:14:29 AM | BRENT | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:14:29 AM | WTI | UP | 30 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:14:29 AM | 10YRRATE | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:14:13 AM | 5YRRATE | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:14:13 AM | NEAR | DOWN | 46 sec | +0.219% | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:14:13 AM | USDJPY | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:13:26 AM | HYPE | DOWN | 1.6 min | +0.242% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:13:26 AM | ETH | DOWN | 1.6 min | +0.270% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
