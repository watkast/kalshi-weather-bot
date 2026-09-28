# Fair-Value Bot

*Updated Mon Sep 28, 5:17 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 672 | $102.39 | +3% | $138.45 / -$36.06 |
| 4¢+ ← live bot | 649 | $242.60 | +8% | $209.71 / $32.89 |
| 6¢+ | 605 | $289.04 | +11% | $116.26 / $172.78 |
| 8¢+ | 539 | $364.93 | +18% | $80.00 / $284.93 |
| 10¢+ | 466 | $291.59 | +17% | $99.63 / $191.96 |
| 15¢+ | 281 | $255.97 | +28% | $110.23 / $145.74 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 667 | 664 | 343 (52%) | 45¢ | 53% | $354.20 | +12% | +8.2¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 262 | 117 (45%) | 74 / 188 | 8.5 | -$37.76 | -$66.71 | -5% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 231 | 87 (38%) | 100 / 131 | 7.5 | -$55.90 | -$112.84 | -11% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 57 | 14 (25%) | 23 / 34 | 2.0 | -$14.97 | -$62.29 | -31% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 59 | 22 (37%) | 18 / 41 | 2.0 | -$13.69 | -$48.06 | -18% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 10 | 6 (60%) | 2 / 8 | 1.2 | -$3.46 | $11.26 | +27% |

*Model accuracy vs Kalshi's prices on the same 6,345 readings (excluding the final minute): V1 **+4.3%**, V2 **+4.3%**, 3-exchange price (V3/V4) **+2.2%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 270 | 142 (53%) | -$50.31 | -8% | 42 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.8%** over 17,635 readings from 684 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3196 | 2% | 4% | 6% |
| 10–20% | 1345 | 15% | 16% | 16% |
| 20–30% | 1570 | 25% | 26% | 27% |
| 30–40% | 1734 | 35% | 36% | 39% |
| 40–50% | 1750 | 45% | 48% | 52% |
| 50–60% | 1754 | 55% | 59% | 58% |
| 60–70% | 1507 | 65% | 71% | 67% |
| 70–80% | 1256 | 75% | 80% | 77% |
| 80–90% | 1087 | 85% | 88% | 79% |
| 90–100% | 2436 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 391 | 203 (52%) | 45¢ | 52% | $205.73 | +11% |
| 6–10¢ | 209 | 111 (53%) | 45¢ | 54% | $143.98 | +15% |
| 10–20¢ | 59 | 27 (46%) | 43¢ | 57% | $4.89 | +2% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 641 | 335 (52%) | 45¢ | 53% | $349.87 | +12% |
| 5–10 min | 23 | 8 (35%) | 32¢ | 40% | $4.33 | +6% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 64 | 15 (23%) | 19¢ | 26% | $24.54 | +20% |
| Toss-up (25–75¢) | 567 | 301 (53%) | 46¢ | 54% | $324.53 | +12% |
| Favorite (75–95¢) | 33 | 27 (82%) | 79¢ | 86% | $5.13 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 74 | 39 (53%) | 43¢ | 51% | $60.49 | +18% |
| XRP | 74 | 41 (55%) | 46¢ | 54% | $55.84 | +16% |
| NEAR | 74 | 40 (54%) | 47¢ | 55% | $38.03 | +11% |
| ETH | 74 | 33 (45%) | 45¢ | 53% | -$15.43 | -4% |
| BNB | 74 | 42 (57%) | 44¢ | 53% | $84.58 | +25% |
| HYPE | 74 | 33 (45%) | 41¢ | 50% | $13.76 | +4% |
| BTC | 74 | 40 (54%) | 49¢ | 57% | $26.95 | +7% |
| ZEC | 73 | 36 (49%) | 42¢ | 51% | $38.78 | +12% |
| DOGE | 73 | 39 (53%) | 45¢ | 53% | $51.20 | +15% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 5:16:31 PM | NEAR | DOWN | 13.5 min | 34¢ | 44% | 8¢ | Open | — |
| 9/28 5:16:23 PM | HYPE | DOWN | 13.6 min | 18¢ | 28% | 9¢ | Open | — |
| 9/28 5:16:13 PM | BNB | DOWN | 13.8 min | 35¢ | 49% | 12¢ | Open | — |
| 9/28 5:05:28 PM | ZEC | DOWN | 9.5 min | 19¢ | 24% | 4¢ | ❌ Lost | -$1.99 |
| 9/28 5:03:02 PM | XRP | UP | 11.9 min | 92¢ | 97% | 5¢ | ❌ Lost | -$9.22 |
| 9/28 5:03:02 PM | BTC | UP | 11.9 min | 80¢ | 86% | 5¢ | ❌ Lost | -$8.12 |
| 9/28 5:02:26 PM | ETH | DOWN | 12.6 min | 32¢ | 38% | 4¢ | ✅ Won | $6.64 |
| 9/28 5:01:44 PM | HYPE | DOWN | 13.3 min | 42¢ | 49% | 5¢ | ❌ Lost | -$4.38 |
| 9/28 5:01:08 PM | NEAR | DOWN | 13.8 min | 37¢ | 44% | 5¢ | ❌ Lost | -$3.87 |
| 9/28 5:01:08 PM | SOL | DOWN | 13.8 min | 31¢ | 44% | 11¢ | ✅ Won | $6.75 |
| 9/28 5:01:08 PM | DOGE | DOWN | 13.8 min | 42¢ | 58% | 15¢ | ✅ Won | $5.68 |
| 9/28 5:01:08 PM | BNB | DOWN | 13.8 min | 46¢ | 55% | 7¢ | ✅ Won | $5.22 |
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

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
