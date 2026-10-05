# 15-Minute 1¢ Study

*Updated Mon Oct 5, 10:01 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 598 finished bets | 1% | $33.35 | +52% | +5.58¢ | -$4.70 / $38.05 |

*Expect about **81 buys a day** (~$12.14/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 598 | $20.10 | +31% |
| Volatility model ≥ 2%, hold to the close | 1115 | $19.30 | +14% |
| 5+ min left, hold to the close | 221 | $9.30 | +28% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8608 | 8602 | 37 (0%) | 1.07% | -$516.70 (-50%) | Hold to the close: -$516.70 (-50%) |

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
| Volatility model | 5677 | 4.1% | 0.4% (25) | -600% | ❌ Worse |
| Momentum model | 5677 | 4.2% | 0.4% (25) | -626% | ❌ Worse |
| Mean-reversion model | 5677 | 6.8% | 0.4% (25) | -703% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5677 | 25 | -44% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1115 | 11 | +14% | -70% | -70% | -65% |
| Volatility model ≥ 5% | 598 | 7 | +52% | -56% | -55% | -51% |
| Volatility model ≥ 10% | 371 | 5 | +98% | -37% | -38% | -33% |
| Momentum model ≥ 2% | 981 | 8 | -2% | -70% | -73% | -70% |
| Momentum model ≥ 5% | 598 | 6 | +31% | -61% | -64% | -61% |
| Momentum model ≥ 10% | 416 | 5 | +71% | -49% | -50% | -47% |
| Mean-reversion model ≥ 2% | 1966 | 14 | -22% | -83% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1319 | 12 | +1% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 871 | 9 | +19% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5874 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2065 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 663 | 3% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8602 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$516.70 | -50% | — |
| Sell at 2¢ | 333 | 4% | -$920.12 | -89% | 33 sec |
| Sell at 3¢ | 216 | 3% | -$922.46 | -89% | 48 sec |
| Sell at 5¢ | 160 | 2% | -$902.70 | -87% | 61 sec |
| Sell at 10¢ | 107 | 1% | -$852.53 | -82% | 66 sec |
| Sell at 25¢ | 59 | 1% | -$769.41 | -74% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$679.70 | -66% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 218 | 3 | 11% | 3% | +30% | -81% | -88% |
| 2–5 min | 2792 | 20 | 7% | 4% | -30% | -87% | -87% |
| 1–2 min | 2270 | 9 | 3% | 2% | -57% | -93% | -93% |
| Under 1 min | 3319 | 5 | 1% | 0% | -77% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 664 | 5 | 5% | 3% | -10% | -89% | -89% |
| DOGE | 656 | 2 | 4% | 2% | -61% | -90% | -90% |
| ETH | 655 | 5 | 6% | 3% | -4% | -87% | -87% |
| HYPE | 655 | 3 | 5% | 3% | -44% | -89% | -87% |
| BNB | 651 | 2 | 4% | 2% | -63% | -90% | -92% |
| XRP | 650 | 4 | 2% | 1% | -22% | -77% | -77% |
| SOL | 650 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 648 | 3 | 6% | 2% | -39% | -86% | -89% |
| NEAR | 645 | 3 | 7% | 3% | -40% | -64% | -65% |
| GOLD | 348 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 334 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 318 | 2 | 3% | 1% | -33% | -94% | -96% |
| COPPER | 294 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 261 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 257 | 2 | 4% | 2% | -27% | -94% | -92% |
| PALLADIUM | 253 | 1 | 2% | 1% | -63% | -97% | -98% |
| EURUSD | 236 | 1 | 5% | 3% | -60% | -92% | -90% |
| GBPUSD | 227 | 1 | 4% | 2% | -59% | -94% | -94% |
| USDJPY | 200 | 3 | 2% | 2% | +40% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4351 | 20 | 4% | 2% | -46% | -89% | -88% |
| DOWN (bought NO) | 4251 | 17 | 4% | 2% | -54% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 968 | 7 | 2% | 1% | +23% | -59% | -58% |
| 0.05–0.1% | 981 | 2 | 3% | 1% | -70% | -91% | -92% |
| 0.1–0.2% | 1464 | 6 | 4% | 2% | -48% | -91% | -91% |
| 0.2–0.5% | 1738 | 8 | 6% | 3% | -49% | -88% | -87% |
| Over 0.5% | 721 | 4 | 7% | 3% | -43% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2229 | 17 | 5% | 3% | -13% | -89% | -88% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,129 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 9:59:49 AM | COPPER | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:59:49 AM | DOGE | UP | 10 sec | -0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:59:17 AM | HYPE | UP | 42 sec | -0.158% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:59:03 AM | USDJPY | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:58:47 AM | BNB | UP | 73 sec | -0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:58:47 AM | SOL | UP | 73 sec | -0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:58:31 AM | ETH | UP | 89 sec | -0.113% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:58:31 AM | BTC | UP | 89 sec | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:58:15 AM | XRP | UP | 1.8 min | -0.201% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:58:15 AM | ZEC | UP | 1.8 min | -0.309% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:57:42 AM | NEAR | DOWN | 2.3 min | +0.284% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:56:06 AM | WTI | UP | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:44:36 AM | COPPER | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:44:36 AM | PLATINUM | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:44:20 AM | PALLADIUM | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:44:20 AM | GOLD | UP | 39 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:44:20 AM | NEAR | UP | 39 sec | -0.403% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:43:30 AM | BNB | UP | 1.5 min | -0.174% | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:43:14 AM | XRP | UP | 1.8 min | -0.320% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:43:14 AM | ETH | UP | 1.8 min | -0.198% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:43:14 AM | DOGE | UP | 1.8 min | -0.311% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:43:14 AM | SOL | UP | 1.8 min | -0.280% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:40:49 AM | ZEC | UP | 4.2 min | -1.090% | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:40:49 AM | BTC | UP | 4.2 min | -0.347% | 6¢ | ❌ Lost | -$0.15 |
| 10/5 9:40:33 AM | HYPE | UP | 4.4 min | -0.630% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:29:51 AM | PALLADIUM | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 9:29:51 AM | GOLD | DOWN | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:29:51 AM | SILVER | DOWN | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 9:29:51 AM | BTC | UP | 9 sec | +0.016% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 9:29:51 AM | DOGE | DOWN | 9 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
