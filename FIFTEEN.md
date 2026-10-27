# 15-Minute 1¢ Study

*Updated Mon Oct 26, 11:34 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2807 finished bets | 1% | $74.60 | +24% | +2.66¢ | $55.05 / $19.55 |

*Expect about **97 buys a day** (~$14.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2612 | $48.30 | +17% |
| Volatility model ≥ 2%, hold to the close | 5217 | -$21.65 | -3% |
| Momentum model ≥ 2%, hold to the close | 4337 | -$44.55 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33977 | 33969 | 126 (0%) | 1.07% | -$2,366.85 (-57%) | Hold to the close: -$2,366.85 (-57%) |

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
| Volatility model | 21627 | 4.6% | 0.4% (86) | -671% | ❌ Worse |
| Momentum model | 21627 | 4.6% | 0.4% (86) | -696% | ❌ Worse |
| Mean-reversion model | 21627 | 7.9% | 0.4% (86) | -813% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21627 | 86 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5217 | 44 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2807 | 28 | +24% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1593 | 18 | +59% | -67% | -65% | -63% |
| Momentum model ≥ 2% | 4337 | 33 | -9% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2612 | 24 | +17% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1707 | 16 | +29% | -71% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8757 | 57 | -29% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6130 | 47 | -16% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4082 | 33 | -9% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21827 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7987 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4155 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33969 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 126 | 0% | -$2,366.85 | -57% | — |
| Sell at 2¢ | 1275 | 4% | -$3,631.35 | -88% | 47 sec |
| Sell at 3¢ | 874 | 3% | -$3,621.99 | -88% | 48 sec |
| Sell at 5¢ | 606 | 2% | -$3,568.95 | -86% | 62 sec |
| Sell at 10¢ | 373 | 1% | -$3,418.22 | -83% | 65 sec |
| Sell at 25¢ | 199 | 1% | -$3,164.16 | -77% | 83 sec |
| Sell at 50¢ | 129 | 0% | -$2,868.10 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1483 | 8 | 11% | 4% | -49% | -81% | -82% |
| 2–5 min | 10903 | 58 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8602 | 31 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12977 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2445 | 12 | 5% | 2% | -37% | -88% | -88% |
| HYPE | 2437 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2435 | 13 | 5% | 2% | -33% | -84% | -83% |
| SOL | 2432 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2425 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2420 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2414 | 12 | 5% | 2% | -35% | -82% | -82% |
| XRP | 2412 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2407 | 12 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1282 | 5 | 4% | 2% | -54% | -81% | -83% |
| SILVER | 1246 | 6 | 4% | 2% | -44% | -82% | -82% |
| WTI | 1226 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1095 | 0 | 2% | 1% | -100% | -97% | -97% |
| COPPER | 1058 | 4 | 1% | 1% | -65% | -71% | -71% |
| EURUSD | 1026 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1016 | 5 | 2% | 1% | -54% | -87% | -87% |
| PALLADIUM | 976 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 969 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 952 | 5 | 1% | 1% | -51% | -98% | -97% |
| AUDUSD | 511 | 2 | 1% | 1% | -63% | -98% | -96% |
| USDCAD | 470 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 88 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 63 | 0 | 3% | 0% | -100% | -94% | -96% |
| 2YRRATE | 57 | 1 | 4% | 0% | +64% | +70% | +68% |
| 30YRRATE | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 50 | 1 | 4% | 4% | +87% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17245 | 69 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16724 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3604 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3737 | 12 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5655 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6418 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2409 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9365 | 31 | 3% | 2% | -62% | -90% | -90% |

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
| 10/26 11:29:58 PM | NATGAS | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:29:42 PM | GOLD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:29:11 PM | BNB | UP | 49 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/26 11:29:11 PM | GBPUSD | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:29:11 PM | BTC | UP | 49 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/26 11:28:53 PM | PALLADIUM | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:28:37 PM | XRP | UP | 83 sec | -0.170% | 0¢ | ❌ Lost | $0.00 |
| 10/26 11:28:37 PM | USDCAD | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:28:21 PM | SOL | UP | 1.6 min | -0.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 11:28:21 PM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:28:21 PM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:28:21 PM | ETH | UP | 1.6 min | -0.138% | 0¢ | ❌ Lost | $0.00 |
| 10/26 11:28:21 PM | SILVER | UP | 1.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 11:27:50 PM | AUDUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:27:34 PM | COPPER | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:27:18 PM | ZEC | UP | 2.7 min | -0.355% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:27:02 PM | DOGE | UP | 3.0 min | -0.198% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:27:02 PM | HYPE | UP | 3.0 min | -0.250% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 11:27:02 PM | NEAR | UP | 3.0 min | -0.531% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 11:26:47 PM | PLATINUM | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:14:35 PM | SOL | DOWN | 24 sec | +0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/26 11:14:35 PM | HYPE | DOWN | 24 sec | +0.010% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:14:21 PM | XRP | DOWN | 39 sec | +0.000% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 11:13:49 PM | USDCAD | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:13:49 PM | GOLD | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:13:49 PM | NEAR | DOWN | 71 sec | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 11:13:49 PM | ETH | DOWN | 71 sec | +0.078% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 11:13:49 PM | PALLADIUM | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:13:22 PM | AUDUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 11:13:22 PM | ZEC | DOWN | 1.6 min | +0.270% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
