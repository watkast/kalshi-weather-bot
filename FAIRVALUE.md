# Fair-Value Bot

*Updated Mon Sep 28, 6:42 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **4¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 286 | $153.46 | +11% | $153.00 / $0.46 |
| 4¢+ ← live bot | 277 | $207.63 | +16% | $205.66 / $1.97 |
| 6¢+ | 262 | $132.07 | +12% | $154.54 / -$22.47 |
| 8¢+ | 239 | $78.30 | +9% | $134.35 / -$56.05 |
| 10¢+ | 216 | $100.53 | +13% | $163.32 / -$62.79 |
| 15¢+ | 138 | $104.35 | +22% | $151.08 / -$46.73 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 297 | 288 | 158 (55%) | 44¢ | 52% | $270.66 | +21% | +14.9¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+1.8%** over 7,839 readings from 297 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1357 | 2% | 4% | 9% |
| 10–20% | 558 | 15% | 16% | 20% |
| 20–30% | 598 | 25% | 26% | 33% |
| 30–40% | 674 | 35% | 36% | 46% |
| 40–50% | 716 | 45% | 48% | 54% |
| 50–60% | 737 | 55% | 59% | 58% |
| 60–70% | 770 | 65% | 70% | 68% |
| 70–80% | 695 | 75% | 79% | 81% |
| 80–90% | 561 | 85% | 87% | 87% |
| 90–100% | 1173 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 181 | 96 (53%) | 45¢ | 52% | $114.27 | +14% |
| 6–10¢ | 85 | 51 (60%) | 41¢ | 51% | $143.82 | +39% |
| 10–20¢ | 20 | 9 (45%) | 42¢ | 56% | $2.70 | +3% |
| 20¢+ | 2 | 2 (100%) | 49¢ | 71% | $9.87 | +97% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 285 | 158 (55%) | 44¢ | 52% | $274.08 | +21% |
| 5–10 min | 3 | 0 (0%) | 11¢ | 17% | -$3.42 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 26 | 7 (27%) | 19¢ | 26% | $18.33 | +35% |
| Toss-up (25–75¢) | 257 | 147 (57%) | 46¢ | 54% | $251.48 | +21% |
| Favorite (75–95¢) | 5 | 4 (80%) | 77¢ | 84% | $0.85 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 32 | 19 (59%) | 40¢ | 48% | $56.13 | +42% |
| ZEC | 32 | 15 (47%) | 43¢ | 51% | $7.25 | +5% |
| XRP | 32 | 18 (56%) | 46¢ | 53% | $28.38 | +19% |
| NEAR | 32 | 19 (59%) | 47¢ | 55% | $34.52 | +22% |
| ETH | 32 | 15 (47%) | 44¢ | 52% | $3.96 | +3% |
| BNB | 32 | 18 (56%) | 42¢ | 51% | $41.87 | +30% |
| DOGE | 32 | 19 (59%) | 45¢ | 53% | $39.30 | +26% |
| HYPE | 32 | 14 (44%) | 42¢ | 51% | -$0.15 | -0% |
| BTC | 32 | 21 (66%) | 45¢ | 53% | $59.40 | +39% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 6:33:50 AM | DOGE | UP | 11.2 min | 40¢ | 46% | 4¢ | Open | — |
| 9/28 6:33:05 AM | HYPE | UP | 11.9 min | 40¢ | 47% | 5¢ | Open | — |
| 9/28 6:33:00 AM | BTC | UP | 12.0 min | 32¢ | 38% | 5¢ | Open | — |
| 9/28 6:32:57 AM | NEAR | UP | 12.0 min | 31¢ | 37% | 5¢ | Open | — |
| 9/28 6:31:25 AM | SOL | UP | 13.6 min | 42¢ | 49% | 5¢ | Open | — |
| 9/28 6:31:19 AM | ZEC | UP | 13.7 min | 40¢ | 46% | 4¢ | Open | — |
| 9/28 6:31:11 AM | XRP | UP | 13.8 min | 38¢ | 49% | 9¢ | Open | — |
| 9/28 6:31:11 AM | BNB | DOWN | 13.8 min | 56¢ | 64% | 6¢ | Open | — |
| 9/28 6:31:09 AM | ETH | DOWN | 13.8 min | 55¢ | 61% | 4¢ | Open | — |
| 9/28 6:17:07 AM | DOGE | DOWN | 12.9 min | 34¢ | 40% | 5¢ | ❌ Lost | -$3.56 |
| 9/28 6:16:52 AM | BNB | DOWN | 13.1 min | 46¢ | 58% | 11¢ | ❌ Lost | -$4.78 |
| 9/28 6:16:46 AM | HYPE | UP | 13.2 min | 30¢ | 36% | 5¢ | ❌ Lost | -$3.15 |
| 9/28 6:16:38 AM | BTC | UP | 13.4 min | 35¢ | 42% | 6¢ | ✅ Won | $6.34 |
| 9/28 6:16:26 AM | ETH | UP | 13.6 min | 36¢ | 42% | 4¢ | ❌ Lost | -$3.77 |
| 9/28 6:16:22 AM | XRP | UP | 13.6 min | 45¢ | 52% | 5¢ | ✅ Won | $5.32 |
| 9/28 6:16:22 AM | ZEC | UP | 13.6 min | 34¢ | 41% | 6¢ | ❌ Lost | -$3.56 |
| 9/28 6:16:08 AM | NEAR | DOWN | 13.9 min | 33¢ | 44% | 9¢ | ❌ Lost | -$3.46 |
| 9/28 6:16:04 AM | SOL | UP | 13.9 min | 36¢ | 45% | 7¢ | ✅ Won | $6.23 |
| 9/28 6:02:06 AM | HYPE | DOWN | 12.9 min | 73¢ | 83% | 9¢ | ❌ Lost | -$7.44 |
| 9/28 6:01:17 AM | NEAR | DOWN | 13.7 min | 71¢ | 80% | 8¢ | ❌ Lost | -$7.25 |
| 9/28 6:01:17 AM | ETH | DOWN | 13.7 min | 74¢ | 80% | 4¢ | ❌ Lost | -$7.54 |
| 9/28 6:01:11 AM | BNB | DOWN | 13.8 min | 46¢ | 58% | 10¢ | ❌ Lost | -$4.78 |
| 9/28 6:01:05 AM | XRP | DOWN | 13.9 min | 69¢ | 81% | 11¢ | ❌ Lost | -$7.05 |
| 9/28 6:01:05 AM | BTC | DOWN | 13.9 min | 56¢ | 66% | 8¢ | ❌ Lost | -$5.78 |
| 9/28 6:01:05 AM | SOL | DOWN | 13.9 min | 58¢ | 66% | 6¢ | ❌ Lost | -$5.98 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
