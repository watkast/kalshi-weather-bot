# Fair-Value Bot

*Updated Mon Sep 28, 6:08 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 699 | $86.04 | +3% | $140.89 / -$54.85 |
| 4¢+ ← live bot | 674 | $259.49 | +8% | $200.27 / $59.22 |
| 6¢+ | 627 | $295.15 | +11% | $145.29 / $149.86 |
| 8¢+ | 558 | $359.77 | +17% | $63.07 / $296.70 |
| 10¢+ | 483 | $278.55 | +15% | $89.39 / $189.16 |
| 15¢+ | 294 | $247.05 | +25% | $113.16 / $133.89 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 696 | 687 | 351 (51%) | 45¢ | 53% | $317.03 | +10% | +7.8¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 285 | 125 (44%) | 79 / 206 | 8.4 | -$37.76 | -$103.88 | -8% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 252 | 90 (36%) | 111 / 141 | 7.4 | -$55.90 | -$141.18 | -14% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 63 | 18 (29%) | 25 / 38 | 2.0 | -$14.97 | -$51.80 | -22% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 65 | 23 (35%) | 19 / 46 | 2.0 | -$13.69 | -$60.60 | -21% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 14 | 6 (43%) | 3 / 11 | 1.3 | -$9.34 | -$4.08 | -7% |

*Model accuracy vs Kalshi's prices on the same 6,976 readings (excluding the final minute): V1 **+4.0%**, V2 **+3.9%**, 3-exchange price (V3/V4) **+2.1%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 293 | 165 (56%) | -$87.48 | -11% | 80 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.6%** over 18,312 readings from 711 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3254 | 2% | 4% | 6% |
| 10–20% | 1398 | 15% | 16% | 16% |
| 20–30% | 1641 | 25% | 26% | 27% |
| 30–40% | 1778 | 35% | 36% | 39% |
| 40–50% | 1821 | 45% | 48% | 52% |
| 50–60% | 1819 | 55% | 59% | 58% |
| 60–70% | 1547 | 65% | 71% | 67% |
| 70–80% | 1312 | 75% | 80% | 78% |
| 80–90% | 1157 | 85% | 88% | 80% |
| 90–100% | 2585 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 400 | 208 (52%) | 45¢ | 52% | $201.52 | +11% |
| 6–10¢ | 219 | 114 (52%) | 45¢ | 54% | $128.26 | +13% |
| 10–20¢ | 63 | 27 (43%) | 43¢ | 57% | -$12.35 | -4% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 660 | 342 (52%) | 45¢ | 53% | $321.01 | +10% |
| 5–10 min | 26 | 8 (31%) | 31¢ | 39% | -$5.01 | -6% |
| 2–5 min | 1 | 1 (100%) | 89¢ | 94% | $1.03 | +11% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 67 | 15 (22%) | 19¢ | 26% | $18.40 | +14% |
| Toss-up (25–75¢) | 584 | 306 (52%) | 46¢ | 54% | $288.23 | +10% |
| Favorite (75–95¢) | 36 | 30 (83%) | 79¢ | 86% | $10.40 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| XRP | 77 | 43 (56%) | 47¢ | 54% | $59.06 | +16% |
| NEAR | 77 | 41 (53%) | 47¢ | 55% | $32.74 | +9% |
| ETH | 77 | 34 (44%) | 45¢ | 53% | -$21.27 | -6% |
| BNB | 77 | 42 (55%) | 43¢ | 53% | $74.20 | +21% |
| HYPE | 77 | 35 (45%) | 42¢ | 50% | $17.94 | +5% |
| BTC | 77 | 41 (53%) | 49¢ | 57% | $23.84 | +6% |
| SOL | 76 | 40 (53%) | 44¢ | 52% | $54.66 | +16% |
| DOGE | 75 | 39 (52%) | 45¢ | 53% | $40.74 | +12% |
| ZEC | 74 | 36 (49%) | 42¢ | 51% | $35.12 | +11% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 6:06:35 PM | ZEC | DOWN | 8.4 min | 15¢ | 28% | 12¢ | Open | — |
| 9/28 6:03:29 PM | HYPE | DOWN | 11.5 min | 68¢ | 84% | 15¢ | Open | — |
| 9/28 6:02:30 PM | XRP | UP | 12.5 min | 66¢ | 74% | 6¢ | Open | — |
| 9/28 6:02:01 PM | BNB | UP | 13.0 min | 28¢ | 40% | 10¢ | Open | — |
| 9/28 6:01:54 PM | ETH | DOWN | 13.1 min | 46¢ | 59% | 11¢ | Open | — |
| 9/28 6:01:41 PM | DOGE | DOWN | 13.3 min | 57¢ | 63% | 4¢ | Open | — |
| 9/28 6:01:12 PM | NEAR | DOWN | 13.8 min | 74¢ | 83% | 8¢ | Open | — |
| 9/28 6:01:04 PM | BTC | DOWN | 13.9 min | 64¢ | 75% | 9¢ | Open | — |
| 9/28 6:01:04 PM | SOL | DOWN | 13.9 min | 80¢ | 91% | 9¢ | Open | — |
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
| 9/28 5:31:32 PM | ETH | DOWN | 13.4 min | 52¢ | 58% | 4¢ | ❌ Lost | -$5.38 |
| 9/28 5:31:09 PM | BNB | DOWN | 13.8 min | 36¢ | 51% | 13¢ | ❌ Lost | -$3.77 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
