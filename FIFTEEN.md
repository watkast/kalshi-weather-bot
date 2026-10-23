# 15-Minute 1¢ Study

*Updated Fri Oct 23, 11:28 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2474 finished bets | 1% | $84.10 | +30% | +3.40¢ | $46.85 / $37.25 |

*Expect about **97 buys a day** (~$14.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2290 | $54.65 | +22% |
| Volatility model ≥ 2%, hold to the close | 4589 | -$2.35 | -0% |
| Momentum model ≥ 2%, hold to the close | 3828 | -$30.15 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30035 | 30016 | 114 (0%) | 1.07% | -$2,068.95 (-56%) | Hold to the close: -$2,068.95 (-56%) |

*In play or awaiting result: 18. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 18991 | 4.6% | 0.4% (80) | -643% | ❌ Worse |
| Momentum model | 18991 | 4.6% | 0.4% (80) | -669% | ❌ Worse |
| Mean-reversion model | 18991 | 7.9% | 0.4% (80) | -776% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18991 | 80 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4589 | 40 | -0% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2474 | 26 | +30% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1408 | 17 | +70% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3828 | 30 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2290 | 22 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1503 | 15 | +37% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7633 | 53 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5335 | 44 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3548 | 31 | -1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19191 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7252 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3573 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30016 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 114 | 0% | -$2,068.95 | -56% | — |
| Sell at 2¢ | 1123 | 4% | -$3,218.97 | -88% | 47 sec |
| Sell at 3¢ | 768 | 3% | -$3,211.43 | -88% | 48 sec |
| Sell at 5¢ | 538 | 2% | -$3,161.25 | -86% | 61 sec |
| Sell at 10¢ | 328 | 1% | -$3,039.27 | -83% | 64 sec |
| Sell at 25¢ | 182 | 1% | -$2,796.53 | -76% | 82 sec |
| Sell at 50¢ | 116 | 0% | -$2,531.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1268 | 7 | 11% | 4% | -47% | -80% | -82% |
| 2–5 min | 9637 | 52 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 7656 | 28 | 3% | 2% | -60% | -93% | -93% |
| Under 1 min | 11451 | 27 | 1% | 0% | -66% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2151 | 12 | 5% | 2% | -30% | -89% | -89% |
| BNB | 2144 | 12 | 5% | 3% | -31% | -83% | -82% |
| HYPE | 2141 | 8 | 5% | 3% | -54% | -88% | -87% |
| ETH | 2133 | 10 | 6% | 3% | -44% | -86% | -85% |
| SOL | 2133 | 4 | 4% | 2% | -77% | -92% | -92% |
| DOGE | 2129 | 4 | 4% | 2% | -77% | -90% | -89% |
| XRP | 2123 | 8 | 3% | 1% | -54% | -88% | -88% |
| NEAR | 2119 | 12 | 6% | 3% | -26% | -81% | -80% |
| BTC | 2118 | 12 | 5% | 2% | -24% | -88% | -89% |
| GOLD | 1178 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1145 | 5 | 4% | 1% | -49% | -82% | -82% |
| WTI | 1113 | 3 | 3% | 1% | -68% | -94% | -95% |
| PLATINUM | 1001 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 980 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 927 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 919 | 5 | 2% | 1% | -49% | -86% | -86% |
| PALLADIUM | 892 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 872 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 855 | 5 | 1% | 1% | -45% | -98% | -97% |
| AUDUSD | 421 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 374 | 0 | 1% | 0% | -100% | -98% | -99% |
| 2YRRATE | 36 | 0 | 3% | 0% | -100% | -95% | -100% |
| 10YRRATE | 34 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 31 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 23 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15136 | 62 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 14880 | 52 | 4% | 2% | -60% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3157 | 16 | 2% | 1% | -15% | -79% | -78% |
| 0.05–0.1% | 3288 | 11 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4951 | 17 | 5% | 2% | -58% | -89% | -89% |
| 0.2–0.5% | 5632 | 28 | 6% | 3% | -45% | -87% | -86% |
| Over 0.5% | 2159 | 10 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7532 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7367 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,596 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 11:28:33 AM | NEAR | UP | 86 sec | -0.426% | — | In play | — |
| 10/23 11:28:17 AM | USDJPY | UP | 1.7 min | — | — | In play | — |
| 10/23 11:28:17 AM | WTI | DOWN | 1.7 min | — | — | In play | — |
| 10/23 11:28:01 AM | ZEC | UP | 2.0 min | -0.459% | — | In play | — |
| 10/23 11:27:11 AM | ETH | UP | 2.8 min | -0.208% | — | In play | — |
| 10/23 11:26:56 AM | SOL | UP | 3.0 min | -0.227% | — | In play | — |
| 10/23 11:26:56 AM | XRP | UP | 3.0 min | -0.267% | — | In play | — |
| 10/23 11:26:38 AM | BNB | UP | 3.4 min | -0.205% | — | In play | — |
| 10/23 11:26:06 AM | BTC | UP | 3.9 min | -0.188% | — | In play | — |
| 10/23 11:25:51 AM | DOGE | UP | 4.1 min | -0.234% | — | In play | — |
| 10/23 11:24:47 AM | HYPE | UP | 5.2 min | -0.435% | — | In play | — |
| 10/23 11:14:36 AM | SILVER | UP | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 11:14:20 AM | DOGE | DOWN | 40 sec | +0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/23 11:14:20 AM | HYPE | DOWN | 40 sec | +0.074% | 0¢ | ❌ Lost | $0.00 |
| 10/23 11:14:20 AM | USDCAD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 11:14:20 AM | SOL | DOWN | 40 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/23 11:14:05 AM | 2YRRATE | UP | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 11:14:05 AM | USDJPY | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 11:13:49 AM | PLATINUM | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 11:13:49 AM | AUDUSD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 11:13:49 AM | GOLD | UP | 70 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 11:13:17 AM | GBPUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 11:13:01 AM | BNB | DOWN | 2.0 min | +0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 11:12:47 AM | NEAR | DOWN | 2.2 min | +0.475% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 11:12:47 AM | BTC | DOWN | 2.2 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 11:12:31 AM | ETH | DOWN | 2.5 min | +0.221% | 0¢ | ❌ Lost | $0.00 |
| 10/23 11:12:31 AM | XRP | DOWN | 2.5 min | +0.237% | 0¢ | ❌ Lost | $0.00 |
| 10/23 11:12:31 AM | ZEC | DOWN | 2.5 min | +0.559% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 11:12:15 AM | COPPER | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 11:10:24 AM | PALLADIUM | UP | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
