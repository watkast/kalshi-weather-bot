# Fair-Value Bot

*Updated Mon Sep 28, 6:38 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 717 | $84.44 | +2% | $150.80 / -$66.36 |
| 4¢+ ← live bot | 690 | $258.26 | +8% | $194.22 / $64.04 |
| 6¢+ | 643 | $271.30 | +10% | $145.47 / $125.83 |
| 8¢+ | 574 | $335.84 | +15% | $73.48 / $262.36 |
| 10¢+ | 496 | $267.72 | +14% | $63.32 / $204.40 |
| 15¢+ | 306 | $241.27 | +23% | $99.35 / $141.92 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 713 | 704 | 359 (51%) | 45¢ | 53% | $300.44 | +9% | +7.6¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 302 | 133 (44%) | 84 / 218 | 8.4 | -$37.76 | -$120.47 | -8% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 266 | 93 (35%) | 117 / 149 | 7.4 | -$55.90 | -$157.63 | -14% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 66 | 21 (32%) | 27 / 39 | 1.9 | -$14.97 | -$36.41 | -15% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 79% of orders | 69 | 26 (38%) | 20 / 49 | 2.0 | -$13.69 | -$54.14 | -17% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 16 | 6 (38%) | 4 / 12 | 1.3 | -$10.05 | -$14.13 | -21% |

