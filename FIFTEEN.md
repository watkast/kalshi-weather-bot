# 15-Minute 1¢ Study

*Updated Mon Oct 26, 9:51 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2797 finished bets | 1% | $75.80 | +24% | +2.71¢ | $27.65 / $48.15 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2602 | $49.35 | +17% |
| Volatility model ≥ 2%, hold to the close | 5204 | -$20.15 | -3% |
| Momentum model ≥ 2%, hold to the close | 4325 | -$43.35 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33850 | 33842 | 126 (0%) | 1.07% | -$2,351.40 (-57%) | Hold to the close: -$2,351.40 (-57%) |

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
| Volatility model | 21565 | 4.6% | 0.4% (86) | -670% | ❌ Worse |
| Momentum model | 21565 | 4.5% | 0.4% (86) | -694% | ❌ Worse |
| Mean-reversion model | 21565 | 7.9% | 0.4% (86) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21565 | 86 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5204 | 44 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2797 | 28 | +24% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1587 | 18 | +60% | -67% | -65% | -63% |
| Momentum model ≥ 2% | 4325 | 33 | -9% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2602 | 24 | +17% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1698 | 16 | +30% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8730 | 57 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6117 | 47 | -15% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4075 | 33 | -9% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21765 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7944 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4133 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33842 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 126 | 0% | -$2,351.40 | -57% | — |
| Sell at 2¢ | 1273 | 4% | -$3,616.42 | -88% | 47 sec |
| Sell at 3¢ | 872 | 3% | -$3,607.32 | -88% | 48 sec |
| Sell at 5¢ | 605 | 2% | -$3,554.15 | -86% | 61 sec |
| Sell at 10¢ | 373 | 1% | -$3,402.77 | -83% | 65 sec |
| Sell at 25¢ | 199 | 1% | -$3,148.71 | -77% | 83 sec |
| Sell at 50¢ | 129 | 0% | -$2,852.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1482 | 8 | 11% | 4% | -49% | -81% | -82% |
| 2–5 min | 10858 | 58 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8560 | 31 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12938 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2438 | 12 | 5% | 3% | -37% | -88% | -88% |
| HYPE | 2430 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2428 | 13 | 5% | 2% | -33% | -84% | -83% |
| SOL | 2425 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2418 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2413 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2407 | 12 | 5% | 2% | -35% | -82% | -82% |
| XRP | 2406 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2400 | 12 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1275 | 5 | 4% | 2% | -53% | -81% | -83% |
| SILVER | 1240 | 6 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1221 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1088 | 0 | 1% | 1% | -100% | -97% | -98% |
| COPPER | 1053 | 4 | 1% | 1% | -65% | -71% | -71% |
| EURUSD | 1022 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1013 | 5 | 2% | 1% | -54% | -87% | -87% |
| PALLADIUM | 971 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 964 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 948 | 5 | 1% | 1% | -51% | -98% | -97% |
| AUDUSD | 505 | 2 | 1% | 1% | -63% | -98% | -96% |
| USDCAD | 467 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 83 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 63 | 0 | 3% | 0% | -100% | -94% | -96% |
| 2YRRATE | 57 | 1 | 4% | 0% | +64% | +70% | +68% |
| 30YRRATE | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 50 | 1 | 4% | 4% | +87% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17162 | 69 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16680 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3592 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3726 | 12 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5631 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6404 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2408 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9238 | 31 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,721 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 9:44:48 PM | NEAR | DOWN | 11 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/26 9:44:32 PM | HYPE | DOWN | 27 sec | -0.022% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:43:43 PM | BRENT | DOWN | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:43:43 PM | WTI | DOWN | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:43:11 PM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:42:55 PM | SOL | DOWN | 2.1 min | +0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 9:42:39 PM | USDCAD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:42:39 PM | PALLADIUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:42:23 PM | USDJPY | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:42:07 PM | EURUSD | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:42:07 PM | AUDUSD | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:41:36 PM | ZEC | DOWN | 3.4 min | +0.471% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 9:41:20 PM | BTC | DOWN | 3.6 min | +0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 9:41:20 PM | ETH | DOWN | 3.6 min | +0.203% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 9:41:02 PM | PLATINUM | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:40:45 PM | SILVER | DOWN | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 9:40:45 PM | XRP | DOWN | 4.2 min | +0.316% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 9:40:29 PM | GOLD | DOWN | 4.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 9:40:29 PM | GBPUSD | DOWN | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:40:13 PM | DOGE | DOWN | 4.8 min | +0.294% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 9:38:51 PM | BNB | DOWN | 6.2 min | +0.206% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 9:29:45 PM | XRP | DOWN | 15 sec | +0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/26 9:29:29 PM | GOLD | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:28:58 PM | ZEC | DOWN | 62 sec | +0.224% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:28:58 PM | BNB | UP | 62 sec | -0.114% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:28:42 PM | WTI | DOWN | 78 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 9:28:42 PM | PLATINUM | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:28:42 PM | DOGE | DOWN | 78 sec | +0.119% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 9:28:42 PM | HYPE | DOWN | 78 sec | +0.115% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 9:28:26 PM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
