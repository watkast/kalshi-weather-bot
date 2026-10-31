# 15-Minute 1¢ Study

*Updated Sat Oct 31, 3:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3266 finished bets | 1% | $96.90 | +27% | +2.97¢ | $84.95 / $11.95 |

*Expect about **99 buys a day** (~$14.79/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3027 | $47.55 | +14% |
| Volatility model ≥ 2%, hold to the close | 6041 | $10.15 | +1% |
| Momentum model ≥ 2%, hold to the close | 4988 | -$59.50 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 40440 | 40430 | 150 (0%) | 1.07% | -$2,832.75 (-57%) | Hold to the close: -$2,832.75 (-57%) |

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
| Volatility model | 24830 | 4.7% | 0.4% (97) | -690% | ❌ Worse |
| Momentum model | 24830 | 4.6% | 0.4% (97) | -713% | ❌ Worse |
| Mean-reversion model | 24830 | 8.1% | 0.4% (97) | -838% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24830 | 97 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6041 | 53 | +1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3266 | 33 | +27% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1850 | 20 | +54% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 4988 | 37 | -10% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3027 | 27 | +14% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1976 | 18 | +27% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10208 | 68 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7146 | 58 | -10% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4775 | 40 | -5% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 25031 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 40430 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 150 | 0% | -$2,832.75 | -57% | — |
| Sell at 2¢ | 1562 | 4% | -$4,302.63 | -87% | 47 sec |
| Sell at 3¢ | 1073 | 3% | -$4,290.28 | -87% | 48 sec |
| Sell at 5¢ | 746 | 2% | -$4,209.85 | -85% | 63 sec |
| Sell at 10¢ | 448 | 1% | -$4,037.87 | -82% | 65 sec |
| Sell at 25¢ | 235 | 1% | -$3,734.90 | -76% | 83 sec |
| Sell at 50¢ | 154 | 0% | -$3,389.25 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1890 | 9 | 11% | 4% | -55% | -80% | -81% |
| 2–5 min | 12893 | 70 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10234 | 35 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15402 | 36 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2802 | 13 | 5% | 3% | -41% | -88% | -88% |
| HYPE | 2795 | 8 | 5% | 2% | -65% | -89% | -87% |
| BNB | 2792 | 16 | 5% | 3% | -28% | -85% | -83% |
| SOL | 2790 | 8 | 4% | 2% | -64% | -91% | -91% |
| DOGE | 2782 | 6 | 4% | 2% | -73% | -90% | -89% |
| ETH | 2780 | 11 | 6% | 3% | -52% | -85% | -85% |
| NEAR | 2764 | 13 | 5% | 2% | -39% | -83% | -83% |
| BTC | 2764 | 13 | 5% | 2% | -37% | -88% | -89% |
| XRP | 2762 | 11 | 3% | 1% | -51% | -89% | -89% |
| GOLD | 1515 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1481 | 7 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1476 | 4 | 3% | 1% | -67% | -93% | -93% |
| PLATINUM | 1314 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1253 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1249 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1212 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1185 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1178 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1171 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 705 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 685 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 283 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20524 | 82 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19906 | 68 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4007 | 20 | 2% | 1% | -13% | -82% | -81% |
| 0.05–0.1% | 4252 | 14 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 6434 | 22 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 7469 | 32 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2865 | 11 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10043 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10122 | 46 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9463 | 33 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 10802 | 35 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,531 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/31 3:44:46 AM | BTC | UP | 14 sec | -0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 3:44:30 AM | DOGE | UP | 30 sec | -0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 3:44:30 AM | NEAR | DOWN | 30 sec | +0.030% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 3:44:30 AM | SOL | UP | 30 sec | -0.055% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 3:44:14 AM | ZEC | UP | 46 sec | -0.135% | 0¢ | ❌ Lost | $0.00 |
| 10/31 3:41:44 AM | HYPE | UP | 3.2 min | -0.418% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 3:29:13 AM | ZEC | DOWN | 46 sec | +0.153% | 0¢ | ❌ Lost | $0.00 |
| 10/31 3:29:13 AM | BNB | DOWN | 46 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/31 3:29:13 AM | SOL | DOWN | 46 sec | +0.006% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 3:29:13 AM | BTC | DOWN | 46 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/31 3:28:54 AM | DOGE | DOWN | 66 sec | -0.004% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 3:28:54 AM | HYPE | UP | 66 sec | -0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 3:27:49 AM | ETH | DOWN | 2.2 min | +0.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 3:26:13 AM | XRP | DOWN | 3.8 min | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 3:14:55 AM | DOGE | DOWN | 4 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/31 3:14:23 AM | NEAR | UP | 36 sec | -0.125% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 3:14:23 AM | XRP | UP | 36 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/31 3:14:23 AM | HYPE | UP | 36 sec | -0.101% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 3:13:17 AM | ETH | DOWN | 1.7 min | +0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 3:12:28 AM | SOL | DOWN | 2.5 min | +0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 3:11:00 AM | BTC | DOWN | 4.0 min | +0.088% | 2¢ | ❌ Lost | -$0.15 |
| 10/31 3:08:22 AM | ZEC | DOWN | 6.6 min | +0.725% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 3:07:34 AM | BNB | DOWN | 7.4 min | +0.267% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 2:59:31 AM | NEAR | UP | 29 sec | -0.150% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 2:59:15 AM | SOL | DOWN | 45 sec | +0.004% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 2:58:10 AM | BTC | DOWN | 1.8 min | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 2:58:10 AM | ZEC | DOWN | 1.8 min | +0.274% | 0¢ | ❌ Lost | $0.00 |
| 10/31 2:57:06 AM | ETH | DOWN | 2.9 min | +0.067% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 2:57:06 AM | XRP | DOWN | 2.9 min | +0.081% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 2:55:47 AM | DOGE | DOWN | 4.2 min | +0.178% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
