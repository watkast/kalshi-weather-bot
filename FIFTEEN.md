# 15-Minute 1¢ Study

*Updated Sat Oct 31, 11:13 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3353 finished bets | 1% | $115.60 | +31% | +3.45¢ | $80.00 / $35.60 |

*Expect about **99 buys a day** (~$14.82/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3102 | $54.20 | +16% |
| Volatility model ≥ 2%, hold to the close | 6192 | $34.60 | +5% |
| Momentum model ≥ 2%, hold to the close | 5113 | -$45.00 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41072 | 41060 | 153 (0%) | 1.07% | -$2,857.65 (-57%) | Hold to the close: -$2,857.65 (-57%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 25459 | 4.7% | 0.4% (100) | -692% | ❌ Worse |
| Momentum model | 25459 | 4.6% | 0.4% (100) | -715% | ❌ Worse |
| Mean-reversion model | 25459 | 8.1% | 0.4% (100) | -840% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 25459 | 100 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6192 | 56 | +5% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3353 | 35 | +31% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1900 | 21 | +58% | -69% | -68% | -64% |
| Momentum model ≥ 2% | 5113 | 39 | -8% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3102 | 28 | +16% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 2028 | 19 | +31% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10472 | 71 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7335 | 61 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4906 | 43 | -0% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 25661 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41060 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 153 | 0% | -$2,857.65 | -57% | — |
| Sell at 2¢ | 1596 | 4% | -$4,360.69 | -87% | 47 sec |
| Sell at 3¢ | 1098 | 3% | -$4,347.43 | -87% | 48 sec |
| Sell at 5¢ | 760 | 2% | -$4,267.65 | -85% | 63 sec |
| Sell at 10¢ | 456 | 1% | -$4,094.29 | -82% | 65 sec |
| Sell at 25¢ | 240 | 1% | -$3,785.25 | -76% | 82 sec |
| Sell at 50¢ | 157 | 0% | -$3,435.90 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1928 | 9 | 11% | 4% | -56% | -80% | -81% |
| 2–5 min | 13108 | 72 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10395 | 35 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 15618 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2874 | 13 | 5% | 3% | -42% | -88% | -88% |
| SOL | 2862 | 9 | 4% | 2% | -60% | -91% | -91% |
| HYPE | 2862 | 8 | 5% | 2% | -65% | -89% | -87% |
| BNB | 2861 | 17 | 5% | 2% | -26% | -85% | -84% |
| DOGE | 2852 | 6 | 4% | 2% | -74% | -90% | -89% |
| ETH | 2851 | 11 | 6% | 3% | -53% | -85% | -85% |
| NEAR | 2834 | 14 | 5% | 2% | -36% | -83% | -83% |
| BTC | 2833 | 13 | 5% | 2% | -38% | -88% | -89% |
| XRP | 2832 | 11 | 3% | 1% | -52% | -89% | -89% |
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
| UP (bought YES) | 20842 | 83 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 20218 | 70 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4169 | 21 | 2% | 1% | -13% | -82% | -81% |
| 0.05–0.1% | 4393 | 15 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 6616 | 22 | 4% | 2% | -59% | -90% | -90% |
| 0.2–0.5% | 7592 | 33 | 7% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2886 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10116 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10310 | 46 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 9655 | 34 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 10979 | 37 | 3% | 2% | -61% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,666 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/31 11:12:56 PM | BTC | DOWN | 2.0 min | +0.030% | — | In play | — |
| 10/31 11:11:18 PM | ETH | DOWN | 3.7 min | +0.100% | — | In play | — |
| 10/31 10:59:45 PM | XRP | DOWN | 14 sec | -0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/31 10:59:12 PM | SOL | UP | 47 sec | -0.072% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:59:12 PM | NEAR | UP | 47 sec | -0.319% | 0¢ | ❌ Lost | $0.00 |
| 10/31 10:59:12 PM | DOGE | UP | 47 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/31 10:58:53 PM | ETH | UP | 66 sec | -0.038% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 10:58:53 PM | BNB | UP | 66 sec | -0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/31 10:58:37 PM | HYPE | DOWN | 82 sec | +0.116% | 0¢ | ❌ Lost | $0.00 |
| 10/31 10:58:37 PM | BTC | UP | 82 sec | -0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:56:26 PM | NEAR | DOWN | 3.5 min | +0.225% | 100¢ | ✅ Won | $13.85 |
| 10/31 10:54:36 PM | ZEC | DOWN | 5.4 min | +0.472% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:44:50 PM | BNB | UP | 9 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/31 10:44:34 PM | HYPE | UP | 25 sec | -0.063% | 0¢ | ❌ Lost | $0.00 |
| 10/31 10:44:18 PM | BTC | DOWN | 41 sec | +0.016% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 10:44:18 PM | NEAR | UP | 41 sec | -0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:43:13 PM | ETH | UP | 1.8 min | -0.071% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:43:13 PM | XRP | UP | 1.8 min | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:43:13 PM | ZEC | UP | 1.8 min | -0.136% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:42:41 PM | SOL | UP | 2.3 min | -0.156% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:42:18 PM | DOGE | UP | 2.7 min | -0.131% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 10:26:48 PM | BNB | DOWN | 3.2 min | +0.199% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 10:26:48 PM | BTC | DOWN | 3.2 min | +0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:26:48 PM | NEAR | DOWN | 3.2 min | +0.308% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:26:32 PM | ETH | DOWN | 3.5 min | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:25:27 PM | ZEC | DOWN | 4.5 min | +0.424% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:25:11 PM | XRP | DOWN | 4.8 min | +0.136% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:25:11 PM | HYPE | DOWN | 4.8 min | +0.377% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:24:39 PM | SOL | DOWN | 5.3 min | +0.207% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:24:39 PM | DOGE | DOWN | 5.3 min | +0.207% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
