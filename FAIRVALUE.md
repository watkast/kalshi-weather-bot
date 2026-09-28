# Fair-Value Bot

*Updated Mon Sep 28, 2:25 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 565 | $127.42 | +5% | $155.82 / -$28.40 |
| 4¢+ ← live bot | 546 | $187.51 | +7% | $215.69 / -$28.18 |
| 6¢+ | 510 | $185.08 | +9% | $144.41 / $40.67 |
| 8¢+ | 454 | $191.13 | +11% | $118.25 / $72.88 |
| 10¢+ | 397 | $141.67 | +10% | $118.55 / $23.12 |
| 15¢+ | 237 | $152.36 | +20% | $100.99 / $51.37 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 574 | 565 | 292 (52%) | 45¢ | 53% | $312.25 | +12% | +10.3¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 163 | 66 (40%) | 45 / 118 | 8.6 | -$37.76 | -$108.66 | -14% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 143 | 42 (29%) | 62 / 81 | 7.5 | -$55.90 | -$184.32 | -31% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 36 | 7 (19%) | 16 / 20 | 2.0 | -$8.62 | -$45.93 | -40% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 79% of orders | 36 | 10 (28%) | 12 / 24 | 2.0 | -$13.69 | -$62.31 | -38% |

*Model accuracy vs Kalshi's prices on the same 3,862 readings (excluding the final minute): V1 **+3.1%**, V2 **+3.3%**, 3-exchange price (V3/V4) **-1.4%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 171 | 59 (35%) | -$68.06 | -25% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.2%** over 14,949 readings from 576 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2741 | 2% | 4% | 7% |
| 10–20% | 1185 | 15% | 16% | 18% |
| 20–30% | 1352 | 25% | 25% | 29% |
| 30–40% | 1474 | 35% | 36% | 40% |
| 40–50% | 1444 | 45% | 48% | 53% |
| 50–60% | 1420 | 55% | 59% | 58% |
| 60–70% | 1298 | 65% | 71% | 68% |
| 70–80% | 1067 | 75% | 80% | 80% |
| 80–90% | 890 | 85% | 88% | 83% |
| 90–100% | 2078 | 98% | 98% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 344 | 182 (53%) | 45¢ | 51% | $224.50 | +14% |
| 6–10¢ | 170 | 88 (52%) | 44¢ | 53% | $101.02 | +13% |
| 10–20¢ | 46 | 20 (43%) | 45¢ | 59% | -$12.87 | -6% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 554 | 290 (52%) | 45¢ | 53% | $317.18 | +12% |
| 5–10 min | 11 | 2 (18%) | 22¢ | 30% | -$4.93 | -20% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 55 | 12 (22%) | 18¢ | 26% | $12.39 | +12% |
| Toss-up (25–75¢) | 485 | 259 (53%) | 46¢ | 54% | $289.12 | +13% |
| Favorite (75–95¢) | 25 | 21 (84%) | 78¢ | 86% | $10.74 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 63 | 35 (56%) | 45¢ | 52% | $59.11 | +20% |
| ZEC | 63 | 33 (52%) | 43¢ | 51% | $49.50 | +18% |
| XRP | 63 | 34 (54%) | 45¢ | 52% | $48.36 | +17% |
| NEAR | 63 | 35 (56%) | 47¢ | 55% | $43.12 | +14% |
| ETH | 63 | 27 (43%) | 44¢ | 52% | -$19.64 | -7% |
| DOGE | 63 | 32 (51%) | 44¢ | 52% | $31.49 | +11% |
| BTC | 63 | 34 (54%) | 47¢ | 55% | $35.60 | +12% |
| BNB | 62 | 34 (55%) | 44¢ | 54% | $54.48 | +19% |
| HYPE | 62 | 28 (45%) | 42¢ | 51% | $10.23 | +4% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 2:20:48 PM | ZEC | DOWN | 9.2 min | 37¢ | 45% | 7¢ | Open | — |
| 9/28 2:17:19 PM | DOGE | UP | 12.7 min | 34¢ | 41% | 5¢ | Open | — |
| 9/28 2:16:34 PM | SOL | UP | 13.4 min | 29¢ | 35% | 4¢ | Open | — |
| 9/28 2:16:27 PM | ETH | DOWN | 13.6 min | 66¢ | 72% | 5¢ | Open | — |
| 9/28 2:16:27 PM | NEAR | DOWN | 13.6 min | 68¢ | 74% | 4¢ | Open | — |
| 9/28 2:16:17 PM | BTC | UP | 13.7 min | 29¢ | 36% | 6¢ | Open | — |
| 9/28 2:16:17 PM | XRP | UP | 13.7 min | 32¢ | 39% | 5¢ | Open | — |
| 9/28 2:16:17 PM | BNB | UP | 13.7 min | 28¢ | 45% | 16¢ | Open | — |
| 9/28 2:16:17 PM | HYPE | UP | 13.7 min | 31¢ | 40% | 7¢ | Open | — |
| 9/28 2:01:56 PM | ZEC | DOWN | 13.1 min | 54¢ | 62% | 6¢ | ❌ Lost | -$5.58 |
| 9/28 2:01:56 PM | BNB | DOWN | 13.1 min | 70¢ | 84% | 12¢ | ❌ Lost | -$7.15 |
| 9/28 2:01:42 PM | NEAR | DOWN | 13.3 min | 59¢ | 65% | 4¢ | ❌ Lost | -$6.07 |
| 9/28 2:01:33 PM | DOGE | UP | 13.4 min | 36¢ | 42% | 5¢ | ✅ Won | $6.23 |
| 9/28 2:01:33 PM | SOL | UP | 13.4 min | 41¢ | 49% | 6¢ | ✅ Won | $5.73 |
| 9/28 2:01:22 PM | BTC | DOWN | 13.6 min | 52¢ | 67% | 13¢ | ❌ Lost | -$5.38 |
| 9/28 2:01:22 PM | XRP | DOWN | 13.6 min | 49¢ | 67% | 16¢ | ❌ Lost | -$5.08 |
| 9/28 2:01:22 PM | ETH | DOWN | 13.6 min | 54¢ | 67% | 11¢ | ❌ Lost | -$5.58 |
| 9/28 2:01:22 PM | HYPE | DOWN | 13.6 min | 80¢ | 92% | 11¢ | ❌ Lost | -$8.12 |
| 9/28 1:49:24 PM | ZEC | UP | 10.6 min | 22¢ | 33% | 10¢ | ❌ Lost | -$2.33 |
| 9/28 1:48:04 PM | ETH | DOWN | 11.9 min | 40¢ | 50% | 8¢ | ❌ Lost | -$4.17 |
| 9/28 1:46:30 PM | BTC | DOWN | 13.5 min | 30¢ | 38% | 7¢ | ❌ Lost | -$3.15 |
| 9/28 1:46:30 PM | SOL | DOWN | 13.5 min | 28¢ | 35% | 5¢ | ❌ Lost | -$2.95 |
| 9/28 1:46:17 PM | DOGE | DOWN | 13.7 min | 27¢ | 33% | 4¢ | ❌ Lost | -$2.84 |
| 9/28 1:46:17 PM | NEAR | DOWN | 13.7 min | 36¢ | 43% | 5¢ | ❌ Lost | -$3.77 |
| 9/28 1:46:17 PM | BNB | DOWN | 13.7 min | 32¢ | 42% | 9¢ | ✅ Won | $6.64 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
