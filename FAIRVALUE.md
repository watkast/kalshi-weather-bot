# Fair-Value Bot

*Updated Mon Sep 28, 1:04 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 520 | $113.92 | +5% | $218.59 / -$104.67 |
| 4¢+ ← live bot | 503 | $141.54 | +6% | $272.06 / -$130.52 |
| 6¢+ | 472 | $160.64 | +8% | $202.16 / -$41.52 |
| 8¢+ | 423 | $173.05 | +11% | $133.59 / $39.46 |
| 10¢+ | 372 | $148.86 | +11% | $125.03 / $23.83 |
| 15¢+ | 227 | $153.91 | +21% | $114.55 / $39.36 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 529 | 520 | 264 (51%) | 44¢ | 52% | $271.43 | +11% | +10.3¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 118 | 38 (32%) | 39 / 79 | 8.4 | -$37.76 | -$149.48 | -28% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 107 | 22 (21%) | 61 / 46 | 7.6 | -$55.90 | -$200.94 | -48% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 28 | 5 (18%) | 14 / 14 | 2.0 | -$8.62 | -$36.15 | -42% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 80% of orders | 26 | 7 (27%) | 9 / 17 | 2.0 | -$10.20 | -$42.44 | -38% |

*Model accuracy vs Kalshi's prices on the same 2,837 readings (excluding the final minute): V1 **-0.7%**, V2 **-0.9%**, 3-exchange price (V3/V4) **-5.1%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 126 | 45 (36%) | -$56.30 | -30% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.2%** over 13,850 readings from 531 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2313 | 2% | 4% | 8% |
| 10–20% | 1123 | 15% | 16% | 18% |
| 20–30% | 1287 | 25% | 25% | 29% |
| 30–40% | 1375 | 35% | 36% | 41% |
| 40–50% | 1367 | 45% | 48% | 53% |
| 50–60% | 1354 | 55% | 59% | 58% |
| 60–70% | 1242 | 65% | 70% | 69% |
| 70–80% | 1015 | 75% | 80% | 80% |
| 80–90% | 844 | 85% | 88% | 84% |
| 90–100% | 1930 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 321 | 167 (52%) | 44¢ | 51% | $191.45 | +13% |
| 6–10¢ | 157 | 77 (49%) | 43¢ | 52% | $62.66 | +9% |
| 10–20¢ | 37 | 18 (49%) | 42¢ | 56% | $17.72 | +11% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 510 | 263 (52%) | 45¢ | 52% | $277.67 | +12% |
| 5–10 min | 10 | 1 (10%) | 15¢ | 23% | -$6.24 | -38% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 52 | 11 (21%) | 18¢ | 25% | $9.58 | +10% |
| Toss-up (25–75¢) | 452 | 240 (53%) | 46¢ | 54% | $257.02 | +12% |
| Favorite (75–95¢) | 16 | 13 (81%) | 77¢ | 83% | $4.83 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 58 | 31 (53%) | 44¢ | 52% | $44.62 | +17% |
| ZEC | 58 | 31 (53%) | 43¢ | 51% | $51.72 | +20% |
| XRP | 58 | 30 (52%) | 44¢ | 51% | $36.90 | +14% |
| NEAR | 58 | 33 (57%) | 46¢ | 54% | $53.13 | +19% |
| ETH | 58 | 25 (43%) | 44¢ | 52% | -$15.12 | -6% |
| DOGE | 58 | 28 (48%) | 44¢ | 51% | $18.47 | +7% |
| BTC | 58 | 31 (53%) | 46¢ | 54% | $34.17 | +12% |
| BNB | 57 | 30 (53%) | 44¢ | 53% | $42.32 | +16% |
| HYPE | 57 | 25 (44%) | 41¢ | 50% | $5.22 | +2% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 1:02:52 PM | XRP | DOWN | 12.1 min | 87¢ | 92% | 5¢ | Open | — |
| 9/28 1:02:26 PM | BTC | DOWN | 12.6 min | 87¢ | 93% | 5¢ | Open | — |
| 9/28 1:02:17 PM | NEAR | DOWN | 12.7 min | 80¢ | 87% | 6¢ | Open | — |
| 9/28 1:01:41 PM | SOL | DOWN | 13.3 min | 76¢ | 83% | 6¢ | Open | — |
| 9/28 1:01:41 PM | DOGE | DOWN | 13.3 min | 76¢ | 84% | 7¢ | Open | — |
| 9/28 1:01:41 PM | HYPE | DOWN | 13.3 min | 77¢ | 86% | 7¢ | Open | — |
| 9/28 1:01:32 PM | ZEC | DOWN | 13.5 min | 82¢ | 94% | 11¢ | Open | — |
| 9/28 1:01:32 PM | ETH | UP | 13.5 min | 22¢ | 29% | 6¢ | Open | — |
| 9/28 1:01:24 PM | BNB | DOWN | 13.6 min | 63¢ | 70% | 5¢ | Open | — |
| 9/28 12:48:06 PM | SOL | DOWN | 11.9 min | 47¢ | 55% | 6¢ | ❌ Lost | -$4.88 |
| 9/28 12:48:06 PM | ETH | DOWN | 11.9 min | 31¢ | 44% | 11¢ | ❌ Lost | -$3.25 |
| 9/28 12:47:44 PM | NEAR | DOWN | 12.2 min | 47¢ | 54% | 5¢ | ❌ Lost | -$4.88 |
| 9/28 12:47:35 PM | BTC | DOWN | 12.4 min | 59¢ | 65% | 4¢ | ❌ Lost | -$6.07 |
| 9/28 12:47:05 PM | ZEC | DOWN | 12.9 min | 63¢ | 73% | 8¢ | ✅ Won | $3.53 |
| 9/28 12:46:58 PM | XRP | DOWN | 13.0 min | 45¢ | 53% | 6¢ | ❌ Lost | -$4.68 |
| 9/28 12:46:52 PM | HYPE | DOWN | 13.1 min | 50¢ | 57% | 5¢ | ❌ Lost | -$5.18 |
| 9/28 12:46:44 PM | DOGE | DOWN | 13.3 min | 56¢ | 62% | 4¢ | ❌ Lost | -$5.78 |
| 9/28 12:46:21 PM | BNB | DOWN | 13.6 min | 64¢ | 75% | 9¢ | ❌ Lost | -$6.57 |
| 9/28 12:38:38 PM | ETH | UP | 6.4 min | 7¢ | 13% | 5¢ | ❌ Lost | -$0.75 |
| 9/28 12:37:28 PM | HYPE | UP | 7.5 min | 22¢ | 30% | 6¢ | ❌ Lost | -$2.33 |
| 9/28 12:34:43 PM | NEAR | UP | 10.3 min | 12¢ | 17% | 4¢ | ❌ Lost | -$1.28 |
| 9/28 12:32:23 PM | SOL | DOWN | 12.6 min | 75¢ | 81% | 4¢ | ✅ Won | $2.36 |
| 9/28 12:32:15 PM | BNB | UP | 12.8 min | 20¢ | 27% | 6¢ | ❌ Lost | -$2.12 |
| 9/28 12:31:50 PM | BTC | DOWN | 13.2 min | 63¢ | 74% | 9¢ | ✅ Won | $3.53 |
| 9/28 12:31:20 PM | DOGE | DOWN | 13.7 min | 62¢ | 71% | 7¢ | ✅ Won | $3.63 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
