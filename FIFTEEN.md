# 15-Minute 1¢ Study

*Updated Sat Oct 31, 3:26 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3319 finished bets | 1% | $104.75 | +28% | +3.16¢ | $81.65 / $23.10 |

*Expect about **99 buys a day** (~$14.81/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3074 | $56.75 | +17% |
| Volatility model ≥ 2%, hold to the close | 6135 | $12.90 | +2% |
| Momentum model ≥ 2%, hold to the close | 5063 | -$53.60 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 40797 | 40787 | 151 (0%) | 1.07% | -$2,855.35 (-57%) | Hold to the close: -$2,855.35 (-57%) |

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
| Volatility model | 25187 | 4.7% | 0.4% (98) | -693% | ❌ Worse |
| Momentum model | 25187 | 4.6% | 0.4% (98) | -715% | ❌ Worse |
| Mean-reversion model | 25187 | 8.1% | 0.4% (98) | -842% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 25187 | 98 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6135 | 54 | +2% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3319 | 34 | +28% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1879 | 21 | +59% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 5063 | 38 | -9% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3074 | 28 | +17% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 2007 | 19 | +32% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10360 | 69 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7259 | 59 | -10% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4852 | 41 | -4% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 25388 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 40787 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 151 | 0% | -$2,855.35 | -57% | — |
| Sell at 2¢ | 1581 | 4% | -$4,334.29 | -87% | 47 sec |
| Sell at 3¢ | 1088 | 3% | -$4,321.03 | -87% | 48 sec |
| Sell at 5¢ | 754 | 2% | -$4,241.25 | -85% | 63 sec |
| Sell at 10¢ | 452 | 1% | -$4,069.23 | -82% | 65 sec |
| Sell at 25¢ | 237 | 1% | -$3,764.88 | -76% | 83 sec |
| Sell at 50¢ | 155 | 0% | -$3,419.10 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1907 | 9 | 11% | 4% | -55% | -80% | -81% |
| 2–5 min | 13009 | 70 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 10315 | 35 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 15545 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2843 | 13 | 5% | 3% | -41% | -88% | -88% |
| HYPE | 2834 | 8 | 5% | 2% | -65% | -89% | -87% |
| SOL | 2831 | 9 | 4% | 2% | -60% | -91% | -91% |
| BNB | 2831 | 16 | 5% | 2% | -29% | -85% | -84% |
| DOGE | 2822 | 6 | 4% | 2% | -73% | -90% | -89% |
| ETH | 2820 | 11 | 6% | 3% | -53% | -85% | -85% |
| NEAR | 2803 | 13 | 5% | 2% | -40% | -83% | -83% |
| BTC | 2802 | 13 | 5% | 2% | -37% | -88% | -89% |
| XRP | 2802 | 11 | 3% | 1% | -51% | -89% | -89% |
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
| UP (bought YES) | 20705 | 82 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 20082 | 69 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4109 | 21 | 2% | 1% | -11% | -82% | -81% |
| 0.05–0.1% | 4336 | 14 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 6530 | 22 | 4% | 2% | -58% | -90% | -89% |
| 0.2–0.5% | 7526 | 32 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2883 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10116 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10310 | 46 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 9559 | 34 | 4% | 2% | -58% | -87% | -87% |
| Evening (6pm–12am) | 10802 | 35 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,601 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/31 3:14:45 PM | DOGE | DOWN | 14 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/31 3:14:29 PM | ZEC | UP | 30 sec | -0.069% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 3:14:29 PM | ETH | UP | 30 sec | -0.054% | 0¢ | ❌ Lost | $0.00 |
| 10/31 3:13:54 PM | HYPE | DOWN | 66 sec | +0.176% | 0¢ | ❌ Lost | $0.00 |
| 10/31 3:12:49 PM | SOL | UP | 2.2 min | -0.141% | 36¢ | ❌ Lost | -$0.15 |
| 10/31 3:12:02 PM | BTC | UP | 3.0 min | -0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 3:10:55 PM | BNB | UP | 4.1 min | -0.228% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 2:59:47 PM | NEAR | UP | 13 sec | -0.109% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 2:59:47 PM | DOGE | UP | 13 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/31 2:59:47 PM | HYPE | DOWN | 13 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/31 2:59:31 PM | SOL | DOWN | 29 sec | +0.044% | 0¢ | ❌ Lost | $0.00 |
| 10/31 2:59:31 PM | ZEC | UP | 29 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/31 2:59:15 PM | XRP | UP | 45 sec | -0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 2:59:00 PM | BTC | UP | 60 sec | -0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 2:59:00 PM | ETH | DOWN | 60 sec | +0.009% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 2:57:40 PM | BNB | UP | 2.3 min | -0.104% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 2:44:40 PM | DOGE | UP | 19 sec | -0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 2:44:40 PM | BTC | UP | 19 sec | -0.016% | 0¢ | ❌ Lost | $0.00 |
| 10/31 2:44:24 PM | ZEC | UP | 35 sec | -0.101% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 2:44:24 PM | ETH | UP | 35 sec | -0.028% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 2:44:10 PM | XRP | UP | 50 sec | -0.064% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 2:43:52 PM | BNB | UP | 68 sec | -0.065% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 2:43:36 PM | HYPE | UP | 84 sec | -0.137% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 2:43:20 PM | SOL | UP | 1.7 min | -0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 2:29:52 PM | HYPE | DOWN | 8 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/31 2:29:36 PM | SOL | UP | 24 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/31 2:29:36 PM | XRP | UP | 24 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/31 2:29:21 PM | NEAR | UP | 38 sec | -0.145% | 0¢ | ❌ Lost | $0.00 |
| 10/31 2:29:03 PM | BTC | UP | 57 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/31 2:28:16 PM | ZEC | UP | 1.7 min | -0.283% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
