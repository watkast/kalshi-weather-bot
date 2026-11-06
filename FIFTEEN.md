# 15-Minute 1¢ Study

*Updated Fri Nov 6, 2:16 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3786 finished bets | 1% | $125.70 | +30% | +3.32¢ | $83.10 / $42.60 |

*Expect about **96 buys a day** (~$14.34/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3530 | $53.00 | +14% |
| Volatility model ≥ 2%, hold to the close | 7002 | $25.00 | +3% |
| Momentum model ≥ 2%, hold to the close | 5781 | -$47.90 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 48212 | 48195 | 174 (0%) | 1.07% | -$3,442.95 (-59%) | Hold to the close: -$3,442.95 (-59%) |

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
| Volatility model | 29015 | 4.7% | 0.4% (111) | -692% | ❌ Worse |
| Momentum model | 29015 | 4.6% | 0.4% (111) | -718% | ❌ Worse |
| Mean-reversion model | 29015 | 8.1% | 0.4% (111) | -841% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 29015 | 111 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 7002 | 62 | +3% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3786 | 39 | +30% | -77% | -75% | -72% |
| Volatility model ≥ 10% | 2168 | 24 | +59% | -72% | -70% | -67% |
| Momentum model ≥ 2% | 5781 | 44 | -7% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3530 | 31 | +14% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2308 | 20 | +22% | -75% | -75% | -71% |
| Mean-reversion model ≥ 2% | 11996 | 80 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8403 | 69 | -9% | -81% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5617 | 49 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 29220 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11621 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7354 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 48195 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 174 | 0% | -$3,442.95 | -59% | — |
| Sell at 2¢ | 1893 | 4% | -$5,134.77 | -87% | 47 sec |
| Sell at 3¢ | 1291 | 3% | -$5,123.46 | -87% | 49 sec |
| Sell at 5¢ | 894 | 2% | -$5,017.85 | -85% | 63 sec |
| Sell at 10¢ | 539 | 1% | -$4,808.86 | -82% | 66 sec |
| Sell at 25¢ | 281 | 1% | -$4,472.84 | -76% | 83 sec |
| Sell at 50¢ | 179 | 0% | -$4,096.70 | -70% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2389 | 10 | 11% | 4% | -60% | -81% | -83% |
| 2–5 min | 15482 | 82 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 12140 | 40 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 18172 | 42 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3275 | 13 | 5% | 3% | -49% | -88% | -88% |
| SOL | 3268 | 12 | 4% | 2% | -53% | -90% | -90% |
| HYPE | 3259 | 10 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3259 | 17 | 5% | 2% | -34% | -85% | -84% |
| DOGE | 3248 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3245 | 12 | 7% | 3% | -55% | -85% | -85% |
| NEAR | 3226 | 16 | 5% | 2% | -36% | -84% | -84% |
| BTC | 3223 | 15 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3217 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1781 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1734 | 6 | 4% | 1% | -58% | -92% | -92% |
| SILVER | 1731 | 8 | 5% | 2% | -45% | -82% | -81% |
| PLATINUM | 1565 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1501 | 3 | 2% | 1% | -81% | -90% | -89% |
| COPPER | 1471 | 6 | 2% | 1% | -62% | -72% | -71% |
| GBPUSD | 1425 | 4 | 2% | 1% | -74% | -96% | -96% |
| NATGAS | 1419 | 8 | 2% | 1% | -47% | -76% | -76% |
| PALLADIUM | 1406 | 3 | 1% | 0% | -80% | -91% | -92% |
| USDJPY | 1406 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 958 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 928 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 514 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 301 | 1 | 4% | 1% | -69% | -62% | -59% |
| 2YRRATE | 285 | 3 | 4% | 1% | -2% | -27% | -26% |
| 30YRRATE | 283 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 260 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24457 | 93 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23738 | 81 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4656 | 22 | 2% | 1% | -17% | -83% | -82% |
| 0.05–0.1% | 4946 | 18 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 7516 | 26 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8762 | 34 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3332 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11768 | 41 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11949 | 51 | 4% | 2% | -51% | -86% | -85% |
| Afternoon (12–6pm) | 11531 | 41 | 4% | 2% | -58% | -86% | -86% |
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
| 11/6 2:14:47 PM | 30YRRATE | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:14:47 PM | NATGAS | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:14:47 PM | 5YRRATE | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:14:30 PM | BTC | DOWN | 30 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 11/6 2:14:30 PM | ZEC | DOWN | 30 sec | +0.166% | 0¢ | ❌ Lost | $0.00 |
| 11/6 2:14:30 PM | PLATINUM | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:14:14 PM | EURUSD | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:13:58 PM | PALLADIUM | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:13:58 PM | ETH | DOWN | 62 sec | +0.043% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:13:43 PM | BNB | DOWN | 76 sec | +0.040% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:13:43 PM | USDJPY | DOWN | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:13:12 PM | DOGE | DOWN | 1.8 min | +0.120% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:12:58 PM | SOL | DOWN | 2.0 min | +0.148% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:12:27 PM | NEAR | DOWN | 2.5 min | +0.432% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:12:27 PM | HYPE | DOWN | 2.5 min | +0.229% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 2:11:39 PM | 2YRRATE | UP | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:11:08 PM | XRP | DOWN | 3.9 min | +0.307% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 1:59:42 PM | INX | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:59:42 PM | PALLADIUM | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:59:26 PM | NEAR | UP | 33 sec | -0.194% | 0¢ | ❌ Lost | $0.00 |
| 11/6 1:59:26 PM | XRP | UP | 33 sec | -0.111% | 0¢ | ❌ Lost | $0.00 |
| 11/6 1:59:10 PM | DOGE | UP | 49 sec | -0.160% | 0¢ | ❌ Lost | $0.00 |
| 11/6 1:59:10 PM | 10YRRATE | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:59:10 PM | 5YRRATE | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:59:10 PM | ZEC | UP | 49 sec | -0.222% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:59:10 PM | SOL | UP | 49 sec | -0.186% | 0¢ | ❌ Lost | $0.00 |
| 11/6 1:58:56 PM | 30YRRATE | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:58:56 PM | 2YRRATE | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:58:41 PM | USDJPY | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 1:58:41 PM | GOLD | DOWN | 78 sec | — | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
