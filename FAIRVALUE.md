# Fair-Value Bot

*Updated Mon Sep 28, 5:07 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 663 | $103.17 | +3% | $113.85 / -$10.68 |
| 4¢+ ← live bot | 640 | $243.08 | +8% | $200.43 / $42.65 |
| 6¢+ | 596 | $286.39 | +11% | $129.74 / $156.65 |
| 8¢+ | 531 | $330.46 | +16% | $90.43 / $240.03 |
| 10¢+ | 458 | $255.61 | +15% | $111.83 / $143.78 |
| 15¢+ | 276 | $238.39 | +26% | $104.35 / $134.04 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 664 | 655 | 339 (52%) | 45¢ | 53% | $357.49 | +12% | +8.7¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 253 | 113 (45%) | 72 / 181 | 8.4 | -$37.76 | -$63.42 | -5% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 222 | 85 (38%) | 94 / 128 | 7.4 | -$55.90 | -$85.46 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 55 | 14 (25%) | 21 / 34 | 2.0 | -$11.65 | -$47.32 | -25% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 57 | 20 (35%) | 18 / 39 | 2.0 | -$13.69 | -$59.76 | -23% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 9 | 5 (56%) | 2 / 7 | 1.3 | -$3.46 | $5.32 | +14% |

*Model accuracy vs Kalshi's prices on the same 6,138 readings (excluding the final minute): V1 **+4.8%**, V2 **+5.1%**, 3-exchange price (V3/V4) **+2.6%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 261 | 133 (51%) | -$47.02 | -8% | 26 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.9%** over 17,410 readings from 675 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3174 | 2% | 4% | 6% |
| 10–20% | 1341 | 15% | 16% | 16% |
| 20–30% | 1563 | 25% | 25% | 27% |
| 30–40% | 1731 | 35% | 36% | 39% |
| 40–50% | 1737 | 45% | 48% | 52% |
| 50–60% | 1730 | 55% | 59% | 58% |
| 60–70% | 1480 | 65% | 71% | 67% |
| 70–80% | 1217 | 75% | 80% | 78% |
| 80–90% | 1038 | 85% | 88% | 80% |
| 90–100% | 2399 | 98% | 98% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 385 | 202 (52%) | 45¢ | 51% | $226.67 | +13% |
| 6–10¢ | 208 | 110 (53%) | 45¢ | 54% | $138.76 | +14% |
| 10–20¢ | 57 | 25 (44%) | 44¢ | 58% | -$7.54 | -3% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 633 | 331 (52%) | 45¢ | 53% | $351.17 | +12% |
| 5–10 min | 22 | 8 (36%) | 32¢ | 40% | $6.32 | +9% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 63 | 15 (24%) | 19¢ | 26% | $26.53 | +21% |
| Toss-up (25–75¢) | 561 | 297 (53%) | 46¢ | 54% | $308.49 | +12% |
| Favorite (75–95¢) | 31 | 27 (87%) | 79¢ | 86% | $22.47 | +9% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 73 | 38 (52%) | 43¢ | 51% | $53.74 | +16% |
| XRP | 73 | 41 (56%) | 46¢ | 53% | $65.06 | +19% |
| NEAR | 73 | 40 (55%) | 47¢ | 55% | $41.90 | +12% |
| ETH | 73 | 32 (44%) | 45¢ | 53% | -$22.07 | -6% |
| BNB | 73 | 41 (56%) | 44¢ | 53% | $79.36 | +24% |
| HYPE | 73 | 33 (45%) | 41¢ | 50% | $18.14 | +6% |
| BTC | 73 | 40 (55%) | 48¢ | 56% | $35.07 | +10% |
| ZEC | 72 | 36 (50%) | 43¢ | 51% | $40.77 | +13% |
| DOGE | 72 | 38 (53%) | 45¢ | 53% | $45.52 | +14% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 5:05:28 PM | ZEC | DOWN | 9.5 min | 19¢ | 24% | 4¢ | Open | — |
| 9/28 5:03:02 PM | XRP | UP | 11.9 min | 92¢ | 97% | 5¢ | Open | — |
| 9/28 5:03:02 PM | BTC | UP | 11.9 min | 80¢ | 86% | 5¢ | Open | — |
| 9/28 5:02:26 PM | ETH | DOWN | 12.6 min | 32¢ | 38% | 4¢ | Open | — |
| 9/28 5:01:44 PM | HYPE | DOWN | 13.3 min | 42¢ | 49% | 5¢ | Open | — |
| 9/28 5:01:08 PM | NEAR | DOWN | 13.8 min | 37¢ | 44% | 5¢ | Open | — |
| 9/28 5:01:08 PM | SOL | DOWN | 13.8 min | 31¢ | 44% | 11¢ | Open | — |
| 9/28 5:01:08 PM | DOGE | DOWN | 13.8 min | 42¢ | 58% | 15¢ | Open | — |
| 9/28 5:01:08 PM | BNB | DOWN | 13.8 min | 46¢ | 55% | 7¢ | Open | — |
| 9/28 4:51:30 PM | HYPE | UP | 8.5 min | 21¢ | 26% | 4¢ | ❌ Lost | -$2.22 |
| 9/28 4:50:54 PM | SOL | DOWN | 9.1 min | 27¢ | 35% | 7¢ | ❌ Lost | -$2.84 |
| 9/28 4:47:14 PM | ZEC | DOWN | 12.8 min | 34¢ | 42% | 6¢ | ❌ Lost | -$3.56 |
| 9/28 4:47:06 PM | XRP | UP | 12.9 min | 40¢ | 50% | 8¢ | ✅ Won | $5.83 |
| 9/28 4:47:06 PM | BTC | UP | 12.9 min | 53¢ | 65% | 10¢ | ✅ Won | $4.52 |
| 9/28 4:47:06 PM | ETH | UP | 12.9 min | 49¢ | 57% | 6¢ | ✅ Won | $4.92 |
| 9/28 4:46:52 PM | DOGE | DOWN | 13.1 min | 41¢ | 47% | 4¢ | ❌ Lost | -$4.26 |
| 9/28 4:46:19 PM | NEAR | DOWN | 13.7 min | 48¢ | 56% | 6¢ | ❌ Lost | -$5.00 |
| 9/28 4:46:11 PM | BNB | DOWN | 13.8 min | 37¢ | 45% | 7¢ | ❌ Lost | -$3.85 |
| 9/28 4:34:37 PM | NEAR | DOWN | 10.4 min | 56¢ | 64% | 7¢ | ❌ Lost | -$5.77 |
| 9/28 4:32:33 PM | SOL | DOWN | 12.4 min | 54¢ | 65% | 10¢ | ❌ Lost | -$5.58 |
| 9/28 4:32:33 PM | ETH | DOWN | 12.4 min | 36¢ | 49% | 12¢ | ❌ Lost | -$3.77 |
| 9/28 4:32:33 PM | DOGE | DOWN | 12.4 min | 41¢ | 58% | 15¢ | ❌ Lost | -$4.27 |
| 9/28 4:32:24 PM | XRP | DOWN | 12.6 min | 52¢ | 59% | 5¢ | ❌ Lost | -$5.42 |
| 9/28 4:31:38 PM | HYPE | DOWN | 13.4 min | 43¢ | 49% | 4¢ | ❌ Lost | -$4.48 |
| 9/28 4:31:17 PM | BNB | DOWN | 13.7 min | 48¢ | 61% | 11¢ | ❌ Lost | -$4.98 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
