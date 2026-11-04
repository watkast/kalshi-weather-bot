# 15-Minute 1¢ Study

*Updated Wed Nov 4, 5:56 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3633 finished bets | 1% | $112.55 | +28% | +3.10¢ | $78.40 / $34.15 |

*Expect about **98 buys a day** (~$14.63/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3369 | $40.15 | +11% |
| Volatility model ≥ 2%, hold to the close | 6726 | $26.70 | +3% |
| Momentum model ≥ 2%, hold to the close | 5543 | -$51.75 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 45130 | 45111 | 167 (0%) | 1.07% | -$3,157.40 (-57%) | Hold to the close: -$3,157.40 (-57%) |

*In play or awaiting result: 18. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 27636 | 4.7% | 0.4% (108) | -679% | ❌ Worse |
| Momentum model | 27636 | 4.6% | 0.4% (108) | -706% | ❌ Worse |
| Mean-reversion model | 27636 | 8.1% | 0.4% (108) | -827% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27636 | 108 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6726 | 60 | +3% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3633 | 37 | +28% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2062 | 22 | +53% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5543 | 42 | -8% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3369 | 29 | +11% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2197 | 19 | +21% | -74% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11435 | 78 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8037 | 67 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5382 | 47 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27841 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10714 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6556 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 45111 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 167 | 0% | -$3,157.40 | -57% | — |
| Sell at 2¢ | 1770 | 4% | -$4,783.20 | -87% | 47 sec |
| Sell at 3¢ | 1213 | 3% | -$4,770.33 | -87% | 49 sec |
| Sell at 5¢ | 839 | 2% | -$4,670.05 | -85% | 63 sec |
| Sell at 10¢ | 507 | 1% | -$4,467.23 | -81% | 66 sec |
| Sell at 25¢ | 266 | 1% | -$4,138.94 | -75% | 83 sec |
| Sell at 50¢ | 170 | 0% | -$3,773.90 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2213 | 10 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 14524 | 79 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 11377 | 39 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 16986 | 39 | 1% | 0% | -67% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3119 | 13 | 5% | 3% | -46% | -88% | -88% |
| SOL | 3113 | 12 | 4% | 2% | -51% | -90% | -90% |
| BNB | 3106 | 17 | 5% | 2% | -31% | -85% | -84% |
| HYPE | 3105 | 9 | 5% | 2% | -64% | -89% | -87% |
| DOGE | 3093 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3087 | 12 | 7% | 3% | -53% | -85% | -85% |
| BTC | 3076 | 14 | 5% | 2% | -38% | -88% | -89% |
| NEAR | 3075 | 15 | 5% | 2% | -37% | -84% | -84% |
| XRP | 3067 | 12 | 3% | 1% | -51% | -89% | -89% |
| GOLD | 1661 | 5 | 5% | 2% | -63% | -81% | -83% |
| WTI | 1616 | 5 | 3% | 1% | -62% | -92% | -93% |
| SILVER | 1615 | 7 | 5% | 2% | -49% | -82% | -81% |
| PLATINUM | 1445 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1388 | 3 | 3% | 1% | -80% | -89% | -89% |
| COPPER | 1365 | 6 | 2% | 1% | -59% | -70% | -69% |
| GBPUSD | 1314 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1311 | 8 | 2% | 1% | -43% | -75% | -74% |
| USDJPY | 1296 | 5 | 2% | 1% | -64% | -97% | -97% |
| PALLADIUM | 1294 | 3 | 1% | 1% | -78% | -91% | -91% |
| AUDUSD | 846 | 4 | 2% | 1% | -56% | -86% | -86% |
| USDCAD | 812 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 407 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 246 | 1 | 5% | 2% | -62% | -54% | -51% |
| 30YRRATE | 227 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 222 | 2 | 4% | 0% | -16% | -10% | -9% |
| 5YRRATE | 205 | 1 | 5% | 2% | -54% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22900 | 89 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 22211 | 78 | 4% | 2% | -60% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4498 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4745 | 18 | 3% | 2% | -43% | -91% | -90% |
| 0.1–0.2% | 7197 | 25 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 8279 | 33 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3114 | 13 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11256 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 11054 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10598 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 12203 | 40 | 3% | 2% | -62% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,712 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 5:56:39 AM | SOL | UP | 3.4 min | -0.379% | — | In play | — |
| 11/4 5:56:39 AM | ETH | UP | 3.4 min | -0.276% | — | In play | — |
| 11/4 5:56:39 AM | NATGAS | DOWN | 3.4 min | — | — | In play | — |
| 11/4 5:56:24 AM | BNB | UP | 3.6 min | -0.243% | — | In play | — |
| 11/4 5:56:24 AM | NEAR | UP | 3.6 min | -0.849% | — | In play | — |
| 11/4 5:55:52 AM | 2YRRATE | UP | 4.1 min | — | — | In play | — |
| 11/4 5:54:47 AM | DOGE | UP | 5.2 min | -0.436% | — | In play | — |
| 11/4 5:54:32 AM | HYPE | UP | 5.5 min | -0.626% | — | In play | — |
| 11/4 5:52:58 AM | USDCAD | UP | 7.0 min | — | — | In play | — |
| 11/4 5:44:54 AM | 2YRRATE | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 5:44:38 AM | DOGE | DOWN | 21 sec | -0.023% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 5:44:38 AM | SOL | UP | 21 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 11/4 5:44:38 AM | BTC | UP | 21 sec | -0.011% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 5:44:38 AM | ETH | UP | 21 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 11/4 5:44:22 AM | USDCAD | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 5:44:06 AM | XRP | DOWN | 53 sec | +0.086% | 0¢ | ❌ Lost | $0.00 |
| 11/4 5:44:06 AM | BNB | UP | 53 sec | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 5:43:50 AM | ZEC | UP | 69 sec | -0.258% | 0¢ | ❌ Lost | $0.00 |
| 11/4 5:43:35 AM | NEAR | UP | 85 sec | -0.552% | 0¢ | ❌ Lost | $0.00 |
| 11/4 5:43:03 AM | COPPER | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 5:42:47 AM | SILVER | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 5:42:47 AM | HYPE | UP | 2.2 min | -0.377% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 5:42:47 AM | 5YRRATE | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 5:42:47 AM | 10YRRATE | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 5:42:31 AM | 30YRRATE | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 5:42:31 AM | WTI | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 5:42:31 AM | NATGAS | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 5:42:15 AM | EURUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 5:42:15 AM | AUDUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 5:41:43 AM | BRENT | DOWN | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
