# Fair-Value Bot

*Updated Mon Sep 28, 6:22 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **4¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 277 | $163.32 | +12% | $135.17 / $28.15 |
| 4¢+ ← live bot | 269 | $219.94 | +18% | $186.37 / $33.57 |
| 6¢+ | 254 | $138.18 | +13% | $155.35 / -$17.17 |
| 8¢+ | 231 | $91.31 | +11% | $136.00 / -$44.69 |
| 10¢+ | 208 | $102.88 | +13% | $156.41 / -$53.53 |
| 15¢+ | 132 | $97.44 | +22% | $148.37 / -$50.93 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 288 | 279 | 155 (56%) | 44¢ | 52% | $275.05 | +22% | +15.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+2.0%** over 7,596 readings from 288 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1343 | 2% | 4% | 9% |
| 10–20% | 546 | 15% | 16% | 20% |
| 20–30% | 579 | 25% | 26% | 32% |
| 30–40% | 648 | 35% | 36% | 46% |
| 40–50% | 676 | 45% | 48% | 53% |
| 50–60% | 700 | 55% | 58% | 57% |
| 60–70% | 733 | 65% | 70% | 68% |
| 70–80% | 680 | 75% | 79% | 80% |
| 80–90% | 548 | 85% | 87% | 87% |
| 90–100% | 1143 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 175 | 94 (54%) | 45¢ | 52% | $116.65 | +14% |
| 6–10¢ | 83 | 50 (60%) | 42¢ | 51% | $141.05 | +39% |
| 10–20¢ | 19 | 9 (47%) | 42¢ | 56% | $7.48 | +9% |
| 20¢+ | 2 | 2 (100%) | 49¢ | 71% | $9.87 | +97% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 276 | 155 (56%) | 44¢ | 52% | $278.47 | +22% |
| 5–10 min | 3 | 0 (0%) | 11¢ | 17% | -$3.42 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 26 | 7 (27%) | 19¢ | 26% | $18.33 | +35% |
| Toss-up (25–75¢) | 248 | 144 (58%) | 46¢ | 54% | $255.87 | +22% |
| Favorite (75–95¢) | 5 | 4 (80%) | 77¢ | 84% | $0.85 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 31 | 18 (58%) | 40¢ | 48% | $49.90 | +38% |
| ZEC | 31 | 15 (48%) | 43¢ | 51% | $10.81 | +8% |
| XRP | 31 | 17 (55%) | 46¢ | 53% | $23.06 | +16% |
| NEAR | 31 | 19 (61%) | 47¢ | 55% | $37.98 | +25% |
| ETH | 31 | 15 (48%) | 44¢ | 52% | $7.73 | +5% |
| BNB | 31 | 18 (58%) | 41¢ | 50% | $46.65 | +35% |
| DOGE | 31 | 19 (61%) | 46¢ | 54% | $42.86 | +29% |
| HYPE | 31 | 14 (45%) | 43¢ | 51% | $3.00 | +2% |
| BTC | 31 | 20 (65%) | 46¢ | 53% | $53.06 | +36% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 6:17:07 AM | DOGE | DOWN | 12.9 min | 34¢ | 40% | 5¢ | Open | — |
| 9/28 6:16:52 AM | BNB | DOWN | 13.1 min | 46¢ | 58% | 11¢ | Open | — |
| 9/28 6:16:46 AM | HYPE | UP | 13.2 min | 30¢ | 36% | 5¢ | Open | — |
| 9/28 6:16:38 AM | BTC | UP | 13.4 min | 35¢ | 42% | 6¢ | Open | — |
| 9/28 6:16:26 AM | ETH | UP | 13.6 min | 36¢ | 42% | 4¢ | Open | — |
| 9/28 6:16:22 AM | XRP | UP | 13.6 min | 45¢ | 52% | 5¢ | Open | — |
| 9/28 6:16:22 AM | ZEC | UP | 13.6 min | 34¢ | 41% | 6¢ | Open | — |
| 9/28 6:16:08 AM | NEAR | DOWN | 13.9 min | 33¢ | 44% | 9¢ | Open | — |
| 9/28 6:16:04 AM | SOL | UP | 13.9 min | 36¢ | 45% | 7¢ | Open | — |
| 9/28 6:02:06 AM | HYPE | DOWN | 12.9 min | 73¢ | 83% | 9¢ | ❌ Lost | -$7.44 |
| 9/28 6:01:17 AM | NEAR | DOWN | 13.7 min | 71¢ | 80% | 8¢ | ❌ Lost | -$7.25 |
| 9/28 6:01:17 AM | ETH | DOWN | 13.7 min | 74¢ | 80% | 4¢ | ❌ Lost | -$7.54 |
| 9/28 6:01:11 AM | BNB | DOWN | 13.8 min | 46¢ | 58% | 10¢ | ❌ Lost | -$4.78 |
| 9/28 6:01:05 AM | XRP | DOWN | 13.9 min | 69¢ | 81% | 11¢ | ❌ Lost | -$7.05 |
| 9/28 6:01:05 AM | BTC | DOWN | 13.9 min | 56¢ | 66% | 8¢ | ❌ Lost | -$5.78 |
| 9/28 6:01:05 AM | SOL | DOWN | 13.9 min | 58¢ | 66% | 6¢ | ❌ Lost | -$5.98 |
| 9/28 6:01:05 AM | DOGE | DOWN | 13.9 min | 68¢ | 77% | 8¢ | ❌ Lost | -$6.96 |
| 9/28 6:01:05 AM | ZEC | UP | 13.9 min | 77¢ | 90% | 12¢ | ✅ Won | $2.17 |
| 9/28 5:48:01 AM | ETH | DOWN | 12.0 min | 67¢ | 73% | 5¢ | ❌ Lost | -$6.86 |
| 9/28 5:47:43 AM | SOL | UP | 12.3 min | 28¢ | 34% | 5¢ | ✅ Won | $7.05 |
| 9/28 5:47:23 AM | HYPE | UP | 12.6 min | 16¢ | 21% | 4¢ | ❌ Lost | -$1.70 |
| 9/28 5:47:21 AM | DOGE | DOWN | 12.6 min | 65¢ | 74% | 7¢ | ✅ Won | $3.34 |
| 9/28 5:46:46 AM | ZEC | UP | 13.2 min | 28¢ | 35% | 6¢ | ✅ Won | $7.05 |
| 9/28 5:46:40 AM | NEAR | DOWN | 13.3 min | 48¢ | 55% | 6¢ | ❌ Lost | -$4.98 |
| 9/28 5:46:26 AM | BNB | DOWN | 13.6 min | 62¢ | 72% | 8¢ | ❌ Lost | -$6.37 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
