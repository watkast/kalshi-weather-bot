# Fair-Value Bot

*Updated Mon Sep 28, 8:20 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 779 | $128.45 | +3% | $211.40 / -$82.95 |
| 4¢+ ← live bot | 750 | $325.95 | +9% | $239.58 / $86.37 |
| 6¢+ | 695 | $303.71 | +10% | $211.14 / $92.57 |
| 8¢+ | 619 | $333.42 | +14% | $147.44 / $185.98 |
| 10¢+ | 534 | $253.88 | +12% | $126.68 / $127.20 |
| 15¢+ | 329 | $228.38 | +21% | $111.80 / $116.58 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 771 | 764 | 386 (51%) | 45¢ | 53% | $325.71 | +9% | +7.3¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 362 | 160 (44%) | 105 / 257 | 8.4 | -$37.76 | -$95.20 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 323 | 114 (35%) | 136 / 187 | 7.5 | -$55.90 | -$151.77 | -12% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 78 | 27 (35%) | 31 / 47 | 1.9 | -$14.97 | -$22.69 | -8% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 75% of orders | 83 | 32 (39%) | 26 / 57 | 2.0 | -$13.69 | -$51.04 | -14% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 26 | 11 (42%) | 8 / 18 | 1.4 | -$10.05 | -$16.02 | -14% |

