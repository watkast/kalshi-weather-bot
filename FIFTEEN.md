# 15-Minute 1¢ Study

*Updated Mon Oct 26, 9:55 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2756 finished bets | 1% | $79.25 | +25% | +2.88¢ | $30.50 / $48.75 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2563 | $52.65 | +19% |
| Volatility model ≥ 2%, hold to the close | 5124 | -$25.45 | -4% |
| Momentum model ≥ 2%, hold to the close | 4262 | -$37.20 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33000 | 32989 | 122 (0%) | 1.07% | -$2,302.55 (-57%) | Hold to the close: -$2,302.55 (-57%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 21145 | 4.6% | 0.4% (85) | -663% | ❌ Worse |
| Momentum model | 21145 | 4.5% | 0.4% (85) | -687% | ❌ Worse |
| Mean-reversion model | 21145 | 7.9% | 0.4% (85) | -805% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21145 | 85 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5124 | 43 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2756 | 28 | +25% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1559 | 18 | +62% | -67% | -65% | -62% |
| Momentum model ≥ 2% | 4262 | 33 | -7% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2563 | 24 | +19% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1670 | 16 | +31% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8553 | 56 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5989 | 47 | -14% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3985 | 33 | -7% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21345 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7707 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3937 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32989 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 122 | 0% | -$2,302.55 | -57% | — |
| Sell at 2¢ | 1241 | 4% | -$3,519.89 | -88% | 47 sec |
| Sell at 3¢ | 849 | 3% | -$3,511.44 | -88% | 48 sec |
| Sell at 5¢ | 591 | 2% | -$3,458.40 | -86% | 61 sec |
| Sell at 10¢ | 366 | 1% | -$3,321.09 | -83% | 65 sec |
| Sell at 25¢ | 195 | 1% | -$3,085.10 | -77% | 83 sec |
| Sell at 50¢ | 126 | 0% | -$2,796.05 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1459 | 8 | 11% | 4% | -48% | -81% | -82% |
| 2–5 min | 10586 | 56 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8363 | 30 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 12577 | 28 | 1% | 0% | -68% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2392 | 12 | 5% | 3% | -36% | -89% | -88% |
| HYPE | 2384 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2381 | 13 | 5% | 3% | -32% | -84% | -83% |
| SOL | 2378 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2372 | 11 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2364 | 4 | 4% | 2% | -79% | -91% | -90% |
| XRP | 2361 | 9 | 3% | 1% | -53% | -89% | -89% |
| NEAR | 2360 | 12 | 5% | 2% | -34% | -82% | -81% |
| BTC | 2353 | 12 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1242 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1210 | 6 | 4% | 2% | -42% | -82% | -81% |
| WTI | 1185 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1056 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1029 | 4 | 1% | 1% | -64% | -70% | -70% |
| EURUSD | 988 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 981 | 5 | 2% | 1% | -52% | -87% | -86% |
| PALLADIUM | 945 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 935 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 915 | 5 | 1% | 1% | -49% | -98% | -97% |
| AUDUSD | 477 | 1 | 1% | 1% | -80% | -98% | -97% |
| USDCAD | 440 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 59 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 52 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 47 | 1 | 4% | 0% | +99% | +106% | +104% |
| 30YRRATE | 45 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 38 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16686 | 67 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16303 | 55 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3540 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3655 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5511 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6261 | 28 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2374 | 10 | 7% | 3% | -56% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8091 | 36 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,753 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 9:55:00 AM | SOL | UP | 5.0 min | -0.341% | — | In play | — |
| 10/26 9:55:00 AM | ETH | UP | 5.0 min | -0.355% | — | In play | — |
| 10/26 9:55:00 AM | NEAR | UP | 5.0 min | -1.080% | — | In play | — |
| 10/26 9:44:52 AM | COPPER | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:44:52 AM | WTI | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:44:52 AM | USDCAD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:44:36 AM | BNB | DOWN | 23 sec | +0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/26 9:44:36 AM | PALLADIUM | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:44:36 AM | SOL | DOWN | 23 sec | +0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/26 9:44:36 AM | NEAR | DOWN | 23 sec | -0.024% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 9:44:20 AM | DOGE | DOWN | 39 sec | +0.062% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:44:04 AM | 30YRRATE | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:43:32 AM | ZEC | DOWN | 88 sec | +0.295% | 0¢ | ❌ Lost | $0.00 |
| 10/26 9:43:32 AM | BTC | DOWN | 88 sec | +0.164% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:43:32 AM | XRP | DOWN | 88 sec | +0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 9:43:32 AM | ETH | DOWN | 88 sec | +0.167% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:42:59 AM | 2YRRATE | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:42:59 AM | 10YRRATE | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:42:59 AM | 5YRRATE | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:42:44 AM | NATGAS | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:42:28 AM | HYPE | DOWN | 2.5 min | +0.269% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 9:29:51 AM | AUDUSD | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:29:51 AM | PALLADIUM | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:29:51 AM | COPPER | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:29:51 AM | SILVER | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 9:29:51 AM | USDCAD | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:29:51 AM | NEAR | UP | 9 sec | -0.260% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:29:19 AM | ZEC | UP | 41 sec | -0.262% | 0¢ | ❌ Lost | $0.00 |
| 10/26 9:29:19 AM | XRP | DOWN | 41 sec | +0.092% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:29:19 AM | GBPUSD | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
