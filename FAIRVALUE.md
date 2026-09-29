# Fair-Value Bot

*Updated Mon Sep 28, 6:18 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 708 | $88.97 | +3% | $143.64 / -$54.67 |
| 4¢+ ← live bot | 683 | $265.97 | +8% | $194.77 / $71.20 |
| 6¢+ | 636 | $296.11 | +11% | $146.23 / $149.88 |
| 8¢+ | 567 | $358.89 | +16% | $68.76 / $290.13 |
| 10¢+ | 490 | $278.84 | +15% | $69.37 / $209.47 |
| 15¢+ | 301 | $252.85 | +25% | $110.55 / $142.30 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 698 | 696 | 355 (51%) | 45¢ | 53% | $305.88 | +9% | +7.6¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 294 | 129 (44%) | 81 / 213 | 8.4 | -$37.76 | -$115.03 | -8% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 259 | 91 (35%) | 113 / 146 | 7.4 | -$55.90 | -$153.90 | -14% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 65 | 20 (31%) | 26 / 39 | 2.0 | -$14.97 | -$44.71 | -18% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 67 | 25 (37%) | 19 / 48 | 2.0 | -$13.69 | -$54.28 | -18% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 16 | 6 (38%) | 4 / 12 | 1.3 | -$10.05 | -$14.13 | -21% |

