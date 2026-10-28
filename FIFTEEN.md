# 15-Minute 1¢ Study

*Updated Tue Oct 27, 8:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2902 finished bets | 1% | $92.70 | +28% | +3.19¢ | $91.20 / $1.50 |

*Expect about **97 buys a day** (~$14.60/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2709 | $52.10 | +17% |
| Volatility model ≥ 2%, hold to the close | 5396 | $27.05 | +4% |
| Momentum model ≥ 2%, hold to the close | 4470 | -$45.10 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 35498 | 35490 | 137 (0%) | 1.07% | -$2,407.85 (-56%) | Hold to the close: -$2,407.85 (-56%) |

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
| Volatility model | 22332 | 4.7% | 0.4% (92) | -659% | ❌ Worse |
| Momentum model | 22332 | 4.6% | 0.4% (92) | -685% | ❌ Worse |
| Mean-reversion model | 22332 | 8.0% | 0.4% (92) | -800% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22332 | 92 | -48% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5396 | 49 | +4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2902 | 30 | +28% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1650 | 19 | +63% | -67% | -65% | -63% |
| Momentum model ≥ 2% | 4470 | 34 | -9% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2709 | 25 | +17% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1776 | 17 | +32% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 9080 | 63 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6366 | 53 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4250 | 38 | +1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22532 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 8408 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4550 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 35490 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 137 | 0% | -$2,407.85 | -56% | — |
| Sell at 2¢ | 1351 | 4% | -$3,778.59 | -87% | 47 sec |
| Sell at 3¢ | 926 | 3% | -$3,768.71 | -87% | 48 sec |
| Sell at 5¢ | 643 | 2% | -$3,711.90 | -86% | 63 sec |
| Sell at 10¢ | 394 | 1% | -$3,557.71 | -82% | 65 sec |
| Sell at 25¢ | 213 | 1% | -$3,270.82 | -76% | 88 sec |
| Sell at 50¢ | 141 | 0% | -$2,940.10 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1587 | 8 | 11% | 4% | -52% | -81% | -82% |
| 2–5 min | 11360 | 65 | 7% | 3% | -44% | -87% | -86% |
| 1–2 min | 8989 | 32 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13550 | 32 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2523 | 12 | 5% | 2% | -39% | -89% | -88% |
| HYPE | 2516 | 8 | 5% | 3% | -61% | -89% | -87% |
| BNB | 2514 | 15 | 5% | 2% | -25% | -84% | -83% |
| SOL | 2510 | 7 | 4% | 2% | -65% | -92% | -92% |
| ETH | 2503 | 11 | 6% | 3% | -47% | -86% | -85% |
| DOGE | 2501 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2491 | 11 | 3% | 1% | -46% | -89% | -89% |
| NEAR | 2490 | 12 | 5% | 2% | -37% | -82% | -82% |
| BTC | 2484 | 13 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1335 | 5 | 4% | 2% | -55% | -81% | -83% |
| SILVER | 1301 | 6 | 4% | 2% | -46% | -82% | -82% |
| WTI | 1287 | 4 | 3% | 1% | -63% | -93% | -94% |
| PLATINUM | 1157 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1104 | 4 | 1% | 1% | -66% | -72% | -72% |
| EURUSD | 1080 | 3 | 2% | 1% | -74% | -88% | -88% |
| NATGAS | 1063 | 6 | 2% | 1% | -47% | -79% | -79% |
| PALLADIUM | 1022 | 2 | 1% | 0% | -82% | -89% | -89% |
| GBPUSD | 1018 | 2 | 2% | 1% | -82% | -96% | -96% |
| USDJPY | 1004 | 5 | 2% | 1% | -54% | -97% | -96% |
| AUDUSD | 559 | 3 | 1% | 1% | -50% | -81% | -80% |
| USDCAD | 519 | 0 | 1% | 0% | -100% | -98% | -98% |
| BRENT | 139 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 101 | 0 | 4% | 0% | -100% | -93% | -92% |
| 30YRRATE | 92 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 89 | 1 | 3% | 1% | +5% | +11% | +11% |
| 5YRRATE | 88 | 1 | 5% | 2% | +6% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17940 | 76 | 4% | 2% | -51% | -87% | -86% |
| DOWN (bought NO) | 17550 | 61 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3704 | 19 | 2% | 1% | -12% | -81% | -80% |
| 0.05–0.1% | 3868 | 14 | 3% | 2% | -46% | -92% | -91% |
| 0.1–0.2% | 5856 | 22 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 6633 | 29 | 7% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2467 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9546 | 32 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,642 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 7:59:45 PM | DOGE | DOWN | 14 sec | +0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/27 7:59:45 PM | GBPUSD | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:59:45 PM | BTC | DOWN | 14 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/27 7:59:45 PM | ZEC | DOWN | 14 sec | -0.065% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:59:29 PM | EURUSD | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:59:13 PM | HYPE | DOWN | 46 sec | +0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:58:57 PM | COPPER | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:58:57 PM | ETH | UP | 62 sec | -0.009% | 4¢ | ❌ Lost | -$0.15 |
| 10/27 7:58:57 PM | BNB | UP | 62 sec | -0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:58:57 PM | AUDUSD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:58:57 PM | SOL | DOWN | 62 sec | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:58:26 PM | SILVER | UP | 1.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 7:57:54 PM | BRENT | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:57:54 PM | NATGAS | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:57:54 PM | WTI | DOWN | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:57:39 PM | XRP | DOWN | 2.4 min | +0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:57:07 PM | PALLADIUM | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:56:51 PM | PLATINUM | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:56:12 PM | NEAR | DOWN | 3.8 min | +0.518% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:55:56 PM | GOLD | UP | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:44:48 PM | USDCAD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:44:32 PM | PLATINUM | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:44:32 PM | GBPUSD | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:44:32 PM | EURUSD | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:44:32 PM | PALLADIUM | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:44:16 PM | HYPE | UP | 43 sec | -0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:44:00 PM | GOLD | UP | 59 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 7:42:25 PM | AUDUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:42:09 PM | USDJPY | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:41:22 PM | ZEC | DOWN | 3.6 min | +0.420% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
