# 15-Minute 1¢ Study

*Updated Mon Oct 26, 6:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2787 finished bets | 1% | $76.55 | +24% | +2.75¢ | $28.40 / $48.15 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2592 | $50.10 | +18% |
| Volatility model ≥ 2%, hold to the close | 5184 | -$18.20 | -3% |
| Momentum model ≥ 2%, hold to the close | 4311 | -$42.15 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33608 | 33600 | 125 (0%) | 1.07% | -$2,335.70 (-57%) | Hold to the close: -$2,335.70 (-57%) |

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
| Volatility model | 21445 | 4.6% | 0.4% (86) | -665% | ❌ Worse |
| Momentum model | 21445 | 4.5% | 0.4% (86) | -689% | ❌ Worse |
| Mean-reversion model | 21445 | 7.9% | 0.4% (86) | -807% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21445 | 86 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5184 | 44 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2787 | 28 | +24% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1579 | 18 | +60% | -67% | -65% | -62% |
| Momentum model ≥ 2% | 4311 | 33 | -8% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2592 | 24 | +18% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1691 | 16 | +30% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8683 | 57 | -28% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 6084 | 47 | -15% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4051 | 33 | -8% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21645 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7872 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4083 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33600 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 125 | 0% | -$2,335.70 | -57% | — |
| Sell at 2¢ | 1266 | 4% | -$3,588.54 | -88% | 47 sec |
| Sell at 3¢ | 866 | 3% | -$3,579.96 | -88% | 48 sec |
| Sell at 5¢ | 601 | 2% | -$3,527.05 | -86% | 61 sec |
| Sell at 10¢ | 371 | 1% | -$3,375.69 | -83% | 65 sec |
| Sell at 25¢ | 197 | 1% | -$3,125.63 | -77% | 82 sec |
| Sell at 50¢ | 127 | 0% | -$2,836.45 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1473 | 8 | 11% | 4% | -48% | -81% | -82% |
| 2–5 min | 10772 | 57 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8503 | 31 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12848 | 29 | 1% | 0% | -68% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2425 | 12 | 5% | 2% | -37% | -88% | -88% |
| HYPE | 2418 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2414 | 13 | 5% | 2% | -33% | -84% | -83% |
| SOL | 2411 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2405 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2399 | 5 | 4% | 2% | -74% | -91% | -90% |
| NEAR | 2393 | 12 | 5% | 2% | -35% | -82% | -82% |
| XRP | 2393 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2387 | 12 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1264 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1230 | 6 | 4% | 2% | -43% | -82% | -82% |
| WTI | 1211 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1074 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1046 | 4 | 1% | 1% | -64% | -71% | -71% |
| EURUSD | 1010 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 1006 | 5 | 2% | 1% | -54% | -87% | -87% |
| PALLADIUM | 963 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 952 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 938 | 5 | 1% | 1% | -50% | -98% | -97% |
| AUDUSD | 497 | 2 | 1% | 1% | -62% | -98% | -96% |
| USDCAD | 459 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 78 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 63 | 0 | 3% | 0% | -100% | -94% | -96% |
| 2YRRATE | 57 | 1 | 4% | 0% | +64% | +70% | +68% |
| 30YRRATE | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 50 | 1 | 4% | 4% | +87% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17026 | 68 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16574 | 57 | 4% | 2% | -60% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3576 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3706 | 12 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5604 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6358 | 28 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2397 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 8996 | 30 | 3% | 2% | -62% | -90% | -90% |

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
| 10/26 6:14:12 PM | PALLADIUM | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:14:12 PM | XRP | DOWN | 48 sec | +0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:14:12 PM | AUDUSD | DOWN | 48 sec | — | 8¢ | ✅ Won | $13.85 |
| 10/26 6:13:40 PM | BRENT | UP | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:13:40 PM | NATGAS | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:13:24 PM | GBPUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:13:08 PM | EURUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:13:08 PM | USDJPY | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:13:08 PM | USDCAD | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:12:52 PM | PLATINUM | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:12:52 PM | SOL | DOWN | 2.1 min | +0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:12:36 PM | HYPE | DOWN | 2.4 min | +0.156% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:12:36 PM | NEAR | DOWN | 2.4 min | +0.368% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:12:20 PM | WTI | UP | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:12:20 PM | DOGE | DOWN | 2.7 min | +0.219% | 0¢ | ❌ Lost | $0.00 |
| 10/26 6:12:20 PM | ETH | DOWN | 2.7 min | +0.181% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:12:20 PM | COPPER | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 6:11:46 PM | BTC | DOWN | 3.2 min | +0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:11:46 PM | ZEC | DOWN | 3.2 min | +0.449% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:10:10 PM | SILVER | DOWN | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:09:36 PM | BNB | DOWN | 5.4 min | +0.217% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 6:08:16 PM | GOLD | DOWN | 6.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:51 PM | USDJPY | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:51 PM | BTC | UP | 8 sec | +0.001% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:51 PM | ZEC | UP | 8 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/26 5:59:35 PM | PALLADIUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:35 PM | HYPE | UP | 24 sec | -0.054% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:35 PM | COPPER | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:19 PM | EURUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:19 PM | ETH | DOWN | 40 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
