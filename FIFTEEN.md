# 15-Minute 1¢ Study

*Updated Mon Oct 26, 11:38 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2757 finished bets | 1% | $79.25 | +25% | +2.87¢ | $30.50 / $48.75 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2566 | $52.35 | +18% |
| Volatility model ≥ 2%, hold to the close | 5134 | -$26.80 | -4% |
| Momentum model ≥ 2%, hold to the close | 4269 | -$38.10 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33136 | 33128 | 123 (0%) | 1.07% | -$2,307.00 (-57%) | Hold to the close: -$2,307.00 (-57%) |

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
| Volatility model | 21208 | 4.6% | 0.4% (85) | -662% | ❌ Worse |
| Momentum model | 21208 | 4.5% | 0.4% (85) | -687% | ❌ Worse |
| Mean-reversion model | 21208 | 7.9% | 0.4% (85) | -804% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21208 | 85 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5134 | 43 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2757 | 28 | +25% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1559 | 18 | +62% | -67% | -65% | -62% |
| Momentum model ≥ 2% | 4269 | 33 | -8% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2566 | 24 | +18% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1671 | 16 | +31% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8583 | 56 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6013 | 47 | -14% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4001 | 33 | -7% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21408 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7742 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3978 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33128 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 123 | 0% | -$2,307.00 | -57% | — |
| Sell at 2¢ | 1249 | 4% | -$3,536.26 | -88% | 47 sec |
| Sell at 3¢ | 854 | 3% | -$3,527.94 | -88% | 48 sec |
| Sell at 5¢ | 593 | 2% | -$3,475.55 | -86% | 62 sec |
| Sell at 10¢ | 367 | 1% | -$3,338.23 | -83% | 65 sec |
| Sell at 25¢ | 195 | 1% | -$3,089.55 | -77% | 83 sec |
| Sell at 50¢ | 126 | 0% | -$2,800.50 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1465 | 8 | 11% | 4% | -48% | -81% | -82% |
| 2–5 min | 10647 | 57 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8395 | 30 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 12617 | 28 | 1% | 0% | -68% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2399 | 12 | 5% | 3% | -36% | -88% | -88% |
| HYPE | 2391 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2388 | 13 | 5% | 3% | -32% | -84% | -83% |
| SOL | 2385 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2379 | 11 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2371 | 4 | 4% | 2% | -79% | -91% | -90% |
| XRP | 2368 | 9 | 3% | 1% | -53% | -89% | -89% |
| NEAR | 2367 | 12 | 5% | 2% | -34% | -82% | -82% |
| BTC | 2360 | 12 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1247 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1213 | 6 | 4% | 2% | -42% | -82% | -82% |
| WTI | 1190 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1060 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1033 | 4 | 1% | 1% | -64% | -71% | -70% |
| EURUSD | 994 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 986 | 5 | 2% | 1% | -53% | -87% | -86% |
| PALLADIUM | 950 | 2 | 1% | 0% | -80% | -88% | -89% |
| GBPUSD | 940 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 921 | 5 | 1% | 1% | -49% | -98% | -97% |
| AUDUSD | 483 | 1 | 1% | 1% | -81% | -98% | -97% |
| USDCAD | 445 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 63 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 55 | 0 | 2% | 0% | -100% | -97% | -95% |
| 2YRRATE | 49 | 1 | 4% | 0% | +90% | +98% | +96% |
| 30YRRATE | 49 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 42 | 1 | 2% | 2% | +122% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16772 | 68 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 16356 | 55 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3540 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3657 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5529 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6294 | 28 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2384 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8230 | 37 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,742 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 11:29:53 AM | PLATINUM | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:29:53 AM | GOLD | UP | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 11:29:53 AM | PALLADIUM | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:29:37 AM | 5YRRATE | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:29:21 AM | 30YRRATE | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:29:06 AM | 10YRRATE | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:29:06 AM | 2YRRATE | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:29:06 AM | BRENT | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:28:50 AM | WTI | UP | 69 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 11:28:50 AM | USDJPY | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:28:50 AM | SOL | UP | 69 sec | -0.165% | 0¢ | ❌ Lost | $0.00 |
| 10/26 11:27:26 AM | HYPE | UP | 2.6 min | -0.413% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:27:26 AM | BNB | UP | 2.6 min | -0.176% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:27:10 AM | XRP | UP | 2.8 min | -0.277% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 11:27:10 AM | BTC | UP | 2.8 min | -0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 11:27:10 AM | USDCAD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:27:10 AM | DOGE | UP | 2.8 min | -0.242% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 11:27:10 AM | ZEC | UP | 2.8 min | -0.643% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 11:26:55 AM | ETH | UP | 3.1 min | -0.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 11:26:55 AM | AUDUSD | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:26:55 AM | GBPUSD | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:26:22 AM | EURUSD | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:25:51 AM | NEAR | UP | 4.2 min | -1.008% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 11:14:51 AM | 30YRRATE | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:14:35 AM | NATGAS | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:13:49 AM | GBPUSD | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:13:33 AM | WTI | UP | 87 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 11:13:33 AM | USDCAD | UP | 87 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 11:13:33 AM | PALLADIUM | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:13:33 AM | BRENT | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
