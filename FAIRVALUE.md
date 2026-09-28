# Fair-Value Bot

*Updated Mon Sep 28, 2:15 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 556 | $182.82 | +7% | $169.55 / $13.27 |
| 4¢+ ← live bot | 537 | $222.08 | +9% | $226.51 / -$4.43 |
| 6¢+ | 502 | $218.51 | +11% | $159.24 / $59.27 |
| 8¢+ | 447 | $223.07 | +13% | $142.23 / $80.84 |
| 10¢+ | 391 | $179.64 | +12% | $112.27 / $67.37 |
| 15¢+ | 235 | $162.62 | +22% | $104.45 / $58.17 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 565 | 556 | 290 (52%) | 44¢ | 52% | $343.25 | +13% | +10.6¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 154 | 64 (42%) | 43 / 111 | 8.6 | -$37.76 | -$77.66 | -11% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 134 | 42 (31%) | 62 / 72 | 7.4 | -$55.90 | -$128.53 | -23% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 34 | 7 (21%) | 16 / 18 | 2.0 | -$8.62 | -$40.38 | -37% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 34 | 10 (29%) | 12 / 22 | 2.0 | -$10.20 | -$48.62 | -33% |

*Model accuracy vs Kalshi's prices on the same 3,655 readings (excluding the final minute): V1 **+4.2%**, V2 **+4.3%**, 3-exchange price (V3/V4) **-0.7%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 162 | 55 (34%) | -$43.90 | -18% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.5%** over 14,733 readings from 567 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2737 | 2% | 4% | 7% |
| 10–20% | 1180 | 15% | 16% | 18% |
| 20–30% | 1346 | 25% | 25% | 28% |
| 30–40% | 1461 | 35% | 36% | 40% |
| 40–50% | 1434 | 45% | 48% | 53% |
| 50–60% | 1412 | 55% | 59% | 57% |
| 60–70% | 1287 | 65% | 71% | 68% |
| 70–80% | 1054 | 75% | 80% | 80% |
| 80–90% | 863 | 85% | 88% | 83% |
| 90–100% | 1959 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 341 | 181 (53%) | 45¢ | 51% | $229.92 | +15% |
| 6–10¢ | 169 | 87 (51%) | 44¢ | 53% | $95.29 | +12% |
| 10–20¢ | 41 | 20 (49%) | 43¢ | 57% | $18.44 | +10% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 545 | 288 (53%) | 45¢ | 53% | $348.18 | +14% |
| 5–10 min | 11 | 2 (18%) | 22¢ | 30% | -$4.93 | -20% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 55 | 12 (22%) | 18¢ | 26% | $12.39 | +12% |
| Toss-up (25–75¢) | 477 | 257 (54%) | 46¢ | 54% | $312.00 | +14% |
| Favorite (75–95¢) | 24 | 21 (88%) | 78¢ | 85% | $18.86 | +10% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 62 | 34 (55%) | 45¢ | 52% | $53.38 | +19% |
| ZEC | 62 | 33 (53%) | 43¢ | 51% | $55.08 | +20% |
| XRP | 62 | 34 (55%) | 45¢ | 52% | $53.44 | +19% |
| NEAR | 62 | 35 (56%) | 47¢ | 54% | $49.19 | +16% |
| ETH | 62 | 27 (44%) | 44¢ | 52% | -$14.06 | -5% |
| DOGE | 62 | 31 (50%) | 44¢ | 52% | $25.26 | +9% |
| BTC | 62 | 34 (55%) | 47¢ | 55% | $40.98 | +14% |
| BNB | 61 | 34 (56%) | 44¢ | 53% | $61.63 | +22% |
| HYPE | 61 | 28 (46%) | 41¢ | 50% | $18.35 | +7% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 2:01:56 PM | ZEC | DOWN | 13.1 min | 54¢ | 62% | 6¢ | Open | — |
| 9/28 2:01:56 PM | BNB | DOWN | 13.1 min | 70¢ | 84% | 12¢ | Open | — |
| 9/28 2:01:42 PM | NEAR | DOWN | 13.3 min | 59¢ | 65% | 4¢ | Open | — |
| 9/28 2:01:33 PM | DOGE | UP | 13.4 min | 36¢ | 42% | 5¢ | Open | — |
| 9/28 2:01:33 PM | SOL | UP | 13.4 min | 41¢ | 49% | 6¢ | Open | — |
| 9/28 2:01:22 PM | BTC | DOWN | 13.6 min | 52¢ | 67% | 13¢ | Open | — |
| 9/28 2:01:22 PM | XRP | DOWN | 13.6 min | 49¢ | 67% | 16¢ | Open | — |
| 9/28 2:01:22 PM | ETH | DOWN | 13.6 min | 54¢ | 67% | 11¢ | Open | — |
| 9/28 2:01:22 PM | HYPE | DOWN | 13.6 min | 80¢ | 92% | 11¢ | Open | — |
| 9/28 1:49:24 PM | ZEC | UP | 10.6 min | 22¢ | 33% | 10¢ | ❌ Lost | -$2.33 |
| 9/28 1:48:04 PM | ETH | DOWN | 11.9 min | 40¢ | 50% | 8¢ | ❌ Lost | -$4.17 |
| 9/28 1:46:30 PM | BTC | DOWN | 13.5 min | 30¢ | 38% | 7¢ | ❌ Lost | -$3.15 |
| 9/28 1:46:30 PM | SOL | DOWN | 13.5 min | 28¢ | 35% | 5¢ | ❌ Lost | -$2.95 |
| 9/28 1:46:17 PM | DOGE | DOWN | 13.7 min | 27¢ | 33% | 4¢ | ❌ Lost | -$2.84 |
| 9/28 1:46:17 PM | NEAR | DOWN | 13.7 min | 36¢ | 43% | 5¢ | ❌ Lost | -$3.77 |
| 9/28 1:46:17 PM | BNB | DOWN | 13.7 min | 32¢ | 42% | 9¢ | ✅ Won | $6.64 |
| 9/28 1:46:17 PM | HYPE | DOWN | 13.7 min | 25¢ | 32% | 6¢ | ✅ Won | $7.36 |
| 9/28 1:46:02 PM | XRP | DOWN | 14.0 min | 24¢ | 30% | 4¢ | ✅ Won | $7.47 |
| 9/28 1:35:37 PM | NEAR | DOWN | 9.4 min | 86¢ | 93% | 6¢ | ✅ Won | $1.31 |
| 9/28 1:32:17 PM | HYPE | DOWN | 12.7 min | 26¢ | 33% | 6¢ | ✅ Won | $7.26 |
| 9/28 1:31:53 PM | SOL | DOWN | 13.1 min | 49¢ | 57% | 6¢ | ✅ Won | $4.92 |
| 9/28 1:31:53 PM | ZEC | DOWN | 13.1 min | 32¢ | 40% | 6¢ | ✅ Won | $6.64 |
| 9/28 1:31:22 PM | DOGE | DOWN | 13.6 min | 55¢ | 61% | 4¢ | ✅ Won | $4.32 |
| 9/28 1:31:14 PM | BTC | DOWN | 13.8 min | 58¢ | 66% | 6¢ | ✅ Won | $4.02 |
| 9/28 1:31:14 PM | XRP | DOWN | 13.8 min | 60¢ | 67% | 5¢ | ✅ Won | $3.83 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
