# Fair-Value Bot

*Updated Mon Sep 28, 7:59 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 761 | $125.96 | +3% | $188.10 / -$62.14 |
| 4¢+ ← live bot | 732 | $319.67 | +9% | $224.29 / $95.38 |
| 6¢+ | 680 | $317.97 | +11% | $213.97 / $104.00 |
| 8¢+ | 606 | $344.95 | +14% | $124.01 / $220.94 |
| 10¢+ | 523 | $268.32 | +13% | $96.33 / $171.99 |
| 15¢+ | 321 | $232.64 | +21% | $88.16 / $144.48 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 755 | 746 | 381 (51%) | 45¢ | 53% | $336.61 | +10% | +7.3¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 344 | 155 (45%) | 100 / 244 | 8.4 | -$37.76 | -$84.30 | -5% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 306 | 113 (37%) | 128 / 178 | 7.5 | -$55.90 | -$123.73 | -10% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 74 | 26 (35%) | 28 / 46 | 1.9 | -$14.97 | -$22.97 | -8% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 79% of orders | 79 | 31 (39%) | 25 / 54 | 2.0 | -$13.69 | -$46.97 | -13% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 23 | 10 (43%) | 7 / 16 | 1.4 | -$10.05 | -$11.44 | -12% |

*Model accuracy vs Kalshi's prices on the same 8,422 readings (excluding the final minute): V1 **+3.4%**, V2 **+4.0%**, 3-exchange price (V3/V4) **+1.6%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 352 | 224 (64%) | -$67.90 | -6% | 682 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.4%** over 19,874 readings from 774 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3803 | 2% | 4% | 7% |
| 10–20% | 1584 | 15% | 16% | 17% |
| 20–30% | 1801 | 25% | 26% | 26% |
| 30–40% | 1890 | 35% | 36% | 39% |
| 40–50% | 1932 | 45% | 48% | 52% |
| 50–60% | 1932 | 55% | 59% | 59% |
| 60–70% | 1649 | 65% | 71% | 67% |
| 70–80% | 1389 | 75% | 80% | 78% |
| 80–90% | 1228 | 85% | 88% | 81% |
| 90–100% | 2666 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 419 | 219 (52%) | 46¢ | 52% | $215.77 | +11% |
| 6–10¢ | 245 | 127 (52%) | 45¢ | 54% | $129.21 | +11% |
| 10–20¢ | 76 | 33 (43%) | 43¢ | 57% | -$6.46 | -2% |
| 20¢+ | 6 | 2 (33%) | 35¢ | 65% | -$1.91 | -9% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 711 | 369 (52%) | 45¢ | 54% | $341.80 | +10% |
| 5–10 min | 32 | 10 (31%) | 32¢ | 40% | -$6.02 | -6% |
| 2–5 min | 2 | 2 (100%) | 88¢ | 94% | $2.34 | +13% |
| 1–2 min | 1 | 0 (0%) | 14¢ | 72% | -$1.51 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 82 | 19 (23%) | 18¢ | 27% | $29.53 | +18% |
| Toss-up (25–75¢) | 620 | 326 (53%) | 46¢ | 54% | $302.95 | +10% |
| Favorite (75–95¢) | 44 | 36 (82%) | 80¢ | 87% | $4.13 | +1% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| XRP | 84 | 48 (57%) | 47¢ | 55% | $70.28 | +17% |
| ETH | 84 | 37 (44%) | 46¢ | 54% | -$29.73 | -7% |
| BNB | 84 | 46 (55%) | 43¢ | 52% | $88.87 | +24% |
| NEAR | 83 | 44 (53%) | 48¢ | 55% | $32.19 | +8% |
| HYPE | 83 | 38 (46%) | 42¢ | 51% | $15.62 | +4% |
| BTC | 83 | 43 (52%) | 49¢ | 58% | $6.30 | +1% |
| SOL | 82 | 45 (55%) | 44¢ | 52% | $74.20 | +20% |
| DOGE | 82 | 42 (51%) | 44¢ | 52% | $42.63 | +11% |
| ZEC | 81 | 38 (47%) | 41¢ | 50% | $36.25 | +11% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 7:52:58 PM | SOL | DOWN | 7.0 min | 24¢ | 35% | 10¢ | Open | — |
| 9/28 7:51:51 PM | NEAR | UP | 8.1 min | 30¢ | 37% | 6¢ | Open | — |
| 9/28 7:50:31 PM | DOGE | DOWN | 9.5 min | 41¢ | 51% | 9¢ | Open | — |
| 9/28 7:48:40 PM | XRP | DOWN | 11.3 min | 35¢ | 41% | 5¢ | Open | — |
| 9/28 7:48:08 PM | HYPE | DOWN | 11.9 min | 20¢ | 29% | 8¢ | Open | — |
| 9/28 7:47:35 PM | ETH | DOWN | 12.4 min | 35¢ | 42% | 6¢ | Open | — |
| 9/28 7:47:35 PM | BTC | DOWN | 12.4 min | 30¢ | 38% | 6¢ | Open | — |
| 9/28 7:47:11 PM | ZEC | DOWN | 12.8 min | 26¢ | 33% | 5¢ | Open | — |
| 9/28 7:46:42 PM | BNB | DOWN | 13.3 min | 22¢ | 29% | 6¢ | Open | — |
| 9/28 7:37:36 PM | NEAR | UP | 7.4 min | 20¢ | 29% | 8¢ | ❌ Lost | -$2.11 |
| 9/28 7:33:04 PM | ZEC | DOWN | 11.9 min | 29¢ | 39% | 9¢ | ❌ Lost | -$3.05 |
| 9/28 7:31:53 PM | SOL | UP | 13.1 min | 51¢ | 59% | 6¢ | ✅ Won | $4.72 |
| 9/28 7:31:09 PM | BNB | DOWN | 13.8 min | 37¢ | 52% | 13¢ | ❌ Lost | -$3.87 |
| 9/28 7:31:09 PM | DOGE | DOWN | 13.8 min | 35¢ | 42% | 5¢ | ❌ Lost | -$3.66 |
| 9/28 7:31:09 PM | ETH | DOWN | 13.8 min | 31¢ | 43% | 10¢ | ❌ Lost | -$3.25 |
| 9/28 7:31:09 PM | HYPE | DOWN | 13.8 min | 36¢ | 44% | 6¢ | ❌ Lost | -$3.77 |
| 9/28 7:31:09 PM | XRP | DOWN | 13.8 min | 37¢ | 51% | 12¢ | ❌ Lost | -$3.87 |
| 9/28 7:31:09 PM | BTC | DOWN | 13.8 min | 28¢ | 38% | 9¢ | ❌ Lost | -$2.95 |
| 9/28 7:21:18 PM | NEAR | DOWN | 8.7 min | 80¢ | 86% | 5¢ | ✅ Won | $1.88 |
| 9/28 7:19:19 PM | HYPE | DOWN | 10.7 min | 87¢ | 93% | 4¢ | ✅ Won | $1.18 |
| 9/28 7:19:01 PM | DOGE | UP | 11.0 min | 22¢ | 31% | 8¢ | ❌ Lost | -$2.33 |
| 9/28 7:18:08 PM | ZEC | UP | 11.9 min | 19¢ | 24% | 4¢ | ❌ Lost | -$2.01 |
| 9/28 7:17:53 PM | XRP | DOWN | 12.1 min | 72¢ | 78% | 5¢ | ✅ Won | $2.62 |
| 9/28 7:17:22 PM | BTC | DOWN | 12.6 min | 67¢ | 75% | 7¢ | ✅ Won | $3.14 |
| 9/28 7:17:07 PM | SOL | DOWN | 12.9 min | 73¢ | 79% | 4¢ | ✅ Won | $2.56 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
