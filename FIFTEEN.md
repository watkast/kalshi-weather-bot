# 15-Minute 1¢ Study

*Updated Thu Oct 22, 6:44 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2359 finished bets | 1% | $70.05 | +26% | +2.97¢ | $40.05 / $30.00 |

*Expect about **97 buys a day** (~$14.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2180 | $52.50 | +22% |
| Volatility model ≥ 2%, hold to the close | 4333 | -$11.80 | -2% |
| Momentum model ≥ 2%, hold to the close | 3634 | -$35.65 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28062 | 28043 | 106 (0%) | 1.07% | -$1,933.00 (-57%) | Hold to the close: -$1,933.00 (-57%) |

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
| Volatility model | 18006 | 4.7% | 0.4% (76) | -657% | ❌ Worse |
| Momentum model | 18006 | 4.6% | 0.4% (76) | -682% | ❌ Worse |
| Mean-reversion model | 18006 | 7.9% | 0.4% (76) | -788% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18006 | 76 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4333 | 37 | -2% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2359 | 24 | +26% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1351 | 16 | +67% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 3634 | 28 | -8% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2180 | 21 | +22% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1432 | 14 | +34% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7176 | 50 | -24% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5013 | 41 | -10% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3340 | 28 | -5% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18205 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6732 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3106 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28043 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 106 | 0% | -$1,933.00 | -57% | — |
| Sell at 2¢ | 1024 | 4% | -$3,010.76 | -88% | 46 sec |
| Sell at 3¢ | 700 | 2% | -$3,004.00 | -88% | 48 sec |
| Sell at 5¢ | 494 | 2% | -$2,955.90 | -87% | 61 sec |
| Sell at 10¢ | 304 | 1% | -$2,850.76 | -83% | 64 sec |
| Sell at 25¢ | 168 | 1% | -$2,622.92 | -77% | 82 sec |
| Sell at 50¢ | 110 | 0% | -$2,366.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1159 | 6 | 11% | 4% | -50% | -81% | -84% |
| 2–5 min | 9021 | 50 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7132 | 27 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 10727 | 23 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2040 | 11 | 5% | 2% | -33% | -89% | -89% |
| BNB | 2036 | 12 | 5% | 3% | -27% | -83% | -82% |
| HYPE | 2032 | 7 | 5% | 3% | -58% | -89% | -87% |
| ETH | 2023 | 10 | 6% | 3% | -40% | -87% | -86% |
| SOL | 2022 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2020 | 4 | 4% | 2% | -75% | -90% | -89% |
| XRP | 2013 | 7 | 3% | 1% | -57% | -88% | -88% |
| NEAR | 2010 | 12 | 6% | 3% | -23% | -80% | -80% |
| BTC | 2009 | 12 | 5% | 2% | -20% | -88% | -90% |
| GOLD | 1102 | 3 | 4% | 1% | -68% | -82% | -84% |
| SILVER | 1063 | 4 | 3% | 1% | -56% | -82% | -82% |
| WTI | 1038 | 3 | 3% | 1% | -66% | -94% | -95% |
| PLATINUM | 925 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 912 | 3 | 1% | 1% | -69% | -77% | -77% |
| NATGAS | 854 | 5 | 2% | 1% | -45% | -86% | -85% |
| EURUSD | 852 | 3 | 2% | 1% | -67% | -85% | -85% |
| PALLADIUM | 831 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 799 | 1 | 2% | 1% | -88% | -97% | -96% |
| USDJPY | 767 | 4 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 355 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 311 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 9 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 7 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14149 | 56 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 13894 | 50 | 3% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3036 | 15 | 2% | 1% | -17% | -78% | -78% |
| 0.05–0.1% | 3147 | 11 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4654 | 17 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5312 | 27 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2052 | 8 | 7% | 3% | -60% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 6633 | 31 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,695 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 6:44:30 AM | SILVER | UP | 29 sec | — | — | In play | — |
| 10/22 6:44:30 AM | USDJPY | DOWN | 29 sec | — | — | In play | — |
| 10/22 6:43:57 AM | COPPER | DOWN | 63 sec | — | — | In play | — |
| 10/22 6:43:57 AM | NEAR | UP | 63 sec | -0.323% | — | In play | — |
| 10/22 6:43:57 AM | SOL | UP | 63 sec | -0.087% | — | In play | — |
| 10/22 6:43:10 AM | ZEC | UP | 1.8 min | -0.395% | — | In play | — |
| 10/22 6:42:53 AM | BTC | UP | 2.1 min | -0.128% | — | In play | — |
| 10/22 6:42:37 AM | GOLD | DOWN | 2.4 min | — | — | In play | — |
| 10/22 6:42:06 AM | XRP | UP | 2.9 min | -0.211% | — | In play | — |
| 10/22 6:40:15 AM | ETH | UP | 4.7 min | -0.237% | — | In play | — |
| 10/22 6:39:59 AM | BNB | UP | 5.0 min | -0.184% | — | In play | — |
| 10/22 6:29:59 AM | COPPER | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:29:59 AM | SILVER | DOWN | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:29:59 AM | NATGAS | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:29:59 AM | WTI | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:29:42 AM | GOLD | DOWN | 18 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:29:42 AM | ZEC | UP | 18 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:29:26 AM | PALLADIUM | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:29:26 AM | GBPUSD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:28:55 AM | EURUSD | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:28:55 AM | BTC | DOWN | 64 sec | +0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:28:38 AM | HYPE | DOWN | 82 sec | +0.091% | 1¢ | ❌ Lost | $0.00 |
| 10/22 6:28:38 AM | SOL | DOWN | 82 sec | +0.140% | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:28:22 AM | USDCAD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:28:06 AM | BNB | DOWN | 1.9 min | +0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:27:51 AM | ETH | DOWN | 2.1 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:27:51 AM | DOGE | DOWN | 2.1 min | +0.227% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:27:04 AM | XRP | DOWN | 2.9 min | +0.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:24:40 AM | NEAR | DOWN | 5.3 min | +0.482% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:14:55 AM | BRENT | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
