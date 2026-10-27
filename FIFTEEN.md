# 15-Minute 1¢ Study

*Updated Mon Oct 26, 6:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2792 finished bets | 1% | $76.25 | +24% | +2.73¢ | $27.95 / $48.30 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2596 | $49.95 | +17% |
| Volatility model ≥ 2%, hold to the close | 5189 | -$18.50 | -3% |
| Momentum model ≥ 2%, hold to the close | 4315 | -$42.30 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33642 | 33634 | 125 (0%) | 1.07% | -$2,339.15 (-57%) | Hold to the close: -$2,339.15 (-57%) |

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
| Volatility model | 21462 | 4.6% | 0.4% (86) | -668% | ❌ Worse |
| Momentum model | 21462 | 4.5% | 0.4% (86) | -692% | ❌ Worse |
| Mean-reversion model | 21462 | 7.9% | 0.4% (86) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21462 | 86 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5189 | 44 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2792 | 28 | +24% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1583 | 18 | +60% | -67% | -65% | -62% |
| Momentum model ≥ 2% | 4315 | 33 | -8% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2596 | 24 | +17% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1694 | 16 | +30% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8689 | 57 | -28% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 6090 | 47 | -15% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4056 | 33 | -8% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21662 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7883 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4089 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33634 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 125 | 0% | -$2,339.15 | -57% | — |
| Sell at 2¢ | 1266 | 4% | -$3,591.99 | -88% | 47 sec |
| Sell at 3¢ | 866 | 3% | -$3,583.41 | -88% | 48 sec |
| Sell at 5¢ | 601 | 2% | -$3,530.50 | -86% | 61 sec |
| Sell at 10¢ | 371 | 1% | -$3,379.14 | -83% | 65 sec |
| Sell at 25¢ | 197 | 1% | -$3,129.08 | -77% | 82 sec |
| Sell at 50¢ | 127 | 0% | -$2,839.90 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1473 | 8 | 11% | 4% | -48% | -81% | -82% |
| 2–5 min | 10779 | 57 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8511 | 31 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12867 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2427 | 12 | 5% | 2% | -37% | -89% | -88% |
| HYPE | 2420 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2416 | 13 | 5% | 2% | -33% | -84% | -83% |
| SOL | 2413 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2407 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2401 | 5 | 4% | 2% | -74% | -91% | -90% |
| NEAR | 2395 | 12 | 5% | 2% | -35% | -82% | -82% |
| XRP | 2395 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2388 | 12 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1265 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1231 | 6 | 4% | 2% | -43% | -82% | -82% |
| WTI | 1213 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1076 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1046 | 4 | 1% | 1% | -64% | -71% | -71% |
| EURUSD | 1011 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 1007 | 5 | 2% | 1% | -54% | -87% | -87% |
| PALLADIUM | 965 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 953 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 940 | 5 | 1% | 1% | -50% | -98% | -97% |
| AUDUSD | 498 | 2 | 1% | 1% | -63% | -98% | -96% |
| USDCAD | 460 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 80 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 63 | 0 | 3% | 0% | -100% | -94% | -96% |
| 2YRRATE | 57 | 1 | 4% | 0% | +64% | +70% | +68% |
| 30YRRATE | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 50 | 1 | 4% | 4% | +87% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17045 | 68 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16589 | 57 | 4% | 2% | -60% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3581 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3711 | 12 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5606 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6362 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2398 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9030 | 30 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,721 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 6:44:47 PM | AUDUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:44:47 PM | HYPE | DOWN | 13 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:44:31 PM | XRP | UP | 29 sec | -0.099% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:44:31 PM | DOGE | UP | 29 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:44:31 PM | SOL | UP | 29 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:44:15 PM | USDJPY | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:44:00 PM | NATGAS | DOWN | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:44:00 PM | PALLADIUM | DOWN | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:44:00 PM | BRENT | DOWN | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:44:00 PM | ETH | UP | 59 sec | -0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:43:44 PM | BNB | UP | 75 sec | -0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:43:44 PM | NEAR | UP | 75 sec | -0.431% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:43:28 PM | ZEC | UP | 1.5 min | -0.299% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:42:08 PM | PLATINUM | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:42:08 PM | WTI | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:29:58 PM | BTC | DOWN | 1 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:29:58 PM | PLATINUM | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:29:58 PM | ETH | DOWN | 1 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:29:42 PM | SILVER | UP | 17 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:29:42 PM | XRP | DOWN | 17 sec | +0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:29:26 PM | DOGE | DOWN | 33 sec | +0.014% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:29:26 PM | GBPUSD | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:29:10 PM | BRENT | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:29:10 PM | BNB | DOWN | 50 sec | -0.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:28:54 PM | EURUSD | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:28:54 PM | USDCAD | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:28:54 PM | GOLD | UP | 66 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:28:22 PM | ZEC | UP | 1.6 min | -0.299% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:28:22 PM | HYPE | DOWN | 1.6 min | +0.277% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:27:48 PM | SOL | UP | 2.2 min | -0.172% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
