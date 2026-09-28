# Fair-Value Bot

*Updated Mon Sep 28, 9:41 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **4¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 394 | $246.87 | +13% | $245.38 / $1.49 |
| 4¢+ ← live bot | 381 | $282.11 | +17% | $336.90 / -$54.79 |
| 6¢+ | 364 | $247.51 | +17% | $260.00 / -$12.49 |
| 8¢+ | 332 | $184.84 | +15% | $188.60 / -$3.76 |
| 10¢+ | 299 | $198.13 | +18% | $179.88 / $18.25 |
| 15¢+ | 194 | $186.01 | +30% | $140.65 / $45.36 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 403 | 394 | 220 (56%) | 44¢ | 52% | $390.53 | +22% | +12.6¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade.*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 0 | — | 0 / 0 | — | — | — | — |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 0 | — | 0 / 0 | — | — | — | — |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 0 | — | 0 / 0 | — | — | — | — |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled — of orders | 0 | — | 0 / 0 | — | — | — | — |

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.3%** over 10,773 readings from 405 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1880 | 2% | 4% | 8% |
| 10–20% | 829 | 15% | 16% | 18% |
| 20–30% | 886 | 25% | 26% | 33% |
| 30–40% | 991 | 35% | 36% | 44% |
| 40–50% | 1031 | 45% | 48% | 52% |
| 50–60% | 1058 | 55% | 59% | 55% |
| 60–70% | 1009 | 65% | 70% | 64% |
| 70–80% | 875 | 75% | 79% | 78% |
| 80–90% | 722 | 85% | 88% | 81% |
| 90–100% | 1492 | 97% | 97% | 95% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 256 | 142 (55%) | 45¢ | 52% | $218.82 | +18% |
| 6–10¢ | 109 | 62 (57%) | 42¢ | 51% | $142.59 | +30% |
| 10–20¢ | 26 | 14 (54%) | 43¢ | 58% | $23.12 | +20% |
| 20¢+ | 3 | 2 (67%) | 45¢ | 69% | $6.00 | +43% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 390 | 220 (56%) | 45¢ | 53% | $394.91 | +22% |
| 5–10 min | 4 | 0 (0%) | 10¢ | 17% | -$4.38 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 38 | 8 (21%) | 18¢ | 25% | $8.28 | +12% |
| Toss-up (25–75¢) | 344 | 201 (58%) | 46¢ | 54% | $366.01 | +22% |
| Favorite (75–95¢) | 12 | 11 (92%) | 77¢ | 83% | $16.24 | +17% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 44 | 27 (61%) | 43¢ | 51% | $73.63 | +37% |
| ZEC | 44 | 24 (55%) | 43¢ | 51% | $41.89 | +21% |
| XRP | 44 | 25 (57%) | 47¢ | 54% | $37.83 | +18% |
| NEAR | 44 | 27 (61%) | 46¢ | 54% | $61.08 | +29% |
| ETH | 44 | 21 (48%) | 44¢ | 52% | $9.64 | +5% |
| DOGE | 44 | 24 (55%) | 44¢ | 52% | $38.35 | +19% |
| BTC | 44 | 27 (61%) | 47¢ | 55% | $55.18 | +26% |
| BNB | 43 | 24 (56%) | 42¢ | 51% | $52.62 | +28% |
| HYPE | 43 | 21 (49%) | 43¢ | 51% | $20.31 | +11% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 9:35:12 AM | ZEC | UP | 9.8 min | 26¢ | 43% | 16¢ | Open | — |
| 9/28 9:34:10 AM | BNB | UP | 10.8 min | 39¢ | 45% | 4¢ | Open | — |
| 9/28 9:32:36 AM | NEAR | DOWN | 12.4 min | 37¢ | 43% | 4¢ | Open | — |
| 9/28 9:32:17 AM | DOGE | UP | 12.7 min | 33¢ | 41% | 7¢ | Open | — |
| 9/28 9:32:17 AM | ETH | UP | 12.7 min | 38¢ | 49% | 10¢ | Open | — |
| 9/28 9:32:17 AM | XRP | UP | 12.7 min | 32¢ | 41% | 8¢ | Open | — |
| 9/28 9:32:17 AM | BTC | UP | 12.7 min | 36¢ | 44% | 6¢ | Open | — |
| 9/28 9:32:17 AM | HYPE | UP | 12.7 min | 34¢ | 43% | 7¢ | Open | — |
| 9/28 9:32:17 AM | SOL | UP | 12.7 min | 34¢ | 43% | 8¢ | Open | — |
| 9/28 9:18:26 AM | DOGE | UP | 11.6 min | 25¢ | 31% | 5¢ | ✅ Won | $7.36 |
| 9/28 9:18:03 AM | NEAR | UP | 11.9 min | 26¢ | 32% | 5¢ | ✅ Won | $7.26 |
| 9/28 9:17:49 AM | HYPE | UP | 12.2 min | 26¢ | 32% | 4¢ | ✅ Won | $7.26 |
| 9/28 9:17:35 AM | BTC | DOWN | 12.4 min | 63¢ | 70% | 5¢ | ❌ Lost | -$6.47 |
| 9/28 9:17:22 AM | ETH | DOWN | 12.6 min | 56¢ | 63% | 5¢ | ❌ Lost | -$5.78 |
| 9/28 9:16:33 AM | XRP | DOWN | 13.4 min | 53¢ | 59% | 4¢ | ❌ Lost | -$5.48 |
| 9/28 9:16:21 AM | ZEC | UP | 13.6 min | 32¢ | 38% | 4¢ | ❌ Lost | -$3.36 |
| 9/28 9:16:07 AM | SOL | DOWN | 13.9 min | 47¢ | 53% | 4¢ | ❌ Lost | -$4.88 |
| 9/28 9:16:05 AM | BNB | DOWN | 13.9 min | 53¢ | 60% | 5¢ | ❌ Lost | -$5.48 |
| 9/28 9:01:59 AM | NEAR | DOWN | 13.0 min | 45¢ | 52% | 5¢ | ✅ Won | $5.32 |
| 9/28 9:01:51 AM | HYPE | DOWN | 13.1 min | 38¢ | 45% | 5¢ | ❌ Lost | -$3.97 |
| 9/28 9:01:31 AM | ZEC | DOWN | 13.5 min | 47¢ | 54% | 5¢ | ✅ Won | $5.12 |
| 9/28 9:01:31 AM | DOGE | DOWN | 13.5 min | 36¢ | 42% | 5¢ | ❌ Lost | -$3.77 |
| 9/28 9:01:19 AM | BNB | DOWN | 13.7 min | 36¢ | 47% | 9¢ | ❌ Lost | -$3.77 |
| 9/28 9:01:15 AM | SOL | DOWN | 13.8 min | 34¢ | 40% | 4¢ | ✅ Won | $6.44 |
| 9/28 9:01:15 AM | ETH | DOWN | 13.8 min | 37¢ | 44% | 5¢ | ✅ Won | $6.13 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
