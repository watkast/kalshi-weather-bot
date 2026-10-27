# 15-Minute 1¢ Study

*Updated Mon Oct 26, 7:32 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2793 finished bets | 1% | $76.10 | +24% | +2.72¢ | $27.95 / $48.15 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

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
| 33696 | 33688 | 126 (0%) | 1.07% | -$2,331.75 (-57%) | Hold to the close: -$2,331.75 (-57%) |

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
| Volatility model | 21487 | 4.6% | 0.4% (86) | -667% | ❌ Worse |
| Momentum model | 21487 | 4.5% | 0.4% (86) | -692% | ❌ Worse |
| Mean-reversion model | 21487 | 7.9% | 0.4% (86) | -810% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21487 | 86 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5193 | 44 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2793 | 28 | +24% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1584 | 18 | +60% | -67% | -65% | -62% |
| Momentum model ≥ 2% | 4317 | 33 | -8% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2597 | 24 | +17% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1695 | 16 | +30% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8700 | 57 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6100 | 47 | -15% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4061 | 33 | -8% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21687 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7899 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4102 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33688 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 126 | 0% | -$2,331.75 | -57% | — |
| Sell at 2¢ | 1270 | 4% | -$3,597.55 | -88% | 47 sec |
| Sell at 3¢ | 869 | 3% | -$3,588.84 | -88% | 48 sec |
| Sell at 5¢ | 603 | 2% | -$3,535.80 | -86% | 61 sec |
| Sell at 10¢ | 373 | 1% | -$3,383.12 | -83% | 65 sec |
| Sell at 25¢ | 199 | 1% | -$3,129.06 | -76% | 83 sec |
| Sell at 50¢ | 129 | 0% | -$2,833.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1477 | 8 | 11% | 4% | -48% | -81% | -82% |
| 2–5 min | 10801 | 58 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8518 | 31 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12888 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2429 | 12 | 5% | 2% | -37% | -89% | -88% |
| HYPE | 2422 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2419 | 13 | 5% | 2% | -33% | -84% | -83% |
| SOL | 2416 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2410 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2404 | 5 | 4% | 2% | -74% | -91% | -90% |
| NEAR | 2398 | 12 | 5% | 2% | -35% | -82% | -82% |
| XRP | 2398 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2391 | 12 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1268 | 5 | 4% | 2% | -53% | -81% | -83% |
| SILVER | 1234 | 6 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1215 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1079 | 0 | 1% | 1% | -100% | -97% | -98% |
| COPPER | 1048 | 4 | 1% | 1% | -64% | -71% | -71% |
| EURUSD | 1014 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 1008 | 5 | 2% | 1% | -54% | -87% | -87% |
| PALLADIUM | 967 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 956 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 941 | 5 | 1% | 1% | -50% | -98% | -97% |
| AUDUSD | 501 | 2 | 1% | 1% | -63% | -98% | -96% |
| USDCAD | 463 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 80 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 63 | 0 | 3% | 0% | -100% | -94% | -96% |
| 2YRRATE | 57 | 1 | 4% | 0% | +64% | +70% | +68% |
| 30YRRATE | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 50 | 1 | 4% | 4% | +87% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17082 | 69 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 16606 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3585 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3716 | 12 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5609 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6371 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2402 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9084 | 31 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,720 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 7:29:20 PM | PALLADIUM | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:29:20 PM | XRP | UP | 40 sec | -0.222% | 0¢ | ❌ Lost | $0.00 |
| 10/26 7:29:20 PM | USDCAD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:28:46 PM | GBPUSD | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:27:26 PM | EURUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:27:10 PM | AUDUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:25:51 PM | PLATINUM | UP | 4.2 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/26 7:25:51 PM | HYPE | UP | 4.2 min | -0.488% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:25:33 PM | GOLD | UP | 4.5 min | — | 91¢ | ✅ Won | $13.85 |
| 10/26 7:25:17 PM | SILVER | UP | 4.7 min | — | 57¢ | ❌ Lost | -$0.15 |
| 10/26 7:25:01 PM | NEAR | UP | 5.0 min | -1.005% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:25:01 PM | DOGE | UP | 5.0 min | -0.338% | 4¢ | ❌ Lost | -$0.15 |
| 10/26 7:25:01 PM | SOL | UP | 5.0 min | -0.365% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:24:46 PM | ZEC | UP | 5.2 min | -0.855% | 2¢ | ❌ Lost | -$0.15 |
| 10/26 7:23:57 PM | ETH | UP | 6.0 min | -0.479% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:23:42 PM | BNB | UP | 6.3 min | -0.297% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:23:42 PM | BTC | UP | 6.3 min | -0.303% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
