# Fair-Value Bot

*Updated Mon Sep 28, 7:09 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 734 | $91.67 | +3% | $196.25 / -$104.58 |
| 4¢+ ← live bot | 705 | $289.50 | +9% | $237.60 / $51.90 |
| 6¢+ | 654 | $299.95 | +11% | $154.82 / $145.13 |
| 8¢+ | 584 | $353.32 | +16% | $73.62 / $279.70 |
| 10¢+ | 505 | $281.86 | +15% | $80.12 / $201.74 |
| 15¢+ | 312 | $257.25 | +25% | $83.27 / $173.98 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 728 | 719 | 364 (51%) | 45¢ | 53% | $299.05 | +9% | +7.5¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 317 | 138 (44%) | 96 / 221 | 8.3 | -$37.76 | -$121.86 | -8% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 281 | 96 (34%) | 128 / 153 | 7.4 | -$55.90 | -$168.88 | -15% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 68 | 21 (31%) | 27 / 41 | 1.9 | -$14.97 | -$40.86 | -16% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 80% of orders | 73 | 27 (37%) | 24 / 49 | 2.0 | -$13.69 | -$56.71 | -17% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 18 | 7 (39%) | 4 / 14 | 1.3 | -$10.05 | -$14.42 | -19% |

*Model accuracy vs Kalshi's prices on the same 7,806 readings (excluding the final minute): V1 **+3.5%**, V2 **+3.9%**, 3-exchange price (V3/V4) **+1.6%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 325 | 197 (61%) | -$105.46 | -12% | 279 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.4%** over 19,204 readings from 747 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3591 | 2% | 4% | 7% |
| 10–20% | 1491 | 15% | 16% | 16% |
| 20–30% | 1723 | 25% | 26% | 26% |
| 30–40% | 1829 | 35% | 36% | 39% |
| 40–50% | 1863 | 45% | 48% | 52% |
| 50–60% | 1869 | 55% | 59% | 59% |
| 60–70% | 1599 | 65% | 71% | 68% |
| 70–80% | 1378 | 75% | 80% | 78% |
| 80–90% | 1216 | 85% | 88% | 81% |
| 90–100% | 2645 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 411 | 213 (52%) | 45¢ | 52% | $206.62 | +11% |
| 6–10¢ | 234 | 121 (52%) | 45¢ | 54% | $119.44 | +11% |
| 10–20¢ | 68 | 28 (41%) | 43¢ | 57% | -$25.10 | -8% |
| 20¢+ | 6 | 2 (33%) | 35¢ | 65% | -$1.91 | -9% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 686 | 353 (51%) | 45¢ | 54% | $304.01 | +9% |
| 5–10 min | 30 | 9 (30%) | 31¢ | 39% | -$5.79 | -6% |
| 2–5 min | 2 | 2 (100%) | 88¢ | 94% | $2.34 | +13% |
| 1–2 min | 1 | 0 (0%) | 14¢ | 72% | -$1.51 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 77 | 17 (22%) | 18¢ | 26% | $20.21 | +13% |
| Toss-up (25–75¢) | 600 | 313 (52%) | 46¢ | 54% | $277.77 | +10% |
| Favorite (75–95¢) | 42 | 34 (81%) | 80¢ | 87% | $1.07 | +0% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| XRP | 81 | 46 (57%) | 47¢ | 55% | $67.51 | +17% |
| ETH | 81 | 35 (43%) | 46¢ | 53% | -$32.78 | -9% |
| BNB | 81 | 44 (54%) | 42¢ | 52% | $85.56 | +24% |
| NEAR | 80 | 42 (52%) | 48¢ | 55% | $24.22 | +6% |
| HYPE | 80 | 36 (45%) | 42¢ | 50% | $14.28 | +4% |
| BTC | 80 | 41 (51%) | 49¢ | 57% | $3.16 | +1% |
| SOL | 79 | 42 (53%) | 44¢ | 51% | $62.00 | +17% |
| DOGE | 79 | 41 (52%) | 45¢ | 53% | $41.36 | +11% |
| ZEC | 78 | 37 (47%) | 42¢ | 50% | $33.74 | +10% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 7:02:34 PM | NEAR | DOWN | 12.4 min | 17¢ | 32% | 14¢ | Open | — |
| 9/28 7:02:34 PM | ZEC | DOWN | 12.4 min | 23¢ | 34% | 10¢ | Open | — |
| 9/28 7:02:27 PM | DOGE | DOWN | 12.6 min | 26¢ | 45% | 17¢ | Open | — |
| 9/28 7:02:04 PM | SOL | DOWN | 12.9 min | 49¢ | 58% | 7¢ | Open | — |
| 9/28 7:01:48 PM | HYPE | DOWN | 13.2 min | 59¢ | 65% | 4¢ | Open | — |
| 9/28 7:01:24 PM | BNB | DOWN | 13.6 min | 73¢ | 84% | 9¢ | Open | — |
| 9/28 7:01:24 PM | BTC | DOWN | 13.6 min | 69¢ | 83% | 12¢ | Open | — |
| 9/28 7:01:24 PM | XRP | DOWN | 13.6 min | 58¢ | 69% | 9¢ | Open | — |
| 9/28 7:01:24 PM | ETH | DOWN | 13.6 min | 62¢ | 78% | 15¢ | Open | — |
| 9/28 6:49:12 PM | BNB | UP | 10.8 min | 9¢ | 15% | 6¢ | ❌ Lost | -$0.94 |
| 9/28 6:46:54 PM | ZEC | UP | 13.1 min | 26¢ | 34% | 6¢ | ❌ Lost | -$2.74 |
| 9/28 6:46:35 PM | DOGE | UP | 13.4 min | 22¢ | 29% | 6¢ | ❌ Lost | -$2.33 |
| 9/28 6:46:26 PM | HYPE | UP | 13.6 min | 20¢ | 30% | 8¢ | ❌ Lost | -$2.12 |
| 9/28 6:46:26 PM | XRP | UP | 13.6 min | 22¢ | 32% | 9¢ | ❌ Lost | -$2.33 |
| 9/28 6:46:26 PM | ETH | UP | 13.6 min | 20¢ | 28% | 7¢ | ❌ Lost | -$2.12 |
| 9/28 6:37:07 PM | BTC | UP | 7.9 min | 63¢ | 76% | 11¢ | ❌ Lost | -$6.47 |
| 9/28 6:33:49 PM | NEAR | DOWN | 11.2 min | 31¢ | 38% | 6¢ | ❌ Lost | -$3.25 |
| 9/28 6:33:27 PM | HYPE | DOWN | 11.6 min | 44¢ | 54% | 8¢ | ❌ Lost | -$4.58 |
| 9/28 6:32:08 PM | SOL | UP | 12.9 min | 24¢ | 31% | 5¢ | ✅ Won | $7.47 |
| 9/28 6:31:52 PM | DOGE | UP | 13.1 min | 30¢ | 39% | 7¢ | ✅ Won | $6.85 |
| 9/28 6:31:32 PM | XRP | UP | 13.4 min | 36¢ | 43% | 5¢ | ✅ Won | $6.23 |
| 9/28 6:31:32 PM | ZEC | UP | 13.4 min | 54¢ | 61% | 6¢ | ✅ Won | $4.46 |
| 9/28 6:31:26 PM | ETH | DOWN | 13.6 min | 53¢ | 59% | 4¢ | ❌ Lost | -$5.48 |
| 9/28 6:31:15 PM | BNB | UP | 13.7 min | 39¢ | 45% | 4¢ | ✅ Won | $5.96 |
| 9/28 6:28:57 PM | ZEC | UP | 1.0 min | 14¢ | 72% | 57¢ | ❌ Lost | -$1.51 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
