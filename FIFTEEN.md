# 15-Minute 1¢ Study

*Updated Fri Oct 2, 2:36 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 171 finished bets | 1% | $2.80 | +11% | +1.64¢ | $15.40 / -$12.60 |

*Expect about **36 buys a day** (~$5.40/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 373 | $2.40 | +6% |
| Momentum model ≥ 5%, sell at 50¢ | 373 | -$4.85 | -12% |
| Volatility model ≥ 5%, sell at 25¢ | 367 | -$8.90 | -23% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5942 | 5936 | 23 (0%) | 1.07% | -$399.50 (-55%) | Hold to the close: -$399.50 (-55%) |

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
| Volatility model | 3422 | 3.8% | 0.3% (11) | -622% | ❌ Worse |
| Momentum model | 3422 | 3.9% | 0.3% (11) | -662% | ❌ Worse |
| Mean-reversion model | 3422 | 6.9% | 0.3% (11) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3422 | 11 | -59% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 731 | 5 | -21% | -65% | -65% | -61% |
| Volatility model ≥ 5% | 367 | 2 | -29% | -41% | -42% | -37% |
| Volatility model ≥ 10% | 212 | 2 | +42% | -5% | -7% | +1% |
| Momentum model ≥ 2% | 644 | 4 | -25% | -63% | -66% | -62% |
| Momentum model ≥ 5% | 373 | 3 | +6% | -48% | -51% | -45% |
| Momentum model ≥ 10% | 249 | 2 | +17% | -28% | -29% | -23% |
| Mean-reversion model ≥ 2% | 1312 | 7 | -42% | -84% | -86% | -81% |
| Mean-reversion model ≥ 5% | 872 | 6 | -25% | -80% | -82% | -76% |
| Mean-reversion model ≥ 10% | 561 | 4 | -18% | -77% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3618 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1767 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 551 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5936 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 23 | 0% | -$399.50 | -55% | — |
| Sell at 2¢ | 235 | 4% | -$646.40 | -90% | 43 sec |
| Sell at 3¢ | 147 | 2% | -$650.17 | -90% | 48 sec |
| Sell at 5¢ | 108 | 2% | -$637.30 | -88% | 64 sec |
| Sell at 10¢ | 74 | 1% | -$596.56 | -83% | 81 sec |
| Sell at 25¢ | 39 | 1% | -$550.41 | -76% | 1.6 min |
| Sell at 50¢ | 21 | 0% | -$495.75 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 1934 | 12 | 8% | 3% | -39% | -86% | -87% |
| 1–2 min | 1539 | 6 | 3% | 2% | -58% | -94% | -93% |
| Under 1 min | 2292 | 3 | 1% | 0% | -81% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 409 | 2 | 4% | 1% | -36% | -89% | -90% |
| ZEC | 404 | 2 | 5% | 3% | -41% | -88% | -90% |
| BNB | 404 | 0 | 4% | 1% | -100% | -91% | -93% |
| BTC | 403 | 1 | 7% | 3% | -68% | -83% | -87% |
| ETH | 403 | 2 | 6% | 3% | -39% | -86% | -85% |
| HYPE | 402 | 2 | 5% | 3% | -38% | -88% | -85% |
| XRP | 399 | 3 | 2% | 1% | -1% | -63% | -63% |
| NEAR | 397 | 1 | 6% | 2% | -66% | -85% | -88% |
| SOL | 397 | 0 | 3% | 1% | -100% | -92% | -91% |
| GOLD | 302 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 284 | 0 | 2% | 1% | -100% | -96% | -95% |
| WTI | 266 | 2 | 3% | 1% | -21% | -94% | -96% |
| COPPER | 253 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 225 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 222 | 2 | 4% | 2% | -16% | -94% | -92% |
| PALLADIUM | 215 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 194 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 193 | 1 | 5% | 3% | -52% | -92% | -91% |
| USDJPY | 164 | 3 | 2% | 2% | +71% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3043 | 14 | 4% | 2% | -47% | -91% | -91% |
| DOWN (bought NO) | 2893 | 9 | 4% | 2% | -64% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 436 | 2 | 1% | 1% | -14% | -53% | -52% |
| 0.05–0.1% | 500 | 0 | 3% | 1% | -100% | -90% | -93% |
| 0.1–0.2% | 881 | 2 | 4% | 1% | -70% | -91% | -91% |
| 0.2–0.5% | 1230 | 5 | 6% | 3% | -54% | -87% | -87% |
| Over 0.5% | 570 | 4 | 7% | 3% | -27% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1640 | 9 | 5% | 3% | -38% | -90% | -88% |
| Afternoon (12–6pm) | 1172 | 3 | 3% | 1% | -70% | -83% | -85% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,080 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 2:29:47 PM | BNB | DOWN | 13 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:29:47 PM | BTC | UP | 13 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:29:47 PM | DOGE | DOWN | 13 sec | +0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:29:47 PM | ZEC | UP | 13 sec | +0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:29:47 PM | SOL | UP | 13 sec | -0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:29:31 PM | XRP | DOWN | 29 sec | +0.054% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:29:15 PM | NEAR | DOWN | 45 sec | +0.229% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:29:15 PM | ETH | UP | 45 sec | -0.081% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:29:15 PM | PLATINUM | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:29:00 PM | HYPE | UP | 59 sec | -0.256% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:26:32 PM | BTC | DOWN | 3.5 min | +0.183% | 100¢ | ✅ Won | $13.85 |
| 10/2 2:14:50 PM | ETH | DOWN | 10 sec | +0.004% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:14:50 PM | USDJPY | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:14:34 PM | GBPUSD | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:14:34 PM | DOGE | DOWN | 26 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:14:34 PM | NATGAS | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:14:18 PM | EURUSD | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:14:18 PM | WTI | UP | 42 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:14:18 PM | BNB | UP | 42 sec | -0.090% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:14:03 PM | HYPE | DOWN | 56 sec | +0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:13:47 PM | PALLADIUM | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:13:31 PM | PLATINUM | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:13:31 PM | NEAR | DOWN | 88 sec | +0.319% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:13:31 PM | SOL | DOWN | 88 sec | +0.152% | 5¢ | ❌ Lost | -$0.15 |
| 10/2 2:13:31 PM | GOLD | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:13:15 PM | SILVER | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:12:27 PM | BTC | DOWN | 2.5 min | +0.137% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:11:55 PM | XRP | DOWN | 3.1 min | +0.320% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:11:23 PM | ZEC | DOWN | 3.6 min | +0.926% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:59:51 PM | COPPER | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
