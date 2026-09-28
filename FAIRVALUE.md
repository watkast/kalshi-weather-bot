# Fair-Value Bot

*Updated Mon Sep 28, 4:31 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **2¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **2¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 51 | $36.95 | +18% | $38.43 / -$1.48 |
| 4¢+ ← live bot | 50 | $17.39 | +10% | $17.95 / -$0.56 |
| 6¢+ | 47 | -$0.32 | -0% | $2.52 / -$2.84 |
| 8¢+ | 42 | $12.15 | +10% | $17.13 / -$4.98 |
| 10¢+ | 38 | $4.06 | +4% | $26.60 / -$22.54 |
| 15¢+ | 27 | -$4.38 | -7% | $5.98 / -$10.36 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 57 | 54 | 27 (50%) | 36¢ | 44% | $65.25 | +32% | +9.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+1.2%** over 1,296 readings from 63 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 143 | 3% | 4% | 0% |
| 10–20% | 123 | 15% | 15% | 20% |
| 20–30% | 149 | 25% | 26% | 36% |
| 30–40% | 150 | 35% | 33% | 51% |
| 40–50% | 97 | 45% | 45% | 62% |
| 50–60% | 68 | 55% | 63% | 71% |
| 60–70% | 95 | 66% | 74% | 79% |
| 70–80% | 104 | 75% | 80% | 87% |
| 80–90% | 104 | 85% | 91% | 91% |
| 90–100% | 263 | 97% | 97% | 100% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 35 | 15 (43%) | 40¢ | 47% | $3.84 | +3% |
| 6–10¢ | 14 | 8 (57%) | 29¢ | 38% | $37.26 | +87% |
| 10–20¢ | 4 | 3 (75%) | 29¢ | 43% | $17.81 | +146% |
| 20¢+ | 1 | 1 (100%) | 35¢ | 58% | $6.34 | +173% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 52 | 27 (52%) | 38¢ | 45% | $66.97 | +33% |
| 5–10 min | 2 | 0 (0%) | 8¢ | 14% | -$1.72 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 15 | 2 (13%) | 18¢ | 25% | -$8.60 | -30% |
| Toss-up (25–75¢) | 37 | 23 (62%) | 42¢ | 50% | $69.41 | +43% |
| Favorite (75–95¢) | 2 | 2 (100%) | 76¢ | 82% | $4.44 | +29% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 6 | 3 (50%) | 26¢ | 33% | $13.28 | +79% |
| ZEC | 6 | 3 (50%) | 44¢ | 52% | $2.70 | +10% |
| XRP | 6 | 3 (50%) | 26¢ | 32% | $13.71 | +84% |
| NEAR | 6 | 3 (50%) | 43¢ | 51% | $3.08 | +11% |
| ETH | 6 | 2 (33%) | 38¢ | 45% | -$3.53 | -15% |
| BNB | 6 | 4 (67%) | 36¢ | 47% | $17.40 | +77% |
| DOGE | 6 | 2 (33%) | 33¢ | 40% | -$0.46 | -2% |
| HYPE | 6 | 3 (50%) | 39¢ | 48% | $5.71 | +24% |
| BTC | 6 | 4 (67%) | 43¢ | 50% | $13.36 | +50% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
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
| 9/28 4:01:00 AM | HYPE | DOWN | 14.0 min | 12¢ | 20% | 7¢ | ❌ Lost | -$1.28 |
| 9/28 4:01:00 AM | BNB | DOWN | 14.0 min | 21¢ | 28% | 6¢ | ❌ Lost | -$2.22 |
| 9/27 11:16:19 PM | ETH | DOWN | 13.7 min | 37¢ | 47% | 8¢ | ✅ Won | $6.13 |
| 9/27 11:16:17 PM | ZEC | DOWN | 13.7 min | 42¢ | 49% | 5¢ | ❌ Lost | -$4.38 |
| 9/27 11:16:13 PM | DOGE | DOWN | 13.8 min | 35¢ | 45% | 8¢ | ✅ Won | $6.34 |
| 9/27 11:16:11 PM | XRP | DOWN | 13.8 min | 35¢ | 42% | 5¢ | ✅ Won | $6.34 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
