# Fair-Value Bot

*Updated Mon Sep 28, 1:24 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 529 | $129.69 | +5% | $212.49 / -$82.80 |
| 4¢+ ← live bot | 511 | $153.57 | +7% | $274.68 / -$121.11 |
| 6¢+ | 477 | $169.69 | +9% | $199.72 / -$30.03 |
| 8¢+ | 425 | $177.68 | +11% | $128.71 / $48.97 |
| 10¢+ | 374 | $153.01 | +11% | $123.33 / $29.68 |
| 15¢+ | 227 | $153.91 | +21% | $114.55 / $39.36 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 538 | 529 | 272 (51%) | 44¢ | 52% | $285.35 | +12% | +10.3¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 127 | 46 (36%) | 40 / 87 | 8.5 | -$37.76 | -$135.56 | -23% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 109 | 23 (21%) | 62 / 47 | 7.3 | -$55.90 | -$199.74 | -46% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 28 | 5 (18%) | 14 / 14 | 2.0 | -$8.62 | -$36.15 | -42% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 79% of orders | 28 | 7 (25%) | 11 / 17 | 2.0 | -$10.20 | -$47.82 | -41% |

*Model accuracy vs Kalshi's prices on the same 3,044 readings (excluding the final minute): V1 **+1.8%**, V2 **+1.2%**, 3-exchange price (V3/V4) **-2.6%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 135 | 47 (35%) | -$53.39 | -26% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.8%** over 14,075 readings from 540 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2519 | 2% | 4% | 7% |
| 10–20% | 1132 | 15% | 16% | 18% |
| 20–30% | 1291 | 25% | 25% | 29% |
| 30–40% | 1381 | 35% | 36% | 41% |
| 40–50% | 1367 | 45% | 48% | 53% |
| 50–60% | 1354 | 55% | 59% | 58% |
| 60–70% | 1242 | 65% | 70% | 69% |
| 70–80% | 1015 | 75% | 80% | 80% |
| 80–90% | 844 | 85% | 88% | 84% |
| 90–100% | 1930 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 325 | 170 (52%) | 45¢ | 51% | $195.09 | +13% |
| 6–10¢ | 161 | 81 (50%) | 44¢ | 53% | $71.25 | +10% |
| 10–20¢ | 38 | 19 (50%) | 43¢ | 57% | $19.41 | +11% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 519 | 271 (52%) | 45¢ | 53% | $291.59 | +12% |
| 5–10 min | 10 | 1 (10%) | 15¢ | 23% | -$6.24 | -38% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 53 | 11 (21%) | 18¢ | 25% | $7.25 | +7% |
| Toss-up (25–75¢) | 453 | 241 (53%) | 46¢ | 54% | $260.55 | +12% |
| Favorite (75–95¢) | 23 | 20 (87%) | 78¢ | 85% | $17.55 | +10% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 59 | 32 (54%) | 45¢ | 52% | $46.89 | +17% |
| ZEC | 59 | 32 (54%) | 44¢ | 52% | $53.41 | +20% |
| XRP | 59 | 31 (53%) | 44¢ | 52% | $38.12 | +14% |
| NEAR | 59 | 34 (58%) | 47¢ | 54% | $55.01 | +19% |
| ETH | 59 | 25 (42%) | 44¢ | 51% | -$17.45 | -7% |
| DOGE | 59 | 29 (49%) | 44¢ | 52% | $20.74 | +8% |
| BTC | 59 | 32 (54%) | 47¢ | 54% | $35.39 | +12% |
| BNB | 58 | 31 (53%) | 44¢ | 53% | $45.85 | +17% |
| HYPE | 58 | 26 (45%) | 42¢ | 51% | $7.39 | +3% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 1:17:38 PM | ZEC | UP | 12.4 min | 25¢ | 31% | 5¢ | Open | — |
| 9/28 1:17:02 PM | DOGE | DOWN | 12.9 min | 68¢ | 74% | 4¢ | Open | — |
| 9/28 1:16:55 PM | ETH | DOWN | 13.1 min | 60¢ | 67% | 6¢ | Open | — |
| 9/28 1:16:42 PM | HYPE | UP | 13.3 min | 35¢ | 41% | 4¢ | Open | — |
| 9/28 1:16:33 PM | SOL | DOWN | 13.4 min | 53¢ | 60% | 5¢ | Open | — |
| 9/28 1:16:33 PM | BTC | DOWN | 13.4 min | 51¢ | 60% | 7¢ | Open | — |
| 9/28 1:16:33 PM | NEAR | DOWN | 13.4 min | 32¢ | 45% | 11¢ | Open | — |
| 9/28 1:16:24 PM | XRP | DOWN | 13.6 min | 58¢ | 64% | 4¢ | Open | — |
| 9/28 1:16:24 PM | BNB | DOWN | 13.6 min | 54¢ | 63% | 7¢ | Open | — |
| 9/28 1:02:52 PM | XRP | DOWN | 12.1 min | 87¢ | 92% | 5¢ | ✅ Won | $1.22 |
| 9/28 1:02:26 PM | BTC | DOWN | 12.6 min | 87¢ | 93% | 5¢ | ✅ Won | $1.22 |
| 9/28 1:02:17 PM | NEAR | DOWN | 12.7 min | 80¢ | 87% | 6¢ | ✅ Won | $1.88 |
| 9/28 1:01:41 PM | SOL | DOWN | 13.3 min | 76¢ | 83% | 6¢ | ✅ Won | $2.27 |
| 9/28 1:01:41 PM | DOGE | DOWN | 13.3 min | 76¢ | 84% | 7¢ | ✅ Won | $2.27 |
| 9/28 1:01:41 PM | HYPE | DOWN | 13.3 min | 77¢ | 86% | 7¢ | ✅ Won | $2.17 |
| 9/28 1:01:32 PM | ZEC | DOWN | 13.5 min | 82¢ | 94% | 11¢ | ✅ Won | $1.69 |
| 9/28 1:01:32 PM | ETH | UP | 13.5 min | 22¢ | 29% | 6¢ | ❌ Lost | -$2.33 |
| 9/28 1:01:24 PM | BNB | DOWN | 13.6 min | 63¢ | 70% | 5¢ | ✅ Won | $3.53 |
| 9/28 12:48:06 PM | SOL | DOWN | 11.9 min | 47¢ | 55% | 6¢ | ❌ Lost | -$4.88 |
| 9/28 12:48:06 PM | ETH | DOWN | 11.9 min | 31¢ | 44% | 11¢ | ❌ Lost | -$3.25 |
| 9/28 12:47:44 PM | NEAR | DOWN | 12.2 min | 47¢ | 54% | 5¢ | ❌ Lost | -$4.88 |
| 9/28 12:47:35 PM | BTC | DOWN | 12.4 min | 59¢ | 65% | 4¢ | ❌ Lost | -$6.07 |
| 9/28 12:47:05 PM | ZEC | DOWN | 12.9 min | 63¢ | 73% | 8¢ | ✅ Won | $3.53 |
| 9/28 12:46:58 PM | XRP | DOWN | 13.0 min | 45¢ | 53% | 6¢ | ❌ Lost | -$4.68 |
| 9/28 12:46:52 PM | HYPE | DOWN | 13.1 min | 50¢ | 57% | 5¢ | ❌ Lost | -$5.18 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
