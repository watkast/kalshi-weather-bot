# Fair-Value Bot

*Updated Mon Sep 28, 4:27 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 636 | $190.88 | +6% | $163.83 / $27.05 |
| 4¢+ ← live bot | 614 | $297.03 | +11% | $240.26 / $56.77 |
| 6¢+ | 573 | $336.52 | +14% | $160.02 / $176.50 |
| 8¢+ | 510 | $371.75 | +19% | $97.70 / $274.05 |
| 10¢+ | 443 | $279.51 | +17% | $115.57 / $163.94 |
| 15¢+ | 267 | $240.37 | +27% | $94.91 / $145.46 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 639 | 630 | 335 (53%) | 45¢ | 53% | $426.69 | +15% | +9.5¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 228 | 109 (48%) | 68 / 160 | 8.4 | -$37.76 | $5.78 | +1% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 200 | 78 (39%) | 87 / 113 | 7.4 | -$55.90 | -$53.65 | -6% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 49 | 13 (27%) | 21 / 28 | 2.0 | -$11.65 | -$36.02 | -22% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 74% of orders | 51 | 20 (39%) | 18 / 33 | 2.0 | -$13.69 | -$31.47 | -14% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 6 | 4 (67%) | 2 / 4 | 1.5 | -$2.14 | $6.96 | +25% |

*Model accuracy vs Kalshi's prices on the same 5,513 readings (excluding the final minute): V1 **+6.2%**, V2 **+6.1%**, 3-exchange price (V3/V4) **+4.0%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 236 | 108 (46%) | $22.18 | +4% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+6.4%** over 16,731 readings from 648 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3167 | 2% | 4% | 6% |
| 10–20% | 1336 | 15% | 16% | 16% |
| 20–30% | 1545 | 25% | 25% | 27% |
| 30–40% | 1708 | 35% | 36% | 39% |
| 40–50% | 1660 | 45% | 47% | 51% |
| 50–60% | 1609 | 55% | 59% | 55% |
| 60–70% | 1402 | 65% | 71% | 65% |
| 70–80% | 1148 | 75% | 80% | 77% |
| 80–90% | 983 | 85% | 88% | 79% |
| 90–100% | 2173 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 379 | 202 (53%) | 45¢ | 52% | $250.76 | +14% |
| 6–10¢ | 193 | 106 (55%) | 45¢ | 54% | $166.37 | +19% |
| 10–20¢ | 53 | 25 (47%) | 44¢ | 58% | $9.96 | +4% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 610 | 327 (54%) | 45¢ | 53% | $415.31 | +15% |
| 5–10 min | 20 | 8 (40%) | 33¢ | 41% | $11.38 | +17% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 62 | 15 (24%) | 18¢ | 26% | $28.75 | +24% |
| Toss-up (25–75¢) | 537 | 293 (55%) | 46¢ | 54% | $375.47 | +15% |
| Favorite (75–95¢) | 31 | 27 (87%) | 79¢ | 86% | $22.47 | +9% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BTC | 71 | 39 (55%) | 48¢ | 56% | $37.02 | +10% |
| SOL | 70 | 38 (54%) | 43¢ | 51% | $65.62 | +21% |
| ZEC | 70 | 36 (51%) | 43¢ | 51% | $47.36 | +15% |
| XRP | 70 | 40 (57%) | 46¢ | 53% | $69.13 | +21% |
| NEAR | 70 | 40 (57%) | 47¢ | 55% | $56.64 | +16% |
| ETH | 70 | 31 (44%) | 45¢ | 53% | -$19.25 | -6% |
| BNB | 70 | 40 (57%) | 44¢ | 53% | $83.27 | +26% |
| HYPE | 70 | 33 (47%) | 42¢ | 50% | $28.17 | +9% |
| DOGE | 69 | 38 (55%) | 45¢ | 53% | $58.73 | +18% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 4:18:20 PM | HYPE | DOWN | 11.7 min | 32¢ | 41% | 8¢ | Open | — |
| 9/28 4:18:13 PM | NEAR | DOWN | 11.8 min | 38¢ | 46% | 7¢ | Open | — |
| 9/28 4:17:44 PM | SOL | DOWN | 12.3 min | 33¢ | 43% | 8¢ | Open | — |
| 9/28 4:17:29 PM | ETH | DOWN | 12.5 min | 38¢ | 49% | 9¢ | Open | — |
| 9/28 4:17:29 PM | DOGE | DOWN | 12.5 min | 45¢ | 53% | 6¢ | Open | — |
| 9/28 4:17:29 PM | BNB | DOWN | 12.5 min | 49¢ | 60% | 9¢ | Open | — |
| 9/28 4:17:14 PM | XRP | DOWN | 12.8 min | 43¢ | 55% | 10¢ | Open | — |
| 9/28 4:17:07 PM | ZEC | DOWN | 12.9 min | 29¢ | 35% | 5¢ | Open | — |
| 9/28 4:16:06 PM | BTC | DOWN | 13.9 min | 63¢ | 71% | 6¢ | Open | — |
| 9/28 4:02:35 PM | NEAR | DOWN | 12.4 min | 55¢ | 61% | 4¢ | ❌ Lost | -$5.68 |
| 9/28 4:02:26 PM | HYPE | UP | 12.6 min | 12¢ | 18% | 5¢ | ❌ Lost | -$1.26 |
| 9/28 4:02:26 PM | ZEC | UP | 12.6 min | 41¢ | 48% | 5¢ | ❌ Lost | -$4.29 |
| 9/28 4:02:01 PM | SOL | DOWN | 13.0 min | 57¢ | 63% | 4¢ | ✅ Won | $4.12 |
| 9/28 4:01:55 PM | ETH | DOWN | 13.1 min | 75¢ | 81% | 5¢ | ✅ Won | $2.36 |
| 9/28 4:01:33 PM | BNB | DOWN | 13.4 min | 62¢ | 72% | 8¢ | ✅ Won | $3.63 |
| 9/28 4:01:13 PM | BTC | DOWN | 13.8 min | 61¢ | 74% | 12¢ | ✅ Won | $3.73 |
| 9/28 4:01:13 PM | XRP | DOWN | 13.8 min | 72¢ | 79% | 6¢ | ✅ Won | $2.65 |
| 9/28 4:01:13 PM | DOGE | DOWN | 13.8 min | 79¢ | 87% | 7¢ | ✅ Won | $1.98 |
| 9/28 3:50:50 PM | ETH | DOWN | 9.2 min | 77¢ | 85% | 6¢ | ✅ Won | $2.17 |
| 9/28 3:50:17 PM | NEAR | DOWN | 9.7 min | 57¢ | 65% | 6¢ | ✅ Won | $4.12 |
| 9/28 3:48:38 PM | BTC | DOWN | 11.4 min | 62¢ | 68% | 4¢ | ✅ Won | $3.63 |
| 9/28 3:48:38 PM | XRP | DOWN | 11.4 min | 82¢ | 89% | 6¢ | ✅ Won | $1.69 |
| 9/28 3:47:22 PM | DOGE | DOWN | 12.6 min | 72¢ | 81% | 8¢ | ✅ Won | $2.65 |
| 9/28 3:47:08 PM | SOL | UP | 12.8 min | 24¢ | 32% | 7¢ | ❌ Lost | -$2.53 |
| 9/28 3:47:01 PM | HYPE | UP | 13.0 min | 27¢ | 39% | 10¢ | ❌ Lost | -$2.84 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
