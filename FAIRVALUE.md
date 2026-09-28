# Fair-Value Bot

*Updated Mon Sep 28, 4:37 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 645 | $158.64 | +5% | $145.93 / $12.71 |
| 4¢+ ← live bot | 623 | $270.41 | +9% | $224.08 / $46.33 |
| 6¢+ | 581 | $315.16 | +13% | $162.42 / $152.74 |
| 8¢+ | 518 | $351.59 | +18% | $103.84 / $247.75 |
| 10¢+ | 449 | $267.64 | +16% | $124.34 / $143.30 |
| 15¢+ | 270 | $240.10 | +27% | $91.51 / $148.59 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 646 | 639 | 336 (53%) | 45¢ | 53% | $398.22 | +13% | +9.2¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 237 | 110 (46%) | 68 / 169 | 8.5 | -$37.76 | -$22.69 | -2% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 209 | 79 (38%) | 87 / 122 | 7.5 | -$55.90 | -$88.15 | -10% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 51 | 14 (27%) | 21 / 30 | 2.0 | -$11.65 | -$36.16 | -21% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 74% of orders | 53 | 20 (38%) | 18 / 35 | 2.0 | -$13.69 | -$43.27 | -18% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 7 | 5 (71%) | 2 / 5 | 1.4 | -$2.14 | $11.62 | +35% |

*Model accuracy vs Kalshi's prices on the same 5,724 readings (excluding the final minute): V1 **+5.5%**, V2 **+5.3%**, 3-exchange price (V3/V4) **+3.4%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 245 | 117 (48%) | -$6.29 | -1% | 3 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+6.2%** over 16,960 readings from 657 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3171 | 2% | 4% | 6% |
| 10–20% | 1339 | 15% | 16% | 16% |
| 20–30% | 1554 | 25% | 25% | 27% |
| 30–40% | 1716 | 35% | 36% | 39% |
| 40–50% | 1695 | 45% | 48% | 51% |
| 50–60% | 1661 | 55% | 59% | 56% |
| 60–70% | 1438 | 65% | 71% | 66% |
| 70–80% | 1174 | 75% | 80% | 77% |
| 80–90% | 1003 | 85% | 88% | 79% |
| 90–100% | 2209 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 381 | 202 (53%) | 45¢ | 52% | $243.05 | +14% |
| 6–10¢ | 199 | 107 (54%) | 45¢ | 54% | $150.09 | +16% |
| 10–20¢ | 54 | 25 (46%) | 44¢ | 58% | $5.48 | +2% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 619 | 328 (53%) | 45¢ | 53% | $386.84 | +13% |
| 5–10 min | 20 | 8 (40%) | 33¢ | 41% | $11.38 | +17% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 62 | 15 (24%) | 18¢ | 26% | $28.75 | +24% |
| Toss-up (25–75¢) | 546 | 294 (54%) | 46¢ | 54% | $347.00 | +13% |
| Favorite (75–95¢) | 31 | 27 (87%) | 79¢ | 86% | $22.47 | +9% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BTC | 72 | 39 (54%) | 48¢ | 56% | $30.55 | +8% |
| SOL | 71 | 38 (54%) | 43¢ | 51% | $62.16 | +20% |
| ZEC | 71 | 36 (51%) | 43¢ | 51% | $44.33 | +14% |
| XRP | 71 | 40 (56%) | 46¢ | 53% | $64.65 | +19% |
| NEAR | 71 | 40 (56%) | 47¢ | 55% | $52.67 | +15% |
| ETH | 71 | 31 (44%) | 45¢ | 53% | -$23.22 | -7% |
| BNB | 71 | 41 (58%) | 44¢ | 53% | $88.19 | +27% |
| HYPE | 71 | 33 (46%) | 41¢ | 50% | $24.84 | +8% |
| DOGE | 70 | 38 (54%) | 45¢ | 53% | $54.05 | +17% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 4:34:37 PM | NEAR | DOWN | 10.4 min | 56¢ | 64% | 7¢ | Open | — |
| 9/28 4:32:33 PM | SOL | DOWN | 12.4 min | 54¢ | 65% | 10¢ | Open | — |
| 9/28 4:32:33 PM | ETH | DOWN | 12.4 min | 36¢ | 49% | 12¢ | Open | — |
| 9/28 4:32:33 PM | DOGE | DOWN | 12.4 min | 41¢ | 58% | 15¢ | Open | — |
| 9/28 4:32:24 PM | XRP | DOWN | 12.6 min | 52¢ | 59% | 5¢ | Open | — |
| 9/28 4:31:38 PM | HYPE | DOWN | 13.4 min | 43¢ | 49% | 4¢ | Open | — |
| 9/28 4:31:17 PM | BNB | DOWN | 13.7 min | 48¢ | 61% | 11¢ | Open | — |
| 9/28 4:18:20 PM | HYPE | DOWN | 11.7 min | 32¢ | 41% | 8¢ | ❌ Lost | -$3.33 |
| 9/28 4:18:13 PM | NEAR | DOWN | 11.8 min | 38¢ | 46% | 7¢ | ❌ Lost | -$3.97 |
| 9/28 4:17:44 PM | SOL | DOWN | 12.3 min | 33¢ | 43% | 8¢ | ❌ Lost | -$3.46 |
| 9/28 4:17:29 PM | ETH | DOWN | 12.5 min | 38¢ | 49% | 9¢ | ❌ Lost | -$3.97 |
| 9/28 4:17:29 PM | DOGE | DOWN | 12.5 min | 45¢ | 53% | 6¢ | ❌ Lost | -$4.68 |
| 9/28 4:17:29 PM | BNB | DOWN | 12.5 min | 49¢ | 60% | 9¢ | ✅ Won | $4.92 |
| 9/28 4:17:14 PM | XRP | DOWN | 12.8 min | 43¢ | 55% | 10¢ | ❌ Lost | -$4.48 |
| 9/28 4:17:07 PM | ZEC | DOWN | 12.9 min | 29¢ | 35% | 5¢ | ❌ Lost | -$3.03 |
| 9/28 4:16:06 PM | BTC | DOWN | 13.9 min | 63¢ | 71% | 6¢ | ❌ Lost | -$6.47 |
| 9/28 4:02:35 PM | NEAR | DOWN | 12.4 min | 55¢ | 61% | 4¢ | ❌ Lost | -$5.68 |
| 9/28 4:02:26 PM | HYPE | UP | 12.6 min | 12¢ | 18% | 5¢ | ❌ Lost | -$1.26 |
| 9/28 4:02:26 PM | ZEC | UP | 12.6 min | 41¢ | 48% | 5¢ | ❌ Lost | -$4.29 |
| 9/28 4:02:01 PM | SOL | DOWN | 13.0 min | 57¢ | 63% | 4¢ | ✅ Won | $4.12 |
| 9/28 4:01:55 PM | ETH | DOWN | 13.1 min | 75¢ | 81% | 5¢ | ✅ Won | $2.36 |
| 9/28 4:01:33 PM | BNB | DOWN | 13.4 min | 62¢ | 72% | 8¢ | ✅ Won | $3.63 |
| 9/28 4:01:13 PM | BTC | DOWN | 13.8 min | 61¢ | 74% | 12¢ | ✅ Won | $3.73 |
| 9/28 4:01:13 PM | XRP | DOWN | 13.8 min | 72¢ | 79% | 6¢ | ✅ Won | $2.65 |
| 9/28 4:01:13 PM | DOGE | DOWN | 13.8 min | 79¢ | 87% | 7¢ | ✅ Won | $1.98 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
