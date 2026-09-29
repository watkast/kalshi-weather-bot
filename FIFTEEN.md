# 15-Minute 1¢ Study

*Updated Tue Sep 29, 2:50 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 59 finished bets | 3% | $19.15 | +216% | +32.46¢ | $23.65 / -$4.50 |

*Expect about **47 buys a day** (~$7.04/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 218 | $13.80 | +49% |
| 5+ min left, sell at 50¢ | 59 | $4.65 | +53% |
| Volatility model ≥ 5%, sell at 25¢ | 78 | $1.83 | +23% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1722 | 1716 | 8 (0%) | 1.07% | -$94.55 (-46%) | Hold to the close: -$94.55 (-46%) |

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
| Volatility model | 888 | 2.8% | 0.5% (4) | -383% | ❌ Worse |
| Momentum model | 888 | 3.0% | 0.5% (4) | -456% | ❌ Worse |
| Mean-reversion model | 888 | 5.9% | 0.5% (4) | -460% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 888 | 4 | -42% | -90% | -91% | -86% |
| Volatility model ≥ 2% | 169 | 1 | -30% | -84% | -86% | -80% |
| Volatility model ≥ 5% | 78 | 0 | -100% | -71% | -71% | -60% |
| Volatility model ≥ 10% | 41 | 0 | -100% | -71% | -68% | -46% |
| Momentum model ≥ 2% | 140 | 0 | -100% | -85% | -90% | -88% |
| Momentum model ≥ 5% | 82 | 0 | -100% | -82% | -91% | -85% |
| Momentum model ≥ 10% | 55 | 0 | -100% | -90% | -85% | -75% |
| Mean-reversion model ≥ 2% | 332 | 3 | -1% | -86% | -86% | -80% |
| Mean-reversion model ≥ 5% | 218 | 3 | +49% | -83% | -83% | -75% |
| Mean-reversion model ≥ 10% | 138 | 2 | +65% | -79% | -79% | -69% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1083 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 531 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 102 | 3% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1716 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$94.55 | -46% | — |
| Sell at 2¢ | 55 | 3% | -$192.25 | -93% | 47 sec |
| Sell at 3¢ | 34 | 2% | -$193.29 | -94% | 47 sec |
| Sell at 5¢ | 25 | 1% | -$190.30 | -92% | 81 sec |
| Sell at 10¢ | 23 | 1% | -$176.42 | -85% | 1.9 min |
| Sell at 25¢ | 13 | 1% | -$163.52 | -79% | 2.1 min |
| Sell at 50¢ | 9 | 1% | -$145.80 | -71% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 59 | 2 | 8% | 3% | +216% | -85% | -87% |
| 2–5 min | 578 | 5 | 6% | 3% | -16% | -89% | -90% |
| 1–2 min | 471 | 1 | 2% | 1% | -77% | -96% | -96% |
| Under 1 min | 608 | 0 | 1% | 0% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 124 | 2 | 5% | 3% | +103% | -89% | -86% |
| ZEC | 122 | 1 | 6% | 2% | +0% | -87% | -94% |
| NEAR | 121 | 0 | 5% | 2% | -100% | -87% | -93% |
| DOGE | 121 | 1 | 4% | 2% | +3% | -90% | -86% |
| XRP | 121 | 2 | 3% | 2% | +107% | -92% | -91% |
| BTC | 120 | 0 | 8% | 2% | -100% | -81% | -87% |
| SOL | 120 | 0 | 2% | 2% | -100% | -93% | -90% |
| BNB | 118 | 0 | 3% | 1% | -100% | -95% | -95% |
| HYPE | 116 | 0 | 3% | 2% | -100% | -94% | -94% |
| GOLD | 93 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 84 | 0 | 1% | 0% | -100% | -98% | -100% |
| SILVER | 84 | 0 | 1% | 0% | -100% | -97% | -96% |
| COPPER | 76 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 72 | 0 | 3% | 1% | -100% | -95% | -93% |
| PLATINUM | 69 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 53 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 38 | 0 | 3% | 0% | -100% | -95% | -93% |
| USDJPY | 33 | 2 | 6% | 6% | +466% | -89% | -84% |
| EURUSD | 31 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 910 | 5 | 4% | 2% | -36% | -92% | -92% |
| DOWN (bought NO) | 806 | 3 | 3% | 1% | -57% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 109 | 0 | 3% | 2% | -100% | -89% | -89% |
| 0.05–0.1% | 127 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 243 | 0 | 4% | 1% | -100% | -90% | -90% |
| 0.2–0.5% | 412 | 2 | 5% | 2% | -47% | -91% | -92% |
| Over 0.5% | 192 | 4 | 7% | 4% | +120% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 459 | 1 | 3% | 1% | -74% | -93% | -95% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,978 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 2:44:55 AM | SILVER | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:44:07 AM | GOLD | UP | 53 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:42:46 AM | PALLADIUM | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:41:24 AM | SOL | UP | 3.6 min | -0.450% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:41:08 AM | XRP | UP | 3.9 min | -0.689% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:41:08 AM | BTC | UP | 3.9 min | -0.392% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:40:53 AM | DOGE | UP | 4.1 min | -0.506% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:40:53 AM | ETH | UP | 4.1 min | -0.468% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:40:53 AM | HYPE | UP | 4.1 min | -0.425% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:40:19 AM | BNB | UP | 4.7 min | -0.282% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:40:03 AM | ZEC | UP | 5.0 min | -0.830% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:39:48 AM | NEAR | UP | 5.2 min | -1.051% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:29:19 AM | ZEC | UP | 40 sec | -0.186% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:29:19 AM | HYPE | DOWN | 40 sec | +0.080% | 0¢ | ❌ Lost | $0.00 |
| 9/29 2:29:03 AM | GBPUSD | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:28:31 AM | NATGAS | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:27:58 AM | BTC | DOWN | 2.0 min | +0.193% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:27:43 AM | XRP | DOWN | 2.3 min | +0.345% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:27:27 AM | SOL | DOWN | 2.5 min | +0.322% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:27:11 AM | ETH | DOWN | 2.8 min | +0.364% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:27:11 AM | DOGE | DOWN | 2.8 min | +0.393% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:26:23 AM | BNB | DOWN | 3.6 min | +0.275% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:25:51 AM | WTI | UP | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:22:37 AM | NEAR | DOWN | 7.4 min | +1.797% | 3¢ | ❌ Lost | -$0.15 |
| 9/29 2:14:20 AM | HYPE | DOWN | 39 sec | +0.068% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:14:20 AM | DOGE | UP | 39 sec | -0.081% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:14:04 AM | USDJPY | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 2:14:04 AM | BTC | DOWN | 56 sec | +0.105% | 0¢ | ❌ Lost | $0.00 |
| 9/29 2:14:04 AM | XRP | UP | 56 sec | -0.119% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 2:13:32 AM | SOL | UP | 88 sec | -0.173% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
