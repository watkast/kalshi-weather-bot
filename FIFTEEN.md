# 15-Minute 1¢ Study

*Updated Sat Oct 3, 4:09 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 171 finished bets | 1% | $2.80 | +11% | +1.64¢ | $15.40 / -$12.60 |

*Expect about **32 buys a day** (~$4.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 419 | -$2.40 | -5% |
| Momentum model ≥ 5%, sell at 50¢ | 419 | -$9.65 | -22% |
| 5+ min left, sell at 50¢ | 171 | -$11.70 | -46% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6413 | 6407 | 24 (0%) | 1.07% | -$438.00 (-57%) | Hold to the close: -$438.00 (-57%) |

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
| Volatility model | 3871 | 4.0% | 0.3% (12) | -715% | ❌ Worse |
| Momentum model | 3871 | 4.1% | 0.3% (12) | -756% | ❌ Worse |
| Mean-reversion model | 3871 | 7.0% | 0.3% (12) | -868% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3871 | 12 | -60% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 815 | 5 | -29% | -67% | -67% | -63% |
| Volatility model ≥ 5% | 420 | 2 | -38% | -47% | -48% | -44% |
| Volatility model ≥ 10% | 250 | 2 | +21% | -17% | -21% | -14% |
| Momentum model ≥ 2% | 713 | 4 | -32% | -66% | -69% | -66% |
| Momentum model ≥ 5% | 419 | 3 | -5% | -52% | -56% | -51% |
| Momentum model ≥ 10% | 285 | 2 | +3% | -34% | -37% | -32% |
| Mean-reversion model ≥ 2% | 1450 | 7 | -48% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 974 | 6 | -32% | -80% | -82% | -75% |
| Mean-reversion model ≥ 10% | 635 | 4 | -27% | -77% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4068 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6407 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 24 | 0% | -$438.00 | -57% | — |
| Sell at 2¢ | 254 | 4% | -$693.96 | -90% | 34 sec |
| Sell at 3¢ | 160 | 2% | -$697.60 | -90% | 48 sec |
| Sell at 5¢ | 118 | 2% | -$683.30 | -88% | 62 sec |
| Sell at 10¢ | 78 | 1% | -$643.82 | -83% | 81 sec |
| Sell at 25¢ | 42 | 1% | -$592.98 | -77% | 1.6 min |
| Sell at 50¢ | 22 | 0% | -$541.50 | -70% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 2096 | 13 | 8% | 4% | -39% | -86% | -87% |
| 1–2 min | 1661 | 6 | 3% | 2% | -61% | -94% | -93% |
| Under 1 min | 2479 | 3 | 1% | 0% | -82% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 458 | 2 | 4% | 1% | -42% | -90% | -91% |
| ZEC | 456 | 2 | 5% | 3% | -48% | -89% | -91% |
| ETH | 455 | 2 | 6% | 3% | -45% | -86% | -85% |
| HYPE | 455 | 2 | 5% | 4% | -46% | -88% | -85% |
| BNB | 451 | 1 | 4% | 2% | -73% | -90% | -92% |
| BTC | 450 | 1 | 6% | 3% | -71% | -85% | -88% |
| SOL | 449 | 0 | 3% | 1% | -100% | -93% | -92% |
| XRP | 448 | 3 | 2% | 1% | -13% | -67% | -67% |
| NEAR | 446 | 1 | 6% | 2% | -70% | -85% | -87% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 274 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 225 | 2 | 4% | 2% | -17% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3258 | 15 | 4% | 2% | -46% | -91% | -91% |
| DOWN (bought NO) | 3149 | 9 | 4% | 2% | -67% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 544 | 2 | 1% | 1% | -32% | -62% | -61% |
| 0.05–0.1% | 615 | 0 | 3% | 1% | -100% | -91% | -93% |
| 0.1–0.2% | 995 | 3 | 4% | 2% | -60% | -90% | -91% |
| 0.2–0.5% | 1321 | 5 | 6% | 3% | -58% | -88% | -87% |
| Over 0.5% | 591 | 4 | 7% | 3% | -30% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1604 | 6 | 4% | 2% | -57% | -91% | -93% |
| Morning (6am–12pm) | 1640 | 9 | 5% | 3% | -38% | -90% | -88% |
| Afternoon (12–6pm) | 1305 | 3 | 4% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,326 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 3:59:49 AM | BTC | DOWN | 10 sec | +0.006% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:59:33 AM | BNB | UP | 26 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:59:17 AM | HYPE | UP | 42 sec | -0.112% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 3:58:43 AM | DOGE | DOWN | 77 sec | +0.028% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:58:11 AM | ETH | UP | 1.8 min | -0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:57:23 AM | ZEC | DOWN | 2.6 min | +0.283% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:56:51 AM | NEAR | DOWN | 3.1 min | +0.403% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:44:41 AM | BTC | UP | 19 sec | -0.018% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:44:41 AM | BNB | UP | 19 sec | -0.043% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 3:44:09 AM | ZEC | DOWN | 51 sec | +0.143% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:44:09 AM | HYPE | DOWN | 51 sec | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:43:54 AM | XRP | DOWN | 65 sec | +0.041% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:43:54 AM | NEAR | DOWN | 65 sec | +0.071% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:43:54 AM | SOL | DOWN | 65 sec | +0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:43:23 AM | DOGE | DOWN | 1.6 min | +0.092% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 3:42:51 AM | ETH | UP | 2.1 min | -0.091% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:29:53 AM | BNB | DOWN | 6 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:29:36 AM | ETH | UP | 24 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:29:04 AM | ZEC | UP | 56 sec | -0.095% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 3:28:32 AM | BTC | UP | 88 sec | -0.055% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:27:45 AM | HYPE | DOWN | 2.2 min | +0.084% | 3¢ | ❌ Lost | -$0.15 |
| 10/3 3:27:30 AM | SOL | UP | 2.5 min | -0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:27:14 AM | NEAR | UP | 2.8 min | -0.287% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:26:58 AM | XRP | UP | 3.0 min | -0.209% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:25:38 AM | DOGE | UP | 4.3 min | -0.290% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:14:32 AM | BTC | DOWN | 28 sec | +0.009% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:14:32 AM | NEAR | UP | 28 sec | -0.205% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:14:32 AM | ZEC | UP | 28 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/3 3:12:56 AM | SOL | DOWN | 2.1 min | +0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 3:12:41 AM | HYPE | DOWN | 2.3 min | +0.116% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
