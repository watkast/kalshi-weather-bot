# 15-Minute 1¢ Study

*Updated Thu Oct 1, 11:09 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 140 finished bets | 1% | $7.45 | +36% | +5.32¢ | $17.50 / -$10.05 |

*Expect about **39 buys a day** (~$5.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 273 | -$2.15 | -7% |
| Volatility model ≥ 5%, sell at 25¢ | 263 | -$5.02 | -17% |
| Volatility model ≥ 5%, sell at 10¢ | 263 | -$5.78 | -20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4494 | 4488 | 14 (0%) | 1.07% | -$354.65 (-64%) | Hold to the close: -$354.65 (-64%) |

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
| Volatility model | 2561 | 3.5% | 0.2% (6) | -672% | ❌ Worse |
| Momentum model | 2561 | 3.7% | 0.2% (6) | -733% | ❌ Worse |
| Mean-reversion model | 2561 | 6.6% | 0.2% (6) | -844% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2561 | 6 | -71% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 523 | 3 | -35% | -63% | -65% | -60% |
| Volatility model ≥ 5% | 263 | 1 | -52% | -33% | -34% | -29% |
| Volatility model ≥ 10% | 151 | 1 | -3% | +15% | +13% | +20% |
| Momentum model ≥ 2% | 467 | 2 | -49% | -59% | -63% | -59% |
| Momentum model ≥ 5% | 273 | 2 | -7% | -39% | -42% | -36% |
| Momentum model ≥ 10% | 182 | 1 | -22% | -12% | -11% | -8% |
| Mean-reversion model ≥ 2% | 961 | 3 | -67% | -86% | -88% | -84% |
| Mean-reversion model ≥ 5% | 633 | 3 | -49% | -83% | -85% | -78% |
| Mean-reversion model ≥ 10% | 404 | 2 | -45% | -78% | -81% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2757 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1333 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 398 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 4488 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$354.65 | -64% | — |
| Sell at 2¢ | 167 | 4% | -$493.23 | -90% | 46 sec |
| Sell at 3¢ | 99 | 2% | -$498.04 | -90% | 49 sec |
| Sell at 5¢ | 73 | 2% | -$489.20 | -89% | 66 sec |
| Sell at 10¢ | 52 | 1% | -$454.53 | -83% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$443.21 | -80% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$413.65 | -75% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 137 | 2 | 13% | 3% | +39% | -77% | -88% |
| 2–5 min | 1475 | 6 | 7% | 3% | -61% | -88% | -89% |
| 1–2 min | 1165 | 4 | 3% | 2% | -64% | -94% | -93% |
| Under 1 min | 1708 | 2 | 1% | 0% | -83% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 312 | 1 | 4% | 1% | -58% | -90% | -92% |
| ETH | 309 | 2 | 5% | 3% | -21% | -89% | -87% |
| NEAR | 306 | 0 | 5% | 1% | -100% | -88% | -92% |
| ZEC | 306 | 1 | 5% | 2% | -61% | -89% | -94% |
| HYPE | 306 | 1 | 5% | 3% | -61% | -90% | -88% |
| BNB | 306 | 0 | 4% | 1% | -100% | -92% | -95% |
| BTC | 305 | 0 | 7% | 3% | -100% | -84% | -87% |
| XRP | 304 | 3 | 2% | 1% | +27% | -54% | -53% |
| SOL | 303 | 0 | 3% | 1% | -100% | -92% | -91% |
| GOLD | 230 | 0 | 4% | 1% | -100% | -90% | -93% |
| SILVER | 214 | 0 | 2% | 1% | -100% | -96% | -95% |
| WTI | 203 | 1 | 3% | 1% | -49% | -94% | -96% |
| COPPER | 188 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 175 | 1 | 4% | 2% | -47% | -93% | -91% |
| PLATINUM | 164 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 159 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 143 | 1 | 5% | 2% | -35% | -92% | -93% |
| EURUSD | 138 | 1 | 4% | 1% | -32% | -94% | -94% |
| USDJPY | 117 | 2 | 3% | 2% | +60% | -96% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2308 | 8 | 4% | 2% | -60% | -92% | -92% |
| DOWN (bought NO) | 2180 | 6 | 4% | 2% | -69% | -87% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 321 | 1 | 1% | 1% | -42% | -38% | -38% |
| 0.05–0.1% | 388 | 0 | 2% | 0% | -100% | -94% | -96% |
| 0.1–0.2% | 657 | 1 | 4% | 2% | -80% | -91% | -92% |
| 0.2–0.5% | 936 | 2 | 6% | 3% | -76% | -88% | -89% |
| Over 0.5% | 454 | 4 | 7% | 2% | -8% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1218 | 6 | 4% | 2% | -44% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,195 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 10:59:53 AM | GBPUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:59:53 AM | PALLADIUM | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:59:38 AM | PLATINUM | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:59:23 AM | NATGAS | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:59:23 AM | XRP | UP | 36 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:59:04 AM | HYPE | UP | 55 sec | -0.280% | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:59:04 AM | GOLD | UP | 55 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:58:18 AM | SILVER | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:58:18 AM | ZEC | UP | 1.7 min | -0.501% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:57:45 AM | BNB | UP | 2.2 min | -0.181% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:57:45 AM | COPPER | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:57:45 AM | ETH | UP | 2.2 min | -0.211% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:57:29 AM | DOGE | UP | 2.5 min | -0.402% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:57:29 AM | SOL | UP | 2.5 min | -0.287% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:57:29 AM | WTI | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:56:56 AM | EURUSD | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:56:24 AM | BTC | UP | 3.6 min | -0.242% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:55:18 AM | NEAR | UP | 4.7 min | -0.888% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:44:45 AM | SOL | UP | 15 sec | -0.108% | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:44:45 AM | WTI | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:44:29 AM | BNB | DOWN | 31 sec | -0.012% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:44:29 AM | DOGE | UP | 31 sec | -0.179% | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:44:29 AM | BTC | DOWN | 31 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:44:29 AM | SILVER | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:44:29 AM | GOLD | UP | 31 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 10:44:29 AM | ETH | UP | 31 sec | -0.034% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 10:43:40 AM | NEAR | UP | 80 sec | -0.465% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:42:52 AM | HYPE | UP | 2.1 min | -0.330% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:42:36 AM | XRP | UP | 2.4 min | -0.370% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 10:40:59 AM | ZEC | UP | 4.0 min | -2.256% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
