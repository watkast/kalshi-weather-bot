# 15-Minute 1¢ Study

*Updated Mon Oct 26, 10:32 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2799 finished bets | 1% | $75.65 | +24% | +2.70¢ | $27.50 / $48.15 |

*Expect about **97 buys a day** (~$14.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2604 | $49.20 | +17% |
| Volatility model ≥ 2%, hold to the close | 5207 | -$20.45 | -3% |
| Momentum model ≥ 2%, hold to the close | 4327 | -$43.50 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33899 | 33891 | 126 (0%) | 1.07% | -$2,356.80 (-57%) | Hold to the close: -$2,356.80 (-57%) |

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
| Volatility model | 21591 | 4.6% | 0.4% (86) | -671% | ❌ Worse |
| Momentum model | 21591 | 4.5% | 0.4% (86) | -696% | ❌ Worse |
| Mean-reversion model | 21591 | 7.9% | 0.4% (86) | -814% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21591 | 86 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5207 | 44 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2799 | 28 | +24% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1589 | 18 | +59% | -67% | -65% | -63% |
| Momentum model ≥ 2% | 4327 | 33 | -9% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2604 | 24 | +17% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1700 | 16 | +30% | -71% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8741 | 57 | -29% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6120 | 47 | -15% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4077 | 33 | -9% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21791 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7960 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4140 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33891 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 126 | 0% | -$2,356.80 | -57% | — |
| Sell at 2¢ | 1275 | 4% | -$3,621.30 | -88% | 47 sec |
| Sell at 3¢ | 874 | 3% | -$3,611.94 | -88% | 48 sec |
| Sell at 5¢ | 606 | 2% | -$3,558.90 | -86% | 62 sec |
| Sell at 10¢ | 373 | 1% | -$3,408.17 | -83% | 65 sec |
| Sell at 25¢ | 199 | 1% | -$3,154.11 | -77% | 83 sec |
| Sell at 50¢ | 129 | 0% | -$2,858.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1483 | 8 | 11% | 4% | -49% | -81% | -82% |
| 2–5 min | 10876 | 58 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8572 | 31 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12956 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2441 | 12 | 5% | 2% | -37% | -88% | -88% |
| HYPE | 2433 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2431 | 13 | 5% | 2% | -33% | -84% | -83% |
| SOL | 2428 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2421 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2416 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2410 | 12 | 5% | 2% | -35% | -82% | -82% |
| XRP | 2408 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2403 | 12 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1278 | 5 | 4% | 2% | -53% | -81% | -83% |
| SILVER | 1242 | 6 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1224 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1091 | 0 | 2% | 1% | -100% | -97% | -97% |
| COPPER | 1054 | 4 | 1% | 1% | -65% | -71% | -71% |
| EURUSD | 1023 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1013 | 5 | 2% | 1% | -54% | -87% | -87% |
| PALLADIUM | 972 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 966 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 950 | 5 | 1% | 1% | -51% | -98% | -97% |
| AUDUSD | 507 | 2 | 1% | 1% | -63% | -98% | -96% |
| USDCAD | 467 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 86 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 63 | 0 | 3% | 0% | -100% | -94% | -96% |
| 2YRRATE | 57 | 1 | 4% | 0% | +64% | +70% | +68% |
| 30YRRATE | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 50 | 1 | 4% | 4% | +87% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17195 | 69 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16696 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3598 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3729 | 12 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5640 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6412 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2408 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9287 | 31 | 3% | 2% | -62% | -90% | -90% |

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
| 10/26 10:29:50 PM | GOLD | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:29:50 PM | NEAR | UP | 9 sec | -0.106% | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:29:50 PM | SOL | DOWN | 9 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:29:34 PM | ETH | UP | 25 sec | -0.063% | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:28:59 PM | ZEC | UP | 61 sec | -0.202% | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:28:27 PM | AUDUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:28:12 PM | BRENT | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:28:12 PM | HYPE | UP | 1.8 min | -0.167% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:27:23 PM | WTI | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:27:23 PM | USDJPY | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:27:07 PM | BTC | UP | 2.9 min | -0.112% | 3¢ | ❌ Lost | -$0.15 |
| 10/26 10:26:49 PM | DOGE | UP | 3.2 min | -0.217% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:26:49 PM | BNB | UP | 3.2 min | -0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:22:25 PM | PLATINUM | DOWN | 7.6 min | — | 9¢ | ❌ Lost | -$0.15 |
| 10/26 10:14:56 PM | NEAR | UP | 3 sec | -0.075% | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:14:56 PM | SOL | UP | 3 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:14:40 PM | BNB | UP | 19 sec | -0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:14:40 PM | USDJPY | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:14:25 PM | COPPER | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:14:25 PM | ETH | DOWN | 34 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:14:25 PM | XRP | DOWN | 34 sec | -0.008% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:14:25 PM | ZEC | DOWN | 34 sec | +0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:14:25 PM | BTC | DOWN | 34 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:14:06 PM | PLATINUM | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:14:06 PM | BRENT | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:14:06 PM | DOGE | DOWN | 54 sec | +0.077% | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:14:06 PM | GBPUSD | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:13:50 PM | HYPE | DOWN | 70 sec | +0.107% | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:13:34 PM | SILVER | DOWN | 86 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:13:19 PM | WTI | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
