# Fair-Value Bot

*Updated Mon Sep 28, 7:19 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 743 | $131.74 | +4% | $190.07 / -$58.33 |
| 4¢+ ← live bot | 714 | $323.21 | +10% | $236.25 / $86.96 |
| 6¢+ | 663 | $324.08 | +12% | $179.02 / $145.06 |
| 8¢+ | 590 | $353.90 | +15% | $83.83 / $270.07 |
| 10¢+ | 509 | $270.63 | +14% | $81.93 / $188.70 |
| 15¢+ | 313 | $260.39 | +25% | $83.27 / $177.12 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 736 | 728 | 373 (51%) | 45¢ | 53% | $344.11 | +10% | +7.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 326 | 147 (45%) | 96 / 230 | 8.4 | -$37.76 | -$76.80 | -5% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 290 | 105 (36%) | 128 / 162 | 7.4 | -$55.90 | -$126.40 | -11% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 70 | 23 (33%) | 27 / 43 | 1.9 | -$14.97 | -$29.96 | -12% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 79% of orders | 75 | 29 (39%) | 24 / 51 | 2.0 | -$13.69 | -$48.31 | -14% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 19 | 7 (37%) | 5 / 14 | 1.4 | -$10.05 | -$17.78 | -22% |

*Model accuracy vs Kalshi's prices on the same 8,013 readings (excluding the final minute): V1 **+3.9%**, V2 **+4.6%**, 3-exchange price (V3/V4) **+2.0%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 334 | 206 (62%) | -$60.40 | -6% | 367 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.7%** over 19,429 readings from 756 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3695 | 2% | 4% | 6% |
| 10–20% | 1511 | 15% | 16% | 16% |
| 20–30% | 1744 | 25% | 26% | 26% |
| 30–40% | 1843 | 35% | 36% | 39% |
| 40–50% | 1882 | 45% | 48% | 52% |
| 50–60% | 1886 | 55% | 59% | 58% |
| 60–70% | 1616 | 65% | 71% | 67% |
| 70–80% | 1385 | 75% | 80% | 78% |
| 80–90% | 1221 | 85% | 88% | 81% |
| 90–100% | 2646 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 412 | 214 (52%) | 45¢ | 52% | $210.55 | +11% |
| 6–10¢ | 237 | 124 (52%) | 45¢ | 54% | $130.94 | +12% |
| 10–20¢ | 73 | 33 (45%) | 43¢ | 57% | $4.53 | +1% |
| 20¢+ | 6 | 2 (33%) | 35¢ | 65% | -$1.91 | -9% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 695 | 362 (52%) | 45¢ | 54% | $349.07 | +11% |
| 5–10 min | 30 | 9 (30%) | 31¢ | 39% | -$5.79 | -6% |
| 2–5 min | 2 | 2 (100%) | 88¢ | 94% | $2.34 | +13% |
| 1–2 min | 1 | 0 (0%) | 14¢ | 72% | -$1.51 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 79 | 19 (24%) | 18¢ | 27% | $35.98 | +23% |
| Toss-up (25–75¢) | 607 | 320 (53%) | 46¢ | 54% | $307.06 | +11% |
| Favorite (75–95¢) | 42 | 34 (81%) | 80¢ | 87% | $1.07 | +0% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| XRP | 82 | 47 (57%) | 47¢ | 55% | $71.53 | +18% |
| ETH | 82 | 36 (44%) | 46¢ | 54% | -$29.13 | -7% |
| BNB | 82 | 45 (55%) | 43¢ | 52% | $88.12 | +24% |
| NEAR | 81 | 43 (53%) | 48¢ | 55% | $32.42 | +8% |
| HYPE | 81 | 37 (46%) | 42¢ | 50% | $18.21 | +5% |
| BTC | 81 | 42 (52%) | 49¢ | 58% | $6.11 | +1% |
| SOL | 80 | 43 (54%) | 44¢ | 52% | $66.92 | +18% |
| DOGE | 80 | 42 (52%) | 45¢ | 53% | $48.62 | +13% |
| ZEC | 79 | 38 (48%) | 41¢ | 50% | $41.31 | +12% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 7:19:19 PM | HYPE | DOWN | 10.7 min | 87¢ | 93% | 4¢ | Open | — |
| 9/28 7:19:01 PM | DOGE | UP | 11.0 min | 22¢ | 31% | 8¢ | Open | — |
| 9/28 7:18:08 PM | ZEC | UP | 11.9 min | 19¢ | 24% | 4¢ | Open | — |
| 9/28 7:17:53 PM | XRP | DOWN | 12.1 min | 72¢ | 78% | 5¢ | Open | — |
| 9/28 7:17:22 PM | BTC | DOWN | 12.6 min | 67¢ | 75% | 7¢ | Open | — |
| 9/28 7:17:07 PM | SOL | DOWN | 12.9 min | 73¢ | 79% | 4¢ | Open | — |
| 9/28 7:17:07 PM | ETH | DOWN | 12.9 min | 72¢ | 79% | 6¢ | Open | — |
| 9/28 7:16:36 PM | BNB | DOWN | 13.4 min | 52¢ | 62% | 8¢ | Open | — |
| 9/28 7:02:34 PM | NEAR | DOWN | 12.4 min | 17¢ | 32% | 14¢ | ✅ Won | $8.20 |
| 9/28 7:02:34 PM | ZEC | DOWN | 12.4 min | 23¢ | 34% | 10¢ | ✅ Won | $7.57 |
| 9/28 7:02:27 PM | DOGE | DOWN | 12.6 min | 26¢ | 45% | 17¢ | ✅ Won | $7.26 |
| 9/28 7:02:04 PM | SOL | DOWN | 12.9 min | 49¢ | 58% | 7¢ | ✅ Won | $4.92 |
| 9/28 7:01:48 PM | HYPE | DOWN | 13.2 min | 59¢ | 65% | 4¢ | ✅ Won | $3.93 |
| 9/28 7:01:24 PM | BNB | DOWN | 13.6 min | 73¢ | 84% | 9¢ | ✅ Won | $2.56 |
| 9/28 7:01:24 PM | BTC | DOWN | 13.6 min | 69¢ | 83% | 12¢ | ✅ Won | $2.95 |
| 9/28 7:01:24 PM | XRP | DOWN | 13.6 min | 58¢ | 69% | 9¢ | ✅ Won | $4.02 |
| 9/28 7:01:24 PM | ETH | DOWN | 13.6 min | 62¢ | 78% | 15¢ | ✅ Won | $3.65 |
| 9/28 6:49:12 PM | BNB | UP | 10.8 min | 9¢ | 15% | 6¢ | ❌ Lost | -$0.94 |
| 9/28 6:46:54 PM | ZEC | UP | 13.1 min | 26¢ | 34% | 6¢ | ❌ Lost | -$2.74 |
| 9/28 6:46:35 PM | DOGE | UP | 13.4 min | 22¢ | 29% | 6¢ | ❌ Lost | -$2.33 |
| 9/28 6:46:26 PM | HYPE | UP | 13.6 min | 20¢ | 30% | 8¢ | ❌ Lost | -$2.12 |
| 9/28 6:46:26 PM | XRP | UP | 13.6 min | 22¢ | 32% | 9¢ | ❌ Lost | -$2.33 |
| 9/28 6:46:26 PM | ETH | UP | 13.6 min | 20¢ | 28% | 7¢ | ❌ Lost | -$2.12 |
| 9/28 6:37:07 PM | BTC | UP | 7.9 min | 63¢ | 76% | 11¢ | ❌ Lost | -$6.47 |
| 9/28 6:33:49 PM | NEAR | DOWN | 11.2 min | 31¢ | 38% | 6¢ | ❌ Lost | -$3.25 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
