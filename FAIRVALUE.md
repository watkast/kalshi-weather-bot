# Fair-Value Bot

*Updated Mon Sep 28, 11:43 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **6¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **6¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 466 | $132.55 | +6% | $246.20 / -$113.65 |
| 4¢+ ← live bot | 451 | $185.35 | +9% | $307.32 / -$121.97 |
| 6¢+ | 427 | $203.63 | +12% | $222.46 / -$18.83 |
| 8¢+ | 382 | $197.30 | +14% | $147.55 / $49.75 |
| 10¢+ | 338 | $195.99 | +16% | $128.43 / $67.56 |
| 15¢+ | 210 | $175.76 | +26% | $124.24 / $51.52 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 475 | 466 | 242 (52%) | 44¢ | 52% | $282.30 | +13% | +11.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 64 | 16 (25%) | 18 / 46 | 8.0 | -$37.18 | -$138.61 | -46% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 60 | 11 (18%) | 34 / 26 | 7.5 | -$55.90 | -$143.99 | -57% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 16 | 4 (25%) | 9 / 7 | 2.0 | -$8.62 | -$9.09 | -19% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 94% of orders | 14 | 3 (21%) | 7 / 7 | 2.0 | -$10.20 | -$27.93 | -48% |

*Model accuracy vs Kalshi's prices on the same 1,593 readings (excluding the final minute): V1 **+1.9%**, V2 **+1.3%**, 3-exchange price (V3/V4) **-3.9%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 72 | 28 (39%) | -$49.56 | -41% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.4%** over 12,498 readings from 477 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2125 | 2% | 4% | 9% |
| 10–20% | 991 | 15% | 16% | 20% |
| 20–30% | 1115 | 25% | 26% | 33% |
| 30–40% | 1206 | 35% | 36% | 44% |
| 40–50% | 1186 | 45% | 48% | 52% |
| 50–60% | 1195 | 55% | 58% | 56% |
| 60–70% | 1126 | 65% | 70% | 66% |
| 70–80% | 958 | 75% | 79% | 79% |
| 80–90% | 810 | 85% | 88% | 83% |
| 90–100% | 1786 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 286 | 154 (54%) | 45¢ | 52% | $196.59 | +15% |
| 6–10¢ | 141 | 69 (49%) | 43¢ | 52% | $65.29 | +10% |
| 10–20¢ | 34 | 17 (50%) | 42¢ | 56% | $20.82 | +14% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 459 | 242 (53%) | 45¢ | 53% | $293.34 | +14% |
| 5–10 min | 7 | 0 (0%) | 15¢ | 23% | -$11.04 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 45 | 10 (22%) | 18¢ | 25% | $12.62 | +14% |
| Toss-up (25–75¢) | 406 | 220 (54%) | 46¢ | 54% | $267.21 | +14% |
| Favorite (75–95¢) | 15 | 12 (80%) | 77¢ | 84% | $2.47 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 52 | 29 (56%) | 44¢ | 52% | $52.90 | +22% |
| ZEC | 52 | 27 (52%) | 43¢ | 50% | $40.32 | +18% |
| XRP | 52 | 26 (50%) | 44¢ | 52% | $20.59 | +9% |
| NEAR | 52 | 31 (60%) | 47¢ | 55% | $56.88 | +22% |
| ETH | 52 | 23 (44%) | 45¢ | 53% | -$14.04 | -6% |
| DOGE | 52 | 26 (50%) | 44¢ | 51% | $24.96 | +11% |
| BTC | 52 | 29 (56%) | 46¢ | 54% | $43.96 | +18% |
| BNB | 51 | 28 (55%) | 43¢ | 52% | $51.01 | +22% |
| HYPE | 51 | 23 (45%) | 42¢ | 51% | $5.72 | +3% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 11:38:25 AM | ZEC | UP | 6.6 min | 20¢ | 26% | 5¢ | Open | — |
| 9/28 11:33:34 AM | BTC | DOWN | 11.4 min | 39¢ | 45% | 5¢ | Open | — |
| 9/28 11:32:36 AM | NEAR | DOWN | 12.4 min | 44¢ | 50% | 4¢ | Open | — |
| 9/28 11:32:16 AM | XRP | DOWN | 12.7 min | 26¢ | 32% | 5¢ | Open | — |
| 9/28 11:32:06 AM | ETH | DOWN | 12.9 min | 34¢ | 40% | 4¢ | Open | — |
| 9/28 11:31:51 AM | HYPE | DOWN | 13.2 min | 46¢ | 52% | 4¢ | Open | — |
| 9/28 11:31:31 AM | SOL | DOWN | 13.5 min | 35¢ | 42% | 5¢ | Open | — |
| 9/28 11:31:31 AM | DOGE | DOWN | 13.5 min | 38¢ | 45% | 5¢ | Open | — |
| 9/28 11:31:14 AM | BNB | DOWN | 13.8 min | 33¢ | 42% | 7¢ | Open | — |
| 9/28 11:18:00 AM | XRP | UP | 12.0 min | 40¢ | 50% | 9¢ | ❌ Lost | -$4.17 |
| 9/28 11:16:58 AM | ZEC | UP | 13.0 min | 55¢ | 62% | 5¢ | ❌ Lost | -$5.68 |
| 9/28 11:16:42 AM | SOL | UP | 13.3 min | 61¢ | 71% | 8¢ | ❌ Lost | -$6.27 |
| 9/28 11:16:42 AM | BTC | UP | 13.3 min | 58¢ | 67% | 7¢ | ❌ Lost | -$5.98 |
| 9/28 11:16:42 AM | ETH | UP | 13.3 min | 55¢ | 66% | 9¢ | ❌ Lost | -$5.68 |
| 9/28 11:16:31 AM | BNB | DOWN | 13.5 min | 48¢ | 61% | 11¢ | ✅ Won | $5.02 |
| 9/28 11:16:31 AM | NEAR | DOWN | 13.5 min | 53¢ | 61% | 6¢ | ✅ Won | $4.52 |
| 9/28 11:16:31 AM | HYPE | DOWN | 13.5 min | 34¢ | 46% | 10¢ | ✅ Won | $6.44 |
| 9/28 11:16:31 AM | DOGE | DOWN | 13.5 min | 41¢ | 48% | 5¢ | ✅ Won | $5.73 |
| 9/28 11:03:02 AM | DOGE | DOWN | 12.0 min | 43¢ | 52% | 7¢ | ❌ Lost | -$4.48 |
| 9/28 11:02:43 AM | BNB | DOWN | 12.3 min | 53¢ | 73% | 18¢ | ❌ Lost | -$5.48 |
| 9/28 11:02:20 AM | BTC | DOWN | 12.7 min | 67¢ | 74% | 6¢ | ❌ Lost | -$6.86 |
| 9/28 11:02:00 AM | NEAR | DOWN | 13.0 min | 77¢ | 83% | 4¢ | ❌ Lost | -$7.83 |
| 9/28 11:01:50 AM | SOL | DOWN | 13.2 min | 76¢ | 82% | 4¢ | ❌ Lost | -$7.73 |
| 9/28 11:01:50 AM | HYPE | DOWN | 13.2 min | 58¢ | 68% | 9¢ | ❌ Lost | -$5.98 |
| 9/28 11:01:50 AM | ETH | DOWN | 13.2 min | 64¢ | 72% | 6¢ | ❌ Lost | -$6.57 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
