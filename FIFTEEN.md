# 15-Minute 1¢ Study

*Updated Mon Oct 26, 7:22 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2793 finished bets | 1% | $76.10 | +24% | +2.72¢ | $27.95 / $48.15 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2597 | $49.80 | +17% |
| Volatility model ≥ 2%, hold to the close | 5193 | -$18.95 | -3% |
| Momentum model ≥ 2%, hold to the close | 4317 | -$42.60 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33679 | 33671 | 125 (0%) | 1.07% | -$2,343.35 (-57%) | Hold to the close: -$2,343.35 (-57%) |

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
| Volatility model | 21478 | 4.6% | 0.4% (86) | -667% | ❌ Worse |
| Momentum model | 21478 | 4.5% | 0.4% (86) | -692% | ❌ Worse |
| Mean-reversion model | 21478 | 7.9% | 0.4% (86) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21478 | 86 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5193 | 44 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2793 | 28 | +24% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1584 | 18 | +60% | -67% | -65% | -62% |
| Momentum model ≥ 2% | 4317 | 33 | -8% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2597 | 24 | +17% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1695 | 16 | +30% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8693 | 57 | -28% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 6093 | 47 | -15% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4058 | 33 | -8% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21678 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7895 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4098 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33671 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 125 | 0% | -$2,343.35 | -57% | — |
| Sell at 2¢ | 1266 | 4% | -$3,596.19 | -88% | 47 sec |
| Sell at 3¢ | 866 | 3% | -$3,587.61 | -88% | 48 sec |
| Sell at 5¢ | 601 | 2% | -$3,534.70 | -86% | 61 sec |
| Sell at 10¢ | 371 | 1% | -$3,383.34 | -83% | 65 sec |
| Sell at 25¢ | 197 | 1% | -$3,133.28 | -77% | 82 sec |
| Sell at 50¢ | 127 | 0% | -$2,844.10 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1473 | 8 | 11% | 4% | -48% | -81% | -82% |
| 2–5 min | 10792 | 57 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8517 | 31 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12885 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2428 | 12 | 5% | 2% | -37% | -89% | -88% |
| HYPE | 2421 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2418 | 13 | 5% | 2% | -33% | -84% | -83% |
| SOL | 2415 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2409 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2403 | 5 | 4% | 2% | -74% | -91% | -90% |
| NEAR | 2397 | 12 | 5% | 2% | -35% | -82% | -82% |
| XRP | 2397 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2390 | 12 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1267 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1233 | 6 | 4% | 2% | -43% | -82% | -82% |
| WTI | 1215 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1078 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1048 | 4 | 1% | 1% | -64% | -71% | -71% |
| EURUSD | 1013 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 1008 | 5 | 2% | 1% | -54% | -87% | -87% |
| PALLADIUM | 966 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 955 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 941 | 5 | 1% | 1% | -50% | -98% | -97% |
| AUDUSD | 500 | 2 | 1% | 1% | -63% | -98% | -96% |
| USDCAD | 462 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 80 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 63 | 0 | 3% | 0% | -100% | -94% | -96% |
| 2YRRATE | 57 | 1 | 4% | 0% | +64% | +70% | +68% |
| 30YRRATE | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 50 | 1 | 4% | 4% | +87% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17069 | 68 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16602 | 57 | 4% | 2% | -60% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3585 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3716 | 12 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5609 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6364 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2400 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9067 | 30 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,718 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 7:14:50 PM | HYPE | UP | 9 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 10/26 7:14:50 PM | WTI | UP | 9 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:14:34 PM | COPPER | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:14:34 PM | XRP | UP | 25 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/26 7:14:34 PM | ZEC | DOWN | 25 sec | -0.004% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:14:18 PM | PLATINUM | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:14:18 PM | AUDUSD | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:14:02 PM | SOL | DOWN | 58 sec | +0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/26 7:13:28 PM | USDCAD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:13:12 PM | GOLD | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:13:12 PM | GBPUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:12:57 PM | BTC | DOWN | 2.0 min | +0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:12:57 PM | SILVER | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:12:23 PM | EURUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:12:23 PM | NATGAS | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:12:23 PM | USDJPY | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:12:23 PM | DOGE | DOWN | 2.6 min | +0.246% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:12:23 PM | ETH | DOWN | 2.6 min | +0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:12:07 PM | BNB | DOWN | 2.9 min | +0.113% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:11:05 PM | NEAR | DOWN | 3.9 min | +0.589% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:59:57 PM | ETH | UP | 2 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:59:57 PM | SOL | UP | 2 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:59:41 PM | EURUSD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:59:41 PM | PALLADIUM | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:59:41 PM | GBPUSD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:59:41 PM | XRP | UP | 18 sec | -0.099% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:59:25 PM | WTI | UP | 34 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:59:08 PM | PLATINUM | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:59:08 PM | BNB | UP | 51 sec | -0.071% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:59:08 PM | BTC | UP | 51 sec | -0.068% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
