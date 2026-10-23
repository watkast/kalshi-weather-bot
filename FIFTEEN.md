# 15-Minute 1¢ Study

*Updated Fri Oct 23, 12:53 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2441 finished bets | 1% | $88.00 | +32% | +3.61¢ | $49.25 / $38.75 |

*Expect about **98 buys a day** (~$14.64/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2246 | $59.60 | +24% |
| Volatility model ≥ 2%, hold to the close | 4509 | $7.70 | +1% |
| Momentum model ≥ 2%, hold to the close | 3753 | -$21.45 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 29305 | 29297 | 112 (0%) | 1.07% | -$2,004.70 (-56%) | Hold to the close: -$2,004.70 (-56%) |

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
| Volatility model | 18648 | 4.7% | 0.4% (80) | -640% | ❌ Worse |
| Momentum model | 18648 | 4.6% | 0.4% (80) | -665% | ❌ Worse |
| Mean-reversion model | 18648 | 7.9% | 0.4% (80) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18648 | 80 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4509 | 40 | +1% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2441 | 26 | +32% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1389 | 17 | +72% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3753 | 30 | -5% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2246 | 22 | +24% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1483 | 15 | +39% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7474 | 53 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5235 | 44 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3488 | 31 | +1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18847 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7064 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3386 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 29297 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 112 | 0% | -$2,004.70 | -56% | — |
| Sell at 2¢ | 1089 | 4% | -$3,149.56 | -88% | 47 sec |
| Sell at 3¢ | 743 | 3% | -$3,142.93 | -88% | 48 sec |
| Sell at 5¢ | 523 | 2% | -$3,092.75 | -87% | 61 sec |
| Sell at 10¢ | 321 | 1% | -$2,984.19 | -84% | 64 sec |
| Sell at 25¢ | 179 | 1% | -$2,742.21 | -77% | 82 sec |
| Sell at 50¢ | 116 | 0% | -$2,467.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1239 | 7 | 11% | 4% | -46% | -80% | -83% |
| 2–5 min | 9413 | 52 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7447 | 28 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 11194 | 25 | 1% | 0% | -68% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2113 | 12 | 5% | 2% | -29% | -89% | -89% |
| BNB | 2106 | 12 | 5% | 3% | -30% | -83% | -82% |
| HYPE | 2103 | 8 | 5% | 3% | -53% | -88% | -87% |
| ETH | 2095 | 10 | 6% | 3% | -43% | -86% | -85% |
| SOL | 2094 | 4 | 4% | 2% | -76% | -92% | -92% |
| DOGE | 2090 | 4 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2085 | 8 | 3% | 1% | -53% | -88% | -88% |
| NEAR | 2082 | 12 | 6% | 3% | -25% | -80% | -80% |
| BTC | 2079 | 12 | 5% | 2% | -23% | -88% | -89% |
| GOLD | 1152 | 3 | 4% | 1% | -69% | -82% | -83% |
| SILVER | 1116 | 5 | 3% | 1% | -48% | -82% | -82% |
| WTI | 1090 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 974 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 955 | 3 | 1% | 1% | -71% | -78% | -78% |
| EURUSD | 901 | 3 | 2% | 1% | -69% | -86% | -86% |
| NATGAS | 895 | 5 | 2% | 1% | -48% | -86% | -86% |
| PALLADIUM | 867 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 848 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 824 | 5 | 1% | 1% | -43% | -99% | -98% |
| AUDUSD | 394 | 0 | 1% | 1% | -100% | -99% | -98% |
| USDCAD | 351 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 15 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14779 | 60 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 14518 | 52 | 4% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3121 | 16 | 2% | 1% | -14% | -79% | -78% |
| 0.05–0.1% | 3240 | 11 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4846 | 17 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5518 | 28 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2118 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7178 | 30 | 4% | 2% | -53% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,666 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 12:44:47 AM | AUDUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:44:47 AM | PLATINUM | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:44:47 AM | COPPER | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:44:31 AM | EURUSD | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:44:31 AM | ZEC | DOWN | 29 sec | +0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/23 12:44:16 AM | BNB | DOWN | 44 sec | -0.011% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 12:44:16 AM | DOGE | DOWN | 44 sec | +0.063% | 0¢ | ❌ Lost | $0.00 |
| 10/23 12:44:16 AM | BTC | DOWN | 44 sec | +0.054% | 0¢ | ❌ Lost | $0.00 |
| 10/23 12:44:16 AM | HYPE | DOWN | 44 sec | +0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/23 12:44:16 AM | SOL | DOWN | 44 sec | +0.085% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:44:16 AM | PALLADIUM | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:43:57 AM | GBPUSD | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:43:41 AM | USDCAD | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:42:51 AM | NEAR | DOWN | 2.1 min | +0.330% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 12:42:51 AM | XRP | DOWN | 2.1 min | +0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 12:42:19 AM | ETH | DOWN | 2.7 min | +0.085% | 3¢ | ❌ Lost | -$0.15 |
| 10/23 12:42:04 AM | USDJPY | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:29:47 AM | DOGE | UP | 13 sec | -0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:29:47 AM | USDJPY | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:29:31 AM | ZEC | UP | 29 sec | -0.158% | 0¢ | ❌ Lost | $0.00 |
| 10/23 12:29:31 AM | AUDUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:29:31 AM | USDCAD | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:29:31 AM | NEAR | UP | 29 sec | -0.187% | 0¢ | ❌ Lost | $0.00 |
| 10/23 12:29:15 AM | GBPUSD | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:29:15 AM | NATGAS | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:28:56 AM | SILVER | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 12:28:40 AM | GOLD | UP | 80 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 12:28:40 AM | BNB | DOWN | 80 sec | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 12:28:24 AM | SOL | UP | 1.6 min | -0.138% | 0¢ | ❌ Lost | $0.00 |
| 10/23 12:28:09 AM | ETH | UP | 1.8 min | -0.134% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
