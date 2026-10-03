# 15-Minute 1¢ Study

*Updated Sat Oct 3, 10:20 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 173 finished bets | 1% | $2.50 | +10% | +1.45¢ | $15.25 / -$12.75 |

*Expect about **31 buys a day** (~$4.66/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 445 | -$4.50 | -10% |
| Momentum model ≥ 5%, sell at 50¢ | 445 | -$11.75 | -25% |
| 5+ min left, sell at 50¢ | 173 | -$12.00 | -47% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6631 | 6625 | 28 (0%) | 1.07% | -$406.15 (-51%) | Hold to the close: -$406.15 (-51%) |

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
| Volatility model | 4089 | 4.1% | 0.4% (16) | -642% | ❌ Worse |
| Momentum model | 4089 | 4.1% | 0.4% (16) | -679% | ❌ Worse |
| Mean-reversion model | 4089 | 7.0% | 0.4% (16) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4089 | 16 | -50% | -83% | -83% | -80% |
| Volatility model ≥ 2% | 854 | 5 | -32% | -67% | -68% | -63% |
| Volatility model ≥ 5% | 446 | 2 | -41% | -49% | -51% | -47% |
| Volatility model ≥ 10% | 268 | 2 | +15% | -20% | -25% | -19% |
| Momentum model ≥ 2% | 746 | 4 | -35% | -66% | -70% | -67% |
| Momentum model ≥ 5% | 445 | 3 | -10% | -54% | -58% | -53% |
| Momentum model ≥ 10% | 302 | 2 | -2% | -37% | -40% | -35% |
| Mean-reversion model ≥ 2% | 1516 | 7 | -50% | -83% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1023 | 6 | -35% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 668 | 4 | -31% | -77% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4286 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6625 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 28 | 0% | -$406.15 | -51% | — |
| Sell at 2¢ | 265 | 4% | -$701.25 | -88% | 34 sec |
| Sell at 3¢ | 168 | 3% | -$704.63 | -88% | 48 sec |
| Sell at 5¢ | 126 | 2% | -$688.25 | -86% | 62 sec |
| Sell at 10¢ | 85 | 1% | -$644.80 | -81% | 81 sec |
| Sell at 25¢ | 46 | 1% | -$589.89 | -74% | 1.6 min |
| Sell at 50¢ | 26 | 0% | -$524.65 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 170 | 2 | 12% | 3% | +12% | -79% | -89% |
| 2–5 min | 2172 | 14 | 8% | 4% | -37% | -86% | -87% |
| 1–2 min | 1719 | 8 | 3% | 2% | -50% | -94% | -93% |
| Under 1 min | 2561 | 4 | 1% | 0% | -77% | -86% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 482 | 2 | 4% | 1% | -45% | -90% | -91% |
| ETH | 481 | 3 | 6% | 3% | -21% | -85% | -85% |
| ZEC | 481 | 3 | 5% | 3% | -26% | -89% | -90% |
| HYPE | 479 | 2 | 5% | 4% | -49% | -88% | -85% |
| BNB | 476 | 1 | 4% | 2% | -75% | -90% | -92% |
| XRP | 473 | 4 | 2% | 1% | +9% | -68% | -68% |
| BTC | 472 | 1 | 6% | 3% | -73% | -85% | -89% |
| SOL | 472 | 0 | 3% | 1% | -100% | -93% | -93% |
| NEAR | 470 | 2 | 6% | 3% | -43% | -55% | -58% |
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
| UP (bought YES) | 3352 | 16 | 4% | 2% | -44% | -88% | -87% |
| DOWN (bought NO) | 3273 | 12 | 4% | 2% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 604 | 4 | 2% | 1% | +21% | -34% | -35% |
| 0.05–0.1% | 669 | 0 | 3% | 1% | -100% | -91% | -93% |
| 0.1–0.2% | 1054 | 4 | 4% | 2% | -50% | -90% | -90% |
| 0.2–0.5% | 1360 | 6 | 6% | 3% | -51% | -88% | -87% |
| Over 0.5% | 597 | 4 | 7% | 3% | -31% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1789 | 12 | 5% | 3% | -23% | -90% | -88% |
| Afternoon (12–6pm) | 1305 | 3 | 4% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,444 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 10:14:34 AM | HYPE | UP | 25 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/3 10:14:02 AM | DOGE | UP | 57 sec | -0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:14:02 AM | BTC | UP | 57 sec | -0.036% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:13:46 AM | BNB | UP | 74 sec | -0.099% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:13:46 AM | XRP | UP | 74 sec | -0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:13:46 AM | SOL | UP | 74 sec | -0.099% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:13:14 AM | NEAR | UP | 1.8 min | -0.443% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:12:58 AM | ETH | UP | 2.0 min | -0.061% | 0¢ | ❌ Lost | $0.00 |
| 10/3 10:10:05 AM | ZEC | UP | 4.9 min | -0.405% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:59:47 AM | BNB | DOWN | 13 sec | +0.023% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 9:59:32 AM | DOGE | UP | 28 sec | -0.087% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:59:32 AM | BTC | DOWN | 28 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/3 9:59:32 AM | NEAR | DOWN | 28 sec | +0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/3 9:59:32 AM | HYPE | UP | 28 sec | -0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:59:16 AM | XRP | UP | 44 sec | -0.127% | 0¢ | ❌ Lost | $0.00 |
| 10/3 9:58:44 AM | ETH | DOWN | 76 sec | +0.029% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:58:44 AM | SOL | DOWN | 76 sec | +0.065% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:58:13 AM | ZEC | DOWN | 1.8 min | +0.257% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:44:15 AM | ETH | UP | 44 sec | -0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/3 9:44:15 AM | NEAR | DOWN | 44 sec | +0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 9:44:15 AM | SOL | DOWN | 44 sec | +0.059% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 9:43:59 AM | ZEC | DOWN | 60 sec | +0.186% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:43:59 AM | XRP | DOWN | 60 sec | +0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/3 9:43:45 AM | HYPE | DOWN | 74 sec | +0.114% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 9:43:29 AM | DOGE | UP | 1.5 min | -0.179% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 9:42:11 AM | BNB | DOWN | 2.8 min | +0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/3 9:29:37 AM | ETH | DOWN | 22 sec | +0.002% | 0¢ | ❌ Lost | $0.00 |
| 10/3 9:29:37 AM | BTC | DOWN | 22 sec | +0.010% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 9:29:21 AM | HYPE | DOWN | 38 sec | +0.051% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 9:29:05 AM | ZEC | UP | 54 sec | -0.221% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
