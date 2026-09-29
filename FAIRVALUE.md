# Fair-Value Bot

*Updated Mon Sep 28, 7:39 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 752 | $151.76 | +4% | $193.78 / -$42.02 |
| 4¢+ ← live bot | 723 | $347.29 | +10% | $229.11 / $118.18 |
| 6¢+ | 671 | $350.29 | +12% | $200.73 / $149.56 |
| 8¢+ | 597 | $367.56 | +16% | $96.76 / $270.80 |
| 10¢+ | 514 | $285.22 | +14% | $88.80 / $196.42 |
| 15¢+ | 313 | $260.39 | +25% | $83.27 / $177.12 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 746 | 737 | 380 (52%) | 45¢ | 53% | $358.42 | +10% | +7.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 335 | 154 (46%) | 98 / 237 | 8.4 | -$37.76 | -$62.49 | -4% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 297 | 112 (38%) | 128 / 169 | 7.4 | -$55.90 | -$100.76 | -8% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 72 | 25 (35%) | 27 / 45 | 1.9 | -$14.97 | -$26.57 | -10% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 80% of orders | 77 | 30 (39%) | 25 / 52 | 2.0 | -$13.69 | -$49.78 | -14% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 22 | 9 (41%) | 6 / 16 | 1.4 | -$10.05 | -$14.88 | -16% |

