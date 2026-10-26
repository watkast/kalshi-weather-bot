# 15-Minute 1¢ Study

*Updated Mon Oct 26, 3:58 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2773 finished bets | 1% | $78.05 | +25% | +2.81¢ | $29.30 / $48.75 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2582 | $51.30 | +18% |
| Volatility model ≥ 2%, hold to the close | 5163 | -$15.80 | -3% |
| Momentum model ≥ 2%, hold to the close | 4292 | -$40.05 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33442 | 33430 | 124 (0%) | 1.07% | -$2,328.10 (-57%) | Hold to the close: -$2,328.10 (-57%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 21357 | 4.6% | 0.4% (86) | -664% | ❌ Worse |
| Momentum model | 21357 | 4.5% | 0.4% (86) | -688% | ❌ Worse |
| Mean-reversion model | 21357 | 7.9% | 0.4% (86) | -805% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21357 | 86 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5163 | 44 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2773 | 28 | +25% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1570 | 18 | +61% | -67% | -65% | -62% |
| Momentum model ≥ 2% | 4292 | 33 | -8% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2582 | 24 | +18% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1682 | 16 | +31% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8639 | 57 | -28% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 6051 | 47 | -15% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4030 | 33 | -8% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21557 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7822 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4051 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33430 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 124 | 0% | -$2,328.10 | -57% | — |
| Sell at 2¢ | 1264 | 4% | -$3,567.46 | -88% | 47 sec |
| Sell at 3¢ | 864 | 3% | -$3,559.14 | -88% | 48 sec |
| Sell at 5¢ | 600 | 2% | -$3,506.10 | -86% | 61 sec |
| Sell at 10¢ | 371 | 1% | -$3,368.09 | -83% | 65 sec |
| Sell at 25¢ | 197 | 1% | -$3,118.03 | -77% | 82 sec |
| Sell at 50¢ | 127 | 0% | -$2,828.85 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1469 | 8 | 11% | 4% | -48% | -80% | -82% |
| 2–5 min | 10719 | 57 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8467 | 31 | 3% | 1% | -60% | -92% | -91% |
| Under 1 min | 12771 | 28 | 1% | 0% | -69% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2415 | 12 | 5% | 2% | -37% | -88% | -88% |
| HYPE | 2408 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2405 | 13 | 5% | 2% | -32% | -84% | -83% |
| SOL | 2401 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2396 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2389 | 5 | 4% | 2% | -74% | -91% | -90% |
| NEAR | 2383 | 12 | 5% | 2% | -35% | -82% | -81% |
| XRP | 2383 | 9 | 3% | 1% | -53% | -89% | -89% |
| BTC | 2377 | 12 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1257 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1223 | 6 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1204 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1070 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1040 | 4 | 1% | 1% | -64% | -71% | -71% |
| EURUSD | 1004 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 998 | 5 | 2% | 1% | -53% | -87% | -86% |
| PALLADIUM | 959 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 946 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 930 | 5 | 1% | 1% | -50% | -98% | -97% |
| AUDUSD | 490 | 1 | 1% | 1% | -81% | -98% | -97% |
| USDCAD | 454 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 71 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 63 | 0 | 3% | 0% | -100% | -94% | -96% |
| 2YRRATE | 57 | 1 | 4% | 0% | +64% | +70% | +68% |
| 30YRRATE | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 50 | 1 | 4% | 4% | +87% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16946 | 68 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16484 | 56 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3560 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3690 | 12 | 3% | 2% | -52% | -92% | -91% |
| 0.1–0.2% | 5579 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6329 | 28 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2395 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 7871 | 25 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,725 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 3:58:13 PM | HYPE | DOWN | 1.8 min | +0.103% | — | In play | — |
| 10/26 3:58:13 PM | SOL | UP | 1.8 min | -0.196% | — | In play | — |
| 10/26 3:57:23 PM | NEAR | UP | 2.6 min | -0.427% | — | In play | — |
| 10/26 3:56:36 PM | ZEC | UP | 3.4 min | -0.421% | — | In play | — |
| 10/26 3:44:56 PM | WTI | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:44:56 PM | GBPUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:44:40 PM | USDJPY | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:44:40 PM | HYPE | UP | 20 sec | -0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:43:36 PM | BTC | DOWN | 84 sec | +0.087% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:43:36 PM | SOL | DOWN | 84 sec | +0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:41:45 PM | DOGE | DOWN | 3.2 min | +0.253% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:40:40 PM | BNB | DOWN | 4.3 min | +0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:40:24 PM | ZEC | DOWN | 4.6 min | +0.597% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:40:24 PM | XRP | DOWN | 4.6 min | +0.256% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:40:08 PM | ETH | DOWN | 4.8 min | +0.238% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:39:52 PM | NEAR | DOWN | 5.1 min | +0.635% | 2¢ | ❌ Lost | -$0.15 |
| 10/26 3:29:54 PM | WTI | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:29:22 PM | USDJPY | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:29:06 PM | NATGAS | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:28:34 PM | BNB | DOWN | 85 sec | +0.066% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:28:34 PM | DOGE | DOWN | 85 sec | +0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:28:18 PM | ETH | DOWN | 1.7 min | +0.155% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:28:18 PM | HYPE | DOWN | 1.7 min | +0.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:27:23 PM | NEAR | DOWN | 2.6 min | +0.399% | 2¢ | ❌ Lost | -$0.15 |
| 10/26 3:27:23 PM | XRP | DOWN | 2.6 min | +0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:27:07 PM | ZEC | DOWN | 2.9 min | +0.539% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:26:52 PM | SOL | DOWN | 3.1 min | +0.217% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:26:52 PM | BTC | DOWN | 3.1 min | +0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:14:48 PM | BNB | DOWN | 12 sec | +0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:14:48 PM | EURUSD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
