# Fair-Value Bot

*Updated Mon Sep 28, 12:03 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **6¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **6¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 484 | $111.79 | +5% | $228.18 / -$116.39 |
| 4¢+ ← live bot | 469 | $170.28 | +8% | $288.91 / -$118.63 |
| 6¢+ | 444 | $210.66 | +12% | $226.64 / -$15.98 |
| 8¢+ | 399 | $201.72 | +14% | $150.90 / $50.82 |
| 10¢+ | 352 | $198.07 | +15% | $129.19 / $68.88 |
| 15¢+ | 221 | $170.56 | +24% | $126.15 / $44.41 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 493 | 484 | 247 (51%) | 44¢ | 52% | $264.50 | +12% | +10.8¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 82 | 21 (26%) | 25 / 57 | 8.2 | -$37.18 | -$156.41 | -43% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 77 | 18 (23%) | 48 / 29 | 7.7 | -$55.90 | -$128.27 | -42% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 20 | 4 (20%) | 11 / 9 | 2.0 | -$8.62 | -$21.37 | -35% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 83% of orders | 18 | 3 (17%) | 9 / 9 | 2.0 | -$10.20 | -$39.58 | -57% |

*Model accuracy vs Kalshi's prices on the same 2,007 readings (excluding the final minute): V1 **+0.1%**, V2 **+0.6%**, 3-exchange price (V3/V4) **-5.0%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 90 | 38 (42%) | -$58.89 | -37% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.2%** over 12,948 readings from 495 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2166 | 2% | 4% | 9% |
| 10–20% | 1014 | 15% | 16% | 20% |
| 20–30% | 1174 | 25% | 25% | 32% |
| 30–40% | 1279 | 35% | 36% | 43% |
| 40–50% | 1279 | 45% | 47% | 53% |
| 50–60% | 1259 | 55% | 59% | 58% |
| 60–70% | 1181 | 65% | 70% | 68% |
| 70–80% | 971 | 75% | 80% | 80% |
| 80–90% | 821 | 85% | 88% | 83% |
| 90–100% | 1804 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 302 | 158 (52%) | 45¢ | 51% | $177.43 | +13% |
| 6–10¢ | 143 | 70 (49%) | 43¢ | 52% | $66.65 | +11% |
| 10–20¢ | 34 | 17 (50%) | 42¢ | 56% | $20.82 | +14% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 476 | 246 (52%) | 44¢ | 52% | $267.66 | +12% |
| 5–10 min | 8 | 1 (12%) | 16¢ | 24% | -$3.16 | -24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 47 | 11 (23%) | 18¢ | 25% | $18.28 | +20% |
| Toss-up (25–75¢) | 422 | 224 (53%) | 46¢ | 54% | $243.75 | +12% |
| Favorite (75–95¢) | 15 | 12 (80%) | 77¢ | 84% | $2.47 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 54 | 29 (54%) | 44¢ | 51% | $45.17 | +18% |
| ZEC | 54 | 28 (52%) | 42¢ | 50% | $43.82 | +19% |
| XRP | 54 | 27 (50%) | 44¢ | 52% | $24.08 | +10% |
| NEAR | 54 | 32 (59%) | 47¢ | 55% | $56.82 | +22% |
| ETH | 54 | 23 (43%) | 45¢ | 53% | -$21.37 | -9% |
| DOGE | 54 | 26 (48%) | 43¢ | 51% | $18.25 | +8% |
| BTC | 54 | 29 (54%) | 45¢ | 53% | $36.64 | +14% |
| BNB | 53 | 29 (55%) | 43¢ | 52% | $52.37 | +22% |
| HYPE | 53 | 24 (45%) | 42¢ | 51% | $8.72 | +4% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 12:02:46 PM | NEAR | UP | 12.2 min | 32¢ | 39% | 5¢ | Open | — |
| 9/28 12:02:40 PM | BTC | DOWN | 12.3 min | 34¢ | 41% | 5¢ | Open | — |
| 9/28 12:02:25 PM | HYPE | UP | 12.6 min | 36¢ | 43% | 5¢ | Open | — |
| 9/28 12:01:16 PM | ZEC | DOWN | 13.7 min | 56¢ | 72% | 14¢ | Open | — |
| 9/28 12:01:16 PM | ETH | UP | 13.7 min | 37¢ | 44% | 5¢ | Open | — |
| 9/28 12:01:08 PM | SOL | UP | 13.9 min | 28¢ | 38% | 9¢ | Open | — |
| 9/28 12:01:08 PM | XRP | UP | 13.9 min | 31¢ | 37% | 4¢ | Open | — |
| 9/28 12:01:08 PM | DOGE | UP | 13.9 min | 29¢ | 35% | 5¢ | Open | — |
| 9/28 12:01:08 PM | BNB | DOWN | 13.9 min | 57¢ | 67% | 8¢ | Open | — |
| 9/28 11:48:32 AM | BTC | UP | 11.4 min | 31¢ | 38% | 6¢ | ❌ Lost | -$3.25 |
| 9/28 11:48:26 AM | XRP | UP | 11.6 min | 36¢ | 42% | 4¢ | ✅ Won | $6.23 |
| 9/28 11:48:18 AM | NEAR | DOWN | 11.7 min | 53¢ | 59% | 4¢ | ❌ Lost | -$5.48 |
| 9/28 11:47:58 AM | DOGE | UP | 12.0 min | 26¢ | 32% | 4¢ | ❌ Lost | -$2.74 |
| 9/28 11:47:23 AM | SOL | UP | 12.6 min | 39¢ | 45% | 5¢ | ❌ Lost | -$4.07 |
| 9/28 11:47:01 AM | HYPE | UP | 13.0 min | 21¢ | 26% | 4¢ | ❌ Lost | -$2.22 |
| 9/28 11:46:41 AM | ETH | UP | 13.3 min | 36¢ | 43% | 5¢ | ❌ Lost | -$3.77 |
| 9/28 11:46:05 AM | ZEC | DOWN | 13.9 min | 42¢ | 48% | 5¢ | ❌ Lost | -$4.38 |
| 9/28 11:46:05 AM | BNB | DOWN | 13.9 min | 50¢ | 61% | 9¢ | ✅ Won | $4.82 |
| 9/28 11:38:25 AM | ZEC | UP | 6.6 min | 20¢ | 26% | 5¢ | ✅ Won | $7.88 |
| 9/28 11:33:34 AM | BTC | DOWN | 11.4 min | 39¢ | 45% | 5¢ | ❌ Lost | -$4.07 |
| 9/28 11:32:36 AM | NEAR | DOWN | 12.4 min | 44¢ | 50% | 4¢ | ✅ Won | $5.42 |
| 9/28 11:32:16 AM | XRP | DOWN | 12.7 min | 26¢ | 32% | 5¢ | ❌ Lost | -$2.74 |
| 9/28 11:32:06 AM | ETH | DOWN | 12.9 min | 34¢ | 40% | 4¢ | ❌ Lost | -$3.56 |
| 9/28 11:31:51 AM | HYPE | DOWN | 13.2 min | 46¢ | 52% | 4¢ | ✅ Won | $5.22 |
| 9/28 11:31:31 AM | SOL | DOWN | 13.5 min | 35¢ | 42% | 5¢ | ❌ Lost | -$3.66 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
