# Fair-Value Bot

*Updated Mon Sep 28, 1:55 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **6¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **6¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 547 | $172.80 | +7% | $189.66 / -$16.86 |
| 4¢+ ← live bot | 528 | $212.17 | +9% | $253.33 / -$41.16 |
| 6¢+ | 493 | $213.35 | +10% | $190.29 / $23.06 |
| 8¢+ | 438 | $205.92 | +12% | $120.11 / $85.81 |
| 10¢+ | 382 | $169.16 | +12% | $109.65 / $59.51 |
| 15¢+ | 229 | $152.64 | +21% | $110.89 / $41.75 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 556 | 547 | 287 (52%) | 45¢ | 53% | $340.99 | +13% | +10.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 145 | 61 (42%) | 42 / 103 | 8.5 | -$37.76 | -$79.92 | -12% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 125 | 38 (30%) | 62 / 63 | 7.4 | -$55.90 | -$138.64 | -27% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 32 | 7 (22%) | 16 / 16 | 2.0 | -$8.62 | -$33.57 | -32% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 32 | 10 (31%) | 12 / 20 | 2.0 | -$10.20 | -$38.82 | -28% |

*Model accuracy vs Kalshi's prices on the same 3,447 readings (excluding the final minute): V1 **+3.9%**, V2 **+3.8%**, 3-exchange price (V3/V4) **-0.7%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 153 | 54 (35%) | -$40.75 | -17% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.4%** over 14,507 readings from 558 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2728 | 2% | 4% | 7% |
| 10–20% | 1177 | 15% | 16% | 18% |
| 20–30% | 1340 | 25% | 25% | 28% |
| 30–40% | 1443 | 35% | 36% | 40% |
| 40–50% | 1408 | 45% | 47% | 52% |
| 50–60% | 1363 | 55% | 59% | 58% |
| 60–70% | 1248 | 65% | 70% | 68% |
| 70–80% | 1021 | 75% | 80% | 80% |
| 80–90% | 845 | 85% | 88% | 84% |
| 90–100% | 1934 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 336 | 179 (53%) | 45¢ | 51% | $224.65 | +14% |
| 6–10¢ | 166 | 86 (52%) | 44¢ | 53% | $95.97 | +13% |
| 10–20¢ | 40 | 20 (50%) | 43¢ | 57% | $20.77 | +12% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 536 | 285 (53%) | 45¢ | 53% | $345.92 | +14% |
| 5–10 min | 11 | 2 (18%) | 22¢ | 30% | -$4.93 | -20% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 53 | 11 (21%) | 18¢ | 25% | $7.25 | +7% |
| Toss-up (25–75¢) | 470 | 255 (54%) | 46¢ | 54% | $314.88 | +14% |
| Favorite (75–95¢) | 24 | 21 (88%) | 78¢ | 85% | $18.86 | +10% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 61 | 34 (56%) | 45¢ | 53% | $56.33 | +20% |
| ZEC | 61 | 33 (54%) | 43¢ | 51% | $57.41 | +21% |
| XRP | 61 | 33 (54%) | 45¢ | 53% | $45.97 | +16% |
| NEAR | 61 | 35 (57%) | 47¢ | 55% | $52.96 | +18% |
| ETH | 61 | 27 (44%) | 44¢ | 52% | -$9.89 | -4% |
| DOGE | 61 | 31 (51%) | 45¢ | 52% | $28.10 | +10% |
| BTC | 61 | 34 (56%) | 47¢ | 55% | $44.13 | +15% |
| BNB | 60 | 33 (55%) | 44¢ | 53% | $54.99 | +20% |
| HYPE | 60 | 27 (45%) | 42¢ | 50% | $10.99 | +4% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 1:49:24 PM | ZEC | UP | 10.6 min | 22¢ | 33% | 10¢ | Open | — |
| 9/28 1:48:04 PM | ETH | DOWN | 11.9 min | 40¢ | 50% | 8¢ | Open | — |
| 9/28 1:46:30 PM | BTC | DOWN | 13.5 min | 30¢ | 38% | 7¢ | Open | — |
| 9/28 1:46:30 PM | SOL | DOWN | 13.5 min | 28¢ | 35% | 5¢ | Open | — |
| 9/28 1:46:17 PM | DOGE | DOWN | 13.7 min | 27¢ | 33% | 4¢ | Open | — |
| 9/28 1:46:17 PM | NEAR | DOWN | 13.7 min | 36¢ | 43% | 5¢ | Open | — |
| 9/28 1:46:17 PM | BNB | DOWN | 13.7 min | 32¢ | 42% | 9¢ | Open | — |
| 9/28 1:46:17 PM | HYPE | DOWN | 13.7 min | 25¢ | 32% | 6¢ | Open | — |
| 9/28 1:46:02 PM | XRP | DOWN | 14.0 min | 24¢ | 30% | 4¢ | Open | — |
| 9/28 1:35:37 PM | NEAR | DOWN | 9.4 min | 86¢ | 93% | 6¢ | ✅ Won | $1.31 |
| 9/28 1:32:17 PM | HYPE | DOWN | 12.7 min | 26¢ | 33% | 6¢ | ✅ Won | $7.26 |
| 9/28 1:31:53 PM | SOL | DOWN | 13.1 min | 49¢ | 57% | 6¢ | ✅ Won | $4.92 |
| 9/28 1:31:53 PM | ZEC | DOWN | 13.1 min | 32¢ | 40% | 6¢ | ✅ Won | $6.64 |
| 9/28 1:31:22 PM | DOGE | DOWN | 13.6 min | 55¢ | 61% | 4¢ | ✅ Won | $4.32 |
| 9/28 1:31:14 PM | BTC | DOWN | 13.8 min | 58¢ | 66% | 6¢ | ✅ Won | $4.02 |
| 9/28 1:31:14 PM | XRP | DOWN | 13.8 min | 60¢ | 67% | 5¢ | ✅ Won | $3.83 |
| 9/28 1:31:14 PM | ETH | DOWN | 13.8 min | 61¢ | 68% | 5¢ | ✅ Won | $3.73 |
| 9/28 1:31:14 PM | BNB | DOWN | 13.8 min | 51¢ | 63% | 11¢ | ✅ Won | $4.72 |
| 9/28 1:17:38 PM | ZEC | UP | 12.4 min | 25¢ | 31% | 5¢ | ❌ Lost | -$2.64 |
| 9/28 1:17:02 PM | DOGE | DOWN | 12.9 min | 68¢ | 74% | 4¢ | ✅ Won | $3.04 |
| 9/28 1:16:55 PM | ETH | DOWN | 13.1 min | 60¢ | 67% | 6¢ | ✅ Won | $3.83 |
| 9/28 1:16:42 PM | HYPE | UP | 13.3 min | 35¢ | 41% | 4¢ | ❌ Lost | -$3.66 |
| 9/28 1:16:33 PM | SOL | DOWN | 13.4 min | 53¢ | 60% | 5¢ | ✅ Won | $4.52 |
| 9/28 1:16:33 PM | BTC | DOWN | 13.4 min | 51¢ | 60% | 7¢ | ✅ Won | $4.72 |
| 9/28 1:16:33 PM | NEAR | DOWN | 13.4 min | 32¢ | 45% | 11¢ | ❌ Lost | -$3.36 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
