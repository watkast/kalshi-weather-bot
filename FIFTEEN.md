# 15-Minute 1¢ Study

*Updated Tue Nov 10, 8:33 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4164 finished bets | 1% | $181.25 | +39% | +4.35¢ | $88.75 / $92.50 |

*Expect about **96 buys a day** (~$14.40/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3882 | $97.70 | +23% |
| Volatility model ≥ 2%, hold to the close | 7620 | $62.75 | +7% |
| Momentum model ≥ 2%, hold to the close | 6319 | -$12.00 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 52217 | 52200 | 200 (0%) | 1.07% | -$3,560.90 (-56%) | Hold to the close: -$3,560.90 (-56%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31623 | 4.8% | 0.4% (128) | -678% | ❌ Worse |
| Momentum model | 31623 | 4.6% | 0.4% (128) | -703% | ❌ Worse |
| Mean-reversion model | 31623 | 8.1% | 0.4% (128) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31623 | 128 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7620 | 70 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4164 | 46 | +39% | -72% | -70% | -66% |
| Volatility model ≥ 10% | 2400 | 28 | +67% | -62% | -60% | -56% |
| Momentum model ≥ 2% | 6319 | 51 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3882 | 37 | +23% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2547 | 25 | +38% | -65% | -65% | -60% |
| Mean-reversion model ≥ 2% | 13091 | 91 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9178 | 78 | -6% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6136 | 56 | +4% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31828 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12396 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7976 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 52200 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 200 | 0% | -$3,560.90 | -56% | — |
| Sell at 2¢ | 2076 | 4% | -$5,541.14 | -87% | 47 sec |
| Sell at 3¢ | 1413 | 3% | -$5,529.83 | -87% | 48 sec |
| Sell at 5¢ | 984 | 2% | -$5,413.30 | -85% | 63 sec |
| Sell at 10¢ | 596 | 1% | -$5,188.14 | -82% | 65 sec |
| Sell at 25¢ | 315 | 1% | -$4,814.25 | -76% | 83 sec |
| Sell at 50¢ | 206 | 0% | -$4,368.40 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2606 | 12 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 16875 | 93 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13172 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19535 | 51 | 1% | 0% | -63% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3564 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3560 | 16 | 4% | 2% | -43% | -87% | -86% |
| HYPE | 3552 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3545 | 19 | 5% | 2% | -32% | -86% | -85% |
| DOGE | 3540 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3535 | 15 | 7% | 3% | -48% | -82% | -81% |
| BTC | 3515 | 17 | 5% | 2% | -34% | -87% | -88% |
| NEAR | 3514 | 16 | 5% | 2% | -41% | -85% | -85% |
| XRP | 3503 | 13 | 3% | 1% | -54% | -89% | -88% |
| GOLD | 1877 | 5 | 5% | 2% | -68% | -81% | -83% |
| WTI | 1852 | 6 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 1830 | 8 | 5% | 2% | -48% | -83% | -82% |
| PLATINUM | 1657 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1592 | 5 | 2% | 1% | -71% | -90% | -89% |
| COPPER | 1555 | 6 | 2% | 1% | -64% | -73% | -73% |
| NATGAS | 1516 | 8 | 2% | 1% | -51% | -78% | -77% |
| GBPUSD | 1511 | 5 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1492 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1492 | 6 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 1056 | 6 | 2% | 1% | -47% | -87% | -87% |
| USDCAD | 1023 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 617 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 342 | 2 | 4% | 2% | -45% | -65% | -63% |
| 2YRRATE | 326 | 4 | 4% | 2% | +15% | -35% | -34% |
| 30YRRATE | 319 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 302 | 2 | 4% | 2% | -38% | -93% | -95% |
| INX | 13 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26464 | 105 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 25736 | 95 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5106 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5435 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8177 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9512 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3590 | 15 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12908 | 43 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 12640 | 57 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12535 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 14117 | 43 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,888 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 8:29:40 AM | PLATINUM | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:29:23 AM | PALLADIUM | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:29:23 AM | GOLD | UP | 36 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:29:04 AM | 2YRRATE | DOWN | 55 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:28:48 AM | INX | UP | 71 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:28:48 AM | BRENT | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:28:32 AM | GBPUSD | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:28:17 AM | BTC | UP | 1.7 min | -0.391% | 0¢ | ❌ Lost | $0.00 |
| 11/10 8:28:17 AM | BNB | UP | 1.7 min | -0.296% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:28:17 AM | ETH | UP | 1.7 min | -0.584% | 0¢ | ❌ Lost | $0.00 |
| 11/10 8:28:17 AM | WTI | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:28:17 AM | NEAR | UP | 1.7 min | -0.820% | 0¢ | ❌ Lost | $0.00 |
| 11/10 8:28:17 AM | USDJPY | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:27:42 AM | XRP | UP | 2.3 min | -0.556% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:27:11 AM | HYPE | UP | 2.8 min | -0.622% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:27:11 AM | USDCAD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:26:56 AM | DOGE | UP | 3.1 min | -0.513% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:26:56 AM | ZEC | UP | 3.1 min | -0.939% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:26:40 AM | NATGAS | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:26:40 AM | SOL | UP | 3.3 min | -0.728% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:26:40 AM | SILVER | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:26:40 AM | AUDUSD | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:14:48 AM | 5YRRATE | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:14:48 AM | AUDUSD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:14:32 AM | BNB | UP | 27 sec | -0.093% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:14:32 AM | DOGE | UP | 27 sec | -0.076% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:14:16 AM | XRP | UP | 43 sec | -0.254% | 0¢ | ❌ Lost | $0.00 |
| 11/10 8:14:16 AM | ETH | UP | 43 sec | -0.260% | 0¢ | ❌ Lost | $0.00 |
| 11/10 8:14:16 AM | SILVER | DOWN | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 8:14:16 AM | ZEC | UP | 43 sec | -0.443% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
