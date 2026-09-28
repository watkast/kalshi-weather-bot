# Fair-Value Bot

*Updated Mon Sep 28, 10:52 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **4¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 439 | $168.94 | +8% | $240.23 / -$71.29 |
| 4¢+ ← live bot | 424 | $223.94 | +12% | $315.33 / -$91.39 |
| 6¢+ | 402 | $223.67 | +14% | $234.24 / -$10.57 |
| 8¢+ | 365 | $199.12 | +15% | $168.08 / $31.04 |
| 10¢+ | 324 | $213.10 | +18% | $153.88 / $59.22 |
| 15¢+ | 202 | $194.51 | +30% | $136.12 / $58.39 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 447 | 439 | 235 (54%) | 44¢ | 52% | $343.57 | +17% | +11.5¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade.*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 37 | 9 (24%) | 7 / 30 | 7.4 | -$37.18 | -$77.34 | -46% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 34 | 8 (24%) | 18 / 16 | 6.8 | -$38.80 | -$47.34 | -37% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 10 | 1 (10%) | 4 / 6 | 2.0 | -$8.62 | -$22.14 | -69% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 100% of orders | 8 | 0 (0%) | 3 / 5 | 2.0 | -$10.20 | -$37.48 | -100% |

*Model accuracy vs Kalshi's prices on the same 999 readings (excluding the final minute): V1 **+0.1%**, V2 **+1.3%**, 3-exchange price (V3/V4) **-12.7%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 45 | 14 (31%) | -$37.79 | -65% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.3%** over 11,850 readings from 450 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2004 | 2% | 4% | 7% |
| 10–20% | 882 | 15% | 16% | 17% |
| 20–30% | 971 | 25% | 26% | 32% |
| 30–40% | 1100 | 35% | 36% | 44% |
| 40–50% | 1139 | 45% | 48% | 52% |
| 50–60% | 1155 | 55% | 59% | 56% |
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
| 4–6¢ | 273 | 150 (55%) | 45¢ | 52% | $218.17 | +17% |
| 6–10¢ | 130 | 68 (52%) | 42¢ | 51% | $110.96 | +19% |
| 10–20¢ | 31 | 15 (48%) | 42¢ | 56% | $14.84 | +11% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 434 | 235 (54%) | 44¢ | 52% | $350.69 | +18% |
| 5–10 min | 5 | 0 (0%) | 13¢ | 22% | -$7.12 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 41 | 9 (22%) | 18¢ | 25% | $11.09 | +14% |
| Toss-up (25–75¢) | 385 | 214 (56%) | 46¢ | 54% | $314.45 | +17% |
| Favorite (75–95¢) | 13 | 12 (92%) | 77¢ | 84% | $18.03 | +18% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 49 | 29 (59%) | 43¢ | 51% | $71.88 | +33% |
| ZEC | 49 | 26 (53%) | 43¢ | 51% | $41.17 | +19% |
| XRP | 49 | 25 (51%) | 45¢ | 53% | $20.85 | +9% |
| NEAR | 49 | 30 (61%) | 46¢ | 54% | $64.46 | +27% |
| ETH | 49 | 23 (47%) | 45¢ | 52% | $3.39 | +1% |
| DOGE | 49 | 25 (51%) | 44¢ | 51% | $29.09 | +13% |
| BTC | 49 | 29 (59%) | 46¢ | 53% | $58.81 | +25% |
| BNB | 48 | 26 (54%) | 43¢ | 52% | $46.75 | +22% |
| HYPE | 48 | 22 (46%) | 43¢ | 52% | $7.17 | +3% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 10:50:32 AM | HYPE | UP | 9.4 min | 18¢ | 24% | 4¢ | Open | — |
| 9/28 10:49:22 AM | ZEC | UP | 10.6 min | 23¢ | 30% | 5¢ | Open | — |
| 9/28 10:47:27 AM | XRP | UP | 12.6 min | 38¢ | 44% | 4¢ | Open | — |
| 9/28 10:46:44 AM | SOL | DOWN | 13.3 min | 48¢ | 57% | 7¢ | Open | — |
| 9/28 10:46:44 AM | NEAR | DOWN | 13.3 min | 41¢ | 49% | 7¢ | Open | — |
| 9/28 10:46:44 AM | DOGE | DOWN | 13.3 min | 52¢ | 60% | 6¢ | Open | — |
| 9/28 10:46:25 AM | BNB | DOWN | 13.6 min | 51¢ | 59% | 7¢ | Open | — |
| 9/28 10:46:25 AM | ETH | DOWN | 13.6 min | 50¢ | 57% | 5¢ | Open | — |
| 9/28 10:34:32 AM | XRP | UP | 10.5 min | 22¢ | 28% | 5¢ | ❌ Lost | -$2.33 |
| 9/28 10:34:13 AM | DOGE | UP | 10.8 min | 27¢ | 33% | 5¢ | ❌ Lost | -$2.84 |
| 9/28 10:33:40 AM | BTC | UP | 11.3 min | 28¢ | 38% | 9¢ | ❌ Lost | -$2.95 |
| 9/28 10:33:18 AM | HYPE | DOWN | 11.7 min | 59¢ | 67% | 6¢ | ✅ Won | $3.93 |
| 9/28 10:32:36 AM | BNB | DOWN | 12.4 min | 59¢ | 65% | 4¢ | ✅ Won | $3.93 |
| 9/28 10:31:37 AM | NEAR | DOWN | 13.4 min | 45¢ | 51% | 4¢ | ✅ Won | $5.32 |
| 9/28 10:31:37 AM | ZEC | DOWN | 13.4 min | 41¢ | 54% | 11¢ | ✅ Won | $5.73 |
| 9/28 10:31:37 AM | SOL | DOWN | 13.4 min | 52¢ | 59% | 5¢ | ✅ Won | $4.62 |
| 9/28 10:31:26 AM | ETH | UP | 13.6 min | 49¢ | 58% | 7¢ | ❌ Lost | -$5.08 |
| 9/28 10:16:52 AM | DOGE | DOWN | 13.1 min | 22¢ | 33% | 10¢ | ❌ Lost | -$2.33 |
| 9/28 10:16:52 AM | XRP | DOWN | 13.1 min | 26¢ | 53% | 26¢ | ❌ Lost | -$2.74 |
| 9/28 10:16:52 AM | BTC | DOWN | 13.1 min | 35¢ | 59% | 22¢ | ❌ Lost | -$3.66 |
| 9/28 10:16:52 AM | HYPE | DOWN | 13.1 min | 35¢ | 48% | 12¢ | ❌ Lost | -$3.66 |
| 9/28 10:16:36 AM | NEAR | DOWN | 13.4 min | 45¢ | 55% | 8¢ | ❌ Lost | -$4.68 |
| 9/28 10:16:36 AM | ETH | DOWN | 13.4 min | 56¢ | 63% | 5¢ | ❌ Lost | -$5.78 |
| 9/28 10:16:36 AM | ZEC | DOWN | 13.4 min | 41¢ | 49% | 6¢ | ❌ Lost | -$4.27 |
| 9/28 10:16:36 AM | SOL | DOWN | 13.4 min | 46¢ | 54% | 6¢ | ❌ Lost | -$4.78 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
