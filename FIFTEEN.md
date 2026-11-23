# 15-Minute 1¢ Study

*Updated Sun Nov 22, 7:03 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4764 finished bets | 1% | $221.65 | +43% | +4.65¢ | $80.90 / $140.75 |

*Expect about **85 buys a day** (~$12.81/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4516 | $119.15 | +25% |
| Volatility model ≥ 2%, hold to the close | 8888 | $59.05 | +6% |
| Momentum model ≥ 2%, hold to the close | 7403 | -$16.85 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 64943 | 64909 | 251 (0%) | 1.07% | -$4,345.85 (-55%) | Hold to the close: -$4,345.85 (-55%) |

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
| Volatility model | 38875 | 4.5% | 0.4% (163) | -636% | ❌ Worse |
| Momentum model | 38875 | 4.4% | 0.4% (163) | -659% | ❌ Worse |
| Mean-reversion model | 38875 | 7.9% | 0.4% (163) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 38875 | 163 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8888 | 80 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4764 | 53 | +43% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2751 | 32 | +71% | -64% | -62% | -58% |
| Momentum model ≥ 2% | 7403 | 59 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4516 | 43 | +25% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2939 | 28 | +37% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 15827 | 111 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 11002 | 91 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7306 | 66 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39081 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15325 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10503 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 64909 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 251 | 0% | -$4,345.85 | -55% | — |
| Sell at 2¢ | 2645 | 4% | -$6,878.15 | -88% | 47 sec |
| Sell at 3¢ | 1782 | 3% | -$6,870.87 | -87% | 48 sec |
| Sell at 5¢ | 1214 | 2% | -$6,748.75 | -86% | 61 sec |
| Sell at 10¢ | 740 | 1% | -$6,484.45 | -83% | 65 sec |
| Sell at 25¢ | 398 | 1% | -$5,982.47 | -76% | 80 sec |
| Sell at 50¢ | 259 | 0% | -$5,383.60 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3361 | 17 | 10% | 4% | -52% | -82% | -83% |
| 2–5 min | 21044 | 112 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16208 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24283 | 65 | 1% | 0% | -61% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4369 | 19 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4363 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4361 | 20 | 4% | 2% | -41% | -86% | -86% |
| BNB | 4351 | 22 | 5% | 2% | -36% | -85% | -85% |
| DOGE | 4348 | 11 | 4% | 2% | -68% | -90% | -89% |
| ETH | 4344 | 19 | 7% | 3% | -45% | -82% | -82% |
| BTC | 4321 | 24 | 5% | 2% | -24% | -86% | -87% |
| NEAR | 4318 | 18 | 5% | 2% | -45% | -85% | -86% |
| XRP | 4306 | 16 | 3% | 2% | -53% | -89% | -88% |
| GOLD | 2272 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2261 | 7 | 4% | 1% | -62% | -92% | -92% |
| SILVER | 2217 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2019 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1975 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1906 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1901 | 6 | 2% | 1% | -71% | -77% | -77% |
| NATGAS | 1867 | 10 | 2% | 1% | -50% | -76% | -76% |
| USDJPY | 1865 | 6 | 2% | 1% | -70% | -96% | -96% |
| PALLADIUM | 1814 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1416 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1345 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 974 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 499 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 476 | 4 | 4% | 2% | -22% | -54% | -53% |
| 30YRRATE | 462 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 451 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33197 | 128 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31712 | 123 | 4% | 2% | -55% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5728 | 25 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 6265 | 26 | 3% | 2% | -34% | -91% | -90% |
| 0.1–0.2% | 9724 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12229 | 55 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5126 | 23 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15529 | 48 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 15984 | 71 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 17810 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,171 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/22 6:59:58 PM | WTI | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:59:58 PM | BRENT | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:59:42 PM | XRP | UP | 17 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:59:26 PM | NEAR | DOWN | 33 sec | -0.010% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:59:26 PM | USDJPY | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:59:10 PM | ZEC | UP | 50 sec | -0.235% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:59:10 PM | AUDUSD | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:58:54 PM | NATGAS | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:58:05 PM | GBPUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:57:49 PM | GOLD | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/22 6:57:33 PM | HYPE | UP | 2.4 min | -0.310% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 6:57:17 PM | ETH | UP | 2.7 min | -0.312% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 6:57:17 PM | SOL | UP | 2.7 min | -0.289% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:57:01 PM | BTC | UP | 3.0 min | -0.292% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 6:57:01 PM | PLATINUM | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:57:01 PM | PALLADIUM | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:56:30 PM | DOGE | UP | 3.5 min | -0.244% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 6:56:14 PM | COPPER | UP | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:55:58 PM | SILVER | UP | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/22 6:55:26 PM | BNB | UP | 4.6 min | -0.452% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:55:10 PM | EURUSD | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:44:53 PM | BNB | UP | 6 sec | -0.095% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:44:53 PM | BTC | UP | 6 sec | -0.044% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:44:53 PM | DOGE | DOWN | 6 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:44:53 PM | SOL | UP | 6 sec | -0.021% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:44:53 PM | BRENT | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:44:53 PM | NEAR | UP | 6 sec | -0.168% | 0¢ | ❌ Lost | $0.00 |
| 11/22 6:44:37 PM | ZEC | UP | 22 sec | -0.213% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:44:37 PM | AUDUSD | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 6:44:21 PM | ETH | UP | 39 sec | -0.101% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
