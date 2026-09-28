# Fair-Value Bot

*Updated Mon Sep 28, 5:11 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **4¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 232 | $243.64 | +22% | $119.39 / $124.25 |
| 4¢+ ← live bot | 225 | $307.32 | +30% | $155.59 / $151.73 |
| 6¢+ | 211 | $227.74 | +27% | $146.23 / $81.51 |
| 8¢+ | 188 | $158.31 | +24% | $99.97 / $58.34 |
| 10¢+ | 169 | $128.43 | +21% | $150.64 / -$22.21 |
| 15¢+ | 104 | $128.01 | +39% | $139.63 / -$11.62 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 243 | 234 | 139 (59%) | 43¢ | 51% | $347.92 | +33% | +17.8¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+3.7%** over 6,381 readings from 243 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1240 | 2% | 4% | 6% |
| 10–20% | 477 | 15% | 16% | 11% |
| 20–30% | 499 | 25% | 25% | 25% |
| 30–40% | 571 | 35% | 36% | 40% |
| 40–50% | 584 | 45% | 47% | 47% |
| 50–60% | 611 | 55% | 58% | 51% |
| 60–70% | 628 | 65% | 71% | 63% |
| 70–80% | 546 | 75% | 79% | 76% |
| 80–90% | 432 | 85% | 88% | 84% |
| 90–100% | 793 | 97% | 97% | 95% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 155 | 86 (55%) | 45¢ | 52% | $137.47 | +19% |
| 6–10¢ | 67 | 44 (66%) | 39¢ | 48% | $167.23 | +61% |
| 10–20¢ | 11 | 8 (73%) | 38¢ | 51% | $36.88 | +86% |
| 20¢+ | 1 | 1 (100%) | 35¢ | 58% | $6.34 | +173% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 231 | 139 (60%) | 43¢ | 51% | $351.34 | +34% |
| 5–10 min | 3 | 0 (0%) | 11¢ | 17% | -$3.42 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 24 | 7 (29%) | 19¢ | 26% | $22.56 | +48% |
| Toss-up (25–75¢) | 206 | 129 (63%) | 45¢ | 53% | $326.68 | +34% |
| Favorite (75–95¢) | 4 | 3 (75%) | 77¢ | 83% | -$1.32 | -4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 26 | 15 (58%) | 40¢ | 47% | $42.63 | +40% |
| ZEC | 26 | 13 (50%) | 43¢ | 50% | $14.70 | +13% |
| XRP | 26 | 14 (54%) | 44¢ | 51% | $20.81 | +17% |
| NEAR | 26 | 17 (65%) | 46¢ | 53% | $47.29 | +39% |
| ETH | 26 | 13 (50%) | 41¢ | 49% | $18.32 | +16% |
| BNB | 26 | 18 (69%) | 40¢ | 49% | $70.40 | +64% |
| DOGE | 26 | 18 (69%) | 45¢ | 53% | $58.35 | +48% |
| HYPE | 26 | 13 (50%) | 43¢ | 51% | $14.80 | +13% |
| BTC | 26 | 18 (69%) | 44¢ | 52% | $60.62 | +51% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 5:01:34 AM | NEAR | UP | 13.4 min | 64¢ | 71% | 5¢ | Open | — |
| 9/28 5:01:34 AM | BTC | UP | 13.4 min | 66¢ | 72% | 4¢ | Open | — |
| 9/28 5:01:20 AM | SOL | UP | 13.7 min | 62¢ | 69% | 5¢ | Open | — |
| 9/28 5:01:20 AM | HYPE | DOWN | 13.7 min | 24¢ | 34% | 9¢ | Open | — |
| 9/28 5:01:08 AM | ZEC | DOWN | 13.9 min | 35¢ | 42% | 5¢ | Open | — |
| 9/28 5:01:08 AM | XRP | DOWN | 13.9 min | 37¢ | 47% | 8¢ | Open | — |
| 9/28 5:01:08 AM | DOGE | DOWN | 13.9 min | 26¢ | 35% | 7¢ | Open | — |
| 9/28 5:01:04 AM | BNB | DOWN | 13.9 min | 25¢ | 35% | 9¢ | Open | — |
| 9/28 5:01:04 AM | ETH | UP | 13.9 min | 73¢ | 80% | 6¢ | Open | — |
| 9/28 4:46:34 AM | HYPE | DOWN | 13.4 min | 60¢ | 67% | 5¢ | ✅ Won | $3.83 |
| 9/28 4:46:32 AM | XRP | DOWN | 13.5 min | 54¢ | 60% | 4¢ | ✅ Won | $4.42 |
| 9/28 4:46:32 AM | DOGE | DOWN | 13.5 min | 59¢ | 66% | 5¢ | ✅ Won | $3.93 |
| 9/28 4:46:18 AM | NEAR | UP | 13.7 min | 69¢ | 76% | 6¢ | ❌ Lost | -$7.05 |
| 9/28 4:46:10 AM | BTC | UP | 13.8 min | 41¢ | 47% | 5¢ | ✅ Won | $5.73 |
| 9/28 4:46:08 AM | SOL | UP | 13.9 min | 38¢ | 46% | 7¢ | ❌ Lost | -$3.97 |
| 9/28 4:46:06 AM | ETH | UP | 13.9 min | 43¢ | 49% | 4¢ | ✅ Won | $5.52 |
| 9/28 4:46:06 AM | ZEC | UP | 13.9 min | 37¢ | 44% | 6¢ | ❌ Lost | -$3.87 |
| 9/28 4:46:04 AM | BNB | DOWN | 13.9 min | 56¢ | 64% | 6¢ | ✅ Won | $4.22 |
| 9/28 4:31:49 AM | BTC | UP | 13.2 min | 49¢ | 56% | 6¢ | ✅ Won | $4.92 |
| 9/28 4:31:45 AM | DOGE | UP | 13.2 min | 48¢ | 59% | 9¢ | ✅ Won | $5.02 |
| 9/28 4:31:41 AM | HYPE | UP | 13.3 min | 37¢ | 44% | 5¢ | ✅ Won | $6.13 |
| 9/28 4:31:35 AM | ZEC | UP | 13.4 min | 41¢ | 52% | 10¢ | ✅ Won | $5.73 |
| 9/28 4:31:33 AM | NEAR | UP | 13.4 min | 50¢ | 56% | 5¢ | ✅ Won | $4.82 |
| 9/28 4:31:31 AM | XRP | UP | 13.5 min | 48¢ | 55% | 6¢ | ✅ Won | $5.02 |
| 9/28 4:31:24 AM | SOL | UP | 13.6 min | 41¢ | 51% | 8¢ | ✅ Won | $5.73 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
