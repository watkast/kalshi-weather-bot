# 15-Minute 1¢ Study

*Updated Thu Oct 15, 10:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1569 finished bets | 1% | $77.85 | +45% | +4.96¢ | $27.55 / $50.30 |

*Expect about **88 buys a day** (~$13.15/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1457 | $52.35 | +33% |
| Momentum model ≥ 2%, hold to the close | 2447 | -$3.20 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 1569 | -$17.40 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20177 | 20170 | 78 (0%) | 1.07% | -$1,359.75 (-55%) | Hold to the close: -$1,359.75 (-55%) |

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
| Volatility model | 12961 | 4.4% | 0.4% (53) | -636% | ❌ Worse |
| Momentum model | 12961 | 4.4% | 0.4% (53) | -661% | ❌ Worse |
| Mean-reversion model | 12961 | 7.3% | 0.4% (53) | -761% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12961 | 53 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2851 | 23 | -7% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1569 | 18 | +45% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 922 | 11 | +69% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2447 | 20 | -1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1457 | 15 | +33% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 975 | 10 | +44% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4850 | 33 | -26% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3335 | 26 | -14% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2183 | 15 | -21% | -80% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13159 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4980 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2031 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20170 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,359.75 | -55% | — |
| Sell at 2¢ | 714 | 4% | -$2,182.11 | -89% | 43 sec |
| Sell at 3¢ | 477 | 2% | -$2,181.72 | -89% | 47 sec |
| Sell at 5¢ | 347 | 2% | -$2,142.20 | -87% | 50 sec |
| Sell at 10¢ | 214 | 1% | -$2,059.41 | -84% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,887.31 | -77% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,681.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 658 | 5 | 11% | 3% | -28% | -81% | -86% |
| 2–5 min | 6535 | 36 | 7% | 3% | -46% | -88% | -88% |
| 1–2 min | 5246 | 20 | 3% | 2% | -59% | -92% | -92% |
| Under 1 min | 7727 | 17 | 1% | 0% | -68% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1477 | 11 | 5% | 3% | -7% | -89% | -89% |
| HYPE | 1472 | 5 | 4% | 2% | -58% | -90% | -89% |
| ETH | 1466 | 8 | 5% | 3% | -34% | -88% | -87% |
| DOGE | 1465 | 2 | 4% | 2% | -83% | -91% | -90% |
| BNB | 1464 | 5 | 5% | 2% | -58% | -90% | -90% |
| SOL | 1460 | 2 | 3% | 2% | -83% | -92% | -92% |
| XRP | 1454 | 7 | 3% | 1% | -41% | -86% | -86% |
| BTC | 1452 | 7 | 5% | 2% | -36% | -88% | -91% |
| NEAR | 1449 | 8 | 5% | 3% | -28% | -78% | -78% |
| GOLD | 811 | 1 | 4% | 1% | -85% | -92% | -94% |
| SILVER | 790 | 4 | 3% | 1% | -41% | -79% | -79% |
| WTI | 763 | 3 | 3% | 1% | -54% | -94% | -96% |
| COPPER | 698 | 2 | 2% | 1% | -73% | -83% | -83% |
| PLATINUM | 672 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 623 | 4 | 2% | 2% | -40% | -96% | -95% |
| PALLADIUM | 623 | 2 | 1% | 0% | -70% | -83% | -83% |
| EURUSD | 614 | 3 | 3% | 1% | -54% | -80% | -80% |
| GBPUSD | 576 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 539 | 3 | 1% | 1% | -48% | -99% | -98% |
| AUDUSD | 160 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 142 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10168 | 39 | 4% | 2% | -56% | -89% | -89% |
| DOWN (bought NO) | 10002 | 39 | 4% | 2% | -55% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2194 | 11 | 2% | 1% | -16% | -79% | -78% |
| 0.05–0.1% | 2278 | 7 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 3315 | 10 | 4% | 2% | -63% | -90% | -90% |
| 0.2–0.5% | 3844 | 21 | 6% | 3% | -40% | -88% | -88% |
| Over 0.5% | 1525 | 6 | 6% | 2% | -59% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5671 | 16 | 3% | 2% | -68% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,477 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 9:59:29 PM | NATGAS | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:59:29 PM | WTI | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:58:22 PM | USDCAD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:58:22 PM | USDJPY | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:58:08 PM | GBPUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:58:08 PM | EURUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:57:03 PM | HYPE | DOWN | 3.0 min | +0.370% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:56:46 PM | COPPER | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:55:58 PM | GOLD | DOWN | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:55:58 PM | PALLADIUM | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:55:25 PM | XRP | DOWN | 4.6 min | +0.377% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:55:25 PM | NEAR | DOWN | 4.6 min | +1.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:55:25 PM | PLATINUM | DOWN | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:55:09 PM | DOGE | DOWN | 4.8 min | +0.490% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:55:09 PM | ETH | DOWN | 4.8 min | +0.391% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:55:09 PM | SILVER | DOWN | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:54:34 PM | BTC | DOWN | 5.4 min | +0.405% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:54:18 PM | SOL | DOWN | 5.7 min | +0.718% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:53:30 PM | ZEC | DOWN | 6.5 min | +1.253% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:51:53 PM | BNB | DOWN | 8.1 min | +0.322% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:44:50 PM | COPPER | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:44:34 PM | PLATINUM | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:44:34 PM | WTI | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:44:18 PM | USDJPY | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:43:13 PM | GBPUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:43:13 PM | SILVER | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:43:13 PM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 9:42:24 PM | GOLD | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:41:02 PM | BTC | UP | 4.0 min | -0.313% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 9:40:45 PM | XRP | UP | 4.2 min | -0.666% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
