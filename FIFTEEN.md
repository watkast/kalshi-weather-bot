# 15-Minute 1¢ Study

*Updated Sat Oct 31, 2:24 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3318 finished bets | 1% | $104.90 | +28% | +3.16¢ | $81.65 / $23.25 |

*Expect about **99 buys a day** (~$14.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3073 | $56.90 | +17% |
| Volatility model ≥ 2%, hold to the close | 6131 | $13.50 | +2% |
| Momentum model ≥ 2%, hold to the close | 5062 | -$53.45 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 40764 | 40754 | 151 (0%) | 1.07% | -$2,852.50 (-57%) | Hold to the close: -$2,852.50 (-57%) |

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
| Volatility model | 25154 | 4.7% | 0.4% (98) | -693% | ❌ Worse |
| Momentum model | 25154 | 4.6% | 0.4% (98) | -715% | ❌ Worse |
| Mean-reversion model | 25154 | 8.1% | 0.4% (98) | -842% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 25154 | 98 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6131 | 54 | +2% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3318 | 34 | +28% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1878 | 21 | +59% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 5062 | 38 | -9% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3073 | 28 | +17% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 2006 | 19 | +32% | -73% | -72% | -67% |
| Mean-reversion model ≥ 2% | 10354 | 69 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7256 | 59 | -10% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4849 | 41 | -4% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 25355 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 40754 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 151 | 0% | -$2,852.50 | -57% | — |
| Sell at 2¢ | 1580 | 4% | -$4,331.70 | -87% | 47 sec |
| Sell at 3¢ | 1087 | 3% | -$4,318.57 | -87% | 48 sec |
| Sell at 5¢ | 753 | 2% | -$4,239.05 | -85% | 63 sec |
| Sell at 10¢ | 451 | 1% | -$4,067.69 | -82% | 65 sec |
| Sell at 25¢ | 236 | 1% | -$3,765.34 | -76% | 82 sec |
| Sell at 50¢ | 155 | 0% | -$3,416.25 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1907 | 9 | 11% | 4% | -55% | -80% | -81% |
| 2–5 min | 13002 | 70 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 10308 | 35 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 15526 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2839 | 13 | 5% | 3% | -41% | -88% | -88% |
| HYPE | 2830 | 8 | 5% | 2% | -65% | -89% | -87% |
| SOL | 2827 | 9 | 4% | 2% | -60% | -91% | -91% |
| BNB | 2827 | 16 | 5% | 2% | -29% | -85% | -84% |
| DOGE | 2818 | 6 | 4% | 2% | -73% | -90% | -89% |
| ETH | 2816 | 11 | 6% | 3% | -52% | -85% | -85% |
| NEAR | 2801 | 13 | 5% | 2% | -40% | -83% | -83% |
| XRP | 2799 | 11 | 3% | 1% | -51% | -89% | -89% |
| BTC | 2798 | 13 | 5% | 2% | -37% | -88% | -89% |
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
| UP (bought YES) | 20678 | 82 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 20076 | 69 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4095 | 21 | 2% | 1% | -11% | -82% | -81% |
| 0.05–0.1% | 4329 | 14 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 6520 | 22 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 7524 | 32 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2883 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10116 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10310 | 46 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 9526 | 34 | 4% | 2% | -58% | -87% | -87% |
| Evening (6pm–12am) | 10802 | 35 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,592 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/31 2:14:54 PM | SOL | DOWN | 5 sec | +0.016% | 0¢ | ❌ Lost | $0.00 |
| 10/31 2:14:54 PM | HYPE | UP | 5 sec | -0.027% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 2:14:38 PM | BNB | DOWN | 21 sec | +0.028% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 2:14:38 PM | NEAR | UP | 21 sec | -0.336% | 0¢ | ❌ Lost | $0.00 |
| 10/31 2:13:21 PM | ZEC | DOWN | 1.6 min | +0.217% | 4¢ | ❌ Lost | -$0.15 |
| 10/31 2:11:42 PM | XRP | DOWN | 3.3 min | +0.104% | 5¢ | ❌ Lost | -$0.15 |
| 10/31 2:11:10 PM | DOGE | DOWN | 3.8 min | +0.151% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 2:11:10 PM | BTC | DOWN | 3.8 min | +0.067% | 3¢ | ❌ Lost | -$0.15 |
| 10/31 2:10:05 PM | ETH | DOWN | 4.9 min | +0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:58:51 PM | HYPE | UP | 68 sec | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/31 1:58:35 PM | NEAR | UP | 84 sec | -0.613% | 0¢ | ❌ Lost | $0.00 |
| 10/31 1:57:29 PM | BNB | UP | 2.5 min | -0.163% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 1:57:29 PM | DOGE | UP | 2.5 min | -0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:57:29 PM | BTC | UP | 2.5 min | -0.063% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:56:25 PM | SOL | UP | 3.6 min | -0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:56:25 PM | ETH | UP | 3.6 min | -0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:55:18 PM | ZEC | UP | 4.7 min | -0.411% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:55:04 PM | XRP | UP | 4.9 min | -0.184% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:44:57 PM | SOL | UP | 2 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/31 1:44:57 PM | BNB | DOWN | 2 sec | -0.014% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 1:44:41 PM | SOL | DOWN | 18 sec | -0.010% | 100¢ | ✅ Won | $13.85 |
| 10/31 1:44:41 PM | HYPE | DOWN | 18 sec | -0.011% | 0¢ | ❌ Lost | $0.00 |
| 10/31 1:44:25 PM | XRP | UP | 34 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/31 1:44:09 PM | NEAR | UP | 51 sec | -0.244% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:43:53 PM | ZEC | UP | 67 sec | -0.097% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:43:37 PM | DOGE | UP | 83 sec | -0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:43:37 PM | BTC | DOWN | 83 sec | +0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:43:10 PM | ETH | DOWN | 1.8 min | +0.025% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 1:29:55 PM | HYPE | DOWN | 5 sec | +0.030% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 1:29:08 PM | ZEC | UP | 51 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
