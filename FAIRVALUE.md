# Fair-Value Bot

*Updated Mon Sep 28, 9:13 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **4¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 376 | $193.78 | +11% | $243.79 / -$50.01 |
| 4¢+ ← live bot | 363 | $236.40 | +14% | $314.84 / -$78.44 |
| 6¢+ | 346 | $213.78 | +15% | $266.36 / -$52.58 |
| 8¢+ | 314 | $148.26 | +13% | $183.11 / -$34.85 |
| 10¢+ | 282 | $165.82 | +16% | $182.98 / -$17.16 |
| 15¢+ | 180 | $172.69 | +29% | $154.84 / $17.85 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 385 | 376 | 212 (56%) | 45¢ | 52% | $386.34 | +22% | +13.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.4%** over 10,287 readings from 387 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1865 | 2% | 4% | 8% |
| 10–20% | 821 | 15% | 16% | 18% |
| 20–30% | 838 | 25% | 26% | 31% |
| 30–40% | 920 | 35% | 37% | 42% |
| 40–50% | 955 | 45% | 48% | 50% |
| 50–60% | 963 | 55% | 58% | 55% |
| 60–70% | 943 | 65% | 70% | 65% |
| 70–80% | 848 | 75% | 79% | 78% |
| 80–90% | 702 | 85% | 88% | 81% |
| 90–100% | 1432 | 97% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 239 | 134 (56%) | 46¢ | 52% | $210.86 | +19% |
| 6–10¢ | 108 | 62 (57%) | 42¢ | 51% | $146.36 | +31% |
| 10–20¢ | 26 | 14 (54%) | 43¢ | 58% | $23.12 | +20% |
| 20¢+ | 3 | 2 (67%) | 45¢ | 69% | $6.00 | +43% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 372 | 212 (57%) | 45¢ | 53% | $390.72 | +23% |
| 5–10 min | 4 | 0 (0%) | 10¢ | 17% | -$4.38 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 38 | 8 (21%) | 18¢ | 25% | $8.28 | +12% |
| Toss-up (25–75¢) | 326 | 193 (59%) | 46¢ | 54% | $361.82 | +23% |
| Favorite (75–95¢) | 12 | 11 (92%) | 77¢ | 83% | $16.24 | +17% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 42 | 26 (62%) | 43¢ | 51% | $72.07 | +38% |
| ZEC | 42 | 23 (55%) | 44¢ | 51% | $40.13 | +21% |
| XRP | 42 | 24 (57%) | 47¢ | 54% | $37.08 | +18% |
| NEAR | 42 | 25 (60%) | 46¢ | 54% | $48.50 | +24% |
| ETH | 42 | 20 (48%) | 44¢ | 51% | $9.29 | +5% |
| DOGE | 42 | 23 (55%) | 45¢ | 53% | $34.76 | +18% |
| BTC | 42 | 27 (64%) | 47¢ | 55% | $65.62 | +32% |
| BNB | 41 | 24 (59%) | 42¢ | 51% | $61.87 | +35% |
| HYPE | 41 | 20 (49%) | 43¢ | 52% | $17.02 | +9% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 9:01:59 AM | NEAR | DOWN | 13.0 min | 45¢ | 52% | 5¢ | Open | — |
| 9/28 9:01:51 AM | HYPE | DOWN | 13.1 min | 38¢ | 45% | 5¢ | Open | — |
| 9/28 9:01:31 AM | ZEC | DOWN | 13.5 min | 47¢ | 54% | 5¢ | Open | — |
| 9/28 9:01:31 AM | DOGE | DOWN | 13.5 min | 36¢ | 42% | 5¢ | Open | — |
| 9/28 9:01:19 AM | BNB | DOWN | 13.7 min | 36¢ | 47% | 9¢ | Open | — |
| 9/28 9:01:15 AM | SOL | DOWN | 13.8 min | 34¢ | 40% | 4¢ | Open | — |
| 9/28 9:01:15 AM | ETH | DOWN | 13.8 min | 37¢ | 44% | 5¢ | Open | — |
| 9/28 9:01:13 AM | BTC | DOWN | 13.8 min | 38¢ | 45% | 5¢ | Open | — |
| 9/28 9:01:13 AM | XRP | DOWN | 13.8 min | 36¢ | 42% | 4¢ | Open | — |
| 9/28 8:46:34 AM | BNB | DOWN | 13.4 min | 42¢ | 48% | 4¢ | ✅ Won | $5.62 |
| 9/28 8:46:32 AM | ZEC | DOWN | 13.5 min | 74¢ | 80% | 4¢ | ✅ Won | $2.46 |
| 9/28 8:46:26 AM | BTC | DOWN | 13.6 min | 35¢ | 42% | 5¢ | ❌ Lost | -$3.66 |
| 9/28 8:46:24 AM | NEAR | UP | 13.6 min | 65¢ | 71% | 4¢ | ✅ Won | $3.34 |
| 9/28 8:46:08 AM | SOL | DOWN | 13.9 min | 40¢ | 46% | 4¢ | ✅ Won | $5.83 |
| 9/28 8:46:08 AM | XRP | DOWN | 13.9 min | 46¢ | 53% | 6¢ | ✅ Won | $5.22 |
| 9/28 8:46:06 AM | ETH | DOWN | 13.9 min | 36¢ | 44% | 6¢ | ❌ Lost | -$3.77 |
| 9/28 8:46:06 AM | DOGE | DOWN | 13.9 min | 35¢ | 42% | 6¢ | ❌ Lost | -$3.66 |
| 9/28 8:46:04 AM | HYPE | DOWN | 13.9 min | 43¢ | 50% | 5¢ | ❌ Lost | -$4.48 |
| 9/28 8:31:26 AM | NEAR | DOWN | 13.6 min | 54¢ | 60% | 4¢ | ✅ Won | $4.42 |
| 9/28 8:31:12 AM | XRP | DOWN | 13.8 min | 42¢ | 49% | 5¢ | ✅ Won | $5.62 |
| 9/28 8:31:12 AM | ETH | DOWN | 13.8 min | 32¢ | 40% | 6¢ | ✅ Won | $6.64 |
| 9/28 8:31:08 AM | SOL | DOWN | 13.8 min | 28¢ | 35% | 5¢ | ✅ Won | $7.05 |
| 9/28 8:31:04 AM | BTC | DOWN | 13.9 min | 29¢ | 38% | 8¢ | ✅ Won | $6.95 |
| 9/28 8:31:04 AM | HYPE | DOWN | 13.9 min | 37¢ | 44% | 5¢ | ✅ Won | $6.13 |
| 9/28 8:31:04 AM | BNB | DOWN | 13.9 min | 29¢ | 35% | 5¢ | ✅ Won | $6.95 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
