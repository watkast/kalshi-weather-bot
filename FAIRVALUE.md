# Fair-Value Bot

*Updated Mon Sep 28, 8:03 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **4¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 340 | $136.54 | +9% | $185.11 / -$48.57 |
| 4¢+ ← live bot | 328 | $197.11 | +13% | $266.41 / -$69.30 |
| 6¢+ | 311 | $140.95 | +11% | $218.43 / -$77.48 |
| 8¢+ | 284 | $73.88 | +7% | $172.52 / -$98.64 |
| 10¢+ | 255 | $87.05 | +9% | $169.71 / -$82.66 |
| 15¢+ | 160 | $88.16 | +16% | $167.05 / -$78.89 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 348 | 340 | 183 (54%) | 44¢ | 52% | $286.10 | +19% | +13.9¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+1.6%** over 9,297 readings from 351 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1629 | 2% | 4% | 9% |
| 10–20% | 717 | 15% | 16% | 20% |
| 20–30% | 738 | 25% | 26% | 34% |
| 30–40% | 838 | 35% | 37% | 46% |
| 40–50% | 866 | 45% | 48% | 53% |
| 50–60% | 852 | 55% | 58% | 58% |
| 60–70% | 853 | 65% | 70% | 68% |
| 70–80% | 789 | 75% | 79% | 82% |
| 80–90% | 628 | 85% | 87% | 89% |
| 90–100% | 1387 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 212 | 112 (53%) | 45¢ | 51% | $139.53 | +14% |
| 6–10¢ | 103 | 59 (57%) | 42¢ | 51% | $139.02 | +31% |
| 10–20¢ | 22 | 10 (45%) | 43¢ | 58% | $1.55 | +2% |
| 20¢+ | 3 | 2 (67%) | 45¢ | 69% | $6.00 | +43% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 337 | 183 (54%) | 44¢ | 52% | $289.52 | +19% |
| 5–10 min | 3 | 0 (0%) | 11¢ | 17% | -$3.42 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 36 | 8 (22%) | 18¢ | 25% | $11.57 | +17% |
| Toss-up (25–75¢) | 297 | 169 (57%) | 46¢ | 54% | $269.44 | +19% |
| Favorite (75–95¢) | 7 | 6 (86%) | 77¢ | 84% | $5.09 | +9% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 38 | 22 (58%) | 42¢ | 50% | $54.07 | +33% |
| ZEC | 38 | 20 (53%) | 43¢ | 51% | $30.92 | +18% |
| XRP | 38 | 20 (53%) | 46¢ | 53% | $20.54 | +11% |
| NEAR | 38 | 22 (58%) | 46¢ | 54% | $39.24 | +22% |
| ETH | 38 | 17 (45%) | 43¢ | 51% | $0.03 | +0% |
| DOGE | 38 | 20 (53%) | 44¢ | 52% | $26.63 | +15% |
| BTC | 38 | 24 (63%) | 47¢ | 54% | $56.04 | +30% |
| BNB | 37 | 21 (57%) | 42¢ | 51% | $49.65 | +31% |
| HYPE | 37 | 17 (46%) | 42¢ | 51% | $8.98 | +6% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 8:02:00 AM | SOL | DOWN | 13.0 min | 76¢ | 82% | 4¢ | Open | — |
| 9/28 8:01:44 AM | DOGE | DOWN | 13.3 min | 76¢ | 82% | 5¢ | Open | — |
| 9/28 8:01:22 AM | ZEC | DOWN | 13.6 min | 72¢ | 78% | 4¢ | Open | — |
| 9/28 8:01:16 AM | ETH | DOWN | 13.7 min | 73¢ | 80% | 5¢ | Open | — |
| 9/28 8:01:16 AM | BTC | DOWN | 13.7 min | 69¢ | 76% | 6¢ | Open | — |
| 9/28 8:01:16 AM | BNB | DOWN | 13.7 min | 79¢ | 85% | 4¢ | Open | — |
| 9/28 8:01:11 AM | HYPE | DOWN | 13.8 min | 76¢ | 84% | 6¢ | Open | — |
| 9/28 8:01:05 AM | XRP | DOWN | 13.9 min | 74¢ | 80% | 4¢ | Open | — |
| 9/28 7:47:26 AM | HYPE | DOWN | 12.6 min | 61¢ | 67% | 4¢ | ✅ Won | $3.73 |
| 9/28 7:46:44 AM | SOL | UP | 13.3 min | 47¢ | 55% | 6¢ | ❌ Lost | -$4.88 |
| 9/28 7:46:10 AM | ZEC | DOWN | 13.8 min | 53¢ | 62% | 8¢ | ✅ Won | $4.52 |
| 9/28 7:46:10 AM | ETH | DOWN | 13.8 min | 50¢ | 56% | 4¢ | ✅ Won | $4.82 |
| 9/28 7:46:08 AM | DOGE | DOWN | 13.9 min | 53¢ | 62% | 7¢ | ✅ Won | $4.52 |
| 9/28 7:46:06 AM | XRP | DOWN | 13.9 min | 55¢ | 64% | 7¢ | ✅ Won | $4.32 |
| 9/28 7:46:06 AM | BTC | DOWN | 13.9 min | 46¢ | 57% | 9¢ | ✅ Won | $5.22 |
| 9/28 7:46:06 AM | BNB | DOWN | 13.9 min | 48¢ | 64% | 15¢ | ✅ Won | $5.02 |
| 9/28 7:46:06 AM | NEAR | DOWN | 13.9 min | 43¢ | 51% | 6¢ | ✅ Won | $5.52 |
| 9/28 7:31:11 AM | NEAR | DOWN | 13.8 min | 59¢ | 65% | 4¢ | ❌ Lost | -$6.07 |
| 9/28 7:31:07 AM | DOGE | DOWN | 13.9 min | 59¢ | 65% | 5¢ | ❌ Lost | -$6.07 |
| 9/28 7:31:07 AM | ZEC | DOWN | 13.9 min | 67¢ | 76% | 7¢ | ✅ Won | $3.14 |
| 9/28 7:31:07 AM | ETH | DOWN | 13.9 min | 67¢ | 76% | 7¢ | ❌ Lost | -$6.86 |
| 9/28 7:31:07 AM | BTC | DOWN | 13.9 min | 55¢ | 63% | 6¢ | ❌ Lost | -$5.68 |
| 9/28 7:31:05 AM | SOL | DOWN | 13.9 min | 65¢ | 74% | 7¢ | ❌ Lost | -$6.66 |
| 9/28 7:31:05 AM | HYPE | DOWN | 13.9 min | 37¢ | 63% | 24¢ | ❌ Lost | -$3.87 |
| 9/28 7:31:05 AM | XRP | DOWN | 13.9 min | 60¢ | 78% | 16¢ | ❌ Lost | -$6.17 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
