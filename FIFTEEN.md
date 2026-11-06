# 15-Minute 1¢ Study

*Updated Fri Nov 6, 10:18 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3773 finished bets | 1% | $126.90 | +30% | +3.36¢ | $84.15 / $42.75 |

*Expect about **96 buys a day** (~$14.35/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3516 | $54.35 | +14% |
| Volatility model ≥ 2%, hold to the close | 6979 | $27.40 | +3% |
| Momentum model ≥ 2%, hold to the close | 5760 | -$45.80 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 47873 | 47856 | 174 (0%) | 1.07% | -$3,402.00 (-58%) | Hold to the close: -$3,402.00 (-58%) |

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
| Volatility model | 28876 | 4.7% | 0.4% (111) | -689% | ❌ Worse |
| Momentum model | 28876 | 4.6% | 0.4% (111) | -716% | ❌ Worse |
| Mean-reversion model | 28876 | 8.1% | 0.4% (111) | -838% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28876 | 111 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6979 | 62 | +3% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3773 | 39 | +30% | -77% | -75% | -72% |
| Volatility model ≥ 10% | 2158 | 24 | +60% | -71% | -70% | -67% |
| Momentum model ≥ 2% | 5760 | 44 | -7% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3516 | 31 | +14% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2300 | 20 | +22% | -75% | -75% | -71% |
| Mean-reversion model ≥ 2% | 11948 | 80 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8375 | 69 | -9% | -81% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5601 | 49 | -0% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 29081 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11528 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7247 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 47856 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 174 | 0% | -$3,402.00 | -58% | — |
| Sell at 2¢ | 1875 | 4% | -$5,098.50 | -87% | 47 sec |
| Sell at 3¢ | 1278 | 3% | -$5,087.58 | -87% | 49 sec |
| Sell at 5¢ | 885 | 2% | -$4,982.75 | -85% | 63 sec |
| Sell at 10¢ | 534 | 1% | -$4,774.46 | -82% | 66 sec |
| Sell at 25¢ | 279 | 1% | -$4,438.51 | -76% | 83 sec |
| Sell at 50¢ | 179 | 0% | -$4,055.75 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2376 | 10 | 10% | 4% | -60% | -82% | -83% |
| 2–5 min | 15399 | 82 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 12044 | 40 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 18025 | 42 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3259 | 13 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3252 | 12 | 4% | 2% | -53% | -90% | -90% |
| BNB | 3245 | 17 | 5% | 2% | -34% | -85% | -84% |
| HYPE | 3244 | 10 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 3232 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3229 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3210 | 16 | 5% | 2% | -35% | -84% | -84% |
| BTC | 3208 | 15 | 5% | 2% | -36% | -88% | -89% |
| XRP | 3202 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1771 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1722 | 6 | 4% | 1% | -58% | -92% | -92% |
| SILVER | 1718 | 8 | 5% | 2% | -45% | -82% | -82% |
| PLATINUM | 1553 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1489 | 3 | 2% | 1% | -81% | -90% | -89% |
| COPPER | 1461 | 6 | 2% | 1% | -62% | -71% | -71% |
| GBPUSD | 1416 | 4 | 2% | 1% | -74% | -96% | -96% |
| NATGAS | 1407 | 8 | 2% | 1% | -47% | -76% | -76% |
| PALLADIUM | 1394 | 3 | 1% | 1% | -80% | -91% | -92% |
| USDJPY | 1394 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 946 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 916 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 502 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 289 | 1 | 4% | 1% | -68% | -61% | -59% |
| 30YRRATE | 275 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 271 | 3 | 4% | 1% | +3% | -25% | -23% |
| 5YRRATE | 249 | 1 | 4% | 2% | -63% | -92% | -95% |
| INX | 2 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24294 | 93 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23562 | 81 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4637 | 22 | 2% | 1% | -17% | -83% | -82% |
| 0.05–0.1% | 4922 | 18 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 7476 | 26 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8717 | 34 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3321 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11768 | 41 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11789 | 51 | 4% | 2% | -51% | -86% | -86% |
| Afternoon (12–6pm) | 11352 | 41 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12947 | 41 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,632 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/6 10:14:58 AM | WTI | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 10:14:41 AM | 5YRRATE | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 10:14:41 AM | 30YRRATE | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 10:14:25 AM | NEAR | UP | 35 sec | -0.175% | 0¢ | ❌ Lost | $0.00 |
| 11/6 10:14:25 AM | GBPUSD | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 10:14:25 AM | 10YRRATE | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 10:14:25 AM | BTC | UP | 35 sec | -0.071% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:14:25 AM | SOL | UP | 35 sec | -0.173% | 0¢ | ❌ Lost | $0.00 |
| 11/6 10:14:25 AM | 2YRRATE | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 10:14:09 AM | ZEC | UP | 51 sec | -0.446% | 0¢ | ❌ Lost | $0.00 |
| 11/6 10:14:09 AM | BNB | UP | 51 sec | -0.100% | 0¢ | ❌ Lost | $0.00 |
| 11/6 10:14:09 AM | INX | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 10:14:09 AM | ETH | UP | 51 sec | -0.156% | 0¢ | ❌ Lost | $0.00 |
| 11/6 10:13:54 AM | DOGE | UP | 65 sec | -0.186% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:13:54 AM | XRP | UP | 65 sec | -0.184% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 10:13:07 AM | COPPER | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 10:12:51 AM | HYPE | UP | 2.1 min | -0.518% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 10:12:18 AM | PALLADIUM | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 10:11:47 AM | USDCAD | DOWN | 3.2 min | — | 20¢ | ❌ Lost | -$0.15 |
| 11/6 10:11:12 AM | AUDUSD | UP | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:10:08 AM | SILVER | UP | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:10:08 AM | PLATINUM | UP | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 10:09:05 AM | GOLD | UP | 5.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:59:56 AM | 5YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:59:56 AM | NATGAS | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:59:56 AM | 2YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:59:41 AM | EURUSD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:59:41 AM | WTI | UP | 18 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/6 9:59:25 AM | USDJPY | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:59:09 AM | USDCAD | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
