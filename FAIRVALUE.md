# Fair-Value Bot

*Updated Mon Sep 28, 5:38 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 681 | $98.09 | +3% | $136.54 / -$38.45 |
| 4¢+ ← live bot | 656 | $243.86 | +8% | $197.11 / $46.75 |
| 6¢+ | 612 | $286.32 | +11% | $136.34 / $149.98 |
| 8¢+ | 544 | $362.04 | +17% | $59.63 / $302.41 |
| 10¢+ | 469 | $286.88 | +16% | $105.36 / $181.52 |
| 15¢+ | 283 | $252.17 | +27% | $117.08 / $135.09 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 676 | 670 | 344 (51%) | 45¢ | 53% | $343.01 | +11% | +8.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 268 | 118 (44%) | 75 / 193 | 8.4 | -$37.76 | -$77.90 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 235 | 87 (37%) | 100 / 135 | 7.3 | -$55.90 | -$119.09 | -12% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 59 | 15 (25%) | 24 / 35 | 2.0 | -$14.97 | -$61.50 | -29% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 61 | 22 (36%) | 18 / 43 | 2.0 | -$13.69 | -$53.43 | -20% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 11 | 6 (55%) | 2 / 9 | 1.2 | -$3.46 | $8.31 | +19% |

*Model accuracy vs Kalshi's prices on the same 6,552 readings (excluding the final minute): V1 **+4.2%**, V2 **+4.2%**, 3-exchange price (V3/V4) **+2.1%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 276 | 148 (54%) | -$61.50 | -9% | 57 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.7%** over 17,860 readings from 693 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3196 | 2% | 4% | 6% |
| 10–20% | 1345 | 15% | 16% | 16% |
| 20–30% | 1570 | 25% | 26% | 27% |
| 30–40% | 1734 | 35% | 36% | 39% |
| 40–50% | 1750 | 45% | 48% | 52% |
| 50–60% | 1759 | 55% | 59% | 58% |
| 60–70% | 1519 | 65% | 71% | 67% |
| 70–80% | 1292 | 75% | 80% | 78% |
| 80–90% | 1138 | 85% | 88% | 80% |
| 90–100% | 2557 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 392 | 204 (52%) | 45¢ | 52% | $207.90 | +11% |
| 6–10¢ | 213 | 111 (52%) | 44¢ | 53% | $134.28 | +14% |
| 10–20¢ | 60 | 27 (45%) | 43¢ | 57% | $1.23 | +0% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 646 | 336 (52%) | 45¢ | 53% | $340.38 | +11% |
| 5–10 min | 24 | 8 (33%) | 31¢ | 39% | $2.63 | +3% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 67 | 15 (22%) | 19¢ | 26% | $18.40 | +14% |
| Toss-up (25–75¢) | 569 | 301 (53%) | 46¢ | 54% | $317.31 | +12% |
| Favorite (75–95¢) | 34 | 28 (82%) | 79¢ | 86% | $7.30 | +3% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| XRP | 75 | 42 (56%) | 47¢ | 54% | $58.01 | +16% |
| NEAR | 75 | 40 (53%) | 47¢ | 55% | $34.47 | +9% |
| ETH | 75 | 33 (44%) | 45¢ | 53% | -$17.96 | -5% |
| BNB | 75 | 42 (56%) | 44¢ | 53% | $80.92 | +24% |
| HYPE | 75 | 33 (44%) | 41¢ | 49% | $11.85 | +4% |
| BTC | 75 | 40 (53%) | 48¢ | 56% | $25.25 | +7% |
| SOL | 74 | 39 (53%) | 43¢ | 51% | $60.49 | +18% |
| ZEC | 73 | 36 (49%) | 42¢ | 51% | $38.78 | +12% |
| DOGE | 73 | 39 (53%) | 45¢ | 53% | $51.20 | +15% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 5:37:04 PM | XRP | UP | 7.9 min | 36¢ | 42% | 4¢ | Open | — |
| 9/28 5:32:09 PM | HYPE | DOWN | 12.8 min | 62¢ | 68% | 5¢ | Open | — |
| 9/28 5:31:54 PM | DOGE | DOWN | 13.1 min | 48¢ | 54% | 4¢ | Open | — |
| 9/28 5:31:32 PM | ETH | DOWN | 13.4 min | 52¢ | 58% | 4¢ | Open | — |
| 9/28 5:31:09 PM | BNB | DOWN | 13.8 min | 36¢ | 51% | 13¢ | Open | — |
| 9/28 5:31:09 PM | NEAR | DOWN | 13.8 min | 44¢ | 51% | 5¢ | Open | — |
| 9/28 5:20:34 PM | BTC | DOWN | 9.4 min | 16¢ | 25% | 8¢ | ❌ Lost | -$1.70 |
| 9/28 5:18:31 PM | XRP | UP | 11.5 min | 77¢ | 83% | 5¢ | ✅ Won | $2.17 |
| 9/28 5:17:56 PM | ETH | DOWN | 12.1 min | 24¢ | 32% | 6¢ | ❌ Lost | -$2.53 |
| 9/28 5:16:31 PM | NEAR | DOWN | 13.5 min | 34¢ | 44% | 8¢ | ❌ Lost | -$3.56 |
| 9/28 5:16:23 PM | HYPE | DOWN | 13.6 min | 18¢ | 28% | 9¢ | ❌ Lost | -$1.91 |
| 9/28 5:16:13 PM | BNB | DOWN | 13.8 min | 35¢ | 49% | 12¢ | ❌ Lost | -$3.66 |
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

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
