# 15-Minute 1¢ Study

*Updated Wed Oct 21, 12:25 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2279 finished bets | 1% | $78.30 | +30% | +3.44¢ | $44.55 / $33.75 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2109 | $59.55 | +25% |
| Volatility model ≥ 2%, hold to the close | 4177 | -$8.10 | -2% |
| Momentum model ≥ 2%, hold to the close | 3526 | -$38.10 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26954 | 26946 | 99 (0%) | 1.07% | -$1,898.70 (-58%) | Hold to the close: -$1,898.70 (-58%) |

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
| Volatility model | 17434 | 4.6% | 0.4% (71) | -657% | ❌ Worse |
| Momentum model | 17434 | 4.6% | 0.4% (71) | -680% | ❌ Worse |
| Mean-reversion model | 17434 | 7.8% | 0.4% (71) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17434 | 71 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4177 | 36 | -2% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2279 | 24 | +30% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1304 | 16 | +72% | -61% | -60% | -57% |
| Momentum model ≥ 2% | 3526 | 27 | -9% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2109 | 21 | +25% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1386 | 14 | +38% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 6912 | 47 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4826 | 39 | -11% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3213 | 27 | -4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17632 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6432 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2882 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26946 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 99 | 0% | -$1,898.70 | -58% | — |
| Sell at 2¢ | 981 | 4% | -$2,889.64 | -88% | 46 sec |
| Sell at 3¢ | 668 | 2% | -$2,884.18 | -88% | 48 sec |
| Sell at 5¢ | 472 | 2% | -$2,837.90 | -86% | 56 sec |
| Sell at 10¢ | 288 | 1% | -$2,739.42 | -83% | 64 sec |
| Sell at 25¢ | 159 | 1% | -$2,534.41 | -77% | 81 sec |
| Sell at 50¢ | 102 | 0% | -$2,302.20 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1083 | 6 | 11% | 4% | -47% | -81% | -83% |
| 2–5 min | 8689 | 45 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 6883 | 25 | 3% | 1% | -61% | -93% | -92% |
| Under 1 min | 10287 | 23 | 1% | 0% | -68% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1978 | 11 | 4% | 2% | -31% | -90% | -90% |
| BNB | 1971 | 11 | 5% | 2% | -32% | -83% | -82% |
| HYPE | 1970 | 7 | 5% | 3% | -56% | -89% | -87% |
| ETH | 1958 | 10 | 6% | 3% | -39% | -87% | -86% |
| DOGE | 1958 | 3 | 4% | 2% | -81% | -90% | -90% |
| SOL | 1957 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1950 | 7 | 3% | 1% | -56% | -88% | -88% |
| NEAR | 1945 | 11 | 6% | 3% | -27% | -79% | -79% |
| BTC | 1945 | 11 | 5% | 2% | -24% | -88% | -90% |
| GOLD | 1052 | 2 | 3% | 1% | -78% | -81% | -84% |
| SILVER | 1015 | 4 | 3% | 1% | -55% | -82% | -82% |
| WTI | 993 | 3 | 3% | 1% | -64% | -94% | -95% |
| PLATINUM | 884 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 877 | 3 | 1% | 1% | -68% | -76% | -76% |
| NATGAS | 813 | 5 | 2% | 1% | -43% | -85% | -84% |
| EURUSD | 807 | 3 | 2% | 1% | -65% | -84% | -84% |
| PALLADIUM | 798 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 756 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 720 | 3 | 1% | 1% | -61% | -99% | -98% |
| AUDUSD | 319 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 277 | 0 | 0% | 0% | -100% | -99% | -99% |
| 2YRRATE | 2 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13525 | 49 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13421 | 50 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2948 | 15 | 2% | 1% | -15% | -78% | -77% |
| 0.05–0.1% | 3051 | 11 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 4488 | 15 | 5% | 2% | -59% | -89% | -89% |
| 0.2–0.5% | 5146 | 25 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 1996 | 7 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6175 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,728 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 12:25:19 PM | HYPE | DOWN | 4.7 min | +0.487% | — | In play | — |
| 10/21 12:14:52 PM | NEAR | DOWN | 7 sec | +0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:14:36 PM | 2YRRATE | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:14:36 PM | SOL | DOWN | 23 sec | +0.096% | 0¢ | ❌ Lost | $0.00 |
| 10/21 12:14:36 PM | GBPUSD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:14:36 PM | BTC | DOWN | 23 sec | +0.043% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:14:36 PM | ETH | DOWN | 23 sec | +0.067% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:14:20 PM | EURUSD | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:14:04 PM | GOLD | DOWN | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:14:04 PM | USDCAD | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:13:47 PM | DOGE | DOWN | 72 sec | +0.113% | 1¢ | ❌ Lost | $0.00 |
| 10/21 12:13:31 PM | COPPER | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:13:15 PM | WTI | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:13:15 PM | HYPE | DOWN | 1.7 min | +0.136% | 5¢ | ❌ Lost | -$0.15 |
| 10/21 12:13:15 PM | PALLADIUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:12:43 PM | XRP | DOWN | 2.3 min | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:12:27 PM | ZEC | UP | 2.5 min | -0.580% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:11:55 PM | BNB | UP | 3.1 min | -0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:10:17 PM | SILVER | DOWN | 4.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 11:59:49 AM | AUDUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 11:59:49 AM | USDCAD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 11:59:33 AM | NEAR | UP | 26 sec | -0.224% | 0¢ | ❌ Lost | $0.00 |
| 10/21 11:59:33 AM | ZEC | UP | 26 sec | -0.216% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 11:59:01 AM | SOL | DOWN | 59 sec | +0.066% | 2¢ | ❌ Lost | $0.00 |
| 10/21 11:59:01 AM | DOGE | DOWN | 59 sec | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 11:58:12 AM | BNB | DOWN | 1.8 min | +0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 11:57:56 AM | WTI | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 11:57:24 AM | BTC | DOWN | 2.6 min | +0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 11:56:03 AM | HYPE | DOWN | 3.9 min | +0.273% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 11:56:03 AM | XRP | DOWN | 3.9 min | +0.267% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
