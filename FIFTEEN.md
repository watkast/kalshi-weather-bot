# 15-Minute 1¢ Study

*Updated Wed Nov 4, 6:17 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3635 finished bets | 1% | $112.25 | +28% | +3.09¢ | $78.40 / $33.85 |

*Expect about **98 buys a day** (~$14.63/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3371 | $39.85 | +11% |
| Volatility model ≥ 2%, hold to the close | 6729 | $26.25 | +3% |
| Momentum model ≥ 2%, hold to the close | 5546 | -$52.20 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 45164 | 45154 | 167 (0%) | 1.07% | -$3,163.55 (-58%) | Hold to the close: -$3,163.55 (-58%) |

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
| Volatility model | 27654 | 4.7% | 0.4% (108) | -679% | ❌ Worse |
| Momentum model | 27654 | 4.6% | 0.4% (108) | -706% | ❌ Worse |
| Mean-reversion model | 27654 | 8.1% | 0.4% (108) | -827% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27654 | 108 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6729 | 60 | +3% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3635 | 37 | +28% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2063 | 22 | +53% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5546 | 42 | -8% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3371 | 29 | +11% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2198 | 19 | +21% | -74% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11446 | 78 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8042 | 67 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5385 | 47 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27859 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10723 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6572 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 45154 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 167 | 0% | -$3,163.55 | -58% | — |
| Sell at 2¢ | 1772 | 4% | -$4,788.83 | -87% | 47 sec |
| Sell at 3¢ | 1214 | 3% | -$4,776.09 | -87% | 49 sec |
| Sell at 5¢ | 839 | 2% | -$4,676.20 | -85% | 63 sec |
| Sell at 10¢ | 507 | 1% | -$4,473.38 | -81% | 66 sec |
| Sell at 25¢ | 266 | 1% | -$4,145.09 | -75% | 83 sec |
| Sell at 50¢ | 170 | 0% | -$3,780.05 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2217 | 10 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 14540 | 79 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 11390 | 39 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 16996 | 39 | 1% | 0% | -67% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3121 | 13 | 5% | 2% | -46% | -88% | -88% |
| SOL | 3115 | 12 | 4% | 2% | -51% | -90% | -90% |
| BNB | 3108 | 17 | 5% | 2% | -31% | -85% | -84% |
| HYPE | 3107 | 9 | 5% | 2% | -64% | -89% | -87% |
| DOGE | 3095 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3089 | 12 | 7% | 3% | -53% | -85% | -85% |
| BTC | 3078 | 14 | 5% | 2% | -38% | -88% | -89% |
| NEAR | 3077 | 15 | 5% | 2% | -37% | -84% | -84% |
| XRP | 3069 | 12 | 3% | 1% | -51% | -89% | -89% |
| GOLD | 1662 | 5 | 5% | 2% | -63% | -81% | -83% |
| WTI | 1618 | 5 | 4% | 1% | -63% | -92% | -93% |
| SILVER | 1616 | 7 | 5% | 2% | -49% | -82% | -81% |
| PLATINUM | 1446 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1390 | 3 | 3% | 1% | -80% | -89% | -89% |
| COPPER | 1366 | 6 | 2% | 1% | -59% | -70% | -69% |
| GBPUSD | 1316 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1312 | 8 | 2% | 1% | -43% | -75% | -74% |
| USDJPY | 1298 | 5 | 2% | 1% | -64% | -97% | -97% |
| PALLADIUM | 1295 | 3 | 1% | 1% | -78% | -91% | -91% |
| AUDUSD | 848 | 4 | 2% | 1% | -56% | -86% | -86% |
| USDCAD | 814 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 408 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 248 | 1 | 5% | 2% | -62% | -54% | -52% |
| 30YRRATE | 227 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 224 | 2 | 4% | 0% | -17% | -10% | -10% |
| 5YRRATE | 207 | 1 | 5% | 2% | -55% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22922 | 89 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 22232 | 78 | 4% | 2% | -60% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4500 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4745 | 18 | 3% | 2% | -43% | -91% | -90% |
| 0.1–0.2% | 7199 | 25 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 8291 | 33 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3116 | 13 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11276 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11077 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10598 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 12203 | 40 | 3% | 2% | -62% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,707 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 6:14:57 AM | BRENT | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:14:57 AM | USDJPY | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:14:57 AM | 10YRRATE | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:14:42 AM | USDCAD | DOWN | 17 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 6:14:42 AM | 5YRRATE | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:14:42 AM | PALLADIUM | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:14:26 AM | SILVER | UP | 33 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 6:13:54 AM | SOL | DOWN | 65 sec | +0.140% | 0¢ | ❌ Lost | $0.00 |
| 11/4 6:13:54 AM | 2YRRATE | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:13:38 AM | NEAR | DOWN | 81 sec | +0.235% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 6:13:38 AM | HYPE | DOWN | 81 sec | +0.246% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:13:22 AM | GBPUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:13:22 AM | BNB | DOWN | 1.6 min | +0.042% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:13:22 AM | ZEC | DOWN | 1.6 min | +0.469% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:13:06 AM | BTC | DOWN | 1.9 min | +0.156% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 6:12:35 AM | XRP | DOWN | 2.4 min | +0.219% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:12:35 AM | AUDUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:12:19 AM | ETH | DOWN | 2.7 min | +0.229% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 6:12:19 AM | DOGE | DOWN | 2.7 min | +0.270% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 6:12:03 AM | WTI | UP | 2.9 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/4 6:11:47 AM | EURUSD | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:10:44 AM | PLATINUM | UP | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 6:08:22 AM | COPPER | UP | 6.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 5:59:50 AM | AUDUSD | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 5:59:35 AM | BTC | DOWN | 24 sec | +0.048% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 5:59:03 AM | GOLD | DOWN | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 5:58:47 AM | EURUSD | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 5:58:47 AM | WTI | UP | 72 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/4 5:58:47 AM | 10YRRATE | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 5:58:32 AM | ZEC | UP | 87 sec | -0.438% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
