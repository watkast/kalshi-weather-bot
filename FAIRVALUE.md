# Fair-Value Bot

*Updated Mon Sep 28, 5:48 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 690 | $101.49 | +3% | $142.48 / -$40.99 |
| 4¢+ ← live bot | 665 | $251.66 | +8% | $200.89 / $50.77 |
| 6¢+ | 620 | $290.79 | +11% | $135.53 / $155.26 |
| 8¢+ | 552 | $367.88 | +17% | $58.60 / $309.28 |
| 10¢+ | 477 | $294.38 | +16% | $100.29 / $194.09 |
| 15¢+ | 290 | $243.72 | +25% | $118.52 / $125.20 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 686 | 678 | 347 (51%) | 45¢ | 53% | $331.32 | +11% | +8.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 276 | 121 (44%) | 76 / 200 | 8.4 | -$37.76 | -$89.59 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 244 | 88 (36%) | 104 / 140 | 7.4 | -$55.90 | -$137.18 | -13% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 61 | 16 (26%) | 24 / 37 | 2.0 | -$14.97 | -$61.78 | -28% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 63 | 23 (37%) | 18 / 45 | 2.0 | -$13.69 | -$51.12 | -18% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 12 | 6 (50%) | 2 / 10 | 1.2 | -$3.46 | $5.26 | +11% |

*Model accuracy vs Kalshi's prices on the same 6,767 readings (excluding the final minute): V1 **+4.0%**, V2 **+4.0%**, 3-exchange price (V3/V4) **+2.0%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 284 | 156 (55%) | -$73.19 | -10% | 74 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.7%** over 18,085 readings from 702 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3239 | 2% | 4% | 6% |
| 10–20% | 1367 | 15% | 16% | 16% |
| 20–30% | 1600 | 25% | 26% | 26% |
| 30–40% | 1749 | 35% | 36% | 39% |
| 40–50% | 1779 | 45% | 48% | 52% |
| 50–60% | 1791 | 55% | 59% | 58% |
| 60–70% | 1534 | 65% | 71% | 67% |
| 70–80% | 1304 | 75% | 80% | 78% |
| 80–90% | 1152 | 85% | 88% | 80% |
| 90–100% | 2570 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 398 | 207 (52%) | 45¢ | 52% | $203.85 | +11% |
| 6–10¢ | 214 | 111 (52%) | 44¢ | 53% | $130.41 | +13% |
| 10–20¢ | 61 | 27 (44%) | 43¢ | 57% | -$2.54 | -1% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 651 | 338 (52%) | 45¢ | 53% | $335.30 | +11% |
| 5–10 min | 26 | 8 (31%) | 31¢ | 39% | -$5.01 | -6% |
| 2–5 min | 1 | 1 (100%) | 89¢ | 94% | $1.03 | +11% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 67 | 15 (22%) | 19¢ | 26% | $18.40 | +14% |
| Toss-up (25–75¢) | 576 | 303 (53%) | 46¢ | 54% | $304.59 | +11% |
| Favorite (75–95¢) | 35 | 29 (83%) | 79¢ | 86% | $8.33 | +3% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| XRP | 76 | 42 (55%) | 47¢ | 54% | $54.24 | +15% |
| NEAR | 76 | 41 (54%) | 47¢ | 55% | $39.89 | +11% |
| ETH | 76 | 33 (43%) | 45¢ | 53% | -$23.34 | -7% |
| BNB | 76 | 42 (55%) | 43¢ | 53% | $77.15 | +23% |
| HYPE | 76 | 34 (45%) | 41¢ | 50% | $15.48 | +5% |
| BTC | 76 | 40 (53%) | 48¢ | 56% | $21.38 | +6% |
| SOL | 75 | 40 (53%) | 44¢ | 51% | $61.52 | +18% |
| DOGE | 74 | 39 (53%) | 45¢ | 53% | $46.22 | +13% |
| ZEC | 73 | 36 (49%) | 42¢ | 51% | $38.78 | +12% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 5:47:18 PM | XRP | UP | 12.7 min | 50¢ | 57% | 5¢ | Open | — |
| 9/28 5:47:10 PM | DOGE | DOWN | 12.8 min | 53¢ | 62% | 8¢ | Open | — |
| 9/28 5:46:35 PM | SOL | DOWN | 13.4 min | 67¢ | 79% | 10¢ | Open | — |
| 9/28 5:46:35 PM | HYPE | DOWN | 13.4 min | 74¢ | 82% | 7¢ | Open | — |
| 9/28 5:46:28 PM | ETH | DOWN | 13.5 min | 78¢ | 88% | 8¢ | Open | — |
| 9/28 5:46:13 PM | BTC | DOWN | 13.8 min | 74¢ | 83% | 7¢ | Open | — |
| 9/28 5:46:13 PM | BNB | UP | 13.8 min | 28¢ | 42% | 13¢ | Open | — |
| 9/28 5:46:13 PM | NEAR | DOWN | 13.8 min | 70¢ | 76% | 4¢ | Open | — |
| 9/28 5:40:18 PM | SOL | DOWN | 4.7 min | 89¢ | 94% | 4¢ | ✅ Won | $1.03 |
| 9/28 5:38:57 PM | BTC | DOWN | 6.0 min | 37¢ | 45% | 6¢ | ❌ Lost | -$3.87 |
| 9/28 5:37:04 PM | XRP | UP | 7.9 min | 36¢ | 42% | 4¢ | ❌ Lost | -$3.77 |
| 9/28 5:32:09 PM | HYPE | DOWN | 12.8 min | 62¢ | 68% | 5¢ | ✅ Won | $3.63 |
| 9/28 5:31:54 PM | DOGE | DOWN | 13.1 min | 48¢ | 54% | 4¢ | ❌ Lost | -$4.98 |
| 9/28 5:31:32 PM | ETH | DOWN | 13.4 min | 52¢ | 58% | 4¢ | ❌ Lost | -$5.38 |
| 9/28 5:31:09 PM | BNB | DOWN | 13.8 min | 36¢ | 51% | 13¢ | ❌ Lost | -$3.77 |
| 9/28 5:31:09 PM | NEAR | DOWN | 13.8 min | 44¢ | 51% | 5¢ | ✅ Won | $5.42 |
| 9/28 5:20:34 PM | BTC | DOWN | 9.4 min | 16¢ | 25% | 8¢ | ❌ Lost | -$1.70 |
| 9/28 5:18:31 PM | XRP | UP | 11.5 min | 77¢ | 83% | 5¢ | ✅ Won | $2.17 |
| 9/28 5:17:56 PM | ETH | DOWN | 12.1 min | 24¢ | 32% | 6¢ | ❌ Lost | -$2.53 |
| 9/28 5:16:31 PM | NEAR | DOWN | 13.5 min | 34¢ | 44% | 8¢ | ❌ Lost | -$3.56 |
| 9/28 5:16:23 PM | HYPE | DOWN | 13.6 min | 18¢ | 28% | 9¢ | ❌ Lost | -$1.91 |
| 9/28 5:16:13 PM | BNB | DOWN | 13.8 min | 35¢ | 49% | 12¢ | ❌ Lost | -$3.66 |
| 9/28 5:05:28 PM | ZEC | DOWN | 9.5 min | 19¢ | 24% | 4¢ | ❌ Lost | -$1.99 |
| 9/28 5:03:02 PM | XRP | UP | 11.9 min | 92¢ | 97% | 5¢ | ❌ Lost | -$9.22 |
| 9/28 5:03:02 PM | BTC | UP | 11.9 min | 80¢ | 86% | 5¢ | ❌ Lost | -$8.12 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
