# 15-Minute 1¢ Study

*Updated Thu Nov 26, 7:51 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4945 finished bets | 1% | $204.25 | +38% | +4.13¢ | $84.40 / $119.85 |

*Expect about **83 buys a day** (~$12.50/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4687 | $103.70 | +21% |
| Volatility model ≥ 2%, hold to the close | 9210 | $38.40 | +4% |
| Momentum model ≥ 2%, hold to the close | 7667 | -$42.95 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 68455 | 68421 | 257 (0%) | 1.07% | -$4,685.00 (-57%) | Hold to the close: -$4,685.00 (-57%) |

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
| Volatility model | 40456 | 4.5% | 0.4% (165) | -654% | ❌ Worse |
| Momentum model | 40456 | 4.4% | 0.4% (165) | -677% | ❌ Worse |
| Mean-reversion model | 40456 | 7.9% | 0.4% (165) | -793% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40456 | 165 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9210 | 81 | +4% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 4945 | 53 | +38% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2865 | 32 | +65% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 7667 | 59 | -5% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4687 | 43 | +21% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3055 | 28 | +33% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16480 | 113 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11472 | 93 | -10% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 7615 | 66 | -1% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40662 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16341 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11418 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 68421 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 257 | 0% | -$4,685.00 | -57% | — |
| Sell at 2¢ | 2801 | 4% | -$7,246.74 | -87% | 47 sec |
| Sell at 3¢ | 1879 | 3% | -$7,242.19 | -87% | 48 sec |
| Sell at 5¢ | 1271 | 2% | -$7,120.85 | -86% | 62 sec |
| Sell at 10¢ | 779 | 1% | -$6,842.51 | -83% | 65 sec |
| Sell at 25¢ | 422 | 1% | -$6,312.18 | -76% | 80 sec |
| Sell at 50¢ | 269 | 0% | -$5,711.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3527 | 17 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 22184 | 116 | 7% | 3% | -48% | -86% | -86% |
| 1–2 min | 17059 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25638 | 66 | 1% | 0% | -63% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4548 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4541 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4534 | 20 | 4% | 2% | -43% | -86% | -86% |
| BNB | 4526 | 22 | 5% | 2% | -38% | -85% | -85% |
| DOGE | 4524 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4518 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4497 | 24 | 6% | 2% | -27% | -86% | -87% |
| NEAR | 4492 | 18 | 5% | 2% | -47% | -86% | -86% |
| XRP | 4482 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2414 | 8 | 5% | 2% | -59% | -83% | -84% |
| WTI | 2396 | 9 | 4% | 2% | -54% | -86% | -87% |
| SILVER | 2360 | 9 | 5% | 2% | -54% | -83% | -84% |
| PLATINUM | 2140 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2092 | 7 | 2% | 1% | -69% | -91% | -90% |
| GBPUSD | 2037 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 2027 | 6 | 2% | 1% | -72% | -79% | -79% |
| USDJPY | 1987 | 6 | 2% | 1% | -72% | -97% | -96% |
| NATGAS | 1984 | 10 | 2% | 1% | -53% | -77% | -77% |
| PALLADIUM | 1927 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1556 | 7 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1464 | 1 | 3% | 1% | -94% | -96% | -96% |
| BRENT | 1093 | 1 | 2% | 1% | -91% | -96% | -96% |
| 10YRRATE | 557 | 2 | 3% | 1% | -66% | -78% | -76% |
| 30YRRATE | 518 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 515 | 4 | 4% | 2% | -28% | -57% | -57% |
| 5YRRATE | 506 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 139 | 1 | 2% | 1% | -33% | -96% | -96% |
| USDMXN | 47 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34922 | 133 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33499 | 124 | 4% | 2% | -57% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5900 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6465 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 10078 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12817 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5393 | 24 | 7% | 3% | -53% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16499 | 51 | 4% | 2% | -65% | -87% | -88% |
| Morning (6am–12pm) | 16246 | 82 | 4% | 2% | -42% | -86% | -85% |
| Afternoon (12–6pm) | 16751 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18925 | 51 | 4% | 2% | -69% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,072 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/26 7:44:46 AM | NATGAS | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:44:46 AM | COPPER | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:44:46 AM | USDJPY | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:44:46 AM | BRENT | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:44:30 AM | USDMXN | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:44:30 AM | SILVER | DOWN | 29 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/26 7:44:14 AM | HYPE | UP | 46 sec | -0.217% | 0¢ | ❌ Lost | $0.00 |
| 11/26 7:44:14 AM | ETH | UP | 46 sec | -0.103% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:44:14 AM | WTI | UP | 46 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/26 7:43:41 AM | AUDUSD | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:43:41 AM | DOGE | UP | 79 sec | -0.242% | 0¢ | ❌ Lost | $0.00 |
| 11/26 7:42:21 AM | EURUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:42:05 AM | ZEC | UP | 2.9 min | -1.278% | 0¢ | ❌ Lost | $0.00 |
| 11/26 7:41:50 AM | NEAR | UP | 3.1 min | -0.672% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 7:40:57 AM | USDCAD | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:40:57 AM | GBPUSD | UP | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:29:46 AM | USDMXN | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:29:46 AM | SILVER | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:29:14 AM | NATGAS | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:28:57 AM | SOL | UP | 63 sec | -0.188% | 0¢ | ❌ Lost | $0.00 |
| 11/26 7:28:57 AM | GBPUSD | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:28:41 AM | DOGE | DOWN | 79 sec | +0.095% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:28:25 AM | BTC | UP | 1.6 min | -0.121% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 7:28:09 AM | ETH | UP | 1.9 min | -0.179% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:27:52 AM | NEAR | UP | 2.1 min | -0.351% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 7:27:20 AM | BRENT | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:26:30 AM | XRP | UP | 3.5 min | -0.252% | 2¢ | ❌ Lost | -$0.15 |
| 11/26 7:26:14 AM | BNB | UP | 3.8 min | -0.259% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 7:25:58 AM | HYPE | UP | 4.0 min | -0.439% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 7:25:41 AM | ZEC | UP | 4.3 min | -0.928% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
