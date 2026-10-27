# 15-Minute 1¢ Study

*Updated Mon Oct 26, 6:11 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

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
| Volatility model ≥ 2%, hold to the close | 5182 | -$17.90 | -3% |
| Momentum model ≥ 2%, hold to the close | 4309 | -$41.85 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33589 | 33578 | 124 (0%) | 1.07% | -$2,346.55 (-57%) | Hold to the close: -$2,346.55 (-57%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 21436 | 4.6% | 0.4% (86) | -665% | ❌ Worse |
| Momentum model | 21436 | 4.5% | 0.4% (86) | -689% | ❌ Worse |
| Mean-reversion model | 21436 | 7.9% | 0.4% (86) | -807% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21436 | 86 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5182 | 44 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2787 | 28 | +24% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1579 | 18 | +60% | -67% | -65% | -62% |
| Momentum model ≥ 2% | 4309 | 33 | -8% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2592 | 24 | +18% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1691 | 16 | +30% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8681 | 57 | -28% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 6082 | 47 | -15% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4050 | 33 | -8% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21636 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7864 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4078 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33578 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 124 | 0% | -$2,346.55 | -57% | — |
| Sell at 2¢ | 1265 | 4% | -$3,585.65 | -88% | 47 sec |
| Sell at 3¢ | 865 | 3% | -$3,577.20 | -88% | 48 sec |
| Sell at 5¢ | 600 | 2% | -$3,524.55 | -86% | 61 sec |
| Sell at 10¢ | 371 | 1% | -$3,386.54 | -83% | 65 sec |
| Sell at 25¢ | 197 | 1% | -$3,136.48 | -77% | 82 sec |
| Sell at 50¢ | 127 | 0% | -$2,847.30 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1471 | 8 | 11% | 4% | -48% | -80% | -82% |
| 2–5 min | 10761 | 57 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8497 | 31 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12845 | 28 | 1% | 0% | -69% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2424 | 12 | 5% | 2% | -37% | -88% | -88% |
| HYPE | 2417 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2413 | 13 | 5% | 2% | -33% | -84% | -83% |
| SOL | 2410 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2404 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2398 | 5 | 4% | 2% | -74% | -91% | -90% |
| NEAR | 2392 | 12 | 5% | 2% | -35% | -82% | -82% |
| XRP | 2392 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2386 | 12 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1263 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1229 | 6 | 4% | 2% | -43% | -82% | -82% |
| WTI | 1210 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1073 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1045 | 4 | 1% | 1% | -64% | -71% | -71% |
| EURUSD | 1009 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 1005 | 5 | 2% | 1% | -54% | -87% | -87% |
| PALLADIUM | 962 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 951 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 937 | 5 | 1% | 1% | -50% | -98% | -97% |
| AUDUSD | 496 | 1 | 1% | 1% | -81% | -98% | -97% |
| USDCAD | 458 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 77 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 63 | 0 | 3% | 0% | -100% | -94% | -96% |
| 2YRRATE | 57 | 1 | 4% | 0% | +64% | +70% | +68% |
| 30YRRATE | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 50 | 1 | 4% | 4% | +87% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17022 | 68 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16556 | 56 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3576 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3705 | 12 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5600 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6354 | 28 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2397 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
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
| 10/26 6:10:10 PM | SILVER | DOWN | 4.8 min | — | — | In play | — |
| 10/26 6:09:36 PM | BNB | DOWN | 5.4 min | +0.217% | — | In play | — |
| 10/26 6:08:16 PM | GOLD | DOWN | 6.7 min | — | — | In play | — |
| 10/26 5:59:51 PM | USDJPY | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:51 PM | BTC | UP | 8 sec | +0.001% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:51 PM | ZEC | UP | 8 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/26 5:59:35 PM | PALLADIUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:35 PM | HYPE | UP | 24 sec | -0.054% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:35 PM | COPPER | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:19 PM | EURUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:59:19 PM | ETH | DOWN | 40 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/26 5:59:03 PM | BNB | DOWN | 56 sec | +0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/26 5:59:03 PM | SOL | DOWN | 56 sec | +0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/26 5:59:03 PM | NATGAS | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:58:31 PM | DOGE | DOWN | 88 sec | +0.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:58:31 PM | NEAR | DOWN | 88 sec | +0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:58:15 PM | WTI | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:58:15 PM | PLATINUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:57:27 PM | XRP | DOWN | 2.5 min | +0.484% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:57:11 PM | AUDUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:57:09 PM | SILVER | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:56:53 PM | GBPUSD | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:56:03 PM | GOLD | UP | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:44:52 PM | WTI | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:44:52 PM | BRENT | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:44:04 PM | BNB | DOWN | 56 sec | +0.001% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:43:46 PM | PLATINUM | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:43:30 PM | GOLD | UP | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:43:14 PM | NEAR | DOWN | 1.8 min | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:42:27 PM | USDJPY | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
