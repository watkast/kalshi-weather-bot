# Fair-Value Bot

*Updated Mon Sep 28, 12:24 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 493 | $118.45 | +5% | $222.31 / -$103.86 |
| 4¢+ ← live bot | 478 | $173.24 | +8% | $299.41 / -$126.17 |
| 6¢+ | 451 | $196.07 | +11% | $229.49 / -$33.42 |
| 8¢+ | 406 | $198.07 | +13% | $151.24 / $46.83 |
| 10¢+ | 359 | $180.47 | +14% | $139.69 / $40.78 |
| 15¢+ | 225 | $161.28 | +23% | $118.82 / $42.46 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 502 | 493 | 253 (51%) | 44¢ | 52% | $289.03 | +13% | +11.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 91 | 27 (30%) | 31 / 60 | 8.3 | -$37.18 | -$131.88 | -33% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 86 | 19 (22%) | 51 / 35 | 7.8 | -$55.90 | -$148.67 | -44% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 22 | 4 (18%) | 11 / 11 | 2.0 | -$8.62 | -$26.64 | -40% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 81% of orders | 20 | 3 (15%) | 9 / 11 | 2.0 | -$10.20 | -$48.17 | -62% |

*Model accuracy vs Kalshi's prices on the same 2,212 readings (excluding the final minute): V1 **-1.1%**, V2 **-0.4%**, 3-exchange price (V3/V4) **-5.6%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 99 | 40 (40%) | -$56.32 | -34% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+3.9%** over 13,171 readings from 504 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2171 | 2% | 4% | 9% |
| 10–20% | 1020 | 15% | 16% | 20% |
| 20–30% | 1190 | 25% | 25% | 31% |
| 30–40% | 1310 | 35% | 36% | 43% |
| 40–50% | 1308 | 45% | 48% | 54% |
| 50–60% | 1304 | 55% | 59% | 59% |
| 60–70% | 1223 | 65% | 70% | 69% |
| 70–80% | 988 | 75% | 80% | 80% |
| 80–90% | 830 | 85% | 88% | 83% |
| 90–100% | 1827 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 308 | 162 (53%) | 45¢ | 51% | $196.57 | +14% |
| 6–10¢ | 145 | 71 (49%) | 43¢ | 52% | $67.82 | +11% |
| 10–20¢ | 35 | 18 (51%) | 43¢ | 57% | $25.04 | +16% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 485 | 252 (52%) | 44¢ | 52% | $292.19 | +13% |
| 5–10 min | 8 | 1 (12%) | 16¢ | 24% | -$3.16 | -24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 47 | 11 (23%) | 18¢ | 25% | $18.28 | +20% |
| Toss-up (25–75¢) | 431 | 230 (53%) | 45¢ | 54% | $268.28 | +13% |
| Favorite (75–95¢) | 15 | 12 (80%) | 77¢ | 84% | $2.47 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 55 | 30 (55%) | 43¢ | 51% | $52.22 | +21% |
| ZEC | 55 | 29 (53%) | 42¢ | 50% | $48.04 | +20% |
| XRP | 55 | 28 (51%) | 44¢ | 51% | $30.83 | +12% |
| NEAR | 55 | 32 (58%) | 47¢ | 54% | $53.46 | +20% |
| ETH | 55 | 24 (44%) | 45¢ | 52% | -$15.24 | -6% |
| DOGE | 55 | 27 (49%) | 43¢ | 51% | $25.20 | +10% |
| BTC | 55 | 29 (53%) | 45¢ | 53% | $33.08 | +13% |
| BNB | 54 | 29 (54%) | 43¢ | 53% | $46.49 | +19% |
| HYPE | 54 | 25 (46%) | 42¢ | 51% | $14.95 | +6% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 12:18:05 PM | ETH | DOWN | 11.9 min | 57¢ | 67% | 8¢ | Open | — |
| 9/28 12:18:05 PM | XRP | DOWN | 11.9 min | 41¢ | 49% | 6¢ | Open | — |
| 9/28 12:18:05 PM | BTC | DOWN | 11.9 min | 62¢ | 71% | 7¢ | Open | — |
| 9/28 12:16:51 PM | ZEC | UP | 13.1 min | 39¢ | 52% | 12¢ | Open | — |
| 9/28 12:16:51 PM | SOL | UP | 13.1 min | 49¢ | 57% | 6¢ | Open | — |
| 9/28 12:16:51 PM | DOGE | UP | 13.1 min | 44¢ | 54% | 8¢ | Open | — |
| 9/28 12:16:31 PM | NEAR | DOWN | 13.5 min | 40¢ | 47% | 5¢ | Open | — |
| 9/28 12:16:25 PM | BNB | DOWN | 13.6 min | 53¢ | 61% | 6¢ | Open | — |
| 9/28 12:16:18 PM | HYPE | UP | 13.7 min | 21¢ | 27% | 5¢ | Open | — |
| 9/28 12:02:46 PM | NEAR | UP | 12.2 min | 32¢ | 39% | 5¢ | ❌ Lost | -$3.36 |
| 9/28 12:02:40 PM | BTC | DOWN | 12.3 min | 34¢ | 41% | 5¢ | ❌ Lost | -$3.56 |
| 9/28 12:02:25 PM | HYPE | UP | 12.6 min | 36¢ | 43% | 5¢ | ✅ Won | $6.23 |
| 9/28 12:01:16 PM | ZEC | DOWN | 13.7 min | 56¢ | 72% | 14¢ | ✅ Won | $4.22 |
| 9/28 12:01:16 PM | ETH | UP | 13.7 min | 37¢ | 44% | 5¢ | ✅ Won | $6.13 |
| 9/28 12:01:08 PM | SOL | UP | 13.9 min | 28¢ | 38% | 9¢ | ✅ Won | $7.05 |
| 9/28 12:01:08 PM | XRP | UP | 13.9 min | 31¢ | 37% | 4¢ | ✅ Won | $6.75 |
| 9/28 12:01:08 PM | DOGE | UP | 13.9 min | 29¢ | 35% | 5¢ | ✅ Won | $6.95 |
| 9/28 12:01:08 PM | BNB | DOWN | 13.9 min | 57¢ | 67% | 8¢ | ❌ Lost | -$5.88 |
| 9/28 11:48:32 AM | BTC | UP | 11.4 min | 31¢ | 38% | 6¢ | ❌ Lost | -$3.25 |
| 9/28 11:48:26 AM | XRP | UP | 11.6 min | 36¢ | 42% | 4¢ | ✅ Won | $6.23 |
| 9/28 11:48:18 AM | NEAR | DOWN | 11.7 min | 53¢ | 59% | 4¢ | ❌ Lost | -$5.48 |
| 9/28 11:47:58 AM | DOGE | UP | 12.0 min | 26¢ | 32% | 4¢ | ❌ Lost | -$2.74 |
| 9/28 11:47:23 AM | SOL | UP | 12.6 min | 39¢ | 45% | 5¢ | ❌ Lost | -$4.07 |
| 9/28 11:47:01 AM | HYPE | UP | 13.0 min | 21¢ | 26% | 4¢ | ❌ Lost | -$2.22 |
| 9/28 11:46:41 AM | ETH | UP | 13.3 min | 36¢ | 43% | 5¢ | ❌ Lost | -$3.77 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
