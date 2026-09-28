# Fair-Value Bot

*Updated Mon Sep 28, 12:44 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 502 | $128.50 | +5% | $224.34 / -$95.84 |
| 4¢+ ← live bot | 487 | $161.22 | +7% | $299.47 / -$138.25 |
| 6¢+ | 459 | $183.63 | +10% | $224.08 / -$40.45 |
| 8¢+ | 413 | $190.81 | +13% | $147.38 / $43.43 |
| 10¢+ | 364 | $165.88 | +13% | $134.74 / $31.14 |
| 15¢+ | 226 | $159.69 | +22% | $114.55 / $45.14 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 511 | 502 | 258 (51%) | 44¢ | 52% | $296.91 | +13% | +10.9¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 100 | 32 (32%) | 35 / 65 | 8.3 | -$37.18 | -$124.00 | -28% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 94 | 21 (22%) | 57 / 37 | 7.8 | -$55.90 | -$157.68 | -43% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 24 | 4 (17%) | 13 / 11 | 2.0 | -$8.62 | -$31.18 | -44% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 22 | 5 (23%) | 9 / 13 | 2.0 | -$10.20 | -$37.57 | -43% |

*Model accuracy vs Kalshi's prices on the same 2,421 readings (excluding the final minute): V1 **-1.1%**, V2 **-0.8%**, 3-exchange price (V3/V4) **-5.4%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 108 | 43 (40%) | -$48.19 | -27% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.0%** over 13,398 readings from 513 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2225 | 2% | 4% | 8% |
| 10–20% | 1055 | 15% | 16% | 19% |
| 20–30% | 1228 | 25% | 25% | 30% |
| 30–40% | 1352 | 35% | 36% | 42% |
| 40–50% | 1340 | 45% | 47% | 53% |
| 50–60% | 1323 | 55% | 59% | 58% |
| 60–70% | 1227 | 65% | 70% | 68% |
| 70–80% | 991 | 75% | 80% | 80% |
| 80–90% | 830 | 85% | 88% | 83% |
| 90–100% | 1827 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 311 | 164 (53%) | 45¢ | 51% | $205.91 | +14% |
| 6–10¢ | 150 | 74 (49%) | 43¢ | 52% | $70.43 | +11% |
| 10–20¢ | 36 | 18 (50%) | 43¢ | 57% | $20.97 | +13% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 494 | 257 (52%) | 44¢ | 52% | $300.07 | +13% |
| 5–10 min | 8 | 1 (12%) | 16¢ | 24% | -$3.16 | -24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 48 | 11 (23%) | 18¢ | 26% | $16.06 | +17% |
| Toss-up (25–75¢) | 439 | 235 (54%) | 46¢ | 54% | $278.38 | +13% |
| Favorite (75–95¢) | 15 | 12 (80%) | 77¢ | 84% | $2.47 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 56 | 30 (54%) | 44¢ | 51% | $47.14 | +19% |
| ZEC | 56 | 29 (52%) | 42¢ | 50% | $43.97 | +18% |
| XRP | 56 | 29 (52%) | 44¢ | 51% | $36.56 | +14% |
| NEAR | 56 | 33 (59%) | 47¢ | 54% | $59.29 | +22% |
| ETH | 56 | 25 (45%) | 45¢ | 53% | -$11.12 | -4% |
| DOGE | 56 | 27 (48%) | 43¢ | 51% | $20.62 | +8% |
| BTC | 56 | 30 (54%) | 45¢ | 53% | $36.71 | +14% |
| BNB | 55 | 30 (55%) | 44¢ | 53% | $51.01 | +20% |
| HYPE | 55 | 25 (45%) | 42¢ | 50% | $12.73 | +5% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 12:38:38 PM | ETH | UP | 6.4 min | 7¢ | 13% | 5¢ | Open | — |
| 9/28 12:37:28 PM | HYPE | UP | 7.5 min | 22¢ | 30% | 6¢ | Open | — |
| 9/28 12:34:43 PM | NEAR | UP | 10.3 min | 12¢ | 17% | 4¢ | Open | — |
| 9/28 12:32:23 PM | SOL | DOWN | 12.6 min | 75¢ | 81% | 4¢ | Open | — |
| 9/28 12:32:15 PM | BNB | UP | 12.8 min | 20¢ | 27% | 6¢ | Open | — |
| 9/28 12:31:50 PM | BTC | DOWN | 13.2 min | 63¢ | 74% | 9¢ | Open | — |
| 9/28 12:31:20 PM | DOGE | DOWN | 13.7 min | 62¢ | 71% | 7¢ | Open | — |
| 9/28 12:31:10 PM | ZEC | DOWN | 13.8 min | 56¢ | 63% | 5¢ | Open | — |
| 9/28 12:31:10 PM | XRP | DOWN | 13.8 min | 48¢ | 56% | 6¢ | Open | — |
| 9/28 12:18:05 PM | ETH | DOWN | 11.9 min | 57¢ | 67% | 8¢ | ✅ Won | $4.12 |
| 9/28 12:18:05 PM | XRP | DOWN | 11.9 min | 41¢ | 49% | 6¢ | ✅ Won | $5.73 |
| 9/28 12:18:05 PM | BTC | DOWN | 11.9 min | 62¢ | 71% | 7¢ | ✅ Won | $3.63 |
| 9/28 12:16:51 PM | ZEC | UP | 13.1 min | 39¢ | 52% | 12¢ | ❌ Lost | -$4.07 |
| 9/28 12:16:51 PM | SOL | UP | 13.1 min | 49¢ | 57% | 6¢ | ❌ Lost | -$5.08 |
| 9/28 12:16:51 PM | DOGE | UP | 13.1 min | 44¢ | 54% | 8¢ | ❌ Lost | -$4.58 |
| 9/28 12:16:31 PM | NEAR | DOWN | 13.5 min | 40¢ | 47% | 5¢ | ✅ Won | $5.83 |
| 9/28 12:16:25 PM | BNB | DOWN | 13.6 min | 53¢ | 61% | 6¢ | ✅ Won | $4.52 |
| 9/28 12:16:18 PM | HYPE | UP | 13.7 min | 21¢ | 27% | 5¢ | ❌ Lost | -$2.22 |
| 9/28 12:02:46 PM | NEAR | UP | 12.2 min | 32¢ | 39% | 5¢ | ❌ Lost | -$3.36 |
| 9/28 12:02:40 PM | BTC | DOWN | 12.3 min | 34¢ | 41% | 5¢ | ❌ Lost | -$3.56 |
| 9/28 12:02:25 PM | HYPE | UP | 12.6 min | 36¢ | 43% | 5¢ | ✅ Won | $6.23 |
| 9/28 12:01:16 PM | ZEC | DOWN | 13.7 min | 56¢ | 72% | 14¢ | ✅ Won | $4.22 |
| 9/28 12:01:16 PM | ETH | UP | 13.7 min | 37¢ | 44% | 5¢ | ✅ Won | $6.13 |
| 9/28 12:01:08 PM | SOL | UP | 13.9 min | 28¢ | 38% | 9¢ | ✅ Won | $7.05 |
| 9/28 12:01:08 PM | XRP | UP | 13.9 min | 31¢ | 37% | 4¢ | ✅ Won | $6.75 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
