# Fair-Value Bot

*Updated Mon Sep 28, 8:53 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **4¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 367 | $196.25 | +11% | $242.05 / -$45.80 |
| 4¢+ ← live bot | 354 | $238.15 | +15% | $302.15 / -$64.00 |
| 6¢+ | 337 | $215.36 | +16% | $257.82 / -$42.46 |
| 8¢+ | 306 | $149.23 | +13% | $181.90 / -$32.67 |
| 10¢+ | 274 | $176.29 | +17% | $180.06 / -$3.77 |
| 15¢+ | 173 | $173.86 | +31% | $152.08 / $21.78 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 376 | 367 | 207 (56%) | 44¢ | 52% | $379.44 | +22% | +13.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.4%** over 10,035 readings from 378 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 1830 | 2% | 4% | 8% |
| 10–20% | 805 | 15% | 16% | 18% |
| 20–30% | 821 | 25% | 26% | 31% |
| 30–40% | 898 | 35% | 36% | 43% |
| 40–50% | 929 | 45% | 48% | 50% |
| 50–60% | 913 | 55% | 58% | 54% |
| 60–70% | 905 | 65% | 70% | 64% |
| 70–80% | 832 | 75% | 79% | 78% |
| 80–90% | 690 | 85% | 88% | 81% |
| 90–100% | 1412 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 231 | 129 (56%) | 46¢ | 52% | $200.19 | +18% |
| 6–10¢ | 107 | 62 (58%) | 42¢ | 51% | $150.13 | +32% |
| 10–20¢ | 26 | 14 (54%) | 43¢ | 58% | $23.12 | +20% |
| 20¢+ | 3 | 2 (67%) | 45¢ | 69% | $6.00 | +43% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 363 | 207 (57%) | 45¢ | 53% | $383.82 | +23% |
| 5–10 min | 4 | 0 (0%) | 10¢ | 17% | -$4.38 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 38 | 8 (21%) | 18¢ | 25% | $8.28 | +12% |
| Toss-up (25–75¢) | 317 | 188 (59%) | 46¢ | 55% | $354.92 | +23% |
| Favorite (75–95¢) | 12 | 11 (92%) | 77¢ | 83% | $16.24 | +17% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| SOL | 41 | 25 (61%) | 43¢ | 51% | $66.24 | +36% |
| ZEC | 41 | 22 (54%) | 43¢ | 51% | $37.67 | +21% |
| XRP | 41 | 23 (56%) | 47¢ | 54% | $31.86 | +16% |
| NEAR | 41 | 24 (59%) | 46¢ | 54% | $45.16 | +23% |
| ETH | 41 | 20 (49%) | 44¢ | 52% | $13.06 | +7% |
| DOGE | 41 | 23 (56%) | 45¢ | 53% | $38.42 | +20% |
| BTC | 41 | 27 (66%) | 47¢ | 55% | $69.28 | +35% |
| BNB | 40 | 23 (57%) | 42¢ | 51% | $56.25 | +32% |
| HYPE | 40 | 20 (50%) | 43¢ | 52% | $21.50 | +12% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 8:46:34 AM | BNB | DOWN | 13.4 min | 42¢ | 48% | 4¢ | Open | — |
| 9/28 8:46:32 AM | ZEC | DOWN | 13.5 min | 74¢ | 80% | 4¢ | Open | — |
| 9/28 8:46:26 AM | BTC | DOWN | 13.6 min | 35¢ | 42% | 5¢ | Open | — |
| 9/28 8:46:24 AM | NEAR | UP | 13.6 min | 65¢ | 71% | 4¢ | Open | — |
| 9/28 8:46:08 AM | SOL | DOWN | 13.9 min | 40¢ | 46% | 4¢ | Open | — |
| 9/28 8:46:08 AM | XRP | DOWN | 13.9 min | 46¢ | 53% | 6¢ | Open | — |
| 9/28 8:46:06 AM | ETH | DOWN | 13.9 min | 36¢ | 44% | 6¢ | Open | — |
| 9/28 8:46:06 AM | DOGE | DOWN | 13.9 min | 35¢ | 42% | 6¢ | Open | — |
| 9/28 8:46:04 AM | HYPE | DOWN | 13.9 min | 43¢ | 50% | 5¢ | Open | — |
| 9/28 8:31:26 AM | NEAR | DOWN | 13.6 min | 54¢ | 60% | 4¢ | ✅ Won | $4.42 |
| 9/28 8:31:12 AM | XRP | DOWN | 13.8 min | 42¢ | 49% | 5¢ | ✅ Won | $5.62 |
| 9/28 8:31:12 AM | ETH | DOWN | 13.8 min | 32¢ | 40% | 6¢ | ✅ Won | $6.64 |
| 9/28 8:31:08 AM | SOL | DOWN | 13.8 min | 28¢ | 35% | 5¢ | ✅ Won | $7.05 |
| 9/28 8:31:04 AM | BTC | DOWN | 13.9 min | 29¢ | 38% | 8¢ | ✅ Won | $6.95 |
| 9/28 8:31:04 AM | HYPE | DOWN | 13.9 min | 37¢ | 44% | 5¢ | ✅ Won | $6.13 |
| 9/28 8:31:04 AM | BNB | DOWN | 13.9 min | 29¢ | 35% | 5¢ | ✅ Won | $6.95 |
| 9/28 8:31:04 AM | ZEC | DOWN | 13.9 min | 28¢ | 40% | 10¢ | ✅ Won | $7.05 |
| 9/28 8:31:04 AM | DOGE | DOWN | 13.9 min | 27¢ | 39% | 10¢ | ✅ Won | $7.16 |
| 9/28 8:17:07 AM | BNB | UP | 12.9 min | 22¢ | 29% | 6¢ | ❌ Lost | -$2.33 |
| 9/28 8:16:19 AM | DOGE | DOWN | 13.7 min | 75¢ | 81% | 4¢ | ✅ Won | $2.36 |
| 9/28 8:16:13 AM | HYPE | DOWN | 13.8 min | 57¢ | 69% | 10¢ | ✅ Won | $4.12 |
| 9/28 8:16:11 AM | SOL | DOWN | 13.8 min | 70¢ | 80% | 8¢ | ✅ Won | $2.85 |
| 9/28 8:16:09 AM | BTC | DOWN | 13.8 min | 65¢ | 72% | 5¢ | ✅ Won | $3.34 |
| 9/28 8:16:09 AM | ETH | DOWN | 13.8 min | 60¢ | 67% | 5¢ | ✅ Won | $3.83 |
| 9/28 8:16:05 AM | XRP | DOWN | 13.9 min | 66¢ | 80% | 12¢ | ✅ Won | $3.24 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
