# 15-Minute 1¢ Study

*Updated Fri Nov 6, 9:26 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3772 finished bets | 1% | $127.05 | +30% | +3.37¢ | $84.15 / $42.90 |

*Expect about **96 buys a day** (~$14.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3516 | $54.35 | +14% |
| Volatility model ≥ 2%, hold to the close | 6975 | $28.00 | +3% |
| Momentum model ≥ 2%, hold to the close | 5759 | -$45.65 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 47795 | 47768 | 174 (0%) | 1.07% | -$3,390.75 (-58%) | Hold to the close: -$3,390.75 (-58%) |

*In play or awaiting result: 19. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 28840 | 4.7% | 0.4% (111) | -689% | ❌ Worse |
| Momentum model | 28840 | 4.6% | 0.4% (111) | -716% | ❌ Worse |
| Mean-reversion model | 28840 | 8.1% | 0.4% (111) | -838% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28840 | 111 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6975 | 62 | +3% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3772 | 39 | +30% | -77% | -75% | -72% |
| Volatility model ≥ 10% | 2158 | 24 | +60% | -71% | -70% | -67% |
| Momentum model ≥ 2% | 5759 | 44 | -7% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3516 | 31 | +14% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2300 | 20 | +22% | -75% | -75% | -71% |
| Mean-reversion model ≥ 2% | 11927 | 80 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8358 | 69 | -8% | -81% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5590 | 49 | -0% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 29045 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11502 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7221 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 47768 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 174 | 0% | -$3,390.75 | -58% | — |
| Sell at 2¢ | 1872 | 4% | -$5,088.03 | -87% | 47 sec |
| Sell at 3¢ | 1277 | 3% | -$5,076.72 | -87% | 49 sec |
| Sell at 5¢ | 884 | 2% | -$4,972.15 | -85% | 63 sec |
| Sell at 10¢ | 533 | 1% | -$4,764.52 | -82% | 65 sec |
| Sell at 25¢ | 279 | 1% | -$4,427.26 | -76% | 83 sec |
| Sell at 50¢ | 179 | 0% | -$4,044.50 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2364 | 10 | 10% | 4% | -60% | -82% | -83% |
| 2–5 min | 15370 | 82 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 12032 | 40 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 17990 | 42 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3255 | 13 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3248 | 12 | 4% | 2% | -53% | -90% | -90% |
| BNB | 3241 | 17 | 5% | 2% | -34% | -85% | -84% |
| HYPE | 3240 | 10 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 3228 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3225 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3206 | 16 | 5% | 2% | -35% | -84% | -84% |
| BTC | 3204 | 15 | 5% | 2% | -36% | -88% | -89% |
| XRP | 3198 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1768 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1718 | 6 | 4% | 1% | -58% | -92% | -92% |
| SILVER | 1714 | 8 | 5% | 2% | -45% | -82% | -82% |
| PLATINUM | 1549 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1487 | 3 | 2% | 1% | -81% | -90% | -89% |
| COPPER | 1459 | 6 | 2% | 1% | -62% | -71% | -71% |
| GBPUSD | 1414 | 4 | 2% | 1% | -74% | -96% | -96% |
| NATGAS | 1404 | 8 | 2% | 1% | -47% | -76% | -76% |
| USDJPY | 1391 | 5 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1390 | 3 | 1% | 1% | -80% | -91% | -92% |
| AUDUSD | 943 | 4 | 2% | 1% | -60% | -87% | -87% |
| USDCAD | 913 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 500 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 287 | 1 | 4% | 1% | -67% | -60% | -58% |
| 30YRRATE | 273 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 267 | 3 | 4% | 1% | +5% | -24% | -22% |
| 5YRRATE | 245 | 1 | 4% | 2% | -62% | -92% | -95% |
| INX | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24250 | 93 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23518 | 81 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4636 | 22 | 2% | 1% | -17% | -83% | -82% |
| 0.05–0.1% | 4920 | 18 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 7466 | 26 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8706 | 34 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3309 | 13 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11768 | 41 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11701 | 51 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 11352 | 41 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12947 | 41 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,637 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/6 9:26:27 AM | WTI | DOWN | 3.5 min | — | — | In play | — |
| 11/6 9:26:11 AM | SOL | DOWN | 3.8 min | +0.644% | — | In play | — |
| 11/6 9:25:24 AM | NEAR | DOWN | 4.6 min | +0.936% | — | In play | — |
| 11/6 9:25:08 AM | XRP | DOWN | 4.9 min | +0.659% | — | In play | — |
| 11/6 9:25:08 AM | ZEC | DOWN | 4.9 min | +1.739% | — | In play | — |
| 11/6 9:24:52 AM | 5YRRATE | DOWN | 5.1 min | — | — | In play | — |
| 11/6 9:24:52 AM | DOGE | DOWN | 5.1 min | +0.552% | — | In play | — |
| 11/6 9:24:36 AM | 10YRRATE | DOWN | 5.4 min | — | — | In play | — |
| 11/6 9:24:36 AM | 30YRRATE | DOWN | 5.4 min | — | — | In play | — |
| 11/6 9:24:36 AM | HYPE | DOWN | 5.4 min | +0.804% | — | In play | — |
| 11/6 9:14:59 AM | COPPER | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:14:59 AM | USDJPY | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:14:43 AM | GBPUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:14:43 AM | WTI | DOWN | 16 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:14:27 AM | EURUSD | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:14:27 AM | BRENT | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:13:55 AM | USDCAD | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:13:24 AM | NATGAS | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:13:24 AM | XRP | UP | 1.6 min | -0.320% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:12:37 AM | 10YRRATE | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:12:37 AM | ETH | UP | 2.4 min | -0.527% | 0¢ | ❌ Lost | $0.00 |
| 11/6 9:12:37 AM | 30YRRATE | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:12:37 AM | 5YRRATE | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:12:05 AM | NEAR | UP | 2.9 min | -1.076% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:12:05 AM | BTC | UP | 2.9 min | -0.354% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:11:49 AM | 2YRRATE | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:11:34 AM | BNB | UP | 3.4 min | -0.326% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:11:18 AM | DOGE | UP | 3.7 min | -0.509% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:11:18 AM | ZEC | UP | 3.7 min | -1.438% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:11:02 AM | SOL | UP | 4.0 min | -0.696% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
