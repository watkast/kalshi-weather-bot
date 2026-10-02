# 15-Minute 1¢ Study

*Updated Fri Oct 2, 1:55 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 171 finished bets | 1% | $2.80 | +11% | +1.64¢ | $15.40 / -$12.60 |

*Expect about **36 buys a day** (~$5.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 368 | $2.70 | +7% |
| Momentum model ≥ 5%, sell at 50¢ | 368 | -$4.55 | -12% |
| Volatility model ≥ 5%, sell at 25¢ | 363 | -$8.60 | -22% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5898 | 5892 | 22 (0%) | 1.07% | -$408.70 (-57%) | Hold to the close: -$408.70 (-57%) |

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
| Volatility model | 3394 | 3.7% | 0.3% (10) | -635% | ❌ Worse |
| Momentum model | 3394 | 3.8% | 0.3% (10) | -678% | ❌ Worse |
| Mean-reversion model | 3394 | 6.8% | 0.3% (10) | -798% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3394 | 10 | -62% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 723 | 5 | -20% | -65% | -65% | -61% |
| Volatility model ≥ 5% | 363 | 2 | -28% | -41% | -41% | -36% |
| Volatility model ≥ 10% | 209 | 2 | +44% | -4% | -6% | +2% |
| Momentum model ≥ 2% | 636 | 4 | -24% | -63% | -66% | -62% |
| Momentum model ≥ 5% | 368 | 3 | +7% | -48% | -51% | -46% |
| Momentum model ≥ 10% | 245 | 2 | +18% | -27% | -28% | -22% |
| Mean-reversion model ≥ 2% | 1304 | 7 | -42% | -84% | -86% | -81% |
| Mean-reversion model ≥ 5% | 868 | 6 | -25% | -80% | -82% | -76% |
| Mean-reversion model ≥ 10% | 558 | 4 | -18% | -76% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3590 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1754 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 548 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5892 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 22 | 0% | -$408.70 | -57% | — |
| Sell at 2¢ | 231 | 4% | -$642.64 | -90% | 45 sec |
| Sell at 3¢ | 144 | 2% | -$646.54 | -90% | 48 sec |
| Sell at 5¢ | 106 | 2% | -$633.80 | -88% | 64 sec |
| Sell at 10¢ | 73 | 1% | -$593.07 | -83% | 81 sec |
| Sell at 25¢ | 38 | 1% | -$548.92 | -77% | 1.6 min |
| Sell at 50¢ | 20 | 0% | -$497.70 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 1927 | 11 | 8% | 3% | -44% | -86% | -87% |
| 1–2 min | 1528 | 6 | 3% | 2% | -58% | -94% | -93% |
| Under 1 min | 2266 | 3 | 1% | 0% | -81% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 406 | 2 | 4% | 1% | -36% | -89% | -90% |
| ZEC | 401 | 2 | 5% | 3% | -40% | -88% | -90% |
| BNB | 401 | 0 | 4% | 1% | -100% | -91% | -93% |
| ETH | 400 | 2 | 6% | 3% | -38% | -86% | -84% |
| BTC | 399 | 0 | 7% | 3% | -100% | -84% | -88% |
| HYPE | 399 | 2 | 5% | 3% | -38% | -89% | -86% |
| XRP | 396 | 3 | 2% | 1% | -1% | -63% | -63% |
| NEAR | 394 | 1 | 6% | 2% | -66% | -85% | -88% |
| SOL | 394 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 300 | 0 | 5% | 1% | -100% | -89% | -92% |
| SILVER | 282 | 0 | 2% | 1% | -100% | -96% | -95% |
| WTI | 265 | 2 | 3% | 1% | -21% | -94% | -96% |
| COPPER | 252 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 222 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 220 | 2 | 4% | 2% | -15% | -94% | -92% |
| PALLADIUM | 213 | 1 | 2% | 1% | -56% | -96% | -98% |
| GBPUSD | 193 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 192 | 1 | 5% | 3% | -51% | -92% | -91% |
| USDJPY | 163 | 3 | 2% | 2% | +72% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3022 | 14 | 4% | 2% | -46% | -92% | -91% |
| DOWN (bought NO) | 2870 | 8 | 4% | 2% | -68% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 430 | 2 | 1% | 1% | -13% | -52% | -52% |
| 0.05–0.1% | 492 | 0 | 3% | 1% | -100% | -91% | -94% |
| 0.1–0.2% | 874 | 1 | 4% | 1% | -85% | -91% | -92% |
| 0.2–0.5% | 1226 | 5 | 6% | 3% | -54% | -87% | -87% |
| Over 0.5% | 567 | 4 | 7% | 3% | -27% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1640 | 9 | 5% | 3% | -38% | -90% | -88% |
| Afternoon (12–6pm) | 1128 | 2 | 3% | 1% | -79% | -83% | -85% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,087 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 1:44:33 PM | BTC | DOWN | 27 sec | +0.051% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:44:33 PM | ETH | UP | 27 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:44:17 PM | NEAR | UP | 43 sec | -0.297% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:44:17 PM | SOL | DOWN | 43 sec | +0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:44:17 PM | PALLADIUM | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:44:17 PM | NATGAS | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:43:45 PM | GOLD | UP | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:43:13 PM | XRP | DOWN | 1.8 min | +0.245% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:42:57 PM | SILVER | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:42:39 PM | ZEC | UP | 2.4 min | -0.300% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:42:39 PM | BNB | DOWN | 2.4 min | +0.084% | 7¢ | ❌ Lost | -$0.15 |
| 10/2 1:41:52 PM | HYPE | DOWN | 3.1 min | +0.421% | 4¢ | ❌ Lost | -$0.15 |
| 10/2 1:41:36 PM | WTI | DOWN | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:41:20 PM | DOGE | DOWN | 3.6 min | +0.440% | 1¢ | ❌ Lost | $0.00 |
| 10/2 1:29:56 PM | BTC | DOWN | 3 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:29:40 PM | PALLADIUM | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:40 PM | NATGAS | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:24 PM | SOL | DOWN | 36 sec | +0.011% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:24 PM | WTI | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:08 PM | PLATINUM | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:08 PM | GBPUSD | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:29:08 PM | ZEC | DOWN | 52 sec | +0.223% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:28:52 PM | SILVER | DOWN | 68 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 1:28:52 PM | ETH | DOWN | 68 sec | +0.128% | 8¢ | ❌ Lost | -$0.15 |
| 10/2 1:28:36 PM | XRP | DOWN | 84 sec | +0.225% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:28:04 PM | COPPER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:27:48 PM | EURUSD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:27:48 PM | NEAR | DOWN | 2.2 min | +0.538% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 1:27:48 PM | DOGE | DOWN | 2.2 min | +0.363% | 0¢ | ❌ Lost | $0.00 |
| 10/2 1:27:32 PM | BNB | DOWN | 2.5 min | +0.100% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
