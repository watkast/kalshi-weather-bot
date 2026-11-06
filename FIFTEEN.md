# 15-Minute 1¢ Study

*Updated Fri Nov 6, 9:05 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

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
| Volatility model ≥ 2%, hold to the close | 6973 | $28.30 | +3% |
| Momentum model ≥ 2%, hold to the close | 5759 | -$45.65 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 47763 | 47746 | 174 (0%) | 1.07% | -$3,387.60 (-58%) | Hold to the close: -$3,387.60 (-58%) |

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
| Volatility model | 28831 | 4.7% | 0.4% (111) | -690% | ❌ Worse |
| Momentum model | 28831 | 4.6% | 0.4% (111) | -716% | ❌ Worse |
| Mean-reversion model | 28831 | 8.1% | 0.4% (111) | -838% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28831 | 111 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6973 | 62 | +3% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3772 | 39 | +30% | -77% | -75% | -72% |
| Volatility model ≥ 10% | 2158 | 24 | +60% | -71% | -70% | -67% |
| Momentum model ≥ 2% | 5759 | 44 | -7% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3516 | 31 | +14% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2300 | 20 | +22% | -75% | -75% | -71% |
| Mean-reversion model ≥ 2% | 11920 | 80 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8353 | 69 | -8% | -81% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5590 | 49 | -0% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 29036 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11497 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7213 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 47746 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 174 | 0% | -$3,387.60 | -58% | — |
| Sell at 2¢ | 1872 | 4% | -$5,084.88 | -87% | 47 sec |
| Sell at 3¢ | 1277 | 3% | -$5,073.57 | -87% | 49 sec |
| Sell at 5¢ | 884 | 2% | -$4,969.00 | -85% | 63 sec |
| Sell at 10¢ | 533 | 1% | -$4,761.37 | -82% | 65 sec |
| Sell at 25¢ | 279 | 1% | -$4,424.11 | -76% | 83 sec |
| Sell at 50¢ | 179 | 0% | -$4,041.35 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2363 | 10 | 10% | 4% | -60% | -82% | -83% |
| 2–5 min | 15358 | 82 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 12029 | 40 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 17984 | 42 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3254 | 13 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3247 | 12 | 4% | 2% | -53% | -90% | -90% |
| BNB | 3240 | 17 | 5% | 2% | -34% | -85% | -84% |
| HYPE | 3239 | 10 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 3227 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3224 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3205 | 16 | 5% | 2% | -35% | -84% | -84% |
| BTC | 3203 | 15 | 5% | 2% | -36% | -88% | -89% |
| XRP | 3197 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1767 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1717 | 6 | 4% | 1% | -58% | -92% | -92% |
| SILVER | 1714 | 8 | 5% | 2% | -45% | -82% | -82% |
| PLATINUM | 1549 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1486 | 3 | 2% | 1% | -81% | -90% | -89% |
| COPPER | 1458 | 6 | 2% | 1% | -62% | -71% | -71% |
| GBPUSD | 1413 | 4 | 2% | 1% | -74% | -96% | -96% |
| NATGAS | 1403 | 8 | 2% | 1% | -47% | -76% | -76% |
| PALLADIUM | 1390 | 3 | 1% | 1% | -80% | -91% | -92% |
| USDJPY | 1390 | 5 | 2% | 1% | -66% | -97% | -96% |
| AUDUSD | 943 | 4 | 2% | 1% | -60% | -87% | -87% |
| USDCAD | 912 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 499 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 286 | 1 | 4% | 1% | -67% | -60% | -58% |
| 30YRRATE | 272 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 266 | 3 | 4% | 1% | +5% | -23% | -22% |
| 5YRRATE | 244 | 1 | 5% | 2% | -62% | -92% | -95% |
| INX | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24236 | 93 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23510 | 81 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4636 | 22 | 2% | 1% | -17% | -83% | -82% |
| 0.05–0.1% | 4920 | 18 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 7466 | 26 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8703 | 34 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3303 | 13 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11768 | 41 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11679 | 51 | 4% | 2% | -50% | -86% | -85% |
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
| 11/6 8:59:56 AM | 30YRRATE | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 8:59:56 AM | BRENT | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 8:59:56 AM | BNB | DOWN | 3 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 11/6 8:59:08 AM | XRP | DOWN | 52 sec | +0.110% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 8:58:53 AM | EURUSD | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 8:58:53 AM | BTC | DOWN | 67 sec | +0.178% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 8:58:37 AM | AUDUSD | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 8:58:37 AM | GBPUSD | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 8:58:37 AM | COPPER | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 8:58:21 AM | ETH | DOWN | 1.6 min | +0.146% | 3¢ | ❌ Lost | -$0.15 |
| 11/6 8:58:21 AM | SOL | DOWN | 1.6 min | +0.261% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 8:58:21 AM | NEAR | DOWN | 1.6 min | +0.356% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 8:58:21 AM | NATGAS | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 8:58:21 AM | HYPE | DOWN | 1.6 min | +0.375% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 8:58:21 AM | ZEC | DOWN | 1.6 min | +0.607% | 4¢ | ❌ Lost | -$0.15 |
| 11/6 8:57:32 AM | GOLD | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 8:57:32 AM | PLATINUM | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 8:57:16 AM | DOGE | DOWN | 2.7 min | +0.354% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 3:14:57 AM | ETH | DOWN | 3 sec | -0.037% | 0¢ | ❌ Lost | $0.00 |
| 11/6 3:14:57 AM | COPPER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 3:14:57 AM | SILVER | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/6 3:14:57 AM | 10YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 3:14:41 AM | PLATINUM | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 3:14:41 AM | DOGE | UP | 19 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |
| 11/6 3:14:41 AM | GBPUSD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 3:14:41 AM | PALLADIUM | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 3:14:25 AM | XRP | UP | 35 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 11/6 3:14:25 AM | 30YRRATE | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 3:14:25 AM | GOLD | UP | 35 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 3:14:25 AM | BTC | DOWN | 35 sec | +0.040% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
