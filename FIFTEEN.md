# 15-Minute 1¢ Study

*Updated Sun Nov 8, 7:26 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3992 finished bets | 1% | $144.30 | +33% | +3.61¢ | $84.65 / $59.65 |

*Expect about **97 buys a day** (~$14.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3705 | $75.05 | +19% |
| Volatility model ≥ 2%, hold to the close | 7317 | $29.50 | +3% |
| Momentum model ≥ 2%, hold to the close | 6041 | -$35.90 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 49592 | 49573 | 180 (0%) | 1.07% | -$3,508.20 (-58%) | Hold to the close: -$3,508.20 (-58%) |

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
| Volatility model | 30330 | 4.8% | 0.4% (116) | -709% | ❌ Worse |
| Momentum model | 30330 | 4.7% | 0.4% (116) | -734% | ❌ Worse |
| Mean-reversion model | 30330 | 8.1% | 0.4% (116) | -856% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30330 | 116 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7317 | 65 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 3992 | 42 | +33% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2304 | 27 | +68% | -60% | -59% | -55% |
| Momentum model ≥ 2% | 6041 | 47 | -5% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 3705 | 34 | +19% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2431 | 23 | +33% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 12523 | 84 | -26% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 8788 | 73 | -8% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5884 | 53 | +3% | -76% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30535 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11670 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 49573 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 180 | 0% | -$3,508.20 | -58% | — |
| Sell at 2¢ | 1935 | 4% | -$5,245.10 | -87% | 47 sec |
| Sell at 3¢ | 1314 | 3% | -$5,235.74 | -87% | 48 sec |
| Sell at 5¢ | 911 | 2% | -$5,128.05 | -85% | 63 sec |
| Sell at 10¢ | 550 | 1% | -$4,915.70 | -82% | 65 sec |
| Sell at 25¢ | 288 | 1% | -$4,570.92 | -76% | 82 sec |
| Sell at 50¢ | 184 | 0% | -$4,184.20 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2448 | 11 | 11% | 4% | -57% | -81% | -83% |
| 2–5 min | 15963 | 84 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 12520 | 40 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18630 | 45 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3424 | 13 | 5% | 2% | -51% | -88% | -88% |
| SOL | 3416 | 14 | 4% | 2% | -48% | -87% | -87% |
| HYPE | 3407 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3400 | 17 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 3396 | 6 | 4% | 2% | -78% | -91% | -90% |
| ETH | 3391 | 13 | 7% | 3% | -53% | -81% | -81% |
| NEAR | 3372 | 16 | 5% | 2% | -38% | -85% | -85% |
| BTC | 3369 | 16 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3360 | 12 | 3% | 1% | -55% | -90% | -89% |
| GOLD | 1783 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1751 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1733 | 8 | 5% | 2% | -45% | -82% | -81% |
| PLATINUM | 1567 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1503 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1471 | 6 | 2% | 1% | -62% | -72% | -71% |
| NATGAS | 1433 | 8 | 2% | 1% | -48% | -77% | -76% |
| GBPUSD | 1426 | 4 | 2% | 1% | -74% | -96% | -96% |
| PALLADIUM | 1408 | 3 | 1% | 0% | -80% | -91% | -92% |
| USDJPY | 1406 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 960 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 929 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 524 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25128 | 95 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 24445 | 85 | 4% | 2% | -60% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4998 | 25 | 2% | 1% | -12% | -77% | -76% |
| 0.05–0.1% | 5260 | 19 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 7883 | 26 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 9017 | 35 | 6% | 3% | -57% | -87% | -87% |
| Over 0.5% | 3369 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12179 | 42 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12131 | 54 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 11900 | 43 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13363 | 41 | 3% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,898 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/8 7:26:23 AM | SOL | UP | 3.6 min | -0.254% | — | In play | — |
| 11/8 7:25:01 AM | DOGE | UP | 5.0 min | -0.255% | — | In play | — |
| 11/8 7:14:36 AM | HYPE | UP | 23 sec | -0.060% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 7:14:03 AM | ZEC | DOWN | 56 sec | +0.110% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 7:14:03 AM | NEAR | DOWN | 56 sec | +0.125% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 7:13:47 AM | BTC | DOWN | 72 sec | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 7:13:47 AM | DOGE | UP | 72 sec | -0.083% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 7:13:47 AM | SOL | DOWN | 72 sec | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 7:13:15 AM | XRP | UP | 1.7 min | -0.173% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 7:13:15 AM | ETH | DOWN | 1.7 min | +0.098% | 0¢ | ❌ Lost | $0.00 |
| 11/8 7:12:09 AM | BNB | UP | 2.9 min | -0.167% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:59:57 AM | ETH | UP | 3 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 11/8 6:59:41 AM | BTC | DOWN | 19 sec | +0.004% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:59:25 AM | DOGE | DOWN | 35 sec | +0.001% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:58:38 AM | ZEC | UP | 81 sec | -0.170% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 6:58:22 AM | SOL | UP | 1.6 min | -0.126% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:57:02 AM | BNB | UP | 3.0 min | -0.158% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:56:15 AM | NEAR | UP | 3.7 min | -0.392% | 3¢ | ❌ Lost | -$0.15 |
| 11/8 6:55:43 AM | HYPE | UP | 4.3 min | -0.334% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:55:01 AM | XRP | UP | 5.0 min | -0.293% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:42:43 AM | HYPE | UP | 2.3 min | -0.246% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:42:11 AM | NEAR | UP | 2.8 min | -0.366% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:41:55 AM | ZEC | UP | 3.1 min | -0.516% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:41:37 AM | DOGE | UP | 3.4 min | -0.260% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:41:37 AM | SOL | UP | 3.4 min | -0.267% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:41:21 AM | BTC | UP | 3.6 min | -0.173% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:41:21 AM | ETH | UP | 3.6 min | -0.154% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:40:50 AM | XRP | UP | 4.2 min | -0.275% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:39:46 AM | BNB | UP | 5.2 min | -0.226% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:29:42 AM | HYPE | DOWN | 17 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
