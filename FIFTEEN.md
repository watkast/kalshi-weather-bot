# 15-Minute 1¢ Study

*Updated Fri Nov 20, 3:01 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4602 finished bets | 1% | $208.35 | +41% | +4.53¢ | $76.05 / $132.30 |

*Expect about **86 buys a day** (~$12.87/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4344 | $107.80 | +23% |
| Volatility model ≥ 2%, hold to the close | 8604 | $60.15 | +6% |
| Momentum model ≥ 2%, hold to the close | 7142 | -$19.50 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 63409 | 63364 | 245 (0%) | 1.07% | -$4,277.30 (-55%) | Hold to the close: -$4,277.30 (-55%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 37457 | 4.5% | 0.4% (157) | -632% | ❌ Worse |
| Momentum model | 37457 | 4.4% | 0.4% (157) | -657% | ❌ Worse |
| Mean-reversion model | 37457 | 7.9% | 0.4% (157) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37457 | 157 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8604 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4602 | 51 | +41% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2646 | 30 | +66% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 7142 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4344 | 41 | +23% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2833 | 26 | +31% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 15294 | 109 | -22% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10636 | 89 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7065 | 64 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37663 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15243 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10458 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 63364 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 245 | 0% | -$4,277.30 | -55% | — |
| Sell at 2¢ | 2564 | 4% | -$6,746.66 | -88% | 47 sec |
| Sell at 3¢ | 1729 | 3% | -$6,738.99 | -87% | 48 sec |
| Sell at 5¢ | 1181 | 2% | -$6,617.65 | -86% | 63 sec |
| Sell at 10¢ | 722 | 1% | -$6,355.48 | -82% | 65 sec |
| Sell at 25¢ | 387 | 1% | -$5,866.33 | -76% | 80 sec |
| Sell at 50¢ | 251 | 0% | -$5,299.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3260 | 17 | 10% | 4% | -51% | -82% | -83% |
| 2–5 min | 20569 | 110 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 15828 | 55 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 23694 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4211 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4207 | 19 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 4201 | 14 | 4% | 2% | -57% | -89% | -88% |
| DOGE | 4191 | 11 | 4% | 2% | -67% | -90% | -89% |
| BNB | 4190 | 21 | 5% | 2% | -36% | -86% | -85% |
| ETH | 4186 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4167 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4162 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4148 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2265 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2243 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2208 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2012 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1967 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1899 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1895 | 6 | 2% | 1% | -70% | -77% | -77% |
| USDJPY | 1854 | 6 | 2% | 1% | -70% | -96% | -96% |
| NATGAS | 1849 | 10 | 2% | 1% | -50% | -76% | -76% |
| PALLADIUM | 1808 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1405 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1339 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 963 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 499 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 476 | 4 | 4% | 2% | -22% | -54% | -53% |
| 30YRRATE | 461 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 450 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32385 | 126 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30979 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5576 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6077 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9404 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11720 | 53 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 4877 | 23 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15327 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15289 | 81 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15452 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17296 | 50 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,968 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/20 2:59:46 PM | DOGE | UP | 13 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 11/20 2:59:46 PM | NEAR | UP | 13 sec | -0.141% | 0¢ | ❌ Lost | $0.00 |
| 11/20 2:59:15 PM | SOL | DOWN | 45 sec | +0.104% | 1¢ | In play | — |
| 11/20 2:59:03 PM | XRP | UP | 57 sec | -0.220% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 2:58:47 PM | 5YRRATE | UP | 73 sec | — | 1¢ | In play | — |
| 11/20 2:58:47 PM | AUDUSD | DOWN | 73 sec | — | 0¢ | In play | — |
| 11/20 2:58:30 PM | USDJPY | UP | 89 sec | — | 0¢ | In play | — |
| 11/20 2:58:14 PM | NATGAS | DOWN | 1.8 min | — | 0¢ | In play | — |
| 11/20 2:58:14 PM | GBPUSD | DOWN | 1.8 min | — | 0¢ | In play | — |
| 11/20 2:58:02 PM | SILVER | DOWN | 1.9 min | — | 0¢ | In play | — |
| 11/20 2:56:59 PM | USDCAD | UP | 3.0 min | — | 0¢ | In play | — |
| 11/20 2:56:27 PM | EURUSD | DOWN | 3.5 min | — | 0¢ | In play | — |
| 11/20 2:55:45 PM | 30YRRATE | UP | 4.2 min | — | 0¢ | In play | — |
| 11/20 2:55:29 PM | HYPE | UP | 4.5 min | -0.805% | 0¢ | In play | — |
| 11/20 2:55:10 PM | ZEC | UP | 4.8 min | -1.543% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 2:55:10 PM | BNB | UP | 4.8 min | -0.565% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 2:55:10 PM | GOLD | DOWN | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 2:55:00 PM | BTC | UP | 5.0 min | -0.710% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 2:54:44 PM | ETH | UP | 5.2 min | -0.772% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 11:14:49 AM | NATGAS | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 11:14:49 AM | COPPER | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 11:14:33 AM | EURUSD | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 11:14:33 AM | SILVER | UP | 26 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/20 11:14:33 AM | DOGE | DOWN | 26 sec | +0.125% | 0¢ | ❌ Lost | $0.00 |
| 11/20 11:14:17 AM | INX | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 11:14:17 AM | USDCAD | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 11:14:17 AM | ZEC | DOWN | 43 sec | +0.608% | 0¢ | ❌ Lost | $0.00 |
| 11/20 11:14:17 AM | GBPUSD | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 11:14:17 AM | USDJPY | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 11:13:59 AM | WTI | UP | 61 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
