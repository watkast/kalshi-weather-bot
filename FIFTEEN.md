# 15-Minute 1¢ Study

*Updated Wed Nov 25, 11:38 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4891 finished bets | 1% | $209.35 | +39% | +4.28¢ | $87.55 / $121.80 |

*Expect about **84 buys a day** (~$12.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4632 | $108.65 | +22% |
| Volatility model ≥ 2%, hold to the close | 9114 | $48.15 | +4% |
| Momentum model ≥ 2%, hold to the close | 7580 | -$34.40 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 67657 | 67623 | 256 (0%) | 1.07% | -$4,603.90 (-56%) | Hold to the close: -$4,603.90 (-56%) |

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
| Volatility model | 40088 | 4.5% | 0.4% (165) | -646% | ❌ Worse |
| Momentum model | 40088 | 4.4% | 0.4% (165) | -669% | ❌ Worse |
| Mean-reversion model | 40088 | 7.9% | 0.4% (165) | -786% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40088 | 165 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 9114 | 81 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4891 | 53 | +39% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2831 | 32 | +67% | -65% | -63% | -59% |
| Momentum model ≥ 2% | 7580 | 59 | -4% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4632 | 43 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3022 | 28 | +34% | -68% | -68% | -63% |
| Mean-reversion model ≥ 2% | 16320 | 113 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11365 | 93 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7547 | 66 | +0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40294 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16096 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11233 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 67623 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 256 | 0% | -$4,603.90 | -56% | — |
| Sell at 2¢ | 2771 | 4% | -$7,173.44 | -88% | 47 sec |
| Sell at 3¢ | 1861 | 3% | -$7,168.11 | -88% | 48 sec |
| Sell at 5¢ | 1260 | 2% | -$7,046.90 | -86% | 62 sec |
| Sell at 10¢ | 769 | 1% | -$6,774.51 | -83% | 65 sec |
| Sell at 25¢ | 415 | 1% | -$6,254.25 | -76% | 79 sec |
| Sell at 50¢ | 266 | 0% | -$5,650.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3496 | 17 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 21935 | 116 | 7% | 3% | -48% | -86% | -86% |
| 1–2 min | 16873 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25306 | 65 | 1% | 0% | -63% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4506 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4500 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4493 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4487 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4483 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4477 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4456 | 24 | 6% | 2% | -26% | -86% | -87% |
| NEAR | 4452 | 18 | 5% | 2% | -47% | -85% | -86% |
| XRP | 4440 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2382 | 8 | 5% | 2% | -59% | -83% | -84% |
| WTI | 2369 | 8 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2323 | 9 | 5% | 2% | -54% | -83% | -84% |
| PLATINUM | 2109 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2062 | 7 | 3% | 1% | -68% | -91% | -90% |
| GBPUSD | 2003 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 1998 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1962 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1956 | 10 | 2% | 1% | -52% | -77% | -77% |
| PALLADIUM | 1894 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1523 | 7 | 2% | 1% | -57% | -90% | -90% |
| USDCAD | 1435 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1065 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 553 | 2 | 3% | 1% | -66% | -77% | -76% |
| 2YRRATE | 513 | 4 | 4% | 2% | -27% | -57% | -57% |
| 30YRRATE | 513 | 0 | 3% | 1% | -100% | -95% | -93% |
| 5YRRATE | 503 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 135 | 1 | 2% | 1% | -31% | -96% | -96% |
| USDMXN | 31 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34570 | 132 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33053 | 124 | 4% | 2% | -57% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5848 | 25 | 2% | 1% | -21% | -79% | -78% |
| 0.05–0.1% | 6399 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 9998 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12697 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5343 | 24 | 7% | 3% | -53% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16330 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16094 | 82 | 4% | 2% | -42% | -86% | -85% |
| Afternoon (12–6pm) | 16634 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18565 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,096 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/25 11:29:51 AM | 10YRRATE | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:29:51 AM | XRP | DOWN | 9 sec | -0.011% | 0¢ | ❌ Lost | $0.00 |
| 11/25 11:29:51 AM | USDCAD | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:29:36 AM | BNB | DOWN | 24 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 11/25 11:29:36 AM | COPPER | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:29:36 AM | NEAR | UP | 24 sec | -0.090% | 0¢ | ❌ Lost | $0.00 |
| 11/25 11:29:36 AM | ZEC | UP | 24 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |
| 11/25 11:29:36 AM | HYPE | UP | 24 sec | -0.053% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 11:29:17 AM | AUDUSD | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:29:17 AM | 30YRRATE | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:29:17 AM | ETH | DOWN | 42 sec | +0.152% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:29:17 AM | GOLD | DOWN | 42 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/25 11:29:01 AM | DOGE | DOWN | 58 sec | +0.162% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 11:28:45 AM | PALLADIUM | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:28:45 AM | SILVER | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:28:29 AM | GBPUSD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:28:09 AM | EURUSD | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 11:28:09 AM | NATGAS | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:28:09 AM | PLATINUM | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:27:37 AM | WTI | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:27:21 AM | BRENT | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:27:21 AM | INX | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:26:31 AM | 5YRRATE | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:26:31 AM | 2YRRATE | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:26:15 AM | USDJPY | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:14:54 AM | BNB | UP | 5 sec | -0.109% | 0¢ | ❌ Lost | $0.00 |
| 11/25 11:14:54 AM | DOGE | UP | 5 sec | -0.078% | 0¢ | ❌ Lost | $0.00 |
| 11/25 11:14:38 AM | ETH | DOWN | 22 sec | +0.064% | 0¢ | ❌ Lost | $0.00 |
| 11/25 11:14:38 AM | 2YRRATE | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:14:38 AM | XRP | DOWN | 22 sec | +0.033% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
