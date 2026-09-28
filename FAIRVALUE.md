# Fair-Value Bot

*Updated Mon Sep 28, 4:06 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 627 | $181.84 | +6% | $158.92 / $22.92 |
| 4¢+ ← live bot | 605 | $287.05 | +10% | $244.55 / $42.50 |
| 6¢+ | 564 | $321.75 | +14% | $162.28 / $159.47 |
| 8¢+ | 501 | $352.65 | +18% | $99.48 / $253.17 |
| 10¢+ | 437 | $267.71 | +16% | $104.37 / $163.34 |
| 15¢+ | 264 | $231.24 | +27% | $97.44 / $133.80 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 630 | 621 | 329 (53%) | 45¢ | 53% | $419.45 | +15% | +9.6¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 219 | 103 (47%) | 66 / 153 | 8.4 | -$37.76 | -$1.46 | -0% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 192 | 72 (38%) | 86 / 106 | 7.4 | -$55.90 | -$64.90 | -8% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 47 | 12 (26%) | 20 / 27 | 2.0 | -$11.65 | -$35.47 | -23% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 73% of orders | 49 | 19 (39%) | 18 / 31 | 2.0 | -$13.69 | -$30.08 | -14% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 4 | 3 (75%) | 1 / 3 | 1.3 | -$0.34 | $9.10 | +52% |

*Model accuracy vs Kalshi's prices on the same 5,306 readings (excluding the final minute): V1 **+5.8%**, V2 **+5.8%**, 3-exchange price (V3/V4) **+3.5%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 227 | 99 (44%) | $14.94 | +3% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+6.2%** over 16,510 readings from 639 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3048 | 2% | 4% | 7% |
| 10–20% | 1308 | 15% | 16% | 17% |
| 20–30% | 1521 | 25% | 25% | 28% |
| 30–40% | 1694 | 35% | 36% | 39% |
| 40–50% | 1644 | 45% | 47% | 51% |
| 50–60% | 1603 | 55% | 59% | 55% |
| 60–70% | 1395 | 65% | 71% | 65% |
| 70–80% | 1146 | 75% | 80% | 77% |
| 80–90% | 982 | 85% | 88% | 79% |
| 90–100% | 2169 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 373 | 199 (53%) | 45¢ | 51% | $252.86 | +15% |
| 6–10¢ | 191 | 104 (54%) | 44¢ | 53% | $160.76 | +18% |
| 10–20¢ | 52 | 24 (46%) | 43¢ | 58% | $6.23 | +3% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 601 | 321 (53%) | 45¢ | 53% | $408.07 | +15% |
| 5–10 min | 20 | 8 (40%) | 33¢ | 41% | $11.38 | +17% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 61 | 15 (25%) | 19¢ | 26% | $30.01 | +25% |
| Toss-up (25–75¢) | 531 | 289 (54%) | 46¢ | 54% | $371.31 | +15% |
| Favorite (75–95¢) | 29 | 25 (86%) | 79¢ | 86% | $18.13 | +8% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BTC | 70 | 38 (54%) | 48¢ | 56% | $33.29 | +10% |
| SOL | 69 | 37 (54%) | 43¢ | 51% | $61.50 | +20% |
| ZEC | 69 | 36 (52%) | 43¢ | 51% | $51.65 | +17% |
| XRP | 69 | 39 (57%) | 45¢ | 53% | $66.48 | +21% |
| NEAR | 69 | 40 (58%) | 47¢ | 55% | $62.32 | +18% |
| ETH | 69 | 30 (43%) | 45¢ | 53% | -$21.61 | -7% |
| BNB | 69 | 39 (57%) | 43¢ | 53% | $79.64 | +26% |
| HYPE | 69 | 33 (48%) | 42¢ | 51% | $29.43 | +10% |
| DOGE | 68 | 37 (54%) | 44¢ | 52% | $56.75 | +18% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 4:02:35 PM | NEAR | DOWN | 12.4 min | 55¢ | 61% | 4¢ | Open | — |
| 9/28 4:02:26 PM | HYPE | UP | 12.6 min | 12¢ | 18% | 5¢ | Open | — |
| 9/28 4:02:26 PM | ZEC | UP | 12.6 min | 41¢ | 48% | 5¢ | Open | — |
| 9/28 4:02:01 PM | SOL | DOWN | 13.0 min | 57¢ | 63% | 4¢ | Open | — |
| 9/28 4:01:55 PM | ETH | DOWN | 13.1 min | 75¢ | 81% | 5¢ | Open | — |
| 9/28 4:01:33 PM | BNB | DOWN | 13.4 min | 62¢ | 72% | 8¢ | Open | — |
| 9/28 4:01:13 PM | BTC | DOWN | 13.8 min | 61¢ | 74% | 12¢ | Open | — |
| 9/28 4:01:13 PM | XRP | DOWN | 13.8 min | 72¢ | 79% | 6¢ | Open | — |
| 9/28 4:01:13 PM | DOGE | DOWN | 13.8 min | 79¢ | 87% | 7¢ | Open | — |
| 9/28 3:50:50 PM | ETH | DOWN | 9.2 min | 77¢ | 85% | 6¢ | ✅ Won | $2.17 |
| 9/28 3:50:17 PM | NEAR | DOWN | 9.7 min | 57¢ | 65% | 6¢ | ✅ Won | $4.12 |
| 9/28 3:48:38 PM | BTC | DOWN | 11.4 min | 62¢ | 68% | 4¢ | ✅ Won | $3.63 |
| 9/28 3:48:38 PM | XRP | DOWN | 11.4 min | 82¢ | 89% | 6¢ | ✅ Won | $1.69 |
| 9/28 3:47:22 PM | DOGE | DOWN | 12.6 min | 72¢ | 81% | 8¢ | ✅ Won | $2.65 |
| 9/28 3:47:08 PM | SOL | UP | 12.8 min | 24¢ | 32% | 7¢ | ❌ Lost | -$2.53 |
| 9/28 3:47:01 PM | HYPE | UP | 13.0 min | 27¢ | 39% | 10¢ | ❌ Lost | -$2.84 |
| 9/28 3:46:47 PM | BNB | UP | 13.2 min | 39¢ | 55% | 14¢ | ❌ Lost | -$4.07 |
| 9/28 3:46:15 PM | ZEC | UP | 13.8 min | 36¢ | 47% | 10¢ | ✅ Won | $6.25 |
| 9/28 3:39:36 PM | SOL | UP | 5.4 min | 12¢ | 18% | 5¢ | ❌ Lost | -$1.28 |
| 9/28 3:36:51 PM | BTC | UP | 8.1 min | 59¢ | 65% | 4¢ | ❌ Lost | -$6.07 |
| 9/28 3:35:11 PM | XRP | DOWN | 9.8 min | 36¢ | 42% | 4¢ | ✅ Won | $6.21 |
| 9/28 3:34:44 PM | DOGE | DOWN | 10.2 min | 44¢ | 53% | 8¢ | ✅ Won | $5.42 |
| 9/28 3:34:27 PM | NEAR | DOWN | 10.6 min | 32¢ | 40% | 7¢ | ✅ Won | $6.64 |
| 9/28 3:33:03 PM | HYPE | DOWN | 11.9 min | 45¢ | 52% | 5¢ | ✅ Won | $5.32 |
| 9/28 3:31:36 PM | ZEC | DOWN | 13.4 min | 46¢ | 52% | 5¢ | ❌ Lost | -$4.76 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
