# 15-Minute 1¢ Study

*Updated Thu Oct 22, 8:27 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2416 finished bets | 1% | $76.70 | +28% | +3.17¢ | $36.75 / $39.95 |

*Expect about **97 buys a day** (~$14.61/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2230 | $46.95 | +19% |
| Volatility model ≥ 2%, hold to the close | 4460 | -$0.75 | -0% |
| Momentum model ≥ 2%, hold to the close | 3726 | -$32.60 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28996 | 28981 | 110 (0%) | 1.07% | -$1,993.10 (-56%) | Hold to the close: -$1,993.10 (-56%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 18489 | 4.7% | 0.4% (79) | -643% | ❌ Worse |
| Momentum model | 18489 | 4.6% | 0.4% (79) | -668% | ❌ Worse |
| Mean-reversion model | 18489 | 7.9% | 0.4% (79) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18489 | 79 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4460 | 39 | -0% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2416 | 25 | +28% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1374 | 16 | +64% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3726 | 29 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2230 | 21 | +19% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1468 | 14 | +31% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7402 | 52 | -23% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5176 | 43 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3444 | 30 | -1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18688 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6971 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3322 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28981 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 110 | 0% | -$1,993.10 | -56% | — |
| Sell at 2¢ | 1074 | 4% | -$3,113.86 | -88% | 47 sec |
| Sell at 3¢ | 733 | 3% | -$3,107.23 | -88% | 48 sec |
| Sell at 5¢ | 516 | 2% | -$3,057.70 | -87% | 61 sec |
| Sell at 10¢ | 316 | 1% | -$2,951.14 | -84% | 64 sec |
| Sell at 25¢ | 175 | 1% | -$2,715.85 | -77% | 83 sec |
| Sell at 50¢ | 115 | 0% | -$2,448.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1222 | 7 | 11% | 4% | -45% | -80% | -83% |
| 2–5 min | 9326 | 52 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7361 | 28 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 11068 | 23 | 1% | 0% | -70% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2095 | 12 | 5% | 2% | -28% | -89% | -89% |
| BNB | 2088 | 12 | 5% | 3% | -29% | -83% | -82% |
| HYPE | 2086 | 8 | 5% | 3% | -53% | -88% | -87% |
| ETH | 2077 | 10 | 6% | 3% | -42% | -86% | -85% |
| SOL | 2077 | 3 | 3% | 1% | -82% | -92% | -92% |
| DOGE | 2073 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2067 | 8 | 3% | 1% | -52% | -88% | -88% |
| NEAR | 2064 | 12 | 6% | 3% | -25% | -80% | -80% |
| BTC | 2061 | 12 | 5% | 2% | -22% | -88% | -90% |
| GOLD | 1140 | 3 | 4% | 1% | -69% | -81% | -83% |
| SILVER | 1100 | 5 | 3% | 1% | -47% | -82% | -82% |
| WTI | 1078 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 959 | 0 | 1% | 1% | -100% | -99% | -98% |
| COPPER | 945 | 3 | 1% | 1% | -70% | -78% | -77% |
| EURUSD | 887 | 3 | 2% | 1% | -68% | -86% | -86% |
| NATGAS | 881 | 5 | 2% | 1% | -47% | -86% | -85% |
| PALLADIUM | 855 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 836 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 809 | 4 | 1% | 1% | -54% | -99% | -98% |
| AUDUSD | 381 | 0 | 1% | 1% | -100% | -99% | -98% |
| USDCAD | 341 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14624 | 59 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 14357 | 51 | 3% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3101 | 15 | 2% | 1% | -19% | -79% | -78% |
| 0.05–0.1% | 3209 | 11 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4801 | 17 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 5466 | 28 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2107 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7896 | 26 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,678 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 8:27:04 PM | DOGE | DOWN | 2.9 min | +0.271% | — | In play | — |
| 10/22 8:27:04 PM | ZEC | DOWN | 2.9 min | +0.576% | — | In play | — |
| 10/22 8:27:04 PM | HYPE | DOWN | 2.9 min | +0.212% | — | In play | — |
| 10/22 8:26:46 PM | BTC | DOWN | 3.2 min | +0.305% | — | In play | — |
| 10/22 8:26:30 PM | XRP | DOWN | 3.5 min | +0.373% | — | In play | — |
| 10/22 8:26:14 PM | ETH | DOWN | 3.8 min | +0.286% | — | In play | — |
| 10/22 8:25:09 PM | BNB | DOWN | 4.8 min | +0.194% | — | In play | — |
| 10/22 8:14:46 PM | ZEC | UP | 14 sec | -0.109% | 0¢ | ❌ Lost | $0.00 |
| 10/22 8:14:46 PM | EURUSD | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:14:30 PM | USDCAD | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:14:30 PM | NEAR | DOWN | 30 sec | +0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/22 8:14:15 PM | DOGE | DOWN | 45 sec | +0.099% | 0¢ | ❌ Lost | $0.00 |
| 10/22 8:14:15 PM | XRP | DOWN | 45 sec | +0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:14:15 PM | HYPE | DOWN | 45 sec | +0.089% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:13:58 PM | SOL | DOWN | 61 sec | +0.108% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:13:58 PM | USDJPY | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:13:42 PM | NATGAS | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:13:26 PM | ETH | DOWN | 1.6 min | +0.151% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:13:26 PM | BTC | DOWN | 1.6 min | +0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:12:51 PM | COPPER | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:12:35 PM | BNB | DOWN | 2.4 min | +0.142% | 1¢ | ❌ Lost | $0.00 |
| 10/22 8:12:04 PM | PALLADIUM | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:10:10 PM | PLATINUM | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 8:09:37 PM | SILVER | DOWN | 5.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 8:08:49 PM | GOLD | DOWN | 6.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:59:29 PM | BNB | DOWN | 31 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:59:29 PM | SOL | UP | 31 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:59:14 PM | DOGE | UP | 45 sec | -0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:59:14 PM | NEAR | DOWN | 45 sec | +0.217% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:58:56 PM | ZEC | UP | 64 sec | -0.422% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
