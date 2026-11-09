# 15-Minute 1¢ Study

*Updated Mon Nov 9, 1:37 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

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
| Volatility model ≥ 2%, hold to the close | 7460 | $82.10 | +9% |
| Momentum model ≥ 2%, hold to the close | 6158 | $6.60 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50548 | 50531 | 187 (0%) | 1.07% | -$3,529.60 (-57%) | Hold to the close: -$3,529.60 (-57%) |

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
| Volatility model | 30897 | 4.8% | 0.4% (122) | -688% | ❌ Worse |
| Momentum model | 30897 | 4.6% | 0.4% (122) | -714% | ❌ Worse |
| Mean-reversion model | 30897 | 8.1% | 0.4% (122) | -831% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30897 | 122 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7460 | 70 | +9% | -76% | -75% | -71% |
| Volatility model ≥ 5% | 4074 | 46 | +42% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2345 | 28 | +71% | -61% | -59% | -55% |
| Momentum model ≥ 2% | 6158 | 51 | +1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3782 | 37 | +26% | -73% | -72% | -68% |
| Momentum model ≥ 10% | 2480 | 25 | +42% | -64% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12772 | 90 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8954 | 77 | -4% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5985 | 56 | +7% | -76% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31102 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11905 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7524 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50531 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 187 | 0% | -$3,529.60 | -57% | — |
| Sell at 2¢ | 1995 | 4% | -$5,348.90 | -87% | 47 sec |
| Sell at 3¢ | 1355 | 3% | -$5,339.15 | -87% | 48 sec |
| Sell at 5¢ | 947 | 2% | -$5,224.05 | -85% | 62 sec |
| Sell at 10¢ | 571 | 1% | -$5,007.59 | -81% | 65 sec |
| Sell at 25¢ | 298 | 1% | -$4,657.22 | -76% | 83 sec |
| Sell at 50¢ | 192 | 0% | -$4,249.60 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2506 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16325 | 88 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12760 | 41 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18928 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3487 | 14 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3478 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3469 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3463 | 18 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3462 | 7 | 4% | 2% | -75% | -90% | -90% |
| ETH | 3455 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3434 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3432 | 16 | 5% | 2% | -36% | -87% | -89% |
| XRP | 3422 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1814 | 5 | 6% | 2% | -66% | -81% | -82% |
| WTI | 1784 | 6 | 4% | 1% | -60% | -92% | -92% |
| SILVER | 1765 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1597 | 4 | 2% | 1% | -77% | -96% | -96% |
| EURUSD | 1532 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1498 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1457 | 8 | 2% | 1% | -49% | -77% | -76% |
| GBPUSD | 1452 | 4 | 2% | 1% | -74% | -96% | -96% |
| USDJPY | 1437 | 5 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1435 | 3 | 1% | 0% | -80% | -92% | -92% |
| AUDUSD | 992 | 5 | 2% | 1% | -53% | -87% | -87% |
| USDCAD | 959 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 555 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 306 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 290 | 3 | 4% | 1% | -3% | -28% | -28% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 264 | 1 | 4% | 2% | -65% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25638 | 96 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24893 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5047 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5325 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8004 | 27 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 9245 | 39 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3473 | 14 | 7% | 3% | -58% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12306 | 43 | 4% | 2% | -60% | -87% | -87% |
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
| 11/9 1:29:53 AM | 10YRRATE | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:29:04 AM | NATGAS | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:28:32 AM | PALLADIUM | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:28:32 AM | 2YRRATE | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:28:32 AM | USDJPY | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:28:32 AM | 5YRRATE | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:28:16 AM | GOLD | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:27:39 AM | PLATINUM | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:26:52 AM | WTI | UP | 3.1 min | — | 17¢ | ❌ Lost | -$0.15 |
| 11/9 1:26:20 AM | SILVER | DOWN | 3.7 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/9 1:25:15 AM | HYPE | DOWN | 4.8 min | +0.583% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:25:15 AM | NEAR | DOWN | 4.8 min | +1.216% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:25:15 AM | AUDUSD | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:25:00 AM | COPPER | DOWN | 5.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:25:00 AM | EURUSD | DOWN | 5.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:24:42 AM | ZEC | DOWN | 5.3 min | +1.278% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:24:10 AM | GBPUSD | DOWN | 5.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:23:22 AM | SOL | DOWN | 6.6 min | +0.765% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:23:22 AM | XRP | DOWN | 6.6 min | +0.793% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:23:22 AM | ETH | DOWN | 6.6 min | +0.585% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:23:22 AM | BTC | DOWN | 6.6 min | +0.447% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:23:06 AM | DOGE | DOWN | 6.9 min | +0.641% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:22:50 AM | BNB | DOWN | 7.2 min | +0.437% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:14:59 AM | 2YRRATE | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:14:59 AM | 10YRRATE | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:14:59 AM | NATGAS | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:14:59 AM | BRENT | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:14:43 AM | ZEC | DOWN | 17 sec | +0.327% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:14:43 AM | USDJPY | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:14:43 AM | WTI | UP | 17 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
