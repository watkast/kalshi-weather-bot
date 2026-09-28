# Fair-Value Bot

*Updated Mon Sep 28, 7:53 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **4¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 331 | $113.85 | +7% | $175.87 / -$62.02 |
| 4¢+ ← live bot | 319 | $194.91 | +14% | $263.18 / -$68.27 |
| 6¢+ | 302 | $116.26 | +10% | $209.80 / -$93.54 |
| 8¢+ | 275 | $53.58 | +5% | $176.32 / -$122.74 |
| 10¢+ | 248 | $63.32 | +7% | $172.67 / -$109.35 |
| 15¢+ | 158 | $85.56 | +16% | $168.22 / -$82.66 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 340 | 331 | 175 (53%) | 44¢ | 52% | $253.31 | +17% | +14.2¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+1.2%** over 9,054 readings from 342 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1556 | 2% | 4% | 10% |
| 10–20% | 669 | 15% | 16% | 22% |
| 20–30% | 712 | 25% | 26% | 36% |
| 30–40% | 813 | 35% | 36% | 47% |
| 40–50% | 835 | 45% | 48% | 55% |
| 50–60% | 829 | 55% | 58% | 60% |
| 60–70% | 837 | 65% | 70% | 69% |
| 70–80% | 788 | 75% | 79% | 82% |
| 80–90% | 628 | 85% | 87% | 89% |
| 90–100% | 1387 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 210 | 110 (52%) | 45¢ | 51% | $130.98 | +14% |
| 6–10¢ | 97 | 54 (56%) | 42¢ | 51% | $119.80 | +29% |
| 10–20¢ | 21 | 9 (43%) | 43¢ | 57% | -$3.47 | -4% |
| 20¢+ | 3 | 2 (67%) | 45¢ | 69% | $6.00 | +43% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 328 | 175 (53%) | 44¢ | 52% | $256.73 | +17% |
| 5–10 min | 3 | 0 (0%) | 11¢ | 17% | -$3.42 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 36 | 8 (22%) | 18¢ | 25% | $11.57 | +17% |
| Toss-up (25–75¢) | 288 | 161 (56%) | 46¢ | 54% | $236.65 | +17% |
| Favorite (75–95¢) | 7 | 6 (86%) | 77¢ | 84% | $5.09 | +9% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 37 | 22 (59%) | 42¢ | 50% | $58.95 | +37% |
| ZEC | 37 | 19 (51%) | 43¢ | 50% | $26.40 | +16% |
| XRP | 37 | 19 (51%) | 45¢ | 53% | $16.22 | +9% |
| NEAR | 37 | 21 (57%) | 46¢ | 54% | $33.72 | +19% |
| ETH | 37 | 16 (43%) | 43¢ | 51% | -$4.79 | -3% |
| DOGE | 37 | 19 (51%) | 44¢ | 51% | $22.11 | +13% |
| BTC | 37 | 23 (62%) | 47¢ | 54% | $50.82 | +28% |
| BNB | 36 | 20 (56%) | 42¢ | 51% | $44.63 | +29% |
| HYPE | 36 | 16 (44%) | 41¢ | 50% | $5.25 | +3% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 7:47:26 AM | HYPE | DOWN | 12.6 min | 61¢ | 67% | 4¢ | Open | — |
| 9/28 7:46:44 AM | SOL | UP | 13.3 min | 47¢ | 55% | 6¢ | Open | — |
| 9/28 7:46:10 AM | ZEC | DOWN | 13.8 min | 53¢ | 62% | 8¢ | Open | — |
| 9/28 7:46:10 AM | ETH | DOWN | 13.8 min | 50¢ | 56% | 4¢ | Open | — |
| 9/28 7:46:08 AM | DOGE | DOWN | 13.9 min | 53¢ | 62% | 7¢ | Open | — |
| 9/28 7:46:06 AM | XRP | DOWN | 13.9 min | 55¢ | 64% | 7¢ | Open | — |
| 9/28 7:46:06 AM | BTC | DOWN | 13.9 min | 46¢ | 57% | 9¢ | Open | — |
| 9/28 7:46:06 AM | BNB | DOWN | 13.9 min | 48¢ | 64% | 15¢ | Open | — |
| 9/28 7:46:06 AM | NEAR | DOWN | 13.9 min | 43¢ | 51% | 6¢ | Open | — |
| 9/28 7:31:11 AM | NEAR | DOWN | 13.8 min | 59¢ | 65% | 4¢ | ❌ Lost | -$6.07 |
| 9/28 7:31:07 AM | DOGE | DOWN | 13.9 min | 59¢ | 65% | 5¢ | ❌ Lost | -$6.07 |
| 9/28 7:31:07 AM | ZEC | DOWN | 13.9 min | 67¢ | 76% | 7¢ | ✅ Won | $3.14 |
| 9/28 7:31:07 AM | ETH | DOWN | 13.9 min | 67¢ | 76% | 7¢ | ❌ Lost | -$6.86 |
| 9/28 7:31:07 AM | BTC | DOWN | 13.9 min | 55¢ | 63% | 6¢ | ❌ Lost | -$5.68 |
| 9/28 7:31:05 AM | SOL | DOWN | 13.9 min | 65¢ | 74% | 7¢ | ❌ Lost | -$6.66 |
| 9/28 7:31:05 AM | HYPE | DOWN | 13.9 min | 37¢ | 63% | 24¢ | ❌ Lost | -$3.87 |
| 9/28 7:31:05 AM | XRP | DOWN | 13.9 min | 60¢ | 78% | 16¢ | ❌ Lost | -$6.17 |
| 9/28 7:31:05 AM | BNB | DOWN | 13.9 min | 44¢ | 50% | 4¢ | ❌ Lost | -$4.58 |
| 9/28 7:17:06 AM | BNB | DOWN | 12.9 min | 50¢ | 58% | 6¢ | ✅ Won | $4.82 |
| 9/28 7:16:49 AM | BTC | DOWN | 13.2 min | 40¢ | 48% | 7¢ | ❌ Lost | -$4.17 |
| 9/28 7:16:25 AM | DOGE | DOWN | 13.6 min | 37¢ | 45% | 6¢ | ❌ Lost | -$3.87 |
| 9/28 7:16:25 AM | ETH | DOWN | 13.6 min | 35¢ | 42% | 5¢ | ❌ Lost | -$3.66 |
| 9/28 7:16:21 AM | XRP | DOWN | 13.7 min | 33¢ | 39% | 4¢ | ❌ Lost | -$3.46 |
| 9/28 7:16:19 AM | NEAR | UP | 13.7 min | 44¢ | 51% | 5¢ | ✅ Won | $5.42 |
| 9/28 7:16:15 AM | SOL | UP | 13.8 min | 57¢ | 63% | 4¢ | ✅ Won | $4.12 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
