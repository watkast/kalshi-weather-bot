# 15-Minute 1¢ Study

*Updated Tue Nov 24, 10:43 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4868 finished bets | 1% | $211.75 | +40% | +4.35¢ | $88.90 / $122.85 |

*Expect about **84 buys a day** (~$12.60/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4618 | $109.85 | +22% |
| Volatility model ≥ 2%, hold to the close | 9068 | $39.70 | +4% |
| Momentum model ≥ 2%, hold to the close | 7544 | -$30.50 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 67103 | 67056 | 255 (0%) | 1.07% | -$4,545.75 (-56%) | Hold to the close: -$4,545.75 (-56%) |

*In play or awaiting result: 19. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 39860 | 4.5% | 0.4% (164) | -649% | ❌ Worse |
| Momentum model | 39860 | 4.4% | 0.4% (164) | -671% | ❌ Worse |
| Mean-reversion model | 39860 | 7.9% | 0.4% (164) | -787% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39860 | 164 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 9068 | 80 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4868 | 53 | +40% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2824 | 32 | +68% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7544 | 59 | -4% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4618 | 43 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3015 | 28 | +34% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16203 | 112 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11277 | 92 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7495 | 66 | +1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40066 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15932 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11058 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 67056 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 255 | 0% | -$4,545.75 | -56% | — |
| Sell at 2¢ | 2741 | 4% | -$7,109.09 | -88% | 47 sec |
| Sell at 3¢ | 1846 | 3% | -$7,101.81 | -88% | 48 sec |
| Sell at 5¢ | 1253 | 2% | -$6,979.30 | -86% | 62 sec |
| Sell at 10¢ | 767 | 1% | -$6,704.98 | -83% | 65 sec |
| Sell at 25¢ | 413 | 1% | -$6,188.72 | -76% | 79 sec |
| Sell at 50¢ | 265 | 0% | -$5,585.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3442 | 17 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 21702 | 116 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16770 | 57 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25129 | 65 | 1% | 0% | -63% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4480 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4474 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4468 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4462 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4458 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4452 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4431 | 24 | 5% | 2% | -26% | -86% | -87% |
| NEAR | 4426 | 18 | 5% | 2% | -47% | -85% | -86% |
| XRP | 4415 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2360 | 8 | 5% | 2% | -58% | -83% | -84% |
| WTI | 2346 | 8 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 2299 | 9 | 5% | 2% | -53% | -83% | -84% |
| PLATINUM | 2089 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2047 | 7 | 3% | 1% | -68% | -91% | -90% |
| GBPUSD | 1981 | 8 | 2% | 1% | -62% | -96% | -96% |
| COPPER | 1980 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1945 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1938 | 10 | 2% | 1% | -52% | -77% | -77% |
| PALLADIUM | 1877 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1501 | 7 | 2% | 1% | -56% | -90% | -90% |
| USDCAD | 1415 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1043 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 538 | 2 | 3% | 1% | -65% | -77% | -75% |
| 2YRRATE | 501 | 4 | 4% | 2% | -25% | -56% | -55% |
| 30YRRATE | 498 | 0 | 3% | 1% | -100% | -95% | -93% |
| 5YRRATE | 488 | 2 | 4% | 2% | -62% | -94% | -95% |
| INX | 124 | 1 | 2% | 1% | -25% | -97% | -98% |
| USDMXN | 20 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34302 | 131 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 32754 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5835 | 25 | 2% | 1% | -21% | -79% | -78% |
| 0.05–0.1% | 6386 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 9975 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12620 | 56 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5241 | 23 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16271 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15699 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16634 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18452 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,113 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/24 10:43:37 PM | NEAR | UP | 82 sec | -0.318% | — | In play | — |
| 11/24 10:43:21 PM | NATGAS | UP | 1.6 min | — | — | In play | — |
| 11/24 10:43:21 PM | GOLD | UP | 1.6 min | — | — | In play | — |
| 11/24 10:43:21 PM | DOGE | UP | 1.6 min | -0.227% | — | In play | — |
| 11/24 10:43:05 PM | XRP | UP | 1.9 min | -0.175% | — | In play | — |
| 11/24 10:42:49 PM | SOL | UP | 2.2 min | -0.256% | — | In play | — |
| 11/24 10:42:43 PM | PLATINUM | UP | 2.3 min | — | — | In play | — |
| 11/24 10:42:43 PM | BTC | UP | 2.3 min | -0.213% | — | In play | — |
| 11/24 10:42:04 PM | BNB | UP | 2.9 min | -0.253% | — | In play | — |
| 11/24 10:41:48 PM | COPPER | UP | 3.2 min | — | — | In play | — |
| 11/24 10:41:17 PM | ETH | UP | 3.7 min | -0.252% | — | In play | — |
| 11/24 10:40:45 PM | ZEC | UP | 4.2 min | -0.531% | — | In play | — |
| 11/24 10:40:29 PM | GBPUSD | UP | 4.5 min | — | — | In play | — |
| 11/24 10:29:55 PM | NEAR | UP | 4 sec | -0.115% | 0¢ | ❌ Lost | $0.00 |
| 11/24 10:29:55 PM | EURUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:29:55 PM | GBPUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:29:55 PM | BTC | UP | 4 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 11/24 10:29:55 PM | DOGE | UP | 4 sec | -0.055% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 10:29:33 PM | PLATINUM | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:29:33 PM | BNB | DOWN | 27 sec | +0.009% | 0¢ | ❌ Lost | $0.00 |
| 11/24 10:29:33 PM | SOL | UP | 27 sec | -0.116% | 0¢ | ❌ Lost | $0.00 |
| 11/24 10:29:33 PM | AUDUSD | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:29:03 PM | COPPER | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:29:03 PM | GOLD | UP | 57 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/24 10:29:03 PM | XRP | UP | 57 sec | -0.142% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 10:29:03 PM | HYPE | DOWN | 57 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |
| 11/24 10:28:48 PM | ZEC | UP | 71 sec | -0.299% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 10:28:13 PM | SILVER | UP | 1.8 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/24 10:28:13 PM | NATGAS | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:27:57 PM | WTI | UP | 2.0 min | — | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
