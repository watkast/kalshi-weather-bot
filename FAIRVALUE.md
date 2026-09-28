# Fair-Value Bot

*Updated Mon Sep 28, 4:41 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **4¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 214 | $222.38 | +22% | $105.18 / $117.20 |
| 4¢+ ← live bot | 208 | $311.69 | +34% | $115.58 / $196.11 |
| 6¢+ | 194 | $237.36 | +32% | $110.91 / $126.45 |
| 8¢+ | 175 | $169.68 | +28% | $62.84 / $106.84 |
| 10¢+ | 159 | $156.17 | +28% | $124.61 / $31.56 |
| 15¢+ | 97 | $140.65 | +47% | $119.52 / $21.13 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 225 | 216 | 125 (58%) | 42¢ | 50% | $297.54 | +31% | +18.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+3.7%** over 5,895 readings from 225 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1205 | 2% | 4% | 7% |
| 10–20% | 446 | 15% | 16% | 11% |
| 20–30% | 460 | 25% | 25% | 26% |
| 30–40% | 522 | 35% | 35% | 41% |
| 40–50% | 532 | 45% | 48% | 48% |
| 50–60% | 574 | 55% | 58% | 50% |
| 60–70% | 589 | 65% | 71% | 62% |
| 70–80% | 512 | 75% | 79% | 75% |
| 80–90% | 395 | 85% | 88% | 83% |
| 90–100% | 660 | 97% | 97% | 95% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 141 | 75 (53%) | 45¢ | 51% | $99.60 | +15% |
| 6–10¢ | 63 | 41 (65%) | 39¢ | 48% | $154.72 | +61% |
| 10–20¢ | 11 | 8 (73%) | 38¢ | 51% | $36.88 | +86% |
| 20¢+ | 1 | 1 (100%) | 35¢ | 58% | $6.34 | +173% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 213 | 125 (59%) | 43¢ | 51% | $300.96 | +32% |
| 5–10 min | 3 | 0 (0%) | 11¢ | 17% | -$3.42 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 24 | 7 (29%) | 19¢ | 26% | $22.56 | +48% |
| Toss-up (25–75¢) | 188 | 115 (61%) | 45¢ | 53% | $276.30 | +32% |
| Favorite (75–95¢) | 4 | 3 (75%) | 77¢ | 83% | -$1.32 | -4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 24 | 14 (58%) | 40¢ | 47% | $40.87 | +41% |
| ZEC | 24 | 12 (50%) | 43¢ | 50% | $12.84 | +12% |
| XRP | 24 | 12 (50%) | 44¢ | 50% | $11.37 | +10% |
| NEAR | 24 | 16 (67%) | 44¢ | 52% | $49.52 | +45% |
| ETH | 24 | 11 (46%) | 41¢ | 49% | $7.07 | +7% |
| BNB | 24 | 17 (71%) | 39¢ | 48% | $71.66 | +73% |
| DOGE | 24 | 16 (67%) | 44¢ | 52% | $49.40 | +45% |
| HYPE | 24 | 11 (46%) | 42¢ | 51% | $4.84 | +5% |
| BTC | 24 | 16 (67%) | 44¢ | 52% | $49.97 | +45% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 4:31:49 AM | BTC | UP | 13.2 min | 49¢ | 56% | 6¢ | Open | — |
| 9/28 4:31:45 AM | DOGE | UP | 13.2 min | 48¢ | 59% | 9¢ | Open | — |
| 9/28 4:31:41 AM | HYPE | UP | 13.3 min | 37¢ | 44% | 5¢ | Open | — |
| 9/28 4:31:35 AM | ZEC | UP | 13.4 min | 41¢ | 52% | 10¢ | Open | — |
| 9/28 4:31:33 AM | NEAR | UP | 13.4 min | 50¢ | 56% | 5¢ | Open | — |
| 9/28 4:31:31 AM | XRP | UP | 13.5 min | 48¢ | 55% | 6¢ | Open | — |
| 9/28 4:31:24 AM | SOL | UP | 13.6 min | 41¢ | 51% | 8¢ | Open | — |
| 9/28 4:31:12 AM | ETH | UP | 13.8 min | 41¢ | 48% | 5¢ | Open | — |
| 9/28 4:31:08 AM | BNB | DOWN | 13.8 min | 53¢ | 60% | 5¢ | Open | — |
| 9/28 4:17:36 AM | BTC | UP | 12.4 min | 77¢ | 83% | 4¢ | ✅ Won | $2.17 |
| 9/28 4:16:23 AM | SOL | DOWN | 13.6 min | 19¢ | 26% | 6¢ | ❌ Lost | -$2.01 |
| 9/28 4:16:19 AM | DOGE | DOWN | 13.7 min | 23¢ | 28% | 4¢ | ❌ Lost | -$2.43 |
| 9/28 4:16:09 AM | ZEC | UP | 13.8 min | 65¢ | 71% | 5¢ | ✅ Won | $3.34 |
| 9/28 4:16:04 AM | HYPE | DOWN | 13.9 min | 26¢ | 33% | 5¢ | ❌ Lost | -$2.74 |
| 9/28 4:16:04 AM | ETH | DOWN | 13.9 min | 25¢ | 32% | 6¢ | ❌ Lost | -$2.64 |
| 9/28 4:16:04 AM | XRP | DOWN | 13.9 min | 23¢ | 29% | 4¢ | ❌ Lost | -$2.43 |
| 9/28 4:16:04 AM | NEAR | DOWN | 13.9 min | 27¢ | 35% | 7¢ | ❌ Lost | -$2.84 |
| 9/28 4:16:04 AM | BNB | DOWN | 13.9 min | 27¢ | 43% | 15¢ | ❌ Lost | -$2.84 |
| 9/28 4:07:14 AM | BTC | DOWN | 7.8 min | 6¢ | 12% | 5¢ | ❌ Lost | -$0.65 |
| 9/28 4:01:58 AM | NEAR | DOWN | 13.0 min | 19¢ | 26% | 5¢ | ✅ Won | $7.99 |
| 9/28 4:01:32 AM | XRP | DOWN | 13.4 min | 20¢ | 27% | 6¢ | ❌ Lost | -$2.12 |
| 9/28 4:01:31 AM | ETH | DOWN | 13.5 min | 15¢ | 20% | 4¢ | ❌ Lost | -$1.59 |
| 9/28 4:01:15 AM | DOGE | DOWN | 13.7 min | 21¢ | 27% | 4¢ | ❌ Lost | -$2.22 |
| 9/28 4:01:02 AM | ZEC | DOWN | 13.9 min | 24¢ | 33% | 8¢ | ❌ Lost | -$2.53 |
| 9/28 4:01:00 AM | SOL | DOWN | 14.0 min | 15¢ | 20% | 4¢ | ❌ Lost | -$1.59 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
