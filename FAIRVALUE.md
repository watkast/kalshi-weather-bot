# Fair-Value Bot

*Updated Mon Sep 28, 4:51 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **4¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 223 | $226.01 | +22% | $105.88 / $120.13 |
| 4¢+ ← live bot | 216 | $306.56 | +32% | $136.18 / $170.38 |
| 6¢+ | 202 | $232.65 | +30% | $126.23 / $106.42 |
| 8¢+ | 179 | $164.02 | +27% | $78.71 / $85.31 |
| 10¢+ | 161 | $149.16 | +27% | $128.54 / $20.62 |
| 15¢+ | 99 | $134.57 | +44% | $125.75 / $8.82 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 234 | 225 | 133 (59%) | 43¢ | 50% | $335.16 | +34% | +18.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+3.5%** over 6,138 readings from 234 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1205 | 2% | 4% | 7% |
| 10–20% | 446 | 15% | 16% | 11% |
| 20–30% | 460 | 25% | 25% | 26% |
| 30–40% | 526 | 35% | 35% | 41% |
| 40–50% | 542 | 45% | 48% | 49% |
| 50–60% | 596 | 55% | 58% | 52% |
| 60–70% | 616 | 65% | 71% | 63% |
| 70–80% | 531 | 75% | 79% | 76% |
| 80–90% | 424 | 85% | 88% | 84% |
| 90–100% | 792 | 97% | 98% | 95% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 147 | 80 (54%) | 45¢ | 51% | $120.74 | +18% |
| 6–10¢ | 66 | 44 (67%) | 39¢ | 48% | $171.20 | +64% |
| 10–20¢ | 11 | 8 (73%) | 38¢ | 51% | $36.88 | +86% |
| 20¢+ | 1 | 1 (100%) | 35¢ | 58% | $6.34 | +173% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 222 | 133 (60%) | 43¢ | 51% | $338.58 | +34% |
| 5–10 min | 3 | 0 (0%) | 11¢ | 17% | -$3.42 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 24 | 7 (29%) | 19¢ | 26% | $22.56 | +48% |
| Toss-up (25–75¢) | 197 | 123 (62%) | 45¢ | 53% | $313.92 | +34% |
| Favorite (75–95¢) | 4 | 3 (75%) | 77¢ | 83% | -$1.32 | -4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 25 | 15 (60%) | 40¢ | 47% | $46.60 | +45% |
| ZEC | 25 | 13 (52%) | 43¢ | 50% | $18.57 | +17% |
| XRP | 25 | 13 (52%) | 44¢ | 51% | $16.39 | +14% |
| NEAR | 25 | 17 (68%) | 45¢ | 52% | $54.34 | +47% |
| ETH | 25 | 12 (48%) | 41¢ | 49% | $12.80 | +12% |
| BNB | 25 | 17 (68%) | 40¢ | 49% | $66.18 | +64% |
| DOGE | 25 | 17 (68%) | 45¢ | 52% | $54.42 | +47% |
| HYPE | 25 | 12 (48%) | 42¢ | 50% | $10.97 | +10% |
| BTC | 25 | 17 (68%) | 44¢ | 52% | $54.89 | +48% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 4:46:34 AM | HYPE | DOWN | 13.4 min | 60¢ | 67% | 5¢ | Open | — |
| 9/28 4:46:32 AM | XRP | DOWN | 13.5 min | 54¢ | 60% | 4¢ | Open | — |
| 9/28 4:46:32 AM | DOGE | DOWN | 13.5 min | 59¢ | 66% | 5¢ | Open | — |
| 9/28 4:46:18 AM | NEAR | UP | 13.7 min | 69¢ | 76% | 6¢ | Open | — |
| 9/28 4:46:10 AM | BTC | UP | 13.8 min | 41¢ | 47% | 5¢ | Open | — |
| 9/28 4:46:08 AM | SOL | UP | 13.9 min | 38¢ | 46% | 7¢ | Open | — |
| 9/28 4:46:06 AM | ETH | UP | 13.9 min | 43¢ | 49% | 4¢ | Open | — |
| 9/28 4:46:06 AM | ZEC | UP | 13.9 min | 37¢ | 44% | 6¢ | Open | — |
| 9/28 4:46:04 AM | BNB | DOWN | 13.9 min | 56¢ | 64% | 6¢ | Open | — |
| 9/28 4:31:49 AM | BTC | UP | 13.2 min | 49¢ | 56% | 6¢ | ✅ Won | $4.92 |
| 9/28 4:31:45 AM | DOGE | UP | 13.2 min | 48¢ | 59% | 9¢ | ✅ Won | $5.02 |
| 9/28 4:31:41 AM | HYPE | UP | 13.3 min | 37¢ | 44% | 5¢ | ✅ Won | $6.13 |
| 9/28 4:31:35 AM | ZEC | UP | 13.4 min | 41¢ | 52% | 10¢ | ✅ Won | $5.73 |
| 9/28 4:31:33 AM | NEAR | UP | 13.4 min | 50¢ | 56% | 5¢ | ✅ Won | $4.82 |
| 9/28 4:31:31 AM | XRP | UP | 13.5 min | 48¢ | 55% | 6¢ | ✅ Won | $5.02 |
| 9/28 4:31:24 AM | SOL | UP | 13.6 min | 41¢ | 51% | 8¢ | ✅ Won | $5.73 |
| 9/28 4:31:12 AM | ETH | UP | 13.8 min | 41¢ | 48% | 5¢ | ✅ Won | $5.73 |
| 9/28 4:31:08 AM | BNB | DOWN | 13.8 min | 53¢ | 60% | 5¢ | ❌ Lost | -$5.48 |
| 9/28 4:17:36 AM | BTC | UP | 12.4 min | 77¢ | 83% | 4¢ | ✅ Won | $2.17 |
| 9/28 4:16:23 AM | SOL | DOWN | 13.6 min | 19¢ | 26% | 6¢ | ❌ Lost | -$2.01 |
| 9/28 4:16:19 AM | DOGE | DOWN | 13.7 min | 23¢ | 28% | 4¢ | ❌ Lost | -$2.43 |
| 9/28 4:16:09 AM | ZEC | UP | 13.8 min | 65¢ | 71% | 5¢ | ✅ Won | $3.34 |
| 9/28 4:16:04 AM | HYPE | DOWN | 13.9 min | 26¢ | 33% | 5¢ | ❌ Lost | -$2.74 |
| 9/28 4:16:04 AM | ETH | DOWN | 13.9 min | 25¢ | 32% | 6¢ | ❌ Lost | -$2.64 |
| 9/28 4:16:04 AM | XRP | DOWN | 13.9 min | 23¢ | 29% | 4¢ | ❌ Lost | -$2.43 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
