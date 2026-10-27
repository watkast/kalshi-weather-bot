# 15-Minute 1¢ Study

*Updated Mon Oct 26, 8:49 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2793 finished bets | 1% | $76.10 | +24% | +2.72¢ | $27.95 / $48.15 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2598 | $49.65 | +17% |
| Volatility model ≥ 2%, hold to the close | 5197 | -$19.40 | -3% |
| Momentum model ≥ 2%, hold to the close | 4320 | -$43.05 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33782 | 33773 | 126 (0%) | 1.07% | -$2,342.25 (-57%) | Hold to the close: -$2,342.25 (-57%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 21529 | 4.6% | 0.4% (86) | -667% | ❌ Worse |
| Momentum model | 21529 | 4.5% | 0.4% (86) | -692% | ❌ Worse |
| Mean-reversion model | 21529 | 7.9% | 0.4% (86) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21529 | 86 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5197 | 44 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2793 | 28 | +24% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1584 | 18 | +60% | -67% | -65% | -62% |
| Momentum model ≥ 2% | 4320 | 33 | -9% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2598 | 24 | +17% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1695 | 16 | +30% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8715 | 57 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6108 | 47 | -15% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4067 | 33 | -8% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21729 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7925 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4119 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33773 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 126 | 0% | -$2,342.25 | -57% | — |
| Sell at 2¢ | 1272 | 4% | -$3,607.53 | -88% | 47 sec |
| Sell at 3¢ | 871 | 3% | -$3,598.56 | -88% | 48 sec |
| Sell at 5¢ | 605 | 2% | -$3,545.00 | -86% | 61 sec |
| Sell at 10¢ | 373 | 1% | -$3,393.62 | -83% | 65 sec |
| Sell at 25¢ | 199 | 1% | -$3,139.56 | -76% | 83 sec |
| Sell at 50¢ | 129 | 0% | -$2,843.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1481 | 8 | 11% | 4% | -48% | -81% | -82% |
| 2–5 min | 10825 | 58 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8540 | 31 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12923 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2434 | 12 | 5% | 3% | -37% | -88% | -88% |
| HYPE | 2427 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2424 | 13 | 5% | 2% | -33% | -84% | -83% |
| SOL | 2421 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2414 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2409 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2402 | 12 | 5% | 2% | -35% | -82% | -82% |
| XRP | 2402 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2396 | 12 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1272 | 5 | 4% | 2% | -53% | -81% | -83% |
| SILVER | 1238 | 6 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1219 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1084 | 0 | 1% | 1% | -100% | -97% | -98% |
| COPPER | 1051 | 4 | 1% | 1% | -64% | -71% | -71% |
| EURUSD | 1018 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 1012 | 5 | 2% | 1% | -54% | -87% | -87% |
| PALLADIUM | 968 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 960 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 946 | 5 | 1% | 1% | -51% | -98% | -97% |
| AUDUSD | 503 | 2 | 1% | 1% | -63% | -98% | -96% |
| USDCAD | 465 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 81 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 63 | 0 | 3% | 0% | -100% | -94% | -96% |
| 2YRRATE | 57 | 1 | 4% | 0% | +64% | +70% | +68% |
| 30YRRATE | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 50 | 1 | 4% | 4% | +87% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17131 | 69 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16642 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3587 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3725 | 12 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5617 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6389 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2407 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9169 | 31 | 3% | 2% | -61% | -90% | -90% |

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
| 10/26 8:44:49 PM | SILVER | UP | 10 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 8:44:49 PM | GBPUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:44:49 PM | ETH | DOWN | 10 sec | +0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/26 8:44:49 PM | EURUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:44:49 PM | NEAR | DOWN | 10 sec | -0.103% | 0¢ | In play | — |
| 10/26 8:44:49 PM | GOLD | UP | 10 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 8:44:33 PM | NATGAS | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:44:33 PM | WTI | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:44:33 PM | ZEC | DOWN | 26 sec | +0.094% | 0¢ | ❌ Lost | $0.00 |
| 10/26 8:44:33 PM | HYPE | UP | 26 sec | -0.079% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:44:33 PM | PLATINUM | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:44:33 PM | BTC | UP | 26 sec | -0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/26 8:44:33 PM | USDJPY | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:44:17 PM | DOGE | DOWN | 43 sec | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:43:58 PM | BNB | UP | 62 sec | -0.088% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:43:58 PM | SOL | UP | 62 sec | -0.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:43:42 PM | AUDUSD | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:29:45 PM | NATGAS | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:29:45 PM | USDJPY | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:29:29 PM | GOLD | UP | 30 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:28:56 PM | XRP | UP | 63 sec | -0.192% | 0¢ | ❌ Lost | $0.00 |
| 10/26 8:28:24 PM | WTI | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:28:24 PM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:28:24 PM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:28:08 PM | ZEC | UP | 1.9 min | -0.331% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:27:51 PM | BTC | UP | 2.1 min | -0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:27:35 PM | SOL | UP | 2.4 min | -0.209% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:27:19 PM | DOGE | UP | 2.7 min | -0.229% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:27:19 PM | NEAR | UP | 2.7 min | -0.499% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:27:03 PM | ETH | UP | 3.0 min | -0.213% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
