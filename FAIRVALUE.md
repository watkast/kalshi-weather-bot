# Fair-Value Bot

*Updated Mon Sep 28, 5:42 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **4¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 250 | $230.12 | +20% | $130.76 / $99.36 |
| 4¢+ ← live bot | 243 | $299.47 | +27% | $168.57 / $130.90 |
| 6¢+ | 229 | $224.08 | +24% | $155.78 / $68.30 |
| 8¢+ | 206 | $147.38 | +20% | $125.96 / $21.42 |
| 10¢+ | 184 | $128.75 | +19% | $157.60 / -$28.85 |
| 15¢+ | 116 | $109.93 | +29% | $128.05 / -$18.12 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 261 | 252 | 145 (58%) | 43¢ | 51% | $329.06 | +29% | +16.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+2.8%** over 6,867 readings from 261 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1251 | 2% | 4% | 7% |
| 10–20% | 480 | 15% | 16% | 11% |
| 20–30% | 506 | 25% | 26% | 26% |
| 30–40% | 583 | 35% | 36% | 41% |
| 40–50% | 624 | 45% | 48% | 50% |
| 50–60% | 663 | 55% | 59% | 54% |
| 60–70% | 703 | 65% | 70% | 66% |
| 70–80% | 645 | 75% | 79% | 79% |
| 80–90% | 509 | 85% | 87% | 86% |
| 90–100% | 903 | 97% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 163 | 90 (55%) | 45¢ | 52% | $136.40 | +18% |
| 6–10¢ | 72 | 46 (64%) | 39¢ | 48% | $169.18 | +58% |
| 10–20¢ | 16 | 8 (50%) | 38¢ | 52% | $17.14 | +27% |
| 20¢+ | 1 | 1 (100%) | 35¢ | 58% | $6.34 | +173% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 249 | 145 (58%) | 43¢ | 51% | $332.48 | +30% |
| 5–10 min | 3 | 0 (0%) | 11¢ | 17% | -$3.42 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 25 | 7 (28%) | 19¢ | 26% | $20.03 | +40% |
| Toss-up (25–75¢) | 223 | 135 (61%) | 45¢ | 53% | $310.35 | +30% |
| Favorite (75–95¢) | 4 | 3 (75%) | 77¢ | 83% | -$1.32 | -4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 28 | 16 (57%) | 40¢ | 48% | $43.31 | +37% |
| ZEC | 28 | 13 (46%) | 42¢ | 50% | $7.07 | +6% |
| XRP | 28 | 16 (57%) | 45¢ | 51% | $30.67 | +24% |
| NEAR | 28 | 18 (64%) | 46¢ | 53% | $47.36 | +36% |
| ETH | 28 | 14 (50%) | 42¢ | 50% | $16.91 | +14% |
| BNB | 28 | 18 (64%) | 40¢ | 49% | $63.08 | +54% |
| DOGE | 28 | 18 (64%) | 44¢ | 52% | $52.36 | +41% |
| HYPE | 28 | 13 (46%) | 42¢ | 50% | $8.61 | +7% |
| BTC | 28 | 19 (68%) | 45¢ | 52% | $59.69 | +46% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 5:34:04 AM | NEAR | DOWN | 10.9 min | 70¢ | 79% | 8¢ | Open | — |
| 9/28 5:32:37 AM | DOGE | DOWN | 12.4 min | 57¢ | 64% | 5¢ | Open | — |
| 9/28 5:31:52 AM | ZEC | DOWN | 13.1 min | 53¢ | 60% | 5¢ | Open | — |
| 9/28 5:31:32 AM | BNB | DOWN | 13.4 min | 51¢ | 61% | 8¢ | Open | — |
| 9/28 5:31:16 AM | XRP | UP | 13.7 min | 45¢ | 52% | 5¢ | Open | — |
| 9/28 5:31:16 AM | HYPE | UP | 13.7 min | 63¢ | 85% | 20¢ | Open | — |
| 9/28 5:31:16 AM | BTC | UP | 13.7 min | 43¢ | 52% | 7¢ | Open | — |
| 9/28 5:31:14 AM | SOL | UP | 13.8 min | 43¢ | 50% | 5¢ | Open | — |
| 9/28 5:31:14 AM | ETH | UP | 13.8 min | 46¢ | 54% | 6¢ | Open | — |
| 9/28 5:16:25 AM | ZEC | DOWN | 13.6 min | 38¢ | 56% | 16¢ | ❌ Lost | -$3.97 |
| 9/28 5:16:25 AM | ETH | DOWN | 13.6 min | 38¢ | 60% | 20¢ | ❌ Lost | -$3.97 |
| 9/28 5:16:23 AM | BNB | DOWN | 13.6 min | 45¢ | 59% | 12¢ | ❌ Lost | -$4.68 |
| 9/28 5:16:23 AM | SOL | DOWN | 13.6 min | 28¢ | 47% | 18¢ | ❌ Lost | -$2.95 |
| 9/28 5:16:23 AM | DOGE | DOWN | 13.6 min | 31¢ | 38% | 6¢ | ❌ Lost | -$3.25 |
| 9/28 5:16:23 AM | BTC | DOWN | 13.6 min | 40¢ | 52% | 10¢ | ❌ Lost | -$4.17 |
| 9/28 5:16:19 AM | HYPE | DOWN | 13.7 min | 35¢ | 41% | 4¢ | ❌ Lost | -$3.66 |
| 9/28 5:16:17 AM | XRP | UP | 13.7 min | 61¢ | 69% | 6¢ | ✅ Won | $3.73 |
| 9/28 5:16:03 AM | NEAR | DOWN | 13.9 min | 32¢ | 39% | 5¢ | ❌ Lost | -$3.36 |
| 9/28 5:01:34 AM | NEAR | UP | 13.4 min | 64¢ | 71% | 5¢ | ✅ Won | $3.43 |
| 9/28 5:01:34 AM | BTC | UP | 13.4 min | 66¢ | 72% | 4¢ | ✅ Won | $3.24 |
| 9/28 5:01:20 AM | SOL | UP | 13.7 min | 62¢ | 69% | 5¢ | ✅ Won | $3.63 |
| 9/28 5:01:20 AM | HYPE | DOWN | 13.7 min | 24¢ | 34% | 9¢ | ❌ Lost | -$2.53 |
| 9/28 5:01:08 AM | ZEC | DOWN | 13.9 min | 35¢ | 42% | 5¢ | ❌ Lost | -$3.66 |
| 9/28 5:01:08 AM | XRP | DOWN | 13.9 min | 37¢ | 47% | 8¢ | ✅ Won | $6.13 |
| 9/28 5:01:08 AM | DOGE | DOWN | 13.9 min | 26¢ | 35% | 7¢ | ❌ Lost | -$2.74 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
