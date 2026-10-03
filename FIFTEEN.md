# 15-Minute 1¢ Study

*Updated Sat Oct 3, 7:18 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 172 finished bets | 1% | $2.65 | +10% | +1.54¢ | $15.25 / -$12.60 |

*Expect about **32 buys a day** (~$4.74/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 436 | -$3.90 | -8% |
| Momentum model ≥ 5%, sell at 50¢ | 436 | -$11.15 | -24% |
| 5+ min left, sell at 50¢ | 172 | -$11.85 | -47% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6528 | 6522 | 26 (0%) | 1.07% | -$422.00 (-54%) | Hold to the close: -$422.00 (-54%) |

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
| Volatility model | 3986 | 4.1% | 0.4% (14) | -693% | ❌ Worse |
| Momentum model | 3986 | 4.2% | 0.4% (14) | -728% | ❌ Worse |
| Mean-reversion model | 3986 | 7.1% | 0.4% (14) | -834% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3986 | 14 | -55% | -82% | -83% | -80% |
| Volatility model ≥ 2% | 840 | 5 | -31% | -67% | -67% | -63% |
| Volatility model ≥ 5% | 439 | 2 | -40% | -49% | -50% | -47% |
| Volatility model ≥ 10% | 264 | 2 | +15% | -20% | -25% | -19% |
| Momentum model ≥ 2% | 735 | 4 | -34% | -66% | -70% | -67% |
| Momentum model ≥ 5% | 436 | 3 | -8% | -53% | -58% | -53% |
| Momentum model ≥ 10% | 297 | 2 | -1% | -36% | -40% | -35% |
| Mean-reversion model ≥ 2% | 1488 | 7 | -49% | -83% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1005 | 6 | -34% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 657 | 4 | -30% | -77% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4183 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6522 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 26 | 0% | -$422.00 | -54% | — |
| Sell at 2¢ | 260 | 4% | -$690.40 | -88% | 38 sec |
| Sell at 3¢ | 165 | 3% | -$693.65 | -88% | 48 sec |
| Sell at 5¢ | 123 | 2% | -$678.05 | -86% | 61 sec |
| Sell at 10¢ | 82 | 1% | -$636.58 | -81% | 81 sec |
| Sell at 25¢ | 44 | 1% | -$584.36 | -74% | 1.6 min |
| Sell at 50¢ | 24 | 0% | -$526.00 | -67% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 169 | 2 | 12% | 3% | +12% | -79% | -89% |
| 2–5 min | 2129 | 13 | 8% | 4% | -40% | -86% | -87% |
| 1–2 min | 1694 | 7 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 2527 | 4 | 1% | 0% | -76% | -86% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 471 | 2 | 4% | 1% | -44% | -90% | -91% |
| ETH | 469 | 3 | 6% | 3% | -19% | -85% | -85% |
| ZEC | 469 | 2 | 5% | 3% | -49% | -89% | -91% |
| HYPE | 468 | 2 | 5% | 4% | -48% | -88% | -85% |
| BNB | 464 | 1 | 4% | 2% | -74% | -90% | -92% |
| SOL | 462 | 0 | 3% | 1% | -100% | -93% | -93% |
| BTC | 461 | 1 | 6% | 3% | -72% | -85% | -88% |
| XRP | 460 | 3 | 2% | 1% | -16% | -68% | -68% |
| NEAR | 459 | 2 | 6% | 3% | -41% | -55% | -57% |
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
| UP (bought YES) | 3305 | 16 | 4% | 2% | -43% | -88% | -87% |
| DOWN (bought NO) | 3217 | 10 | 4% | 2% | -64% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 585 | 4 | 2% | 1% | +26% | -32% | -32% |
| 0.05–0.1% | 642 | 0 | 3% | 1% | -100% | -91% | -93% |
| 0.1–0.2% | 1021 | 3 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 1339 | 5 | 6% | 3% | -58% | -88% | -87% |
| Over 0.5% | 594 | 4 | 7% | 3% | -30% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1686 | 10 | 5% | 3% | -32% | -90% | -88% |
| Afternoon (12–6pm) | 1305 | 3 | 4% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,382 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 7:14:42 AM | SOL | DOWN | 18 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/3 7:14:42 AM | ZEC | UP | 18 sec | -0.126% | 0¢ | ❌ Lost | $0.00 |
| 10/3 7:14:42 AM | NEAR | UP | 18 sec | -0.302% | 0¢ | ❌ Lost | $0.00 |
| 10/3 7:13:39 AM | XRP | UP | 81 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/3 7:13:39 AM | BTC | UP | 81 sec | -0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:13:23 AM | DOGE | UP | 1.6 min | -0.189% | 0¢ | ❌ Lost | $0.00 |
| 10/3 7:13:07 AM | ETH | UP | 1.9 min | -0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:11:48 AM | HYPE | DOWN | 3.2 min | +0.434% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:11:16 AM | BNB | DOWN | 3.7 min | +0.083% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 6:58:11 AM | DOGE | DOWN | 1.8 min | +0.078% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 6:57:24 AM | ETH | DOWN | 2.6 min | +0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 6:57:08 AM | XRP | DOWN | 2.9 min | +0.216% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 6:57:08 AM | ZEC | DOWN | 2.9 min | +0.404% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 6:57:08 AM | BTC | DOWN | 2.9 min | +0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 6:56:37 AM | SOL | DOWN | 3.4 min | +0.211% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 6:55:49 AM | NEAR | DOWN | 4.2 min | +0.564% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 6:55:34 AM | HYPE | DOWN | 4.4 min | +0.307% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 6:54:47 AM | BNB | DOWN | 5.2 min | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 6:44:33 AM | NEAR | UP | 27 sec | -0.239% | 0¢ | ❌ Lost | $0.00 |
| 10/3 6:44:33 AM | BNB | DOWN | 27 sec | -0.009% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 6:44:17 AM | BTC | UP | 43 sec | -0.055% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 6:43:27 AM | HYPE | UP | 1.5 min | -0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 6:43:27 AM | ETH | UP | 1.5 min | -0.097% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 6:43:11 AM | DOGE | UP | 1.8 min | -0.196% | 0¢ | ❌ Lost | $0.00 |
| 10/3 6:43:11 AM | SOL | UP | 1.8 min | -0.185% | 0¢ | ❌ Lost | $0.00 |
| 10/3 6:42:57 AM | XRP | UP | 2.0 min | -0.189% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 6:42:41 AM | ZEC | UP | 2.3 min | -0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 6:29:50 AM | ETH | UP | 9 sec | -0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 6:29:50 AM | BNB | UP | 9 sec | -0.078% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 6:29:35 AM | HYPE | UP | 24 sec | -0.104% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
