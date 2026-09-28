# Fair-Value Bot

*Updated Mon Sep 28, 10:01 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **4¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 412 | $204.27 | +11% | $237.92 / -$33.65 |
| 4¢+ ← live bot | 398 | $246.50 | +14% | $333.74 / -$87.24 |
| 6¢+ | 380 | $239.42 | +16% | $244.78 / -$5.36 |
| 8¢+ | 345 | $182.10 | +14% | $176.34 / $5.76 |
| 10¢+ | 309 | $198.84 | +18% | $167.06 / $31.78 |
| 15¢+ | 198 | $189.74 | +30% | $134.57 / $55.17 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 416 | 412 | 226 (55%) | 44¢ | 52% | $382.16 | +20% | +12.2¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade.*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 10 | 0 (0%) | 1 / 9 | 5.0 | -$36.01 | -$38.75 | -100% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 9 | 1 (11%) | 2 / 7 | 4.5 | -$10.38 | -$17.01 | -63% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 4 | 0 (0%) | 1 / 3 | 2.0 | -$8.62 | -$15.63 | -100% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 100% of orders | 2 | 0 (0%) | 0 / 2 | 2.0 | -$7.08 | -$7.08 | -100% |

*Model accuracy vs Kalshi's prices on the same 398 readings (excluding the final minute): V1 **-8.0%**, V2 **-0.7%**, 3-exchange price (V3/V4) **-22.3%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 18 | 6 (33%) | -$15.23 | -60% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.1%** over 11,207 readings from 423 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1890 | 2% | 4% | 8% |
| 10–20% | 834 | 15% | 16% | 18% |
| 20–30% | 897 | 25% | 26% | 33% |
| 30–40% | 1030 | 35% | 36% | 44% |
| 40–50% | 1084 | 45% | 48% | 53% |
| 50–60% | 1114 | 55% | 59% | 56% |
| 60–70% | 1084 | 65% | 70% | 66% |
| 70–80% | 927 | 75% | 79% | 79% |
| 80–90% | 768 | 85% | 88% | 82% |
| 90–100% | 1579 | 97% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 262 | 144 (55%) | 45¢ | 52% | $213.69 | +17% |
| 6–10¢ | 120 | 66 (55%) | 42¢ | 51% | $142.09 | +27% |
| 10–20¢ | 27 | 14 (52%) | 43¢ | 57% | $20.38 | +17% |
| 20¢+ | 3 | 2 (67%) | 45¢ | 69% | $6.00 | +43% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 407 | 226 (56%) | 44¢ | 52% | $389.28 | +21% |
| 5–10 min | 5 | 0 (0%) | 13¢ | 22% | -$7.12 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 38 | 8 (21%) | 18¢ | 25% | $8.28 | +12% |
| Toss-up (25–75¢) | 362 | 207 (57%) | 46¢ | 54% | $357.64 | +21% |
| Favorite (75–95¢) | 12 | 11 (92%) | 77¢ | 83% | $16.24 | +17% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 46 | 28 (61%) | 43¢ | 50% | $76.82 | +38% |
| ZEC | 46 | 24 (52%) | 43¢ | 51% | $35.59 | +17% |
| XRP | 46 | 25 (54%) | 46¢ | 54% | $30.40 | +14% |
| NEAR | 46 | 28 (61%) | 46¢ | 53% | $62.03 | +28% |
| ETH | 46 | 22 (48%) | 44¢ | 51% | $11.40 | +5% |
| DOGE | 46 | 25 (54%) | 44¢ | 52% | $40.92 | +20% |
| BTC | 46 | 28 (61%) | 47¢ | 54% | $57.95 | +26% |
| BNB | 45 | 25 (56%) | 42¢ | 51% | $54.17 | +28% |
| HYPE | 45 | 21 (47%) | 42¢ | 51% | $12.88 | +7% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 10:01:46 AM | XRP | DOWN | 13.2 min | 43¢ | 50% | 5¢ | Open | — |
| 9/28 10:01:46 AM | ZEC | DOWN | 13.2 min | 57¢ | 66% | 8¢ | Open | — |
| 9/28 10:01:33 AM | BNB | DOWN | 13.4 min | 59¢ | 66% | 6¢ | Open | — |
| 9/28 10:01:13 AM | SOL | UP | 13.8 min | 46¢ | 54% | 6¢ | Open | — |
| 9/28 9:48:20 AM | ETH | DOWN | 11.7 min | 41¢ | 49% | 6¢ | ❌ Lost | -$4.27 |
| 9/28 9:48:20 AM | BTC | DOWN | 11.7 min | 33¢ | 42% | 7¢ | ❌ Lost | -$3.46 |
| 9/28 9:47:06 AM | SOL | DOWN | 12.9 min | 31¢ | 42% | 9¢ | ❌ Lost | -$3.25 |
| 9/28 9:46:37 AM | DOGE | DOWN | 13.4 min | 38¢ | 47% | 8¢ | ❌ Lost | -$3.97 |
| 9/28 9:46:37 AM | NEAR | DOWN | 13.4 min | 50¢ | 57% | 5¢ | ❌ Lost | -$5.18 |
| 9/28 9:46:37 AM | ZEC | DOWN | 13.4 min | 34¢ | 40% | 4¢ | ❌ Lost | -$3.56 |
| 9/28 9:46:20 AM | XRP | DOWN | 13.7 min | 39¢ | 45% | 5¢ | ❌ Lost | -$4.07 |
| 9/28 9:46:20 AM | BNB | DOWN | 13.7 min | 42¢ | 48% | 5¢ | ❌ Lost | -$4.38 |
| 9/28 9:46:20 AM | HYPE | DOWN | 13.7 min | 37¢ | 45% | 7¢ | ❌ Lost | -$3.87 |
| 9/28 9:35:12 AM | ZEC | UP | 9.8 min | 26¢ | 43% | 16¢ | ❌ Lost | -$2.74 |
| 9/28 9:34:10 AM | BNB | UP | 10.8 min | 39¢ | 45% | 4¢ | ✅ Won | $5.93 |
| 9/28 9:32:36 AM | NEAR | DOWN | 12.4 min | 37¢ | 43% | 4¢ | ✅ Won | $6.13 |
| 9/28 9:32:17 AM | DOGE | UP | 12.7 min | 33¢ | 41% | 7¢ | ✅ Won | $6.54 |
| 9/28 9:32:17 AM | ETH | UP | 12.7 min | 38¢ | 49% | 10¢ | ✅ Won | $6.03 |
| 9/28 9:32:17 AM | XRP | UP | 12.7 min | 32¢ | 41% | 8¢ | ❌ Lost | -$3.36 |
| 9/28 9:32:17 AM | BTC | UP | 12.7 min | 36¢ | 44% | 6¢ | ✅ Won | $6.23 |
| 9/28 9:32:17 AM | HYPE | UP | 12.7 min | 34¢ | 43% | 7¢ | ❌ Lost | -$3.56 |
| 9/28 9:32:17 AM | SOL | UP | 12.7 min | 34¢ | 43% | 8¢ | ✅ Won | $6.44 |
| 9/28 9:18:26 AM | DOGE | UP | 11.6 min | 25¢ | 31% | 5¢ | ✅ Won | $7.36 |
| 9/28 9:18:03 AM | NEAR | UP | 11.9 min | 26¢ | 32% | 5¢ | ✅ Won | $7.26 |
| 9/28 9:17:49 AM | HYPE | UP | 12.2 min | 26¢ | 32% | 4¢ | ✅ Won | $7.26 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
