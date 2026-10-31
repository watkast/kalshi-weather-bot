# 15-Minute 1¢ Study

*Updated Fri Oct 30, 11:30 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3234 finished bets | 1% | $86.80 | +24% | +2.68¢ | $72.60 / $14.20 |

*Expect about **98 buys a day** (~$14.72/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2999 | $36.85 | +11% |
| Volatility model ≥ 2%, hold to the close | 5994 | $2.00 | +0% |
| Volatility model ≥ 5%, sell at 50¢ | 3234 | -$67.95 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 40294 | 40283 | 149 (0%) | 1.07% | -$2,831.30 (-58%) | Hold to the close: -$2,831.30 (-58%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 24683 | 4.7% | 0.4% (96) | -687% | ❌ Worse |
| Momentum model | 24683 | 4.6% | 0.4% (96) | -710% | ❌ Worse |
| Mean-reversion model | 24683 | 8.1% | 0.4% (96) | -835% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24683 | 96 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5994 | 52 | +0% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3234 | 32 | +24% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1827 | 19 | +49% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 4946 | 36 | -12% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2999 | 26 | +11% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1953 | 17 | +21% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10144 | 67 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7098 | 57 | -11% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4735 | 39 | -6% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24884 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 40283 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 149 | 0% | -$2,831.30 | -58% | — |
| Sell at 2¢ | 1555 | 4% | -$4,289.00 | -87% | 47 sec |
| Sell at 3¢ | 1069 | 3% | -$4,276.39 | -87% | 48 sec |
| Sell at 5¢ | 745 | 2% | -$4,195.05 | -85% | 63 sec |
| Sell at 10¢ | 447 | 1% | -$4,023.73 | -82% | 65 sec |
| Sell at 25¢ | 234 | 1% | -$3,722.76 | -76% | 83 sec |
| Sell at 50¢ | 153 | 0% | -$3,380.55 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1881 | 9 | 11% | 4% | -54% | -80% | -81% |
| 2–5 min | 12854 | 70 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10196 | 35 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15341 | 35 | 1% | 0% | -68% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2785 | 13 | 5% | 3% | -40% | -88% | -88% |
| HYPE | 2777 | 8 | 5% | 2% | -64% | -89% | -87% |
| BNB | 2776 | 16 | 5% | 3% | -28% | -85% | -84% |
| SOL | 2772 | 7 | 4% | 2% | -68% | -91% | -91% |
| DOGE | 2766 | 6 | 4% | 2% | -73% | -90% | -89% |
| ETH | 2764 | 11 | 6% | 3% | -52% | -85% | -85% |
| NEAR | 2749 | 13 | 5% | 2% | -38% | -83% | -83% |
| BTC | 2748 | 13 | 5% | 2% | -36% | -88% | -89% |
| XRP | 2747 | 11 | 3% | 1% | -51% | -89% | -89% |
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
| UP (bought YES) | 20457 | 81 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 19826 | 68 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3967 | 19 | 2% | 1% | -17% | -81% | -81% |
| 0.05–0.1% | 4217 | 14 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 6403 | 22 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 7435 | 32 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2858 | 11 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9916 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10122 | 46 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9463 | 33 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 10782 | 34 | 3% | 2% | -64% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,503 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 11:29:58 PM | ZEC | UP | 2 sec | -0.008% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 11:29:42 PM | DOGE | DOWN | 18 sec | -0.068% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 11:29:42 PM | XRP | DOWN | 18 sec | -0.008% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 11:29:11 PM | HYPE | DOWN | 49 sec | +0.078% | 0¢ | In play | — |
| 10/30 11:28:39 PM | ETH | DOWN | 80 sec | +0.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 11:28:23 PM | BTC | DOWN | 1.6 min | +0.051% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 11:28:23 PM | SOL | DOWN | 1.6 min | +0.116% | 0¢ | ❌ Lost | $0.00 |
| 10/30 11:27:49 PM | BNB | DOWN | 2.2 min | +0.023% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 11:26:30 PM | NEAR | DOWN | 3.5 min | +0.374% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 11:13:52 PM | NEAR | UP | 68 sec | -0.373% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 11:13:36 PM | HYPE | DOWN | 84 sec | +0.268% | 0¢ | ❌ Lost | $0.00 |
| 10/30 11:12:17 PM | ZEC | DOWN | 2.7 min | +0.367% | 5¢ | ❌ Lost | -$0.15 |
| 10/30 11:12:01 PM | BTC | DOWN | 3.0 min | +0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 11:11:29 PM | ETH | DOWN | 3.5 min | +0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 11:11:29 PM | DOGE | DOWN | 3.5 min | +0.177% | 2¢ | ❌ Lost | -$0.15 |
| 10/30 11:11:29 PM | XRP | DOWN | 3.5 min | +0.153% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 11:10:57 PM | SOL | DOWN | 4.0 min | +0.273% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 11:09:58 PM | BNB | DOWN | 5.0 min | +0.181% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 10:59:44 PM | HYPE | UP | 16 sec | -0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/30 10:59:28 PM | ZEC | UP | 32 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/30 10:59:13 PM | DOGE | UP | 47 sec | -0.116% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:58:56 PM | SOL | DOWN | 63 sec | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 10:58:24 PM | ETH | DOWN | 1.6 min | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 10:57:49 PM | BNB | DOWN | 2.2 min | +0.077% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:57:33 PM | XRP | DOWN | 2.4 min | +0.113% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 10:57:17 PM | NEAR | DOWN | 2.7 min | +0.384% | 0¢ | ❌ Lost | $0.00 |
| 10/30 10:42:18 PM | BTC | UP | 2.7 min | -0.131% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 10:42:18 PM | ETH | UP | 2.7 min | -0.131% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 10:41:44 PM | XRP | UP | 3.3 min | -0.209% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 10:41:44 PM | DOGE | UP | 3.3 min | -0.281% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
