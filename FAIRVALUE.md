# Fair-Value Bot

*Updated Mon Sep 28, 3:36 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 609 | $151.61 | +5% | $151.72 / -$0.11 |
| 4¢+ ← live bot | 588 | $237.09 | +9% | $231.37 / $5.72 |
| 6¢+ | 550 | $269.02 | +12% | $157.45 / $111.57 |
| 8¢+ | 488 | $295.42 | +16% | $94.14 / $201.28 |
| 10¢+ | 428 | $231.81 | +15% | $95.37 / $136.44 |
| 15¢+ | 258 | $207.07 | +25% | $91.44 / $115.63 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 610 | 603 | 318 (53%) | 45¢ | 53% | $396.13 | +14% | +10.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 201 | 92 (46%) | 59 / 142 | 8.4 | -$37.76 | -$24.78 | -3% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 178 | 59 (33%) | 85 / 93 | 7.4 | -$55.90 | -$125.80 | -18% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 43 | 9 (21%) | 18 / 25 | 2.0 | -$11.65 | -$53.98 | -37% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 72% of orders | 45 | 17 (38%) | 15 / 30 | 2.0 | -$13.69 | -$32.39 | -16% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 1 | 1 (100%) | 0 / 1 | 1.0 | $6.40 | $6.40 | +242% |

*Model accuracy vs Kalshi's prices on the same 4,888 readings (excluding the final minute): V1 **+5.1%**, V2 **+4.7%**, 3-exchange price (V3/V4) **+2.7%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 209 | 81 (39%) | -$8.38 | -2% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.8%** over 16,065 readings from 621 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2923 | 2% | 4% | 7% |
| 10–20% | 1264 | 15% | 16% | 17% |
| 20–30% | 1458 | 25% | 25% | 29% |
| 30–40% | 1630 | 35% | 36% | 40% |
| 40–50% | 1592 | 45% | 48% | 52% |
| 50–60% | 1555 | 55% | 59% | 56% |
| 60–70% | 1379 | 65% | 71% | 66% |
| 70–80% | 1134 | 75% | 80% | 77% |
| 80–90% | 978 | 85% | 88% | 79% |
| 90–100% | 2152 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 366 | 195 (53%) | 45¢ | 51% | $245.69 | +14% |
| 6–10¢ | 182 | 97 (53%) | 44¢ | 53% | $137.70 | +17% |
| 10–20¢ | 50 | 24 (48%) | 44¢ | 58% | $13.14 | +6% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 588 | 313 (53%) | 45¢ | 53% | $389.90 | +14% |
| 5–10 min | 15 | 5 (33%) | 28¢ | 37% | $6.23 | +14% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 59 | 15 (25%) | 19¢ | 26% | $33.82 | +29% |
| Toss-up (25–75¢) | 517 | 280 (54%) | 46¢ | 54% | $348.04 | +14% |
| Favorite (75–95¢) | 27 | 23 (85%) | 79¢ | 86% | $14.27 | +7% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BTC | 68 | 37 (54%) | 48¢ | 55% | $35.73 | +11% |
| SOL | 67 | 37 (55%) | 44¢ | 51% | $65.31 | +21% |
| ZEC | 67 | 35 (52%) | 43¢ | 51% | $50.16 | +17% |
| XRP | 67 | 37 (55%) | 45¢ | 53% | $58.58 | +19% |
| NEAR | 67 | 38 (57%) | 47¢ | 55% | $51.56 | +16% |
| ETH | 67 | 29 (43%) | 44¢ | 52% | -$18.50 | -6% |
| BNB | 67 | 38 (57%) | 43¢ | 53% | $77.66 | +26% |
| HYPE | 67 | 32 (48%) | 42¢ | 51% | $26.95 | +9% |
| DOGE | 66 | 35 (53%) | 44¢ | 52% | $48.68 | +16% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 3:35:11 PM | XRP | DOWN | 9.8 min | 36¢ | 42% | 4¢ | Open | — |
| 9/28 3:34:44 PM | DOGE | DOWN | 10.2 min | 44¢ | 53% | 8¢ | Open | — |
| 9/28 3:34:27 PM | NEAR | DOWN | 10.6 min | 32¢ | 40% | 7¢ | Open | — |
| 9/28 3:33:03 PM | HYPE | DOWN | 11.9 min | 45¢ | 52% | 5¢ | Open | — |
| 9/28 3:31:36 PM | ZEC | DOWN | 13.4 min | 46¢ | 52% | 5¢ | Open | — |
| 9/28 3:31:21 PM | ETH | UP | 13.7 min | 51¢ | 60% | 7¢ | Open | — |
| 9/28 3:31:07 PM | BNB | DOWN | 13.9 min | 38¢ | 46% | 6¢ | Open | — |
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
| 9/28 2:46:38 PM | ZEC | UP | 13.4 min | 56¢ | 63% | 5¢ | ❌ Lost | -$5.78 |
| 9/28 2:46:25 PM | DOGE | UP | 13.6 min | 41¢ | 50% | 8¢ | ✅ Won | $5.73 |
| 9/28 2:46:25 PM | ETH | UP | 13.6 min | 49¢ | 55% | 5¢ | ✅ Won | $4.92 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
