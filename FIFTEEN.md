# 15-Minute 1¢ Study

*Updated Thu Oct 15, 6:47 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1494 finished bets | 1% | $86.85 | +53% | +5.81¢ | $31.75 / $55.10 |

*Expect about **87 buys a day** (~$12.99/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1400 | $58.35 | +38% |
| Momentum model ≥ 2%, hold to the close | 2331 | $10.15 | +4% |
| Volatility model ≥ 2%, hold to the close | 2694 | -$3.35 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19237 | 19230 | 75 (0%) | 1.07% | -$1,282.80 (-55%) | Hold to the close: -$1,282.80 (-55%) |

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
| Volatility model | 12426 | 4.5% | 0.4% (52) | -645% | ❌ Worse |
| Momentum model | 12426 | 4.4% | 0.4% (52) | -669% | ❌ Worse |
| Mean-reversion model | 12426 | 7.4% | 0.4% (52) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12426 | 52 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2694 | 23 | -1% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1494 | 18 | +53% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 889 | 11 | +76% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2331 | 20 | +4% | -79% | -80% | -77% |
| Momentum model ≥ 5% | 1400 | 15 | +38% | -76% | -76% | -72% |
| Momentum model ≥ 10% | 941 | 10 | +49% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4603 | 32 | -24% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3153 | 25 | -12% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 2072 | 14 | -22% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12624 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4730 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1876 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19230 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 75 | 0% | -$1,282.80 | -55% | — |
| Sell at 2¢ | 682 | 4% | -$2,099.48 | -90% | 34 sec |
| Sell at 3¢ | 459 | 2% | -$2,097.79 | -90% | 47 sec |
| Sell at 5¢ | 335 | 2% | -$2,059.05 | -88% | 50 sec |
| Sell at 10¢ | 210 | 1% | -$1,973.70 | -85% | 64 sec |
| Sell at 25¢ | 122 | 1% | -$1,802.98 | -77% | 80 sec |
| Sell at 50¢ | 79 | 0% | -$1,603.55 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 613 | 5 | 11% | 3% | -22% | -81% | -86% |
| 2–5 min | 6211 | 35 | 7% | 3% | -44% | -88% | -88% |
| 1–2 min | 5006 | 19 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 7396 | 16 | 1% | 0% | -69% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1417 | 11 | 5% | 3% | -3% | -89% | -89% |
| HYPE | 1411 | 4 | 4% | 2% | -65% | -90% | -89% |
| ETH | 1407 | 8 | 5% | 3% | -31% | -88% | -87% |
| BNB | 1406 | 5 | 5% | 2% | -56% | -90% | -89% |
| DOGE | 1405 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1401 | 2 | 3% | 1% | -82% | -93% | -92% |
| XRP | 1394 | 7 | 3% | 1% | -38% | -85% | -86% |
| BTC | 1392 | 7 | 5% | 2% | -33% | -88% | -91% |
| NEAR | 1391 | 8 | 5% | 3% | -25% | -78% | -78% |
| GOLD | 772 | 1 | 4% | 1% | -85% | -92% | -94% |
| SILVER | 751 | 4 | 3% | 1% | -38% | -78% | -78% |
| WTI | 721 | 3 | 3% | 1% | -52% | -94% | -96% |
| COPPER | 665 | 1 | 2% | 2% | -86% | -97% | -96% |
| PLATINUM | 639 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 592 | 1 | 1% | 0% | -84% | -98% | -98% |
| NATGAS | 590 | 4 | 3% | 2% | -37% | -96% | -94% |
| EURUSD | 580 | 3 | 3% | 1% | -52% | -79% | -79% |
| GBPUSD | 544 | 1 | 2% | 1% | -83% | -97% | -97% |
| USDJPY | 500 | 3 | 1% | 1% | -44% | -99% | -98% |
| AUDUSD | 130 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 122 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9738 | 38 | 3% | 2% | -55% | -89% | -88% |
| DOWN (bought NO) | 9492 | 37 | 4% | 2% | -55% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2137 | 11 | 2% | 1% | -14% | -78% | -78% |
| 0.05–0.1% | 2194 | 7 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 3185 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3667 | 20 | 6% | 3% | -40% | -88% | -88% |
| Over 0.5% | 1438 | 6 | 6% | 2% | -57% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4363 | 23 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,466 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 6:44:52 AM | ZEC | UP | 7 sec | -0.117% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:44:37 AM | COPPER | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:44:37 AM | GOLD | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:44:37 AM | SILVER | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:44:21 AM | WTI | DOWN | 38 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:44:05 AM | BTC | UP | 54 sec | -0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:43:49 AM | EURUSD | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:43:49 AM | BNB | UP | 71 sec | -0.183% | 1¢ | ❌ Lost | $0.00 |
| 10/15 6:43:33 AM | SOL | UP | 86 sec | -0.234% | 2¢ | ❌ Lost | -$0.15 |
| 10/15 6:43:33 AM | NEAR | UP | 86 sec | -0.549% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:43:17 AM | USDJPY | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:43:17 AM | GBPUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:43:01 AM | XRP | UP | 2.0 min | -0.550% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:43:01 AM | DOGE | UP | 2.0 min | -0.388% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:43:01 AM | ETH | UP | 2.0 min | -0.510% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:42:30 AM | HYPE | UP | 2.5 min | -0.499% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:41:42 AM | PALLADIUM | DOWN | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:29:52 AM | ZEC | UP | 8 sec | -0.200% | 0¢ | ❌ Lost | $0.00 |
| 10/15 6:29:52 AM | HYPE | DOWN | 8 sec | +0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/15 6:29:36 AM | DOGE | DOWN | 23 sec | +0.001% | 1¢ | ❌ Lost | $0.00 |
| 10/15 6:29:36 AM | GOLD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:29:36 AM | AUDUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:29:36 AM | USDCAD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:29:20 AM | PALLADIUM | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:29:20 AM | BNB | DOWN | 39 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/15 6:29:04 AM | SOL | DOWN | 55 sec | +0.132% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:29:04 AM | WTI | UP | 55 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:28:48 AM | XRP | DOWN | 72 sec | +0.245% | 0¢ | ❌ Lost | $0.00 |
| 10/15 6:28:48 AM | BTC | DOWN | 72 sec | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:28:48 AM | ETH | DOWN | 72 sec | +0.191% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
