# 15-Minute 1¢ Study

*Updated Sat Oct 31, 1:53 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

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
| Momentum model ≥ 5%, hold to the close | 3071 | $57.05 | +17% |
| Volatility model ≥ 2%, hold to the close | 6129 | $13.80 | +2% |
| Momentum model ≥ 2%, hold to the close | 5060 | -$53.30 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 40746 | 40736 | 151 (0%) | 1.07% | -$2,850.40 (-57%) | Hold to the close: -$2,850.40 (-57%) |

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
| Volatility model | 25136 | 4.7% | 0.4% (98) | -693% | ❌ Worse |
| Momentum model | 25136 | 4.6% | 0.4% (98) | -716% | ❌ Worse |
| Mean-reversion model | 25136 | 8.1% | 0.4% (98) | -842% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 25136 | 98 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6129 | 54 | +2% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3318 | 34 | +28% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1878 | 21 | +59% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 5060 | 38 | -9% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3071 | 28 | +17% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 2006 | 19 | +32% | -73% | -72% | -67% |
| Mean-reversion model ≥ 2% | 10351 | 69 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7254 | 59 | -10% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4849 | 41 | -4% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 25337 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 40736 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 151 | 0% | -$2,850.40 | -57% | — |
| Sell at 2¢ | 1577 | 4% | -$4,330.38 | -87% | 47 sec |
| Sell at 3¢ | 1085 | 3% | -$4,317.25 | -87% | 48 sec |
| Sell at 5¢ | 752 | 2% | -$4,237.60 | -85% | 63 sec |
| Sell at 10¢ | 451 | 1% | -$4,065.59 | -82% | 65 sec |
| Sell at 25¢ | 236 | 1% | -$3,763.24 | -76% | 82 sec |
| Sell at 50¢ | 155 | 0% | -$3,414.15 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1907 | 9 | 11% | 4% | -55% | -80% | -81% |
| 2–5 min | 12991 | 70 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 10305 | 35 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 15522 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2837 | 13 | 5% | 3% | -41% | -88% | -88% |
| HYPE | 2828 | 8 | 5% | 2% | -65% | -89% | -87% |
| SOL | 2825 | 9 | 4% | 2% | -60% | -91% | -91% |
| BNB | 2825 | 16 | 5% | 2% | -29% | -85% | -84% |
| DOGE | 2816 | 6 | 4% | 2% | -73% | -90% | -89% |
| ETH | 2814 | 11 | 6% | 3% | -52% | -85% | -85% |
| NEAR | 2799 | 13 | 5% | 2% | -40% | -83% | -83% |
| XRP | 2797 | 11 | 3% | 1% | -51% | -89% | -89% |
| BTC | 2796 | 13 | 5% | 2% | -37% | -88% | -89% |
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
| UP (bought YES) | 20667 | 82 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 20069 | 69 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4092 | 21 | 2% | 1% | -11% | -82% | -81% |
| 0.05–0.1% | 4327 | 14 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 6511 | 22 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 7521 | 32 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2882 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10116 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10310 | 46 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 9508 | 34 | 4% | 2% | -58% | -87% | -87% |
| Evening (6pm–12am) | 10802 | 35 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,590 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
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
| 10/31 1:27:33 PM | DOGE | UP | 2.5 min | -0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:25:27 PM | BTC | UP | 4.5 min | -0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:24:55 PM | ETH | UP | 5.1 min | -0.182% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:24:55 PM | NEAR | UP | 5.1 min | -0.847% | 2¢ | ❌ Lost | -$0.15 |
| 10/31 1:24:38 PM | SOL | UP | 5.3 min | -0.171% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:24:38 PM | XRP | UP | 5.3 min | -0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:24:38 PM | BNB | UP | 5.3 min | -0.151% | 2¢ | ❌ Lost | -$0.15 |
| 10/31 1:14:22 PM | HYPE | UP | 37 sec | -0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:14:22 PM | SOL | DOWN | 37 sec | +0.063% | 0¢ | ❌ Lost | $0.00 |
| 10/31 1:13:48 PM | DOGE | DOWN | 72 sec | +0.041% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:13:32 PM | BTC | DOWN | 88 sec | +0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/31 1:13:16 PM | ZEC | DOWN | 1.7 min | +0.122% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:13:16 PM | BNB | DOWN | 1.7 min | +0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:12:45 PM | NEAR | UP | 2.2 min | -0.473% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 1:12:27 PM | XRP | DOWN | 2.5 min | +0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 1:11:56 PM | ETH | DOWN | 3.0 min | +0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 12:59:52 PM | XRP | DOWN | 8 sec | +0.016% | 0¢ | ❌ Lost | $0.00 |
| 10/31 12:59:52 PM | NEAR | DOWN | 8 sec | -0.064% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
