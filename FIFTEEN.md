# 15-Minute 1¢ Study

*Updated Thu Nov 5, 5:33 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3699 finished bets | 1% | $134.10 | +33% | +3.63¢ | $88.50 / $45.60 |

*Expect about **97 buys a day** (~$14.51/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3439 | $61.55 | +17% |
| Volatility model ≥ 2%, hold to the close | 6847 | $42.10 | +5% |
| Momentum model ≥ 2%, hold to the close | 5651 | -$34.40 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 46488 | 46477 | 170 (0%) | 1.07% | -$3,286.85 (-58%) | Hold to the close: -$3,286.85 (-58%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 28258 | 4.7% | 0.4% (110) | -686% | ❌ Worse |
| Momentum model | 28258 | 4.6% | 0.4% (110) | -713% | ❌ Worse |
| Mean-reversion model | 28258 | 8.1% | 0.4% (110) | -834% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28258 | 110 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6847 | 62 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3699 | 39 | +33% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2111 | 24 | +63% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5651 | 44 | -5% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3439 | 31 | +17% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2247 | 20 | +25% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11689 | 80 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8202 | 69 | -7% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5495 | 49 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28463 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11120 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6894 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 46477 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 170 | 0% | -$3,286.85 | -58% | — |
| Sell at 2¢ | 1819 | 4% | -$4,941.91 | -87% | 47 sec |
| Sell at 3¢ | 1243 | 3% | -$4,930.08 | -87% | 48 sec |
| Sell at 5¢ | 860 | 2% | -$4,827.85 | -85% | 63 sec |
| Sell at 10¢ | 520 | 1% | -$4,621.65 | -82% | 65 sec |
| Sell at 25¢ | 269 | 1% | -$4,300.46 | -76% | 83 sec |
| Sell at 50¢ | 173 | 0% | -$3,925.10 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2301 | 10 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 14961 | 79 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 11691 | 39 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17512 | 42 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3188 | 13 | 5% | 2% | -47% | -88% | -88% |
| SOL | 3181 | 12 | 4% | 2% | -52% | -90% | -90% |
| HYPE | 3177 | 9 | 5% | 2% | -65% | -89% | -87% |
| BNB | 3177 | 17 | 5% | 2% | -33% | -85% | -85% |
| DOGE | 3164 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3158 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3142 | 16 | 5% | 2% | -34% | -84% | -84% |
| BTC | 3142 | 15 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3134 | 12 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1719 | 5 | 5% | 2% | -65% | -81% | -83% |
| SILVER | 1669 | 8 | 5% | 2% | -44% | -82% | -82% |
| WTI | 1667 | 5 | 4% | 1% | -64% | -92% | -93% |
| PLATINUM | 1498 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1436 | 3 | 2% | 1% | -81% | -89% | -89% |
| COPPER | 1414 | 6 | 2% | 1% | -60% | -71% | -70% |
| GBPUSD | 1365 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1354 | 8 | 2% | 1% | -45% | -76% | -75% |
| PALLADIUM | 1346 | 3 | 1% | 1% | -79% | -91% | -91% |
| USDJPY | 1345 | 5 | 2% | 1% | -65% | -97% | -97% |
| AUDUSD | 890 | 4 | 2% | 1% | -58% | -86% | -86% |
| USDCAD | 868 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 453 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 266 | 1 | 5% | 2% | -65% | -57% | -55% |
| 30YRRATE | 249 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 248 | 2 | 3% | 0% | -25% | -19% | -18% |
| 5YRRATE | 227 | 1 | 4% | 2% | -59% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23573 | 90 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 22904 | 80 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4570 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4854 | 18 | 3% | 2% | -44% | -91% | -90% |
| 0.1–0.2% | 7338 | 26 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8489 | 33 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3204 | 13 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11469 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11422 | 50 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 10960 | 39 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12626 | 41 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,673 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/5 5:29:51 AM | USDCAD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:29:51 AM | 2YRRATE | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:29:35 AM | 10YRRATE | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:29:19 AM | NEAR | UP | 41 sec | -0.140% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:29:04 AM | 30YRRATE | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:28:49 AM | ZEC | UP | 70 sec | -0.246% | 0¢ | ❌ Lost | $0.00 |
| 11/5 5:28:49 AM | BRENT | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:28:49 AM | NATGAS | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:28:33 AM | PALLADIUM | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:27:12 AM | XRP | UP | 2.8 min | -0.266% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:27:12 AM | BTC | UP | 2.8 min | -0.142% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:26:57 AM | GOLD | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:26:26 AM | PLATINUM | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:26:10 AM | DOGE | UP | 3.8 min | -0.401% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:26:10 AM | HYPE | UP | 3.8 min | -0.363% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:26:10 AM | ETH | UP | 3.8 min | -0.238% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:26:10 AM | SILVER | UP | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:25:54 AM | SOL | UP | 4.1 min | -0.377% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:25:39 AM | AUDUSD | UP | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:24:51 AM | BNB | UP | 5.2 min | -0.284% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:23:47 AM | COPPER | UP | 6.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:14:56 AM | WTI | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:14:56 AM | PALLADIUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:14:08 AM | 10YRRATE | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:14:08 AM | USDCAD | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:13:52 AM | PLATINUM | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:13:52 AM | USDJPY | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:13:52 AM | 5YRRATE | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:13:37 AM | 2YRRATE | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:13:21 AM | SILVER | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
