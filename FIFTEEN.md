# 15-Minute 1¢ Study

*Updated Tue Oct 27, 12:46 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2810 finished bets | 1% | $74.45 | +23% | +2.65¢ | $54.90 / $19.55 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2619 | $47.55 | +16% |
| Volatility model ≥ 2%, hold to the close | 5226 | -$22.70 | -4% |
| Momentum model ≥ 2%, hold to the close | 4346 | -$45.60 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34070 | 34049 | 126 (0%) | 1.07% | -$2,377.05 (-57%) | Hold to the close: -$2,377.05 (-57%) |

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
| Volatility model | 21669 | 4.6% | 0.4% (86) | -672% | ❌ Worse |
| Momentum model | 21669 | 4.6% | 0.4% (86) | -697% | ❌ Worse |
| Mean-reversion model | 21669 | 7.9% | 0.4% (86) | -815% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21669 | 86 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5226 | 44 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2810 | 28 | +23% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1596 | 18 | +59% | -67% | -65% | -63% |
| Momentum model ≥ 2% | 4346 | 33 | -9% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2619 | 24 | +16% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1711 | 16 | +29% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8772 | 57 | -29% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6143 | 47 | -16% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4093 | 33 | -9% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21869 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8013 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4167 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34049 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 126 | 0% | -$2,377.05 | -57% | — |
| Sell at 2¢ | 1278 | 4% | -$3,640.77 | -88% | 47 sec |
| Sell at 3¢ | 876 | 3% | -$3,631.41 | -88% | 48 sec |
| Sell at 5¢ | 606 | 2% | -$3,579.15 | -86% | 62 sec |
| Sell at 10¢ | 373 | 1% | -$3,428.42 | -83% | 65 sec |
| Sell at 25¢ | 199 | 1% | -$3,174.36 | -77% | 83 sec |
| Sell at 50¢ | 129 | 0% | -$2,878.30 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1485 | 8 | 11% | 4% | -49% | -81% | -82% |
| 2–5 min | 10933 | 58 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8629 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 12998 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2450 | 12 | 5% | 2% | -38% | -89% | -88% |
| HYPE | 2442 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2440 | 13 | 5% | 2% | -33% | -84% | -83% |
| SOL | 2436 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2430 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2425 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2418 | 12 | 5% | 2% | -35% | -82% | -82% |
| XRP | 2416 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2412 | 12 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1285 | 5 | 4% | 2% | -54% | -81% | -83% |
| SILVER | 1249 | 6 | 4% | 2% | -44% | -82% | -82% |
| WTI | 1229 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1099 | 0 | 2% | 1% | -100% | -97% | -97% |
| COPPER | 1062 | 4 | 1% | 1% | -65% | -71% | -71% |
| EURUSD | 1029 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1018 | 5 | 2% | 1% | -54% | -87% | -87% |
| PALLADIUM | 980 | 2 | 1% | 0% | -81% | -89% | -89% |
| GBPUSD | 970 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 956 | 5 | 1% | 1% | -51% | -98% | -97% |
| AUDUSD | 513 | 2 | 1% | 1% | -64% | -98% | -96% |
| USDCAD | 472 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 91 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 63 | 0 | 3% | 0% | -100% | -94% | -96% |
| 2YRRATE | 57 | 1 | 4% | 0% | +64% | +70% | +68% |
| 30YRRATE | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 50 | 1 | 4% | 4% | +87% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17281 | 69 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16768 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3608 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3748 | 12 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5665 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6434 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2410 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8363 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,718 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 12:44:58 AM | GOLD | UP | 2 sec | — | 0¢ | In play | — |
| 10/27 12:44:58 AM | PLATINUM | UP | 2 sec | — | 0¢ | In play | — |
| 10/27 12:44:42 AM | HYPE | UP | 18 sec | -0.032% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 12:44:26 AM | BTC | UP | 34 sec | -0.054% | 0¢ | ❌ Lost | $0.00 |
| 10/27 12:44:26 AM | AUDUSD | UP | 34 sec | — | 0¢ | In play | — |
| 10/27 12:44:26 AM | ETH | UP | 34 sec | -0.053% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:44:26 AM | EURUSD | UP | 34 sec | — | 0¢ | In play | — |
| 10/27 12:44:11 AM | USDCAD | DOWN | 48 sec | — | 0¢ | In play | — |
| 10/27 12:44:11 AM | SILVER | UP | 48 sec | — | 1¢ | In play | — |
| 10/27 12:44:11 AM | BNB | UP | 48 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/27 12:44:11 AM | NATGAS | UP | 48 sec | — | 0¢ | In play | — |
| 10/27 12:43:55 AM | DOGE | DOWN | 64 sec | +0.093% | 3¢ | ❌ Lost | -$0.15 |
| 10/27 12:43:55 AM | BRENT | DOWN | 64 sec | — | 0¢ | In play | — |
| 10/27 12:43:39 AM | USDJPY | UP | 80 sec | — | 0¢ | In play | — |
| 10/27 12:43:39 AM | NEAR | DOWN | 80 sec | +0.161% | 1¢ | In play | — |
| 10/27 12:43:23 AM | SOL | DOWN | 1.6 min | +0.096% | 0¢ | In play | — |
| 10/27 12:42:33 AM | ZEC | DOWN | 2.5 min | +0.328% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 12:42:02 AM | XRP | DOWN | 3.0 min | +0.146% | 1¢ | In play | — |
| 10/27 12:40:41 AM | WTI | DOWN | 4.3 min | — | 1¢ | In play | — |
| 10/27 12:29:44 AM | EURUSD | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:29:28 AM | USDJPY | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:29:13 AM | BRENT | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:28:55 AM | AUDUSD | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:28:55 AM | HYPE | UP | 65 sec | -0.124% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:28:23 AM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:28:08 AM | COPPER | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:28:08 AM | USDCAD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:28:08 AM | GOLD | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 12:28:08 AM | WTI | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 12:27:51 AM | NEAR | UP | 2.1 min | -0.373% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
