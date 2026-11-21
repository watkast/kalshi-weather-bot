# 15-Minute 1¢ Study

*Updated Fri Nov 20, 7:22 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4622 finished bets | 1% | $206.40 | +41% | +4.47¢ | $75.00 / $131.40 |

*Expect about **86 buys a day** (~$12.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4368 | $105.25 | +22% |
| Volatility model ≥ 2%, hold to the close | 8636 | $57.00 | +6% |
| Momentum model ≥ 2%, hold to the close | 7171 | -$22.65 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 63570 | 63536 | 245 (0%) | 1.07% | -$4,292.45 (-56%) | Hold to the close: -$4,292.45 (-56%) |

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
| Volatility model | 37604 | 4.5% | 0.4% (157) | -635% | ❌ Worse |
| Momentum model | 37604 | 4.4% | 0.4% (157) | -660% | ❌ Worse |
| Mean-reversion model | 37604 | 7.9% | 0.4% (157) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37604 | 157 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8636 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4622 | 51 | +41% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2661 | 30 | +65% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7171 | 57 | -3% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4368 | 41 | +22% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2848 | 26 | +31% | -67% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15342 | 109 | -22% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10665 | 89 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7090 | 64 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37810 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15261 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 63536 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 245 | 0% | -$4,292.45 | -56% | — |
| Sell at 2¢ | 2567 | 4% | -$6,761.03 | -88% | 47 sec |
| Sell at 3¢ | 1731 | 3% | -$6,753.36 | -87% | 48 sec |
| Sell at 5¢ | 1181 | 2% | -$6,632.80 | -86% | 63 sec |
| Sell at 10¢ | 722 | 1% | -$6,370.63 | -82% | 65 sec |
| Sell at 25¢ | 387 | 1% | -$5,881.48 | -76% | 80 sec |
| Sell at 50¢ | 251 | 0% | -$5,314.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3261 | 17 | 10% | 4% | -51% | -82% | -83% |
| 2–5 min | 20608 | 110 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 15876 | 55 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 23778 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4227 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4223 | 19 | 4% | 2% | -42% | -86% | -87% |
| HYPE | 4219 | 14 | 5% | 2% | -58% | -89% | -88% |
| DOGE | 4207 | 11 | 4% | 2% | -67% | -90% | -89% |
| BNB | 4207 | 21 | 5% | 2% | -37% | -86% | -85% |
| ETH | 4203 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4181 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4179 | 18 | 5% | 2% | -44% | -85% | -86% |
| XRP | 4164 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2265 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2251 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2209 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2012 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1968 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1900 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1895 | 6 | 2% | 1% | -70% | -77% | -77% |
| NATGAS | 1855 | 10 | 2% | 1% | -50% | -76% | -76% |
| USDJPY | 1855 | 6 | 2% | 1% | -70% | -96% | -96% |
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
| UP (bought YES) | 32468 | 126 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31068 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5593 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6097 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9448 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11772 | 53 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 4891 | 23 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15327 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15289 | 81 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15576 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17344 | 50 | 4% | 2% | -67% | -89% | -89% |

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
| 11/20 7:14:57 PM | ZEC | UP | 2 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 11/20 7:14:57 PM | NATGAS | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:14:57 PM | SOL | DOWN | 2 sec | -0.011% | 0¢ | ❌ Lost | $0.00 |
| 11/20 7:14:41 PM | XRP | DOWN | 18 sec | +0.000% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 7:14:25 PM | ETH | DOWN | 34 sec | +0.055% | 0¢ | ❌ Lost | $0.00 |
| 11/20 7:14:25 PM | BTC | DOWN | 34 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 11/20 7:14:25 PM | WTI | DOWN | 34 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/20 7:14:09 PM | HYPE | UP | 51 sec | -0.183% | 0¢ | ❌ Lost | $0.00 |
| 11/20 7:13:53 PM | BNB | DOWN | 67 sec | +0.056% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 7:13:21 PM | NEAR | UP | 1.6 min | -0.465% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 7:13:21 PM | DOGE | DOWN | 1.6 min | +0.248% | 0¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
