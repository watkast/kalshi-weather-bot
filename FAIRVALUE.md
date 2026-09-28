# Fair-Value Bot

*Updated Mon Sep 28, 7:22 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **4¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 313 | $158.92 | +11% | $172.15 / -$13.23 |
| 4¢+ ← live bot | 301 | $239.83 | +18% | $237.23 / $2.60 |
| 6¢+ | 284 | $160.78 | +14% | $188.83 / -$28.05 |
| 8¢+ | 257 | $103.90 | +11% | $165.11 / -$61.21 |
| 10¢+ | 231 | $109.28 | +13% | $191.11 / -$81.83 |
| 15¢+ | 146 | $116.93 | +24% | $141.80 / -$24.87 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 322 | 313 | 169 (54%) | 43¢ | 51% | $287.39 | +20% | +14.5¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+2.1%** over 8,568 readings from 324 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1529 | 2% | 4% | 9% |
| 10–20% | 623 | 15% | 16% | 19% |
| 20–30% | 635 | 25% | 26% | 32% |
| 30–40% | 741 | 35% | 36% | 45% |
| 40–50% | 769 | 45% | 48% | 53% |
| 50–60% | 777 | 55% | 59% | 58% |
| 60–70% | 818 | 65% | 70% | 69% |
| 70–80% | 768 | 75% | 79% | 82% |
| 80–90% | 614 | 85% | 87% | 88% |
| 90–100% | 1294 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 201 | 107 (53%) | 44¢ | 51% | $144.43 | +16% |
| 6–10¢ | 90 | 51 (57%) | 41¢ | 50% | $130.39 | +34% |
| 10–20¢ | 20 | 9 (45%) | 42¢ | 56% | $2.70 | +3% |
| 20¢+ | 2 | 2 (100%) | 49¢ | 71% | $9.87 | +97% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 310 | 169 (55%) | 44¢ | 51% | $290.81 | +21% |
| 5–10 min | 3 | 0 (0%) | 11¢ | 17% | -$3.42 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 36 | 8 (22%) | 18¢ | 25% | $11.57 | +17% |
| Toss-up (25–75¢) | 270 | 155 (57%) | 46¢ | 54% | $270.73 | +21% |
| Favorite (75–95¢) | 7 | 6 (86%) | 77¢ | 84% | $5.09 | +9% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 35 | 21 (60%) | 41¢ | 49% | $61.49 | +41% |
| ZEC | 35 | 17 (49%) | 42¢ | 49% | $18.44 | +12% |
| XRP | 35 | 19 (54%) | 45¢ | 52% | $25.85 | +16% |
| NEAR | 35 | 20 (57%) | 46¢ | 54% | $34.37 | +21% |
| ETH | 35 | 16 (46%) | 42¢ | 50% | $5.73 | +4% |
| DOGE | 35 | 19 (54%) | 44¢ | 51% | $32.05 | +20% |
| BTC | 35 | 23 (66%) | 47¢ | 54% | $60.67 | +36% |
| BNB | 34 | 19 (56%) | 41¢ | 50% | $44.39 | +30% |
| HYPE | 34 | 15 (44%) | 41¢ | 50% | $4.40 | +3% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 7:17:06 AM | BNB | DOWN | 12.9 min | 50¢ | 58% | 6¢ | Open | — |
| 9/28 7:16:49 AM | BTC | DOWN | 13.2 min | 40¢ | 48% | 7¢ | Open | — |
| 9/28 7:16:25 AM | DOGE | DOWN | 13.6 min | 37¢ | 45% | 6¢ | Open | — |
| 9/28 7:16:25 AM | ETH | DOWN | 13.6 min | 35¢ | 42% | 5¢ | Open | — |
| 9/28 7:16:21 AM | XRP | DOWN | 13.7 min | 33¢ | 39% | 4¢ | Open | — |
| 9/28 7:16:19 AM | NEAR | UP | 13.7 min | 44¢ | 51% | 5¢ | Open | — |
| 9/28 7:16:15 AM | SOL | UP | 13.8 min | 57¢ | 63% | 4¢ | Open | — |
| 9/28 7:16:05 AM | ZEC | DOWN | 13.9 min | 50¢ | 59% | 8¢ | Open | — |
| 9/28 7:16:05 AM | HYPE | DOWN | 13.9 min | 51¢ | 59% | 6¢ | Open | — |
| 9/28 7:03:08 AM | ETH | UP | 11.9 min | 13¢ | 19% | 5¢ | ❌ Lost | -$1.38 |
| 9/28 7:02:38 AM | DOGE | UP | 12.3 min | 17¢ | 22% | 4¢ | ❌ Lost | -$1.80 |
| 9/28 7:01:57 AM | BTC | DOWN | 13.0 min | 73¢ | 79% | 4¢ | ✅ Won | $2.56 |
| 9/28 7:01:51 AM | SOL | UP | 13.1 min | 23¢ | 28% | 4¢ | ❌ Lost | -$2.43 |
| 9/28 7:01:45 AM | XRP | DOWN | 13.2 min | 67¢ | 73% | 4¢ | ✅ Won | $3.14 |
| 9/28 7:01:27 AM | ZEC | UP | 13.5 min | 27¢ | 34% | 5¢ | ✅ Won | $7.16 |
| 9/28 7:01:04 AM | NEAR | UP | 13.9 min | 21¢ | 28% | 5¢ | ✅ Won | $7.78 |
| 9/28 6:47:18 AM | ETH | DOWN | 12.7 min | 11¢ | 16% | 4¢ | ❌ Lost | -$1.17 |
| 9/28 6:47:00 AM | NEAR | DOWN | 13.0 min | 45¢ | 55% | 8¢ | ❌ Lost | -$4.68 |
| 9/28 6:46:58 AM | ZEC | DOWN | 13.0 min | 17¢ | 24% | 6¢ | ❌ Lost | -$1.80 |
| 9/28 6:46:48 AM | DOGE | DOWN | 13.2 min | 12¢ | 19% | 6¢ | ❌ Lost | -$1.28 |
| 9/28 6:46:36 AM | HYPE | DOWN | 13.4 min | 12¢ | 20% | 8¢ | ❌ Lost | -$1.28 |
| 9/28 6:46:32 AM | XRP | DOWN | 13.5 min | 16¢ | 21% | 4¢ | ❌ Lost | -$1.70 |
| 9/28 6:46:16 AM | BTC | UP | 13.7 min | 78¢ | 84% | 4¢ | ✅ Won | $2.07 |
| 9/28 6:46:04 AM | SOL | UP | 13.9 min | 77¢ | 83% | 5¢ | ✅ Won | $2.17 |
| 9/28 6:46:04 AM | BNB | DOWN | 13.9 min | 16¢ | 25% | 8¢ | ❌ Lost | -$1.70 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
