# 15-Minute 1¢ Study

*Updated Fri Nov 6, 2:50 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3788 finished bets | 1% | $125.70 | +30% | +3.32¢ | $82.95 / $42.75 |

*Expect about **96 buys a day** (~$14.34/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3531 | $53.00 | +14% |
| Volatility model ≥ 2%, hold to the close | 7005 | $24.85 | +3% |
| Momentum model ≥ 2%, hold to the close | 5782 | -$47.90 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 48233 | 48216 | 174 (0%) | 1.07% | -$3,445.50 (-59%) | Hold to the close: -$3,445.50 (-59%) |

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
| Volatility model | 29024 | 4.7% | 0.4% (111) | -693% | ❌ Worse |
| Momentum model | 29024 | 4.6% | 0.4% (111) | -719% | ❌ Worse |
| Mean-reversion model | 29024 | 8.1% | 0.4% (111) | -842% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 29024 | 111 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 7005 | 62 | +3% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3788 | 39 | +30% | -77% | -75% | -72% |
| Volatility model ≥ 10% | 2170 | 24 | +59% | -72% | -70% | -67% |
| Momentum model ≥ 2% | 5782 | 44 | -7% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3531 | 31 | +14% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2309 | 20 | +22% | -75% | -75% | -71% |
| Mean-reversion model ≥ 2% | 12001 | 80 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8407 | 69 | -9% | -81% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5620 | 49 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 29229 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11626 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7361 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 48216 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 174 | 0% | -$3,445.50 | -59% | — |
| Sell at 2¢ | 1894 | 4% | -$5,137.06 | -87% | 47 sec |
| Sell at 3¢ | 1292 | 3% | -$5,125.62 | -87% | 49 sec |
| Sell at 5¢ | 895 | 2% | -$5,019.75 | -85% | 63 sec |
| Sell at 10¢ | 539 | 1% | -$4,811.41 | -82% | 66 sec |
| Sell at 25¢ | 281 | 1% | -$4,475.39 | -76% | 83 sec |
| Sell at 50¢ | 179 | 0% | -$4,099.25 | -70% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2389 | 10 | 11% | 4% | -60% | -81% | -83% |
| 2–5 min | 15485 | 82 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 12147 | 40 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 18183 | 42 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3276 | 13 | 5% | 3% | -49% | -88% | -88% |
| SOL | 3269 | 12 | 4% | 2% | -53% | -90% | -90% |
| HYPE | 3260 | 10 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3260 | 17 | 5% | 2% | -34% | -85% | -84% |
| DOGE | 3249 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3246 | 12 | 7% | 3% | -55% | -85% | -85% |
| NEAR | 3227 | 16 | 5% | 2% | -36% | -84% | -84% |
| BTC | 3224 | 15 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3218 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1782 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1734 | 6 | 4% | 1% | -58% | -92% | -92% |
| SILVER | 1732 | 8 | 5% | 2% | -45% | -82% | -81% |
| PLATINUM | 1566 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1502 | 3 | 2% | 1% | -81% | -90% | -89% |
| COPPER | 1471 | 6 | 2% | 1% | -62% | -72% | -71% |
| GBPUSD | 1425 | 4 | 2% | 1% | -74% | -96% | -96% |
| NATGAS | 1420 | 8 | 2% | 1% | -47% | -76% | -76% |
| PALLADIUM | 1407 | 3 | 1% | 0% | -80% | -91% | -92% |
| USDJPY | 1406 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 959 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 929 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 514 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 302 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 286 | 3 | 4% | 1% | -2% | -27% | -27% |
| 30YRRATE | 284 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 261 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24464 | 93 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23752 | 81 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4659 | 22 | 2% | 1% | -17% | -83% | -82% |
| 0.05–0.1% | 4948 | 18 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 7519 | 26 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8763 | 34 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3332 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11768 | 41 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11949 | 51 | 4% | 2% | -51% | -86% | -85% |
| Afternoon (12–6pm) | 11552 | 41 | 4% | 2% | -59% | -86% | -86% |
| Evening (6pm–12am) | 12947 | 41 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,616 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/6 2:44:51 PM | 5YRRATE | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:44:51 PM | 2YRRATE | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:44:35 PM | BNB | DOWN | 25 sec | -0.030% | 0¢ | ❌ Lost | $0.00 |
| 11/6 2:44:35 PM | 10YRRATE | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:44:35 PM | HYPE | DOWN | 25 sec | +0.012% | 0¢ | ❌ Lost | $0.00 |
| 11/6 2:44:19 PM | AUDUSD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:44:19 PM | ZEC | UP | 41 sec | -0.271% | 0¢ | ❌ Lost | $0.00 |
| 11/6 2:44:19 PM | PALLADIUM | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:44:19 PM | XRP | DOWN | 41 sec | +0.043% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:44:03 PM | 30YRRATE | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:44:03 PM | BTC | DOWN | 56 sec | +0.053% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:43:47 PM | SILVER | DOWN | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:43:47 PM | SOL | DOWN | 72 sec | +0.122% | 0¢ | ❌ Lost | $0.00 |
| 11/6 2:43:47 PM | EURUSD | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:43:47 PM | ETH | DOWN | 72 sec | +0.063% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:43:31 PM | NEAR | DOWN | 88 sec | +0.200% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:43:31 PM | GOLD | DOWN | 88 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:43:15 PM | USDCAD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:42:43 PM | DOGE | UP | 2.3 min | -0.161% | 10¢ | ❌ Lost | -$0.15 |
| 11/6 2:42:27 PM | NATGAS | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:40:36 PM | PLATINUM | DOWN | 4.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:14:47 PM | 30YRRATE | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:14:47 PM | NATGAS | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:14:47 PM | 5YRRATE | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:14:30 PM | BTC | DOWN | 30 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 11/6 2:14:30 PM | ZEC | DOWN | 30 sec | +0.166% | 0¢ | ❌ Lost | $0.00 |
| 11/6 2:14:30 PM | PLATINUM | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:14:14 PM | EURUSD | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:13:58 PM | PALLADIUM | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:13:58 PM | ETH | DOWN | 62 sec | +0.043% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
