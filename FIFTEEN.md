# 15-Minute 1¢ Study

*Updated Sun Nov 8, 4:09 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3975 finished bets | 1% | $146.40 | +33% | +3.68¢ | $86.00 / $60.40 |

*Expect about **97 buys a day** (~$14.48/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3693 | $76.40 | +19% |
| Volatility model ≥ 2%, hold to the close | 7289 | $33.10 | +4% |
| Momentum model ≥ 2%, hold to the close | 6022 | -$33.65 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 49477 | 49460 | 180 (0%) | 1.07% | -$3,494.55 (-58%) | Hold to the close: -$3,494.55 (-58%) |

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
| Volatility model | 30217 | 4.8% | 0.4% (116) | -705% | ❌ Worse |
| Momentum model | 30217 | 4.6% | 0.4% (116) | -730% | ❌ Worse |
| Mean-reversion model | 30217 | 8.1% | 0.4% (116) | -852% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30217 | 116 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7289 | 65 | +4% | -76% | -75% | -72% |
| Volatility model ≥ 5% | 3975 | 42 | +33% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2294 | 27 | +69% | -60% | -59% | -55% |
| Momentum model ≥ 2% | 6022 | 47 | -5% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 3693 | 34 | +19% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2423 | 23 | +33% | -64% | -64% | -60% |
| Mean-reversion model ≥ 2% | 12463 | 84 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8742 | 73 | -7% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5849 | 53 | +3% | -76% | -76% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30422 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11670 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 49460 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 180 | 0% | -$3,494.55 | -58% | — |
| Sell at 2¢ | 1930 | 4% | -$5,232.75 | -87% | 47 sec |
| Sell at 3¢ | 1311 | 3% | -$5,223.26 | -87% | 48 sec |
| Sell at 5¢ | 910 | 2% | -$5,115.05 | -85% | 63 sec |
| Sell at 10¢ | 550 | 1% | -$4,902.05 | -82% | 65 sec |
| Sell at 25¢ | 288 | 1% | -$4,557.27 | -76% | 82 sec |
| Sell at 50¢ | 184 | 0% | -$4,170.55 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2437 | 11 | 11% | 4% | -57% | -81% | -83% |
| 2–5 min | 15910 | 84 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 12499 | 40 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18602 | 45 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3411 | 13 | 5% | 2% | -50% | -88% | -88% |
| SOL | 3403 | 14 | 4% | 2% | -48% | -87% | -87% |
| HYPE | 3395 | 11 | 5% | 2% | -59% | -89% | -88% |
| BNB | 3388 | 17 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 3383 | 6 | 4% | 2% | -78% | -91% | -90% |
| ETH | 3379 | 13 | 7% | 3% | -53% | -81% | -82% |
| NEAR | 3359 | 16 | 5% | 2% | -38% | -85% | -85% |
| BTC | 3356 | 16 | 5% | 2% | -34% | -88% | -89% |
| XRP | 3348 | 12 | 3% | 1% | -55% | -90% | -89% |
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
| UP (bought YES) | 25074 | 95 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 24386 | 85 | 4% | 2% | -60% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4973 | 25 | 2% | 1% | -12% | -76% | -76% |
| 0.05–0.1% | 5243 | 19 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 7846 | 26 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 8986 | 35 | 6% | 3% | -57% | -87% | -87% |
| Over 0.5% | 3366 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12111 | 42 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 12086 | 54 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 11900 | 43 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13363 | 41 | 3% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,877 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/8 3:59:57 AM | BTC | UP | 2 sec | -0.004% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:59:34 AM | SOL | DOWN | 26 sec | +0.020% | 0¢ | ❌ Lost | $0.00 |
| 11/8 3:59:34 AM | DOGE | DOWN | 26 sec | +0.011% | 0¢ | ❌ Lost | $0.00 |
| 11/8 3:59:34 AM | ETH | DOWN | 26 sec | +0.011% | 0¢ | ❌ Lost | $0.00 |
| 11/8 3:59:03 AM | HYPE | DOWN | 57 sec | +0.086% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:59:03 AM | XRP | UP | 57 sec | -0.060% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 3:58:47 AM | BNB | UP | 72 sec | -0.077% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:58:15 AM | ZEC | UP | 1.7 min | -0.170% | 4¢ | ❌ Lost | -$0.15 |
| 11/8 3:58:15 AM | NEAR | DOWN | 1.7 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:44:20 AM | NEAR | DOWN | 40 sec | +0.046% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 3:44:20 AM | BTC | DOWN | 40 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 11/8 3:44:20 AM | HYPE | DOWN | 40 sec | +0.020% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 3:43:48 AM | XRP | DOWN | 72 sec | +0.035% | 0¢ | ❌ Lost | $0.00 |
| 11/8 3:43:16 AM | SOL | DOWN | 1.7 min | +0.075% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:43:16 AM | ETH | DOWN | 1.7 min | +0.072% | 0¢ | ❌ Lost | $0.00 |
| 11/8 3:42:29 AM | BNB | DOWN | 2.5 min | +0.023% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:42:29 AM | DOGE | DOWN | 2.5 min | +0.068% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:41:57 AM | ZEC | DOWN | 3.0 min | +0.276% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:29:14 AM | BTC | UP | 46 sec | -0.022% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:28:59 AM | DOGE | UP | 60 sec | -0.065% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 3:28:33 AM | ETH | UP | 86 sec | -0.045% | 0¢ | ❌ Lost | $0.00 |
| 11/8 3:27:11 AM | NEAR | UP | 2.8 min | -0.332% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:26:56 AM | ZEC | UP | 3.0 min | -0.325% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:26:56 AM | SOL | UP | 3.0 min | -0.194% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:26:40 AM | BNB | UP | 3.3 min | -0.102% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:25:18 AM | XRP | UP | 4.7 min | -0.215% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:14:37 AM | DOGE | UP | 22 sec | -0.082% | 0¢ | ❌ Lost | $0.00 |
| 11/8 3:14:21 AM | NEAR | UP | 38 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 11/8 3:13:31 AM | SOL | UP | 89 sec | -0.095% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:13:15 AM | BTC | UP | 1.8 min | -0.067% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
