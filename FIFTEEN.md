# 15-Minute 1¢ Study

*Updated Mon Oct 26, 2:32 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2769 finished bets | 1% | $78.50 | +25% | +2.83¢ | $29.60 / $48.90 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2579 | $51.60 | +18% |
| Volatility model ≥ 2%, hold to the close | 5156 | -$14.90 | -2% |
| Momentum model ≥ 2%, hold to the close | 4287 | -$39.45 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33372 | 33364 | 124 (0%) | 1.07% | -$2,320.60 (-57%) | Hold to the close: -$2,320.60 (-57%) |

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
| Volatility model | 21313 | 4.6% | 0.4% (86) | -662% | ❌ Worse |
| Momentum model | 21313 | 4.5% | 0.4% (86) | -687% | ❌ Worse |
| Mean-reversion model | 21313 | 7.9% | 0.4% (86) | -804% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21313 | 86 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5156 | 44 | -2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2769 | 28 | +25% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1568 | 18 | +61% | -67% | -65% | -62% |
| Momentum model ≥ 2% | 4287 | 33 | -8% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2579 | 24 | +18% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1680 | 16 | +31% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8622 | 57 | -28% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 6040 | 47 | -14% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4023 | 33 | -7% | -78% | -77% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21513 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7812 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4039 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33364 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 124 | 0% | -$2,320.60 | -57% | — |
| Sell at 2¢ | 1262 | 4% | -$3,560.48 | -88% | 47 sec |
| Sell at 3¢ | 863 | 3% | -$3,552.03 | -88% | 48 sec |
| Sell at 5¢ | 599 | 2% | -$3,499.25 | -86% | 61 sec |
| Sell at 10¢ | 371 | 1% | -$3,360.59 | -83% | 65 sec |
| Sell at 25¢ | 197 | 1% | -$3,110.53 | -77% | 82 sec |
| Sell at 50¢ | 127 | 0% | -$2,821.35 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1468 | 8 | 11% | 4% | -48% | -81% | -82% |
| 2–5 min | 10706 | 57 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8452 | 31 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12734 | 28 | 1% | 0% | -68% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2410 | 12 | 5% | 2% | -37% | -88% | -88% |
| HYPE | 2403 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2400 | 13 | 5% | 2% | -32% | -84% | -83% |
| SOL | 2397 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2391 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2384 | 5 | 4% | 2% | -74% | -91% | -90% |
| NEAR | 2378 | 12 | 5% | 2% | -34% | -82% | -81% |
| XRP | 2378 | 9 | 3% | 1% | -53% | -89% | -89% |
| BTC | 2372 | 12 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1255 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1222 | 6 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1201 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1070 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1040 | 4 | 1% | 1% | -64% | -71% | -71% |
| EURUSD | 1003 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 995 | 5 | 2% | 1% | -53% | -87% | -86% |
| PALLADIUM | 959 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 945 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 926 | 5 | 1% | 1% | -50% | -98% | -97% |
| AUDUSD | 490 | 1 | 1% | 1% | -81% | -98% | -97% |
| USDCAD | 452 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 70 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 63 | 0 | 3% | 0% | -100% | -94% | -96% |
| 30YRRATE | 56 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 55 | 1 | 4% | 0% | +70% | +76% | +74% |
| 5YRRATE | 49 | 1 | 4% | 4% | +90% | -93% | -89% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16918 | 68 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16446 | 56 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3555 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3679 | 12 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5563 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6320 | 28 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2392 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 7805 | 25 | 4% | 2% | -62% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,722 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 2:29:51 PM | 2YRRATE | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:29:35 PM | NEAR | UP | 24 sec | -0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:29:35 PM | PALLADIUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:29:35 PM | ZEC | UP | 24 sec | -0.008% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:29:35 PM | EURUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:29:19 PM | NATGAS | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:29:02 PM | BRENT | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:29:02 PM | DOGE | UP | 57 sec | -0.131% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:29:02 PM | PLATINUM | DOWN | 57 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:29:02 PM | XRP | UP | 57 sec | -0.193% | 0¢ | ❌ Lost | $0.00 |
| 10/26 2:28:29 PM | BNB | UP | 1.5 min | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/26 2:28:29 PM | WTI | UP | 1.5 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 2:28:29 PM | SOL | UP | 1.5 min | -0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:28:13 PM | ETH | UP | 1.8 min | -0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:27:58 PM | SILVER | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:27:42 PM | HYPE | UP | 2.3 min | -0.468% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:27:42 PM | BTC | UP | 2.3 min | -0.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:14:58 PM | DOGE | DOWN | 1 sec | +0.006% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:14:58 PM | USDCAD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:14:58 PM | COPPER | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:14:58 PM | PLATINUM | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:14:58 PM | XRP | DOWN | 1 sec | +0.008% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:14:58 PM | WTI | UP | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 2:14:42 PM | 2YRRATE | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:14:42 PM | EURUSD | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:14:26 PM | 5YRRATE | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:14:26 PM | PALLADIUM | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:14:26 PM | SILVER | UP | 33 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:14:26 PM | GOLD | UP | 33 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:14:26 PM | 10YRRATE | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
