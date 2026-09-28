# Fair-Value Bot

*Updated Mon Sep 28, 6:52 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **4¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 295 | $167.47 | +12% | $163.28 / $4.19 |
| 4¢+ ← live bot | 286 | $243.13 | +19% | $224.00 / $19.13 |
| 6¢+ | 271 | $163.72 | +15% | $157.98 / $5.74 |
| 8¢+ | 247 | $103.73 | +11% | $147.32 / -$43.59 |
| 10¢+ | 223 | $125.41 | +15% | $174.28 / -$48.87 |
| 15¢+ | 143 | $122.65 | +26% | $145.09 / -$22.44 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 306 | 297 | 163 (55%) | 44¢ | 52% | $281.73 | +21% | +15.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+2.0%** over 8,082 readings from 306 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1403 | 2% | 4% | 9% |
| 10–20% | 569 | 15% | 16% | 20% |
| 20–30% | 608 | 25% | 26% | 32% |
| 30–40% | 717 | 35% | 36% | 44% |
| 40–50% | 758 | 45% | 48% | 53% |
| 50–60% | 768 | 55% | 59% | 57% |
| 60–70% | 792 | 65% | 70% | 68% |
| 70–80% | 723 | 75% | 79% | 81% |
| 80–90% | 570 | 85% | 87% | 88% |
| 90–100% | 1174 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 189 | 101 (53%) | 45¢ | 52% | $129.31 | +15% |
| 6–10¢ | 86 | 51 (59%) | 41¢ | 51% | $139.85 | +38% |
| 10–20¢ | 20 | 9 (45%) | 42¢ | 56% | $2.70 | +3% |
| 20¢+ | 2 | 2 (100%) | 49¢ | 71% | $9.87 | +97% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 294 | 163 (55%) | 44¢ | 52% | $285.15 | +21% |
| 5–10 min | 3 | 0 (0%) | 11¢ | 17% | -$3.42 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 26 | 7 (27%) | 19¢ | 26% | $18.33 | +35% |
| Toss-up (25–75¢) | 266 | 152 (57%) | 46¢ | 54% | $262.55 | +21% |
| Favorite (75–95¢) | 5 | 4 (80%) | 77¢ | 84% | $0.85 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 33 | 20 (61%) | 40¢ | 48% | $61.75 | +45% |
| ZEC | 33 | 16 (48%) | 43¢ | 51% | $13.08 | +9% |
| XRP | 33 | 18 (55%) | 46¢ | 53% | $24.41 | +16% |
| NEAR | 33 | 19 (58%) | 47¢ | 54% | $31.27 | +20% |
| ETH | 33 | 16 (48%) | 44¢ | 52% | $8.28 | +5% |
| BNB | 33 | 19 (58%) | 42¢ | 51% | $46.09 | +32% |
| DOGE | 33 | 19 (58%) | 45¢ | 53% | $35.13 | +23% |
| HYPE | 33 | 15 (45%) | 42¢ | 51% | $5.68 | +4% |
| BTC | 33 | 21 (64%) | 45¢ | 52% | $56.04 | +36% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 6:47:18 AM | ETH | DOWN | 12.7 min | 11¢ | 16% | 4¢ | Open | — |
| 9/28 6:47:00 AM | NEAR | DOWN | 13.0 min | 45¢ | 55% | 8¢ | Open | — |
| 9/28 6:46:58 AM | ZEC | DOWN | 13.0 min | 17¢ | 24% | 6¢ | Open | — |
| 9/28 6:46:48 AM | DOGE | DOWN | 13.2 min | 12¢ | 19% | 6¢ | Open | — |
| 9/28 6:46:36 AM | HYPE | DOWN | 13.4 min | 12¢ | 20% | 8¢ | Open | — |
| 9/28 6:46:32 AM | XRP | DOWN | 13.5 min | 16¢ | 21% | 4¢ | Open | — |
| 9/28 6:46:16 AM | BTC | UP | 13.7 min | 78¢ | 84% | 4¢ | Open | — |
| 9/28 6:46:04 AM | SOL | UP | 13.9 min | 77¢ | 83% | 5¢ | Open | — |
| 9/28 6:46:04 AM | BNB | DOWN | 13.9 min | 16¢ | 25% | 8¢ | Open | — |
| 9/28 6:33:50 AM | DOGE | UP | 11.2 min | 40¢ | 46% | 4¢ | ❌ Lost | -$4.17 |
| 9/28 6:33:05 AM | HYPE | UP | 11.9 min | 40¢ | 47% | 5¢ | ✅ Won | $5.83 |
| 9/28 6:33:00 AM | BTC | UP | 12.0 min | 32¢ | 38% | 5¢ | ❌ Lost | -$3.36 |
| 9/28 6:32:57 AM | NEAR | UP | 12.0 min | 31¢ | 37% | 5¢ | ❌ Lost | -$3.25 |
| 9/28 6:31:25 AM | SOL | UP | 13.6 min | 42¢ | 49% | 5¢ | ✅ Won | $5.62 |
| 9/28 6:31:19 AM | ZEC | UP | 13.7 min | 40¢ | 46% | 4¢ | ✅ Won | $5.83 |
| 9/28 6:31:11 AM | XRP | UP | 13.8 min | 38¢ | 49% | 9¢ | ❌ Lost | -$3.97 |
| 9/28 6:31:11 AM | BNB | DOWN | 13.8 min | 56¢ | 64% | 6¢ | ✅ Won | $4.22 |
| 9/28 6:31:09 AM | ETH | DOWN | 13.8 min | 55¢ | 61% | 4¢ | ✅ Won | $4.32 |
| 9/28 6:17:07 AM | DOGE | DOWN | 12.9 min | 34¢ | 40% | 5¢ | ❌ Lost | -$3.56 |
| 9/28 6:16:52 AM | BNB | DOWN | 13.1 min | 46¢ | 58% | 11¢ | ❌ Lost | -$4.78 |
| 9/28 6:16:46 AM | HYPE | UP | 13.2 min | 30¢ | 36% | 5¢ | ❌ Lost | -$3.15 |
| 9/28 6:16:38 AM | BTC | UP | 13.4 min | 35¢ | 42% | 6¢ | ✅ Won | $6.34 |
| 9/28 6:16:26 AM | ETH | UP | 13.6 min | 36¢ | 42% | 4¢ | ❌ Lost | -$3.77 |
| 9/28 6:16:22 AM | XRP | UP | 13.6 min | 45¢ | 52% | 5¢ | ✅ Won | $5.32 |
| 9/28 6:16:22 AM | ZEC | UP | 13.6 min | 34¢ | 41% | 6¢ | ❌ Lost | -$3.56 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
