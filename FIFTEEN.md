# 15-Minute 1¢ Study

*Updated Tue Oct 27, 7:46 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2899 finished bets | 1% | $93.15 | +28% | +3.21¢ | $91.35 / $1.80 |

*Expect about **97 buys a day** (~$14.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2705 | $52.70 | +18% |
| Volatility model ≥ 2%, hold to the close | 5391 | $27.65 | +4% |
| Momentum model ≥ 2%, hold to the close | 4466 | -$44.50 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 35478 | 35464 | 137 (0%) | 1.07% | -$2,404.40 (-56%) | Hold to the close: -$2,404.40 (-56%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 22322 | 4.7% | 0.4% (92) | -658% | ❌ Worse |
| Momentum model | 22322 | 4.6% | 0.4% (92) | -683% | ❌ Worse |
| Mean-reversion model | 22322 | 8.0% | 0.4% (92) | -799% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22322 | 92 | -48% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5391 | 49 | +4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2899 | 30 | +28% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1647 | 19 | +63% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4466 | 34 | -9% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2705 | 25 | +18% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1772 | 17 | +32% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 9074 | 63 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6361 | 53 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4245 | 38 | +1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22522 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 8398 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4544 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 35464 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 137 | 0% | -$2,404.40 | -56% | — |
| Sell at 2¢ | 1350 | 4% | -$3,775.40 | -87% | 47 sec |
| Sell at 3¢ | 925 | 3% | -$3,765.65 | -87% | 48 sec |
| Sell at 5¢ | 643 | 2% | -$3,708.45 | -86% | 63 sec |
| Sell at 10¢ | 394 | 1% | -$3,554.26 | -82% | 65 sec |
| Sell at 25¢ | 213 | 1% | -$3,267.37 | -76% | 88 sec |
| Sell at 50¢ | 141 | 0% | -$2,936.65 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1587 | 8 | 11% | 4% | -52% | -81% | -82% |
| 2–5 min | 11352 | 65 | 7% | 3% | -44% | -87% | -86% |
| 1–2 min | 8983 | 32 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13538 | 32 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2522 | 12 | 5% | 2% | -39% | -89% | -88% |
| HYPE | 2514 | 8 | 5% | 3% | -61% | -89% | -87% |
| BNB | 2513 | 15 | 5% | 2% | -25% | -84% | -83% |
| SOL | 2509 | 7 | 4% | 2% | -65% | -92% | -92% |
| ETH | 2502 | 11 | 6% | 3% | -47% | -86% | -85% |
| DOGE | 2500 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2490 | 11 | 3% | 1% | -46% | -89% | -89% |
| NEAR | 2489 | 12 | 5% | 2% | -37% | -82% | -82% |
| BTC | 2483 | 13 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1334 | 5 | 4% | 2% | -55% | -81% | -83% |
| SILVER | 1300 | 6 | 4% | 2% | -46% | -82% | -82% |
| WTI | 1286 | 4 | 3% | 1% | -63% | -93% | -94% |
| PLATINUM | 1155 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1103 | 4 | 1% | 1% | -66% | -72% | -72% |
| EURUSD | 1078 | 3 | 2% | 1% | -74% | -87% | -87% |
| NATGAS | 1062 | 6 | 2% | 1% | -47% | -79% | -79% |
| PALLADIUM | 1020 | 2 | 1% | 0% | -82% | -89% | -89% |
| GBPUSD | 1016 | 2 | 2% | 1% | -82% | -96% | -96% |
| USDJPY | 1004 | 5 | 2% | 1% | -54% | -97% | -96% |
| AUDUSD | 558 | 3 | 1% | 1% | -50% | -81% | -80% |
| USDCAD | 518 | 0 | 1% | 0% | -100% | -98% | -98% |
| BRENT | 138 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 101 | 0 | 4% | 0% | -100% | -93% | -92% |
| 30YRRATE | 92 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 89 | 1 | 3% | 1% | +5% | +11% | +11% |
| 5YRRATE | 88 | 1 | 5% | 2% | +6% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17926 | 76 | 4% | 2% | -51% | -87% | -86% |
| DOWN (bought NO) | 17538 | 61 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3699 | 19 | 2% | 1% | -12% | -81% | -80% |
| 0.05–0.1% | 3866 | 14 | 3% | 2% | -46% | -92% | -91% |
| 0.1–0.2% | 5855 | 22 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 6632 | 29 | 7% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2466 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9520 | 32 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,644 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 7:44:48 PM | USDCAD | DOWN | 11 sec | — | 0¢ | In play | — |
| 10/27 7:44:32 PM | PLATINUM | UP | 27 sec | — | 0¢ | In play | — |
| 10/27 7:44:32 PM | GBPUSD | UP | 27 sec | — | 0¢ | In play | — |
| 10/27 7:44:32 PM | EURUSD | UP | 27 sec | — | 0¢ | In play | — |
| 10/27 7:44:32 PM | PALLADIUM | UP | 27 sec | — | 0¢ | In play | — |
| 10/27 7:44:16 PM | HYPE | UP | 43 sec | -0.103% | 1¢ | In play | — |
| 10/27 7:44:00 PM | GOLD | UP | 59 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 7:42:25 PM | AUDUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:42:09 PM | USDJPY | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:41:22 PM | ZEC | DOWN | 3.6 min | +0.420% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:41:06 PM | DOGE | DOWN | 3.9 min | +0.289% | 3¢ | ❌ Lost | -$0.15 |
| 10/27 7:41:06 PM | BTC | DOWN | 3.9 min | +0.220% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:40:18 PM | SILVER | UP | 4.7 min | — | 15¢ | ❌ Lost | -$0.15 |
| 10/27 7:40:02 PM | SOL | DOWN | 5.0 min | +0.272% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:39:31 PM | XRP | DOWN | 5.5 min | +0.346% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:39:31 PM | BNB | DOWN | 5.5 min | +0.222% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:38:59 PM | ETH | DOWN | 6.0 min | +0.288% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:38:27 PM | NEAR | DOWN | 6.5 min | +0.548% | 0¢ | ❌ Lost | $0.00 |
| 10/27 7:29:50 PM | EURUSD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:29:50 PM | BRENT | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:29:50 PM | COPPER | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:29:34 PM | USDJPY | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:29:18 PM | GBPUSD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:27:59 PM | PALLADIUM | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:27:10 PM | SILVER | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:26:40 PM | HYPE | DOWN | 3.3 min | +0.327% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:25:51 PM | PLATINUM | DOWN | 4.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 7:25:51 PM | BTC | DOWN | 4.1 min | +0.242% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:24:52 PM | ZEC | DOWN | 5.1 min | +0.709% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 7:24:37 PM | DOGE | DOWN | 5.4 min | +0.328% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
