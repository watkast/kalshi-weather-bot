# 15-Minute 1¢ Study

*Updated Sun Nov 1, 9:09 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3461 finished bets | 1% | $131.45 | +34% | +3.80¢ | $74.30 / $57.15 |

*Expect about **99 buys a day** (~$14.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3191 | $58.90 | +17% |
| Volatility model ≥ 2%, hold to the close | 6392 | $52.15 | +7% |
| Momentum model ≥ 2%, hold to the close | 5266 | -$34.85 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41966 | 41956 | 158 (0%) | 1.07% | -$2,893.40 (-57%) | Hold to the close: -$2,893.40 (-57%) |

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
| Volatility model | 26190 | 4.7% | 0.4% (105) | -676% | ❌ Worse |
| Momentum model | 26190 | 4.6% | 0.4% (105) | -698% | ❌ Worse |
| Mean-reversion model | 26190 | 8.1% | 0.4% (105) | -824% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26190 | 105 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6392 | 59 | +7% | -79% | -78% | -73% |
| Volatility model ≥ 5% | 3461 | 37 | +34% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1961 | 22 | +60% | -70% | -68% | -64% |
| Momentum model ≥ 2% | 5266 | 41 | -6% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3191 | 29 | +17% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 2084 | 19 | +27% | -73% | -73% | -68% |
| Mean-reversion model ≥ 2% | 10825 | 75 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7589 | 64 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5076 | 46 | +3% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26392 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 9814 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5750 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41956 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 158 | 0% | -$2,893.40 | -57% | — |
| Sell at 2¢ | 1646 | 4% | -$4,453.44 | -87% | 47 sec |
| Sell at 3¢ | 1131 | 3% | -$4,440.31 | -87% | 48 sec |
| Sell at 5¢ | 786 | 2% | -$4,342.50 | -85% | 63 sec |
| Sell at 10¢ | 473 | 1% | -$4,163.77 | -82% | 65 sec |
| Sell at 25¢ | 250 | 1% | -$3,843.90 | -75% | 83 sec |
| Sell at 50¢ | 163 | 0% | -$3,487.15 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1994 | 9 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 13465 | 75 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 10606 | 37 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15880 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2956 | 13 | 5% | 3% | -44% | -88% | -87% |
| SOL | 2947 | 11 | 4% | 2% | -53% | -91% | -90% |
| BNB | 2944 | 17 | 5% | 2% | -28% | -85% | -84% |
| HYPE | 2943 | 9 | 5% | 3% | -62% | -89% | -87% |
| ETH | 2932 | 11 | 6% | 3% | -54% | -85% | -85% |
| DOGE | 2931 | 6 | 4% | 2% | -74% | -90% | -90% |
| BTC | 2914 | 14 | 5% | 2% | -35% | -87% | -89% |
| XRP | 2913 | 11 | 3% | 1% | -53% | -89% | -89% |
| NEAR | 2912 | 15 | 5% | 2% | -33% | -83% | -83% |
| GOLD | 1531 | 5 | 5% | 2% | -61% | -82% | -84% |
| SILVER | 1495 | 7 | 5% | 2% | -44% | -82% | -81% |
| WTI | 1489 | 4 | 3% | 1% | -68% | -93% | -93% |
| PLATINUM | 1326 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1266 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1263 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1222 | 7 | 2% | 1% | -47% | -81% | -80% |
| GBPUSD | 1196 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1188 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1184 | 5 | 2% | 1% | -61% | -97% | -96% |
| AUDUSD | 717 | 4 | 2% | 1% | -48% | -84% | -83% |
| USDCAD | 698 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 297 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21281 | 87 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20675 | 71 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4311 | 21 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 4544 | 17 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 6825 | 24 | 4% | 2% | -56% | -90% | -90% |
| 0.2–0.5% | 7777 | 33 | 7% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2930 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10303 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9923 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11217 | 37 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,806 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 8:59:56 PM | BTC | UP | 4 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 11/1 8:59:40 PM | USDJPY | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 8:59:24 PM | SOL | UP | 36 sec | -0.106% | 0¢ | ❌ Lost | $0.00 |
| 11/1 8:59:24 PM | EURUSD | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 8:59:24 PM | GBPUSD | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 8:59:24 PM | BNB | UP | 36 sec | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 11/1 8:59:24 PM | DOGE | DOWN | 36 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 11/1 8:59:24 PM | NEAR | UP | 36 sec | -0.279% | 0¢ | ❌ Lost | $0.00 |
| 11/1 8:59:08 PM | XRP | DOWN | 52 sec | +0.056% | 0¢ | ❌ Lost | $0.00 |
| 11/1 8:58:15 PM | NATGAS | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 8:58:15 PM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 8:57:25 PM | ETH | DOWN | 2.6 min | +0.137% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 8:57:08 PM | SILVER | UP | 2.9 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/1 8:57:08 PM | BRENT | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 8:56:51 PM | WTI | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 8:56:51 PM | HYPE | DOWN | 3.1 min | +0.279% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 8:56:35 PM | ZEC | DOWN | 3.4 min | +0.491% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 8:56:03 PM | GOLD | UP | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/1 8:55:28 PM | PLATINUM | UP | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 8:44:50 PM | WTI | DOWN | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/1 8:44:50 PM | NATGAS | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 8:44:18 PM | PLATINUM | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 8:44:18 PM | SOL | DOWN | 42 sec | +0.046% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 8:44:01 PM | EURUSD | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 8:44:01 PM | XRP | DOWN | 58 sec | +0.080% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 8:44:01 PM | HYPE | DOWN | 58 sec | +0.134% | 0¢ | ❌ Lost | $0.00 |
| 11/1 8:44:01 PM | BTC | UP | 58 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 11/1 8:44:01 PM | NEAR | UP | 58 sec | -0.315% | 0¢ | ❌ Lost | $0.00 |
| 11/1 8:44:01 PM | COPPER | DOWN | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 8:43:45 PM | SILVER | DOWN | 74 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
