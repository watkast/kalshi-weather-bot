# 15-Minute 1¢ Study

*Updated Sun Nov 8, 2:47 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3968 finished bets | 1% | $147.15 | +33% | +3.71¢ | $86.45 / $60.70 |

*Expect about **96 buys a day** (~$14.47/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3686 | $77.30 | +19% |
| Volatility model ≥ 2%, hold to the close | 7279 | $34.30 | +4% |
| Momentum model ≥ 2%, hold to the close | 6011 | -$32.15 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 49434 | 49417 | 180 (0%) | 1.07% | -$3,490.05 (-58%) | Hold to the close: -$3,490.05 (-58%) |

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
| Volatility model | 30174 | 4.8% | 0.4% (116) | -705% | ❌ Worse |
| Momentum model | 30174 | 4.7% | 0.4% (116) | -731% | ❌ Worse |
| Mean-reversion model | 30174 | 8.1% | 0.4% (116) | -853% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30174 | 116 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7279 | 65 | +4% | -76% | -75% | -72% |
| Volatility model ≥ 5% | 3968 | 42 | +33% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2291 | 27 | +69% | -60% | -59% | -55% |
| Momentum model ≥ 2% | 6011 | 47 | -5% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3686 | 34 | +19% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2421 | 23 | +33% | -64% | -64% | -60% |
| Mean-reversion model ≥ 2% | 12449 | 84 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8732 | 73 | -7% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5843 | 53 | +3% | -76% | -76% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30379 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11670 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 49417 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 180 | 0% | -$3,490.05 | -58% | — |
| Sell at 2¢ | 1928 | 4% | -$5,228.77 | -87% | 47 sec |
| Sell at 3¢ | 1310 | 3% | -$5,219.15 | -87% | 48 sec |
| Sell at 5¢ | 910 | 2% | -$5,110.55 | -85% | 63 sec |
| Sell at 10¢ | 550 | 1% | -$4,897.55 | -81% | 65 sec |
| Sell at 25¢ | 288 | 1% | -$4,552.77 | -76% | 82 sec |
| Sell at 50¢ | 184 | 0% | -$4,166.05 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2437 | 11 | 11% | 4% | -57% | -81% | -83% |
| 2–5 min | 15896 | 84 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 12487 | 40 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18585 | 45 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3406 | 13 | 5% | 2% | -50% | -88% | -88% |
| SOL | 3398 | 14 | 4% | 2% | -47% | -87% | -87% |
| HYPE | 3391 | 11 | 5% | 2% | -59% | -89% | -88% |
| BNB | 3384 | 17 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 3378 | 6 | 4% | 2% | -78% | -91% | -90% |
| ETH | 3374 | 13 | 7% | 3% | -53% | -81% | -81% |
| NEAR | 3354 | 16 | 5% | 2% | -38% | -85% | -85% |
| BTC | 3351 | 16 | 5% | 2% | -34% | -88% | -89% |
| XRP | 3343 | 12 | 3% | 1% | -55% | -90% | -89% |
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
| UP (bought YES) | 25047 | 95 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 24370 | 85 | 4% | 2% | -60% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4958 | 25 | 2% | 1% | -11% | -76% | -76% |
| 0.05–0.1% | 5229 | 19 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 7839 | 26 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 8979 | 35 | 6% | 3% | -57% | -87% | -87% |
| Over 0.5% | 3366 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12068 | 42 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 12086 | 54 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 11900 | 43 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13363 | 41 | 3% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,869 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/8 2:44:35 AM | XRP | DOWN | 25 sec | -0.017% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:43:32 AM | DOGE | DOWN | 87 sec | +0.055% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 2:43:00 AM | ETH | DOWN | 2.0 min | +0.061% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:41:39 AM | ZEC | DOWN | 3.3 min | +0.341% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:41:23 AM | BTC | DOWN | 3.6 min | +0.073% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:39:46 AM | HYPE | DOWN | 5.2 min | +0.356% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:39:46 AM | NEAR | DOWN | 5.2 min | +0.615% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:29:46 AM | BTC | UP | 13 sec | -0.013% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:29:46 AM | NEAR | UP | 13 sec | -0.079% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 2:29:30 AM | HYPE | DOWN | 29 sec | +0.082% | 0¢ | ❌ Lost | $0.00 |
| 11/8 2:28:40 AM | ZEC | DOWN | 80 sec | +0.144% | 0¢ | ❌ Lost | $0.00 |
| 11/8 2:28:40 AM | BNB | DOWN | 80 sec | +0.024% | 2¢ | ❌ Lost | -$0.15 |
| 11/8 2:28:24 AM | SOL | DOWN | 1.6 min | +0.092% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:27:05 AM | XRP | DOWN | 2.9 min | +0.146% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:25:15 AM | DOGE | UP | 4.8 min | -0.438% | 2¢ | ❌ Lost | -$0.15 |
| 11/8 2:22:18 AM | HYPE | UP | 7.7 min | -0.463% | 100¢ | ✅ Won | $13.85 |
| 11/8 2:13:40 AM | BTC | UP | 79 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 11/8 2:13:40 AM | NEAR | UP | 79 sec | -0.184% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 2:13:24 AM | ZEC | UP | 1.6 min | -0.230% | 0¢ | ❌ Lost | $0.00 |
| 11/8 2:13:24 AM | BNB | UP | 1.6 min | -0.132% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 2:13:08 AM | HYPE | UP | 1.9 min | -0.091% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:12:36 AM | XRP | UP | 2.4 min | -0.146% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:11:33 AM | SOL | UP | 3.4 min | -0.143% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:10:45 AM | ETH | UP | 4.2 min | -0.105% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:10:27 AM | DOGE | UP | 4.5 min | -0.196% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 1:59:40 AM | BNB | UP | 19 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 11/8 1:59:09 AM | XRP | UP | 50 sec | -0.052% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 1:59:09 AM | SOL | DOWN | 50 sec | +0.054% | 0¢ | ❌ Lost | $0.00 |
| 11/8 1:59:09 AM | ETH | DOWN | 50 sec | +0.041% | 0¢ | ❌ Lost | $0.00 |
| 11/8 1:59:09 AM | BTC | DOWN | 50 sec | +0.017% | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
