# 15-Minute 1¢ Study

*Updated Mon Nov 9, 1:27 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4074 finished bets | 1% | $191.00 | +42% | +4.69¢ | $93.40 / $97.60 |

*Expect about **97 buys a day** (~$14.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3782 | $108.50 | +26% |
| Volatility model ≥ 2%, hold to the close | 7459 | $82.25 | +9% |
| Momentum model ≥ 2%, hold to the close | 6158 | $6.60 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50540 | 50508 | 187 (0%) | 1.07% | -$3,526.30 (-57%) | Hold to the close: -$3,526.30 (-57%) |

*In play or awaiting result: 24. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 30888 | 4.8% | 0.4% (122) | -688% | ❌ Worse |
| Momentum model | 30888 | 4.6% | 0.4% (122) | -714% | ❌ Worse |
| Mean-reversion model | 30888 | 8.1% | 0.4% (122) | -831% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30888 | 122 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7459 | 70 | +9% | -76% | -75% | -71% |
| Volatility model ≥ 5% | 4074 | 46 | +42% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2345 | 28 | +71% | -61% | -59% | -55% |
| Momentum model ≥ 2% | 6158 | 51 | +1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3782 | 37 | +26% | -73% | -72% | -68% |
| Momentum model ≥ 10% | 2480 | 25 | +42% | -64% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12765 | 90 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8947 | 77 | -4% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5981 | 56 | +7% | -76% | -76% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31093 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11898 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7517 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50508 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 187 | 0% | -$3,526.30 | -57% | — |
| Sell at 2¢ | 1994 | 4% | -$5,345.86 | -87% | 47 sec |
| Sell at 3¢ | 1354 | 3% | -$5,336.24 | -87% | 48 sec |
| Sell at 5¢ | 946 | 2% | -$5,221.40 | -85% | 62 sec |
| Sell at 10¢ | 570 | 1% | -$5,005.60 | -81% | 65 sec |
| Sell at 25¢ | 298 | 1% | -$4,653.92 | -76% | 83 sec |
| Sell at 50¢ | 192 | 0% | -$4,246.30 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2498 | 12 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 16317 | 88 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12755 | 41 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18926 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3486 | 14 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3477 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3468 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3462 | 18 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3461 | 7 | 4% | 2% | -75% | -90% | -90% |
| ETH | 3454 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3433 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3431 | 16 | 5% | 2% | -36% | -87% | -89% |
| XRP | 3421 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1813 | 5 | 6% | 2% | -66% | -81% | -82% |
| WTI | 1783 | 6 | 4% | 1% | -60% | -92% | -92% |
| SILVER | 1764 | 8 | 5% | 2% | -46% | -82% | -82% |
| PLATINUM | 1596 | 4 | 2% | 1% | -77% | -96% | -96% |
| EURUSD | 1531 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1497 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1456 | 8 | 2% | 1% | -49% | -77% | -76% |
| GBPUSD | 1451 | 4 | 2% | 1% | -74% | -96% | -96% |
| USDJPY | 1436 | 5 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1434 | 3 | 1% | 0% | -80% | -92% | -92% |
| AUDUSD | 991 | 5 | 2% | 1% | -53% | -87% | -87% |
| USDCAD | 959 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 555 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 305 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 289 | 3 | 4% | 1% | -3% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 263 | 1 | 4% | 2% | -65% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25637 | 96 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24871 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5047 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5325 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8004 | 27 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 9243 | 39 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3466 | 14 | 7% | 3% | -58% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12283 | 43 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,950 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 1:26:52 AM | WTI | UP | 3.1 min | — | — | In play | — |
| 11/9 1:26:20 AM | SILVER | DOWN | 3.7 min | — | — | In play | — |
| 11/9 1:25:15 AM | HYPE | DOWN | 4.8 min | +0.583% | — | In play | — |
| 11/9 1:25:15 AM | NEAR | DOWN | 4.8 min | +1.216% | — | In play | — |
| 11/9 1:25:15 AM | AUDUSD | DOWN | 4.8 min | — | — | In play | — |
| 11/9 1:25:00 AM | COPPER | DOWN | 5.0 min | — | — | In play | — |
| 11/9 1:25:00 AM | EURUSD | DOWN | 5.0 min | — | — | In play | — |
| 11/9 1:24:42 AM | ZEC | DOWN | 5.3 min | +1.278% | — | In play | — |
| 11/9 1:24:10 AM | GBPUSD | DOWN | 5.8 min | — | — | In play | — |
| 11/9 1:23:22 AM | SOL | DOWN | 6.6 min | +0.765% | — | In play | — |
| 11/9 1:23:22 AM | XRP | DOWN | 6.6 min | +0.793% | — | In play | — |
| 11/9 1:23:22 AM | ETH | DOWN | 6.6 min | +0.585% | — | In play | — |
| 11/9 1:23:22 AM | BTC | DOWN | 6.6 min | +0.447% | — | In play | — |
| 11/9 1:23:06 AM | DOGE | DOWN | 6.9 min | +0.641% | — | In play | — |
| 11/9 1:22:50 AM | BNB | DOWN | 7.2 min | +0.437% | — | In play | — |
| 11/9 1:14:59 AM | 2YRRATE | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:14:59 AM | 10YRRATE | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:14:59 AM | NATGAS | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:14:59 AM | BRENT | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:14:43 AM | ZEC | DOWN | 17 sec | +0.327% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:14:43 AM | USDJPY | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:14:43 AM | WTI | UP | 17 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:14:43 AM | BTC | DOWN | 17 sec | +0.052% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:14:27 AM | XRP | DOWN | 33 sec | +0.139% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:14:27 AM | ETH | DOWN | 33 sec | +0.074% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:14:12 AM | HYPE | DOWN | 47 sec | +0.220% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:13:55 AM | USDCAD | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:13:55 AM | SOL | DOWN | 64 sec | +0.210% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:13:39 AM | NEAR | UP | 80 sec | -0.314% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:13:07 AM | DOGE | DOWN | 1.9 min | +0.257% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
