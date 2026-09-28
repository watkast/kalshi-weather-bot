# Fair-Value Bot

*Updated Mon Sep 28, 11:23 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **6¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **6¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 457 | $121.59 | +6% | $241.56 / -$119.97 |
| 4¢+ ← live bot | 442 | $181.21 | +9% | $305.33 / -$124.12 |
| 6¢+ | 418 | $210.46 | +12% | $233.60 / -$23.14 |
| 8¢+ | 374 | $200.76 | +14% | $152.89 / $47.87 |
| 10¢+ | 331 | $194.96 | +16% | $138.21 / $56.75 |
| 15¢+ | 207 | $182.77 | +27% | $135.06 / $47.71 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 466 | 457 | 238 (52%) | 44¢ | 52% | $288.37 | +14% | +11.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade.*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 55 | 12 (22%) | 13 / 42 | 7.9 | -$37.18 | -$132.54 | -52% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 51 | 11 (22%) | 25 / 26 | 7.3 | -$55.90 | -$104.17 | -49% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 14 | 4 (29%) | 7 / 7 | 2.0 | -$8.62 | -$4.65 | -10% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 93% of orders | 12 | 2 (17%) | 6 / 6 | 2.0 | -$10.20 | -$32.26 | -62% |

*Model accuracy vs Kalshi's prices on the same 1,395 readings (excluding the final minute): V1 **+1.6%**, V2 **+1.4%**, 3-exchange price (V3/V4) **-4.5%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 63 | 22 (35%) | -$61.42 | -67% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.3%** over 12,282 readings from 468 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2057 | 2% | 4% | 9% |
| 10–20% | 959 | 15% | 16% | 21% |
| 20–30% | 1057 | 25% | 26% | 34% |
| 30–40% | 1182 | 35% | 36% | 45% |
| 40–50% | 1177 | 45% | 48% | 52% |
| 50–60% | 1176 | 55% | 59% | 57% |
| 60–70% | 1120 | 65% | 70% | 67% |
| 70–80% | 958 | 75% | 79% | 79% |
| 80–90% | 810 | 85% | 88% | 83% |
| 90–100% | 1786 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 283 | 152 (54%) | 45¢ | 52% | $192.02 | +14% |
| 6–10¢ | 137 | 69 (50%) | 42¢ | 51% | $87.39 | +15% |
| 10–20¢ | 32 | 15 (47%) | 42¢ | 57% | $9.36 | +7% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 450 | 238 (53%) | 45¢ | 53% | $299.41 | +14% |
| 5–10 min | 7 | 0 (0%) | 15¢ | 23% | -$11.04 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 45 | 10 (22%) | 18¢ | 25% | $12.62 | +14% |
| Toss-up (25–75¢) | 397 | 216 (54%) | 46¢ | 54% | $273.28 | +14% |
| Favorite (75–95¢) | 15 | 12 (80%) | 77¢ | 84% | $2.47 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 51 | 29 (57%) | 44¢ | 51% | $59.17 | +26% |
| ZEC | 51 | 27 (53%) | 42¢ | 50% | $46.00 | +21% |
| XRP | 51 | 26 (51%) | 45¢ | 52% | $24.76 | +11% |
| NEAR | 51 | 30 (59%) | 47¢ | 55% | $52.36 | +21% |
| ETH | 51 | 23 (45%) | 45¢ | 53% | -$8.36 | -4% |
| DOGE | 51 | 25 (49%) | 44¢ | 51% | $19.23 | +8% |
| BTC | 51 | 29 (57%) | 45¢ | 53% | $49.94 | +21% |
| BNB | 50 | 27 (54%) | 43¢ | 52% | $45.99 | +21% |
| HYPE | 50 | 22 (44%) | 43¢ | 51% | -$0.72 | -0% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 11:18:00 AM | XRP | UP | 12.0 min | 40¢ | 50% | 9¢ | Open | — |
| 9/28 11:16:58 AM | ZEC | UP | 13.0 min | 55¢ | 62% | 5¢ | Open | — |
| 9/28 11:16:42 AM | SOL | UP | 13.3 min | 61¢ | 71% | 8¢ | Open | — |
| 9/28 11:16:42 AM | BTC | UP | 13.3 min | 58¢ | 67% | 7¢ | Open | — |
| 9/28 11:16:42 AM | ETH | UP | 13.3 min | 55¢ | 66% | 9¢ | Open | — |
| 9/28 11:16:31 AM | BNB | DOWN | 13.5 min | 48¢ | 61% | 11¢ | Open | — |
| 9/28 11:16:31 AM | NEAR | DOWN | 13.5 min | 53¢ | 61% | 6¢ | Open | — |
| 9/28 11:16:31 AM | HYPE | DOWN | 13.5 min | 34¢ | 46% | 10¢ | Open | — |
| 9/28 11:16:31 AM | DOGE | DOWN | 13.5 min | 41¢ | 48% | 5¢ | Open | — |
| 9/28 11:03:02 AM | DOGE | DOWN | 12.0 min | 43¢ | 52% | 7¢ | ❌ Lost | -$4.48 |
| 9/28 11:02:43 AM | BNB | DOWN | 12.3 min | 53¢ | 73% | 18¢ | ❌ Lost | -$5.48 |
| 9/28 11:02:20 AM | BTC | DOWN | 12.7 min | 67¢ | 74% | 6¢ | ❌ Lost | -$6.86 |
| 9/28 11:02:00 AM | NEAR | DOWN | 13.0 min | 77¢ | 83% | 4¢ | ❌ Lost | -$7.83 |
| 9/28 11:01:50 AM | SOL | DOWN | 13.2 min | 76¢ | 82% | 4¢ | ❌ Lost | -$7.73 |
| 9/28 11:01:50 AM | HYPE | DOWN | 13.2 min | 58¢ | 68% | 9¢ | ❌ Lost | -$5.98 |
| 9/28 11:01:50 AM | ETH | DOWN | 13.2 min | 64¢ | 72% | 6¢ | ❌ Lost | -$6.57 |
| 9/28 11:01:42 AM | XRP | UP | 13.3 min | 20¢ | 26% | 5¢ | ✅ Won | $7.88 |
| 9/28 11:01:21 AM | ZEC | UP | 13.7 min | 26¢ | 33% | 5¢ | ✅ Won | $7.26 |
| 9/28 10:52:51 AM | BTC | UP | 7.2 min | 19¢ | 30% | 10¢ | ❌ Lost | -$2.01 |
| 9/28 10:50:32 AM | HYPE | UP | 9.4 min | 18¢ | 24% | 4¢ | ❌ Lost | -$1.91 |
| 9/28 10:49:22 AM | ZEC | UP | 10.6 min | 23¢ | 30% | 5¢ | ❌ Lost | -$2.43 |
| 9/28 10:47:27 AM | XRP | UP | 12.6 min | 38¢ | 44% | 4¢ | ❌ Lost | -$3.97 |
| 9/28 10:46:44 AM | SOL | DOWN | 13.3 min | 48¢ | 57% | 7¢ | ❌ Lost | -$4.98 |
| 9/28 10:46:44 AM | NEAR | DOWN | 13.3 min | 41¢ | 49% | 7¢ | ❌ Lost | -$4.27 |
| 9/28 10:46:44 AM | DOGE | DOWN | 13.3 min | 52¢ | 60% | 6¢ | ❌ Lost | -$5.38 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
