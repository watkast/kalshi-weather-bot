# 15-Minute 1¢ Study

*Updated Thu Nov 26, 4:02 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4927 finished bets | 1% | $206.05 | +38% | +4.18¢ | $85.60 / $120.45 |

*Expect about **83 buys a day** (~$12.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4671 | $105.35 | +21% |
| Volatility model ≥ 2%, hold to the close | 9179 | $42.00 | +4% |
| Momentum model ≥ 2%, hold to the close | 7636 | -$39.35 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 68186 | 68152 | 256 (0%) | 1.07% | -$4,666.30 (-57%) | Hold to the close: -$4,666.30 (-57%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 40329 | 4.5% | 0.4% (165) | -651% | ❌ Worse |
| Momentum model | 40329 | 4.4% | 0.4% (165) | -674% | ❌ Worse |
| Mean-reversion model | 40329 | 7.9% | 0.4% (165) | -790% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40329 | 165 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9179 | 81 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4927 | 53 | +38% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2851 | 32 | +66% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 7636 | 59 | -5% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4671 | 43 | +21% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3043 | 28 | +33% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16425 | 113 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11434 | 93 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7592 | 66 | -0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40535 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16260 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11357 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 68152 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 256 | 0% | -$4,666.30 | -57% | — |
| Sell at 2¢ | 2788 | 4% | -$7,231.42 | -88% | 47 sec |
| Sell at 3¢ | 1871 | 3% | -$7,226.61 | -88% | 48 sec |
| Sell at 5¢ | 1264 | 2% | -$7,106.70 | -86% | 62 sec |
| Sell at 10¢ | 772 | 1% | -$6,832.98 | -83% | 65 sec |
| Sell at 25¢ | 416 | 1% | -$6,313.34 | -77% | 80 sec |
| Sell at 50¢ | 266 | 0% | -$5,712.80 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3520 | 17 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 22098 | 116 | 7% | 3% | -48% | -86% | -87% |
| 1–2 min | 16997 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25524 | 65 | 1% | 0% | -63% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4533 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4526 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4520 | 20 | 4% | 2% | -43% | -86% | -86% |
| BNB | 4512 | 22 | 5% | 2% | -38% | -86% | -85% |
| DOGE | 4510 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4504 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4484 | 24 | 6% | 2% | -26% | -86% | -87% |
| NEAR | 4478 | 18 | 5% | 2% | -47% | -86% | -86% |
| XRP | 4468 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2403 | 8 | 5% | 2% | -59% | -83% | -84% |
| WTI | 2386 | 8 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2347 | 9 | 5% | 2% | -54% | -83% | -84% |
| PLATINUM | 2132 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2081 | 7 | 2% | 1% | -69% | -91% | -90% |
| GBPUSD | 2025 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 2018 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1979 | 6 | 2% | 1% | -72% | -96% | -96% |
| NATGAS | 1975 | 10 | 2% | 1% | -53% | -77% | -77% |
| PALLADIUM | 1918 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1546 | 7 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1453 | 1 | 3% | 1% | -94% | -95% | -96% |
| BRENT | 1081 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 557 | 2 | 3% | 1% | -66% | -78% | -76% |
| 30YRRATE | 518 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 515 | 4 | 4% | 2% | -28% | -57% | -57% |
| 5YRRATE | 506 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 139 | 1 | 2% | 1% | -33% | -96% | -96% |
| USDMXN | 38 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34806 | 132 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33346 | 124 | 4% | 2% | -57% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5887 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6431 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 10048 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12779 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5381 | 24 | 7% | 3% | -53% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16347 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16129 | 82 | 4% | 2% | -42% | -86% | -85% |
| Afternoon (12–6pm) | 16751 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18925 | 51 | 4% | 2% | -69% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,084 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/26 3:59:53 AM | COPPER | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:59:53 AM | EURUSD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:59:53 AM | GBPUSD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:59:53 AM | USDJPY | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:59:53 AM | BTC | UP | 7 sec | -0.036% | 0¢ | ❌ Lost | $0.00 |
| 11/26 3:59:36 AM | DOGE | DOWN | 23 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 11/26 3:59:36 AM | ETH | DOWN | 23 sec | +0.006% | 0¢ | ❌ Lost | $0.00 |
| 11/26 3:59:20 AM | SOL | UP | 39 sec | -0.068% | 0¢ | ❌ Lost | $0.00 |
| 11/26 3:59:04 AM | BNB | DOWN | 55 sec | -0.016% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:58:48 AM | PALLADIUM | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:58:31 AM | PLATINUM | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:58:31 AM | ZEC | UP | 88 sec | -0.312% | 0¢ | ❌ Lost | $0.00 |
| 11/26 3:58:31 AM | USDCAD | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:58:15 AM | BRENT | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:57:26 AM | XRP | DOWN | 2.5 min | +0.169% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:56:21 AM | WTI | DOWN | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:53:55 AM | HYPE | UP | 6.1 min | -0.991% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:44:47 PM | EURUSD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:44:47 PM | PALLADIUM | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:44:47 PM | PLATINUM | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:44:47 PM | SILVER | UP | 13 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/25 10:44:28 PM | GOLD | UP | 31 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/25 10:44:12 PM | DOGE | UP | 47 sec | -0.136% | 0¢ | ❌ Lost | $0.00 |
| 11/25 10:44:12 PM | XRP | UP | 47 sec | -0.156% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:44:12 PM | NEAR | DOWN | 47 sec | -0.016% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 10:44:12 PM | NATGAS | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:43:56 PM | ETH | UP | 63 sec | -0.160% | 0¢ | ❌ Lost | $0.00 |
| 11/25 10:42:49 PM | GBPUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:42:32 PM | BTC | UP | 2.5 min | -0.173% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 10:42:32 PM | SOL | UP | 2.5 min | -0.211% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
