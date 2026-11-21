# 15-Minute 1¢ Study

*Updated Sat Nov 21, 9:36 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4653 finished bets | 1% | $203.10 | +40% | +4.36¢ | $73.50 / $129.60 |

*Expect about **86 buys a day** (~$12.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4410 | $100.60 | +21% |
| Volatility model ≥ 2%, hold to the close | 8706 | $48.60 | +5% |
| Momentum model ≥ 2%, hold to the close | 7246 | -$31.05 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 63943 | 63909 | 245 (0%) | 1.07% | -$4,329.35 (-56%) | Hold to the close: -$4,329.35 (-56%) |

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
| Volatility model | 37965 | 4.5% | 0.4% (157) | -638% | ❌ Worse |
| Momentum model | 37965 | 4.4% | 0.4% (157) | -662% | ❌ Worse |
| Mean-reversion model | 37965 | 7.8% | 0.4% (157) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37965 | 157 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8706 | 78 | +5% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4653 | 51 | +40% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2677 | 30 | +64% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7246 | 57 | -4% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4410 | 41 | +21% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2868 | 26 | +30% | -67% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15481 | 109 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10753 | 89 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7142 | 64 | +2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 38171 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15273 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 63909 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 245 | 0% | -$4,329.35 | -56% | — |
| Sell at 2¢ | 2580 | 4% | -$6,794.55 | -88% | 47 sec |
| Sell at 3¢ | 1737 | 3% | -$6,787.92 | -87% | 48 sec |
| Sell at 5¢ | 1183 | 2% | -$6,668.40 | -86% | 63 sec |
| Sell at 10¢ | 722 | 1% | -$6,407.53 | -83% | 65 sec |
| Sell at 25¢ | 387 | 1% | -$5,918.38 | -76% | 80 sec |
| Sell at 50¢ | 251 | 0% | -$5,351.10 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3303 | 17 | 10% | 4% | -51% | -82% | -83% |
| 2–5 min | 20723 | 110 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 15964 | 55 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 23906 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4267 | 19 | 5% | 2% | -41% | -88% | -87% |
| SOL | 4261 | 19 | 4% | 2% | -43% | -86% | -86% |
| HYPE | 4260 | 14 | 4% | 2% | -58% | -89% | -88% |
| DOGE | 4249 | 11 | 4% | 2% | -67% | -90% | -89% |
| BNB | 4248 | 21 | 5% | 2% | -37% | -86% | -85% |
| ETH | 4243 | 19 | 7% | 3% | -44% | -82% | -82% |
| BTC | 4221 | 22 | 5% | 2% | -29% | -86% | -88% |
| NEAR | 4219 | 18 | 5% | 2% | -44% | -85% | -86% |
| XRP | 4203 | 16 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2265 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2257 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2209 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2012 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1968 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1900 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1895 | 6 | 2% | 1% | -70% | -77% | -77% |
| NATGAS | 1858 | 10 | 2% | 1% | -50% | -76% | -76% |
| USDJPY | 1855 | 6 | 2% | 1% | -70% | -96% | -96% |
| PALLADIUM | 1808 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1406 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1340 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 969 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 499 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 476 | 4 | 4% | 2% | -22% | -54% | -53% |
| 30YRRATE | 462 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 451 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32663 | 126 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 31246 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5609 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6116 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9497 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11899 | 53 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5041 | 23 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15401 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15411 | 81 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15576 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17521 | 50 | 4% | 2% | -67% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,056 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/21 9:29:31 AM | DOGE | UP | 28 sec | -0.166% | 0¢ | ❌ Lost | $0.00 |
| 11/21 9:29:31 AM | ZEC | UP | 28 sec | -0.193% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 9:29:15 AM | SOL | DOWN | 44 sec | +0.098% | 0¢ | ❌ Lost | $0.00 |
| 11/21 9:29:15 AM | NEAR | UP | 44 sec | -0.228% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 9:28:59 AM | ETH | DOWN | 60 sec | +0.147% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 9:28:44 AM | BTC | DOWN | 75 sec | +0.328% | 0¢ | ❌ Lost | $0.00 |
| 11/21 9:28:44 AM | BNB | DOWN | 75 sec | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 9:28:12 AM | HYPE | UP | 1.8 min | -0.396% | 2¢ | ❌ Lost | -$0.15 |
| 11/21 9:27:25 AM | XRP | DOWN | 2.6 min | +0.346% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 9:14:43 AM | NEAR | DOWN | 16 sec | +0.270% | 0¢ | ❌ Lost | $0.00 |
| 11/21 9:14:27 AM | SOL | UP | 32 sec | -0.136% | 0¢ | ❌ Lost | $0.00 |
| 11/21 9:14:27 AM | BNB | UP | 32 sec | -0.192% | 0¢ | ❌ Lost | $0.00 |
| 11/21 9:14:27 AM | HYPE | UP | 32 sec | -0.108% | 0¢ | ❌ Lost | $0.00 |
| 11/21 9:14:11 AM | ZEC | UP | 48 sec | -0.231% | 0¢ | ❌ Lost | $0.00 |
| 11/21 9:14:11 AM | BTC | UP | 48 sec | -0.108% | 0¢ | ❌ Lost | $0.00 |
| 11/21 9:13:40 AM | DOGE | UP | 79 sec | -0.256% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 9:13:24 AM | XRP | DOWN | 1.6 min | +0.282% | 4¢ | ❌ Lost | -$0.15 |
| 11/21 9:12:21 AM | ETH | UP | 2.6 min | -0.343% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 8:58:30 AM | HYPE | UP | 1.5 min | -0.315% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 8:58:14 AM | ZEC | UP | 1.8 min | -0.831% | 0¢ | ❌ Lost | $0.00 |
| 11/21 8:58:14 AM | BNB | UP | 1.8 min | -0.278% | 0¢ | ❌ Lost | $0.00 |
| 11/21 8:57:58 AM | BTC | UP | 2.0 min | -0.353% | 0¢ | ❌ Lost | $0.00 |
| 11/21 8:57:58 AM | ETH | UP | 2.0 min | -0.330% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 8:57:43 AM | SOL | UP | 2.3 min | -0.338% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 8:57:43 AM | DOGE | UP | 2.3 min | -0.324% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 8:57:43 AM | NEAR | UP | 2.3 min | -0.559% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 8:57:28 AM | XRP | UP | 2.5 min | -0.303% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 8:44:51 AM | BTC | DOWN | 9 sec | +0.233% | 0¢ | ❌ Lost | $0.00 |
| 11/21 8:44:51 AM | HYPE | DOWN | 9 sec | +0.300% | 0¢ | ❌ Lost | $0.00 |
| 11/21 8:44:16 AM | ETH | DOWN | 43 sec | +0.127% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
