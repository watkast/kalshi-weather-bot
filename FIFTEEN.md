# 15-Minute 1¢ Study

*Updated Thu Oct 22, 1:09 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2387 finished bets | 1% | $80.30 | +30% | +3.36¢ | $38.55 / $41.75 |

*Expect about **97 buys a day** (~$14.60/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2203 | $49.65 | +20% |
| Volatility model ≥ 2%, hold to the close | 4396 | $7.50 | +1% |
| Momentum model ≥ 2%, hold to the close | 3684 | -$27.95 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28497 | 28489 | 108 (0%) | 1.07% | -$1,961.10 (-56%) | Hold to the close: -$1,961.10 (-56%) |

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
| Volatility model | 18233 | 4.7% | 0.4% (78) | -644% | ❌ Worse |
| Momentum model | 18233 | 4.6% | 0.4% (78) | -670% | ❌ Worse |
| Mean-reversion model | 18233 | 7.9% | 0.4% (78) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18233 | 78 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4396 | 39 | +1% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2387 | 25 | +30% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1359 | 16 | +66% | -63% | -61% | -59% |
| Momentum model ≥ 2% | 3684 | 29 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2203 | 21 | +20% | -76% | -75% | -72% |
| Momentum model ≥ 10% | 1448 | 14 | +32% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7287 | 52 | -22% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5089 | 43 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3384 | 30 | +1% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18432 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6849 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3208 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28489 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 108 | 0% | -$1,961.10 | -56% | — |
| Sell at 2¢ | 1044 | 4% | -$3,061.66 | -88% | 47 sec |
| Sell at 3¢ | 713 | 3% | -$3,055.03 | -88% | 48 sec |
| Sell at 5¢ | 501 | 2% | -$3,007.45 | -87% | 61 sec |
| Sell at 10¢ | 309 | 1% | -$2,900.31 | -84% | 64 sec |
| Sell at 25¢ | 171 | 1% | -$2,669.09 | -77% | 83 sec |
| Sell at 50¢ | 112 | 0% | -$2,409.10 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1187 | 7 | 11% | 4% | -44% | -80% | -83% |
| 2–5 min | 9175 | 51 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7245 | 27 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 10878 | 23 | 1% | 0% | -70% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2066 | 12 | 5% | 2% | -27% | -89% | -89% |
| BNB | 2061 | 12 | 5% | 3% | -28% | -83% | -82% |
| HYPE | 2058 | 8 | 5% | 3% | -52% | -88% | -87% |
| ETH | 2048 | 10 | 6% | 3% | -41% | -86% | -86% |
| SOL | 2048 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2044 | 4 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2038 | 7 | 3% | 1% | -58% | -88% | -88% |
| NEAR | 2035 | 12 | 6% | 3% | -23% | -80% | -80% |
| BTC | 2034 | 12 | 5% | 2% | -21% | -88% | -90% |
| GOLD | 1118 | 3 | 3% | 1% | -68% | -82% | -84% |
| SILVER | 1082 | 4 | 3% | 1% | -57% | -83% | -82% |
| WTI | 1058 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 941 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 933 | 3 | 1% | 1% | -70% | -78% | -77% |
| EURUSD | 870 | 3 | 2% | 1% | -68% | -85% | -85% |
| NATGAS | 866 | 5 | 2% | 1% | -46% | -86% | -85% |
| PALLADIUM | 841 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 815 | 1 | 2% | 1% | -89% | -97% | -96% |
| USDJPY | 788 | 4 | 1% | 1% | -53% | -99% | -98% |
| AUDUSD | 369 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 325 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 14 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 10 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14390 | 57 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 14099 | 51 | 3% | 1% | -58% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3056 | 15 | 2% | 1% | -18% | -78% | -78% |
| 0.05–0.1% | 3167 | 11 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4715 | 17 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 5402 | 27 | 6% | 3% | -45% | -87% | -87% |
| Over 0.5% | 2088 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6617 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,683 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 12:59:59 PM | 2YRRATE | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:59:59 PM | COPPER | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:59:59 PM | EURUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:59:43 PM | USDJPY | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:59:27 PM | GOLD | UP | 32 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 12:59:27 PM | USDCAD | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:59:00 PM | SILVER | UP | 59 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 12:58:45 PM | SOL | UP | 75 sec | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:58:13 PM | PALLADIUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:57:41 PM | BTC | DOWN | 2.3 min | +0.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:57:25 PM | XRP | DOWN | 2.6 min | +0.238% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:57:25 PM | PLATINUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:57:09 PM | BNB | DOWN | 2.8 min | +0.090% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:55:50 PM | ETH | DOWN | 4.2 min | +0.212% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:55:34 PM | HYPE | DOWN | 4.4 min | +0.317% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:55:34 PM | ZEC | DOWN | 4.4 min | +0.588% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:55:18 PM | NEAR | DOWN | 4.7 min | +0.525% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:44:46 PM | EURUSD | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:44:46 PM | 30YRRATE | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:44:30 PM | HYPE | DOWN | 30 sec | +0.065% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:44:14 PM | ETH | DOWN | 46 sec | +0.049% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:44:14 PM | XRP | DOWN | 46 sec | +0.131% | 0¢ | ❌ Lost | $0.00 |
| 10/22 12:43:58 PM | BNB | DOWN | 62 sec | +0.022% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:43:58 PM | AUDUSD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:43:58 PM | COPPER | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:43:26 PM | DOGE | DOWN | 1.6 min | +0.074% | 0¢ | ❌ Lost | $0.00 |
| 10/22 12:43:26 PM | GOLD | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:43:10 PM | BTC | DOWN | 1.8 min | +0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:43:10 PM | NEAR | UP | 1.8 min | -0.411% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:43:10 PM | ZEC | DOWN | 1.8 min | +0.257% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
