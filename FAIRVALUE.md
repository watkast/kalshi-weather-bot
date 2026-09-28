# Fair-Value Bot

*Updated Mon Sep 28, 9:23 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **4¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 385 | $206.74 | +11% | $241.98 / -$35.24 |
| 4¢+ ← live bot | 372 | $241.67 | +14% | $330.67 / -$89.00 |
| 6¢+ | 355 | $233.21 | +16% | $255.76 / -$22.55 |
| 8¢+ | 323 | $169.54 | +14% | $183.51 / -$13.97 |
| 10¢+ | 290 | $181.75 | +17% | $172.66 / $9.09 |
| 15¢+ | 188 | $190.22 | +31% | $147.42 / $42.80 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 394 | 385 | 217 (56%) | 44¢ | 52% | $400.10 | +23% | +12.7¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.4%** over 10,530 readings from 396 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1880 | 2% | 4% | 8% |
| 10–20% | 827 | 15% | 16% | 18% |
| 20–30% | 848 | 25% | 26% | 31% |
| 30–40% | 929 | 35% | 37% | 42% |
| 40–50% | 977 | 45% | 48% | 50% |
| 50–60% | 1041 | 55% | 59% | 54% |
| 60–70% | 997 | 65% | 70% | 63% |
| 70–80% | 864 | 75% | 79% | 78% |
| 80–90% | 714 | 85% | 88% | 81% |
| 90–100% | 1453 | 97% | 97% | 95% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 247 | 139 (56%) | 45¢ | 52% | $228.39 | +20% |
| 6–10¢ | 109 | 62 (57%) | 42¢ | 51% | $142.59 | +30% |
| 10–20¢ | 26 | 14 (54%) | 43¢ | 58% | $23.12 | +20% |
| 20¢+ | 3 | 2 (67%) | 45¢ | 69% | $6.00 | +43% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 381 | 217 (57%) | 45¢ | 53% | $404.48 | +23% |
| 5–10 min | 4 | 0 (0%) | 10¢ | 17% | -$4.38 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 38 | 8 (21%) | 18¢ | 25% | $8.28 | +12% |
| Toss-up (25–75¢) | 335 | 198 (59%) | 46¢ | 54% | $375.58 | +23% |
| Favorite (75–95¢) | 12 | 11 (92%) | 77¢ | 83% | $16.24 | +17% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 43 | 27 (63%) | 43¢ | 50% | $78.51 | +41% |
| ZEC | 43 | 24 (56%) | 44¢ | 51% | $45.25 | +23% |
| XRP | 43 | 25 (58%) | 46¢ | 54% | $43.31 | +21% |
| NEAR | 43 | 26 (60%) | 46¢ | 54% | $53.82 | +26% |
| ETH | 43 | 21 (49%) | 44¢ | 51% | $15.42 | +8% |
| DOGE | 43 | 23 (53%) | 45¢ | 52% | $30.99 | +16% |
| BTC | 43 | 27 (63%) | 47¢ | 54% | $61.65 | +30% |
| BNB | 42 | 24 (57%) | 42¢ | 51% | $58.10 | +32% |
| HYPE | 42 | 20 (48%) | 43¢ | 52% | $13.05 | +7% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 9:18:26 AM | DOGE | UP | 11.6 min | 25¢ | 31% | 5¢ | Open | — |
| 9/28 9:18:03 AM | NEAR | UP | 11.9 min | 26¢ | 32% | 5¢ | Open | — |
| 9/28 9:17:49 AM | HYPE | UP | 12.2 min | 26¢ | 32% | 4¢ | Open | — |
| 9/28 9:17:35 AM | BTC | DOWN | 12.4 min | 63¢ | 70% | 5¢ | Open | — |
| 9/28 9:17:22 AM | ETH | DOWN | 12.6 min | 56¢ | 63% | 5¢ | Open | — |
| 9/28 9:16:33 AM | XRP | DOWN | 13.4 min | 53¢ | 59% | 4¢ | Open | — |
| 9/28 9:16:21 AM | ZEC | UP | 13.6 min | 32¢ | 38% | 4¢ | Open | — |
| 9/28 9:16:07 AM | SOL | DOWN | 13.9 min | 47¢ | 53% | 4¢ | Open | — |
| 9/28 9:16:05 AM | BNB | DOWN | 13.9 min | 53¢ | 60% | 5¢ | Open | — |
| 9/28 9:01:59 AM | NEAR | DOWN | 13.0 min | 45¢ | 52% | 5¢ | ✅ Won | $5.32 |
| 9/28 9:01:51 AM | HYPE | DOWN | 13.1 min | 38¢ | 45% | 5¢ | ❌ Lost | -$3.97 |
| 9/28 9:01:31 AM | ZEC | DOWN | 13.5 min | 47¢ | 54% | 5¢ | ✅ Won | $5.12 |
| 9/28 9:01:31 AM | DOGE | DOWN | 13.5 min | 36¢ | 42% | 5¢ | ❌ Lost | -$3.77 |
| 9/28 9:01:19 AM | BNB | DOWN | 13.7 min | 36¢ | 47% | 9¢ | ❌ Lost | -$3.77 |
| 9/28 9:01:15 AM | SOL | DOWN | 13.8 min | 34¢ | 40% | 4¢ | ✅ Won | $6.44 |
| 9/28 9:01:15 AM | ETH | DOWN | 13.8 min | 37¢ | 44% | 5¢ | ✅ Won | $6.13 |
| 9/28 9:01:13 AM | BTC | DOWN | 13.8 min | 38¢ | 45% | 5¢ | ❌ Lost | -$3.97 |
| 9/28 9:01:13 AM | XRP | DOWN | 13.8 min | 36¢ | 42% | 4¢ | ✅ Won | $6.23 |
| 9/28 8:46:34 AM | BNB | DOWN | 13.4 min | 42¢ | 48% | 4¢ | ✅ Won | $5.62 |
| 9/28 8:46:32 AM | ZEC | DOWN | 13.5 min | 74¢ | 80% | 4¢ | ✅ Won | $2.46 |
| 9/28 8:46:26 AM | BTC | DOWN | 13.6 min | 35¢ | 42% | 5¢ | ❌ Lost | -$3.66 |
| 9/28 8:46:24 AM | NEAR | UP | 13.6 min | 65¢ | 71% | 4¢ | ✅ Won | $3.34 |
| 9/28 8:46:08 AM | SOL | DOWN | 13.9 min | 40¢ | 46% | 4¢ | ✅ Won | $5.83 |
| 9/28 8:46:08 AM | XRP | DOWN | 13.9 min | 46¢ | 53% | 6¢ | ✅ Won | $5.22 |
| 9/28 8:46:06 AM | ETH | DOWN | 13.9 min | 36¢ | 44% | 6¢ | ❌ Lost | -$3.77 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
