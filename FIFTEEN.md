# 15-Minute 1¢ Study

*Updated Wed Sep 30, 4:37 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 92 finished bets | 2% | $14.35 | +105% | +15.60¢ | $21.10 / -$6.75 |

*Expect about **39 buys a day** (~$5.92/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 92 | -$0.15 | -1% |
| Momentum model ≥ 5%, hold to the close | 164 | -$4.30 | -23% |
| Volatility model ≥ 5%, sell at 25¢ | 149 | -$5.82 | -37% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3017 | 3011 | 13 (0%) | 1.07% | -$186.55 (-51%) | Hold to the close: -$186.55 (-51%) |

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
| Volatility model | 1684 | 3.0% | 0.3% (5) | -475% | ❌ Worse |
| Momentum model | 1684 | 3.1% | 0.3% (5) | -535% | ❌ Worse |
| Mean-reversion model | 1684 | 5.8% | 0.3% (5) | -590% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1684 | 5 | -63% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 324 | 2 | -29% | -85% | -86% | -82% |
| Volatility model ≥ 5% | 149 | 0 | -100% | -74% | -73% | -63% |
| Volatility model ≥ 10% | 81 | 0 | -100% | -75% | -73% | -64% |
| Momentum model ≥ 2% | 292 | 1 | -60% | -85% | -88% | -85% |
| Momentum model ≥ 5% | 164 | 1 | -23% | -83% | -87% | -82% |
| Momentum model ≥ 10% | 103 | 0 | -100% | -87% | -84% | -80% |
| Mean-reversion model ≥ 2% | 622 | 3 | -48% | -86% | -87% | -82% |
| Mean-reversion model ≥ 5% | 401 | 3 | -20% | -83% | -82% | -74% |
| Mean-reversion model ≥ 10% | 247 | 2 | -9% | -77% | -77% | -68% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1880 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 910 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 221 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 3011 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$186.55 | -51% | — |
| Sell at 2¢ | 112 | 4% | -$339.43 | -92% | 47 sec |
| Sell at 3¢ | 70 | 2% | -$341.25 | -93% | 48 sec |
| Sell at 5¢ | 51 | 2% | -$335.40 | -91% | 64 sec |
| Sell at 10¢ | 42 | 1% | -$299.53 | -81% | 80 sec |
| Sell at 25¢ | 20 | 1% | -$288.35 | -78% | 1.7 min |
| Sell at 50¢ | 11 | 0% | -$252.30 | -68% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 92 | 2 | 10% | 2% | +105% | -83% | -89% |
| 2–5 min | 1008 | 6 | 7% | 3% | -42% | -88% | -90% |
| 1–2 min | 802 | 4 | 3% | 2% | -47% | -93% | -92% |
| Under 1 min | 1109 | 1 | 1% | 0% | -87% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 212 | 1 | 4% | 1% | -39% | -91% | -92% |
| ZEC | 211 | 1 | 5% | 3% | -43% | -88% | -90% |
| ETH | 210 | 2 | 5% | 4% | +14% | -88% | -86% |
| NEAR | 209 | 0 | 5% | 1% | -100% | -88% | -91% |
| XRP | 209 | 2 | 2% | 2% | +24% | -94% | -93% |
| SOL | 209 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 207 | 0 | 6% | 2% | -100% | -85% | -90% |
| BNB | 207 | 0 | 2% | 0% | -100% | -95% | -97% |
| HYPE | 206 | 1 | 5% | 3% | -39% | -89% | -86% |
| GOLD | 161 | 0 | 6% | 1% | -100% | -87% | -92% |
| SILVER | 141 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 140 | 1 | 4% | 1% | -24% | -93% | -94% |
| COPPER | 133 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 125 | 1 | 3% | 2% | -25% | -94% | -92% |
| PLATINUM | 105 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 105 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 80 | 1 | 5% | 2% | +17% | -91% | -90% |
| EURUSD | 74 | 1 | 4% | 1% | +26% | -93% | -96% |
| USDJPY | 67 | 2 | 3% | 3% | +179% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1559 | 8 | 4% | 2% | -41% | -92% | -92% |
| DOWN (bought NO) | 1452 | 5 | 4% | 2% | -61% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 191 | 0 | 2% | 2% | -100% | -92% | -91% |
| 0.05–0.1% | 252 | 0 | 1% | 0% | -100% | -96% | -98% |
| 0.1–0.2% | 456 | 1 | 4% | 2% | -71% | -91% | -92% |
| 0.2–0.5% | 686 | 2 | 6% | 3% | -68% | -88% | -89% |
| Over 0.5% | 294 | 4 | 6% | 2% | +41% | -89% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 817 | 2 | 4% | 1% | -72% | -91% | -94% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,526 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 4:29:58 AM | WTI | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:29:43 AM | USDJPY | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:29:43 AM | HYPE | DOWN | 17 sec | +0.005% | 0¢ | ❌ Lost | $0.00 |
| 9/30 4:29:43 AM | XRP | DOWN | 17 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 9/30 4:29:27 AM | EURUSD | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:29:11 AM | COPPER | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:29:11 AM | NATGAS | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:28:23 AM | PALLADIUM | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:28:07 AM | PLATINUM | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:27:51 AM | NEAR | DOWN | 2.1 min | +0.773% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:27:33 AM | ETH | DOWN | 2.4 min | +0.114% | 14¢ | ❌ Lost | -$0.15 |
| 9/30 4:27:33 AM | BNB | DOWN | 2.4 min | +0.108% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 4:27:01 AM | BTC | DOWN | 3.0 min | +0.127% | 11¢ | ❌ Lost | -$0.15 |
| 9/30 4:26:46 AM | SOL | DOWN | 3.2 min | +0.318% | 3¢ | ❌ Lost | -$0.15 |
| 9/30 4:26:31 AM | ZEC | DOWN | 3.5 min | +0.411% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:25:59 AM | DOGE | DOWN | 4.0 min | +0.468% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:25:27 AM | GBPUSD | DOWN | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:14:48 AM | ZEC | DOWN | 12 sec | -0.012% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:14:32 AM | SOL | DOWN | 28 sec | +0.064% | 0¢ | ❌ Lost | $0.00 |
| 9/30 4:14:32 AM | PALLADIUM | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:14:16 AM | XRP | UP | 44 sec | -0.073% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:14:16 AM | COPPER | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:13:44 AM | DOGE | DOWN | 75 sec | +0.193% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:13:44 AM | ETH | DOWN | 75 sec | +0.105% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:13:28 AM | HYPE | UP | 1.5 min | -0.142% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:12:07 AM | BTC | DOWN | 2.9 min | +0.138% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:11:21 AM | NATGAS | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:10:33 AM | NEAR | DOWN | 4.4 min | +0.653% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:10:01 AM | BNB | DOWN | 5.0 min | +0.248% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:59:56 AM | XRP | UP | 3 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
