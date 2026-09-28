# Fair-Value Bot

*Updated Mon Sep 28, 4:21 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **2¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **2¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 42 | $55.33 | +32% | $17.37 / $37.96 |
| 4¢+ ← live bot | 41 | $39.44 | +25% | -$7.02 / $46.46 |
| 6¢+ | 38 | $20.17 | +14% | -$16.96 / $37.13 |
| 8¢+ | 33 | $31.07 | +31% | $0.70 / $30.37 |
| 10¢+ | 29 | $23.09 | +27% | $6.65 / $16.44 |
| 15¢+ | 20 | $9.81 | +20% | -$4.10 / $13.91 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 54 | 45 | 25 (56%) | 37¢ | 45% | $77.67 | +45% | +11.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.5%** over 1,053 readings from 54 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 143 | 3% | 4% | 0% |
| 10–20% | 123 | 15% | 15% | 20% |
| 20–30% | 149 | 25% | 26% | 36% |
| 30–40% | 150 | 35% | 33% | 51% |
| 40–50% | 88 | 44% | 44% | 58% |
| 50–60% | 40 | 55% | 60% | 50% |
| 60–70% | 39 | 66% | 76% | 49% |
| 70–80% | 63 | 75% | 82% | 78% |
| 80–90% | 80 | 86% | 92% | 89% |
| 90–100% | 178 | 96% | 97% | 100% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 29 | 13 (45%) | 41¢ | 47% | $7.94 | +7% |
| 6–10¢ | 12 | 8 (67%) | 30¢ | 38% | $42.74 | +115% |
| 10–20¢ | 3 | 3 (100%) | 30¢ | 43% | $20.65 | +221% |
| 20¢+ | 1 | 1 (100%) | 35¢ | 58% | $6.34 | +173% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 43 | 25 (58%) | 38¢ | 46% | $79.39 | +47% |
| 5–10 min | 2 | 0 (0%) | 8¢ | 14% | -$1.72 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 12 | 2 (17%) | 17¢ | 24% | -$1.73 | -8% |
| Toss-up (25–75¢) | 32 | 22 (69%) | 43¢ | 51% | $77.13 | +54% |
| Favorite (75–95¢) | 1 | 1 (100%) | 76¢ | 82% | $2.27 | +29% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 5 | 3 (60%) | 28¢ | 35% | $15.29 | +104% |
| ZEC | 5 | 2 (40%) | 40¢ | 48% | -$0.64 | -3% |
| XRP | 5 | 3 (60%) | 26¢ | 33% | $16.14 | +116% |
| NEAR | 5 | 3 (60%) | 47¢ | 54% | $5.92 | +25% |
| ETH | 5 | 2 (40%) | 40¢ | 47% | -$0.89 | -4% |
| BNB | 5 | 4 (80%) | 38¢ | 47% | $20.24 | +102% |
| DOGE | 5 | 2 (40%) | 35¢ | 42% | $1.97 | +11% |
| HYPE | 5 | 3 (60%) | 42¢ | 51% | $8.45 | +39% |
| BTC | 5 | 3 (60%) | 36¢ | 43% | $11.19 | +59% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 4:17:36 AM | BTC | UP | 12.4 min | 77¢ | 83% | 4¢ | Open | — |
| 9/28 4:16:23 AM | SOL | DOWN | 13.6 min | 19¢ | 26% | 6¢ | Open | — |
| 9/28 4:16:19 AM | DOGE | DOWN | 13.7 min | 23¢ | 28% | 4¢ | Open | — |
| 9/28 4:16:09 AM | ZEC | UP | 13.8 min | 65¢ | 71% | 5¢ | Open | — |
| 9/28 4:16:04 AM | HYPE | DOWN | 13.9 min | 26¢ | 33% | 5¢ | Open | — |
| 9/28 4:16:04 AM | ETH | DOWN | 13.9 min | 25¢ | 32% | 6¢ | Open | — |
| 9/28 4:16:04 AM | XRP | DOWN | 13.9 min | 23¢ | 29% | 4¢ | Open | — |
| 9/28 4:16:04 AM | NEAR | DOWN | 13.9 min | 27¢ | 35% | 7¢ | Open | — |
| 9/28 4:16:04 AM | BNB | DOWN | 13.9 min | 27¢ | 43% | 15¢ | Open | — |
| 9/28 4:07:14 AM | BTC | DOWN | 7.8 min | 6¢ | 12% | 5¢ | ❌ Lost | -$0.65 |
| 9/28 4:01:58 AM | NEAR | DOWN | 13.0 min | 19¢ | 26% | 5¢ | ✅ Won | $7.99 |
| 9/28 4:01:32 AM | XRP | DOWN | 13.4 min | 20¢ | 27% | 6¢ | ❌ Lost | -$2.12 |
| 9/28 4:01:31 AM | ETH | DOWN | 13.5 min | 15¢ | 20% | 4¢ | ❌ Lost | -$1.59 |
| 9/28 4:01:15 AM | DOGE | DOWN | 13.7 min | 21¢ | 27% | 4¢ | ❌ Lost | -$2.22 |
| 9/28 4:01:02 AM | ZEC | DOWN | 13.9 min | 24¢ | 33% | 8¢ | ❌ Lost | -$2.53 |
| 9/28 4:01:00 AM | SOL | DOWN | 14.0 min | 15¢ | 20% | 4¢ | ❌ Lost | -$1.59 |
| 9/28 4:01:00 AM | HYPE | DOWN | 14.0 min | 12¢ | 20% | 7¢ | ❌ Lost | -$1.28 |
| 9/28 4:01:00 AM | BNB | DOWN | 14.0 min | 21¢ | 28% | 6¢ | ❌ Lost | -$2.22 |
| 9/27 11:16:19 PM | ETH | DOWN | 13.7 min | 37¢ | 47% | 8¢ | ✅ Won | $6.13 |
| 9/27 11:16:17 PM | ZEC | DOWN | 13.7 min | 42¢ | 49% | 5¢ | ❌ Lost | -$4.38 |
| 9/27 11:16:13 PM | DOGE | DOWN | 13.8 min | 35¢ | 45% | 8¢ | ✅ Won | $6.34 |
| 9/27 11:16:11 PM | XRP | DOWN | 13.8 min | 35¢ | 42% | 5¢ | ✅ Won | $6.34 |
| 9/27 11:16:11 PM | BTC | DOWN | 13.8 min | 35¢ | 43% | 7¢ | ✅ Won | $6.34 |
| 9/27 11:16:11 PM | SOL | DOWN | 13.8 min | 28¢ | 35% | 6¢ | ✅ Won | $7.05 |
| 9/27 11:16:11 PM | NEAR | DOWN | 13.8 min | 32¢ | 44% | 10¢ | ✅ Won | $6.64 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
