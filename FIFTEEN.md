# 15-Minute 1¢ Study

*Updated Fri Oct 23, 11:08 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2473 finished bets | 1% | $84.25 | +30% | +3.41¢ | $47.00 / $37.25 |

*Expect about **97 buys a day** (~$14.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2289 | $54.80 | +22% |
| Volatility model ≥ 2%, hold to the close | 4586 | -$1.90 | -0% |
| Momentum model ≥ 2%, hold to the close | 3825 | -$29.85 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30005 | 29997 | 114 (0%) | 1.07% | -$2,067.00 (-56%) | Hold to the close: -$2,067.00 (-56%) |

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
| Volatility model | 18982 | 4.6% | 0.4% (80) | -643% | ❌ Worse |
| Momentum model | 18982 | 4.6% | 0.4% (80) | -669% | ❌ Worse |
| Mean-reversion model | 18982 | 7.9% | 0.4% (80) | -776% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18982 | 80 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4586 | 40 | -0% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2473 | 26 | +30% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1407 | 17 | +70% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3825 | 30 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2289 | 22 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1503 | 15 | +37% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7629 | 53 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5333 | 44 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3547 | 31 | -1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19182 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7247 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3568 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 29997 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 114 | 0% | -$2,067.00 | -56% | — |
| Sell at 2¢ | 1123 | 4% | -$3,217.02 | -88% | 47 sec |
| Sell at 3¢ | 768 | 3% | -$3,209.48 | -88% | 48 sec |
| Sell at 5¢ | 538 | 2% | -$3,159.30 | -86% | 61 sec |
| Sell at 10¢ | 328 | 1% | -$3,037.32 | -83% | 64 sec |
| Sell at 25¢ | 182 | 1% | -$2,794.58 | -76% | 82 sec |
| Sell at 50¢ | 116 | 0% | -$2,530.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1268 | 7 | 11% | 4% | -47% | -80% | -82% |
| 2–5 min | 9630 | 52 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 7651 | 28 | 3% | 2% | -60% | -93% | -93% |
| Under 1 min | 11444 | 27 | 1% | 0% | -66% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2150 | 12 | 5% | 2% | -30% | -89% | -89% |
| BNB | 2143 | 12 | 5% | 3% | -31% | -83% | -82% |
| HYPE | 2140 | 8 | 5% | 3% | -54% | -88% | -87% |
| ETH | 2132 | 10 | 6% | 3% | -44% | -86% | -85% |
| SOL | 2132 | 4 | 4% | 2% | -77% | -92% | -92% |
| DOGE | 2128 | 4 | 4% | 2% | -77% | -90% | -89% |
| XRP | 2122 | 8 | 3% | 1% | -54% | -88% | -88% |
| NEAR | 2118 | 12 | 6% | 3% | -26% | -81% | -80% |
| BTC | 2117 | 12 | 5% | 2% | -24% | -88% | -89% |
| GOLD | 1177 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1144 | 5 | 4% | 1% | -49% | -82% | -82% |
| WTI | 1113 | 3 | 3% | 1% | -68% | -94% | -95% |
| PLATINUM | 1000 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 979 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 927 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 919 | 5 | 2% | 1% | -49% | -86% | -86% |
| PALLADIUM | 891 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 871 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 854 | 5 | 1% | 1% | -45% | -98% | -97% |
| AUDUSD | 420 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 373 | 0 | 1% | 0% | -100% | -98% | -99% |
| 2YRRATE | 35 | 0 | 3% | 0% | -100% | -95% | -100% |
| 10YRRATE | 34 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 31 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 23 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15127 | 62 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 14870 | 52 | 4% | 2% | -60% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3156 | 16 | 2% | 1% | -15% | -79% | -78% |
| 0.05–0.1% | 3285 | 11 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4950 | 17 | 5% | 2% | -58% | -89% | -89% |
| 0.2–0.5% | 5629 | 28 | 6% | 3% | -45% | -87% | -86% |
| Over 0.5% | 2158 | 10 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7532 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7348 | 34 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,601 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 10:59:53 AM | WTI | DOWN | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 10:59:53 AM | HYPE | UP | 7 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:59:53 AM | NATGAS | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:59:53 AM | GOLD | UP | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 10:59:37 AM | NEAR | UP | 23 sec | -0.188% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:59:06 AM | PLATINUM | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:59:06 AM | ZEC | UP | 54 sec | -0.292% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:58:49 AM | BTC | UP | 70 sec | -0.077% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:58:49 AM | AUDUSD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:58:33 AM | PALLADIUM | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:58:17 AM | DOGE | UP | 1.7 min | -0.184% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:58:01 AM | SOL | UP | 2.0 min | -0.173% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:57:45 AM | ETH | UP | 2.2 min | -0.142% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:57:45 AM | COPPER | UP | 2.2 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/23 10:57:29 AM | GBPUSD | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:57:29 AM | BNB | UP | 2.5 min | -0.165% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:57:29 AM | EURUSD | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:57:29 AM | XRP | UP | 2.5 min | -0.244% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:57:29 AM | SILVER | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:56:26 AM | USDCAD | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:44:59 AM | 5YRRATE | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:44:59 AM | EURUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:44:59 AM | GOLD | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 10:44:43 AM | 2YRRATE | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:44:43 AM | PALLADIUM | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:43:39 AM | AUDUSD | DOWN | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:43:39 AM | SILVER | DOWN | 81 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:43:23 AM | USDJPY | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 10:43:23 AM | WTI | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:43:07 AM | GBPUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
