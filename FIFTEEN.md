# 15-Minute 1¢ Study

*Updated Mon Nov 23, 2:55 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4805 finished bets | 1% | $217.45 | +41% | +4.53¢ | $78.20 / $139.25 |

*Expect about **85 buys a day** (~$12.73/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4556 | $114.95 | +24% |
| Volatility model ≥ 2%, hold to the close | 8948 | $52.30 | +5% |
| Momentum model ≥ 2%, hold to the close | 7459 | -$23.00 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 65756 | 65721 | 253 (0%) | 1.07% | -$4,415.80 (-55%) | Hold to the close: -$4,415.80 (-55%) |

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
| Volatility model | 39232 | 4.5% | 0.4% (164) | -639% | ❌ Worse |
| Momentum model | 39232 | 4.4% | 0.4% (164) | -663% | ❌ Worse |
| Mean-reversion model | 39232 | 7.9% | 0.4% (164) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39232 | 164 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 8948 | 80 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4805 | 53 | +41% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2780 | 32 | +70% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7459 | 59 | -3% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4556 | 43 | +24% | -75% | -74% | -71% |
| Momentum model ≥ 10% | 2968 | 28 | +36% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15965 | 112 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 11107 | 92 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7382 | 66 | +2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39438 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15552 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10731 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 65721 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 253 | 0% | -$4,415.80 | -55% | — |
| Sell at 2¢ | 2692 | 4% | -$6,963.88 | -88% | 47 sec |
| Sell at 3¢ | 1814 | 3% | -$6,956.34 | -87% | 48 sec |
| Sell at 5¢ | 1238 | 2% | -$6,831.10 | -86% | 62 sec |
| Sell at 10¢ | 759 | 1% | -$6,557.51 | -82% | 65 sec |
| Sell at 25¢ | 408 | 1% | -$6,047.32 | -76% | 79 sec |
| Sell at 50¢ | 261 | 0% | -$5,454.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3402 | 17 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 21290 | 114 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16422 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24594 | 65 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4409 | 19 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4403 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4400 | 20 | 4% | 2% | -41% | -86% | -86% |
| BNB | 4392 | 22 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 4388 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4383 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4361 | 24 | 6% | 2% | -25% | -86% | -87% |
| NEAR | 4357 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4345 | 16 | 4% | 2% | -53% | -89% | -88% |
| GOLD | 2306 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2289 | 8 | 4% | 2% | -57% | -91% | -92% |
| SILVER | 2250 | 9 | 5% | 2% | -52% | -83% | -84% |
| PLATINUM | 2046 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 2002 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1936 | 8 | 2% | 1% | -61% | -96% | -96% |
| COPPER | 1933 | 6 | 2% | 1% | -71% | -77% | -77% |
| NATGAS | 1894 | 10 | 2% | 1% | -51% | -77% | -76% |
| USDJPY | 1894 | 6 | 2% | 1% | -70% | -97% | -96% |
| PALLADIUM | 1837 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1449 | 6 | 2% | 1% | -61% | -90% | -90% |
| USDCAD | 1373 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 997 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 519 | 2 | 3% | 1% | -64% | -77% | -75% |
| 2YRRATE | 493 | 4 | 4% | 2% | -24% | -56% | -55% |
| 30YRRATE | 479 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 470 | 2 | 3% | 1% | -60% | -94% | -96% |
| INX | 112 | 1 | 2% | 1% | -17% | -97% | -98% |
| USDMXN | 4 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33633 | 130 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 32088 | 123 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5770 | 25 | 2% | 1% | -21% | -78% | -78% |
| 0.05–0.1% | 6308 | 26 | 3% | 2% | -34% | -91% | -90% |
| 0.1–0.2% | 9816 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12369 | 56 | 7% | 3% | -48% | -86% | -86% |
| Over 0.5% | 5166 | 23 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15988 | 49 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16135 | 72 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 18012 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,134 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/23 2:55:08 PM | ZEC | UP | 4.8 min | -1.099% | — | In play | — |
| 11/23 2:44:59 PM | NATGAS | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:44:59 PM | PALLADIUM | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:44:59 PM | EURUSD | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:44:59 PM | BRENT | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:44:26 PM | WTI | DOWN | 34 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:44:26 PM | USDJPY | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:44:26 PM | COPPER | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:44:10 PM | XRP | UP | 50 sec | -0.149% | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:44:10 PM | GBPUSD | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:43:55 PM | BNB | UP | 64 sec | -0.197% | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:43:55 PM | SILVER | UP | 64 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 2:43:55 PM | GOLD | UP | 64 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:43:55 PM | HYPE | UP | 64 sec | -0.267% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:43:55 PM | AUDUSD | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:43:38 PM | DOGE | UP | 82 sec | -0.261% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:43:38 PM | SOL | UP | 82 sec | -0.289% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:43:22 PM | BTC | UP | 1.6 min | -0.189% | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:43:22 PM | NEAR | UP | 1.6 min | -0.460% | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:43:06 PM | ETH | UP | 1.9 min | -0.190% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 2:42:34 PM | USDCAD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:42:02 PM | ZEC | UP | 3.0 min | -0.563% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:41:47 PM | PLATINUM | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:39:23 PM | 10YRRATE | DOWN | 5.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:39:23 PM | 2YRRATE | DOWN | 5.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:39:23 PM | 30YRRATE | DOWN | 5.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:39:07 PM | 5YRRATE | DOWN | 5.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:29:54 PM | ETH | UP | 6 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:29:38 PM | WTI | DOWN | 22 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:29:38 PM | 10YRRATE | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
