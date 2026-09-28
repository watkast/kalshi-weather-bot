# Fair-Value Bot

*Updated Mon Sep 28, 4:47 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 654 | $119.32 | +4% | $118.77 / $0.55 |
| 4¢+ ← live bot | 631 | $248.91 | +9% | $209.36 / $39.55 |
| 6¢+ | 587 | $300.79 | +12% | $151.12 / $149.67 |
| 8¢+ | 523 | $341.80 | +17% | $105.50 / $236.30 |
| 10¢+ | 453 | $258.85 | +15% | $118.28 / $140.57 |
| 15¢+ | 272 | $239.84 | +27% | $98.67 / $141.17 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 653 | 646 | 336 (52%) | 45¢ | 53% | $363.95 | +12% | +8.8¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 244 | 110 (45%) | 68 / 176 | 8.4 | -$37.76 | -$56.96 | -5% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 213 | 79 (37%) | 87 / 126 | 7.3 | -$55.90 | -$102.87 | -12% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 53 | 14 (26%) | 21 / 32 | 2.0 | -$11.65 | -$40.10 | -22% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 75% of orders | 55 | 20 (36%) | 18 / 37 | 2.0 | -$13.69 | -$52.37 | -21% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 8 | 5 (62%) | 2 / 6 | 1.3 | -$2.84 | $8.78 | +25% |

*Model accuracy vs Kalshi's prices on the same 5,931 readings (excluding the final minute): V1 **+5.3%**, V2 **+5.1%**, 3-exchange price (V3/V4) **+3.2%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 252 | 124 (49%) | -$40.56 | -7% | 6 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+6.1%** over 17,185 readings from 666 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3171 | 2% | 4% | 6% |
| 10–20% | 1339 | 15% | 16% | 16% |
| 20–30% | 1554 | 25% | 25% | 27% |
| 30–40% | 1723 | 35% | 36% | 39% |
| 40–50% | 1707 | 45% | 48% | 52% |
| 50–60% | 1676 | 55% | 59% | 57% |
| 60–70% | 1448 | 65% | 71% | 66% |
| 70–80% | 1193 | 75% | 80% | 78% |
| 80–90% | 1019 | 85% | 88% | 80% |
| 90–100% | 2355 | 98% | 98% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 383 | 202 (53%) | 45¢ | 52% | $233.15 | +13% |
| 6–10¢ | 201 | 107 (53%) | 45¢ | 54% | $138.74 | +15% |
| 10–20¢ | 57 | 25 (44%) | 44¢ | 58% | -$7.54 | -3% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 626 | 328 (52%) | 45¢ | 53% | $352.57 | +12% |
| 5–10 min | 20 | 8 (40%) | 33¢ | 41% | $11.38 | +17% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 62 | 15 (24%) | 18¢ | 26% | $28.75 | +24% |
| Toss-up (25–75¢) | 553 | 294 (53%) | 46¢ | 54% | $312.73 | +12% |
| Favorite (75–95¢) | 31 | 27 (87%) | 79¢ | 86% | $22.47 | +9% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 72 | 38 (53%) | 43¢ | 51% | $56.58 | +17% |
| XRP | 72 | 40 (56%) | 46¢ | 53% | $59.23 | +17% |
| NEAR | 72 | 40 (56%) | 47¢ | 55% | $46.90 | +13% |
| ETH | 72 | 31 (43%) | 45¢ | 53% | -$26.99 | -8% |
| BNB | 72 | 41 (57%) | 44¢ | 53% | $83.21 | +25% |
| HYPE | 72 | 33 (46%) | 41¢ | 50% | $20.36 | +7% |
| BTC | 72 | 39 (54%) | 48¢ | 56% | $30.55 | +8% |
| ZEC | 71 | 36 (51%) | 43¢ | 51% | $44.33 | +14% |
| DOGE | 71 | 38 (54%) | 45¢ | 53% | $49.78 | +15% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 4:47:14 PM | ZEC | DOWN | 12.8 min | 34¢ | 42% | 6¢ | Open | — |
| 9/28 4:47:06 PM | XRP | UP | 12.9 min | 40¢ | 50% | 8¢ | Open | — |
| 9/28 4:47:06 PM | BTC | UP | 12.9 min | 53¢ | 65% | 10¢ | Open | — |
| 9/28 4:47:06 PM | ETH | UP | 12.9 min | 49¢ | 57% | 6¢ | Open | — |
| 9/28 4:46:52 PM | DOGE | DOWN | 13.1 min | 41¢ | 47% | 4¢ | Open | — |
| 9/28 4:46:19 PM | NEAR | DOWN | 13.7 min | 48¢ | 56% | 6¢ | Open | — |
| 9/28 4:46:11 PM | BNB | DOWN | 13.8 min | 37¢ | 45% | 7¢ | Open | — |
| 9/28 4:34:37 PM | NEAR | DOWN | 10.4 min | 56¢ | 64% | 7¢ | ❌ Lost | -$5.77 |
| 9/28 4:32:33 PM | SOL | DOWN | 12.4 min | 54¢ | 65% | 10¢ | ❌ Lost | -$5.58 |
| 9/28 4:32:33 PM | ETH | DOWN | 12.4 min | 36¢ | 49% | 12¢ | ❌ Lost | -$3.77 |
| 9/28 4:32:33 PM | DOGE | DOWN | 12.4 min | 41¢ | 58% | 15¢ | ❌ Lost | -$4.27 |
| 9/28 4:32:24 PM | XRP | DOWN | 12.6 min | 52¢ | 59% | 5¢ | ❌ Lost | -$5.42 |
| 9/28 4:31:38 PM | HYPE | DOWN | 13.4 min | 43¢ | 49% | 4¢ | ❌ Lost | -$4.48 |
| 9/28 4:31:17 PM | BNB | DOWN | 13.7 min | 48¢ | 61% | 11¢ | ❌ Lost | -$4.98 |
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

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
