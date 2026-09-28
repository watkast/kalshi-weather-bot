# Fair-Value Bot

*Updated Mon Sep 28, 4:10 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **2¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **2¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 33 | $62.17 | +39% | -$0.20 / $62.37 |
| 4¢+ ← live bot | 32 | $42.60 | +29% | -$14.28 / $56.88 |
| 6¢+ | 30 | $18.08 | +14% | -$15.72 / $33.80 |
| 8¢+ | 27 | $27.68 | +30% | $4.64 / $23.04 |
| 10¢+ | 23 | $22.25 | +29% | $2.98 / $19.27 |
| 15¢+ | 16 | $7.05 | +16% | -$4.50 / $11.55 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 45 | 36 | 24 (67%) | 42¢ | 50% | $83.88 | +54% | +19.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.9%** over 810 readings from 45 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 139 | 3% | 3% | 0% |
| 10–20% | 123 | 15% | 15% | 20% |
| 20–30% | 149 | 25% | 26% | 36% |
| 30–40% | 149 | 35% | 33% | 51% |
| 40–50% | 87 | 44% | 44% | 57% |
| 50–60% | 33 | 55% | 57% | 45% |
| 60–70% | 23 | 65% | 71% | 39% |
| 70–80% | 21 | 75% | 80% | 62% |
| 80–90% | 11 | 86% | 94% | 100% |
| 90–100% | 75 | 98% | 98% | 100% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 23 | 12 (52%) | 47¢ | 53% | $8.22 | +7% |
| 6–10¢ | 9 | 8 (89%) | 33¢ | 42% | $48.67 | +155% |
| 10–20¢ | 3 | 3 (100%) | 30¢ | 43% | $20.65 | +221% |
| 20¢+ | 1 | 1 (100%) | 35¢ | 58% | $6.34 | +173% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 35 | 24 (69%) | 43¢ | 51% | $84.95 | +55% |
| 5–10 min | 1 | 0 (0%) | 10¢ | 16% | -$1.07 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 3 | 1 (33%) | 17¢ | 27% | $4.48 | +81% |
| Toss-up (25–75¢) | 32 | 22 (69%) | 43¢ | 51% | $77.13 | +54% |
| Favorite (75–95¢) | 1 | 1 (100%) | 76¢ | 82% | $2.27 | +29% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 4 | 3 (75%) | 31¢ | 39% | $16.88 | +129% |
| ZEC | 4 | 2 (50%) | 44¢ | 52% | $1.89 | +10% |
| XRP | 4 | 3 (75%) | 28¢ | 34% | $18.26 | +156% |
| NEAR | 4 | 2 (50%) | 54¢ | 61% | -$2.07 | -9% |
| ETH | 4 | 2 (50%) | 46¢ | 54% | $0.70 | +4% |
| BNB | 4 | 4 (100%) | 42¢ | 52% | $22.46 | +128% |
| DOGE | 4 | 2 (50%) | 38¢ | 46% | $4.19 | +27% |
| HYPE | 4 | 3 (75%) | 49¢ | 59% | $9.73 | +48% |
| BTC | 4 | 3 (75%) | 44¢ | 51% | $11.84 | +65% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 4:07:14 AM | BTC | DOWN | 7.8 min | 6¢ | 12% | 5¢ | Open | — |
| 9/28 4:01:58 AM | NEAR | DOWN | 13.0 min | 19¢ | 26% | 5¢ | Open | — |
| 9/28 4:01:32 AM | XRP | DOWN | 13.4 min | 20¢ | 27% | 6¢ | Open | — |
| 9/28 4:01:31 AM | ETH | DOWN | 13.5 min | 15¢ | 20% | 4¢ | Open | — |
| 9/28 4:01:15 AM | DOGE | DOWN | 13.7 min | 21¢ | 27% | 4¢ | Open | — |
| 9/28 4:01:02 AM | ZEC | DOWN | 13.9 min | 24¢ | 33% | 8¢ | Open | — |
| 9/28 4:01:00 AM | SOL | DOWN | 14.0 min | 15¢ | 20% | 4¢ | Open | — |
| 9/28 4:01:00 AM | HYPE | DOWN | 14.0 min | 12¢ | 20% | 7¢ | Open | — |
| 9/28 4:01:00 AM | BNB | DOWN | 14.0 min | 21¢ | 28% | 6¢ | Open | — |
| 9/27 11:16:19 PM | ETH | DOWN | 13.7 min | 37¢ | 47% | 8¢ | ✅ Won | $6.13 |
| 9/27 11:16:17 PM | ZEC | DOWN | 13.7 min | 42¢ | 49% | 5¢ | ❌ Lost | -$4.38 |
| 9/27 11:16:13 PM | DOGE | DOWN | 13.8 min | 35¢ | 45% | 8¢ | ✅ Won | $6.34 |
| 9/27 11:16:11 PM | XRP | DOWN | 13.8 min | 35¢ | 42% | 5¢ | ✅ Won | $6.34 |
| 9/27 11:16:11 PM | BTC | DOWN | 13.8 min | 35¢ | 43% | 7¢ | ✅ Won | $6.34 |
| 9/27 11:16:11 PM | SOL | DOWN | 13.8 min | 28¢ | 35% | 6¢ | ✅ Won | $7.05 |
| 9/27 11:16:11 PM | NEAR | DOWN | 13.8 min | 32¢ | 44% | 10¢ | ✅ Won | $6.64 |
| 9/27 11:16:09 PM | HYPE | DOWN | 13.8 min | 37¢ | 43% | 4¢ | ✅ Won | $6.13 |
| 9/27 11:16:04 PM | BNB | DOWN | 13.9 min | 34¢ | 42% | 7¢ | ✅ Won | $6.44 |
| 9/27 11:02:20 PM | DOGE | DOWN | 12.7 min | 35¢ | 47% | 10¢ | ✅ Won | $6.34 |
| 9/27 11:02:04 PM | BTC | DOWN | 12.9 min | 46¢ | 53% | 5¢ | ✅ Won | $5.22 |
| 9/27 11:02:02 PM | XRP | DOWN | 12.9 min | 27¢ | 33% | 5¢ | ✅ Won | $7.16 |
| 9/27 11:01:30 PM | SOL | DOWN | 13.5 min | 27¢ | 34% | 6¢ | ✅ Won | $7.16 |
| 9/27 11:01:16 PM | ETH | DOWN | 13.7 min | 37¢ | 45% | 6¢ | ✅ Won | $6.13 |
| 9/27 11:01:05 PM | HYPE | DOWN | 13.9 min | 35¢ | 58% | 21¢ | ✅ Won | $6.34 |
| 9/27 11:01:05 PM | ZEC | DOWN | 13.9 min | 29¢ | 39% | 8¢ | ✅ Won | $6.95 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
