# 15-Minute 1¢ Study

*Updated Tue Oct 27, 4:00 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2827 finished bets | 1% | $72.20 | +23% | +2.55¢ | $68.00 / $4.20 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2636 | $45.30 | +16% |
| Volatility model ≥ 2%, hold to the close | 5253 | -$26.30 | -4% |
| Momentum model ≥ 2%, hold to the close | 4370 | -$48.75 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34317 | 34292 | 126 (0%) | 1.07% | -$2,407.65 (-58%) | Hold to the close: -$2,407.65 (-58%) |

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
| Volatility model | 21772 | 4.6% | 0.4% (86) | -675% | ❌ Worse |
| Momentum model | 21772 | 4.6% | 0.4% (86) | -700% | ❌ Worse |
| Mean-reversion model | 21772 | 8.0% | 0.4% (86) | -819% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21772 | 86 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5253 | 44 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2827 | 28 | +23% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1607 | 18 | +57% | -67% | -66% | -63% |
| Momentum model ≥ 2% | 4370 | 33 | -10% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2636 | 24 | +16% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1722 | 16 | +28% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8813 | 57 | -29% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6172 | 47 | -16% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4113 | 33 | -9% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21972 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8078 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4242 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34292 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 126 | 0% | -$2,407.65 | -58% | — |
| Sell at 2¢ | 1284 | 4% | -$3,669.81 | -88% | 47 sec |
| Sell at 3¢ | 877 | 3% | -$3,661.62 | -88% | 48 sec |
| Sell at 5¢ | 607 | 2% | -$3,609.10 | -87% | 62 sec |
| Sell at 10¢ | 374 | 1% | -$3,457.71 | -83% | 65 sec |
| Sell at 25¢ | 200 | 1% | -$3,201.65 | -77% | 83 sec |
| Sell at 50¢ | 130 | 0% | -$2,902.15 | -70% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1504 | 8 | 11% | 4% | -49% | -81% | -82% |
| 2–5 min | 10994 | 58 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8699 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13091 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2461 | 12 | 5% | 2% | -38% | -89% | -88% |
| HYPE | 2454 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2452 | 13 | 5% | 2% | -34% | -84% | -83% |
| SOL | 2447 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2441 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2437 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2430 | 12 | 5% | 2% | -36% | -82% | -82% |
| XRP | 2428 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2422 | 12 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1292 | 5 | 4% | 2% | -54% | -82% | -83% |
| SILVER | 1259 | 6 | 4% | 2% | -44% | -82% | -82% |
| WTI | 1238 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1108 | 0 | 2% | 1% | -100% | -97% | -97% |
| COPPER | 1070 | 4 | 1% | 1% | -65% | -72% | -71% |
| EURUSD | 1038 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1026 | 5 | 2% | 1% | -55% | -87% | -87% |
| PALLADIUM | 986 | 2 | 1% | 0% | -81% | -89% | -89% |
| GBPUSD | 980 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 965 | 5 | 1% | 1% | -52% | -98% | -97% |
| AUDUSD | 522 | 2 | 1% | 1% | -64% | -98% | -97% |
| USDCAD | 482 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 99 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 70 | 0 | 3% | 0% | -100% | -95% | -96% |
| 30YRRATE | 64 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 62 | 1 | 3% | 0% | +51% | +56% | +55% |
| 5YRRATE | 59 | 1 | 3% | 3% | +58% | -94% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17403 | 69 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16889 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3622 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3767 | 12 | 3% | 2% | -53% | -92% | -92% |
| 0.1–0.2% | 5698 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6467 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2414 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8606 | 33 | 4% | 2% | -56% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,686 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 3:59:37 AM | DOGE | DOWN | 23 sec | +0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/27 3:59:37 AM | NEAR | DOWN | 23 sec | +0.054% | 0¢ | ❌ Lost | $0.00 |
| 10/27 3:59:37 AM | 5YRRATE | DOWN | 23 sec | — | 0¢ | In play | — |
| 10/27 3:59:21 AM | XRP | DOWN | 39 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/27 3:59:21 AM | 10YRRATE | DOWN | 39 sec | — | 0¢ | In play | — |
| 10/27 3:59:05 AM | HYPE | DOWN | 55 sec | +0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:59:05 AM | SILVER | DOWN | 55 sec | — | 1¢ | In play | — |
| 10/27 3:59:05 AM | USDCAD | UP | 55 sec | — | 0¢ | In play | — |
| 10/27 3:59:05 AM | GOLD | DOWN | 55 sec | — | 1¢ | In play | — |
| 10/27 3:58:50 AM | ETH | DOWN | 69 sec | +0.111% | 0¢ | In play | — |
| 10/27 3:58:50 AM | BTC | DOWN | 69 sec | +0.057% | 0¢ | In play | — |
| 10/27 3:58:50 AM | USDJPY | DOWN | 69 sec | — | 0¢ | In play | — |
| 10/27 3:58:03 AM | COPPER | DOWN | 1.9 min | — | 0¢ | In play | — |
| 10/27 3:57:30 AM | NATGAS | UP | 2.5 min | — | 0¢ | In play | — |
| 10/27 3:57:14 AM | ZEC | DOWN | 2.8 min | +0.658% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:57:14 AM | SOL | DOWN | 2.8 min | +0.187% | 1¢ | In play | — |
| 10/27 3:57:14 AM | GBPUSD | DOWN | 2.8 min | — | 0¢ | In play | — |
| 10/27 3:57:14 AM | BNB | DOWN | 2.8 min | +0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 3:57:14 AM | BRENT | UP | 2.8 min | — | 0¢ | In play | — |
| 10/27 3:56:43 AM | EURUSD | DOWN | 3.3 min | — | 0¢ | In play | — |
| 10/27 3:56:28 AM | PLATINUM | UP | 3.5 min | — | 96¢ | In play | — |
| 10/27 3:56:28 AM | WTI | UP | 3.5 min | — | 1¢ | In play | — |
| 10/27 3:56:12 AM | PALLADIUM | UP | 3.8 min | — | 2¢ | In play | — |
| 10/27 3:44:52 AM | PLATINUM | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:44:52 AM | GOLD | DOWN | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 3:44:37 AM | HYPE | UP | 22 sec | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/27 3:44:37 AM | USDJPY | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:44:37 AM | 30YRRATE | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 3:44:37 AM | BNB | UP | 22 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/27 3:44:21 AM | PALLADIUM | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
