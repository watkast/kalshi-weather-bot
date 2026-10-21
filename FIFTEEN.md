# 15-Minute 1¢ Study

*Updated Wed Oct 21, 1:27 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2280 finished bets | 1% | $78.15 | +30% | +3.43¢ | $44.40 / $33.75 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2110 | $59.40 | +25% |
| Volatility model ≥ 2%, hold to the close | 4183 | -$8.55 | -2% |
| Momentum model ≥ 2%, hold to the close | 3529 | -$38.40 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27031 | 27015 | 99 (0%) | 1.07% | -$1,906.65 (-58%) | Hold to the close: -$1,906.65 (-58%) |

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
| Volatility model | 17470 | 4.6% | 0.4% (71) | -656% | ❌ Worse |
| Momentum model | 17470 | 4.6% | 0.4% (71) | -680% | ❌ Worse |
| Mean-reversion model | 17470 | 7.8% | 0.4% (71) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17470 | 71 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4183 | 36 | -2% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2280 | 24 | +30% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1304 | 16 | +72% | -61% | -60% | -57% |
| Momentum model ≥ 2% | 3529 | 27 | -9% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2110 | 21 | +25% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1387 | 14 | +37% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6926 | 47 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4836 | 39 | -11% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3220 | 27 | -5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17668 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6447 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2900 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 27015 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 99 | 0% | -$1,906.65 | -58% | — |
| Sell at 2¢ | 990 | 4% | -$2,895.25 | -88% | 46 sec |
| Sell at 3¢ | 673 | 2% | -$2,890.18 | -88% | 48 sec |
| Sell at 5¢ | 476 | 2% | -$2,843.25 | -86% | 56 sec |
| Sell at 10¢ | 290 | 1% | -$2,744.75 | -83% | 64 sec |
| Sell at 25¢ | 159 | 1% | -$2,542.36 | -77% | 81 sec |
| Sell at 50¢ | 102 | 0% | -$2,310.15 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1091 | 6 | 11% | 4% | -47% | -81% | -83% |
| 2–5 min | 8713 | 45 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 6888 | 25 | 3% | 1% | -61% | -93% | -92% |
| Under 1 min | 10319 | 23 | 1% | 0% | -68% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1982 | 11 | 5% | 2% | -31% | -89% | -89% |
| BNB | 1975 | 11 | 5% | 2% | -32% | -83% | -82% |
| HYPE | 1974 | 7 | 5% | 3% | -56% | -88% | -86% |
| ETH | 1962 | 10 | 6% | 3% | -39% | -87% | -86% |
| DOGE | 1962 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1961 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1954 | 7 | 3% | 1% | -56% | -88% | -88% |
| NEAR | 1949 | 11 | 6% | 3% | -27% | -79% | -79% |
| BTC | 1949 | 11 | 5% | 2% | -24% | -88% | -90% |
| GOLD | 1056 | 2 | 3% | 1% | -78% | -81% | -84% |
| SILVER | 1018 | 4 | 3% | 1% | -55% | -82% | -82% |
| WTI | 994 | 3 | 3% | 1% | -64% | -94% | -95% |
| PLATINUM | 886 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 878 | 3 | 1% | 1% | -68% | -76% | -76% |
| NATGAS | 814 | 5 | 2% | 1% | -43% | -85% | -84% |
| EURUSD | 809 | 3 | 2% | 1% | -65% | -84% | -84% |
| PALLADIUM | 801 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 759 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 723 | 3 | 1% | 1% | -61% | -99% | -98% |
| AUDUSD | 322 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 279 | 0 | 0% | 0% | -100% | -99% | -99% |
| 2YRRATE | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 2 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13565 | 49 | 4% | 2% | -59% | -88% | -87% |
| DOWN (bought NO) | 13450 | 50 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2950 | 15 | 2% | 1% | -15% | -78% | -77% |
| 0.05–0.1% | 3056 | 11 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 4496 | 15 | 5% | 2% | -59% | -89% | -89% |
| 0.2–0.5% | 5160 | 25 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 2003 | 7 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6244 | 19 | 4% | 2% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,735 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 1:27:23 PM | 30YRRATE | UP | 2.6 min | — | — | In play | — |
| 10/21 1:27:23 PM | WTI | UP | 2.6 min | — | — | In play | — |
| 10/21 1:27:06 PM | XRP | DOWN | 2.9 min | +0.282% | — | In play | — |
| 10/21 1:26:50 PM | HYPE | DOWN | 3.1 min | +0.464% | — | In play | — |
| 10/21 1:26:34 PM | DOGE | DOWN | 3.4 min | +0.276% | — | In play | — |
| 10/21 1:26:18 PM | SOL | DOWN | 3.7 min | +0.326% | — | In play | — |
| 10/21 1:26:02 PM | ZEC | DOWN | 4.0 min | +0.618% | — | In play | — |
| 10/21 1:25:46 PM | ETH | DOWN | 4.2 min | +0.399% | — | In play | — |
| 10/21 1:25:30 PM | NEAR | DOWN | 4.5 min | +0.742% | — | In play | — |
| 10/21 1:14:50 PM | GOLD | DOWN | 10 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 1:14:50 PM | BNB | UP | 10 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/21 1:14:50 PM | GBPUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 1:14:34 PM | ZEC | UP | 26 sec | -0.114% | 10¢ | ❌ Lost | $0.00 |
| 10/21 1:14:34 PM | PALLADIUM | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 1:14:18 PM | SILVER | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 1:14:03 PM | BTC | UP | 56 sec | -0.108% | 0¢ | ❌ Lost | $0.00 |
| 10/21 1:14:03 PM | HYPE | UP | 56 sec | -0.229% | 0¢ | ❌ Lost | $0.00 |
| 10/21 1:14:03 PM | DOGE | UP | 56 sec | -0.199% | 0¢ | ❌ Lost | $0.00 |
| 10/21 1:14:03 PM | EURUSD | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 1:11:06 PM | NEAR | UP | 3.9 min | -0.870% | 3¢ | ❌ Lost | -$0.15 |
| 10/21 1:11:06 PM | SOL | UP | 3.9 min | -0.593% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:11:06 PM | XRP | UP | 3.9 min | -0.620% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 1:10:49 PM | ETH | UP | 4.2 min | -0.459% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 12:59:34 PM | USDCAD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:59:17 PM | 2YRRATE | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:59:17 PM | 5YRRATE | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:59:17 PM | AUDUSD | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:59:17 PM | 30YRRATE | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:59:00 PM | NATGAS | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 12:58:13 PM | 10YRRATE | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