*Model accuracy vs Kalshi's prices on the same 8,215 readings (excluding the final minute): V1 **+4.2%**, V2 **+4.9%**, 3-exchange price (V3/V4) **+2.3%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 343 | 215 (63%) | -$46.09 | -5% | 469 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.9%** over 19,649 readings from 765 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3788 | 2% | 4% | 6% |
| 10–20% | 1558 | 15% | 16% | 16% |
| 20–30% | 1774 | 25% | 26% | 26% |
| 30–40% | 1865 | 35% | 36% | 38% |
| 40–50% | 1901 | 45% | 48% | 51% |
| 50–60% | 1889 | 55% | 59% | 58% |
| 60–70% | 1619 | 65% | 71% | 67% |
| 70–80% | 1387 | 75% | 80% | 78% |
| 80–90% | 1222 | 85% | 88% | 81% |
| 90–100% | 2646 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 418 | 219 (52%) | 46¢ | 52% | $219.43 | +11% |
| 6–10¢ | 240 | 126 (52%) | 45¢ | 54% | $136.37 | +12% |
| 10–20¢ | 73 | 33 (45%) | 43¢ | 57% | $4.53 | +1% |
| 20¢+ | 6 | 2 (33%) | 35¢ | 65% | -$1.91 | -9% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 703 | 368 (52%) | 46¢ | 54% | $361.50 | +11% |
| 5–10 min | 31 | 10 (32%) | 32¢ | 40% | -$3.91 | -4% |
| 2–5 min | 2 | 2 (100%) | 88¢ | 94% | $2.34 | +13% |
| 1–2 min | 1 | 0 (0%) | 14¢ | 72% | -$1.51 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 81 | 19 (23%) | 18¢ | 27% | $31.64 | +20% |
| Toss-up (25–75¢) | 612 | 325 (53%) | 46¢ | 55% | $322.65 | +11% |
| Favorite (75–95¢) | 44 | 36 (82%) | 80¢ | 87% | $4.13 | +1% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| XRP | 83 | 48 (58%) | 47¢ | 55% | $74.15 | +18% |
| ETH | 83 | 37 (45%) | 46¢ | 54% | -$26.48 | -7% |
| BNB | 83 | 46 (55%) | 43¢ | 52% | $92.74 | +25% |
| NEAR | 82 | 44 (54%) | 48¢ | 55% | $34.30 | +8% |
| HYPE | 82 | 38 (46%) | 42¢ | 51% | $19.39 | +5% |
| BTC | 82 | 43 (52%) | 50¢ | 58% | $9.25 | +2% |
| SOL | 81 | 44 (54%) | 44¢ | 52% | $69.48 | +19% |
| DOGE | 81 | 42 (52%) | 45¢ | 53% | $46.29 | +12% |
| ZEC | 80 | 38 (48%) | 41¢ | 50% | $39.30 | +12% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 7:37:36 PM | NEAR | UP | 7.4 min | 20¢ | 29% | 8¢ | Open | — |
| 9/28 7:33:04 PM | ZEC | DOWN | 11.9 min | 29¢ | 39% | 9¢ | Open | — |
| 9/28 7:31:53 PM | SOL | UP | 13.1 min | 51¢ | 59% | 6¢ | Open | — |
| 9/28 7:31:09 PM | BNB | DOWN | 13.8 min | 37¢ | 52% | 13¢ | Open | — |
| 9/28 7:31:09 PM | DOGE | DOWN | 13.8 min | 35¢ | 42% | 5¢ | Open | — |
| 9/28 7:31:09 PM | ETH | DOWN | 13.8 min | 31¢ | 43% | 10¢ | Open | — |
| 9/28 7:31:09 PM | HYPE | DOWN | 13.8 min | 36¢ | 44% | 6¢ | Open | — |
| 9/28 7:31:09 PM | XRP | DOWN | 13.8 min | 37¢ | 51% | 12¢ | Open | — |
| 9/28 7:31:09 PM | BTC | DOWN | 13.8 min | 28¢ | 38% | 9¢ | Open | — |
| 9/28 7:21:18 PM | NEAR | DOWN | 8.7 min | 80¢ | 86% | 5¢ | ✅ Won | $1.88 |
| 9/28 7:19:19 PM | HYPE | DOWN | 10.7 min | 87¢ | 93% | 4¢ | ✅ Won | $1.18 |
| 9/28 7:19:01 PM | DOGE | UP | 11.0 min | 22¢ | 31% | 8¢ | ❌ Lost | -$2.33 |
| 9/28 7:18:08 PM | ZEC | UP | 11.9 min | 19¢ | 24% | 4¢ | ❌ Lost | -$2.01 |
| 9/28 7:17:53 PM | XRP | DOWN | 12.1 min | 72¢ | 78% | 5¢ | ✅ Won | $2.62 |
| 9/28 7:17:22 PM | BTC | DOWN | 12.6 min | 67¢ | 75% | 7¢ | ✅ Won | $3.14 |
| 9/28 7:17:07 PM | SOL | DOWN | 12.9 min | 73¢ | 79% | 4¢ | ✅ Won | $2.56 |
| 9/28 7:17:07 PM | ETH | DOWN | 12.9 min | 72¢ | 79% | 6¢ | ✅ Won | $2.65 |
| 9/28 7:16:36 PM | BNB | DOWN | 13.4 min | 52¢ | 62% | 8¢ | ✅ Won | $4.62 |
| 9/28 7:02:34 PM | NEAR | DOWN | 12.4 min | 17¢ | 32% | 14¢ | ✅ Won | $8.20 |
| 9/28 7:02:34 PM | ZEC | DOWN | 12.4 min | 23¢ | 34% | 10¢ | ✅ Won | $7.57 |
| 9/28 7:02:27 PM | DOGE | DOWN | 12.6 min | 26¢ | 45% | 17¢ | ✅ Won | $7.26 |
| 9/28 7:02:04 PM | SOL | DOWN | 12.9 min | 49¢ | 58% | 7¢ | ✅ Won | $4.92 |
| 9/28 7:01:48 PM | HYPE | DOWN | 13.2 min | 59¢ | 65% | 4¢ | ✅ Won | $3.93 |
| 9/28 7:01:24 PM | BNB | DOWN | 13.6 min | 73¢ | 84% | 9¢ | ✅ Won | $2.56 |
| 9/28 7:01:24 PM | BTC | DOWN | 13.6 min | 69¢ | 83% | 12¢ | ✅ Won | $2.95 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
