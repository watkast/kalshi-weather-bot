# Fair-Value Bot

*Updated Mon Sep 28, 5:21 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **4¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 241 | $232.25 | +21% | $120.89 / $111.36 |
| 4¢+ ← live bot | 234 | $288.91 | +27% | $146.81 / $142.10 |
| 6¢+ | 220 | $218.58 | +25% | $133.29 / $85.29 |
| 8¢+ | 197 | $144.72 | +21% | $119.77 / $24.95 |
| 10¢+ | 176 | $129.19 | +20% | $160.77 / -$31.58 |
| 15¢+ | 109 | $121.93 | +35% | $135.20 / -$13.27 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 252 | 243 | 144 (59%) | 43¢ | 51% | $355.34 | +33% | +17.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+3.4%** over 6,624 readings from 252 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1248 | 2% | 4% | 6% |
| 10–20% | 479 | 15% | 16% | 11% |
| 20–30% | 502 | 25% | 25% | 25% |
| 30–40% | 573 | 35% | 36% | 40% |
| 40–50% | 597 | 45% | 48% | 47% |
| 50–60% | 633 | 55% | 59% | 52% |
| 60–70% | 669 | 65% | 71% | 65% |
| 70–80% | 608 | 75% | 79% | 78% |
| 80–90% | 463 | 85% | 88% | 85% |
| 90–100% | 852 | 97% | 98% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 160 | 90 (56%) | 45¢ | 52% | $146.67 | +19% |
| 6–10¢ | 71 | 45 (63%) | 38¢ | 48% | $165.45 | +58% |
| 10–20¢ | 11 | 8 (73%) | 38¢ | 51% | $36.88 | +86% |
| 20¢+ | 1 | 1 (100%) | 35¢ | 58% | $6.34 | +173% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 240 | 144 (60%) | 43¢ | 51% | $358.76 | +33% |
| 5–10 min | 3 | 0 (0%) | 11¢ | 17% | -$3.42 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 25 | 7 (28%) | 19¢ | 26% | $20.03 | +40% |
| Toss-up (25–75¢) | 214 | 134 (63%) | 45¢ | 53% | $336.63 | +34% |
| Favorite (75–95¢) | 4 | 3 (75%) | 77¢ | 83% | -$1.32 | -4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 27 | 16 (59%) | 41¢ | 48% | $46.26 | +41% |
| ZEC | 27 | 13 (48%) | 42¢ | 50% | $11.04 | +9% |
| XRP | 27 | 15 (56%) | 44¢ | 51% | $26.94 | +22% |
| NEAR | 27 | 18 (67%) | 46¢ | 54% | $50.72 | +39% |
| ETH | 27 | 14 (52%) | 42¢ | 50% | $20.88 | +18% |
| BNB | 27 | 18 (67%) | 40¢ | 49% | $67.76 | +60% |
| DOGE | 27 | 18 (67%) | 44¢ | 52% | $55.61 | +45% |
| HYPE | 27 | 13 (48%) | 42¢ | 50% | $12.27 | +10% |
| BTC | 27 | 19 (70%) | 45¢ | 52% | $63.86 | +51% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 5:16:25 AM | ZEC | DOWN | 13.6 min | 38¢ | 56% | 16¢ | Open | — |
| 9/28 5:16:25 AM | ETH | DOWN | 13.6 min | 38¢ | 60% | 20¢ | Open | — |
| 9/28 5:16:23 AM | BNB | DOWN | 13.6 min | 45¢ | 59% | 12¢ | Open | — |
| 9/28 5:16:23 AM | SOL | DOWN | 13.6 min | 28¢ | 47% | 18¢ | Open | — |
| 9/28 5:16:23 AM | DOGE | DOWN | 13.6 min | 31¢ | 38% | 6¢ | Open | — |
| 9/28 5:16:23 AM | BTC | DOWN | 13.6 min | 40¢ | 52% | 10¢ | Open | — |
| 9/28 5:16:19 AM | HYPE | DOWN | 13.7 min | 35¢ | 41% | 4¢ | Open | — |
| 9/28 5:16:17 AM | XRP | UP | 13.7 min | 61¢ | 69% | 6¢ | Open | — |
| 9/28 5:16:03 AM | NEAR | DOWN | 13.9 min | 32¢ | 39% | 5¢ | Open | — |
| 9/28 5:01:34 AM | NEAR | UP | 13.4 min | 64¢ | 71% | 5¢ | ✅ Won | $3.43 |
| 9/28 5:01:34 AM | BTC | UP | 13.4 min | 66¢ | 72% | 4¢ | ✅ Won | $3.24 |
| 9/28 5:01:20 AM | SOL | UP | 13.7 min | 62¢ | 69% | 5¢ | ✅ Won | $3.63 |
| 9/28 5:01:20 AM | HYPE | DOWN | 13.7 min | 24¢ | 34% | 9¢ | ❌ Lost | -$2.53 |
| 9/28 5:01:08 AM | ZEC | DOWN | 13.9 min | 35¢ | 42% | 5¢ | ❌ Lost | -$3.66 |
| 9/28 5:01:08 AM | XRP | DOWN | 13.9 min | 37¢ | 47% | 8¢ | ✅ Won | $6.13 |
| 9/28 5:01:08 AM | DOGE | DOWN | 13.9 min | 26¢ | 35% | 7¢ | ❌ Lost | -$2.74 |
| 9/28 5:01:04 AM | BNB | DOWN | 13.9 min | 25¢ | 35% | 9¢ | ❌ Lost | -$2.64 |
| 9/28 5:01:04 AM | ETH | UP | 13.9 min | 73¢ | 80% | 6¢ | ✅ Won | $2.56 |
| 9/28 4:46:34 AM | HYPE | DOWN | 13.4 min | 60¢ | 67% | 5¢ | ✅ Won | $3.83 |
| 9/28 4:46:32 AM | XRP | DOWN | 13.5 min | 54¢ | 60% | 4¢ | ✅ Won | $4.42 |
| 9/28 4:46:32 AM | DOGE | DOWN | 13.5 min | 59¢ | 66% | 5¢ | ✅ Won | $3.93 |
| 9/28 4:46:18 AM | NEAR | UP | 13.7 min | 69¢ | 76% | 6¢ | ❌ Lost | -$7.05 |
| 9/28 4:46:10 AM | BTC | UP | 13.8 min | 41¢ | 47% | 5¢ | ✅ Won | $5.73 |
| 9/28 4:46:08 AM | SOL | UP | 13.9 min | 38¢ | 46% | 7¢ | ❌ Lost | -$3.97 |
| 9/28 4:46:06 AM | ETH | UP | 13.9 min | 43¢ | 49% | 4¢ | ✅ Won | $5.52 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
