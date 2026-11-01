# 15-Minute 1¢ Study

*Updated Sun Nov 1, 10:34 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3419 finished bets | 1% | $108.40 | +28% | +3.17¢ | $75.95 / $32.45 |

*Expect about **99 buys a day** (~$14.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3156 | $48.65 | +14% |
| Volatility model ≥ 2%, hold to the close | 6307 | $34.50 | +5% |
| Momentum model ≥ 2%, hold to the close | 5201 | -$55.20 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41434 | 41424 | 155 (0%) | 1.07% | -$2,870.90 (-57%) | Hold to the close: -$2,870.90 (-57%) |

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
| Volatility model | 25823 | 4.7% | 0.4% (102) | -689% | ❌ Worse |
| Momentum model | 25823 | 4.6% | 0.4% (102) | -711% | ❌ Worse |
| Mean-reversion model | 25823 | 8.1% | 0.4% (102) | -838% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 25823 | 102 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6307 | 57 | +5% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3419 | 35 | +28% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1940 | 21 | +55% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5201 | 39 | -9% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3156 | 28 | +14% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 2063 | 19 | +29% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10656 | 72 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7470 | 62 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4997 | 44 | +0% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26025 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41424 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 155 | 0% | -$2,870.90 | -57% | — |
| Sell at 2¢ | 1622 | 4% | -$4,395.18 | -87% | 47 sec |
| Sell at 3¢ | 1115 | 3% | -$4,382.05 | -87% | 48 sec |
| Sell at 5¢ | 773 | 2% | -$4,286.45 | -85% | 63 sec |
| Sell at 10¢ | 466 | 1% | -$4,108.44 | -82% | 65 sec |
| Sell at 25¢ | 246 | 1% | -$3,792.64 | -75% | 83 sec |
| Sell at 50¢ | 160 | 0% | -$3,442.90 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1951 | 9 | 11% | 4% | -56% | -80% | -82% |
| 2–5 min | 13259 | 73 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10482 | 36 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15721 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2915 | 13 | 5% | 3% | -43% | -88% | -88% |
| SOL | 2904 | 10 | 4% | 2% | -57% | -91% | -91% |
| HYPE | 2902 | 9 | 5% | 2% | -62% | -89% | -87% |
| BNB | 2902 | 17 | 5% | 2% | -27% | -85% | -84% |
| DOGE | 2893 | 6 | 4% | 2% | -74% | -90% | -90% |
| ETH | 2891 | 11 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 2873 | 14 | 5% | 2% | -37% | -83% | -83% |
| BTC | 2873 | 13 | 5% | 2% | -39% | -88% | -89% |
| XRP | 2872 | 11 | 3% | 1% | -53% | -89% | -89% |
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
| UP (bought YES) | 21020 | 85 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20404 | 70 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4251 | 21 | 2% | 1% | -14% | -82% | -81% |
| 0.05–0.1% | 4482 | 16 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 6727 | 23 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 7669 | 33 | 7% | 3% | -52% | -86% | -86% |
| Over 0.5% | 2891 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10303 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10460 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9655 | 34 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 11006 | 37 | 3% | 2% | -61% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,742 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 10:29:37 AM | SOL | DOWN | 23 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 11/1 10:29:22 AM | BNB | DOWN | 38 sec | +0.039% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:29:22 AM | XRP | DOWN | 38 sec | +0.040% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:29:05 AM | BTC | UP | 54 sec | -0.011% | 2¢ | ❌ Lost | $0.00 |
| 11/1 10:28:49 AM | ETH | UP | 70 sec | -0.035% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 10:28:33 AM | ZEC | UP | 86 sec | -0.158% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:27:44 AM | NEAR | UP | 2.2 min | -0.366% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:26:53 AM | DOGE | UP | 3.1 min | -0.138% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 10:14:50 AM | BTC | DOWN | 9 sec | +0.004% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 10:14:50 AM | ETH | UP | 9 sec | -0.008% | 0¢ | ❌ Lost | $0.00 |
| 11/1 10:14:10 AM | XRP | DOWN | 49 sec | +0.064% | 0¢ | ❌ Lost | $0.00 |
| 11/1 10:14:10 AM | SOL | DOWN | 49 sec | +0.053% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 10:14:10 AM | BNB | DOWN | 49 sec | -0.024% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 10:13:19 AM | HYPE | UP | 1.7 min | -0.141% | 0¢ | ❌ Lost | $0.00 |
| 11/1 10:12:15 AM | DOGE | DOWN | 2.8 min | +0.087% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 10:10:38 AM | ZEC | DOWN | 4.3 min | +0.252% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 9:59:48 AM | XRP | DOWN | 12 sec | +0.016% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 9:59:32 AM | ZEC | DOWN | 28 sec | +0.084% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 9:59:32 AM | DOGE | UP | 28 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 11/1 9:58:59 AM | SOL | DOWN | 61 sec | +0.055% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 9:58:43 AM | ETH | DOWN | 77 sec | +0.030% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 9:58:12 AM | BNB | DOWN | 1.8 min | +0.042% | 2¢ | ❌ Lost | -$0.15 |
| 11/1 9:57:54 AM | BTC | DOWN | 2.1 min | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 11/1 9:57:07 AM | NEAR | DOWN | 2.9 min | +0.148% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 9:55:29 AM | HYPE | DOWN | 4.5 min | +0.207% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 9:44:13 AM | BTC | UP | 47 sec | -0.032% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 9:43:40 AM | BNB | UP | 79 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 11/1 9:42:48 AM | HYPE | UP | 2.2 min | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 9:42:48 AM | XRP | UP | 2.2 min | -0.088% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 9:42:01 AM | ETH | UP | 3.0 min | -0.114% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
