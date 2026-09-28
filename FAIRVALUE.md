# Fair-Value Bot

*Updated Sun Sep 27, 11:24 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

⏳ **Too early to call.** 27 settled trades so far — a verdict needs at least 30, spread over many 15-minute windows (coins tend to move together, so trades in the same window aren't independent).

**Edge thresholds so far** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return |
|---|---|---|---|
| 2¢+ | 27 | $39.20 | +30% |
| 4¢+ ← live bot | 27 | $19.85 | +17% |
| 6¢+ | 27 | $4.47 | +4% |
| 8¢+ | 26 | $23.16 | +27% |
| 10¢+ | 23 | $22.25 | +29% |
| 15¢+ | 16 | $7.05 | +16% |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 36 | 27 | 16 (59%) | 44¢ | 52% | $36.85 | +30% | +19.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.9%** over 783 readings from 36 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 139 | 3% | 3% | 0% |
| 10–20% | 123 | 15% | 15% | 20% |
| 20–30% | 147 | 25% | 26% | 36% |
| 30–40% | 143 | 35% | 33% | 53% |
| 40–50% | 78 | 44% | 43% | 62% |
| 50–60% | 29 | 55% | 57% | 48% |
| 60–70% | 18 | 65% | 73% | 50% |
| 70–80% | 20 | 75% | 80% | 65% |
| 80–90% | 11 | 86% | 94% | 100% |
| 90–100% | 75 | 98% | 98% | 100% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 19 | 9 (47%) | 49¢ | 56% | -$6.92 | -7% |
| 6–10¢ | 5 | 4 (80%) | 32¢ | 40% | $23.42 | +141% |
| 10–20¢ | 2 | 2 (100%) | 28¢ | 43% | $14.01 | +234% |
| 20¢+ | 1 | 1 (100%) | 35¢ | 58% | $6.34 | +173% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 26 | 16 (62%) | 45¢ | 53% | $37.92 | +31% |
| 5–10 min | 1 | 0 (0%) | 10¢ | 16% | -$1.07 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 3 | 1 (33%) | 17¢ | 27% | $4.48 | +81% |
| Toss-up (25–75¢) | 23 | 14 (61%) | 46¢ | 54% | $30.10 | +27% |
| Favorite (75–95¢) | 1 | 1 (100%) | 76¢ | 82% | $2.27 | +29% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 3 | 2 (67%) | 32¢ | 40% | $9.83 | +97% |
| ZEC | 3 | 2 (67%) | 44¢ | 53% | $6.27 | +46% |
| XRP | 3 | 2 (67%) | 26¢ | 31% | $11.92 | +148% |
| NEAR | 3 | 1 (33%) | 61¢ | 67% | -$8.71 | -47% |
| ETH | 3 | 1 (33%) | 50¢ | 57% | -$5.43 | -35% |
| BNB | 3 | 3 (100%) | 45¢ | 56% | $16.02 | +115% |
| DOGE | 3 | 1 (33%) | 39¢ | 47% | -$2.15 | -18% |
| HYPE | 3 | 2 (67%) | 53¢ | 65% | $3.60 | +22% |
| BTC | 3 | 2 (67%) | 47¢ | 54% | $5.50 | +38% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/27 11:16:19 PM | ETH | DOWN | 13.7 min | 37¢ | 47% | 8¢ | Open | — |
| 9/27 11:16:17 PM | ZEC | DOWN | 13.7 min | 42¢ | 49% | 5¢ | Open | — |
| 9/27 11:16:13 PM | DOGE | DOWN | 13.8 min | 35¢ | 45% | 8¢ | Open | — |
| 9/27 11:16:11 PM | XRP | DOWN | 13.8 min | 35¢ | 42% | 5¢ | Open | — |
| 9/27 11:16:11 PM | BTC | DOWN | 13.8 min | 35¢ | 43% | 7¢ | Open | — |
| 9/27 11:16:11 PM | SOL | DOWN | 13.8 min | 28¢ | 35% | 6¢ | Open | — |
| 9/27 11:16:11 PM | NEAR | DOWN | 13.8 min | 32¢ | 44% | 10¢ | Open | — |
| 9/27 11:16:09 PM | HYPE | DOWN | 13.8 min | 37¢ | 43% | 4¢ | Open | — |
| 9/27 11:16:04 PM | BNB | DOWN | 13.9 min | 34¢ | 42% | 7¢ | Open | — |
| 9/27 11:02:20 PM | DOGE | DOWN | 12.7 min | 35¢ | 47% | 10¢ | ✅ Won | $6.34 |
| 9/27 11:02:04 PM | BTC | DOWN | 12.9 min | 46¢ | 53% | 5¢ | ✅ Won | $5.22 |
| 9/27 11:02:02 PM | XRP | DOWN | 12.9 min | 27¢ | 33% | 5¢ | ✅ Won | $7.16 |
| 9/27 11:01:30 PM | SOL | DOWN | 13.5 min | 27¢ | 34% | 6¢ | ✅ Won | $7.16 |
| 9/27 11:01:16 PM | ETH | DOWN | 13.7 min | 37¢ | 45% | 6¢ | ✅ Won | $6.13 |
| 9/27 11:01:05 PM | HYPE | DOWN | 13.9 min | 35¢ | 58% | 21¢ | ✅ Won | $6.34 |
| 9/27 11:01:05 PM | ZEC | DOWN | 13.9 min | 29¢ | 39% | 8¢ | ✅ Won | $6.95 |
| 9/27 11:01:05 PM | BNB | DOWN | 13.9 min | 22¢ | 40% | 16¢ | ✅ Won | $7.67 |
| 9/27 11:01:05 PM | NEAR | DOWN | 13.9 min | 57¢ | 64% | 5¢ | ✅ Won | $4.12 |
| 9/27 10:50:43 PM | XRP | UP | 9.3 min | 10¢ | 16% | 5¢ | ❌ Lost | -$1.07 |
| 9/27 10:48:51 PM | DOGE | UP | 11.2 min | 20¢ | 25% | 4¢ | ❌ Lost | -$2.12 |
| 9/27 10:47:23 PM | BTC | DOWN | 12.6 min | 63¢ | 70% | 6¢ | ❌ Lost | -$6.47 |
| 9/27 10:47:20 PM | HYPE | DOWN | 12.7 min | 67¢ | 73% | 4¢ | ✅ Won | $3.14 |
| 9/27 10:46:32 PM | ZEC | DOWN | 13.5 min | 76¢ | 82% | 5¢ | ✅ Won | $2.27 |
| 9/27 10:46:26 PM | ETH | DOWN | 13.6 min | 56¢ | 62% | 4¢ | ❌ Lost | -$5.78 |
| 9/27 10:46:20 PM | SOL | UP | 13.7 min | 33¢ | 39% | 5¢ | ❌ Lost | -$3.46 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
