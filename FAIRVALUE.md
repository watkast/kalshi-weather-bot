# Fair-Value Bot

*Updated Mon Sep 28, 3:46 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 618 | $169.74 | +6% | $163.46 / $6.28 |
| 4¢+ ← live bot | 597 | $267.52 | +10% | $243.13 / $24.39 |
| 6¢+ | 558 | $305.17 | +13% | $148.20 / $156.97 |
| 8¢+ | 496 | $340.69 | +18% | $101.93 / $238.76 |
| 10¢+ | 432 | $255.75 | +16% | $100.53 / $155.22 |
| 15¢+ | 261 | $227.46 | +27% | $84.97 / $142.49 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 613 | 612 | 323 (53%) | 45¢ | 53% | $408.38 | +14% | +9.7¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 210 | 97 (46%) | 62 / 148 | 8.4 | -$37.76 | -$12.53 | -1% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 187 | 67 (36%) | 85 / 102 | 7.5 | -$55.90 | -$87.43 | -12% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 45 | 11 (24%) | 18 / 27 | 2.0 | -$11.65 | -$38.53 | -26% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 73% of orders | 47 | 18 (38%) | 16 / 31 | 2.0 | -$13.69 | -$32.79 | -15% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 3 | 2 (67%) | 1 / 2 | 1.5 | -$0.34 | $6.06 | +52% |

*Model accuracy vs Kalshi's prices on the same 5,099 readings (excluding the final minute): V1 **+5.5%**, V2 **+5.4%**, 3-exchange price (V3/V4) **+3.3%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 218 | 90 (41%) | $3.87 | +1% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+6.0%** over 16,285 readings from 630 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2968 | 2% | 4% | 7% |
| 10–20% | 1277 | 15% | 16% | 17% |
| 20–30% | 1476 | 25% | 25% | 28% |
| 30–40% | 1659 | 35% | 36% | 40% |
| 40–50% | 1629 | 45% | 48% | 51% |
| 50–60% | 1589 | 55% | 59% | 55% |
| 60–70% | 1393 | 65% | 71% | 65% |
| 70–80% | 1145 | 75% | 80% | 77% |
| 80–90% | 982 | 85% | 88% | 79% |
| 90–100% | 2167 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 371 | 197 (53%) | 45¢ | 51% | $245.11 | +14% |
| 6–10¢ | 186 | 100 (54%) | 44¢ | 53% | $150.53 | +18% |
| 10–20¢ | 50 | 24 (48%) | 44¢ | 58% | $13.14 | +6% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 594 | 317 (53%) | 45¢ | 53% | $403.29 | +15% |
| 5–10 min | 18 | 6 (33%) | 29¢ | 38% | $5.09 | +9% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 60 | 15 (25%) | 18¢ | 26% | $32.54 | +28% |
| Toss-up (25–75¢) | 525 | 285 (54%) | 46¢ | 54% | $361.57 | +15% |
| Favorite (75–95¢) | 27 | 23 (85%) | 79¢ | 86% | $14.27 | +7% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BTC | 69 | 37 (54%) | 48¢ | 56% | $29.66 | +9% |
| SOL | 68 | 37 (54%) | 43¢ | 51% | $64.03 | +21% |
| ZEC | 68 | 35 (51%) | 43¢ | 51% | $45.40 | +15% |
| XRP | 68 | 38 (56%) | 45¢ | 52% | $64.79 | +21% |
| NEAR | 68 | 39 (57%) | 47¢ | 55% | $58.20 | +18% |
| ETH | 68 | 29 (43%) | 45¢ | 52% | -$23.78 | -8% |
| BNB | 68 | 39 (57%) | 43¢ | 53% | $83.71 | +27% |
| HYPE | 68 | 33 (49%) | 42¢ | 51% | $32.27 | +11% |
| DOGE | 67 | 36 (54%) | 44¢ | 52% | $54.10 | +18% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 3:46:15 PM | ZEC | UP | 13.8 min | 36¢ | 47% | 10¢ | Open | — |
| 9/28 3:39:36 PM | SOL | UP | 5.4 min | 12¢ | 18% | 5¢ | ❌ Lost | -$1.28 |
| 9/28 3:36:51 PM | BTC | UP | 8.1 min | 59¢ | 65% | 4¢ | ❌ Lost | -$6.07 |
| 9/28 3:35:11 PM | XRP | DOWN | 9.8 min | 36¢ | 42% | 4¢ | ✅ Won | $6.21 |
| 9/28 3:34:44 PM | DOGE | DOWN | 10.2 min | 44¢ | 53% | 8¢ | ✅ Won | $5.42 |
| 9/28 3:34:27 PM | NEAR | DOWN | 10.6 min | 32¢ | 40% | 7¢ | ✅ Won | $6.64 |
| 9/28 3:33:03 PM | HYPE | DOWN | 11.9 min | 45¢ | 52% | 5¢ | ✅ Won | $5.32 |
| 9/28 3:31:36 PM | ZEC | DOWN | 13.4 min | 46¢ | 52% | 5¢ | ❌ Lost | -$4.76 |
| 9/28 3:31:21 PM | ETH | UP | 13.7 min | 51¢ | 60% | 7¢ | ❌ Lost | -$5.28 |
| 9/28 3:31:07 PM | BNB | DOWN | 13.9 min | 38¢ | 46% | 6¢ | ✅ Won | $6.05 |
| 9/28 3:20:17 PM | ZEC | DOWN | 9.7 min | 25¢ | 42% | 15¢ | ✅ Won | $7.36 |
| 9/28 3:19:47 PM | XRP | DOWN | 10.2 min | 67¢ | 77% | 8¢ | ✅ Won | $3.14 |
| 9/28 3:19:47 PM | NEAR | DOWN | 10.2 min | 65¢ | 72% | 5¢ | ✅ Won | $3.34 |
| 9/28 3:18:24 PM | BTC | DOWN | 11.6 min | 80¢ | 86% | 5¢ | ✅ Won | $1.88 |
| 9/28 3:17:48 PM | BNB | UP | 12.2 min | 18¢ | 26% | 7¢ | ❌ Lost | -$1.91 |
| 9/28 3:17:18 PM | HYPE | DOWN | 12.7 min | 82¢ | 89% | 6¢ | ✅ Won | $1.65 |
| 9/28 3:17:10 PM | ETH | UP | 12.8 min | 28¢ | 34% | 4¢ | ❌ Lost | -$2.95 |
| 9/28 3:01:22 PM | SOL | DOWN | 13.6 min | 17¢ | 22% | 4¢ | ✅ Won | $8.20 |
| 9/28 3:01:22 PM | BTC | UP | 13.6 min | 74¢ | 80% | 4¢ | ✅ Won | $2.46 |
| 9/28 3:01:14 PM | BNB | DOWN | 13.8 min | 22¢ | 41% | 18¢ | ✅ Won | $7.67 |
| 9/28 3:01:14 PM | HYPE | DOWN | 13.8 min | 24¢ | 33% | 7¢ | ✅ Won | $7.47 |
| 9/28 2:48:01 PM | BNB | UP | 12.0 min | 34¢ | 40% | 5¢ | ✅ Won | $6.44 |
| 9/28 2:46:58 PM | SOL | DOWN | 13.0 min | 46¢ | 53% | 6¢ | ❌ Lost | -$4.78 |
| 9/28 2:46:58 PM | HYPE | DOWN | 13.0 min | 37¢ | 48% | 9¢ | ❌ Lost | -$3.87 |
| 9/28 2:46:58 PM | XRP | DOWN | 13.0 min | 48¢ | 55% | 5¢ | ❌ Lost | -$4.98 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
