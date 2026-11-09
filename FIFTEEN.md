# 15-Minute 1¢ Study

*Updated Mon Nov 9, 6:53 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4102 finished bets | 1% | $187.85 | +41% | +4.58¢ | $91.90 / $95.95 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3805 | $106.10 | +26% |
| Volatility model ≥ 2%, hold to the close | 7507 | $76.25 | +8% |
| Momentum model ≥ 2%, hold to the close | 6196 | $2.25 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50980 | 50963 | 187 (0%) | 1.07% | -$3,584.65 (-58%) | Hold to the close: -$3,584.65 (-58%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31075 | 4.8% | 0.4% (122) | -692% | ❌ Worse |
| Momentum model | 31075 | 4.6% | 0.4% (122) | -717% | ❌ Worse |
| Mean-reversion model | 31075 | 8.1% | 0.4% (122) | -836% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31075 | 122 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7507 | 70 | +8% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4102 | 46 | +41% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2360 | 28 | +70% | -61% | -60% | -56% |
| Momentum model ≥ 2% | 6196 | 51 | +0% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3805 | 37 | +26% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 2496 | 25 | +41% | -65% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12858 | 90 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9016 | 77 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6028 | 56 | +6% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31280 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12027 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7656 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50963 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 187 | 0% | -$3,584.65 | -58% | — |
| Sell at 2¢ | 2012 | 4% | -$5,399.53 | -87% | 47 sec |
| Sell at 3¢ | 1369 | 3% | -$5,388.74 | -87% | 48 sec |
| Sell at 5¢ | 955 | 2% | -$5,273.90 | -85% | 62 sec |
| Sell at 10¢ | 576 | 1% | -$5,056.09 | -82% | 65 sec |
| Sell at 25¢ | 299 | 1% | -$4,708.96 | -76% | 83 sec |
| Sell at 50¢ | 192 | 0% | -$4,304.65 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2525 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16466 | 88 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12889 | 41 | 3% | 2% | -65% | -92% | -92% |
| Under 1 min | 19071 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3506 | 14 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3498 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3489 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3483 | 18 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 3481 | 7 | 4% | 2% | -75% | -90% | -90% |
| ETH | 3475 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3454 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3452 | 16 | 5% | 2% | -36% | -87% | -89% |
| XRP | 3442 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1831 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1802 | 6 | 4% | 1% | -60% | -92% | -92% |
| SILVER | 1780 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1613 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1546 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1510 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1472 | 8 | 2% | 1% | -49% | -77% | -77% |
| GBPUSD | 1466 | 4 | 2% | 1% | -75% | -96% | -96% |
| USDJPY | 1449 | 5 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1448 | 3 | 1% | 0% | -81% | -92% | -92% |
| AUDUSD | 1007 | 5 | 2% | 1% | -54% | -87% | -87% |
| USDCAD | 973 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 571 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 323 | 1 | 4% | 2% | -71% | -64% | -61% |
| 2YRRATE | 304 | 3 | 4% | 1% | -8% | -32% | -31% |
| 30YRRATE | 301 | 0 | 2% | 1% | -100% | -97% | -95% |
| 5YRRATE | 280 | 1 | 4% | 1% | -67% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25848 | 96 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 25115 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5056 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5349 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8045 | 27 | 5% | 2% | -58% | -89% | -89% |
| 0.2–0.5% | 9316 | 39 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3506 | 14 | 7% | 3% | -59% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12671 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12290 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,922 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 6:44:49 AM | PALLADIUM | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:44:49 AM | EURUSD | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:44:32 AM | 2YRRATE | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:44:16 AM | 5YRRATE | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:44:16 AM | SILVER | UP | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 6:43:44 AM | GOLD | UP | 75 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 6:43:44 AM | ETH | UP | 75 sec | -0.228% | 0¢ | ❌ Lost | $0.00 |
| 11/9 6:43:28 AM | BTC | UP | 1.5 min | -0.240% | 0¢ | ❌ Lost | $0.00 |
| 11/9 6:43:28 AM | GBPUSD | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:43:28 AM | ZEC | UP | 1.5 min | -0.506% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 6:43:28 AM | XRP | UP | 1.5 min | -0.483% | 0¢ | ❌ Lost | $0.00 |
| 11/9 6:43:12 AM | PLATINUM | DOWN | 1.8 min | — | 14¢ | ❌ Lost | -$0.15 |
| 11/9 6:42:47 AM | 10YRRATE | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:42:47 AM | BNB | UP | 2.2 min | -0.142% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 6:42:47 AM | DOGE | UP | 2.2 min | -0.300% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:42:47 AM | WTI | UP | 2.2 min | — | 6¢ | ❌ Lost | -$0.15 |
| 11/9 6:42:31 AM | SOL | UP | 2.5 min | -0.257% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 6:42:31 AM | NATGAS | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:42:16 AM | NEAR | UP | 2.7 min | -0.653% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 6:41:57 AM | 30YRRATE | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:41:41 AM | HYPE | UP | 3.3 min | -0.400% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:29:57 AM | 10YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:29:57 AM | GBPUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:29:57 AM | 30YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:29:41 AM | NATGAS | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:29:41 AM | PLATINUM | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:29:41 AM | ETH | DOWN | 19 sec | +0.041% | 0¢ | ❌ Lost | $0.00 |
| 11/9 6:29:41 AM | 5YRRATE | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:29:26 AM | PALLADIUM | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:29:26 AM | NEAR | DOWN | 33 sec | -0.065% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