*Model accuracy vs Kalshi's prices on the same 8,836 readings (excluding the final minute): V1 **+3.0%**, V2 **+3.6%**, 3-exchange price (V3/V4) **+1.3%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 370 | 242 (65%) | -$78.80 | -7% | 1,519 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.3%** over 20,315 readings from 792 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3873 | 2% | 4% | 7% |
| 10–20% | 1618 | 15% | 16% | 17% |
| 20–30% | 1826 | 25% | 26% | 26% |
| 30–40% | 1938 | 35% | 36% | 39% |
| 40–50% | 1982 | 45% | 47% | 52% |
| 50–60% | 1974 | 55% | 59% | 59% |
| 60–70% | 1704 | 65% | 71% | 68% |
| 70–80% | 1450 | 75% | 80% | 79% |
| 80–90% | 1257 | 85% | 88% | 81% |
| 90–100% | 2693 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 431 | 224 (52%) | 45¢ | 52% | $224.22 | +11% |
| 6–10¢ | 251 | 127 (51%) | 45¢ | 54% | $109.86 | +9% |
| 10–20¢ | 76 | 33 (43%) | 43¢ | 57% | -$6.46 | -2% |
| 20¢+ | 6 | 2 (33%) | 35¢ | 65% | -$1.91 | -9% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 722 | 373 (52%) | 45¢ | 53% | $343.89 | +10% |
| 5–10 min | 39 | 11 (28%) | 32¢ | 40% | -$19.01 | -15% |
| 2–5 min | 2 | 2 (100%) | 88¢ | 94% | $2.34 | +13% |
| 1–2 min | 1 | 0 (0%) | 14¢ | 72% | -$1.51 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 86 | 19 (22%) | 19¢ | 27% | $20.54 | +12% |
| Toss-up (25–75¢) | 634 | 331 (52%) | 46¢ | 54% | $301.04 | +10% |
| Favorite (75–95¢) | 44 | 36 (82%) | 80¢ | 87% | $4.13 | +1% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| XRP | 86 | 48 (56%) | 47¢ | 55% | $62.55 | +15% |
| ETH | 86 | 38 (44%) | 46¢ | 54% | -$27.34 | -7% |
| BNB | 86 | 47 (55%) | 42¢ | 52% | $92.95 | +25% |
| NEAR | 85 | 45 (53%) | 47¢ | 55% | $35.84 | +9% |
| HYPE | 85 | 38 (45%) | 42¢ | 51% | $8.22 | +2% |
| BTC | 85 | 43 (51%) | 49¢ | 57% | -$0.62 | -0% |
| SOL | 84 | 46 (55%) | 44¢ | 52% | $78.31 | +21% |
| DOGE | 84 | 42 (50%) | 44¢ | 52% | $36.36 | +9% |
| ZEC | 83 | 39 (47%) | 41¢ | 50% | $39.44 | +11% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 8:19:25 PM | ZEC | UP | 10.6 min | 23¢ | 35% | 10¢ | Open | — |
| 9/28 8:18:49 PM | BTC | DOWN | 11.2 min | 38¢ | 48% | 9¢ | Open | — |
| 9/28 8:16:52 PM | NEAR | DOWN | 13.1 min | 43¢ | 49% | 4¢ | Open | — |
| 9/28 8:16:23 PM | DOGE | DOWN | 13.6 min | 34¢ | 40% | 4¢ | Open | — |
| 9/28 8:16:23 PM | ETH | DOWN | 13.6 min | 42¢ | 48% | 5¢ | Open | — |
| 9/28 8:16:23 PM | XRP | DOWN | 13.6 min | 33¢ | 39% | 4¢ | Open | — |
| 9/28 8:16:14 PM | BNB | DOWN | 13.8 min | 42¢ | 48% | 4¢ | Open | — |
| 9/28 8:08:32 PM | BTC | UP | 6.5 min | 36¢ | 42% | 5¢ | ❌ Lost | -$3.77 |
| 9/28 8:07:27 PM | DOGE | UP | 7.5 min | 19¢ | 26% | 6¢ | ❌ Lost | -$2.01 |
| 9/28 8:06:10 PM | XRP | UP | 8.8 min | 39¢ | 46% | 5¢ | ❌ Lost | -$4.07 |
| 9/28 8:05:08 PM | NEAR | UP | 9.8 min | 30¢ | 37% | 5¢ | ❌ Lost | -$3.20 |
| 9/28 8:02:25 PM | HYPE | DOWN | 12.6 min | 51¢ | 60% | 8¢ | ❌ Lost | -$5.28 |
| 9/28 8:01:23 PM | ZEC | DOWN | 13.6 min | 39¢ | 46% | 6¢ | ✅ Won | $5.93 |
| 9/28 8:01:15 PM | BNB | DOWN | 13.8 min | 34¢ | 41% | 5¢ | ✅ Won | $6.41 |
| 9/28 8:01:15 PM | SOL | DOWN | 13.8 min | 32¢ | 39% | 5¢ | ✅ Won | $6.64 |
| 9/28 8:01:15 PM | ETH | DOWN | 13.8 min | 38¢ | 44% | 5¢ | ✅ Won | $6.05 |
| 9/28 7:52:58 PM | SOL | DOWN | 7.0 min | 24¢ | 35% | 10¢ | ❌ Lost | -$2.53 |
| 9/28 7:51:51 PM | NEAR | UP | 8.1 min | 30¢ | 37% | 6¢ | ✅ Won | $6.85 |
| 9/28 7:50:31 PM | DOGE | DOWN | 9.5 min | 41¢ | 51% | 9¢ | ❌ Lost | -$4.26 |
| 9/28 7:48:40 PM | XRP | DOWN | 11.3 min | 35¢ | 41% | 5¢ | ❌ Lost | -$3.66 |
| 9/28 7:48:08 PM | HYPE | DOWN | 11.9 min | 20¢ | 29% | 8¢ | ❌ Lost | -$2.12 |
| 9/28 7:47:35 PM | ETH | DOWN | 12.4 min | 35¢ | 42% | 6¢ | ❌ Lost | -$3.66 |
| 9/28 7:47:35 PM | BTC | DOWN | 12.4 min | 30¢ | 38% | 6¢ | ❌ Lost | -$3.15 |
| 9/28 7:47:11 PM | ZEC | DOWN | 12.8 min | 26¢ | 33% | 5¢ | ❌ Lost | -$2.74 |
| 9/28 7:46:42 PM | BNB | DOWN | 13.3 min | 22¢ | 29% | 6¢ | ❌ Lost | -$2.33 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
