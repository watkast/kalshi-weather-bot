# 15-Minute 1¢ Study

*Updated Sun Oct 4, 6:04 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 559 finished bets | 1% | $23.70 | +39% | +4.24¢ | -$16.75 / $40.45 |

*Expect about **83 buys a day** (~$12.47/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1033 | $15.50 | +12% |
| 5+ min left, hold to the close | 191 | $13.80 | +49% |
| Momentum model ≥ 5%, hold to the close | 562 | $10.15 | +17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7755 | 7749 | 35 (0%) | 1.07% | -$437.60 (-47%) | Hold to the close: -$437.60 (-47%) |

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
| Volatility model | 5175 | 4.2% | 0.4% (23) | -618% | ❌ Worse |
| Momentum model | 5175 | 4.3% | 0.4% (23) | -649% | ❌ Worse |
| Mean-reversion model | 5175 | 6.9% | 0.4% (23) | -718% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5175 | 23 | -44% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1033 | 10 | +12% | -68% | -68% | -63% |
| Volatility model ≥ 5% | 559 | 6 | +39% | -54% | -53% | -49% |
| Volatility model ≥ 10% | 349 | 4 | +69% | -35% | -37% | -30% |
| Momentum model ≥ 2% | 909 | 7 | -7% | -69% | -71% | -68% |
| Momentum model ≥ 5% | 562 | 5 | +17% | -60% | -63% | -59% |
| Momentum model ≥ 10% | 390 | 4 | +47% | -47% | -48% | -44% |
| Mean-reversion model ≥ 2% | 1824 | 13 | -22% | -82% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1226 | 11 | -0% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 809 | 8 | +15% | -77% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5372 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 1813 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 564 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7749 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 35 | 0% | -$437.60 | -47% | — |
| Sell at 2¢ | 314 | 4% | -$817.96 | -88% | 34 sec |
| Sell at 3¢ | 202 | 3% | -$820.82 | -88% | 48 sec |
| Sell at 5¢ | 148 | 2% | -$803.40 | -87% | 61 sec |
| Sell at 10¢ | 102 | 1% | -$751.98 | -81% | 78 sec |
| Sell at 25¢ | 57 | 1% | -$682.93 | -74% | 1.6 min |
| Sell at 50¢ | 35 | 0% | -$593.35 | -64% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 188 | 3 | 12% | 3% | +51% | -78% | -87% |
| 2–5 min | 2496 | 19 | 8% | 4% | -26% | -86% | -86% |
| 1–2 min | 2038 | 8 | 3% | 2% | -57% | -93% | -93% |
| Under 1 min | 3024 | 5 | 1% | 0% | -75% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 606 | 5 | 5% | 3% | -2% | -88% | -89% |
| DOGE | 602 | 2 | 4% | 1% | -57% | -90% | -90% |
| HYPE | 600 | 2 | 5% | 3% | -59% | -88% | -86% |
| ETH | 599 | 5 | 6% | 3% | +5% | -86% | -85% |
| SOL | 595 | 0 | 3% | 1% | -100% | -93% | -91% |
| BNB | 595 | 2 | 4% | 2% | -60% | -90% | -92% |
| BTC | 593 | 3 | 6% | 2% | -33% | -86% | -90% |
| XRP | 592 | 4 | 2% | 1% | -14% | -74% | -75% |
| NEAR | 590 | 2 | 6% | 3% | -55% | -62% | -64% |
| GOLD | 307 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 291 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 280 | 2 | 3% | 1% | -25% | -94% | -96% |
| COPPER | 257 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 229 | 2 | 3% | 2% | -18% | -94% | -92% |
| PLATINUM | 229 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 220 | 1 | 2% | 1% | -58% | -96% | -98% |
| EURUSD | 199 | 1 | 5% | 3% | -53% | -91% | -90% |
| GBPUSD | 197 | 1 | 4% | 2% | -53% | -93% | -93% |
| USDJPY | 168 | 3 | 2% | 2% | +67% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3901 | 19 | 4% | 2% | -43% | -88% | -87% |
| DOWN (bought NO) | 3848 | 16 | 4% | 2% | -52% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 908 | 7 | 2% | 1% | +30% | -57% | -56% |
| 0.05–0.1% | 920 | 2 | 3% | 1% | -68% | -90% | -92% |
| 0.1–0.2% | 1324 | 4 | 4% | 2% | -61% | -90% | -91% |
| 0.2–0.5% | 1558 | 8 | 6% | 4% | -43% | -87% | -86% |
| Over 0.5% | 660 | 4 | 7% | 3% | -38% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,128 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 5:59:58 PM | BTC | DOWN | 1 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:59:26 PM | HYPE | DOWN | 33 sec | +0.077% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:59:10 PM | NATGAS | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:59:08 PM | WTI | UP | 51 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:59:03 PM | PALLADIUM | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:58:46 PM | COPPER | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:58:10 PM | XRP | UP | 1.8 min | -0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:57:51 PM | NEAR | DOWN | 2.1 min | +0.181% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:57:41 PM | SILVER | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:44:47 PM | SILVER | UP | 12 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:44:41 PM | GOLD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:44:33 PM | PLATINUM | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:44:25 PM | EURUSD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:44:19 PM | WTI | UP | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:43:55 PM | XRP | UP | 65 sec | -0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:43:41 PM | USDJPY | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:42:48 PM | ZEC | UP | 2.2 min | -0.245% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:42:18 PM | NEAR | UP | 2.7 min | -0.774% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:42:10 PM | ETH | UP | 2.8 min | -0.265% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:42:10 PM | SOL | UP | 2.8 min | -0.305% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:42:08 PM | HYPE | UP | 2.9 min | -0.201% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:41:58 PM | BNB | UP | 3.0 min | -0.195% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:41:58 PM | BTC | UP | 3.0 min | -0.296% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 5:41:08 PM | DOGE | UP | 3.9 min | -0.468% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:29:45 PM | HYPE | DOWN | 14 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:29:39 PM | ETH | UP | 20 sec | -0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 5:29:33 PM | DOGE | UP | 26 sec | -0.168% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:29:29 PM | ZEC | UP | 30 sec | -0.170% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:29:25 PM | SOL | UP | 34 sec | -0.119% | 0¢ | ❌ Lost | $0.00 |
| 10/4 5:29:19 PM | PLATINUM | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
