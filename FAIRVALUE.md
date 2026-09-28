# Fair-Value Bot

*Updated Mon Sep 28, 1:45 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 538 | $137.65 | +5% | $215.43 / -$77.78 |
| 4¢+ ← live bot | 520 | $171.83 | +7% | $269.88 / -$98.05 |
| 6¢+ | 485 | $186.93 | +9% | $197.69 / -$10.76 |
| 8¢+ | 431 | $191.54 | +12% | $122.81 / $68.73 |
| 10¢+ | 377 | $160.99 | +12% | $122.37 / $38.62 |
| 15¢+ | 227 | $153.91 | +21% | $114.55 / $39.36 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 547 | 538 | 278 (52%) | 44¢ | 52% | $300.24 | +12% | +10.2¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 136 | 52 (38%) | 42 / 94 | 8.5 | -$37.76 | -$120.67 | -19% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 117 | 30 (26%) | 62 / 55 | 7.3 | -$55.90 | -$173.34 | -37% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 30 | 6 (20%) | 15 / 15 | 2.0 | -$8.62 | -$33.84 | -36% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 80% of orders | 30 | 8 (27%) | 12 / 18 | 2.0 | -$10.20 | -$47.32 | -37% |

*Model accuracy vs Kalshi's prices on the same 3,242 readings (excluding the final minute): V1 **+2.1%**, V2 **+1.6%**, 3-exchange price (V3/V4) **-2.6%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 144 | 50 (35%) | -$56.65 | -26% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.0%** over 14,291 readings from 549 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2585 | 2% | 4% | 7% |
| 10–20% | 1161 | 15% | 16% | 18% |
| 20–30% | 1335 | 25% | 25% | 28% |
| 30–40% | 1429 | 35% | 36% | 40% |
| 40–50% | 1389 | 45% | 48% | 53% |
| 50–60% | 1354 | 55% | 59% | 58% |
| 60–70% | 1243 | 65% | 70% | 69% |
| 70–80% | 1016 | 75% | 80% | 80% |
| 80–90% | 845 | 85% | 88% | 84% |
| 90–100% | 1934 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 331 | 174 (53%) | 45¢ | 51% | $204.20 | +13% |
| 6–10¢ | 163 | 83 (51%) | 44¢ | 53% | $80.39 | +11% |
| 10–20¢ | 39 | 19 (49%) | 43¢ | 57% | $16.05 | +9% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 528 | 277 (52%) | 45¢ | 53% | $306.48 | +12% |
| 5–10 min | 10 | 1 (10%) | 15¢ | 23% | -$6.24 | -38% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 53 | 11 (21%) | 18¢ | 25% | $7.25 | +7% |
| Toss-up (25–75¢) | 462 | 247 (53%) | 46¢ | 54% | $275.44 | +13% |
| Favorite (75–95¢) | 23 | 20 (87%) | 78¢ | 85% | $17.55 | +10% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 60 | 33 (55%) | 45¢ | 52% | $51.41 | +18% |
| ZEC | 60 | 32 (53%) | 43¢ | 51% | $50.77 | +19% |
| XRP | 60 | 32 (53%) | 45¢ | 52% | $42.14 | +15% |
| NEAR | 60 | 34 (57%) | 46¢ | 54% | $51.65 | +18% |
| ETH | 60 | 26 (43%) | 44¢ | 52% | -$13.62 | -5% |
| DOGE | 60 | 30 (50%) | 44¢ | 52% | $23.78 | +9% |
| BTC | 60 | 33 (55%) | 47¢ | 55% | $40.11 | +14% |
| BNB | 59 | 32 (54%) | 44¢ | 53% | $50.27 | +19% |
| HYPE | 59 | 26 (44%) | 42¢ | 50% | $3.73 | +1% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 1:35:37 PM | NEAR | DOWN | 9.4 min | 86¢ | 93% | 6¢ | Open | — |
| 9/28 1:32:17 PM | HYPE | DOWN | 12.7 min | 26¢ | 33% | 6¢ | Open | — |
| 9/28 1:31:53 PM | SOL | DOWN | 13.1 min | 49¢ | 57% | 6¢ | Open | — |
| 9/28 1:31:53 PM | ZEC | DOWN | 13.1 min | 32¢ | 40% | 6¢ | Open | — |
| 9/28 1:31:22 PM | DOGE | DOWN | 13.6 min | 55¢ | 61% | 4¢ | Open | — |
| 9/28 1:31:14 PM | BTC | DOWN | 13.8 min | 58¢ | 66% | 6¢ | Open | — |
| 9/28 1:31:14 PM | XRP | DOWN | 13.8 min | 60¢ | 67% | 5¢ | Open | — |
| 9/28 1:31:14 PM | ETH | DOWN | 13.8 min | 61¢ | 68% | 5¢ | Open | — |
| 9/28 1:31:14 PM | BNB | DOWN | 13.8 min | 51¢ | 63% | 11¢ | Open | — |
| 9/28 1:17:38 PM | ZEC | UP | 12.4 min | 25¢ | 31% | 5¢ | ❌ Lost | -$2.64 |
| 9/28 1:17:02 PM | DOGE | DOWN | 12.9 min | 68¢ | 74% | 4¢ | ✅ Won | $3.04 |
| 9/28 1:16:55 PM | ETH | DOWN | 13.1 min | 60¢ | 67% | 6¢ | ✅ Won | $3.83 |
| 9/28 1:16:42 PM | HYPE | UP | 13.3 min | 35¢ | 41% | 4¢ | ❌ Lost | -$3.66 |
| 9/28 1:16:33 PM | SOL | DOWN | 13.4 min | 53¢ | 60% | 5¢ | ✅ Won | $4.52 |
| 9/28 1:16:33 PM | BTC | DOWN | 13.4 min | 51¢ | 60% | 7¢ | ✅ Won | $4.72 |
| 9/28 1:16:33 PM | NEAR | DOWN | 13.4 min | 32¢ | 45% | 11¢ | ❌ Lost | -$3.36 |
| 9/28 1:16:24 PM | XRP | DOWN | 13.6 min | 58¢ | 64% | 4¢ | ✅ Won | $4.02 |
| 9/28 1:16:24 PM | BNB | DOWN | 13.6 min | 54¢ | 63% | 7¢ | ✅ Won | $4.42 |
| 9/28 1:02:52 PM | XRP | DOWN | 12.1 min | 87¢ | 92% | 5¢ | ✅ Won | $1.22 |
| 9/28 1:02:26 PM | BTC | DOWN | 12.6 min | 87¢ | 93% | 5¢ | ✅ Won | $1.22 |
| 9/28 1:02:17 PM | NEAR | DOWN | 12.7 min | 80¢ | 87% | 6¢ | ✅ Won | $1.88 |
| 9/28 1:01:41 PM | SOL | DOWN | 13.3 min | 76¢ | 83% | 6¢ | ✅ Won | $2.27 |
| 9/28 1:01:41 PM | DOGE | DOWN | 13.3 min | 76¢ | 84% | 7¢ | ✅ Won | $2.27 |
| 9/28 1:01:41 PM | HYPE | DOWN | 13.3 min | 77¢ | 86% | 7¢ | ✅ Won | $2.17 |
| 9/28 1:01:32 PM | ZEC | DOWN | 13.5 min | 82¢ | 94% | 11¢ | ✅ Won | $1.69 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
