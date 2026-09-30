# 15-Minute 1¢ Study

*Updated Wed Sep 30, 10:01 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 111 finished bets | 2% | $11.50 | +70% | +10.36¢ | $19.75 / -$8.25 |

*Expect about **43 buys a day** (~$6.51/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 111 | -$3.00 | -18% |
| Momentum model ≥ 5%, hold to the close | 184 | -$6.55 | -32% |
| Volatility model ≥ 5%, sell at 25¢ | 172 | -$8.82 | -47% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3306 | 3300 | 13 (0%) | 1.07% | -$222.40 (-55%) | Hold to the close: -$222.40 (-55%) |

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
| Volatility model | 1859 | 3.1% | 0.3% (5) | -531% | ❌ Worse |
| Momentum model | 1859 | 3.2% | 0.3% (5) | -591% | ❌ Worse |
| Mean-reversion model | 1859 | 6.1% | 0.3% (5) | -662% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1859 | 5 | -66% | -90% | -90% | -87% |
| Volatility model ≥ 2% | 366 | 2 | -38% | -85% | -85% | -81% |
| Volatility model ≥ 5% | 172 | 0 | -100% | -76% | -75% | -69% |
| Volatility model ≥ 10% | 92 | 0 | -100% | -79% | -77% | -70% |
| Momentum model ≥ 2% | 332 | 1 | -65% | -84% | -85% | -82% |
| Momentum model ≥ 5% | 184 | 1 | -32% | -84% | -87% | -81% |
| Momentum model ≥ 10% | 117 | 0 | -100% | -89% | -86% | -83% |
| Mean-reversion model ≥ 2% | 707 | 3 | -55% | -87% | -87% | -83% |
| Mean-reversion model ≥ 5% | 459 | 3 | -31% | -84% | -83% | -76% |
| Mean-reversion model ≥ 10% | 283 | 2 | -22% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2055 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 996 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 249 | 4% | 2% | 2% | 2% | 1% | 1% |
| **All** | 3300 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$222.40 | -55% | — |
| Sell at 2¢ | 125 | 4% | -$371.90 | -92% | 47 sec |
| Sell at 3¢ | 81 | 2% | -$372.81 | -92% | 49 sec |
| Sell at 5¢ | 60 | 2% | -$365.40 | -90% | 64 sec |
| Sell at 10¢ | 47 | 1% | -$328.83 | -81% | 78 sec |
| Sell at 25¢ | 23 | 1% | -$314.27 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$281.40 | -70% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 111 | 2 | 10% | 3% | +70% | -83% | -88% |
| 2–5 min | 1103 | 6 | 7% | 3% | -47% | -88% | -89% |
| 1–2 min | 876 | 4 | 4% | 2% | -51% | -93% | -91% |
| Under 1 min | 1210 | 1 | 1% | 0% | -88% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 232 | 1 | 4% | 2% | -45% | -90% | -89% |
| ZEC | 230 | 1 | 5% | 3% | -48% | -88% | -91% |
| NEAR | 229 | 0 | 5% | 1% | -100% | -89% | -91% |
| ETH | 229 | 2 | 5% | 4% | +5% | -88% | -85% |
| XRP | 229 | 2 | 2% | 2% | +15% | -95% | -94% |
| BTC | 227 | 0 | 7% | 3% | -100% | -85% | -88% |
| BNB | 227 | 0 | 3% | 1% | -100% | -94% | -94% |
| SOL | 226 | 0 | 3% | 1% | -100% | -92% | -92% |
| HYPE | 226 | 1 | 4% | 3% | -45% | -90% | -88% |
| GOLD | 175 | 0 | 6% | 2% | -100% | -87% | -90% |
| SILVER | 155 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 153 | 1 | 3% | 1% | -30% | -94% | -94% |
| COPPER | 143 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 136 | 1 | 4% | 2% | -31% | -94% | -90% |
| PLATINUM | 118 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 116 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 91 | 1 | 5% | 2% | +3% | -90% | -91% |
| EURUSD | 82 | 1 | 4% | 1% | +14% | -94% | -97% |
| USDJPY | 76 | 2 | 3% | 3% | +146% | -95% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1703 | 8 | 4% | 2% | -46% | -92% | -92% |
| DOWN (bought NO) | 1597 | 5 | 4% | 2% | -64% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 207 | 0 | 2% | 1% | -100% | -93% | -92% |
| 0.05–0.1% | 265 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 489 | 1 | 4% | 1% | -73% | -91% | -92% |
| 0.2–0.5% | 739 | 2 | 6% | 3% | -70% | -88% | -88% |
| Over 0.5% | 354 | 4 | 6% | 3% | +17% | -89% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 865 | 6 | 4% | 2% | -21% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,414 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 9:59:49 AM | ETH | DOWN | 11 sec | -0.004% | 0¢ | ❌ Lost | $0.00 |
| 9/30 9:59:49 AM | BTC | DOWN | 11 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 9/30 9:59:33 AM | NATGAS | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:59:16 AM | SILVER | UP | 43 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 9:59:16 AM | GBPUSD | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:58:57 AM | PLATINUM | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:58:25 AM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:58:25 AM | DOGE | DOWN | 1.6 min | +0.225% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:58:11 AM | XRP | DOWN | 1.8 min | +0.213% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:57:54 AM | WTI | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:57:38 AM | BNB | DOWN | 2.4 min | +0.117% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:57:22 AM | ZEC | DOWN | 2.6 min | +0.561% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:57:06 AM | SOL | DOWN | 2.9 min | +0.324% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:53:51 AM | HYPE | DOWN | 6.1 min | +1.351% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:53:19 AM | NEAR | DOWN | 6.7 min | +1.337% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:44:30 AM | COPPER | UP | 30 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:44:30 AM | USDJPY | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:44:15 AM | GBPUSD | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:43:42 AM | EURUSD | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:43:42 AM | NATGAS | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:42:21 AM | XRP | DOWN | 2.6 min | +0.408% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:41:32 AM | SOL | DOWN | 3.5 min | +0.405% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:41:32 AM | BNB | DOWN | 3.5 min | +0.291% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:41:15 AM | DOGE | DOWN | 3.7 min | +0.755% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:40:26 AM | ETH | DOWN | 4.5 min | +0.388% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:39:54 AM | NEAR | DOWN | 5.1 min | +1.042% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:39:37 AM | BTC | DOWN | 5.4 min | +0.409% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:39:21 AM | HYPE | DOWN | 5.7 min | +1.168% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:39:21 AM | ZEC | DOWN | 5.7 min | +1.119% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:28:52 AM | PALLADIUM | UP | 68 sec | — | 14¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
