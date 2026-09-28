# Fair-Value Bot

*Updated Mon Sep 28, 5:52 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **4¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 259 | $215.16 | +18% | $137.05 / $78.11 |
| 4¢+ ← live bot | 252 | $271.42 | +24% | $184.77 / $86.65 |
| 6¢+ | 238 | $199.72 | +21% | $153.76 / $45.96 |
| 8¢+ | 215 | $122.81 | +16% | $138.47 / -$15.66 |
| 10¢+ | 193 | $107.21 | +15% | $155.19 / -$47.98 |
| 15¢+ | 120 | $99.18 | +25% | $125.39 / -$26.21 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 270 | 261 | 151 (58%) | 43¢ | 51% | $340.38 | +29% | +15.9¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+2.4%** over 7,110 readings from 270 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1262 | 2% | 4% | 7% |
| 10–20% | 485 | 15% | 16% | 11% |
| 20–30% | 521 | 25% | 26% | 26% |
| 30–40% | 606 | 35% | 36% | 43% |
| 40–50% | 660 | 45% | 48% | 52% |
| 50–60% | 686 | 55% | 59% | 56% |
| 60–70% | 724 | 65% | 70% | 67% |
| 70–80% | 668 | 75% | 79% | 80% |
| 80–90% | 535 | 85% | 87% | 87% |
| 90–100% | 963 | 97% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 167 | 92 (55%) | 45¢ | 52% | $135.88 | +17% |
| 6–10¢ | 76 | 49 (64%) | 40¢ | 49% | $177.49 | +57% |
| 10–20¢ | 16 | 8 (50%) | 38¢ | 52% | $17.14 | +27% |
| 20¢+ | 2 | 2 (100%) | 49¢ | 71% | $9.87 | +97% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 258 | 151 (59%) | 44¢ | 52% | $343.80 | +29% |
| 5–10 min | 3 | 0 (0%) | 11¢ | 17% | -$3.42 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 25 | 7 (28%) | 19¢ | 26% | $20.03 | +40% |
| Toss-up (25–75¢) | 232 | 141 (61%) | 45¢ | 53% | $321.67 | +30% |
| Favorite (75–95¢) | 4 | 3 (75%) | 77¢ | 83% | -$1.32 | -4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 29 | 17 (59%) | 40¢ | 48% | $48.83 | +40% |
| ZEC | 29 | 13 (45%) | 43¢ | 50% | $1.59 | +1% |
| XRP | 29 | 17 (59%) | 45¢ | 51% | $35.99 | +27% |
| NEAR | 29 | 19 (66%) | 47¢ | 54% | $50.21 | +36% |
| ETH | 29 | 15 (52%) | 42¢ | 51% | $22.13 | +17% |
| BNB | 29 | 18 (62%) | 40¢ | 49% | $57.80 | +47% |
| DOGE | 29 | 18 (62%) | 44¢ | 52% | $46.48 | +35% |
| HYPE | 29 | 14 (48%) | 42¢ | 51% | $12.14 | +9% |
| BTC | 29 | 20 (69%) | 45¢ | 52% | $65.21 | +48% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 5:48:01 AM | ETH | DOWN | 12.0 min | 67¢ | 73% | 5¢ | Open | — |
| 9/28 5:47:43 AM | SOL | UP | 12.3 min | 28¢ | 34% | 5¢ | Open | — |
| 9/28 5:47:23 AM | HYPE | UP | 12.6 min | 16¢ | 21% | 4¢ | Open | — |
| 9/28 5:47:21 AM | DOGE | DOWN | 12.6 min | 65¢ | 74% | 7¢ | Open | — |
| 9/28 5:46:46 AM | ZEC | UP | 13.2 min | 28¢ | 35% | 6¢ | Open | — |
| 9/28 5:46:40 AM | NEAR | DOWN | 13.3 min | 48¢ | 55% | 6¢ | Open | — |
| 9/28 5:46:26 AM | BNB | DOWN | 13.6 min | 62¢ | 72% | 8¢ | Open | — |
| 9/28 5:46:26 AM | BTC | DOWN | 13.6 min | 62¢ | 68% | 4¢ | Open | — |
| 9/28 5:46:04 AM | XRP | DOWN | 13.9 min | 57¢ | 64% | 5¢ | Open | — |
| 9/28 5:34:04 AM | NEAR | DOWN | 10.9 min | 70¢ | 79% | 8¢ | ✅ Won | $2.85 |
| 9/28 5:32:37 AM | DOGE | DOWN | 12.4 min | 57¢ | 64% | 5¢ | ❌ Lost | -$5.88 |
| 9/28 5:31:52 AM | ZEC | DOWN | 13.1 min | 53¢ | 60% | 5¢ | ❌ Lost | -$5.48 |
| 9/28 5:31:32 AM | BNB | DOWN | 13.4 min | 51¢ | 61% | 8¢ | ❌ Lost | -$5.28 |
| 9/28 5:31:16 AM | XRP | UP | 13.7 min | 45¢ | 52% | 5¢ | ✅ Won | $5.32 |
| 9/28 5:31:16 AM | HYPE | UP | 13.7 min | 63¢ | 85% | 20¢ | ✅ Won | $3.53 |
| 9/28 5:31:16 AM | BTC | UP | 13.7 min | 43¢ | 52% | 7¢ | ✅ Won | $5.52 |
| 9/28 5:31:14 AM | SOL | UP | 13.8 min | 43¢ | 50% | 5¢ | ✅ Won | $5.52 |
| 9/28 5:31:14 AM | ETH | UP | 13.8 min | 46¢ | 54% | 6¢ | ✅ Won | $5.22 |
| 9/28 5:16:25 AM | ZEC | DOWN | 13.6 min | 38¢ | 56% | 16¢ | ❌ Lost | -$3.97 |
| 9/28 5:16:25 AM | ETH | DOWN | 13.6 min | 38¢ | 60% | 20¢ | ❌ Lost | -$3.97 |
| 9/28 5:16:23 AM | BNB | DOWN | 13.6 min | 45¢ | 59% | 12¢ | ❌ Lost | -$4.68 |
| 9/28 5:16:23 AM | SOL | DOWN | 13.6 min | 28¢ | 47% | 18¢ | ❌ Lost | -$2.95 |
| 9/28 5:16:23 AM | DOGE | DOWN | 13.6 min | 31¢ | 38% | 6¢ | ❌ Lost | -$3.25 |
| 9/28 5:16:23 AM | BTC | DOWN | 13.6 min | 40¢ | 52% | 10¢ | ❌ Lost | -$4.17 |
| 9/28 5:16:19 AM | HYPE | DOWN | 13.7 min | 35¢ | 41% | 4¢ | ❌ Lost | -$3.66 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
