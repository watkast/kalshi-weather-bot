# Fair-Value Bot

*Updated Mon Sep 28, 6:12 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **4¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 268 | $213.26 | +17% | $147.76 / $65.50 |
| 4¢+ ← live bot | 260 | $269.88 | +23% | $183.16 / $86.72 |
| 6¢+ | 245 | $188.12 | +19% | $157.54 / $30.58 |
| 8¢+ | 222 | $140.06 | +17% | $141.73 / -$1.67 |
| 10¢+ | 200 | $133.08 | +18% | $149.08 / -$16.00 |
| 15¢+ | 126 | $110.25 | +26% | $127.31 / -$17.06 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 279 | 270 | 154 (57%) | 43¢ | 51% | $325.66 | +27% | +15.5¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+2.0%** over 7,353 readings from 279 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1343 | 2% | 4% | 9% |
| 10–20% | 532 | 15% | 16% | 17% |
| 20–30% | 562 | 25% | 26% | 30% |
| 30–40% | 632 | 35% | 36% | 45% |
| 40–50% | 674 | 45% | 48% | 53% |
| 50–60% | 694 | 55% | 59% | 56% |
| 60–70% | 728 | 65% | 70% | 67% |
| 70–80% | 673 | 75% | 79% | 80% |
| 80–90% | 537 | 85% | 87% | 87% |
| 90–100% | 978 | 97% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 174 | 94 (54%) | 45¢ | 52% | $124.19 | +15% |
| 6–10¢ | 78 | 50 (64%) | 40¢ | 49% | $174.46 | +54% |
| 10–20¢ | 16 | 8 (50%) | 38¢ | 52% | $17.14 | +27% |
| 20¢+ | 2 | 2 (100%) | 49¢ | 71% | $9.87 | +97% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 267 | 154 (58%) | 44¢ | 52% | $329.08 | +27% |
| 5–10 min | 3 | 0 (0%) | 11¢ | 17% | -$3.42 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 26 | 7 (27%) | 19¢ | 26% | $18.33 | +35% |
| Toss-up (25–75¢) | 240 | 144 (60%) | 45¢ | 53% | $308.65 | +27% |
| Favorite (75–95¢) | 4 | 3 (75%) | 77¢ | 83% | -$1.32 | -4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 30 | 18 (60%) | 40¢ | 48% | $55.88 | +45% |
| ZEC | 30 | 14 (47%) | 42¢ | 50% | $8.64 | +7% |
| XRP | 30 | 17 (57%) | 45¢ | 52% | $30.11 | +22% |
| NEAR | 30 | 19 (63%) | 47¢ | 54% | $45.23 | +31% |
| ETH | 30 | 15 (50%) | 43¢ | 51% | $15.27 | +11% |
| BNB | 30 | 18 (60%) | 41¢ | 50% | $51.43 | +40% |
| DOGE | 30 | 19 (63%) | 45¢ | 53% | $49.82 | +36% |
| HYPE | 30 | 14 (47%) | 42¢ | 50% | $10.44 | +8% |
| BTC | 30 | 20 (67%) | 45¢ | 53% | $58.84 | +42% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 6:02:06 AM | HYPE | DOWN | 12.9 min | 73¢ | 83% | 9¢ | Open | — |
| 9/28 6:01:17 AM | NEAR | DOWN | 13.7 min | 71¢ | 80% | 8¢ | Open | — |
| 9/28 6:01:17 AM | ETH | DOWN | 13.7 min | 74¢ | 80% | 4¢ | Open | — |
| 9/28 6:01:11 AM | BNB | DOWN | 13.8 min | 46¢ | 58% | 10¢ | Open | — |
| 9/28 6:01:05 AM | XRP | DOWN | 13.9 min | 69¢ | 81% | 11¢ | Open | — |
| 9/28 6:01:05 AM | BTC | DOWN | 13.9 min | 56¢ | 66% | 8¢ | Open | — |
| 9/28 6:01:05 AM | SOL | DOWN | 13.9 min | 58¢ | 66% | 6¢ | Open | — |
| 9/28 6:01:05 AM | DOGE | DOWN | 13.9 min | 68¢ | 77% | 8¢ | Open | — |
| 9/28 6:01:05 AM | ZEC | UP | 13.9 min | 77¢ | 90% | 12¢ | Open | — |
| 9/28 5:48:01 AM | ETH | DOWN | 12.0 min | 67¢ | 73% | 5¢ | ❌ Lost | -$6.86 |
| 9/28 5:47:43 AM | SOL | UP | 12.3 min | 28¢ | 34% | 5¢ | ✅ Won | $7.05 |
| 9/28 5:47:23 AM | HYPE | UP | 12.6 min | 16¢ | 21% | 4¢ | ❌ Lost | -$1.70 |
| 9/28 5:47:21 AM | DOGE | DOWN | 12.6 min | 65¢ | 74% | 7¢ | ✅ Won | $3.34 |
| 9/28 5:46:46 AM | ZEC | UP | 13.2 min | 28¢ | 35% | 6¢ | ✅ Won | $7.05 |
| 9/28 5:46:40 AM | NEAR | DOWN | 13.3 min | 48¢ | 55% | 6¢ | ❌ Lost | -$4.98 |
| 9/28 5:46:26 AM | BNB | DOWN | 13.6 min | 62¢ | 72% | 8¢ | ❌ Lost | -$6.37 |
| 9/28 5:46:26 AM | BTC | DOWN | 13.6 min | 62¢ | 68% | 4¢ | ❌ Lost | -$6.37 |
| 9/28 5:46:04 AM | XRP | DOWN | 13.9 min | 57¢ | 64% | 5¢ | ❌ Lost | -$5.88 |
| 9/28 5:34:04 AM | NEAR | DOWN | 10.9 min | 70¢ | 79% | 8¢ | ✅ Won | $2.85 |
| 9/28 5:32:37 AM | DOGE | DOWN | 12.4 min | 57¢ | 64% | 5¢ | ❌ Lost | -$5.88 |
| 9/28 5:31:52 AM | ZEC | DOWN | 13.1 min | 53¢ | 60% | 5¢ | ❌ Lost | -$5.48 |
| 9/28 5:31:32 AM | BNB | DOWN | 13.4 min | 51¢ | 61% | 8¢ | ❌ Lost | -$5.28 |
| 9/28 5:31:16 AM | XRP | UP | 13.7 min | 45¢ | 52% | 5¢ | ✅ Won | $5.32 |
| 9/28 5:31:16 AM | HYPE | UP | 13.7 min | 63¢ | 85% | 20¢ | ✅ Won | $3.53 |
| 9/28 5:31:16 AM | BTC | UP | 13.7 min | 43¢ | 52% | 7¢ | ✅ Won | $5.52 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
