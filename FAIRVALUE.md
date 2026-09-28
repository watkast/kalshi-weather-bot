# Fair-Value Bot

*Updated Mon Sep 28, 2:56 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 583 | $142.18 | +5% | $155.56 / -$13.38 |
| 4¢+ ← live bot | 564 | $230.69 | +9% | $223.98 / $6.71 |
| 6¢+ | 527 | $242.96 | +11% | $137.29 / $105.67 |
| 8¢+ | 469 | $258.47 | +15% | $80.63 / $177.84 |
| 10¢+ | 409 | $190.78 | +13% | $117.05 / $73.73 |
| 15¢+ | 245 | $175.67 | +22% | $96.87 / $78.80 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 592 | 583 | 305 (52%) | 45¢ | 53% | $359.99 | +13% | +10.2¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 181 | 79 (44%) | 52 / 129 | 8.6 | -$37.76 | -$60.92 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 161 | 50 (31%) | 78 / 83 | 7.7 | -$55.90 | -$163.98 | -25% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 40 | 9 (22%) | 17 / 23 | 2.0 | -$8.62 | -$41.38 | -31% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 75% of orders | 40 | 13 (32%) | 14 / 26 | 2.0 | -$13.69 | -$48.49 | -27% |

*Model accuracy vs Kalshi's prices on the same 4,276 readings (excluding the final minute): V1 **+4.2%**, V2 **+3.5%**, 3-exchange price (V3/V4) **+0.4%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 189 | 67 (35%) | -$35.73 | -12% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.5%** over 15,399 readings from 594 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2784 | 2% | 4% | 7% |
| 10–20% | 1211 | 15% | 16% | 18% |
| 20–30% | 1391 | 25% | 25% | 28% |
| 30–40% | 1561 | 35% | 36% | 40% |
| 40–50% | 1537 | 45% | 47% | 52% |
| 50–60% | 1498 | 55% | 59% | 57% |
| 60–70% | 1329 | 65% | 71% | 67% |
| 70–80% | 1080 | 75% | 80% | 80% |
| 80–90% | 913 | 85% | 88% | 83% |
| 90–100% | 2095 | 98% | 98% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 354 | 188 (53%) | 45¢ | 51% | $241.07 | +15% |
| 6–10¢ | 176 | 93 (53%) | 44¢ | 53% | $121.21 | +15% |
| 10–20¢ | 48 | 22 (46%) | 45¢ | 59% | -$1.89 | -1% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 569 | 301 (53%) | 45¢ | 53% | $361.12 | +14% |
| 5–10 min | 14 | 4 (29%) | 28¢ | 36% | -$1.13 | -3% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 55 | 12 (22%) | 18¢ | 26% | $12.39 | +12% |
| Toss-up (25–75¢) | 503 | 272 (54%) | 46¢ | 54% | $336.86 | +14% |
| Favorite (75–95¢) | 25 | 21 (84%) | 78¢ | 86% | $10.74 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 65 | 36 (55%) | 44¢ | 52% | $61.89 | +21% |
| ZEC | 65 | 34 (52%) | 43¢ | 51% | $48.58 | +17% |
| XRP | 65 | 36 (55%) | 44¢ | 52% | $60.42 | +20% |
| NEAR | 65 | 36 (55%) | 47¢ | 55% | $42.29 | +13% |
| ETH | 65 | 28 (43%) | 45¢ | 52% | -$20.47 | -7% |
| DOGE | 65 | 34 (52%) | 44¢ | 52% | $42.95 | +14% |
| BTC | 65 | 35 (54%) | 47¢ | 55% | $37.17 | +12% |
| BNB | 64 | 36 (56%) | 44¢ | 54% | $65.46 | +22% |
| HYPE | 64 | 30 (47%) | 42¢ | 51% | $21.70 | +8% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 2:48:01 PM | BNB | UP | 12.0 min | 34¢ | 40% | 5¢ | Open | — |
| 9/28 2:46:58 PM | SOL | DOWN | 13.0 min | 46¢ | 53% | 6¢ | Open | — |
| 9/28 2:46:58 PM | HYPE | DOWN | 13.0 min | 37¢ | 48% | 9¢ | Open | — |
| 9/28 2:46:58 PM | XRP | DOWN | 13.0 min | 48¢ | 55% | 5¢ | Open | — |
| 9/28 2:46:38 PM | ZEC | UP | 13.4 min | 56¢ | 63% | 5¢ | Open | — |
| 9/28 2:46:25 PM | DOGE | UP | 13.6 min | 41¢ | 50% | 8¢ | Open | — |
| 9/28 2:46:25 PM | ETH | UP | 13.6 min | 49¢ | 55% | 5¢ | Open | — |
| 9/28 2:46:17 PM | NEAR | DOWN | 13.7 min | 39¢ | 47% | 6¢ | Open | — |
| 9/28 2:46:17 PM | BTC | DOWN | 13.7 min | 56¢ | 62% | 4¢ | Open | — |
| 9/28 2:37:20 PM | HYPE | DOWN | 7.7 min | 51¢ | 60% | 8¢ | ✅ Won | $4.72 |
| 9/28 2:36:58 PM | ZEC | DOWN | 8.0 min | 69¢ | 79% | 8¢ | ✅ Won | $2.95 |
| 9/28 2:34:35 PM | SOL | DOWN | 10.4 min | 40¢ | 47% | 6¢ | ✅ Won | $5.83 |
| 9/28 2:33:35 PM | ETH | UP | 11.4 min | 39¢ | 46% | 5¢ | ❌ Lost | -$4.07 |
| 9/28 2:33:00 PM | DOGE | DOWN | 12.0 min | 48¢ | 56% | 7¢ | ✅ Won | $5.02 |
| 9/28 2:32:53 PM | BTC | DOWN | 12.1 min | 52¢ | 60% | 7¢ | ✅ Won | $4.62 |
| 9/28 2:32:08 PM | XRP | DOWN | 12.8 min | 44¢ | 52% | 6¢ | ✅ Won | $5.42 |
| 9/28 2:32:08 PM | NEAR | DOWN | 12.8 min | 37¢ | 44% | 5¢ | ✅ Won | $6.13 |
| 9/28 2:31:53 PM | BNB | DOWN | 13.1 min | 59¢ | 71% | 11¢ | ✅ Won | $3.93 |
| 9/28 2:20:48 PM | ZEC | DOWN | 9.2 min | 37¢ | 45% | 7¢ | ❌ Lost | -$3.87 |
| 9/28 2:17:19 PM | DOGE | UP | 12.7 min | 34¢ | 41% | 5¢ | ✅ Won | $6.44 |
| 9/28 2:16:34 PM | SOL | UP | 13.4 min | 29¢ | 35% | 4¢ | ❌ Lost | -$3.05 |
| 9/28 2:16:27 PM | ETH | DOWN | 13.6 min | 66¢ | 72% | 5¢ | ✅ Won | $3.24 |
| 9/28 2:16:27 PM | NEAR | DOWN | 13.6 min | 68¢ | 74% | 4¢ | ❌ Lost | -$6.96 |
| 9/28 2:16:17 PM | BTC | UP | 13.7 min | 29¢ | 36% | 6¢ | ❌ Lost | -$3.05 |
| 9/28 2:16:17 PM | XRP | UP | 13.7 min | 32¢ | 39% | 5¢ | ✅ Won | $6.64 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
