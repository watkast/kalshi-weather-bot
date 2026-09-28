# Fair-Value Bot

*Updated Mon Sep 28, 10:42 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **4¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 430 | $174.72 | +9% | $227.40 / -$52.68 |
| 4¢+ ← live bot | 416 | $222.73 | +12% | $311.69 / -$88.96 |
| 6¢+ | 397 | $216.56 | +13% | $241.00 / -$24.44 |
| 8¢+ | 361 | $188.02 | +14% | $168.74 / $19.28 |
| 10¢+ | 321 | $206.04 | +17% | $152.00 / $54.04 |
| 15¢+ | 202 | $194.51 | +30% | $136.12 / $58.39 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 439 | 430 | 230 (53%) | 44¢ | 52% | $333.24 | +17% | +11.6¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade.*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 28 | 4 (14%) | 3 / 25 | 7.0 | -$37.18 | -$87.67 | -69% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 25 | 8 (32%) | 9 / 16 | 6.2 | -$22.87 | -$8.54 | -10% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 8 | 1 (12%) | 2 / 6 | 2.0 | -$8.62 | -$18.12 | -64% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 100% of orders | 6 | 0 (0%) | 1 / 5 | 2.0 | -$10.20 | -$27.48 | -100% |

*Model accuracy vs Kalshi's prices on the same 799 readings (excluding the final minute): V1 **-5.6%**, V2 **+1.4%**, 3-exchange price (V3/V4) **-20.9%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 36 | 11 (31%) | -$33.69 | -77% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+3.9%** over 11,635 readings from 441 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1907 | 2% | 4% | 8% |
| 10–20% | 858 | 15% | 16% | 18% |
| 20–30% | 934 | 25% | 26% | 34% |
| 30–40% | 1074 | 35% | 36% | 45% |
| 40–50% | 1118 | 45% | 48% | 53% |
| 50–60% | 1145 | 55% | 59% | 56% |
| 60–70% | 1107 | 65% | 70% | 66% |
| 70–80% | 950 | 75% | 79% | 79% |
| 80–90% | 806 | 85% | 88% | 83% |
| 90–100% | 1736 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 268 | 147 (55%) | 45¢ | 52% | $209.47 | +17% |
| 6–10¢ | 127 | 67 (53%) | 42¢ | 51% | $115.06 | +21% |
| 10–20¢ | 30 | 14 (47%) | 42¢ | 56% | $9.11 | +7% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 425 | 230 (54%) | 44¢ | 52% | $340.36 | +17% |
| 5–10 min | 5 | 0 (0%) | 13¢ | 22% | -$7.12 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 40 | 9 (22%) | 18¢ | 25% | $13.42 | +18% |
| Toss-up (25–75¢) | 377 | 209 (55%) | 46¢ | 54% | $301.79 | +17% |
| Favorite (75–95¢) | 13 | 12 (92%) | 77¢ | 84% | $18.03 | +18% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 48 | 28 (58%) | 43¢ | 50% | $67.26 | +32% |
| ZEC | 48 | 25 (52%) | 43¢ | 51% | $35.44 | +17% |
| XRP | 48 | 25 (52%) | 46¢ | 53% | $23.18 | +10% |
| NEAR | 48 | 29 (60%) | 47¢ | 54% | $59.14 | +26% |
| ETH | 48 | 23 (48%) | 45¢ | 52% | $8.47 | +4% |
| DOGE | 48 | 25 (52%) | 44¢ | 52% | $31.93 | +15% |
| BTC | 48 | 29 (60%) | 46¢ | 54% | $61.76 | +27% |
| BNB | 47 | 25 (53%) | 42¢ | 51% | $42.82 | +21% |
| HYPE | 47 | 21 (45%) | 42¢ | 51% | $3.24 | +2% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 10:34:32 AM | XRP | UP | 10.5 min | 22¢ | 28% | 5¢ | Open | — |
| 9/28 10:34:13 AM | DOGE | UP | 10.8 min | 27¢ | 33% | 5¢ | Open | — |
| 9/28 10:33:40 AM | BTC | UP | 11.3 min | 28¢ | 38% | 9¢ | Open | — |
| 9/28 10:33:18 AM | HYPE | DOWN | 11.7 min | 59¢ | 67% | 6¢ | Open | — |
| 9/28 10:32:36 AM | BNB | DOWN | 12.4 min | 59¢ | 65% | 4¢ | Open | — |
| 9/28 10:31:37 AM | NEAR | DOWN | 13.4 min | 45¢ | 51% | 4¢ | Open | — |
| 9/28 10:31:37 AM | ZEC | DOWN | 13.4 min | 41¢ | 54% | 11¢ | Open | — |
| 9/28 10:31:37 AM | SOL | DOWN | 13.4 min | 52¢ | 59% | 5¢ | Open | — |
| 9/28 10:31:26 AM | ETH | UP | 13.6 min | 49¢ | 58% | 7¢ | Open | — |
| 9/28 10:16:52 AM | DOGE | DOWN | 13.1 min | 22¢ | 33% | 10¢ | ❌ Lost | -$2.33 |
| 9/28 10:16:52 AM | XRP | DOWN | 13.1 min | 26¢ | 53% | 26¢ | ❌ Lost | -$2.74 |
| 9/28 10:16:52 AM | BTC | DOWN | 13.1 min | 35¢ | 59% | 22¢ | ❌ Lost | -$3.66 |
| 9/28 10:16:52 AM | HYPE | DOWN | 13.1 min | 35¢ | 48% | 12¢ | ❌ Lost | -$3.66 |
| 9/28 10:16:36 AM | NEAR | DOWN | 13.4 min | 45¢ | 55% | 8¢ | ❌ Lost | -$4.68 |
| 9/28 10:16:36 AM | ETH | DOWN | 13.4 min | 56¢ | 63% | 5¢ | ❌ Lost | -$5.78 |
| 9/28 10:16:36 AM | ZEC | DOWN | 13.4 min | 41¢ | 49% | 6¢ | ❌ Lost | -$4.27 |
| 9/28 10:16:36 AM | SOL | DOWN | 13.4 min | 46¢ | 54% | 6¢ | ❌ Lost | -$4.78 |
| 9/28 10:16:27 AM | BNB | DOWN | 13.6 min | 51¢ | 65% | 12¢ | ❌ Lost | -$5.28 |
| 9/28 10:05:00 AM | BTC | UP | 10.0 min | 24¢ | 30% | 5¢ | ✅ Won | $7.47 |
| 9/28 10:03:52 AM | NEAR | DOWN | 11.1 min | 81¢ | 88% | 6¢ | ✅ Won | $1.79 |
| 9/28 10:02:57 AM | ETH | DOWN | 12.1 min | 70¢ | 77% | 5¢ | ✅ Won | $2.85 |
| 9/28 10:02:42 AM | DOGE | DOWN | 12.3 min | 65¢ | 74% | 7¢ | ❌ Lost | -$6.66 |
| 9/28 10:02:42 AM | HYPE | DOWN | 12.3 min | 58¢ | 68% | 8¢ | ❌ Lost | -$5.98 |
| 9/28 10:01:46 AM | XRP | DOWN | 13.2 min | 43¢ | 50% | 5¢ | ❌ Lost | -$4.48 |
| 9/28 10:01:46 AM | ZEC | DOWN | 13.2 min | 57¢ | 66% | 8¢ | ✅ Won | $4.12 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
