# 15-Minute 1¢ Study

*Updated Wed Nov 4, 6:38 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3637 finished bets | 1% | $112.10 | +28% | +3.08¢ | $78.40 / $33.70 |

*Expect about **98 buys a day** (~$14.63/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3372 | $39.70 | +11% |
| Volatility model ≥ 2%, hold to the close | 6735 | $25.65 | +3% |
| Momentum model ≥ 2%, hold to the close | 5549 | -$52.35 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 45181 | 45171 | 167 (0%) | 1.07% | -$3,165.35 (-58%) | Hold to the close: -$3,165.35 (-58%) |

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
| Volatility model | 27663 | 4.7% | 0.4% (108) | -679% | ❌ Worse |
| Momentum model | 27663 | 4.6% | 0.4% (108) | -706% | ❌ Worse |
| Mean-reversion model | 27663 | 8.1% | 0.4% (108) | -827% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27663 | 108 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6735 | 60 | +3% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3637 | 37 | +28% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2065 | 22 | +53% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5549 | 42 | -8% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3372 | 29 | +11% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2198 | 19 | +21% | -74% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11452 | 78 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8047 | 67 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5389 | 47 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27868 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10726 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6577 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 45171 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 167 | 0% | -$3,165.35 | -58% | — |
| Sell at 2¢ | 1773 | 4% | -$4,790.37 | -87% | 47 sec |
| Sell at 3¢ | 1215 | 3% | -$4,777.50 | -87% | 49 sec |
| Sell at 5¢ | 840 | 2% | -$4,677.35 | -85% | 63 sec |
| Sell at 10¢ | 508 | 1% | -$4,473.87 | -81% | 66 sec |
| Sell at 25¢ | 266 | 1% | -$4,146.89 | -75% | 83 sec |
| Sell at 50¢ | 170 | 0% | -$3,781.85 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2218 | 10 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 14541 | 79 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 11395 | 39 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 17006 | 39 | 1% | 0% | -67% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3122 | 13 | 5% | 2% | -46% | -88% | -88% |
| SOL | 3116 | 12 | 4% | 2% | -51% | -90% | -90% |
| BNB | 3109 | 17 | 5% | 2% | -31% | -85% | -85% |
| HYPE | 3108 | 9 | 5% | 2% | -64% | -89% | -87% |
| DOGE | 3096 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3090 | 12 | 7% | 3% | -53% | -85% | -85% |
| BTC | 3079 | 14 | 5% | 2% | -38% | -88% | -89% |
| NEAR | 3078 | 15 | 5% | 2% | -37% | -84% | -84% |
| XRP | 3070 | 12 | 3% | 1% | -51% | -89% | -89% |
| GOLD | 1663 | 5 | 5% | 2% | -63% | -81% | -83% |
| WTI | 1618 | 5 | 4% | 1% | -63% | -92% | -93% |
| SILVER | 1616 | 7 | 5% | 2% | -49% | -82% | -81% |
| PLATINUM | 1446 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1391 | 3 | 3% | 1% | -80% | -89% | -89% |
| COPPER | 1367 | 6 | 2% | 1% | -59% | -70% | -69% |
| GBPUSD | 1317 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1313 | 8 | 2% | 1% | -43% | -75% | -74% |
| USDJPY | 1299 | 5 | 2% | 1% | -64% | -97% | -97% |
| PALLADIUM | 1295 | 3 | 1% | 1% | -78% | -91% | -91% |
| AUDUSD | 848 | 4 | 2% | 1% | -56% | -86% | -86% |
| USDCAD | 814 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 408 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 248 | 1 | 5% | 2% | -62% | -54% | -52% |
| 30YRRATE | 227 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 225 | 2 | 4% | 0% | -17% | -11% | -10% |
| 5YRRATE | 208 | 1 | 5% | 2% | -55% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22928 | 89 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 22243 | 78 | 4% | 2% | -60% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4502 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4750 | 18 | 3% | 2% | -43% | -91% | -90% |
| 0.1–0.2% | 7201 | 25 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 8291 | 33 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3116 | 13 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11276 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11094 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10598 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 12203 | 40 | 3% | 2% | -62% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,704 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 6:29:51 AM | ZEC | UP | 9 sec | -0.129% | 0¢ | ❌ Lost | $0.00 |
| 11/4 6:29:35 AM | NEAR | DOWN | 25 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 11/4 6:29:35 AM | HYPE | DOWN | 25 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 11/4 6:29:35 AM | 5YRRATE | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:29:35 AM | XRP | DOWN | 25 sec | +0.023% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 6:29:35 AM | ETH | DOWN | 25 sec | +0.065% | 0¢ | ❌ Lost | $0.00 |
| 11/4 6:29:04 AM | GBPUSD | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:29:04 AM | GOLD | UP | 55 sec | — | 11¢ | ❌ Lost | -$0.15 |
| 11/4 6:29:04 AM | USDJPY | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:29:04 AM | EURUSD | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:28:47 AM | BTC | DOWN | 72 sec | +0.077% | 1¢ | ❌ Lost | $0.00 |
| 11/4 6:28:47 AM | 2YRRATE | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:28:47 AM | DOGE | DOWN | 72 sec | +0.096% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:28:15 AM | BNB | DOWN | 1.7 min | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 6:28:01 AM | SOL | DOWN | 2.0 min | +0.165% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 6:27:29 AM | NATGAS | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 6:23:32 AM | COPPER | UP | 6.5 min | — | 0¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
