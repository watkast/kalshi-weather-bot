# 15-Minute 1¢ Study

*Updated Mon Oct 26, 2:01 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2768 finished bets | 1% | $78.65 | +25% | +2.84¢ | $29.60 / $49.05 |

*Expect about **97 buys a day** (~$14.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2578 | $51.75 | +18% |
| Volatility model ≥ 2%, hold to the close | 5154 | -$14.60 | -2% |
| Momentum model ≥ 2%, hold to the close | 4286 | -$39.30 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33332 | 33324 | 124 (0%) | 1.07% | -$2,315.35 (-57%) | Hold to the close: -$2,315.35 (-57%) |

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
| Volatility model | 21295 | 4.6% | 0.4% (86) | -663% | ❌ Worse |
| Momentum model | 21295 | 4.5% | 0.4% (86) | -687% | ❌ Worse |
| Mean-reversion model | 21295 | 7.9% | 0.4% (86) | -804% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21295 | 86 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5154 | 44 | -2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2768 | 28 | +25% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1567 | 18 | +61% | -67% | -65% | -62% |
| Momentum model ≥ 2% | 4286 | 33 | -8% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2578 | 24 | +18% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1679 | 16 | +31% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8619 | 57 | -28% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 6038 | 47 | -14% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4022 | 33 | -7% | -78% | -77% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21495 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7800 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4029 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33324 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 124 | 0% | -$2,315.35 | -57% | — |
| Sell at 2¢ | 1260 | 4% | -$3,555.75 | -88% | 47 sec |
| Sell at 3¢ | 862 | 3% | -$3,547.17 | -88% | 48 sec |
| Sell at 5¢ | 599 | 2% | -$3,494.00 | -86% | 61 sec |
| Sell at 10¢ | 371 | 1% | -$3,355.34 | -83% | 65 sec |
| Sell at 25¢ | 197 | 1% | -$3,105.28 | -77% | 82 sec |
| Sell at 50¢ | 127 | 0% | -$2,816.10 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1468 | 8 | 11% | 4% | -48% | -81% | -82% |
| 2–5 min | 10697 | 57 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8446 | 31 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12709 | 28 | 1% | 0% | -68% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2408 | 12 | 5% | 2% | -37% | -88% | -88% |
| HYPE | 2401 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2398 | 13 | 5% | 3% | -32% | -84% | -83% |
| SOL | 2395 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2389 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2382 | 5 | 4% | 2% | -74% | -91% | -90% |
| NEAR | 2376 | 12 | 5% | 2% | -34% | -82% | -82% |
| XRP | 2376 | 9 | 3% | 1% | -53% | -89% | -89% |
| BTC | 2370 | 12 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1254 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1220 | 6 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1199 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1068 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1039 | 4 | 1% | 1% | -64% | -71% | -71% |
| EURUSD | 1001 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 994 | 5 | 2% | 1% | -53% | -87% | -86% |
| PALLADIUM | 957 | 2 | 1% | 0% | -80% | -88% | -89% |
| GBPUSD | 944 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 926 | 5 | 1% | 1% | -50% | -98% | -97% |
| AUDUSD | 489 | 1 | 1% | 1% | -81% | -98% | -97% |
| USDCAD | 451 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 69 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 62 | 0 | 3% | 0% | -100% | -94% | -96% |
| 30YRRATE | 55 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 53 | 1 | 4% | 0% | +76% | +83% | +81% |
| 5YRRATE | 48 | 1 | 4% | 4% | +94% | -93% | -89% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16887 | 68 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16437 | 56 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3552 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3677 | 12 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5556 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6315 | 28 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2391 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 7765 | 25 | 4% | 2% | -62% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,725 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 1:59:48 PM | SOL | UP | 11 sec | -0.054% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:59:48 PM | ETH | DOWN | 11 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:59:48 PM | BNB | DOWN | 11 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:59:32 PM | DOGE | UP | 27 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:59:32 PM | PALLADIUM | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:59:16 PM | AUDUSD | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:59:02 PM | BRENT | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:59:02 PM | ZEC | UP | 58 sec | -0.261% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 1:59:02 PM | WTI | UP | 58 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:58:46 PM | NEAR | UP | 73 sec | -0.399% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:58:46 PM | 5YRRATE | UP | 73 sec | — | 30¢ | ❌ Lost | -$0.15 |
| 10/26 1:58:46 PM | BTC | UP | 73 sec | -0.059% | 1¢ | ❌ Lost | $0.00 |
| 10/26 1:58:14 PM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:58:14 PM | 10YRRATE | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:58:14 PM | 30YRRATE | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:54:11 PM | HYPE | UP | 5.8 min | -0.679% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 1:44:50 PM | SOL | UP | 10 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:44:50 PM | DOGE | DOWN | 10 sec | +0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:44:50 PM | NEAR | DOWN | 10 sec | +0.096% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:44:50 PM | GOLD | DOWN | 10 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:44:34 PM | USDJPY | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:44:34 PM | BNB | UP | 26 sec | -0.044% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:44:18 PM | HYPE | DOWN | 42 sec | +0.115% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:44:03 PM | BTC | DOWN | 56 sec | +0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 1:43:47 PM | XRP | UP | 72 sec | -0.131% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 1:43:47 PM | ZEC | UP | 72 sec | -0.306% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:43:47 PM | EURUSD | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:43:47 PM | 2YRRATE | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:43:47 PM | 5YRRATE | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:43:15 PM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
