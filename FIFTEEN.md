# 15-Minute 1¢ Study

*Updated Tue Oct 27, 3:19 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2825 finished bets | 1% | $72.50 | +23% | +2.57¢ | $68.15 / $4.35 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2634 | $45.60 | +16% |
| Volatility model ≥ 2%, hold to the close | 5249 | -$25.85 | -4% |
| Momentum model ≥ 2%, hold to the close | 4366 | -$48.30 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34254 | 34246 | 126 (0%) | 1.07% | -$2,402.25 (-58%) | Hold to the close: -$2,402.25 (-58%) |

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
| Volatility model | 21750 | 4.6% | 0.4% (86) | -675% | ❌ Worse |
| Momentum model | 21750 | 4.6% | 0.4% (86) | -700% | ❌ Worse |
| Mean-reversion model | 21750 | 8.0% | 0.4% (86) | -819% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21750 | 86 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5249 | 44 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2825 | 28 | +23% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1606 | 18 | +57% | -67% | -65% | -63% |
| Momentum model ≥ 2% | 4366 | 33 | -9% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2634 | 24 | +16% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1720 | 16 | +28% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8807 | 57 | -29% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6167 | 47 | -16% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4111 | 33 | -9% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21950 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8066 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4230 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34246 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 126 | 0% | -$2,402.25 | -58% | — |
| Sell at 2¢ | 1282 | 4% | -$3,664.93 | -88% | 47 sec |
| Sell at 3¢ | 877 | 3% | -$3,656.22 | -88% | 48 sec |
| Sell at 5¢ | 607 | 2% | -$3,603.70 | -86% | 62 sec |
| Sell at 10¢ | 374 | 1% | -$3,452.31 | -83% | 65 sec |
| Sell at 25¢ | 200 | 1% | -$3,196.25 | -77% | 83 sec |
| Sell at 50¢ | 130 | 0% | -$2,896.75 | -70% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1504 | 8 | 11% | 4% | -49% | -81% | -82% |
| 2–5 min | 10984 | 58 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8685 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13069 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2459 | 12 | 5% | 2% | -38% | -89% | -88% |
| HYPE | 2451 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2449 | 13 | 5% | 2% | -34% | -84% | -83% |
| SOL | 2445 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2439 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2434 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2427 | 12 | 5% | 2% | -36% | -82% | -82% |
| XRP | 2425 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2421 | 12 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1291 | 5 | 4% | 2% | -54% | -82% | -83% |
| SILVER | 1257 | 6 | 4% | 2% | -44% | -82% | -82% |
| WTI | 1236 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1107 | 0 | 2% | 1% | -100% | -97% | -97% |
| COPPER | 1068 | 4 | 1% | 1% | -65% | -72% | -71% |
| EURUSD | 1037 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1024 | 5 | 2% | 1% | -54% | -87% | -87% |
| PALLADIUM | 985 | 2 | 1% | 0% | -81% | -89% | -89% |
| GBPUSD | 978 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 963 | 5 | 1% | 1% | -52% | -98% | -97% |
| AUDUSD | 521 | 2 | 1% | 1% | -64% | -98% | -97% |
| USDCAD | 481 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 98 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 69 | 0 | 3% | 0% | -100% | -95% | -96% |
| 30YRRATE | 62 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 61 | 1 | 3% | 0% | +53% | +59% | +57% |
| 5YRRATE | 58 | 1 | 3% | 3% | +61% | -94% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17382 | 69 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16864 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3618 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3763 | 12 | 3% | 2% | -53% | -92% | -92% |
| 0.1–0.2% | 5690 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6462 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2413 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8560 | 33 | 4% | 2% | -56% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,694 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 3:14:30 AM | XRP | DOWN | 29 sec | -0.023% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:14:30 AM | BNB | DOWN | 29 sec | -0.035% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:14:14 AM | SOL | UP | 45 sec | -0.099% | 0¢ | ❌ Lost | $0.00 |
| 10/27 3:14:14 AM | ETH | UP | 45 sec | -0.098% | 0¢ | ❌ Lost | $0.00 |
| 10/27 3:13:42 AM | NEAR | UP | 78 sec | -0.289% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:13:26 AM | USDJPY | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:13:26 AM | 5YRRATE | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:13:26 AM | BTC | UP | 1.6 min | -0.127% | 0¢ | ❌ Lost | $0.00 |
| 10/27 3:13:26 AM | DOGE | UP | 1.6 min | -0.167% | 0¢ | ❌ Lost | $0.00 |
| 10/27 3:13:10 AM | ZEC | UP | 1.8 min | -0.308% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:13:10 AM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:12:37 AM | 30YRRATE | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:12:37 AM | GBPUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:12:21 AM | HYPE | UP | 2.6 min | -0.323% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 3:12:21 AM | EURUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:11:35 AM | PLATINUM | DOWN | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:10:32 AM | USDCAD | DOWN | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:09:44 AM | 10YRRATE | UP | 5.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:09:44 AM | BRENT | UP | 5.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:09:05 AM | GOLD | DOWN | 5.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 3:09:05 AM | SILVER | DOWN | 5.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 3:08:49 AM | WTI | UP | 6.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 2:59:53 AM | GBPUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:59:53 AM | USDCAD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:59:20 AM | USDJPY | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:59:20 AM | PLATINUM | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:59:20 AM | 30YRRATE | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:59:20 AM | 2YRRATE | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:59:20 AM | DOGE | UP | 39 sec | -0.057% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:59:06 AM | BRENT | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
