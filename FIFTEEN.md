# 15-Minute 1¢ Study

*Updated Tue Oct 27, 9:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2912 finished bets | 1% | $91.65 | +28% | +3.15¢ | $90.45 / $1.20 |

*Expect about **98 buys a day** (~$14.63/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2714 | $51.80 | +17% |
| Volatility model ≥ 2%, hold to the close | 5408 | $25.70 | +4% |
| Momentum model ≥ 2%, hold to the close | 4480 | -$46.15 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 35559 | 35551 | 137 (0%) | 1.07% | -$2,414.30 (-56%) | Hold to the close: -$2,414.30 (-56%) |

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
| Volatility model | 22366 | 4.7% | 0.4% (92) | -662% | ❌ Worse |
| Momentum model | 22366 | 4.6% | 0.4% (92) | -687% | ❌ Worse |
| Mean-reversion model | 22366 | 8.0% | 0.4% (92) | -802% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22366 | 92 | -48% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5408 | 49 | +4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2912 | 30 | +28% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1655 | 19 | +62% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4480 | 34 | -9% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2714 | 25 | +17% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1780 | 17 | +32% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 9098 | 63 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6381 | 53 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4262 | 38 | +1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22566 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 8427 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4558 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 35551 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 137 | 0% | -$2,414.30 | -56% | — |
| Sell at 2¢ | 1353 | 4% | -$3,784.52 | -87% | 47 sec |
| Sell at 3¢ | 928 | 3% | -$3,774.38 | -87% | 48 sec |
| Sell at 5¢ | 644 | 2% | -$3,717.70 | -86% | 63 sec |
| Sell at 10¢ | 394 | 1% | -$3,564.16 | -82% | 65 sec |
| Sell at 25¢ | 213 | 1% | -$3,277.27 | -76% | 88 sec |
| Sell at 50¢ | 141 | 0% | -$2,946.55 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1588 | 8 | 11% | 4% | -52% | -81% | -82% |
| 2–5 min | 11373 | 65 | 7% | 3% | -44% | -87% | -86% |
| 1–2 min | 9002 | 32 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13584 | 32 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2527 | 12 | 5% | 2% | -39% | -88% | -88% |
| HYPE | 2520 | 8 | 5% | 3% | -61% | -89% | -87% |
| BNB | 2518 | 15 | 5% | 2% | -25% | -84% | -83% |
| SOL | 2514 | 7 | 4% | 2% | -65% | -92% | -92% |
| ETH | 2506 | 11 | 6% | 3% | -47% | -86% | -85% |
| DOGE | 2505 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2495 | 11 | 3% | 1% | -46% | -89% | -89% |
| NEAR | 2493 | 12 | 5% | 2% | -37% | -82% | -82% |
| BTC | 2488 | 13 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1338 | 5 | 4% | 2% | -55% | -81% | -83% |
| SILVER | 1305 | 6 | 4% | 2% | -46% | -82% | -82% |
| WTI | 1289 | 4 | 3% | 1% | -63% | -93% | -94% |
| PLATINUM | 1159 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1105 | 4 | 1% | 1% | -66% | -72% | -72% |
| EURUSD | 1083 | 3 | 2% | 1% | -74% | -88% | -88% |
| NATGAS | 1065 | 6 | 2% | 1% | -47% | -79% | -79% |
| PALLADIUM | 1024 | 2 | 1% | 0% | -82% | -89% | -89% |
| GBPUSD | 1020 | 2 | 2% | 1% | -82% | -96% | -96% |
| USDJPY | 1004 | 5 | 2% | 1% | -54% | -97% | -96% |
| AUDUSD | 561 | 3 | 1% | 1% | -50% | -81% | -80% |
| USDCAD | 520 | 0 | 1% | 0% | -100% | -98% | -98% |
| BRENT | 142 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 101 | 0 | 4% | 0% | -100% | -93% | -92% |
| 30YRRATE | 92 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 89 | 1 | 3% | 1% | +5% | +11% | +11% |
| 5YRRATE | 88 | 1 | 5% | 2% | +6% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17972 | 76 | 4% | 2% | -51% | -87% | -86% |
| DOWN (bought NO) | 17579 | 61 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3712 | 19 | 2% | 1% | -13% | -81% | -80% |
| 0.05–0.1% | 3877 | 14 | 3% | 2% | -46% | -92% | -91% |
| 0.1–0.2% | 5865 | 22 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 6639 | 29 | 7% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2469 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9607 | 32 | 3% | 2% | -62% | -90% | -90% |

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
| 10/27 8:59:58 PM | SILVER | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:59:41 PM | GOLD | UP | 19 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:59:41 PM | HYPE | DOWN | 19 sec | -0.018% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:59:41 PM | USDCAD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:58:54 PM | ETH | DOWN | 65 sec | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:58:54 PM | ZEC | DOWN | 65 sec | +0.076% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:58:07 PM | PLATINUM | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:57:52 PM | PALLADIUM | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:57:37 PM | XRP | DOWN | 2.4 min | +0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:57:37 PM | BTC | DOWN | 2.4 min | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:57:05 PM | SOL | DOWN | 2.9 min | +0.137% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:56:49 PM | BNB | DOWN | 3.2 min | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:55:45 PM | DOGE | DOWN | 4.2 min | +0.223% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:49 PM | DOGE | UP | 10 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:44:49 PM | AUDUSD | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:49 PM | BNB | UP | 10 sec | -0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:44:33 PM | BTC | UP | 26 sec | -0.030% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:17 PM | NEAR | DOWN | 42 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:44:17 PM | SOL | DOWN | 42 sec | +0.033% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:01 PM | WTI | UP | 59 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:44:01 PM | SILVER | DOWN | 59 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:43:14 PM | GOLD | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:43:14 PM | HYPE | UP | 1.8 min | -0.218% | 0¢ | ❌ Lost | $0.00 |
| 10/27 8:43:14 PM | GBPUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:42:25 PM | XRP | UP | 2.6 min | -0.307% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:42:09 PM | BRENT | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:41:54 PM | ZEC | DOWN | 3.1 min | +0.290% | 4¢ | ❌ Lost | -$0.15 |
| 10/27 8:41:54 PM | EURUSD | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 8:41:07 PM | PLATINUM | DOWN | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 8:29:46 PM | ZEC | DOWN | 13 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
