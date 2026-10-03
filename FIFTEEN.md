# 15-Minute 1¢ Study

*Updated Sat Oct 3, 1:47 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 171 finished bets | 1% | $2.80 | +11% | +1.64¢ | $15.40 / -$12.60 |

*Expect about **33 buys a day** (~$4.92/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 412 | -$1.50 | -3% |
| Momentum model ≥ 5%, sell at 50¢ | 412 | -$8.75 | -20% |
| 5+ min left, sell at 50¢ | 171 | -$11.70 | -46% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6337 | 6331 | 23 (0%) | 1.07% | -$443.60 (-58%) | Hold to the close: -$443.60 (-58%) |

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
| Volatility model | 3795 | 4.0% | 0.3% (11) | -724% | ❌ Worse |
| Momentum model | 3795 | 4.1% | 0.3% (11) | -764% | ❌ Worse |
| Mean-reversion model | 3795 | 7.0% | 0.3% (11) | -884% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3795 | 11 | -63% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 800 | 5 | -28% | -66% | -67% | -62% |
| Volatility model ≥ 5% | 410 | 2 | -36% | -46% | -47% | -43% |
| Volatility model ≥ 10% | 244 | 2 | +25% | -14% | -18% | -11% |
| Momentum model ≥ 2% | 702 | 4 | -31% | -65% | -69% | -65% |
| Momentum model ≥ 5% | 412 | 3 | -3% | -51% | -55% | -50% |
| Momentum model ≥ 10% | 279 | 2 | +5% | -33% | -36% | -30% |
| Mean-reversion model ≥ 2% | 1428 | 7 | -47% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 955 | 6 | -31% | -80% | -82% | -75% |
| Mean-reversion model ≥ 10% | 622 | 4 | -26% | -77% | -81% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3992 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6331 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 23 | 0% | -$443.60 | -58% | — |
| Sell at 2¢ | 250 | 4% | -$686.60 | -90% | 43 sec |
| Sell at 3¢ | 156 | 2% | -$690.76 | -90% | 48 sec |
| Sell at 5¢ | 116 | 2% | -$676.20 | -88% | 64 sec |
| Sell at 10¢ | 77 | 1% | -$636.73 | -83% | 81 sec |
| Sell at 25¢ | 41 | 1% | -$587.89 | -77% | 1.6 min |
| Sell at 50¢ | 21 | 0% | -$539.85 | -71% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 2068 | 12 | 8% | 3% | -43% | -86% | -87% |
| 1–2 min | 1643 | 6 | 3% | 2% | -61% | -94% | -93% |
| Under 1 min | 2449 | 3 | 1% | 0% | -82% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 450 | 2 | 4% | 1% | -41% | -90% | -91% |
| ZEC | 447 | 2 | 5% | 3% | -47% | -89% | -90% |
| ETH | 446 | 2 | 6% | 3% | -44% | -85% | -85% |
| HYPE | 446 | 2 | 5% | 4% | -45% | -88% | -85% |
| BTC | 442 | 1 | 6% | 3% | -71% | -85% | -89% |
| BNB | 442 | 0 | 4% | 2% | -100% | -90% | -92% |
| SOL | 441 | 0 | 3% | 1% | -100% | -93% | -92% |
| XRP | 440 | 3 | 2% | 1% | -11% | -67% | -67% |
| NEAR | 438 | 1 | 6% | 2% | -69% | -85% | -87% |
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
| UP (bought YES) | 3226 | 14 | 4% | 2% | -49% | -91% | -91% |
| DOWN (bought NO) | 3105 | 9 | 4% | 2% | -67% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 521 | 2 | 1% | 1% | -28% | -60% | -59% |
| 0.05–0.1% | 595 | 0 | 3% | 1% | -100% | -91% | -94% |
| 0.1–0.2% | 978 | 2 | 4% | 2% | -73% | -90% | -91% |
| 0.2–0.5% | 1305 | 5 | 6% | 3% | -57% | -87% | -87% |
| Over 0.5% | 591 | 4 | 7% | 3% | -30% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1528 | 5 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 1640 | 9 | 5% | 3% | -38% | -90% | -88% |
| Afternoon (12–6pm) | 1305 | 3 | 4% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,278 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 1:44:39 AM | ETH | DOWN | 21 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:44:23 AM | BTC | UP | 37 sec | -0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:43:51 AM | SOL | UP | 68 sec | -0.093% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 1:43:19 AM | ZEC | UP | 1.7 min | -0.149% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:42:48 AM | NEAR | UP | 2.2 min | -0.402% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:42:32 AM | BNB | UP | 2.5 min | -0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:42:16 AM | DOGE | UP | 2.7 min | -0.205% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:42:16 AM | XRP | UP | 2.7 min | -0.236% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:29:44 AM | BTC | DOWN | 16 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:29:28 AM | ETH | UP | 32 sec | -0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:29:28 AM | BNB | DOWN | 32 sec | -0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 1:29:28 AM | ZEC | DOWN | 32 sec | +0.055% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 1:29:12 AM | XRP | UP | 48 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:27:17 AM | NEAR | UP | 2.7 min | -0.411% | 10¢ | ❌ Lost | -$0.15 |
| 10/3 1:27:02 AM | HYPE | UP | 3.0 min | -0.249% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:26:47 AM | DOGE | UP | 3.2 min | -0.240% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:26:47 AM | SOL | UP | 3.2 min | -0.218% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:14:29 AM | ETH | DOWN | 31 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:14:13 AM | SOL | DOWN | 47 sec | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 10/3 1:13:58 AM | BTC | DOWN | 61 sec | +0.048% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 1:13:58 AM | XRP | UP | 61 sec | -0.094% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:12:54 AM | HYPE | DOWN | 2.1 min | +0.199% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 1:11:51 AM | NEAR | UP | 3.1 min | -0.333% | 4¢ | ❌ Lost | -$0.15 |
| 10/3 1:11:20 AM | ZEC | UP | 3.7 min | -0.306% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 1:11:04 AM | BNB | UP | 3.9 min | -0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 12:59:42 AM | XRP | UP | 17 sec | -0.013% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 12:59:26 AM | DOGE | UP | 33 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/3 12:59:26 AM | BNB | DOWN | 33 sec | -0.006% | 2¢ | ❌ Lost | $0.00 |
| 10/3 12:59:10 AM | ZEC | DOWN | 49 sec | +0.173% | 0¢ | ❌ Lost | $0.00 |
| 10/3 12:58:54 AM | ETH | DOWN | 66 sec | +0.035% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
