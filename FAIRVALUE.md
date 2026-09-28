# Fair-Value Bot

*Updated Mon Sep 28, 3:26 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 601 | $147.87 | +5% | $162.43 / -$14.56 |
| 4¢+ ← live bot | 581 | $218.50 | +8% | $240.83 / -$22.33 |
| 6¢+ | 544 | $250.84 | +11% | $162.02 / $88.82 |
| 8¢+ | 486 | $291.46 | +16% | $87.60 / $203.86 |
| 10¢+ | 426 | $227.85 | +14% | $97.28 / $130.57 |
| 15¢+ | 258 | $207.07 | +25% | $91.44 / $115.63 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 603 | 596 | 313 (53%) | 44¢ | 53% | $383.62 | +14% | +10.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 194 | 87 (45%) | 57 / 137 | 8.4 | -$37.76 | -$37.29 | -4% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 173 | 58 (34%) | 81 / 92 | 7.5 | -$55.90 | -$122.38 | -17% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 42 | 9 (21%) | 17 / 25 | 2.0 | -$11.65 | -$53.03 | -37% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 73% of orders | 43 | 15 (35%) | 15 / 28 | 2.0 | -$13.69 | -$37.71 | -20% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 0 | — | 0 / 0 | — | — | — | — |

*Model accuracy vs Kalshi's prices on the same 4,681 readings (excluding the final minute): V1 **+4.6%**, V2 **+4.4%**, 3-exchange price (V3/V4) **+2.2%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 202 | 74 (37%) | -$20.89 | -7% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.6%** over 15,840 readings from 612 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2819 | 2% | 4% | 7% |
| 10–20% | 1226 | 15% | 16% | 18% |
| 20–30% | 1422 | 25% | 25% | 30% |
| 30–40% | 1598 | 35% | 36% | 41% |
| 40–50% | 1583 | 45% | 48% | 52% |
| 50–60% | 1551 | 55% | 59% | 56% |
| 60–70% | 1378 | 65% | 71% | 66% |
| 70–80% | 1134 | 75% | 80% | 77% |
| 80–90% | 977 | 85% | 88% | 79% |
| 90–100% | 2152 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 362 | 192 (53%) | 45¢ | 51% | $241.77 | +14% |
| 6–10¢ | 180 | 96 (53%) | 44¢ | 53% | $136.47 | +17% |
| 10–20¢ | 49 | 23 (47%) | 44¢ | 58% | $5.78 | +3% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 582 | 309 (53%) | 45¢ | 53% | $384.75 | +14% |
| 5–10 min | 14 | 4 (29%) | 28¢ | 36% | -$1.13 | -3% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 58 | 15 (26%) | 19¢ | 26% | $35.73 | +31% |
| Toss-up (25–75¢) | 513 | 277 (54%) | 46¢ | 54% | $337.15 | +14% |
| Favorite (75–95¢) | 25 | 21 (84%) | 78¢ | 86% | $10.74 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 67 | 37 (55%) | 44¢ | 51% | $65.31 | +21% |
| BTC | 67 | 36 (54%) | 47¢ | 55% | $33.85 | +10% |
| ZEC | 66 | 34 (52%) | 43¢ | 52% | $42.80 | +14% |
| XRP | 66 | 36 (55%) | 45¢ | 52% | $55.44 | +18% |
| NEAR | 66 | 37 (56%) | 47¢ | 55% | $48.22 | +15% |
| ETH | 66 | 29 (44%) | 45¢ | 52% | -$15.55 | -5% |
| BNB | 66 | 38 (58%) | 44¢ | 53% | $79.57 | +26% |
| DOGE | 66 | 35 (53%) | 44¢ | 52% | $48.68 | +16% |
| HYPE | 66 | 31 (47%) | 42¢ | 50% | $25.30 | +9% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 3:20:17 PM | ZEC | DOWN | 9.7 min | 25¢ | 42% | 15¢ | Open | — |
| 9/28 3:19:47 PM | XRP | DOWN | 10.2 min | 67¢ | 77% | 8¢ | Open | — |
| 9/28 3:19:47 PM | NEAR | DOWN | 10.2 min | 65¢ | 72% | 5¢ | Open | — |
| 9/28 3:18:24 PM | BTC | DOWN | 11.6 min | 80¢ | 86% | 5¢ | Open | — |
| 9/28 3:17:48 PM | BNB | UP | 12.2 min | 18¢ | 26% | 7¢ | Open | — |
| 9/28 3:17:18 PM | HYPE | DOWN | 12.7 min | 82¢ | 89% | 6¢ | Open | — |
| 9/28 3:17:10 PM | ETH | UP | 12.8 min | 28¢ | 34% | 4¢ | Open | — |
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
| 9/28 2:46:17 PM | NEAR | DOWN | 13.7 min | 39¢ | 47% | 6¢ | ✅ Won | $5.93 |
| 9/28 2:46:17 PM | BTC | DOWN | 13.7 min | 56¢ | 62% | 4¢ | ❌ Lost | -$5.78 |
| 9/28 2:37:20 PM | HYPE | DOWN | 7.7 min | 51¢ | 60% | 8¢ | ✅ Won | $4.72 |
| 9/28 2:36:58 PM | ZEC | DOWN | 8.0 min | 69¢ | 79% | 8¢ | ✅ Won | $2.95 |
| 9/28 2:34:35 PM | SOL | DOWN | 10.4 min | 40¢ | 47% | 6¢ | ✅ Won | $5.83 |
| 9/28 2:33:35 PM | ETH | UP | 11.4 min | 39¢ | 46% | 5¢ | ❌ Lost | -$4.07 |
| 9/28 2:33:00 PM | DOGE | DOWN | 12.0 min | 48¢ | 56% | 7¢ | ✅ Won | $5.02 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
