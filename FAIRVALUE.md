# Fair-Value Bot

*Updated Mon Sep 28, 2:35 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 574 | $149.69 | +5% | $157.68 / -$7.99 |
| 4¢+ ← live bot | 555 | $198.04 | +8% | $207.63 / -$9.59 |
| 6¢+ | 519 | $204.79 | +10% | $131.51 / $73.28 |
| 8¢+ | 462 | $213.40 | +12% | $91.31 / $122.09 |
| 10¢+ | 403 | $145.99 | +10% | $135.25 / $10.74 |
| 15¢+ | 241 | $156.70 | +20% | $99.18 / $57.52 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 581 | 574 | 297 (52%) | 44¢ | 52% | $325.44 | +12% | +10.3¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 172 | 71 (41%) | 51 / 121 | 8.6 | -$37.76 | -$95.47 | -12% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 152 | 48 (32%) | 71 / 81 | 7.6 | -$55.90 | -$152.97 | -24% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 38 | 7 (18%) | 17 / 21 | 2.0 | -$8.62 | -$53.05 | -43% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 38 | 11 (29%) | 14 / 24 | 2.0 | -$13.69 | -$58.49 | -35% |

*Model accuracy vs Kalshi's prices on the same 4,069 readings (excluding the final minute): V1 **+2.9%**, V2 **+3.3%**, 3-exchange price (V3/V4) **-1.4%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 180 | 65 (36%) | -$47.28 | -16% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.1%** over 15,174 readings from 585 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2754 | 2% | 4% | 7% |
| 10–20% | 1199 | 15% | 16% | 18% |
| 20–30% | 1380 | 25% | 25% | 29% |
| 30–40% | 1529 | 35% | 36% | 41% |
| 40–50% | 1475 | 45% | 48% | 54% |
| 50–60% | 1457 | 55% | 59% | 58% |
| 60–70% | 1308 | 65% | 71% | 69% |
| 70–80% | 1075 | 75% | 80% | 80% |
| 80–90% | 902 | 85% | 88% | 84% |
| 90–100% | 2095 | 98% | 98% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 350 | 185 (53%) | 45¢ | 51% | $227.76 | +14% |
| 6–10¢ | 172 | 89 (52%) | 44¢ | 53% | $103.90 | +13% |
| 10–20¢ | 47 | 21 (45%) | 44¢ | 58% | -$5.82 | -3% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 562 | 295 (52%) | 45¢ | 53% | $334.24 | +13% |
| 5–10 min | 12 | 2 (17%) | 23¢ | 31% | -$8.80 | -31% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 55 | 12 (22%) | 18¢ | 26% | $12.39 | +12% |
| Toss-up (25–75¢) | 494 | 264 (53%) | 46¢ | 54% | $302.31 | +13% |
| Favorite (75–95¢) | 25 | 21 (84%) | 78¢ | 86% | $10.74 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 64 | 35 (55%) | 44¢ | 52% | $56.06 | +19% |
| ZEC | 64 | 33 (52%) | 43¢ | 51% | $45.63 | +16% |
| XRP | 64 | 35 (55%) | 44¢ | 52% | $55.00 | +19% |
| NEAR | 64 | 35 (55%) | 47¢ | 55% | $36.16 | +12% |
| ETH | 64 | 28 (44%) | 45¢ | 53% | -$16.40 | -6% |
| DOGE | 64 | 33 (52%) | 44¢ | 52% | $37.93 | +13% |
| BTC | 64 | 34 (53%) | 46¢ | 54% | $32.55 | +11% |
| BNB | 63 | 35 (56%) | 44¢ | 54% | $61.53 | +21% |
| HYPE | 63 | 29 (46%) | 42¢ | 50% | $16.98 | +6% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 2:34:35 PM | SOL | DOWN | 10.4 min | 40¢ | 47% | 6¢ | Open | — |
| 9/28 2:33:35 PM | ETH | UP | 11.4 min | 39¢ | 46% | 5¢ | Open | — |
| 9/28 2:33:00 PM | DOGE | DOWN | 12.0 min | 48¢ | 56% | 7¢ | Open | — |
| 9/28 2:32:53 PM | BTC | DOWN | 12.1 min | 52¢ | 60% | 7¢ | Open | — |
| 9/28 2:32:08 PM | XRP | DOWN | 12.8 min | 44¢ | 52% | 6¢ | Open | — |
| 9/28 2:32:08 PM | NEAR | DOWN | 12.8 min | 37¢ | 44% | 5¢ | Open | — |
| 9/28 2:31:53 PM | BNB | DOWN | 13.1 min | 59¢ | 71% | 11¢ | Open | — |
| 9/28 2:20:48 PM | ZEC | DOWN | 9.2 min | 37¢ | 45% | 7¢ | ❌ Lost | -$3.87 |
| 9/28 2:17:19 PM | DOGE | UP | 12.7 min | 34¢ | 41% | 5¢ | ✅ Won | $6.44 |
| 9/28 2:16:34 PM | SOL | UP | 13.4 min | 29¢ | 35% | 4¢ | ❌ Lost | -$3.05 |
| 9/28 2:16:27 PM | ETH | DOWN | 13.6 min | 66¢ | 72% | 5¢ | ✅ Won | $3.24 |
| 9/28 2:16:27 PM | NEAR | DOWN | 13.6 min | 68¢ | 74% | 4¢ | ❌ Lost | -$6.96 |
| 9/28 2:16:17 PM | BTC | UP | 13.7 min | 29¢ | 36% | 6¢ | ❌ Lost | -$3.05 |
| 9/28 2:16:17 PM | XRP | UP | 13.7 min | 32¢ | 39% | 5¢ | ✅ Won | $6.64 |
| 9/28 2:16:17 PM | BNB | UP | 13.7 min | 28¢ | 45% | 16¢ | ✅ Won | $7.05 |
| 9/28 2:16:17 PM | HYPE | UP | 13.7 min | 31¢ | 40% | 7¢ | ✅ Won | $6.75 |
| 9/28 2:01:56 PM | ZEC | DOWN | 13.1 min | 54¢ | 62% | 6¢ | ❌ Lost | -$5.58 |
| 9/28 2:01:56 PM | BNB | DOWN | 13.1 min | 70¢ | 84% | 12¢ | ❌ Lost | -$7.15 |
| 9/28 2:01:42 PM | NEAR | DOWN | 13.3 min | 59¢ | 65% | 4¢ | ❌ Lost | -$6.07 |
| 9/28 2:01:33 PM | DOGE | UP | 13.4 min | 36¢ | 42% | 5¢ | ✅ Won | $6.23 |
| 9/28 2:01:33 PM | SOL | UP | 13.4 min | 41¢ | 49% | 6¢ | ✅ Won | $5.73 |
| 9/28 2:01:22 PM | BTC | DOWN | 13.6 min | 52¢ | 67% | 13¢ | ❌ Lost | -$5.38 |
| 9/28 2:01:22 PM | XRP | DOWN | 13.6 min | 49¢ | 67% | 16¢ | ❌ Lost | -$5.08 |
| 9/28 2:01:22 PM | ETH | DOWN | 13.6 min | 54¢ | 67% | 11¢ | ❌ Lost | -$5.58 |
| 9/28 2:01:22 PM | HYPE | DOWN | 13.6 min | 80¢ | 92% | 11¢ | ❌ Lost | -$8.12 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
