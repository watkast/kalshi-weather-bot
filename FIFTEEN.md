# 15-Minute 1¢ Study

*Updated Sun Nov 22, 5:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4757 finished bets | 1% | $194.40 | +37% | +4.09¢ | $81.50 / $112.90 |

*Expect about **85 buys a day** (~$12.81/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4508 | $92.05 | +19% |
| Volatility model ≥ 2%, hold to the close | 8877 | $32.10 | +3% |
| Momentum model ≥ 2%, hold to the close | 7393 | -$43.80 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 64803 | 64769 | 249 (0%) | 1.07% | -$4,357.65 (-56%) | Hold to the close: -$4,357.65 (-56%) |

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
| Volatility model | 38803 | 4.5% | 0.4% (161) | -641% | ❌ Worse |
| Momentum model | 38803 | 4.4% | 0.4% (161) | -665% | ❌ Worse |
| Mean-reversion model | 38803 | 7.9% | 0.4% (161) | -779% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 38803 | 161 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8877 | 78 | +3% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4757 | 51 | +37% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2746 | 30 | +61% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7393 | 57 | -5% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4508 | 41 | +19% | -75% | -74% | -71% |
| Momentum model ≥ 10% | 2932 | 26 | +28% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15805 | 109 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10988 | 89 | -10% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7296 | 64 | +0% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39009 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15283 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10477 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 64769 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 249 | 0% | -$4,357.65 | -56% | — |
| Sell at 2¢ | 2636 | 4% | -$6,864.29 | -88% | 47 sec |
| Sell at 3¢ | 1777 | 3% | -$6,856.62 | -87% | 48 sec |
| Sell at 5¢ | 1209 | 2% | -$6,735.80 | -86% | 62 sec |
| Sell at 10¢ | 737 | 1% | -$6,472.18 | -83% | 65 sec |
| Sell at 25¢ | 396 | 1% | -$5,972.89 | -76% | 80 sec |
| Sell at 50¢ | 258 | 0% | -$5,388.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3356 | 17 | 10% | 4% | -52% | -82% | -83% |
| 2–5 min | 20998 | 112 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16179 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24223 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4361 | 19 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4355 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4353 | 19 | 4% | 2% | -44% | -86% | -86% |
| BNB | 4343 | 22 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 4340 | 11 | 4% | 2% | -68% | -90% | -89% |
| ETH | 4336 | 19 | 7% | 3% | -45% | -82% | -82% |
| BTC | 4313 | 23 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 4310 | 18 | 5% | 2% | -45% | -85% | -86% |
| XRP | 4298 | 16 | 3% | 2% | -53% | -89% | -88% |
| GOLD | 2267 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2258 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2210 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2013 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1971 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1902 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1896 | 6 | 2% | 1% | -70% | -77% | -77% |
| NATGAS | 1860 | 10 | 2% | 1% | -50% | -76% | -76% |
| USDJPY | 1859 | 6 | 2% | 1% | -70% | -96% | -96% |
| PALLADIUM | 1809 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1409 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1340 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 970 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 499 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 476 | 4 | 4% | 2% | -22% | -54% | -53% |
| 30YRRATE | 462 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 451 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33109 | 128 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31660 | 121 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5718 | 25 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 6257 | 25 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 9708 | 35 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12199 | 55 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5118 | 23 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15529 | 48 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 15922 | 69 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 17732 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,174 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/22 4:59:48 PM | XRP | DOWN | 12 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 11/22 4:59:48 PM | BNB | DOWN | 12 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 11/22 4:59:48 PM | DOGE | UP | 12 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 11/22 4:59:48 PM | SOL | DOWN | 12 sec | +0.108% | 0¢ | ❌ Lost | $0.00 |
| 11/22 4:59:32 PM | ETH | DOWN | 28 sec | +0.090% | 0¢ | ❌ Lost | $0.00 |
| 11/22 4:59:32 PM | GOLD | DOWN | 28 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/22 4:59:32 PM | NEAR | DOWN | 28 sec | -0.037% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 4:59:32 PM | PLATINUM | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 4:59:32 PM | PALLADIUM | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 4:59:16 PM | SILVER | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 4:59:16 PM | HYPE | DOWN | 44 sec | +0.095% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 4:59:01 PM | NATGAS | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 4:58:45 PM | BTC | UP | 75 sec | -0.132% | 22¢ | ❌ Lost | -$0.15 |
| 11/22 4:58:45 PM | ZEC | DOWN | 75 sec | +0.227% | 4¢ | ❌ Lost | -$0.15 |
| 11/22 4:58:08 PM | USDJPY | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 4:55:40 PM | AUDUSD | DOWN | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 4:44:57 PM | GBPUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 4:44:41 PM | EURUSD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 4:44:41 PM | ETH | DOWN | 18 sec | -0.011% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 4:44:41 PM | GOLD | DOWN | 18 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/22 4:44:08 PM | XRP | DOWN | 51 sec | +0.130% | 0¢ | ❌ Lost | $0.00 |
| 11/22 4:44:08 PM | SOL | DOWN | 51 sec | +0.085% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 4:43:52 PM | USDJPY | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 4:43:52 PM | ZEC | DOWN | 67 sec | +0.142% | 0¢ | ❌ Lost | $0.00 |
| 11/22 4:43:52 PM | NEAR | DOWN | 67 sec | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 4:43:52 PM | COPPER | UP | 67 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/22 4:42:47 PM | DOGE | DOWN | 2.2 min | +0.185% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 4:40:06 PM | HYPE | DOWN | 4.9 min | +0.519% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 4:40:06 PM | BNB | DOWN | 4.9 min | +0.257% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 4:39:17 PM | BTC | DOWN | 5.7 min | +0.518% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
