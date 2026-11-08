# 15-Minute 1¢ Study

*Updated Sun Nov 8, 12:47 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4006 finished bets | 1% | $142.50 | +32% | +3.56¢ | $97.90 / $44.60 |

*Expect about **96 buys a day** (~$14.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3718 | $73.40 | +18% |
| Volatility model ≥ 2%, hold to the close | 7342 | $26.35 | +3% |
| Momentum model ≥ 2%, hold to the close | 6064 | -$38.75 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 49706 | 49689 | 180 (0%) | 1.07% | -$3,521.25 (-58%) | Hold to the close: -$3,521.25 (-58%) |

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
| Volatility model | 30446 | 4.8% | 0.4% (116) | -709% | ❌ Worse |
| Momentum model | 30446 | 4.6% | 0.4% (116) | -734% | ❌ Worse |
| Mean-reversion model | 30446 | 8.1% | 0.4% (116) | -857% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30446 | 116 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7342 | 65 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4006 | 42 | +32% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2314 | 27 | +67% | -61% | -59% | -55% |
| Momentum model ≥ 2% | 6064 | 47 | -6% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 3718 | 34 | +18% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2439 | 23 | +32% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 12574 | 84 | -27% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 8818 | 73 | -8% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5903 | 53 | +2% | -76% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30651 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11670 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 49689 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 180 | 0% | -$3,521.25 | -58% | — |
| Sell at 2¢ | 1938 | 4% | -$5,257.37 | -87% | 47 sec |
| Sell at 3¢ | 1316 | 3% | -$5,248.01 | -87% | 48 sec |
| Sell at 5¢ | 913 | 2% | -$5,139.80 | -85% | 63 sec |
| Sell at 10¢ | 551 | 1% | -$4,927.44 | -82% | 65 sec |
| Sell at 25¢ | 288 | 1% | -$4,583.97 | -76% | 82 sec |
| Sell at 50¢ | 184 | 0% | -$4,197.25 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2460 | 11 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 16005 | 84 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 12549 | 40 | 3% | 1% | -65% | -92% | -92% |
| Under 1 min | 18663 | 45 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3437 | 13 | 5% | 2% | -51% | -88% | -88% |
| SOL | 3429 | 14 | 4% | 2% | -48% | -87% | -87% |
| HYPE | 3421 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3413 | 17 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 3411 | 6 | 4% | 2% | -78% | -91% | -90% |
| ETH | 3403 | 13 | 7% | 3% | -53% | -81% | -82% |
| NEAR | 3385 | 16 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3381 | 16 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3371 | 12 | 3% | 1% | -56% | -90% | -89% |
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
| UP (bought YES) | 25184 | 95 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 24505 | 85 | 4% | 2% | -60% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5019 | 25 | 2% | 1% | -12% | -77% | -76% |
| 0.05–0.1% | 5282 | 19 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 7917 | 26 | 4% | 2% | -59% | -90% | -90% |
| 0.2–0.5% | 9049 | 35 | 6% | 3% | -57% | -87% | -87% |
| Over 0.5% | 3376 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12179 | 42 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 11924 | 43 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13363 | 41 | 3% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,924 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/8 12:44:20 PM | ZEC | DOWN | 39 sec | +0.059% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 12:44:20 PM | BTC | DOWN | 39 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 11/8 12:44:06 PM | BNB | DOWN | 53 sec | -0.026% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 12:43:50 PM | NEAR | DOWN | 69 sec | +0.192% | 0¢ | ❌ Lost | $0.00 |
| 11/8 12:43:34 PM | SOL | DOWN | 85 sec | +0.088% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 12:43:05 PM | DOGE | DOWN | 1.9 min | +0.119% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 12:42:22 PM | HYPE | UP | 2.6 min | -0.217% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 12:29:45 PM | ZEC | DOWN | 14 sec | +0.039% | 0¢ | ❌ Lost | $0.00 |
| 11/8 12:28:58 PM | NEAR | DOWN | 61 sec | +0.120% | 0¢ | ❌ Lost | $0.00 |
| 11/8 12:28:42 PM | DOGE | DOWN | 77 sec | +0.038% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 12:28:09 PM | BNB | UP | 1.8 min | -0.059% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 12:28:09 PM | HYPE | DOWN | 1.8 min | +0.179% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 12:28:09 PM | BTC | DOWN | 1.8 min | +0.050% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 12:26:30 PM | XRP | DOWN | 3.5 min | +0.174% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 12:24:52 PM | SOL | DOWN | 5.1 min | +0.260% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 12:14:30 PM | BNB | UP | 29 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 11/8 12:13:25 PM | ZEC | UP | 1.6 min | -0.289% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 12:11:50 PM | BTC | UP | 3.2 min | -0.101% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 12:10:15 PM | NEAR | UP | 4.8 min | -0.714% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 12:10:15 PM | HYPE | UP | 4.8 min | -0.351% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 12:10:01 PM | SOL | UP | 5.0 min | -0.346% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 12:09:29 PM | DOGE | UP | 5.5 min | -0.230% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 12:09:29 PM | ETH | UP | 5.5 min | -0.174% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 12:08:30 PM | XRP | UP | 6.5 min | -0.467% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 11:59:44 AM | SOL | UP | 16 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 11/8 11:59:44 AM | DOGE | DOWN | 16 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 11/8 11:59:28 AM | BNB | DOWN | 32 sec | +0.011% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 11:59:28 AM | ZEC | DOWN | 32 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 11/8 11:58:39 AM | HYPE | DOWN | 81 sec | +0.074% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 11:58:39 AM | ETH | DOWN | 81 sec | +0.054% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
