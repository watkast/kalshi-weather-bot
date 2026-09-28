# Fair-Value Bot

*Updated Mon Sep 28, 8:23 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **4¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 349 | $140.89 | +8% | $215.19 / -$74.30 |
| 4¢+ ← live bot | 336 | $197.81 | +13% | $287.11 / -$89.30 |
| 6¢+ | 319 | $145.69 | +11% | $235.62 / -$89.93 |
| 8¢+ | 288 | $72.94 | +7% | $185.29 / -$112.35 |
| 10¢+ | 256 | $85.56 | +9% | $178.33 / -$92.77 |
| 15¢+ | 161 | $86.57 | +16% | $167.05 / -$80.48 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 358 | 349 | 191 (55%) | 44¢ | 52% | $304.55 | +19% | +13.8¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+2.0%** over 9,540 readings from 360 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1748 | 2% | 4% | 8% |
| 10–20% | 787 | 15% | 16% | 18% |
| 20–30% | 778 | 25% | 26% | 33% |
| 30–40% | 848 | 35% | 36% | 45% |
| 40–50% | 866 | 45% | 48% | 53% |
| 50–60% | 854 | 55% | 58% | 58% |
| 60–70% | 854 | 65% | 70% | 68% |
| 70–80% | 789 | 75% | 79% | 82% |
| 80–90% | 629 | 85% | 87% | 89% |
| 90–100% | 1387 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 219 | 119 (54%) | 46¢ | 52% | $156.67 | +15% |
| 6–10¢ | 105 | 60 (57%) | 42¢ | 51% | $140.33 | +31% |
| 10–20¢ | 22 | 10 (45%) | 43¢ | 58% | $1.55 | +2% |
| 20¢+ | 3 | 2 (67%) | 45¢ | 69% | $6.00 | +43% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 345 | 191 (55%) | 45¢ | 53% | $308.93 | +19% |
| 5–10 min | 4 | 0 (0%) | 10¢ | 17% | -$4.38 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 37 | 8 (22%) | 18¢ | 25% | $10.61 | +15% |
| Toss-up (25–75¢) | 301 | 173 (57%) | 46¢ | 55% | $280.06 | +19% |
| Favorite (75–95¢) | 11 | 10 (91%) | 77¢ | 84% | $13.88 | +16% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 39 | 23 (59%) | 43¢ | 51% | $56.34 | +32% |
| ZEC | 39 | 21 (54%) | 44¢ | 51% | $33.57 | +19% |
| XRP | 39 | 21 (54%) | 46¢ | 54% | $23.00 | +12% |
| NEAR | 39 | 22 (56%) | 45¢ | 53% | $38.28 | +21% |
| ETH | 39 | 18 (46%) | 44¢ | 52% | $2.59 | +1% |
| DOGE | 39 | 21 (54%) | 45¢ | 52% | $28.90 | +16% |
| BTC | 39 | 25 (64%) | 47¢ | 55% | $58.99 | +31% |
| BNB | 38 | 22 (58%) | 43¢ | 52% | $51.63 | +31% |
| HYPE | 38 | 18 (47%) | 43¢ | 52% | $11.25 | +7% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 8:17:07 AM | BNB | UP | 12.9 min | 22¢ | 29% | 6¢ | Open | — |
| 9/28 8:16:19 AM | DOGE | DOWN | 13.7 min | 75¢ | 81% | 4¢ | Open | — |
| 9/28 8:16:13 AM | HYPE | DOWN | 13.8 min | 57¢ | 69% | 10¢ | Open | — |
| 9/28 8:16:11 AM | SOL | DOWN | 13.8 min | 70¢ | 80% | 8¢ | Open | — |
| 9/28 8:16:09 AM | BTC | DOWN | 13.8 min | 65¢ | 72% | 5¢ | Open | — |
| 9/28 8:16:09 AM | ETH | DOWN | 13.8 min | 60¢ | 67% | 5¢ | Open | — |
| 9/28 8:16:05 AM | XRP | DOWN | 13.9 min | 66¢ | 80% | 12¢ | Open | — |
| 9/28 8:16:05 AM | ZEC | UP | 13.9 min | 28¢ | 34% | 4¢ | Open | — |
| 9/28 8:16:05 AM | NEAR | DOWN | 13.9 min | 74¢ | 81% | 6¢ | Open | — |
| 9/28 8:08:06 AM | NEAR | UP | 6.9 min | 9¢ | 17% | 7¢ | ❌ Lost | -$0.96 |
| 9/28 8:02:00 AM | SOL | DOWN | 13.0 min | 76¢ | 82% | 4¢ | ✅ Won | $2.27 |
| 9/28 8:01:44 AM | DOGE | DOWN | 13.3 min | 76¢ | 82% | 5¢ | ✅ Won | $2.27 |
| 9/28 8:01:22 AM | ZEC | DOWN | 13.6 min | 72¢ | 78% | 4¢ | ✅ Won | $2.65 |
| 9/28 8:01:16 AM | ETH | DOWN | 13.7 min | 73¢ | 80% | 5¢ | ✅ Won | $2.56 |
| 9/28 8:01:16 AM | BTC | DOWN | 13.7 min | 69¢ | 76% | 6¢ | ✅ Won | $2.95 |
| 9/28 8:01:16 AM | BNB | DOWN | 13.7 min | 79¢ | 85% | 4¢ | ✅ Won | $1.98 |
| 9/28 8:01:11 AM | HYPE | DOWN | 13.8 min | 76¢ | 84% | 6¢ | ✅ Won | $2.27 |
| 9/28 8:01:05 AM | XRP | DOWN | 13.9 min | 74¢ | 80% | 4¢ | ✅ Won | $2.46 |
| 9/28 7:47:26 AM | HYPE | DOWN | 12.6 min | 61¢ | 67% | 4¢ | ✅ Won | $3.73 |
| 9/28 7:46:44 AM | SOL | UP | 13.3 min | 47¢ | 55% | 6¢ | ❌ Lost | -$4.88 |
| 9/28 7:46:10 AM | ZEC | DOWN | 13.8 min | 53¢ | 62% | 8¢ | ✅ Won | $4.52 |
| 9/28 7:46:10 AM | ETH | DOWN | 13.8 min | 50¢ | 56% | 4¢ | ✅ Won | $4.82 |
| 9/28 7:46:08 AM | DOGE | DOWN | 13.9 min | 53¢ | 62% | 7¢ | ✅ Won | $4.52 |
| 9/28 7:46:06 AM | XRP | DOWN | 13.9 min | 55¢ | 64% | 7¢ | ✅ Won | $4.32 |
| 9/28 7:46:06 AM | BTC | DOWN | 13.9 min | 46¢ | 57% | 9¢ | ✅ Won | $5.22 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
