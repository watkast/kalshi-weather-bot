# Fair-Value Bot

*Updated Mon Sep 28, 11:53 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **6¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **6¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 475 | $117.88 | +5% | $237.33 / -$119.45 |
| 4¢+ ← live bot | 460 | $183.12 | +9% | $294.28 / -$111.16 |
| 6¢+ | 436 | $204.30 | +12% | $217.90 / -$13.60 |
| 8¢+ | 391 | $192.96 | +13% | $142.59 / $50.37 |
| 10¢+ | 344 | $198.70 | +16% | $125.47 / $73.23 |
| 15¢+ | 213 | $177.93 | +26% | $123.60 / $54.33 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 484 | 475 | 245 (52%) | 44¢ | 52% | $279.36 | +13% | +11.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 73 | 19 (26%) | 19 / 54 | 8.1 | -$37.18 | -$141.55 | -43% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 69 | 17 (25%) | 42 / 27 | 7.7 | -$55.90 | -$115.19 | -40% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 18 | 4 (22%) | 9 / 9 | 2.0 | -$8.62 | -$17.13 | -30% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 81% of orders | 16 | 3 (19%) | 7 / 9 | 2.0 | -$10.20 | -$35.22 | -54% |

*Model accuracy vs Kalshi's prices on the same 1,800 readings (excluding the final minute): V1 **+0.9%**, V2 **+1.3%**, 3-exchange price (V3/V4) **-4.4%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 81 | 32 (40%) | -$55.43 | -41% | 0 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.3%** over 12,723 readings from 486 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 2132 | 2% | 4% | 9% |
| 10–20% | 994 | 15% | 16% | 20% |
| 20–30% | 1129 | 25% | 26% | 33% |
| 30–40% | 1226 | 35% | 36% | 44% |
| 40–50% | 1231 | 45% | 48% | 53% |
| 50–60% | 1251 | 55% | 59% | 57% |
| 60–70% | 1171 | 65% | 70% | 67% |
| 70–80% | 969 | 75% | 80% | 80% |
| 80–90% | 818 | 85% | 88% | 83% |
| 90–100% | 1802 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 294 | 157 (53%) | 45¢ | 52% | $197.11 | +14% |
| 6–10¢ | 142 | 69 (49%) | 43¢ | 52% | $61.83 | +10% |
| 10–20¢ | 34 | 17 (50%) | 42¢ | 56% | $20.82 | +14% |
| 20¢+ | 5 | 2 (40%) | 39¢ | 64% | -$0.40 | -2% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 467 | 244 (52%) | 45¢ | 53% | $282.52 | +13% |
| 5–10 min | 8 | 1 (12%) | 16¢ | 24% | -$3.16 | -24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 46 | 11 (24%) | 18¢ | 25% | $20.50 | +23% |
| Toss-up (25–75¢) | 414 | 222 (54%) | 46¢ | 54% | $256.39 | +13% |
| Favorite (75–95¢) | 15 | 12 (80%) | 77¢ | 84% | $2.47 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 53 | 29 (55%) | 44¢ | 51% | $49.24 | +20% |
| ZEC | 53 | 28 (53%) | 42¢ | 50% | $48.20 | +21% |
| XRP | 53 | 26 (49%) | 44¢ | 52% | $17.85 | +7% |
| NEAR | 53 | 32 (60%) | 47¢ | 55% | $62.30 | +24% |
| ETH | 53 | 23 (43%) | 45¢ | 53% | -$17.60 | -7% |
| DOGE | 53 | 26 (49%) | 44¢ | 51% | $20.99 | +9% |
| BTC | 53 | 29 (55%) | 46¢ | 53% | $39.89 | +16% |
| BNB | 52 | 28 (54%) | 43¢ | 52% | $47.55 | +20% |
| HYPE | 52 | 24 (46%) | 42¢ | 51% | $10.94 | +5% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 11:48:32 AM | BTC | UP | 11.4 min | 31¢ | 38% | 6¢ | Open | — |
| 9/28 11:48:26 AM | XRP | UP | 11.6 min | 36¢ | 42% | 4¢ | Open | — |
| 9/28 11:48:18 AM | NEAR | DOWN | 11.7 min | 53¢ | 59% | 4¢ | Open | — |
| 9/28 11:47:58 AM | DOGE | UP | 12.0 min | 26¢ | 32% | 4¢ | Open | — |
| 9/28 11:47:23 AM | SOL | UP | 12.6 min | 39¢ | 45% | 5¢ | Open | — |
| 9/28 11:47:01 AM | HYPE | UP | 13.0 min | 21¢ | 26% | 4¢ | Open | — |
| 9/28 11:46:41 AM | ETH | UP | 13.3 min | 36¢ | 43% | 5¢ | Open | — |
| 9/28 11:46:05 AM | ZEC | DOWN | 13.9 min | 42¢ | 48% | 5¢ | Open | — |
| 9/28 11:46:05 AM | BNB | DOWN | 13.9 min | 50¢ | 61% | 9¢ | Open | — |
| 9/28 11:38:25 AM | ZEC | UP | 6.6 min | 20¢ | 26% | 5¢ | ✅ Won | $7.88 |
| 9/28 11:33:34 AM | BTC | DOWN | 11.4 min | 39¢ | 45% | 5¢ | ❌ Lost | -$4.07 |
| 9/28 11:32:36 AM | NEAR | DOWN | 12.4 min | 44¢ | 50% | 4¢ | ✅ Won | $5.42 |
| 9/28 11:32:16 AM | XRP | DOWN | 12.7 min | 26¢ | 32% | 5¢ | ❌ Lost | -$2.74 |
| 9/28 11:32:06 AM | ETH | DOWN | 12.9 min | 34¢ | 40% | 4¢ | ❌ Lost | -$3.56 |
| 9/28 11:31:51 AM | HYPE | DOWN | 13.2 min | 46¢ | 52% | 4¢ | ✅ Won | $5.22 |
| 9/28 11:31:31 AM | SOL | DOWN | 13.5 min | 35¢ | 42% | 5¢ | ❌ Lost | -$3.66 |
| 9/28 11:31:31 AM | DOGE | DOWN | 13.5 min | 38¢ | 45% | 5¢ | ❌ Lost | -$3.97 |
| 9/28 11:31:14 AM | BNB | DOWN | 13.8 min | 33¢ | 42% | 7¢ | ❌ Lost | -$3.46 |
| 9/28 11:18:00 AM | XRP | UP | 12.0 min | 40¢ | 50% | 9¢ | ❌ Lost | -$4.17 |
| 9/28 11:16:58 AM | ZEC | UP | 13.0 min | 55¢ | 62% | 5¢ | ❌ Lost | -$5.68 |
| 9/28 11:16:42 AM | SOL | UP | 13.3 min | 61¢ | 71% | 8¢ | ❌ Lost | -$6.27 |
| 9/28 11:16:42 AM | BTC | UP | 13.3 min | 58¢ | 67% | 7¢ | ❌ Lost | -$5.98 |
| 9/28 11:16:42 AM | ETH | UP | 13.3 min | 55¢ | 66% | 9¢ | ❌ Lost | -$5.68 |
| 9/28 11:16:31 AM | BNB | DOWN | 13.5 min | 48¢ | 61% | 11¢ | ✅ Won | $5.02 |
| 9/28 11:16:31 AM | NEAR | DOWN | 13.5 min | 53¢ | 61% | 6¢ | ✅ Won | $4.52 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
