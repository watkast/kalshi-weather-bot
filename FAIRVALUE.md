# Fair-Value Bot

*Updated Mon Sep 28, 10:22 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **4¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 421 | $181.44 | +9% | $227.37 / -$45.93 |
| 4¢+ ← live bot | 407 | $226.29 | +12% | $322.99 / -$96.70 |
| 6¢+ | 389 | $219.48 | +14% | $237.36 / -$17.88 |
| 8¢+ | 354 | $192.45 | +15% | $171.24 / $21.21 |
| 10¢+ | 317 | $207.01 | +18% | $158.29 / $48.72 |
| 15¢+ | 202 | $194.51 | +30% | $136.12 / $58.39 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 430 | 421 | 230 (55%) | 44¢ | 52% | $370.42 | +19% | +12.3¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade.*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 19 | 4 (21%) | 3 / 16 | 6.3 | -$36.01 | -$50.49 | -56% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 18 | 8 (44%) | 9 / 9 | 6.0 | -$10.38 | $14.33 | +22% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 6 | 1 (17%) | 2 / 4 | 2.0 | -$8.62 | -$13.91 | -58% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 100% of orders | 4 | 0 (0%) | 1 / 3 | 2.0 | -$10.20 | -$17.28 | -100% |

*Model accuracy vs Kalshi's prices on the same 607 readings (excluding the final minute): V1 **-6.1%**, V2 **+1.6%**, 3-exchange price (V3/V4) **-19.3%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 27 | 7 (26%) | -$21.30 | -68% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+3.9%** over 11,434 readings from 432 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1907 | 2% | 4% | 8% |
| 10–20% | 858 | 15% | 16% | 18% |
| 20–30% | 934 | 25% | 26% | 34% |
| 30–40% | 1072 | 35% | 36% | 44% |
| 40–50% | 1114 | 45% | 48% | 53% |
| 50–60% | 1135 | 55% | 59% | 56% |
| 60–70% | 1097 | 65% | 70% | 66% |
| 70–80% | 943 | 75% | 79% | 79% |
| 80–90% | 783 | 85% | 88% | 82% |
| 90–100% | 1591 | 97% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 267 | 147 (55%) | 45¢ | 52% | $215.25 | +17% |
| 6–10¢ | 124 | 67 (54%) | 42¢ | 51% | $128.79 | +24% |
| 10–20¢ | 27 | 14 (52%) | 43¢ | 57% | $20.38 | +17% |
| 20¢+ | 3 | 2 (67%) | 45¢ | 69% | $6.00 | +43% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 416 | 230 (55%) | 45¢ | 52% | $377.54 | +20% |
| 5–10 min | 5 | 0 (0%) | 13¢ | 22% | -$7.12 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 39 | 9 (23%) | 18¢ | 25% | $15.75 | +21% |
| Toss-up (25–75¢) | 369 | 209 (57%) | 46¢ | 54% | $336.64 | +19% |
| Favorite (75–95¢) | 13 | 12 (92%) | 77¢ | 84% | $18.03 | +18% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 47 | 28 (60%) | 43¢ | 50% | $72.04 | +35% |
| ZEC | 47 | 25 (53%) | 43¢ | 51% | $39.71 | +19% |
| XRP | 47 | 25 (53%) | 46¢ | 53% | $25.92 | +12% |
| NEAR | 47 | 29 (62%) | 47¢ | 54% | $63.82 | +28% |
| ETH | 47 | 23 (49%) | 44¢ | 52% | $14.25 | +7% |
| DOGE | 47 | 25 (53%) | 44¢ | 52% | $34.26 | +16% |
| BTC | 47 | 29 (62%) | 46¢ | 54% | $65.42 | +29% |
| BNB | 46 | 25 (54%) | 42¢ | 51% | $48.10 | +24% |
| HYPE | 46 | 21 (46%) | 43¢ | 51% | $6.90 | +3% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 10:16:52 AM | DOGE | DOWN | 13.1 min | 22¢ | 33% | 10¢ | Open | — |
| 9/28 10:16:52 AM | XRP | DOWN | 13.1 min | 26¢ | 53% | 26¢ | Open | — |
| 9/28 10:16:52 AM | BTC | DOWN | 13.1 min | 35¢ | 59% | 22¢ | Open | — |
| 9/28 10:16:52 AM | HYPE | DOWN | 13.1 min | 35¢ | 48% | 12¢ | Open | — |
| 9/28 10:16:36 AM | NEAR | DOWN | 13.4 min | 45¢ | 55% | 8¢ | Open | — |
| 9/28 10:16:36 AM | ETH | DOWN | 13.4 min | 56¢ | 63% | 5¢ | Open | — |
| 9/28 10:16:36 AM | ZEC | DOWN | 13.4 min | 41¢ | 49% | 6¢ | Open | — |
| 9/28 10:16:36 AM | SOL | DOWN | 13.4 min | 46¢ | 54% | 6¢ | Open | — |
| 9/28 10:16:27 AM | BNB | DOWN | 13.6 min | 51¢ | 65% | 12¢ | Open | — |
| 9/28 10:05:00 AM | BTC | UP | 10.0 min | 24¢ | 30% | 5¢ | ✅ Won | $7.47 |
| 9/28 10:03:52 AM | NEAR | DOWN | 11.1 min | 81¢ | 88% | 6¢ | ✅ Won | $1.79 |
| 9/28 10:02:57 AM | ETH | DOWN | 12.1 min | 70¢ | 77% | 5¢ | ✅ Won | $2.85 |
| 9/28 10:02:42 AM | DOGE | DOWN | 12.3 min | 65¢ | 74% | 7¢ | ❌ Lost | -$6.66 |
| 9/28 10:02:42 AM | HYPE | DOWN | 12.3 min | 58¢ | 68% | 8¢ | ❌ Lost | -$5.98 |
| 9/28 10:01:46 AM | XRP | DOWN | 13.2 min | 43¢ | 50% | 5¢ | ❌ Lost | -$4.48 |
| 9/28 10:01:46 AM | ZEC | DOWN | 13.2 min | 57¢ | 66% | 8¢ | ✅ Won | $4.12 |
| 9/28 10:01:33 AM | BNB | DOWN | 13.4 min | 59¢ | 66% | 6¢ | ❌ Lost | -$6.07 |
| 9/28 10:01:13 AM | SOL | UP | 13.8 min | 46¢ | 54% | 6¢ | ❌ Lost | -$4.78 |
| 9/28 9:48:20 AM | ETH | DOWN | 11.7 min | 41¢ | 49% | 6¢ | ❌ Lost | -$4.27 |
| 9/28 9:48:20 AM | BTC | DOWN | 11.7 min | 33¢ | 42% | 7¢ | ❌ Lost | -$3.46 |
| 9/28 9:47:06 AM | SOL | DOWN | 12.9 min | 31¢ | 42% | 9¢ | ❌ Lost | -$3.25 |
| 9/28 9:46:37 AM | DOGE | DOWN | 13.4 min | 38¢ | 47% | 8¢ | ❌ Lost | -$3.97 |
| 9/28 9:46:37 AM | NEAR | DOWN | 13.4 min | 50¢ | 57% | 5¢ | ❌ Lost | -$5.18 |
| 9/28 9:46:37 AM | ZEC | DOWN | 13.4 min | 34¢ | 40% | 4¢ | ❌ Lost | -$3.56 |
| 9/28 9:46:20 AM | XRP | DOWN | 13.7 min | 39¢ | 45% | 5¢ | ❌ Lost | -$4.07 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
