# Fair-Value Bot

*Updated Mon Sep 28, 7:02 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **4¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 304 | $151.72 | +11% | $189.40 / -$37.68 |
| 4¢+ ← live bot | 295 | $229.99 | +17% | $236.84 / -$6.85 |
| 6¢+ | 279 | $148.20 | +13% | $176.41 / -$28.21 |
| 8¢+ | 254 | $89.82 | +10% | $158.26 / -$68.44 |
| 10¢+ | 229 | $111.83 | +13% | $186.79 / -$74.96 |
| 15¢+ | 145 | $118.52 | +25% | $144.23 / -$25.71 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 312 | 306 | 165 (54%) | 43¢ | 51% | $272.36 | +20% | +14.8¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+1.6%** over 8,325 readings from 315 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1407 | 2% | 4% | 9% |
| 10–20% | 572 | 15% | 16% | 20% |
| 20–30% | 611 | 25% | 26% | 32% |
| 30–40% | 718 | 35% | 36% | 44% |
| 40–50% | 761 | 45% | 48% | 53% |
| 50–60% | 772 | 55% | 59% | 57% |
| 60–70% | 814 | 65% | 70% | 69% |
| 70–80% | 765 | 75% | 79% | 82% |
| 80–90% | 612 | 85% | 87% | 88% |
| 90–100% | 1293 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 194 | 103 (53%) | 45¢ | 51% | $129.40 | +14% |
| 6–10¢ | 90 | 51 (57%) | 41¢ | 50% | $130.39 | +34% |
| 10–20¢ | 20 | 9 (45%) | 42¢ | 56% | $2.70 | +3% |
| 20¢+ | 2 | 2 (100%) | 49¢ | 71% | $9.87 | +97% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 303 | 165 (54%) | 44¢ | 52% | $275.78 | +20% |
| 5–10 min | 3 | 0 (0%) | 11¢ | 17% | -$3.42 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 32 | 7 (22%) | 18¢ | 25% | $9.40 | +16% |
| Toss-up (25–75¢) | 267 | 152 (57%) | 46¢ | 54% | $257.87 | +20% |
| Favorite (75–95¢) | 7 | 6 (86%) | 77¢ | 84% | $5.09 | +9% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 34 | 21 (62%) | 41¢ | 49% | $63.92 | +44% |
| ZEC | 34 | 16 (47%) | 42¢ | 50% | $11.28 | +8% |
| XRP | 34 | 18 (53%) | 45¢ | 52% | $22.71 | +14% |
| NEAR | 34 | 19 (56%) | 46¢ | 54% | $26.59 | +16% |
| ETH | 34 | 16 (47%) | 43¢ | 51% | $7.11 | +5% |
| BNB | 34 | 19 (56%) | 41¢ | 50% | $44.39 | +30% |
| DOGE | 34 | 19 (56%) | 44¢ | 52% | $33.85 | +22% |
| HYPE | 34 | 15 (44%) | 41¢ | 50% | $4.40 | +3% |
| BTC | 34 | 22 (65%) | 46¢ | 53% | $58.11 | +36% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 7:02:38 AM | DOGE | UP | 12.3 min | 17¢ | 22% | 4¢ | Open | — |
| 9/28 7:01:57 AM | BTC | DOWN | 13.0 min | 73¢ | 79% | 4¢ | Open | — |
| 9/28 7:01:51 AM | SOL | UP | 13.1 min | 23¢ | 28% | 4¢ | Open | — |
| 9/28 7:01:45 AM | XRP | DOWN | 13.2 min | 67¢ | 73% | 4¢ | Open | — |
| 9/28 7:01:27 AM | ZEC | UP | 13.5 min | 27¢ | 34% | 5¢ | Open | — |
| 9/28 7:01:04 AM | NEAR | UP | 13.9 min | 21¢ | 28% | 5¢ | Open | — |
| 9/28 6:47:18 AM | ETH | DOWN | 12.7 min | 11¢ | 16% | 4¢ | ❌ Lost | -$1.17 |
| 9/28 6:47:00 AM | NEAR | DOWN | 13.0 min | 45¢ | 55% | 8¢ | ❌ Lost | -$4.68 |
| 9/28 6:46:58 AM | ZEC | DOWN | 13.0 min | 17¢ | 24% | 6¢ | ❌ Lost | -$1.80 |
| 9/28 6:46:48 AM | DOGE | DOWN | 13.2 min | 12¢ | 19% | 6¢ | ❌ Lost | -$1.28 |
| 9/28 6:46:36 AM | HYPE | DOWN | 13.4 min | 12¢ | 20% | 8¢ | ❌ Lost | -$1.28 |
| 9/28 6:46:32 AM | XRP | DOWN | 13.5 min | 16¢ | 21% | 4¢ | ❌ Lost | -$1.70 |
| 9/28 6:46:16 AM | BTC | UP | 13.7 min | 78¢ | 84% | 4¢ | ✅ Won | $2.07 |
| 9/28 6:46:04 AM | SOL | UP | 13.9 min | 77¢ | 83% | 5¢ | ✅ Won | $2.17 |
| 9/28 6:46:04 AM | BNB | DOWN | 13.9 min | 16¢ | 25% | 8¢ | ❌ Lost | -$1.70 |
| 9/28 6:33:50 AM | DOGE | UP | 11.2 min | 40¢ | 46% | 4¢ | ❌ Lost | -$4.17 |
| 9/28 6:33:05 AM | HYPE | UP | 11.9 min | 40¢ | 47% | 5¢ | ✅ Won | $5.83 |
| 9/28 6:33:00 AM | BTC | UP | 12.0 min | 32¢ | 38% | 5¢ | ❌ Lost | -$3.36 |
| 9/28 6:32:57 AM | NEAR | UP | 12.0 min | 31¢ | 37% | 5¢ | ❌ Lost | -$3.25 |
| 9/28 6:31:25 AM | SOL | UP | 13.6 min | 42¢ | 49% | 5¢ | ✅ Won | $5.62 |
| 9/28 6:31:19 AM | ZEC | UP | 13.7 min | 40¢ | 46% | 4¢ | ✅ Won | $5.83 |
| 9/28 6:31:11 AM | XRP | UP | 13.8 min | 38¢ | 49% | 9¢ | ❌ Lost | -$3.97 |
| 9/28 6:31:11 AM | BNB | DOWN | 13.8 min | 56¢ | 64% | 6¢ | ✅ Won | $4.22 |
| 9/28 6:31:09 AM | ETH | DOWN | 13.8 min | 55¢ | 61% | 4¢ | ✅ Won | $4.32 |
| 9/28 6:17:07 AM | DOGE | DOWN | 12.9 min | 34¢ | 40% | 5¢ | ❌ Lost | -$3.56 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
