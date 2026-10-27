# 15-Minute 1¢ Study

*Updated Mon Oct 26, 11:03 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2803 finished bets | 1% | $75.20 | +24% | +2.68¢ | $27.35 / $47.85 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2607 | $48.90 | +17% |
| Volatility model ≥ 2%, hold to the close | 5212 | -$20.90 | -3% |
| Momentum model ≥ 2%, hold to the close | 4331 | -$43.80 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33938 | 33930 | 126 (0%) | 1.07% | -$2,361.90 (-57%) | Hold to the close: -$2,361.90 (-57%) |

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
| Volatility model | 21609 | 4.6% | 0.4% (86) | -671% | ❌ Worse |
| Momentum model | 21609 | 4.5% | 0.4% (86) | -696% | ❌ Worse |
| Mean-reversion model | 21609 | 7.9% | 0.4% (86) | -814% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21609 | 86 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5212 | 44 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2803 | 28 | +24% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1590 | 18 | +59% | -67% | -65% | -63% |
| Momentum model ≥ 2% | 4331 | 33 | -9% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2607 | 24 | +17% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1703 | 16 | +29% | -71% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8751 | 57 | -29% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6125 | 47 | -15% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4078 | 33 | -9% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21809 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7975 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4146 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33930 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 126 | 0% | -$2,361.90 | -57% | — |
| Sell at 2¢ | 1275 | 4% | -$3,626.40 | -88% | 47 sec |
| Sell at 3¢ | 874 | 3% | -$3,617.04 | -88% | 48 sec |
| Sell at 5¢ | 606 | 2% | -$3,564.00 | -86% | 62 sec |
| Sell at 10¢ | 373 | 1% | -$3,413.27 | -83% | 65 sec |
| Sell at 25¢ | 199 | 1% | -$3,159.21 | -77% | 83 sec |
| Sell at 50¢ | 129 | 0% | -$2,863.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1483 | 8 | 11% | 4% | -49% | -81% | -82% |
| 2–5 min | 10889 | 58 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8585 | 31 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12969 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2443 | 12 | 5% | 2% | -37% | -88% | -88% |
| HYPE | 2435 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2433 | 13 | 5% | 2% | -33% | -84% | -83% |
| SOL | 2430 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2423 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2418 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2412 | 12 | 5% | 2% | -35% | -82% | -82% |
| XRP | 2410 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2405 | 12 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1280 | 5 | 4% | 2% | -53% | -81% | -83% |
| SILVER | 1244 | 6 | 4% | 2% | -44% | -82% | -82% |
| WTI | 1226 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1093 | 0 | 2% | 1% | -100% | -97% | -97% |
| COPPER | 1056 | 4 | 1% | 1% | -65% | -71% | -71% |
| EURUSD | 1024 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1014 | 5 | 2% | 1% | -54% | -87% | -87% |
| PALLADIUM | 974 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 967 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 951 | 5 | 1% | 1% | -51% | -98% | -97% |
| AUDUSD | 509 | 2 | 1% | 1% | -63% | -98% | -96% |
| USDCAD | 468 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 88 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 63 | 0 | 3% | 0% | -100% | -94% | -96% |
| 2YRRATE | 57 | 1 | 4% | 0% | +64% | +70% | +68% |
| 30YRRATE | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 50 | 1 | 4% | 4% | +87% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17220 | 69 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16710 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3601 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3732 | 12 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5649 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6415 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2408 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9326 | 31 | 3% | 2% | -62% | -90% | -90% |

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
| 10/26 10:59:58 PM | USDJPY | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:59:42 PM | NEAR | DOWN | 17 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:59:42 PM | PALLADIUM | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:59:26 PM | COPPER | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:59:26 PM | WTI | UP | 33 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:59:26 PM | BRENT | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:59:26 PM | BNB | DOWN | 33 sec | +0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:59:10 PM | EURUSD | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:59:10 PM | XRP | DOWN | 50 sec | +0.031% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:58:52 PM | SOL | DOWN | 68 sec | +0.087% | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:58:36 PM | ZEC | DOWN | 84 sec | +0.151% | 0¢ | ❌ Lost | $0.00 |
| 10/26 10:58:36 PM | HYPE | DOWN | 84 sec | +0.049% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:58:20 PM | SILVER | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:58:20 PM | AUDUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:58:20 PM | USDCAD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:58:20 PM | BTC | DOWN | 1.7 min | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:58:20 PM | GBPUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:57:49 PM | ETH | DOWN | 2.2 min | +0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:57:33 PM | GOLD | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:57:17 PM | DOGE | DOWN | 2.7 min | +0.122% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:56:44 PM | PLATINUM | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:44:34 PM | NEAR | UP | 25 sec | -0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:44:18 PM | PLATINUM | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:44:01 PM | BRENT | DOWN | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:44:01 PM | PALLADIUM | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:43:45 PM | COPPER | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 10:43:45 PM | ZEC | UP | 74 sec | -0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:43:29 PM | WTI | DOWN | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:43:29 PM | DOGE | UP | 1.5 min | -0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 10:43:13 PM | AUDUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