*Model accuracy vs Kalshi's prices on the same 7,390 readings (excluding the final minute): V1 **+3.2%**, V2 **+3.6%**, 3-exchange price (V3/V4) **+1.2%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 310 | 182 (59%) | -$104.07 | -12% | 189 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.2%** over 18,757 readings from 729 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3426 | 2% | 4% | 7% |
| 10–20% | 1461 | 15% | 16% | 16% |
| 20–30% | 1689 | 25% | 26% | 27% |
| 30–40% | 1800 | 35% | 36% | 39% |
| 40–50% | 1841 | 45% | 48% | 52% |
| 50–60% | 1846 | 55% | 59% | 59% |
| 60–70% | 1564 | 65% | 71% | 67% |
| 70–80% | 1343 | 75% | 80% | 78% |
| 80–90% | 1175 | 85% | 88% | 80% |
| 90–100% | 2612 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 403 | 209 (52%) | 45¢ | 52% | $194.50 | +10% |
| 6–10¢ | 228 | 120 (53%) | 45¢ | 54% | $126.48 | +12% |
| 10–20¢ | 67 | 28 (42%) | 43¢ | 57% | -$18.63 | -6% |
| 20¢+ | 6 | 2 (33%) | 35¢ | 65% | -$1.91 | -9% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 672 | 348 (52%) | 46¢ | 54% | $298.93 | +9% |
| 5–10 min | 29 | 9 (31%) | 30¢ | 38% | $0.68 | +1% |
| 2–5 min | 2 | 2 (100%) | 88¢ | 94% | $2.34 | +13% |
| 1–2 min | 1 | 0 (0%) | 14¢ | 72% | -$1.51 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 71 | 16 (23%) | 18¢ | 26% | $22.58 | +16% |
| Toss-up (25–75¢) | 591 | 309 (52%) | 46¢ | 54% | $276.79 | +10% |
| Favorite (75–95¢) | 42 | 34 (81%) | 80¢ | 87% | $1.07 | +0% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| XRP | 79 | 45 (57%) | 47¢ | 55% | $63.61 | +16% |
| NEAR | 79 | 42 (53%) | 48¢ | 56% | $27.47 | +7% |
| ETH | 79 | 35 (44%) | 46¢ | 54% | -$25.18 | -7% |
| BNB | 79 | 43 (54%) | 43¢ | 52% | $80.54 | +23% |
| BTC | 79 | 41 (52%) | 49¢ | 57% | $9.63 | +2% |
| SOL | 78 | 41 (53%) | 44¢ | 52% | $54.53 | +15% |
| HYPE | 78 | 36 (46%) | 42¢ | 51% | $20.98 | +6% |
| DOGE | 77 | 40 (52%) | 46¢ | 53% | $36.84 | +10% |
| ZEC | 76 | 36 (47%) | 42¢ | 51% | $32.02 | +10% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 6:37:07 PM | BTC | UP | 7.9 min | 63¢ | 76% | 11¢ | Open | — |
| 9/28 6:33:49 PM | NEAR | DOWN | 11.2 min | 31¢ | 38% | 6¢ | Open | — |
| 9/28 6:33:27 PM | HYPE | DOWN | 11.6 min | 44¢ | 54% | 8¢ | Open | — |
| 9/28 6:32:08 PM | SOL | UP | 12.9 min | 24¢ | 31% | 5¢ | Open | — |
| 9/28 6:31:52 PM | DOGE | UP | 13.1 min | 30¢ | 39% | 7¢ | Open | — |
| 9/28 6:31:32 PM | XRP | UP | 13.4 min | 36¢ | 43% | 5¢ | Open | — |
| 9/28 6:31:32 PM | ZEC | UP | 13.4 min | 54¢ | 61% | 6¢ | Open | — |
| 9/28 6:31:26 PM | ETH | DOWN | 13.6 min | 53¢ | 59% | 4¢ | Open | — |
| 9/28 6:31:15 PM | BNB | UP | 13.7 min | 39¢ | 45% | 4¢ | Open | — |
| 9/28 6:28:57 PM | ZEC | UP | 1.0 min | 14¢ | 72% | 57¢ | ❌ Lost | -$1.51 |
| 9/28 6:25:54 PM | XRP | DOWN | 4.1 min | 86¢ | 94% | 7¢ | ✅ Won | $1.31 |
| 9/28 6:23:18 PM | BNB | UP | 6.7 min | 7¢ | 15% | 8¢ | ✅ Won | $9.29 |
| 9/28 6:20:02 PM | SOL | UP | 9.9 min | 19¢ | 26% | 6¢ | ❌ Lost | -$2.01 |
| 9/28 6:19:47 PM | NEAR | DOWN | 10.2 min | 76¢ | 84% | 7¢ | ❌ Lost | -$7.73 |
| 9/28 6:18:48 PM | ETH | DOWN | 11.2 min | 91¢ | 95% | 4¢ | ✅ Won | $0.87 |
| 9/28 6:16:29 PM | DOGE | DOWN | 13.5 min | 79¢ | 87% | 6¢ | ✅ Won | $1.98 |
| 9/28 6:16:29 PM | BTC | DOWN | 13.5 min | 75¢ | 83% | 6¢ | ❌ Lost | -$7.64 |
| 9/28 6:06:35 PM | ZEC | DOWN | 8.4 min | 15¢ | 28% | 12¢ | ❌ Lost | -$1.59 |
| 9/28 6:03:29 PM | HYPE | DOWN | 11.5 min | 68¢ | 84% | 15¢ | ✅ Won | $3.04 |
| 9/28 6:02:30 PM | XRP | UP | 12.5 min | 66¢ | 74% | 6¢ | ✅ Won | $3.24 |
| 9/28 6:02:01 PM | BNB | UP | 13.0 min | 28¢ | 40% | 10¢ | ❌ Lost | -$2.95 |
| 9/28 6:01:54 PM | ETH | DOWN | 13.1 min | 46¢ | 59% | 11¢ | ❌ Lost | -$4.78 |
| 9/28 6:01:41 PM | DOGE | DOWN | 13.3 min | 57¢ | 63% | 4¢ | ❌ Lost | -$5.88 |
| 9/28 6:01:12 PM | NEAR | DOWN | 13.8 min | 74¢ | 83% | 8¢ | ✅ Won | $2.46 |
| 9/28 6:01:04 PM | BTC | DOWN | 13.9 min | 64¢ | 75% | 9¢ | ❌ Lost | -$6.57 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
