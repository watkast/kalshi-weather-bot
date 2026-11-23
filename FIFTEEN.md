# 15-Minute 1¢ Study

*Updated Mon Nov 23, 2:44 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4782 finished bets | 1% | $219.70 | +42% | +4.59¢ | $79.70 / $140.00 |

*Expect about **85 buys a day** (~$12.78/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4536 | $116.75 | +24% |
| Volatility model ≥ 2%, hold to the close | 8917 | $55.75 | +5% |
| Momentum model ≥ 2%, hold to the close | 7436 | -$20.75 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 65336 | 65279 | 252 (0%) | 1.07% | -$4,375.95 (-55%) | Hold to the close: -$4,375.95 (-55%) |

*In play or awaiting result: 29. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 39046 | 4.5% | 0.4% (163) | -637% | ❌ Worse |
| Momentum model | 39046 | 4.4% | 0.4% (163) | -660% | ❌ Worse |
| Mean-reversion model | 39046 | 7.9% | 0.4% (163) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39046 | 163 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8917 | 80 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4782 | 53 | +42% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2766 | 32 | +70% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7436 | 59 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4536 | 43 | +24% | -75% | -74% | -71% |
| Momentum model ≥ 10% | 2953 | 28 | +36% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15892 | 111 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 11056 | 91 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7347 | 66 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39252 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15432 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10595 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 65279 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 252 | 0% | -$4,375.95 | -55% | — |
| Sell at 2¢ | 2661 | 4% | -$6,918.09 | -88% | 47 sec |
| Sell at 3¢ | 1793 | 3% | -$6,910.68 | -87% | 48 sec |
| Sell at 5¢ | 1223 | 2% | -$6,787.00 | -86% | 62 sec |
| Sell at 10¢ | 747 | 1% | -$6,519.38 | -82% | 65 sec |
| Sell at 25¢ | 401 | 1% | -$6,016.64 | -76% | 80 sec |
| Sell at 50¢ | 259 | 0% | -$5,413.70 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3381 | 17 | 11% | 4% | -52% | -81% | -83% |
| 2–5 min | 21157 | 113 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16313 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24415 | 65 | 1% | 0% | -61% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4388 | 19 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4382 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4379 | 20 | 4% | 2% | -41% | -86% | -86% |
| BNB | 4371 | 22 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 4366 | 11 | 4% | 2% | -68% | -90% | -89% |
| ETH | 4363 | 19 | 7% | 3% | -45% | -82% | -82% |
| BTC | 4341 | 24 | 5% | 2% | -24% | -86% | -88% |
| NEAR | 4336 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4326 | 16 | 3% | 2% | -53% | -89% | -88% |
| GOLD | 2288 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2274 | 8 | 4% | 1% | -57% | -91% | -92% |
| SILVER | 2234 | 9 | 5% | 2% | -52% | -83% | -84% |
| PLATINUM | 2030 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1990 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1921 | 8 | 2% | 1% | -61% | -96% | -96% |
| COPPER | 1917 | 6 | 2% | 1% | -71% | -77% | -77% |
| NATGAS | 1880 | 10 | 2% | 1% | -50% | -77% | -76% |
| USDJPY | 1879 | 6 | 2% | 1% | -70% | -96% | -96% |
| PALLADIUM | 1825 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1432 | 6 | 2% | 1% | -61% | -90% | -90% |
| USDCAD | 1357 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 984 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 503 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 479 | 4 | 4% | 2% | -22% | -55% | -53% |
| 30YRRATE | 468 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 455 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |
| USDMXN | 3 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33374 | 129 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31905 | 123 | 4% | 2% | -55% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5752 | 25 | 2% | 1% | -21% | -78% | -78% |
| 0.05–0.1% | 6286 | 26 | 3% | 2% | -34% | -91% | -90% |
| 0.1–0.2% | 9764 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12290 | 55 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5151 | 23 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15697 | 49 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 15984 | 71 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 18012 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,161 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/23 2:44:46 AM | NATGAS | DOWN | 14 sec | — | — | In play | — |
| 11/23 2:44:30 AM | 5YRRATE | UP | 30 sec | — | — | In play | — |
| 11/23 2:44:30 AM | 30YRRATE | UP | 30 sec | — | — | In play | — |
| 11/23 2:44:30 AM | GOLD | UP | 30 sec | — | — | In play | — |
| 11/23 2:44:30 AM | EURUSD | UP | 30 sec | — | — | In play | — |
| 11/23 2:44:30 AM | USDCAD | DOWN | 30 sec | — | — | In play | — |
| 11/23 2:44:15 AM | USDMXN | DOWN | 44 sec | — | — | In play | — |
| 11/23 2:43:58 AM | 10YRRATE | UP | 61 sec | — | — | In play | — |
| 11/23 2:43:58 AM | PLATINUM | UP | 61 sec | — | — | In play | — |
| 11/23 2:43:42 AM | USDJPY | UP | 77 sec | — | — | In play | — |
| 11/23 2:43:26 AM | XRP | UP | 1.6 min | -0.170% | — | In play | — |
| 11/23 2:43:26 AM | 2YRRATE | UP | 1.6 min | — | — | In play | — |
| 11/23 2:43:10 AM | HYPE | UP | 1.8 min | -0.462% | — | In play | — |
| 11/23 2:42:53 AM | GBPUSD | UP | 2.1 min | — | — | In play | — |
| 11/23 2:42:37 AM | ZEC | UP | 2.4 min | -0.596% | — | In play | — |
| 11/23 2:42:21 AM | BTC | UP | 2.6 min | -0.202% | — | In play | — |
| 11/23 2:42:05 AM | NEAR | UP | 2.9 min | -0.500% | — | In play | — |
| 11/23 2:41:48 AM | SOL | UP | 3.2 min | -0.327% | — | In play | — |
| 11/23 2:41:32 AM | ETH | UP | 3.5 min | -0.272% | — | In play | — |
| 11/23 2:40:41 AM | BNB | UP | 4.3 min | -0.304% | — | In play | — |
| 11/23 2:39:54 AM | SILVER | UP | 5.1 min | — | — | In play | — |
| 11/23 2:39:54 AM | DOGE | UP | 5.1 min | -0.404% | — | In play | — |
| 11/23 2:39:03 AM | AUDUSD | UP | 6.0 min | — | — | In play | — |
| 11/23 2:29:48 AM | PLATINUM | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:29:48 AM | BTC | UP | 11 sec | -0.040% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 2:29:32 AM | GOLD | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:29:32 AM | EURUSD | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:29:32 AM | SOL | DOWN | 27 sec | +0.073% | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:29:32 AM | GBPUSD | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:29:32 AM | DOGE | UP | 27 sec | -0.063% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
