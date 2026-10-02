# 15-Minute 1¢ Study

*Updated Fri Oct 2, 1:25 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 358 finished bets | 1% | $3.75 | +10% | +1.05¢ | -$6.10 / $9.85 |

*Expect about **79 buys a day** (~$11.85/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 171 | $2.80 | +11% |
| Momentum model ≥ 5%, sell at 50¢ | 358 | -$3.50 | -9% |
| Volatility model ≥ 5%, sell at 25¢ | 351 | -$7.40 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5867 | 5861 | 22 (0%) | 1.07% | -$404.95 (-57%) | Hold to the close: -$404.95 (-57%) |

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
| Volatility model | 3376 | 3.7% | 0.3% (10) | -623% | ❌ Worse |
| Momentum model | 3376 | 3.8% | 0.3% (10) | -669% | ❌ Worse |
| Mean-reversion model | 3376 | 6.8% | 0.3% (10) | -784% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3376 | 10 | -62% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 709 | 5 | -19% | -65% | -66% | -62% |
| Volatility model ≥ 5% | 351 | 2 | -26% | -41% | -42% | -37% |
| Volatility model ≥ 10% | 200 | 2 | +51% | -1% | -4% | +3% |
| Momentum model ≥ 2% | 623 | 4 | -23% | -64% | -67% | -64% |
| Momentum model ≥ 5% | 358 | 3 | +10% | -47% | -51% | -46% |
| Momentum model ≥ 10% | 240 | 2 | +21% | -26% | -28% | -23% |
| Mean-reversion model ≥ 2% | 1290 | 7 | -41% | -84% | -86% | -82% |
| Mean-reversion model ≥ 5% | 855 | 6 | -24% | -80% | -82% | -76% |
| Mean-reversion model ≥ 10% | 546 | 4 | -17% | -77% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3572 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1743 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 546 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5861 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 22 | 0% | -$404.95 | -57% | — |
| Sell at 2¢ | 228 | 4% | -$639.67 | -90% | 46 sec |
| Sell at 3¢ | 141 | 2% | -$643.96 | -90% | 48 sec |
| Sell at 5¢ | 104 | 2% | -$631.35 | -89% | 64 sec |
| Sell at 10¢ | 73 | 1% | -$589.32 | -83% | 81 sec |
| Sell at 25¢ | 38 | 1% | -$545.17 | -76% | 1.6 min |
| Sell at 50¢ | 20 | 0% | -$493.95 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 1916 | 11 | 7% | 3% | -44% | -86% | -88% |
| 1–2 min | 1522 | 6 | 3% | 2% | -57% | -94% | -93% |
| Under 1 min | 2252 | 3 | 1% | 0% | -81% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 404 | 2 | 4% | 1% | -36% | -89% | -90% |
| ZEC | 399 | 2 | 6% | 3% | -40% | -88% | -90% |
| BNB | 399 | 0 | 4% | 1% | -100% | -92% | -94% |
| ETH | 398 | 2 | 6% | 3% | -38% | -87% | -85% |
| BTC | 397 | 0 | 7% | 3% | -100% | -84% | -88% |
| HYPE | 397 | 2 | 5% | 3% | -38% | -89% | -87% |
| XRP | 394 | 3 | 2% | 1% | -0% | -63% | -63% |
| NEAR | 392 | 1 | 6% | 2% | -66% | -85% | -88% |
| SOL | 392 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 299 | 0 | 5% | 1% | -100% | -89% | -92% |
| SILVER | 280 | 0 | 2% | 1% | -100% | -96% | -95% |
| WTI | 263 | 2 | 3% | 1% | -20% | -94% | -96% |
| COPPER | 251 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 221 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 218 | 2 | 4% | 2% | -14% | -94% | -92% |
| PALLADIUM | 211 | 1 | 2% | 1% | -56% | -96% | -98% |
| GBPUSD | 192 | 1 | 4% | 2% | -51% | -93% | -93% |
| EURUSD | 191 | 1 | 5% | 3% | -51% | -92% | -90% |
| USDJPY | 163 | 3 | 2% | 2% | +72% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3016 | 14 | 4% | 2% | -46% | -92% | -91% |
| DOWN (bought NO) | 2845 | 8 | 4% | 1% | -68% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 426 | 2 | 1% | 1% | -12% | -52% | -51% |
| 0.05–0.1% | 489 | 0 | 3% | 0% | -100% | -92% | -95% |
| 0.1–0.2% | 873 | 1 | 3% | 1% | -85% | -91% | -92% |
| 0.2–0.5% | 1218 | 5 | 6% | 3% | -54% | -87% | -87% |
| Over 0.5% | 565 | 4 | 7% | 3% | -27% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1640 | 9 | 5% | 3% | -38% | -90% | -88% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
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
| 10/2 11:56:08 AM | HYPE | DOWN | 3.9 min | +0.356% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:44:51 AM | BNB | DOWN | 9 sec | +0.034% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 11:44:19 AM | GOLD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 11:44:19 AM | NATGAS | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 11:44:04 AM | WTI | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 11:43:48 AM | PLATINUM | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 11:43:48 AM | SILVER | DOWN | 71 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:43:32 AM | ZEC | DOWN | 87 sec | +0.303% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:43:32 AM | BTC | UP | 87 sec | -0.149% | 2¢ | ❌ Lost | -$0.15 |
| 10/2 11:43:16 AM | EURUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 11:43:16 AM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 11:43:16 AM | ETH | UP | 1.7 min | -0.161% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:42:44 AM | SOL | UP | 2.2 min | -0.311% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:42:44 AM | XRP | UP | 2.2 min | -0.234% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:42:28 AM | GBPUSD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 11:41:35 AM | DOGE | UP | 3.4 min | -0.363% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:40:50 AM | HYPE | UP | 4.2 min | -0.414% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:40:18 AM | USDJPY | UP | 4.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:40:18 AM | NEAR | UP | 4.7 min | -1.017% | 1¢ | ❌ Lost | $0.00 |
| 10/2 11:29:53 AM | NEAR | DOWN | 7 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/2 11:29:53 AM | SILVER | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 11:29:53 AM | ETH | UP | 7 sec | +0.024% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:29:37 AM | PALLADIUM | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 11:29:37 AM | GOLD | UP | 23 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:29:37 AM | XRP | UP | 23 sec | -0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:29:21 AM | DOGE | UP | 39 sec | -0.133% | 0¢ | ❌ Lost | $0.00 |
| 10/2 11:29:21 AM | SOL | UP | 39 sec | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 11:29:21 AM | NATGAS | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 11:29:04 AM | WTI | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 11:28:48 AM | USDJPY | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
