# 15-Minute 1¢ Study

*Updated Fri Oct 2, 5:29 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 171 finished bets | 1% | $2.80 | +11% | +1.64¢ | $15.40 / -$12.60 |

*Expect about **35 buys a day** (~$5.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 382 | $1.50 | +4% |
| Momentum model ≥ 5%, sell at 50¢ | 382 | -$5.75 | -14% |
| Volatility model ≥ 5%, sell at 25¢ | 380 | -$10.25 | -25% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6058 | 6043 | 23 (0%) | 1.07% | -$411.35 (-56%) | Hold to the close: -$411.35 (-56%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 3513 | 3.8% | 0.3% (11) | -639% | ❌ Worse |
| Momentum model | 3513 | 3.9% | 0.3% (11) | -681% | ❌ Worse |
| Mean-reversion model | 3513 | 6.9% | 0.3% (11) | -790% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3513 | 11 | -60% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 751 | 5 | -23% | -65% | -65% | -60% |
| Volatility model ≥ 5% | 380 | 2 | -31% | -43% | -44% | -39% |
| Volatility model ≥ 10% | 219 | 2 | +38% | -8% | -10% | -2% |
| Momentum model ≥ 2% | 662 | 4 | -27% | -64% | -67% | -63% |
| Momentum model ≥ 5% | 382 | 3 | +4% | -49% | -52% | -46% |
| Momentum model ≥ 10% | 255 | 2 | +15% | -29% | -30% | -24% |
| Mean-reversion model ≥ 2% | 1343 | 7 | -44% | -84% | -86% | -81% |
| Mean-reversion model ≥ 5% | 896 | 6 | -27% | -80% | -82% | -75% |
| Mean-reversion model ≥ 10% | 578 | 4 | -21% | -77% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3710 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1778 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6043 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 23 | 0% | -$411.35 | -56% | — |
| Sell at 2¢ | 240 | 4% | -$656.95 | -90% | 43 sec |
| Sell at 3¢ | 150 | 2% | -$660.85 | -90% | 48 sec |
| Sell at 5¢ | 111 | 2% | -$647.20 | -88% | 64 sec |
| Sell at 10¢ | 74 | 1% | -$608.41 | -83% | 81 sec |
| Sell at 25¢ | 39 | 1% | -$562.26 | -77% | 1.6 min |
| Sell at 50¢ | 21 | 0% | -$507.60 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 1973 | 12 | 8% | 3% | -41% | -86% | -87% |
| 1–2 min | 1570 | 6 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 2329 | 3 | 1% | 0% | -81% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 419 | 2 | 4% | 1% | -37% | -89% | -90% |
| ZEC | 415 | 2 | 6% | 3% | -42% | -88% | -90% |
| ETH | 414 | 2 | 6% | 3% | -40% | -85% | -85% |
| HYPE | 413 | 2 | 5% | 3% | -40% | -88% | -86% |
| BNB | 413 | 0 | 4% | 1% | -100% | -91% | -93% |
| BTC | 412 | 1 | 7% | 3% | -69% | -84% | -88% |
| XRP | 410 | 3 | 1% | 1% | -4% | -64% | -64% |
| SOL | 408 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 406 | 1 | 6% | 2% | -67% | -85% | -88% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 270 | 2 | 3% | 1% | -22% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 223 | 2 | 4% | 2% | -16% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3089 | 14 | 4% | 2% | -47% | -91% | -91% |
| DOWN (bought NO) | 2954 | 9 | 4% | 2% | -65% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 451 | 2 | 1% | 1% | -17% | -54% | -54% |
| 0.05–0.1% | 517 | 0 | 3% | 1% | -100% | -90% | -93% |
| 0.1–0.2% | 909 | 2 | 4% | 1% | -70% | -91% | -91% |
| 0.2–0.5% | 1253 | 5 | 6% | 3% | -55% | -87% | -87% |
| Over 0.5% | 578 | 4 | 7% | 3% | -28% | -86% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1640 | 9 | 5% | 3% | -38% | -90% | -88% |
| Afternoon (12–6pm) | 1279 | 3 | 4% | 1% | -72% | -83% | -85% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,122 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 5:28:49 PM | SOL | DOWN | 71 sec | +0.082% | — | In play | — |
| 10/2 5:28:39 PM | BTC | DOWN | 81 sec | +0.062% | — | In play | — |
| 10/2 5:28:11 PM | NEAR | DOWN | 1.8 min | +0.178% | — | In play | — |
| 10/2 5:28:04 PM | ETH | DOWN | 1.9 min | +0.045% | — | In play | — |
| 10/2 5:27:24 PM | HYPE | DOWN | 2.6 min | +0.407% | — | In play | — |
| 10/2 5:26:51 PM | DOGE | DOWN | 3.1 min | +0.236% | — | In play | — |
| 10/2 5:26:51 PM | BNB | DOWN | 3.1 min | +0.121% | — | In play | — |
| 10/2 5:26:49 PM | XRP | DOWN | 3.2 min | +0.223% | — | In play | — |
| 10/2 5:26:05 PM | ZEC | DOWN | 3.9 min | +0.494% | — | In play | — |
| 10/2 5:14:55 PM | ZEC | UP | 4 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:14:51 PM | XRP | DOWN | 8 sec | +0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:14:47 PM | BNB | DOWN | 12 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:14:35 PM | HYPE | DOWN | 24 sec | +0.133% | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:13:58 PM | NEAR | DOWN | 61 sec | +0.142% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:13:42 PM | ETH | UP | 77 sec | -0.099% | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:13:08 PM | BTC | UP | 1.9 min | -0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:12:30 PM | SOL | UP | 2.5 min | -0.206% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:59:44 PM | WTI | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:59:07 PM | NEAR | DOWN | 53 sec | +0.185% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:58:57 PM | BTC | DOWN | 62 sec | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:58:57 PM | DOGE | DOWN | 62 sec | +0.129% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:58:49 PM | XRP | DOWN | 70 sec | +0.101% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:58:37 PM | SOL | DOWN | 82 sec | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 4:58:23 PM | ETH | DOWN | 1.6 min | +0.055% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:56:58 PM | HYPE | DOWN | 3.0 min | +0.378% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:56:10 PM | ZEC | DOWN | 3.8 min | +0.637% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:44:35 PM | ETH | DOWN | 25 sec | +0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:44:29 PM | DOGE | DOWN | 31 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/2 4:44:08 PM | BNB | DOWN | 52 sec | +0.003% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 4:43:56 PM | XRP | DOWN | 63 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
