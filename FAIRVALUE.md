# Fair-Value Bot

*Updated Mon Sep 28, 8:43 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **4¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 358 | $150.80 | +9% | $229.54 / -$78.74 |
| 4¢+ ← live bot | 345 | $194.22 | +12% | $295.53 / -$101.31 |
| 6¢+ | 328 | $157.86 | +12% | $262.67 / -$104.81 |
| 8¢+ | 297 | $89.60 | +8% | $187.12 / -$97.52 |
| 10¢+ | 265 | $112.47 | +11% | $185.57 / -$73.10 |
| 15¢+ | 164 | $111.80 | +20% | $165.24 / -$53.44 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 367 | 358 | 198 (55%) | 45¢ | 53% | $321.47 | +19% | +13.6¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+2.5%** over 9,783 readings from 369 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1791 | 2% | 4% | 8% |
| 10–20% | 804 | 15% | 16% | 18% |
| 20–30% | 813 | 25% | 26% | 31% |
| 30–40% | 883 | 35% | 36% | 43% |
| 40–50% | 909 | 45% | 48% | 51% |
| 50–60% | 879 | 55% | 58% | 56% |
| 60–70% | 869 | 65% | 70% | 67% |
| 70–80% | 804 | 75% | 79% | 81% |
| 80–90% | 637 | 85% | 87% | 87% |
| 90–100% | 1394 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 225 | 123 (55%) | 46¢ | 52% | $163.38 | +15% |
| 6–10¢ | 106 | 61 (58%) | 42¢ | 51% | $143.18 | +31% |
| 10–20¢ | 24 | 12 (50%) | 45¢ | 59% | $8.91 | +8% |
| 20¢+ | 3 | 2 (67%) | 45¢ | 69% | $6.00 | +43% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 354 | 198 (56%) | 45¢ | 53% | $325.85 | +20% |
| 5–10 min | 4 | 0 (0%) | 10¢ | 17% | -$4.38 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 38 | 8 (21%) | 18¢ | 25% | $8.28 | +12% |
| Toss-up (25–75¢) | 308 | 179 (58%) | 47¢ | 55% | $296.95 | +20% |
| Favorite (75–95¢) | 12 | 11 (92%) | 77¢ | 83% | $16.24 | +17% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 40 | 24 (60%) | 44¢ | 51% | $59.19 | +33% |
| ZEC | 40 | 21 (52%) | 43¢ | 51% | $30.62 | +17% |
| XRP | 40 | 22 (55%) | 47¢ | 54% | $26.24 | +14% |
| NEAR | 40 | 23 (57%) | 46¢ | 53% | $40.74 | +22% |
| ETH | 40 | 19 (48%) | 44¢ | 52% | $6.42 | +3% |
| DOGE | 40 | 22 (55%) | 46¢ | 53% | $31.26 | +17% |
| BTC | 40 | 26 (65%) | 48¢ | 55% | $62.33 | +32% |
| BNB | 39 | 22 (56%) | 42¢ | 51% | $49.30 | +29% |
| HYPE | 39 | 19 (49%) | 43¢ | 52% | $15.37 | +9% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 8:31:26 AM | NEAR | DOWN | 13.6 min | 54¢ | 60% | 4¢ | Open | — |
| 9/28 8:31:12 AM | XRP | DOWN | 13.8 min | 42¢ | 49% | 5¢ | Open | — |
| 9/28 8:31:12 AM | ETH | DOWN | 13.8 min | 32¢ | 40% | 6¢ | Open | — |
| 9/28 8:31:08 AM | SOL | DOWN | 13.8 min | 28¢ | 35% | 5¢ | Open | — |
| 9/28 8:31:04 AM | BTC | DOWN | 13.9 min | 29¢ | 38% | 8¢ | Open | — |
| 9/28 8:31:04 AM | HYPE | DOWN | 13.9 min | 37¢ | 44% | 5¢ | Open | — |
| 9/28 8:31:04 AM | BNB | DOWN | 13.9 min | 29¢ | 35% | 5¢ | Open | — |
| 9/28 8:31:04 AM | ZEC | DOWN | 13.9 min | 28¢ | 40% | 10¢ | Open | — |
| 9/28 8:31:04 AM | DOGE | DOWN | 13.9 min | 27¢ | 39% | 10¢ | Open | — |
| 9/28 8:17:07 AM | BNB | UP | 12.9 min | 22¢ | 29% | 6¢ | ❌ Lost | -$2.33 |
| 9/28 8:16:19 AM | DOGE | DOWN | 13.7 min | 75¢ | 81% | 4¢ | ✅ Won | $2.36 |
| 9/28 8:16:13 AM | HYPE | DOWN | 13.8 min | 57¢ | 69% | 10¢ | ✅ Won | $4.12 |
| 9/28 8:16:11 AM | SOL | DOWN | 13.8 min | 70¢ | 80% | 8¢ | ✅ Won | $2.85 |
| 9/28 8:16:09 AM | BTC | DOWN | 13.8 min | 65¢ | 72% | 5¢ | ✅ Won | $3.34 |
| 9/28 8:16:09 AM | ETH | DOWN | 13.8 min | 60¢ | 67% | 5¢ | ✅ Won | $3.83 |
| 9/28 8:16:05 AM | XRP | DOWN | 13.9 min | 66¢ | 80% | 12¢ | ✅ Won | $3.24 |
| 9/28 8:16:05 AM | ZEC | UP | 13.9 min | 28¢ | 34% | 4¢ | ❌ Lost | -$2.95 |
| 9/28 8:16:05 AM | NEAR | DOWN | 13.9 min | 74¢ | 81% | 6¢ | ✅ Won | $2.46 |
| 9/28 8:08:06 AM | NEAR | UP | 6.9 min | 9¢ | 17% | 7¢ | ❌ Lost | -$0.96 |
| 9/28 8:02:00 AM | SOL | DOWN | 13.0 min | 76¢ | 82% | 4¢ | ✅ Won | $2.27 |
| 9/28 8:01:44 AM | DOGE | DOWN | 13.3 min | 76¢ | 82% | 5¢ | ✅ Won | $2.27 |
| 9/28 8:01:22 AM | ZEC | DOWN | 13.6 min | 72¢ | 78% | 4¢ | ✅ Won | $2.65 |
| 9/28 8:01:16 AM | ETH | DOWN | 13.7 min | 73¢ | 80% | 5¢ | ✅ Won | $2.56 |
| 9/28 8:01:16 AM | BTC | DOWN | 13.7 min | 69¢ | 76% | 6¢ | ✅ Won | $2.95 |
| 9/28 8:01:16 AM | BNB | DOWN | 13.7 min | 79¢ | 85% | 4¢ | ✅ Won | $1.98 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
