# 15-Minute 1¢ Study

*Updated Mon Oct 26, 4:59 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2779 finished bets | 1% | $77.60 | +25% | +2.79¢ | $29.00 / $48.60 |

*Expect about **97 buys a day** (~$14.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2585 | $51.00 | +18% |
| Volatility model ≥ 2%, hold to the close | 5171 | -$16.55 | -3% |
| Momentum model ≥ 2%, hold to the close | 4297 | -$40.50 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33511 | 33490 | 124 (0%) | 1.07% | -$2,334.55 (-57%) | Hold to the close: -$2,334.55 (-57%) |

*In play or awaiting result: 20. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 21392 | 4.6% | 0.4% (86) | -663% | ❌ Worse |
| Momentum model | 21392 | 4.5% | 0.4% (86) | -687% | ❌ Worse |
| Mean-reversion model | 21392 | 7.9% | 0.4% (86) | -805% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21392 | 86 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5171 | 44 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2779 | 28 | +25% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1574 | 18 | +61% | -67% | -65% | -62% |
| Momentum model ≥ 2% | 4297 | 33 | -8% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2585 | 24 | +18% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1685 | 16 | +31% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8657 | 57 | -28% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 6062 | 47 | -15% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4038 | 33 | -8% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21592 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7834 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4064 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33490 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 124 | 0% | -$2,334.55 | -57% | — |
| Sell at 2¢ | 1264 | 4% | -$3,573.91 | -88% | 47 sec |
| Sell at 3¢ | 864 | 3% | -$3,565.59 | -88% | 48 sec |
| Sell at 5¢ | 600 | 2% | -$3,512.55 | -86% | 61 sec |
| Sell at 10¢ | 371 | 1% | -$3,374.54 | -83% | 65 sec |
| Sell at 25¢ | 197 | 1% | -$3,124.48 | -77% | 82 sec |
| Sell at 50¢ | 127 | 0% | -$2,835.30 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1469 | 8 | 11% | 4% | -48% | -80% | -82% |
| 2–5 min | 10726 | 57 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8480 | 31 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12811 | 28 | 1% | 0% | -69% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2419 | 12 | 5% | 2% | -37% | -88% | -88% |
| HYPE | 2412 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2408 | 13 | 5% | 2% | -33% | -84% | -83% |
| SOL | 2405 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2400 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2393 | 5 | 4% | 2% | -74% | -91% | -90% |
| NEAR | 2387 | 12 | 5% | 2% | -35% | -82% | -82% |
| XRP | 2387 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2381 | 12 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1258 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1225 | 6 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1206 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1070 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1042 | 4 | 1% | 1% | -64% | -71% | -71% |
| EURUSD | 1007 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 1001 | 5 | 2% | 1% | -53% | -87% | -87% |
| PALLADIUM | 959 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 948 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 933 | 5 | 1% | 1% | -50% | -98% | -97% |
| AUDUSD | 492 | 1 | 1% | 1% | -81% | -98% | -97% |
| USDCAD | 457 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 73 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 63 | 0 | 3% | 0% | -100% | -94% | -96% |
| 2YRRATE | 57 | 1 | 4% | 0% | +64% | +70% | +68% |
| 30YRRATE | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 50 | 1 | 4% | 4% | +87% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16978 | 68 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16512 | 56 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3568 | 18 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3697 | 12 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5593 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6335 | 28 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2395 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 7931 | 25 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

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
| 10/26 4:59:33 PM | BNB | UP | 27 sec | -0.082% | — | In play | — |
| 10/26 4:59:33 PM | PALLADIUM | DOWN | 27 sec | — | — | In play | — |
| 10/26 4:59:33 PM | BRENT | UP | 27 sec | — | — | In play | — |
| 10/26 4:59:33 PM | HYPE | UP | 27 sec | -0.095% | — | In play | — |
| 10/26 4:59:33 PM | WTI | UP | 27 sec | — | — | In play | — |
| 10/26 4:59:17 PM | DOGE | UP | 43 sec | -0.027% | — | In play | — |
| 10/26 4:59:17 PM | SILVER | UP | 43 sec | — | — | In play | — |
| 10/26 4:59:17 PM | SOL | UP | 43 sec | -0.047% | — | In play | — |
| 10/26 4:58:28 PM | ZEC | UP | 1.5 min | -0.258% | — | In play | — |
| 10/26 4:57:58 PM | GOLD | UP | 2.0 min | — | — | In play | — |
| 10/26 4:57:26 PM | NEAR | UP | 2.5 min | -0.376% | — | In play | — |
| 10/26 4:57:10 PM | AUDUSD | UP | 2.8 min | — | — | In play | — |
| 10/26 4:57:10 PM | XRP | UP | 2.8 min | -0.163% | — | In play | — |
| 10/26 4:44:55 PM | SILVER | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:44:55 PM | COPPER | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:44:39 PM | BNB | DOWN | 21 sec | +0.001% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:44:39 PM | BTC | DOWN | 21 sec | +0.009% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:44:39 PM | GBPUSD | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:44:23 PM | SOL | DOWN | 37 sec | +0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 4:44:23 PM | WTI | DOWN | 37 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 4:44:07 PM | ZEC | DOWN | 53 sec | +0.195% | 0¢ | ❌ Lost | $0.00 |
| 10/26 4:44:07 PM | EURUSD | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:44:07 PM | XRP | DOWN | 53 sec | +0.062% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:43:35 PM | USDJPY | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:43:35 PM | NEAR | DOWN | 85 sec | +0.193% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:43:19 PM | ETH | DOWN | 1.7 min | +0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 4:43:19 PM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:43:03 PM | DOGE | DOWN | 1.9 min | +0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 4:42:00 PM | HYPE | DOWN | 3.0 min | +0.261% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 4:42:00 PM | USDCAD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
