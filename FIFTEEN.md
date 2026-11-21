# 15-Minute 1¢ Study

*Updated Fri Nov 20, 7:02 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4619 finished bets | 1% | $206.70 | +41% | +4.47¢ | $75.15 / $131.55 |

*Expect about **86 buys a day** (~$12.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4365 | $105.55 | +23% |
| Volatility model ≥ 2%, hold to the close | 8633 | $57.30 | +6% |
| Momentum model ≥ 2%, hold to the close | 7168 | -$22.35 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 63559 | 63525 | 245 (0%) | 1.07% | -$4,291.70 (-56%) | Hold to the close: -$4,291.70 (-56%) |

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
| Volatility model | 37595 | 4.5% | 0.4% (157) | -634% | ❌ Worse |
| Momentum model | 37595 | 4.4% | 0.4% (157) | -659% | ❌ Worse |
| Mean-reversion model | 37595 | 7.9% | 0.4% (157) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37595 | 157 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8633 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4619 | 51 | +41% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2658 | 30 | +65% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7168 | 57 | -3% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4365 | 41 | +23% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2845 | 26 | +31% | -67% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15339 | 109 | -22% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10662 | 89 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7088 | 64 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37801 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15259 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 63525 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 245 | 0% | -$4,291.70 | -56% | — |
| Sell at 2¢ | 2567 | 4% | -$6,760.28 | -88% | 47 sec |
| Sell at 3¢ | 1731 | 3% | -$6,752.61 | -87% | 48 sec |
| Sell at 5¢ | 1181 | 2% | -$6,632.05 | -86% | 63 sec |
| Sell at 10¢ | 722 | 1% | -$6,369.88 | -82% | 65 sec |
| Sell at 25¢ | 387 | 1% | -$5,880.73 | -76% | 80 sec |
| Sell at 50¢ | 251 | 0% | -$5,313.45 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3261 | 17 | 10% | 4% | -51% | -82% | -83% |
| 2–5 min | 20608 | 110 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 15873 | 55 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 23770 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4226 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4222 | 19 | 4% | 2% | -42% | -86% | -87% |
| HYPE | 4218 | 14 | 5% | 2% | -58% | -89% | -88% |
| DOGE | 4206 | 11 | 4% | 2% | -67% | -90% | -89% |
| BNB | 4206 | 21 | 5% | 2% | -37% | -86% | -85% |
| ETH | 4202 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4180 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4178 | 18 | 5% | 2% | -44% | -85% | -86% |
| XRP | 4163 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2265 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2250 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2209 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2012 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1968 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1900 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1895 | 6 | 2% | 1% | -70% | -77% | -77% |
| USDJPY | 1855 | 6 | 2% | 1% | -70% | -96% | -96% |
| NATGAS | 1854 | 10 | 2% | 1% | -50% | -76% | -76% |
| PALLADIUM | 1808 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1406 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1340 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 966 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 499 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 476 | 4 | 4% | 2% | -22% | -54% | -53% |
| 30YRRATE | 462 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 451 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32465 | 126 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31060 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5591 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6093 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9447 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11770 | 53 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 4891 | 23 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15327 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15289 | 81 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15576 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17333 | 50 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,993 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/20 6:59:36 PM | BTC | DOWN | 24 sec | +0.041% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:59:20 PM | HYPE | DOWN | 40 sec | +0.110% | 0¢ | ❌ Lost | $0.00 |
| 11/20 6:59:06 PM | ZEC | DOWN | 54 sec | +0.318% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:59:06 PM | NEAR | DOWN | 54 sec | +0.086% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:59:06 PM | DOGE | DOWN | 54 sec | +0.072% | 0¢ | ❌ Lost | $0.00 |
| 11/20 6:59:06 PM | ETH | DOWN | 54 sec | +0.089% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:58:51 PM | XRP | DOWN | 68 sec | +0.166% | 0¢ | ❌ Lost | $0.00 |
| 11/20 6:57:55 PM | BNB | UP | 2.1 min | -0.206% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:57:34 PM | SOL | UP | 2.4 min | -0.274% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:44:54 PM | BTC | UP | 5 sec | -0.021% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:44:54 PM | HYPE | DOWN | 5 sec | -0.027% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:44:54 PM | WTI | UP | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/20 6:44:54 PM | BNB | UP | 5 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 11/20 6:44:38 PM | XRP | DOWN | 21 sec | +0.088% | 0¢ | ❌ Lost | $0.00 |
| 11/20 6:44:22 PM | SOL | DOWN | 37 sec | +0.118% | 0¢ | ❌ Lost | $0.00 |
| 11/20 6:44:22 PM | NEAR | UP | 37 sec | -0.161% | 0¢ | ❌ Lost | $0.00 |
| 11/20 6:44:06 PM | DOGE | DOWN | 53 sec | +0.100% | 0¢ | ❌ Lost | $0.00 |
| 11/20 6:44:06 PM | ETH | DOWN | 53 sec | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:42:54 PM | ZEC | UP | 2.1 min | -0.507% | 0¢ | ❌ Lost | $0.00 |
| 11/20 6:29:02 PM | BNB | UP | 58 sec | -0.171% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:28:46 PM | ETH | UP | 74 sec | -0.266% | 0¢ | ❌ Lost | $0.00 |
| 11/20 6:28:46 PM | NEAR | UP | 74 sec | -0.356% | 0¢ | ❌ Lost | $0.00 |
| 11/20 6:28:14 PM | BTC | UP | 1.8 min | -0.256% | 0¢ | ❌ Lost | $0.00 |
| 11/20 6:28:14 PM | DOGE | UP | 1.8 min | -0.331% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:28:07 PM | XRP | UP | 1.9 min | -0.253% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:28:07 PM | SOL | UP | 1.9 min | -0.334% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:27:52 PM | HYPE | UP | 2.1 min | -0.439% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:27:36 PM | ZEC | UP | 2.4 min | -0.705% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:14:43 PM | WTI | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:14:11 PM | DOGE | DOWN | 49 sec | +0.171% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
