# Fair-Value Bot

*Updated Mon Sep 28, 12:54 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 511 | $148.76 | +6% | $212.35 / -$63.59 |
| 4¢+ ← live bot | 494 | $175.36 | +8% | $290.27 / -$114.91 |
| 6¢+ | 463 | $193.35 | +10% | $213.52 / -$20.17 |
| 8¢+ | 415 | $200.88 | +13% | $141.90 / $58.98 |
| 10¢+ | 365 | $172.42 | +13% | $134.74 / $37.68 |
| 15¢+ | 226 | $159.69 | +22% | $114.55 / $45.14 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 520 | 511 | 263 (51%) | 44¢ | 52% | $309.19 | +13% | +10.8¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 109 | 37 (34%) | 39 / 70 | 8.4 | -$37.18 | -$111.72 | -23% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 98 | 21 (21%) | 61 / 37 | 7.5 | -$55.90 | -$164.55 | -44% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 26 | 5 (19%) | 14 / 12 | 2.0 | -$8.62 | -$29.85 | -37% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 79% of orders | 24 | 7 (29%) | 9 / 15 | 2.0 | -$10.20 | -$33.34 | -32% |

*Model accuracy vs Kalshi's prices on the same 2,628 readings (excluding the final minute): V1 **-0.3%**, V2 **-0.3%**, 3-exchange price (V3/V4) **-4.8%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 117 | 44 (38%) | -$50.52 | -28% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.3%** over 13,623 readings from 522 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2306 | 2% | 4% | 8% |
| 10–20% | 1122 | 15% | 16% | 18% |
| 20–30% | 1278 | 25% | 25% | 29% |
| 30–40% | 1368 | 35% | 36% | 42% |
| 40–50% | 1344 | 45% | 47% | 53% |
| 50–60% | 1329 | 55% | 59% | 58% |
| 60–70% | 1228 | 65% | 70% | 68% |
| 70–80% | 991 | 75% | 80% | 80% |
| 80–90% | 830 | 85% | 88% | 83% |
| 90–100% | 1827 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 317 | 167 (53%) | 44¢ | 51% | $213.36 | +15% |
| 6–10¢ | 153 | 76 (50%) | 43¢ | 52% | $75.26 | +11% |
| 10–20¢ | 36 | 18 (50%) | 43¢ | 57% | $20.97 | +13% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 501 | 262 (52%) | 44¢ | 52% | $315.43 | +14% |
| 5–10 min | 10 | 1 (10%) | 15¢ | 23% | -$6.24 | -38% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 52 | 11 (21%) | 18¢ | 25% | $9.58 | +10% |
| Toss-up (25–75¢) | 443 | 239 (54%) | 46¢ | 54% | $294.78 | +14% |
| Favorite (75–95¢) | 16 | 13 (81%) | 77¢ | 83% | $4.83 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 57 | 31 (54%) | 44¢ | 52% | $49.50 | +19% |
| ZEC | 57 | 30 (53%) | 43¢ | 51% | $48.19 | +19% |
| XRP | 57 | 30 (53%) | 44¢ | 51% | $41.58 | +16% |
| NEAR | 57 | 33 (58%) | 46¢ | 54% | $58.01 | +21% |
| ETH | 57 | 25 (44%) | 44¢ | 52% | -$11.87 | -5% |
| DOGE | 57 | 28 (49%) | 43¢ | 51% | $24.25 | +9% |
| BTC | 57 | 31 (54%) | 46¢ | 54% | $40.24 | +15% |
| BNB | 56 | 30 (54%) | 43¢ | 52% | $48.89 | +19% |
| HYPE | 56 | 25 (45%) | 41¢ | 50% | $10.40 | +4% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 12:48:06 PM | SOL | DOWN | 11.9 min | 47¢ | 55% | 6¢ | Open | — |
| 9/28 12:48:06 PM | ETH | DOWN | 11.9 min | 31¢ | 44% | 11¢ | Open | — |
| 9/28 12:47:44 PM | NEAR | DOWN | 12.2 min | 47¢ | 54% | 5¢ | Open | — |
| 9/28 12:47:35 PM | BTC | DOWN | 12.4 min | 59¢ | 65% | 4¢ | Open | — |
| 9/28 12:47:05 PM | ZEC | DOWN | 12.9 min | 63¢ | 73% | 8¢ | Open | — |
| 9/28 12:46:58 PM | XRP | DOWN | 13.0 min | 45¢ | 53% | 6¢ | Open | — |
| 9/28 12:46:52 PM | HYPE | DOWN | 13.1 min | 50¢ | 57% | 5¢ | Open | — |
| 9/28 12:46:44 PM | DOGE | DOWN | 13.3 min | 56¢ | 62% | 4¢ | Open | — |
| 9/28 12:46:21 PM | BNB | DOWN | 13.6 min | 64¢ | 75% | 9¢ | Open | — |
| 9/28 12:38:38 PM | ETH | UP | 6.4 min | 7¢ | 13% | 5¢ | ❌ Lost | -$0.75 |
| 9/28 12:37:28 PM | HYPE | UP | 7.5 min | 22¢ | 30% | 6¢ | ❌ Lost | -$2.33 |
| 9/28 12:34:43 PM | NEAR | UP | 10.3 min | 12¢ | 17% | 4¢ | ❌ Lost | -$1.28 |
| 9/28 12:32:23 PM | SOL | DOWN | 12.6 min | 75¢ | 81% | 4¢ | ✅ Won | $2.36 |
| 9/28 12:32:15 PM | BNB | UP | 12.8 min | 20¢ | 27% | 6¢ | ❌ Lost | -$2.12 |
| 9/28 12:31:50 PM | BTC | DOWN | 13.2 min | 63¢ | 74% | 9¢ | ✅ Won | $3.53 |
| 9/28 12:31:20 PM | DOGE | DOWN | 13.7 min | 62¢ | 71% | 7¢ | ✅ Won | $3.63 |
| 9/28 12:31:10 PM | ZEC | DOWN | 13.8 min | 56¢ | 63% | 5¢ | ✅ Won | $4.22 |
| 9/28 12:31:10 PM | XRP | DOWN | 13.8 min | 48¢ | 56% | 6¢ | ✅ Won | $5.02 |
| 9/28 12:18:05 PM | ETH | DOWN | 11.9 min | 57¢ | 67% | 8¢ | ✅ Won | $4.12 |
| 9/28 12:18:05 PM | XRP | DOWN | 11.9 min | 41¢ | 49% | 6¢ | ✅ Won | $5.73 |
| 9/28 12:18:05 PM | BTC | DOWN | 11.9 min | 62¢ | 71% | 7¢ | ✅ Won | $3.63 |
| 9/28 12:16:51 PM | ZEC | UP | 13.1 min | 39¢ | 52% | 12¢ | ❌ Lost | -$4.07 |
| 9/28 12:16:51 PM | SOL | UP | 13.1 min | 49¢ | 57% | 6¢ | ❌ Lost | -$5.08 |
| 9/28 12:16:51 PM | DOGE | UP | 13.1 min | 44¢ | 54% | 8¢ | ❌ Lost | -$4.58 |
| 9/28 12:16:31 PM | NEAR | DOWN | 13.5 min | 40¢ | 47% | 5¢ | ✅ Won | $5.83 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
