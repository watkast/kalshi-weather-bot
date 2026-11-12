# 15-Minute 1¢ Study

*Updated Thu Nov 12, 6:35 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4243 finished bets | 1% | $173.30 | +37% | +4.08¢ | $83.65 / $89.65 |

*Expect about **94 buys a day** (~$14.05/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3978 | $101.05 | +23% |
| Volatility model ≥ 2%, hold to the close | 7804 | $41.30 | +4% |
| Momentum model ≥ 2%, hold to the close | 6482 | -$16.75 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 54716 | 54695 | 209 (0%) | 1.07% | -$3,747.95 (-56%) | Hold to the close: -$3,747.95 (-56%) |

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
| Volatility model | 32801 | 4.7% | 0.4% (132) | -670% | ❌ Worse |
| Momentum model | 32801 | 4.6% | 0.4% (132) | -695% | ❌ Worse |
| Mean-reversion model | 32801 | 8.0% | 0.4% (132) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32801 | 132 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7804 | 70 | +4% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4243 | 46 | +37% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2452 | 28 | +64% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6482 | 52 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3978 | 38 | +23% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2607 | 25 | +35% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13529 | 92 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9457 | 78 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6314 | 56 | +1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33006 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13140 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8549 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 54695 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 209 | 0% | -$3,747.95 | -56% | — |
| Sell at 2¢ | 2179 | 4% | -$5,813.41 | -87% | 47 sec |
| Sell at 3¢ | 1483 | 3% | -$5,801.58 | -87% | 49 sec |
| Sell at 5¢ | 1024 | 2% | -$5,686.35 | -85% | 63 sec |
| Sell at 10¢ | 619 | 1% | -$5,457.06 | -82% | 65 sec |
| Sell at 25¢ | 328 | 1% | -$5,070.27 | -76% | 82 sec |
| Sell at 50¢ | 215 | 0% | -$4,592.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2733 | 13 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 17694 | 96 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 13780 | 45 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 20475 | 55 | 1% | 0% | -62% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3694 | 17 | 5% | 3% | -40% | -88% | -87% |
| SOL | 3690 | 16 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3683 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3675 | 19 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 3671 | 8 | 4% | 2% | -73% | -90% | -90% |
| ETH | 3666 | 16 | 7% | 3% | -46% | -82% | -82% |
| NEAR | 3647 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3646 | 17 | 5% | 2% | -36% | -87% | -88% |
| XRP | 3634 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1974 | 5 | 5% | 2% | -69% | -82% | -84% |
| WTI | 1959 | 6 | 4% | 2% | -63% | -91% | -92% |
| SILVER | 1924 | 9 | 5% | 2% | -45% | -83% | -82% |
| PLATINUM | 1755 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1693 | 6 | 3% | 1% | -67% | -90% | -89% |
| COPPER | 1640 | 6 | 2% | 1% | -66% | -74% | -74% |
| GBPUSD | 1620 | 6 | 2% | 1% | -65% | -96% | -96% |
| NATGAS | 1609 | 9 | 2% | 1% | -48% | -73% | -73% |
| USDJPY | 1593 | 6 | 2% | 1% | -65% | -97% | -96% |
| PALLADIUM | 1572 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1149 | 6 | 2% | 1% | -51% | -88% | -88% |
| USDCAD | 1104 | 0 | 2% | 1% | -100% | -96% | -96% |
| BRENT | 707 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 360 | 2 | 4% | 2% | -48% | -67% | -65% |
| 2YRRATE | 343 | 4 | 4% | 2% | +9% | -39% | -37% |
| 30YRRATE | 339 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 316 | 2 | 4% | 2% | -41% | -92% | -94% |
| INX | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27794 | 109 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 26901 | 100 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5215 | 25 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 5607 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8456 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9947 | 41 | 6% | 3% | -54% | -87% | -87% |
| Over 0.5% | 3773 | 17 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13478 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13124 | 60 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 13132 | 58 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14961 | 47 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,853 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/12 6:29:51 AM | PALLADIUM | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 6:29:51 AM | COPPER | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 6:29:35 AM | PLATINUM | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 6:29:35 AM | NATGAS | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 6:29:19 AM | NEAR | DOWN | 40 sec | +0.151% | 0¢ | ❌ Lost | -$0.15 |
| 11/12 6:29:19 AM | GBPUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 6:29:19 AM | ZEC | DOWN | 40 sec | +0.215% | 0¢ | ❌ Lost | $0.00 |
| 11/12 6:29:03 AM | BTC | DOWN | 56 sec | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 6:28:47 AM | DOGE | DOWN | 73 sec | +0.306% | 0¢ | ❌ Lost | $0.00 |
| 11/12 6:28:47 AM | BNB | DOWN | 73 sec | +0.157% | 0¢ | ❌ Lost | -$0.15 |
| 11/12 6:28:32 AM | EURUSD | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 6:27:44 AM | GOLD | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 6:27:44 AM | HYPE | DOWN | 2.3 min | +0.466% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 6:27:27 AM | XRP | DOWN | 2.5 min | +0.389% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 6:27:11 AM | USDCAD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 6:27:11 AM | AUDUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 6:26:40 AM | ETH | DOWN | 3.3 min | +0.399% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 6:14:54 AM | COPPER | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 6:14:11 AM | PLATINUM | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 6:14:11 AM | USDJPY | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 6:14:11 AM | GOLD | UP | 49 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/12 6:13:56 AM | SILVER | UP | 64 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 6:13:08 AM | 30YRRATE | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 6:12:52 AM | 10YRRATE | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 6:12:04 AM | BTC | UP | 2.9 min | -0.476% | 3¢ | ❌ Lost | -$0.15 |
| 11/12 6:12:04 AM | HYPE | UP | 2.9 min | -0.754% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 6:11:49 AM | NEAR | UP | 3.2 min | -1.308% | 2¢ | ❌ Lost | -$0.15 |
| 11/12 6:11:33 AM | WTI | DOWN | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 6:11:33 AM | AUDUSD | UP | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 6:11:17 AM | EURUSD | UP | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
