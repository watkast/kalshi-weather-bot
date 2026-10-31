# 15-Minute 1¢ Study

*Updated Sat Oct 31, 6:50 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3286 finished bets | 1% | $94.35 | +26% | +2.87¢ | $83.45 / $10.90 |

*Expect about **99 buys a day** (~$14.82/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3045 | $45.45 | +14% |
| Volatility model ≥ 2%, hold to the close | 6068 | $6.70 | +1% |
| Momentum model ≥ 2%, hold to the close | 5010 | -$62.05 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 40530 | 40520 | 150 (0%) | 1.07% | -$2,842.20 (-58%) | Hold to the close: -$2,842.20 (-58%) |

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
| Volatility model | 24920 | 4.7% | 0.4% (97) | -695% | ❌ Worse |
| Momentum model | 24920 | 4.6% | 0.4% (97) | -718% | ❌ Worse |
| Mean-reversion model | 24920 | 8.1% | 0.4% (97) | -844% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24920 | 97 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6068 | 53 | +1% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3286 | 33 | +26% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1862 | 20 | +53% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 5010 | 37 | -11% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3045 | 27 | +14% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 1989 | 18 | +26% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10248 | 68 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7178 | 58 | -10% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4797 | 40 | -5% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 25121 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 40520 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 150 | 0% | -$2,842.20 | -58% | — |
| Sell at 2¢ | 1568 | 4% | -$4,310.52 | -87% | 47 sec |
| Sell at 3¢ | 1078 | 3% | -$4,297.78 | -87% | 48 sec |
| Sell at 5¢ | 749 | 2% | -$4,217.35 | -85% | 63 sec |
| Sell at 10¢ | 449 | 1% | -$4,046.01 | -82% | 65 sec |
| Sell at 25¢ | 235 | 1% | -$3,744.35 | -76% | 83 sec |
| Sell at 50¢ | 154 | 0% | -$3,398.70 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1897 | 9 | 11% | 4% | -55% | -80% | -81% |
| 2–5 min | 12922 | 70 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 10253 | 35 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 15437 | 36 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2812 | 13 | 5% | 3% | -41% | -88% | -88% |
| HYPE | 2804 | 8 | 5% | 2% | -65% | -89% | -87% |
| BNB | 2802 | 16 | 5% | 2% | -28% | -85% | -84% |
| SOL | 2800 | 8 | 4% | 2% | -64% | -91% | -91% |
| DOGE | 2792 | 6 | 4% | 2% | -73% | -90% | -89% |
| ETH | 2790 | 11 | 6% | 3% | -52% | -85% | -85% |
| NEAR | 2775 | 13 | 5% | 2% | -39% | -83% | -83% |
| BTC | 2774 | 13 | 5% | 2% | -37% | -88% | -89% |
| XRP | 2772 | 11 | 3% | 1% | -51% | -89% | -89% |
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
| UP (bought YES) | 20557 | 82 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19963 | 68 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4036 | 20 | 2% | 1% | -14% | -82% | -81% |
| 0.05–0.1% | 4270 | 14 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 6456 | 22 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 7485 | 32 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2870 | 11 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10116 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10139 | 46 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 9463 | 33 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 10802 | 35 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,546 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/31 6:44:09 AM | BTC | DOWN | 50 sec | +0.003% | 16¢ | ❌ Lost | -$0.15 |
| 10/31 6:43:53 AM | XRP | DOWN | 67 sec | +0.024% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 6:41:11 AM | BNB | DOWN | 3.8 min | +0.270% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 6:40:40 AM | ZEC | DOWN | 4.3 min | +0.579% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 6:40:08 AM | SOL | DOWN | 4.8 min | +0.299% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 6:40:08 AM | DOGE | DOWN | 4.8 min | +0.227% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 6:39:36 AM | NEAR | DOWN | 5.4 min | +0.804% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 6:39:36 AM | ETH | DOWN | 5.4 min | +0.250% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 6:29:56 AM | SOL | UP | 3 sec | -0.016% | 0¢ | ❌ Lost | $0.00 |
| 10/31 6:29:56 AM | XRP | DOWN | 3 sec | +0.016% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 6:29:56 AM | ZEC | DOWN | 3 sec | +0.085% | 0¢ | ❌ Lost | $0.00 |
| 10/31 6:29:40 AM | DOGE | DOWN | 20 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/31 6:29:24 AM | ETH | DOWN | 36 sec | +0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/31 6:29:08 AM | BNB | UP | 52 sec | -0.101% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 6:28:02 AM | BTC | UP | 2.0 min | -0.088% | 2¢ | ❌ Lost | $0.00 |
| 10/31 6:26:26 AM | HYPE | DOWN | 3.5 min | +0.486% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 6:24:18 AM | NEAR | DOWN | 5.7 min | +0.989% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 5:55:55 AM | BTC | DOWN | 4.1 min | +0.123% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 5:54:31 AM | NEAR | DOWN | 5.5 min | +0.372% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 5:44:39 AM | SOL | DOWN | 21 sec | +0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/31 5:44:07 AM | XRP | DOWN | 52 sec | +0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 5:44:07 AM | DOGE | DOWN | 52 sec | +0.013% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 5:43:51 AM | NEAR | DOWN | 68 sec | +0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 5:42:44 AM | BNB | DOWN | 2.2 min | +0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 5:42:28 AM | HYPE | DOWN | 2.5 min | +0.633% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 5:42:14 AM | BTC | DOWN | 2.8 min | +0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 5:40:51 AM | ZEC | DOWN | 4.2 min | +0.435% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 5:39:13 AM | ETH | DOWN | 5.8 min | +0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 5:29:43 AM | SOL | UP | 16 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/31 5:29:43 AM | DOGE | UP | 16 sec | -0.039% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
