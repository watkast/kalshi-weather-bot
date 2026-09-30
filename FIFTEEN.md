# 15-Minute 1¢ Study

*Updated Wed Sep 30, 4:47 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 93 finished bets | 2% | $14.20 | +103% | +15.27¢ | $21.10 / -$6.90 |

*Expect about **40 buys a day** (~$5.97/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 93 | -$0.30 | -2% |
| Momentum model ≥ 5%, hold to the close | 165 | -$4.45 | -24% |
| Volatility model ≥ 5%, sell at 25¢ | 150 | -$5.97 | -38% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3030 | 3024 | 13 (0%) | 1.07% | -$188.05 (-51%) | Hold to the close: -$188.05 (-51%) |

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
| Volatility model | 1693 | 2.9% | 0.3% (5) | -474% | ❌ Worse |
| Momentum model | 1693 | 3.1% | 0.3% (5) | -534% | ❌ Worse |
| Mean-reversion model | 1693 | 5.8% | 0.3% (5) | -589% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1693 | 5 | -63% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 325 | 2 | -29% | -85% | -86% | -82% |
| Volatility model ≥ 5% | 150 | 0 | -100% | -74% | -73% | -63% |
| Volatility model ≥ 10% | 82 | 0 | -100% | -75% | -73% | -65% |
| Momentum model ≥ 2% | 293 | 1 | -60% | -85% | -88% | -85% |
| Momentum model ≥ 5% | 165 | 1 | -24% | -83% | -87% | -82% |
| Momentum model ≥ 10% | 104 | 0 | -100% | -87% | -84% | -81% |
| Mean-reversion model ≥ 2% | 625 | 3 | -49% | -86% | -87% | -82% |
| Mean-reversion model ≥ 5% | 403 | 3 | -20% | -83% | -82% | -74% |
| Mean-reversion model ≥ 10% | 249 | 2 | -10% | -78% | -78% | -69% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1889 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 914 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 221 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 3024 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$188.05 | -51% | — |
| Sell at 2¢ | 113 | 4% | -$340.67 | -92% | 47 sec |
| Sell at 3¢ | 71 | 2% | -$342.36 | -93% | 49 sec |
| Sell at 5¢ | 52 | 2% | -$336.25 | -91% | 64 sec |
| Sell at 10¢ | 43 | 1% | -$299.72 | -81% | 78 sec |
| Sell at 25¢ | 21 | 1% | -$286.54 | -77% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$247.05 | -67% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 93 | 2 | 10% | 2% | +103% | -83% | -89% |
| 2–5 min | 1012 | 6 | 7% | 3% | -43% | -88% | -90% |
| 1–2 min | 805 | 4 | 4% | 2% | -47% | -93% | -91% |
| Under 1 min | 1114 | 1 | 1% | 0% | -87% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 213 | 1 | 4% | 1% | -40% | -91% | -92% |
| ZEC | 212 | 1 | 5% | 3% | -43% | -88% | -91% |
| ETH | 211 | 2 | 5% | 4% | +13% | -88% | -86% |
| NEAR | 210 | 0 | 5% | 1% | -100% | -89% | -91% |
| XRP | 210 | 2 | 2% | 2% | +23% | -94% | -93% |
| SOL | 210 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 208 | 0 | 6% | 2% | -100% | -86% | -90% |
| BNB | 208 | 0 | 2% | 0% | -100% | -95% | -97% |
| HYPE | 207 | 1 | 5% | 3% | -39% | -89% | -86% |
| GOLD | 162 | 0 | 6% | 1% | -100% | -88% | -92% |
| SILVER | 142 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 141 | 1 | 4% | 1% | -25% | -93% | -94% |
| COPPER | 133 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 126 | 1 | 4% | 2% | -26% | -93% | -90% |
| PLATINUM | 105 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 105 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 80 | 1 | 5% | 2% | +17% | -91% | -90% |
| EURUSD | 74 | 1 | 4% | 1% | +26% | -93% | -96% |
| USDJPY | 67 | 2 | 3% | 3% | +179% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1563 | 8 | 4% | 2% | -42% | -92% | -92% |
| DOWN (bought NO) | 1461 | 5 | 4% | 2% | -61% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 193 | 0 | 2% | 2% | -100% | -92% | -91% |
| 0.05–0.1% | 252 | 0 | 1% | 0% | -100% | -96% | -98% |
| 0.1–0.2% | 459 | 1 | 4% | 2% | -71% | -91% | -92% |
| 0.2–0.5% | 688 | 2 | 6% | 3% | -68% | -89% | -89% |
| Over 0.5% | 296 | 4 | 6% | 2% | +40% | -89% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 830 | 2 | 4% | 1% | -73% | -91% | -94% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,518 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 4:44:50 AM | SILVER | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 4:44:18 AM | ETH | DOWN | 41 sec | +0.049% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:44:18 AM | HYPE | DOWN | 41 sec | +0.143% | 0¢ | ❌ Lost | $0.00 |
| 9/30 4:44:02 AM | SOL | DOWN | 58 sec | +0.182% | 0¢ | ❌ Lost | $0.00 |
| 9/30 4:44:02 AM | GOLD | UP | 58 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:43:44 AM | WTI | UP | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:43:44 AM | BNB | DOWN | 75 sec | +0.050% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:43:44 AM | NATGAS | UP | 75 sec | — | 51¢ | ❌ Lost | -$0.15 |
| 9/30 4:42:58 AM | DOGE | DOWN | 2.0 min | +0.311% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:42:41 AM | BTC | DOWN | 2.3 min | +0.127% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:42:09 AM | XRP | DOWN | 2.9 min | +0.258% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:40:19 AM | ZEC | DOWN | 4.7 min | +0.538% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:38:10 AM | NEAR | DOWN | 6.8 min | +1.417% | 2¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
