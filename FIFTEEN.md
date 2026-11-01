# 15-Minute 1¢ Study

*Updated Sun Nov 1, 1:11 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3375 finished bets | 1% | $113.20 | +30% | +3.35¢ | $78.80 / $34.40 |

*Expect about **99 buys a day** (~$14.87/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3119 | $52.70 | +16% |
| Volatility model ≥ 2%, hold to the close | 6224 | $30.70 | +4% |
| Momentum model ≥ 2%, hold to the close | 5139 | -$47.70 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41167 | 41156 | 153 (0%) | 1.07% | -$2,868.60 (-57%) | Hold to the close: -$2,868.60 (-57%) |

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
| Volatility model | 25555 | 4.7% | 0.4% (100) | -696% | ❌ Worse |
| Momentum model | 25555 | 4.6% | 0.4% (100) | -719% | ❌ Worse |
| Mean-reversion model | 25555 | 8.1% | 0.4% (100) | -845% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 25555 | 100 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6224 | 56 | +4% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3375 | 35 | +30% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1915 | 21 | +57% | -70% | -68% | -64% |
| Momentum model ≥ 2% | 5139 | 39 | -8% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3119 | 28 | +16% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 2040 | 19 | +30% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10527 | 71 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7377 | 61 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4938 | 43 | -1% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 25757 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41156 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 153 | 0% | -$2,868.60 | -57% | — |
| Sell at 2¢ | 1601 | 4% | -$4,370.34 | -87% | 47 sec |
| Sell at 3¢ | 1100 | 3% | -$4,357.60 | -87% | 48 sec |
| Sell at 5¢ | 762 | 2% | -$4,277.30 | -85% | 63 sec |
| Sell at 10¢ | 457 | 1% | -$4,103.93 | -82% | 65 sec |
| Sell at 25¢ | 240 | 1% | -$3,796.20 | -76% | 82 sec |
| Sell at 50¢ | 157 | 0% | -$3,446.85 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1936 | 9 | 11% | 4% | -56% | -80% | -81% |
| 2–5 min | 13155 | 72 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10418 | 35 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 15636 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2885 | 13 | 5% | 3% | -42% | -88% | -88% |
| SOL | 2873 | 9 | 4% | 2% | -60% | -91% | -91% |
| HYPE | 2873 | 8 | 5% | 3% | -65% | -89% | -87% |
| BNB | 2872 | 17 | 5% | 2% | -26% | -85% | -84% |
| DOGE | 2863 | 6 | 4% | 2% | -74% | -90% | -89% |
| ETH | 2861 | 11 | 7% | 3% | -53% | -85% | -85% |
| BTC | 2844 | 13 | 5% | 2% | -39% | -88% | -89% |
| NEAR | 2843 | 14 | 5% | 2% | -36% | -83% | -83% |
| XRP | 2843 | 11 | 3% | 1% | -52% | -89% | -89% |
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
| UP (bought YES) | 20885 | 83 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 20271 | 70 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4188 | 21 | 2% | 1% | -13% | -82% | -81% |
| 0.05–0.1% | 4413 | 15 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 6656 | 22 | 4% | 2% | -59% | -90% | -90% |
| 0.2–0.5% | 7608 | 33 | 7% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2887 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10185 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10310 | 46 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 9655 | 34 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 11006 | 37 | 3% | 2% | -61% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,682 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 1:11:24 AM | DOGE | UP | 3.6 min | -0.090% | — | In play | — |
| 11/1 1:59:09 AM | HYPE | UP | 51 sec | -0.038% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 1:58:51 AM | XRP | DOWN | 69 sec | +0.056% | 0¢ | ❌ Lost | $0.00 |
| 11/1 1:58:35 AM | NEAR | DOWN | 85 sec | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:58:04 AM | DOGE | DOWN | 1.9 min | +0.037% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:58:04 AM | SOL | DOWN | 1.9 min | +0.073% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:56:50 AM | ZEC | DOWN | 3.2 min | +0.192% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:56:18 AM | ETH | DOWN | 3.7 min | +0.083% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:56:04 AM | BNB | DOWN | 3.9 min | +0.301% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:55:33 AM | BTC | DOWN | 4.5 min | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:44:50 AM | ETH | DOWN | 10 sec | -0.004% | 0¢ | ❌ Lost | $0.00 |
| 11/1 1:44:34 AM | BTC | UP | 26 sec | -0.022% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:44:18 AM | SOL | DOWN | 42 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 11/1 1:44:18 AM | ZEC | UP | 42 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |
| 11/1 1:43:49 AM | HYPE | UP | 70 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 11/1 1:42:48 AM | BNB | DOWN | 2.2 min | +0.101% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:42:16 AM | XRP | DOWN | 2.7 min | +0.072% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:41:44 AM | DOGE | DOWN | 3.3 min | +0.104% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 1:29:50 AM | ZEC | UP | 10 sec | -0.035% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 1:27:18 AM | HYPE | UP | 2.7 min | -0.250% | 16¢ | ❌ Lost | -$0.15 |
| 11/1 1:25:59 AM | BTC | UP | 4.0 min | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:25:44 AM | SOL | UP | 4.2 min | -0.151% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:24:27 AM | DOGE | UP | 5.5 min | -0.192% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:23:16 AM | BNB | UP | 6.7 min | -0.216% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:21:58 AM | XRP | UP | 8.0 min | -0.272% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 1:14:56 AM | XRP | DOWN | 4 sec | -0.072% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 1:14:24 AM | DOGE | UP | 36 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 11/1 1:14:08 AM | ZEC | UP | 52 sec | -0.107% | 0¢ | ❌ Lost | $0.00 |
| 11/1 1:14:08 AM | HYPE | UP | 52 sec | -0.163% | 0¢ | ❌ Lost | $0.00 |
| 11/1 1:13:37 AM | BNB | UP | 83 sec | -0.021% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