*Model accuracy vs Kalshi's prices on the same 7,183 readings (excluding the final minute): V1 **+3.9%**, V2 **+3.7%**, 3-exchange price (V3/V4) **+2.0%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 302 | 174 (58%) | -$98.63 | -12% | 138 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.6%** over 18,537 readings from 720 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3290 | 2% | 4% | 6% |
| 10–20% | 1416 | 15% | 16% | 16% |
| 20–30% | 1671 | 25% | 26% | 27% |
| 30–40% | 1798 | 35% | 36% | 39% |
| 40–50% | 1838 | 45% | 48% | 52% |
| 50–60% | 1842 | 55% | 59% | 59% |
| 60–70% | 1564 | 65% | 71% | 67% |
| 70–80% | 1336 | 75% | 80% | 78% |
| 80–90% | 1174 | 85% | 88% | 80% |
| 90–100% | 2608 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 401 | 208 (52%) | 45¢ | 52% | $195.64 | +10% |
| 6–10¢ | 223 | 117 (52%) | 45¢ | 54% | $129.27 | +12% |
| 10–20¢ | 67 | 28 (42%) | 43¢ | 57% | -$18.63 | -6% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 668 | 346 (52%) | 46¢ | 54% | $311.45 | +10% |
| 5–10 min | 27 | 8 (30%) | 31¢ | 39% | -$6.60 | -8% |
| 2–5 min | 1 | 1 (100%) | 89¢ | 94% | $1.03 | +11% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 68 | 15 (22%) | 18¢ | 26% | $16.81 | +13% |
| Toss-up (25–75¢) | 591 | 309 (52%) | 46¢ | 54% | $276.79 | +10% |
| Favorite (75–95¢) | 37 | 31 (84%) | 79¢ | 86% | $12.28 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| XRP | 78 | 44 (56%) | 47¢ | 54% | $62.30 | +16% |
| NEAR | 78 | 42 (54%) | 48¢ | 55% | $35.20 | +9% |
| ETH | 78 | 34 (44%) | 45¢ | 53% | -$26.05 | -7% |
| BNB | 78 | 42 (54%) | 43¢ | 53% | $71.25 | +20% |
| HYPE | 78 | 36 (46%) | 42¢ | 51% | $20.98 | +6% |
| BTC | 78 | 41 (53%) | 49¢ | 57% | $17.27 | +4% |
| SOL | 77 | 41 (53%) | 44¢ | 52% | $56.54 | +16% |
| DOGE | 76 | 39 (51%) | 45¢ | 53% | $34.86 | +10% |
| ZEC | 75 | 36 (48%) | 42¢ | 50% | $33.53 | +10% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 6:16:29 PM | DOGE | DOWN | 13.5 min | 79¢ | 87% | 6¢ | Open | — |
| 9/28 6:16:29 PM | BTC | DOWN | 13.5 min | 75¢ | 83% | 6¢ | Open | — |
| 9/28 6:06:35 PM | ZEC | DOWN | 8.4 min | 15¢ | 28% | 12¢ | ❌ Lost | -$1.59 |
| 9/28 6:03:29 PM | HYPE | DOWN | 11.5 min | 68¢ | 84% | 15¢ | ✅ Won | $3.04 |
| 9/28 6:02:30 PM | XRP | UP | 12.5 min | 66¢ | 74% | 6¢ | ✅ Won | $3.24 |
| 9/28 6:02:01 PM | BNB | UP | 13.0 min | 28¢ | 40% | 10¢ | ❌ Lost | -$2.95 |
| 9/28 6:01:54 PM | ETH | DOWN | 13.1 min | 46¢ | 59% | 11¢ | ❌ Lost | -$4.78 |
| 9/28 6:01:41 PM | DOGE | DOWN | 13.3 min | 57¢ | 63% | 4¢ | ❌ Lost | -$5.88 |
| 9/28 6:01:12 PM | NEAR | DOWN | 13.8 min | 74¢ | 83% | 8¢ | ✅ Won | $2.46 |
| 9/28 6:01:04 PM | BTC | DOWN | 13.9 min | 64¢ | 75% | 9¢ | ❌ Lost | -$6.57 |
| 9/28 6:01:04 PM | SOL | DOWN | 13.9 min | 80¢ | 91% | 9¢ | ✅ Won | $1.88 |
| 9/28 5:48:44 PM | ZEC | UP | 11.2 min | 35¢ | 43% | 6¢ | ❌ Lost | -$3.66 |
| 9/28 5:47:18 PM | XRP | UP | 12.7 min | 50¢ | 57% | 5¢ | ✅ Won | $4.82 |
| 9/28 5:47:10 PM | DOGE | DOWN | 12.8 min | 53¢ | 62% | 8¢ | ❌ Lost | -$5.48 |
| 9/28 5:46:35 PM | SOL | DOWN | 13.4 min | 67¢ | 79% | 10¢ | ❌ Lost | -$6.86 |
| 9/28 5:46:35 PM | HYPE | DOWN | 13.4 min | 74¢ | 82% | 7¢ | ✅ Won | $2.46 |
| 9/28 5:46:28 PM | ETH | DOWN | 13.5 min | 78¢ | 88% | 8¢ | ✅ Won | $2.07 |
| 9/28 5:46:13 PM | BTC | DOWN | 13.8 min | 74¢ | 83% | 7¢ | ✅ Won | $2.46 |
| 9/28 5:46:13 PM | BNB | UP | 13.8 min | 28¢ | 42% | 13¢ | ❌ Lost | -$2.95 |
| 9/28 5:46:13 PM | NEAR | DOWN | 13.8 min | 70¢ | 76% | 4¢ | ❌ Lost | -$7.15 |
| 9/28 5:40:18 PM | SOL | DOWN | 4.7 min | 89¢ | 94% | 4¢ | ✅ Won | $1.03 |
| 9/28 5:38:57 PM | BTC | DOWN | 6.0 min | 37¢ | 45% | 6¢ | ❌ Lost | -$3.87 |
| 9/28 5:37:04 PM | XRP | UP | 7.9 min | 36¢ | 42% | 4¢ | ❌ Lost | -$3.77 |
| 9/28 5:32:09 PM | HYPE | DOWN | 12.8 min | 62¢ | 68% | 5¢ | ✅ Won | $3.63 |
| 9/28 5:31:54 PM | DOGE | DOWN | 13.1 min | 48¢ | 54% | 4¢ | ❌ Lost | -$4.98 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
