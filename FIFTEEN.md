# 15-Minute 1¢ Study

*Updated Thu Oct 22, 7:56 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2413 finished bets | 1% | $76.85 | +28% | +3.18¢ | $36.90 / $39.95 |

*Expect about **97 buys a day** (~$14.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2228 | $46.95 | +19% |
| Volatility model ≥ 2%, hold to the close | 4456 | -$0.45 | -0% |
| Momentum model ≥ 2%, hold to the close | 3722 | -$32.45 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28956 | 28944 | 110 (0%) | 1.07% | -$1,988.75 (-56%) | Hold to the close: -$1,988.75 (-56%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 18472 | 4.7% | 0.4% (79) | -643% | ❌ Worse |
| Momentum model | 18472 | 4.6% | 0.4% (79) | -668% | ❌ Worse |
| Mean-reversion model | 18472 | 7.9% | 0.4% (79) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18472 | 79 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4456 | 39 | -0% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2413 | 25 | +28% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1372 | 16 | +64% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3722 | 29 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2228 | 21 | +19% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1467 | 14 | +31% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7392 | 52 | -23% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5173 | 43 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3442 | 30 | -1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18671 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6959 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3314 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28944 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 110 | 0% | -$1,988.75 | -56% | — |
| Sell at 2¢ | 1074 | 4% | -$3,109.51 | -88% | 47 sec |
| Sell at 3¢ | 733 | 3% | -$3,102.88 | -88% | 48 sec |
| Sell at 5¢ | 516 | 2% | -$3,053.35 | -87% | 61 sec |
| Sell at 10¢ | 316 | 1% | -$2,946.79 | -84% | 64 sec |
| Sell at 25¢ | 175 | 1% | -$2,711.50 | -77% | 83 sec |
| Sell at 50¢ | 115 | 0% | -$2,444.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1219 | 7 | 11% | 4% | -45% | -80% | -83% |
| 2–5 min | 9315 | 52 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7349 | 28 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 11057 | 23 | 1% | 0% | -70% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2093 | 12 | 5% | 2% | -28% | -89% | -89% |
| BNB | 2086 | 12 | 5% | 3% | -29% | -83% | -82% |
| HYPE | 2084 | 8 | 5% | 3% | -53% | -88% | -87% |
| ETH | 2075 | 10 | 6% | 3% | -42% | -86% | -85% |
| SOL | 2075 | 3 | 3% | 1% | -82% | -92% | -92% |
| DOGE | 2071 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2066 | 8 | 3% | 1% | -52% | -88% | -88% |
| NEAR | 2062 | 12 | 6% | 3% | -25% | -80% | -80% |
| BTC | 2059 | 12 | 5% | 2% | -22% | -88% | -90% |
| GOLD | 1138 | 3 | 4% | 1% | -69% | -81% | -83% |
| SILVER | 1098 | 5 | 3% | 1% | -47% | -82% | -82% |
| WTI | 1077 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 957 | 0 | 1% | 1% | -100% | -99% | -98% |
| COPPER | 943 | 3 | 1% | 1% | -70% | -78% | -77% |
| EURUSD | 885 | 3 | 2% | 1% | -68% | -86% | -86% |
| NATGAS | 880 | 5 | 2% | 1% | -47% | -86% | -85% |
| PALLADIUM | 853 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 835 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 807 | 4 | 1% | 1% | -54% | -99% | -98% |
| AUDUSD | 380 | 0 | 1% | 1% | -100% | -99% | -98% |
| USDCAD | 339 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14608 | 59 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 14336 | 51 | 3% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3098 | 15 | 2% | 1% | -19% | -79% | -78% |
| 0.05–0.1% | 3206 | 11 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4793 | 17 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 5463 | 28 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2107 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7859 | 26 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,679 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 7:56:14 PM | SILVER | UP | 3.8 min | — | — | In play | — |
| 10/22 7:55:58 PM | GOLD | UP | 4.0 min | — | — | In play | — |
| 10/22 7:55:25 PM | WTI | DOWN | 4.6 min | — | — | In play | — |
| 10/22 7:54:18 PM | PLATINUM | UP | 5.7 min | — | — | In play | — |
| 10/22 7:44:46 PM | PALLADIUM | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:44:46 PM | ZEC | DOWN | 13 sec | +0.236% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:44:46 PM | BNB | DOWN | 13 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:44:46 PM | GOLD | UP | 13 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:44:46 PM | GBPUSD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:44:30 PM | NEAR | UP | 29 sec | -0.191% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:44:30 PM | AUDUSD | DOWN | 29 sec | — | 19¢ | ❌ Lost | -$0.15 |
| 10/22 7:44:30 PM | SILVER | UP | 29 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:44:30 PM | SOL | DOWN | 29 sec | +0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:44:14 PM | DOGE | DOWN | 45 sec | +0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:44:14 PM | XRP | DOWN | 45 sec | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:44:14 PM | BTC | UP | 45 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:43:59 PM | USDCAD | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:43:59 PM | ETH | DOWN | 60 sec | +0.153% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:43:59 PM | HYPE | DOWN | 60 sec | +0.159% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:43:10 PM | NATGAS | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:42:19 PM | USDJPY | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:40:43 PM | PLATINUM | DOWN | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:29:31 PM | DOGE | UP | 28 sec | -0.104% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:28:42 PM | BTC | DOWN | 78 sec | +0.066% | 3¢ | ❌ Lost | -$0.15 |
| 10/22 7:28:26 PM | ETH | DOWN | 1.6 min | +0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:28:26 PM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:28:26 PM | WTI | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:28:26 PM | ZEC | DOWN | 1.6 min | +0.341% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:28:10 PM | XRP | DOWN | 1.8 min | +0.199% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:27:55 PM | HYPE | DOWN | 2.1 min | +0.225% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
