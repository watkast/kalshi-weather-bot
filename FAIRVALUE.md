# Fair-Value Bot

*Updated Mon Sep 28, 11:02 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **4¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 448 | $165.19 | +8% | $230.23 / -$65.04 |
| 4¢+ ← live bot | 433 | $222.99 | +11% | $306.56 / -$83.57 |
| 6¢+ | 411 | $217.42 | +13% | $236.71 / -$19.29 |
| 8¢+ | 369 | $195.30 | +14% | $157.59 / $37.71 |
| 10¢+ | 327 | $212.56 | +18% | $148.70 / $63.86 |
| 15¢+ | 204 | $196.30 | +30% | $131.04 / $65.26 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 456 | 448 | 236 (53%) | 44¢ | 52% | $318.16 | +16% | +11.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade.*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 46 | 10 (22%) | 11 / 35 | 7.7 | -$37.18 | -$102.75 | -51% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 42 | 11 (26%) | 25 / 17 | 7.0 | -$38.80 | -$48.27 | -30% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 12 | 2 (17%) | 5 / 7 | 2.0 | -$8.62 | -$20.43 | -51% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 100% of orders | 10 | 0 (0%) | 4 / 6 | 2.0 | -$10.20 | -$45.87 | -100% |

*Model accuracy vs Kalshi's prices on the same 1,206 readings (excluding the final minute): V1 **-0.1%**, V2 **+0.4%**, 3-exchange price (V3/V4) **-9.9%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 54 | 19 (35%) | -$56.96 | -74% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.3%** over 12,075 readings from 459 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2020 | 2% | 4% | 7% |
| 10–20% | 914 | 15% | 16% | 17% |
| 20–30% | 1019 | 25% | 26% | 32% |
| 30–40% | 1153 | 35% | 36% | 43% |
| 40–50% | 1171 | 45% | 48% | 52% |
| 50–60% | 1169 | 55% | 59% | 56% |
| 60–70% | 1117 | 65% | 70% | 67% |
| 70–80% | 957 | 75% | 79% | 79% |
| 80–90% | 809 | 85% | 88% | 83% |
| 90–100% | 1746 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 278 | 150 (54%) | 45¢ | 52% | $199.30 | +15% |
| 6–10¢ | 134 | 69 (51%) | 42¢ | 51% | $104.42 | +18% |
| 10–20¢ | 31 | 15 (48%) | 42¢ | 56% | $14.84 | +11% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 441 | 236 (54%) | 44¢ | 52% | $329.20 | +16% |
| 5–10 min | 7 | 0 (0%) | 15¢ | 23% | -$11.04 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 44 | 9 (20%) | 18¢ | 25% | $4.74 | +6% |
| Toss-up (25–75¢) | 391 | 215 (55%) | 46¢ | 54% | $295.39 | +16% |
| Favorite (75–95¢) | 13 | 12 (92%) | 77¢ | 84% | $18.03 | +18% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 50 | 29 (58%) | 43¢ | 51% | $66.90 | +30% |
| ZEC | 50 | 26 (52%) | 43¢ | 51% | $38.74 | +18% |
| XRP | 50 | 25 (50%) | 45¢ | 53% | $16.88 | +7% |
| NEAR | 50 | 30 (60%) | 46¢ | 54% | $60.19 | +25% |
| ETH | 50 | 23 (46%) | 45¢ | 52% | -$1.79 | -1% |
| DOGE | 50 | 25 (50%) | 44¢ | 51% | $23.71 | +10% |
| BTC | 50 | 29 (58%) | 45¢ | 53% | $56.80 | +24% |
| BNB | 49 | 27 (55%) | 43¢ | 52% | $51.47 | +24% |
| HYPE | 49 | 22 (45%) | 42¢ | 51% | $5.26 | +2% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 11:02:43 AM | BNB | DOWN | 12.3 min | 53¢ | 73% | 18¢ | Open | — |
| 9/28 11:02:20 AM | BTC | DOWN | 12.7 min | 67¢ | 74% | 6¢ | Open | — |
| 9/28 11:02:00 AM | NEAR | DOWN | 13.0 min | 77¢ | 83% | 4¢ | Open | — |
| 9/28 11:01:50 AM | SOL | DOWN | 13.2 min | 76¢ | 82% | 4¢ | Open | — |
| 9/28 11:01:50 AM | HYPE | DOWN | 13.2 min | 58¢ | 68% | 9¢ | Open | — |
| 9/28 11:01:50 AM | ETH | DOWN | 13.2 min | 64¢ | 72% | 6¢ | Open | — |
| 9/28 11:01:42 AM | XRP | UP | 13.3 min | 20¢ | 26% | 5¢ | Open | — |
| 9/28 11:01:21 AM | ZEC | UP | 13.7 min | 26¢ | 33% | 5¢ | Open | — |
| 9/28 10:52:51 AM | BTC | UP | 7.2 min | 19¢ | 30% | 10¢ | ❌ Lost | -$2.01 |
| 9/28 10:50:32 AM | HYPE | UP | 9.4 min | 18¢ | 24% | 4¢ | ❌ Lost | -$1.91 |
| 9/28 10:49:22 AM | ZEC | UP | 10.6 min | 23¢ | 30% | 5¢ | ❌ Lost | -$2.43 |
| 9/28 10:47:27 AM | XRP | UP | 12.6 min | 38¢ | 44% | 4¢ | ❌ Lost | -$3.97 |
| 9/28 10:46:44 AM | SOL | DOWN | 13.3 min | 48¢ | 57% | 7¢ | ❌ Lost | -$4.98 |
| 9/28 10:46:44 AM | NEAR | DOWN | 13.3 min | 41¢ | 49% | 7¢ | ❌ Lost | -$4.27 |
| 9/28 10:46:44 AM | DOGE | DOWN | 13.3 min | 52¢ | 60% | 6¢ | ❌ Lost | -$5.38 |
| 9/28 10:46:25 AM | BNB | DOWN | 13.6 min | 51¢ | 59% | 7¢ | ✅ Won | $4.72 |
| 9/28 10:46:25 AM | ETH | DOWN | 13.6 min | 50¢ | 57% | 5¢ | ❌ Lost | -$5.18 |
| 9/28 10:34:32 AM | XRP | UP | 10.5 min | 22¢ | 28% | 5¢ | ❌ Lost | -$2.33 |
| 9/28 10:34:13 AM | DOGE | UP | 10.8 min | 27¢ | 33% | 5¢ | ❌ Lost | -$2.84 |
| 9/28 10:33:40 AM | BTC | UP | 11.3 min | 28¢ | 38% | 9¢ | ❌ Lost | -$2.95 |
| 9/28 10:33:18 AM | HYPE | DOWN | 11.7 min | 59¢ | 67% | 6¢ | ✅ Won | $3.93 |
| 9/28 10:32:36 AM | BNB | DOWN | 12.4 min | 59¢ | 65% | 4¢ | ✅ Won | $3.93 |
| 9/28 10:31:37 AM | NEAR | DOWN | 13.4 min | 45¢ | 51% | 4¢ | ✅ Won | $5.32 |
| 9/28 10:31:37 AM | ZEC | DOWN | 13.4 min | 41¢ | 54% | 11¢ | ✅ Won | $5.73 |
| 9/28 10:31:37 AM | SOL | DOWN | 13.4 min | 52¢ | 59% | 5¢ | ✅ Won | $4.62 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
