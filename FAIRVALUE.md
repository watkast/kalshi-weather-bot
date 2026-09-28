# Fair-Value Bot

*Updated Mon Sep 28, 7:43 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **4¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 322 | $145.93 | +10% | $164.08 / -$18.15 |
| 4¢+ ← live bot | 310 | $228.66 | +17% | $249.86 / -$21.20 |
| 6¢+ | 293 | $151.12 | +13% | $189.63 / -$38.51 |
| 8¢+ | 266 | $88.63 | +9% | $182.47 / -$93.84 |
| 10¢+ | 239 | $99.43 | +11% | $175.64 / -$76.21 |
| 15¢+ | 152 | $105.52 | +21% | $163.50 / -$57.98 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 331 | 322 | 174 (54%) | 43¢ | 51% | $296.13 | +21% | +14.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+1.9%** over 8,811 readings from 333 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1541 | 2% | 4% | 9% |
| 10–20% | 643 | 15% | 16% | 19% |
| 20–30% | 676 | 25% | 26% | 33% |
| 30–40% | 787 | 35% | 36% | 46% |
| 40–50% | 810 | 45% | 48% | 54% |
| 50–60% | 808 | 55% | 59% | 59% |
| 60–70% | 827 | 65% | 70% | 69% |
| 70–80% | 776 | 75% | 79% | 82% |
| 80–90% | 618 | 85% | 87% | 89% |
| 90–100% | 1325 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 207 | 110 (53%) | 44¢ | 51% | $147.70 | +16% |
| 6–10¢ | 93 | 53 (57%) | 41¢ | 50% | $135.86 | +34% |
| 10–20¢ | 20 | 9 (45%) | 42¢ | 56% | $2.70 | +3% |
| 20¢+ | 2 | 2 (100%) | 49¢ | 71% | $9.87 | +97% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 319 | 174 (55%) | 44¢ | 51% | $299.55 | +21% |
| 5–10 min | 3 | 0 (0%) | 11¢ | 17% | -$3.42 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 36 | 8 (22%) | 18¢ | 25% | $11.57 | +17% |
| Toss-up (25–75¢) | 279 | 160 (57%) | 46¢ | 54% | $279.47 | +21% |
| Favorite (75–95¢) | 7 | 6 (86%) | 77¢ | 84% | $5.09 | +9% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 36 | 22 (61%) | 41¢ | 49% | $65.61 | +42% |
| ZEC | 36 | 18 (50%) | 42¢ | 50% | $23.26 | +15% |
| XRP | 36 | 19 (53%) | 45¢ | 52% | $22.39 | +13% |
| NEAR | 36 | 21 (58%) | 46¢ | 53% | $39.79 | +23% |
| ETH | 36 | 16 (44%) | 42¢ | 50% | $2.07 | +1% |
| DOGE | 36 | 19 (53%) | 43¢ | 51% | $28.18 | +17% |
| BTC | 36 | 23 (64%) | 47¢ | 54% | $56.50 | +33% |
| BNB | 35 | 20 (57%) | 41¢ | 51% | $49.21 | +33% |
| HYPE | 35 | 16 (46%) | 42¢ | 50% | $9.12 | +6% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 7:31:11 AM | NEAR | DOWN | 13.8 min | 59¢ | 65% | 4¢ | Open | — |
| 9/28 7:31:07 AM | DOGE | DOWN | 13.9 min | 59¢ | 65% | 5¢ | Open | — |
| 9/28 7:31:07 AM | ZEC | DOWN | 13.9 min | 67¢ | 76% | 7¢ | Open | — |
| 9/28 7:31:07 AM | ETH | DOWN | 13.9 min | 67¢ | 76% | 7¢ | Open | — |
| 9/28 7:31:07 AM | BTC | DOWN | 13.9 min | 55¢ | 63% | 6¢ | Open | — |
| 9/28 7:31:05 AM | SOL | DOWN | 13.9 min | 65¢ | 74% | 7¢ | Open | — |
| 9/28 7:31:05 AM | HYPE | DOWN | 13.9 min | 37¢ | 63% | 24¢ | Open | — |
| 9/28 7:31:05 AM | XRP | DOWN | 13.9 min | 60¢ | 78% | 16¢ | Open | — |
| 9/28 7:31:05 AM | BNB | DOWN | 13.9 min | 44¢ | 50% | 4¢ | Open | — |
| 9/28 7:17:06 AM | BNB | DOWN | 12.9 min | 50¢ | 58% | 6¢ | ✅ Won | $4.82 |
| 9/28 7:16:49 AM | BTC | DOWN | 13.2 min | 40¢ | 48% | 7¢ | ❌ Lost | -$4.17 |
| 9/28 7:16:25 AM | DOGE | DOWN | 13.6 min | 37¢ | 45% | 6¢ | ❌ Lost | -$3.87 |
| 9/28 7:16:25 AM | ETH | DOWN | 13.6 min | 35¢ | 42% | 5¢ | ❌ Lost | -$3.66 |
| 9/28 7:16:21 AM | XRP | DOWN | 13.7 min | 33¢ | 39% | 4¢ | ❌ Lost | -$3.46 |
| 9/28 7:16:19 AM | NEAR | UP | 13.7 min | 44¢ | 51% | 5¢ | ✅ Won | $5.42 |
| 9/28 7:16:15 AM | SOL | UP | 13.8 min | 57¢ | 63% | 4¢ | ✅ Won | $4.12 |
| 9/28 7:16:05 AM | ZEC | DOWN | 13.9 min | 50¢ | 59% | 8¢ | ✅ Won | $4.82 |
| 9/28 7:16:05 AM | HYPE | DOWN | 13.9 min | 51¢ | 59% | 6¢ | ✅ Won | $4.72 |
| 9/28 7:03:08 AM | ETH | UP | 11.9 min | 13¢ | 19% | 5¢ | ❌ Lost | -$1.38 |
| 9/28 7:02:38 AM | DOGE | UP | 12.3 min | 17¢ | 22% | 4¢ | ❌ Lost | -$1.80 |
| 9/28 7:01:57 AM | BTC | DOWN | 13.0 min | 73¢ | 79% | 4¢ | ✅ Won | $2.56 |
| 9/28 7:01:51 AM | SOL | UP | 13.1 min | 23¢ | 28% | 4¢ | ❌ Lost | -$2.43 |
| 9/28 7:01:45 AM | XRP | DOWN | 13.2 min | 67¢ | 73% | 4¢ | ✅ Won | $3.14 |
| 9/28 7:01:27 AM | ZEC | UP | 13.5 min | 27¢ | 34% | 5¢ | ✅ Won | $7.16 |
| 9/28 7:01:04 AM | NEAR | UP | 13.9 min | 21¢ | 28% | 5¢ | ✅ Won | $7.78 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
