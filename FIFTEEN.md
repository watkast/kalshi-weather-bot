# 15-Minute 1¢ Study

*Updated Wed Oct 14, 10:03 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1467 finished bets | 1% | $89.40 | +55% | +6.09¢ | $33.25 / $56.15 |

*Expect about **87 buys a day** (~$13.03/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1372 | $61.20 | +41% |
| Momentum model ≥ 2%, hold to the close | 2281 | $15.55 | +6% |
| Volatility model ≥ 2%, hold to the close | 2628 | $4.15 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18811 | 18804 | 74 (0%) | 1.07% | -$1,243.85 (-55%) | Hold to the close: -$1,243.85 (-55%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 12197 | 4.5% | 0.4% (52) | -636% | ❌ Worse |
| Momentum model | 12197 | 4.4% | 0.4% (52) | -661% | ❌ Worse |
| Mean-reversion model | 12197 | 7.3% | 0.4% (52) | -755% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12197 | 52 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2628 | 23 | +1% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1467 | 18 | +55% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 877 | 11 | +78% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2281 | 20 | +6% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1372 | 15 | +41% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 925 | 10 | +52% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4501 | 32 | -22% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3081 | 25 | -10% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2024 | 14 | -21% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12395 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4611 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1798 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18804 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 74 | 0% | -$1,243.85 | -55% | — |
| Sell at 2¢ | 659 | 4% | -$2,052.51 | -90% | 34 sec |
| Sell at 3¢ | 443 | 2% | -$2,051.08 | -90% | 46 sec |
| Sell at 5¢ | 323 | 2% | -$2,013.90 | -88% | 49 sec |
| Sell at 10¢ | 203 | 1% | -$1,929.92 | -85% | 63 sec |
| Sell at 25¢ | 118 | 1% | -$1,763.27 | -77% | 80 sec |
| Sell at 50¢ | 78 | 0% | -$1,557.35 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 587 | 5 | 10% | 3% | -19% | -82% | -87% |
| 2–5 min | 6069 | 35 | 7% | 3% | -43% | -88% | -88% |
| 1–2 min | 4911 | 18 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 7233 | 16 | 1% | 0% | -68% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1391 | 11 | 5% | 3% | -1% | -89% | -89% |
| HYPE | 1384 | 4 | 4% | 2% | -64% | -90% | -89% |
| ETH | 1381 | 8 | 5% | 3% | -29% | -88% | -87% |
| BNB | 1381 | 5 | 4% | 2% | -56% | -90% | -89% |
| DOGE | 1379 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1376 | 2 | 3% | 1% | -82% | -93% | -92% |
| BTC | 1369 | 7 | 5% | 2% | -32% | -88% | -91% |
| XRP | 1368 | 7 | 2% | 1% | -37% | -85% | -86% |
| NEAR | 1366 | 8 | 5% | 2% | -23% | -77% | -78% |
| GOLD | 752 | 1 | 4% | 1% | -84% | -92% | -93% |
| SILVER | 734 | 4 | 3% | 1% | -37% | -78% | -77% |
| WTI | 705 | 3 | 3% | 1% | -51% | -94% | -96% |
| COPPER | 651 | 1 | 2% | 2% | -86% | -97% | -96% |
| PLATINUM | 624 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 573 | 1 | 1% | 0% | -84% | -98% | -98% |
| NATGAS | 572 | 3 | 2% | 2% | -51% | -96% | -95% |
| EURUSD | 561 | 3 | 2% | 1% | -50% | -79% | -78% |
| GBPUSD | 527 | 1 | 2% | 1% | -82% | -97% | -97% |
| USDJPY | 480 | 3 | 1% | 1% | -42% | -99% | -98% |
| AUDUSD | 120 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 110 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9517 | 38 | 3% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9287 | 36 | 4% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2117 | 11 | 2% | 1% | -13% | -78% | -78% |
| 0.05–0.1% | 2170 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3137 | 10 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 3578 | 20 | 6% | 3% | -38% | -88% | -88% |
| Over 0.5% | 1390 | 6 | 6% | 2% | -55% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5276 | 15 | 3% | 2% | -68% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,512 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 9:59:52 PM | USDCAD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:59:52 PM | NEAR | DOWN | 8 sec | +0.129% | 0¢ | ❌ Lost | $0.00 |
| 10/14 9:59:36 PM | EURUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:59:36 PM | DOGE | DOWN | 24 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/14 9:59:20 PM | XRP | DOWN | 40 sec | +0.085% | 0¢ | ❌ Lost | $0.00 |
| 10/14 9:59:20 PM | GBPUSD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:59:05 PM | SOL | DOWN | 54 sec | +0.193% | 0¢ | ❌ Lost | $0.00 |
| 10/14 9:58:49 PM | BTC | DOWN | 70 sec | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:58:33 PM | ETH | DOWN | 86 sec | +0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:58:17 PM | SILVER | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:58:17 PM | BNB | UP | 1.7 min | -0.133% | 1¢ | ❌ Lost | $0.00 |
| 10/14 9:58:01 PM | USDJPY | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:58:01 PM | HYPE | DOWN | 2.0 min | +0.235% | 1¢ | ❌ Lost | $0.00 |
| 10/14 9:57:45 PM | ZEC | UP | 2.2 min | -0.398% | 2¢ | ❌ Lost | -$0.15 |
| 10/14 9:57:29 PM | AUDUSD | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:57:13 PM | COPPER | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:56:25 PM | PLATINUM | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:55:03 PM | PALLADIUM | UP | 5.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:54:48 PM | GOLD | UP | 5.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:44:56 PM | WTI | DOWN | 3 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:44:56 PM | PALLADIUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:44:40 PM | ZEC | UP | 19 sec | +0.036% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:44:40 PM | SILVER | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:44:24 PM | EURUSD | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:44:24 PM | DOGE | UP | 35 sec | -0.155% | 0¢ | ❌ Lost | $0.00 |
| 10/14 9:44:24 PM | NATGAS | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:44:24 PM | SOL | UP | 35 sec | -0.103% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:44:08 PM | XRP | UP | 52 sec | -0.276% | 0¢ | ❌ Lost | $0.00 |
| 10/14 9:44:08 PM | BNB | UP | 52 sec | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:43:50 PM | PLATINUM | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
