# 15-Minute 1¢ Study

*Updated Fri Oct 23, 1:57 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2445 finished bets | 1% | $87.55 | +32% | +3.58¢ | $48.95 / $38.60 |

*Expect about **98 buys a day** (~$14.64/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2251 | $59.00 | +24% |
| Volatility model ≥ 2%, hold to the close | 4517 | $6.65 | +1% |
| Momentum model ≥ 2%, hold to the close | 3760 | -$22.35 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 29368 | 29352 | 113 (0%) | 1.07% | -$1,998.50 (-56%) | Hold to the close: -$1,998.50 (-56%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 18673 | 4.7% | 0.4% (80) | -639% | ❌ Worse |
| Momentum model | 18673 | 4.6% | 0.4% (80) | -665% | ❌ Worse |
| Mean-reversion model | 18673 | 7.9% | 0.4% (80) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18673 | 80 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4517 | 40 | +1% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2445 | 26 | +32% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1392 | 17 | +72% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3760 | 30 | -5% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2251 | 22 | +24% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1485 | 15 | +39% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7485 | 53 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5242 | 44 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3492 | 31 | +1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18872 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7077 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3403 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 29352 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 113 | 0% | -$1,998.50 | -56% | — |
| Sell at 2¢ | 1091 | 4% | -$3,142.84 | -88% | 47 sec |
| Sell at 3¢ | 745 | 3% | -$3,135.95 | -88% | 48 sec |
| Sell at 5¢ | 524 | 2% | -$3,085.90 | -86% | 61 sec |
| Sell at 10¢ | 321 | 1% | -$2,977.99 | -83% | 64 sec |
| Sell at 25¢ | 179 | 1% | -$2,736.01 | -76% | 82 sec |
| Sell at 50¢ | 116 | 0% | -$2,461.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1241 | 7 | 11% | 4% | -46% | -80% | -82% |
| 2–5 min | 9428 | 52 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7467 | 28 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 11212 | 26 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2115 | 12 | 5% | 2% | -29% | -89% | -89% |
| BNB | 2109 | 12 | 5% | 3% | -30% | -83% | -82% |
| HYPE | 2105 | 8 | 5% | 3% | -53% | -88% | -87% |
| ETH | 2098 | 10 | 6% | 3% | -43% | -86% | -85% |
| SOL | 2097 | 4 | 4% | 2% | -76% | -92% | -92% |
| DOGE | 2093 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2088 | 8 | 3% | 1% | -53% | -88% | -88% |
| NEAR | 2085 | 12 | 6% | 3% | -25% | -80% | -80% |
| BTC | 2082 | 12 | 5% | 2% | -23% | -88% | -89% |
| GOLD | 1154 | 3 | 4% | 1% | -69% | -82% | -83% |
| SILVER | 1119 | 5 | 3% | 1% | -48% | -82% | -82% |
| WTI | 1091 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 976 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 957 | 4 | 1% | 1% | -61% | -68% | -68% |
| EURUSD | 904 | 3 | 2% | 1% | -69% | -86% | -86% |
| NATGAS | 898 | 5 | 2% | 1% | -48% | -86% | -86% |
| PALLADIUM | 867 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 850 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 826 | 5 | 1% | 1% | -44% | -99% | -98% |
| AUDUSD | 396 | 0 | 1% | 1% | -100% | -99% | -98% |
| USDCAD | 352 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 20 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 20 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 15 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 12 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14809 | 61 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 14543 | 52 | 4% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3126 | 16 | 2% | 1% | -14% | -79% | -78% |
| 0.05–0.1% | 3246 | 11 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4853 | 17 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5524 | 28 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2119 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7233 | 31 | 4% | 2% | -51% | -84% | -84% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,656 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 1:57:23 AM | GOLD | UP | 2.6 min | — | — | In play | — |
| 10/23 1:57:23 AM | BNB | UP | 2.6 min | -0.217% | — | In play | — |
| 10/23 1:56:51 AM | ZEC | UP | 3.1 min | -0.390% | — | In play | — |
| 10/23 1:56:51 AM | ETH | UP | 3.1 min | -0.214% | — | In play | — |
| 10/23 1:56:35 AM | WTI | DOWN | 3.4 min | — | — | In play | — |
| 10/23 1:56:35 AM | NEAR | UP | 3.4 min | -0.602% | — | In play | — |
| 10/23 1:56:35 AM | BTC | UP | 3.4 min | -0.160% | — | In play | — |
| 10/23 1:55:47 AM | SOL | UP | 4.2 min | -0.195% | — | In play | — |
| 10/23 1:44:55 AM | SOL | UP | 4 sec | -0.032% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:44:40 AM | USDCAD | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:44:24 AM | NEAR | DOWN | 36 sec | +0.022% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 1:44:24 AM | USDJPY | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:44:24 AM | BTC | UP | 36 sec | -0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 1:44:24 AM | 2YRRATE | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:43:36 AM | 10YRRATE | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:43:20 AM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 1:43:20 AM | WTI | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 1:43:20 AM | NATGAS | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:43:20 AM | 30YRRATE | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:43:04 AM | AUDUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:42:48 AM | EURUSD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:42:33 AM | DOGE | DOWN | 2.5 min | +0.148% | 6¢ | ❌ Lost | -$0.15 |
| 10/23 1:42:17 AM | SILVER | DOWN | 2.7 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 1:42:01 AM | PLATINUM | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:40:57 AM | ETH | DOWN | 4.0 min | +0.175% | 2¢ | ❌ Lost | -$0.15 |
| 10/23 1:40:08 AM | BNB | DOWN | 4.8 min | +0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 1:39:36 AM | HYPE | DOWN | 5.4 min | +0.330% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 1:39:36 AM | XRP | DOWN | 5.4 min | +0.212% | 3¢ | ❌ Lost | -$0.15 |
| 10/23 1:29:49 AM | 2YRRATE | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 1:29:33 AM | 5YRRATE | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
