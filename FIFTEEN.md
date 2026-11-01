# 15-Minute 1¢ Study

*Updated Sun Nov 1, 12:05 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3423 finished bets | 1% | $107.95 | +28% | +3.15¢ | $75.80 / $32.15 |

*Expect about **99 buys a day** (~$14.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3162 | $48.20 | +14% |
| Volatility model ≥ 2%, hold to the close | 6316 | $33.60 | +4% |
| Momentum model ≥ 2%, hold to the close | 5209 | -$55.95 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41487 | 41477 | 155 (0%) | 1.07% | -$2,876.45 (-57%) | Hold to the close: -$2,876.45 (-57%) |

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
| Volatility model | 25876 | 4.7% | 0.4% (102) | -690% | ❌ Worse |
| Momentum model | 25876 | 4.6% | 0.4% (102) | -712% | ❌ Worse |
| Mean-reversion model | 25876 | 8.1% | 0.4% (102) | -839% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 25876 | 102 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6316 | 57 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3423 | 35 | +28% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 1941 | 21 | +55% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5209 | 39 | -9% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3162 | 28 | +14% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 2067 | 19 | +29% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10670 | 72 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7478 | 62 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5001 | 44 | -0% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26078 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41477 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 155 | 0% | -$2,876.45 | -57% | — |
| Sell at 2¢ | 1624 | 4% | -$4,400.21 | -87% | 47 sec |
| Sell at 3¢ | 1116 | 3% | -$4,387.21 | -87% | 48 sec |
| Sell at 5¢ | 774 | 2% | -$4,291.35 | -85% | 63 sec |
| Sell at 10¢ | 467 | 1% | -$4,112.68 | -81% | 65 sec |
| Sell at 25¢ | 247 | 1% | -$3,794.88 | -75% | 83 sec |
| Sell at 50¢ | 160 | 0% | -$3,448.45 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1951 | 9 | 11% | 4% | -56% | -80% | -82% |
| 2–5 min | 13284 | 73 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10495 | 36 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15736 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2921 | 13 | 5% | 3% | -43% | -88% | -88% |
| SOL | 2910 | 10 | 4% | 2% | -57% | -91% | -91% |
| HYPE | 2908 | 9 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2908 | 17 | 5% | 2% | -27% | -85% | -84% |
| DOGE | 2898 | 6 | 4% | 2% | -74% | -90% | -90% |
| ETH | 2897 | 11 | 6% | 3% | -54% | -85% | -85% |
| NEAR | 2879 | 14 | 5% | 2% | -37% | -83% | -83% |
| BTC | 2879 | 13 | 5% | 2% | -39% | -88% | -89% |
| XRP | 2878 | 11 | 3% | 1% | -53% | -89% | -89% |
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
| UP (bought YES) | 21058 | 85 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20419 | 70 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4264 | 21 | 2% | 1% | -15% | -82% | -81% |
| 0.05–0.1% | 4493 | 16 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 6744 | 23 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 7680 | 33 | 7% | 3% | -52% | -86% | -86% |
| Over 0.5% | 2892 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10303 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9655 | 34 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 11006 | 37 | 3% | 2% | -61% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,758 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 11:56:14 AM | XRP | UP | 3.8 min | -0.176% | 2¢ | ❌ Lost | -$0.15 |
| 11/1 11:55:59 AM | BNB | UP | 4.0 min | -0.172% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:55:59 AM | ZEC | UP | 4.0 min | -0.404% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:55:59 AM | ETH | UP | 4.0 min | -0.160% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:55:59 AM | SOL | UP | 4.0 min | -0.333% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:55:59 AM | BTC | UP | 4.0 min | -0.124% | 3¢ | ❌ Lost | -$0.15 |
| 11/1 11:55:59 AM | HYPE | UP | 4.0 min | -0.469% | 0¢ | ❌ Lost | $0.00 |
| 11/1 11:55:59 AM | DOGE | UP | 4.0 min | -0.243% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:55:59 AM | NEAR | UP | 4.0 min | -0.530% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:44:58 AM | BTC | DOWN | 1 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 11/1 11:44:58 AM | BNB | DOWN | 1 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 11/1 11:44:12 AM | SOL | DOWN | 48 sec | +0.022% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:43:55 AM | HYPE | DOWN | 64 sec | +0.080% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:43:55 AM | NEAR | UP | 64 sec | -0.180% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:43:39 AM | ETH | DOWN | 80 sec | +0.025% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 11:43:23 AM | ZEC | DOWN | 1.6 min | +0.150% | 0¢ | ❌ Lost | $0.00 |
| 11/1 11:43:07 AM | DOGE | DOWN | 1.9 min | +0.100% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:41:45 AM | XRP | DOWN | 3.2 min | +0.120% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:29:33 AM | DOGE | UP | 26 sec | -0.058% | 0¢ | ❌ Lost | $0.00 |
| 11/1 11:29:17 AM | ETH | DOWN | 42 sec | +0.015% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:29:17 AM | NEAR | UP | 42 sec | -0.184% | 0¢ | ❌ Lost | $0.00 |
| 11/1 11:29:17 AM | BTC | UP | 42 sec | -0.036% | 0¢ | ❌ Lost | $0.00 |
| 11/1 11:29:17 AM | BNB | UP | 42 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 11/1 11:29:17 AM | ZEC | DOWN | 42 sec | +0.113% | 0¢ | ❌ Lost | $0.00 |
| 11/1 11:29:17 AM | XRP | DOWN | 42 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 11/1 11:28:46 AM | SOL | UP | 73 sec | -0.095% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:25:07 AM | HYPE | UP | 4.9 min | -0.327% | 42¢ | ❌ Lost | -$0.15 |
| 11/1 11:14:28 AM | SOL | DOWN | 31 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 11/1 11:14:28 AM | ETH | UP | 31 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 11/1 11:14:11 AM | BTC | UP | 48 sec | -0.035% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
