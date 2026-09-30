# Fair-Value Bot

*Updated Wed Sep 30, 5:54 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1902 | $175.33 | +2% | $109.35 / $65.98 |
| 4¢+ | 1850 | $334.30 | +4% | $300.39 / $33.91 |
| 6¢+ | 1714 | $280.92 | +4% | $308.47 / -$27.55 |
| 8¢+ ← live bot | 1496 | $425.99 | +7% | $299.27 / $126.72 |
| 10¢+ | 1278 | $422.99 | +9% | $205.54 / $217.45 |
| 15¢+ | 790 | $557.19 | +21% | $217.23 / $339.96 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1761 | 1757 | 788 (45%) | 43¢ | 53% | $27.12 | +0% | +3.2¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 376 | 251 | 157 / 94 | -$29.18 | $78.60 | $107.78 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1355 | 562 (41%) | 391 / 964 | 8.1 | -$43.45 | -$393.79 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1231 | 411 (33%) | 513 / 718 | 7.4 | -$55.90 | -$400.38 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 311 | 108 (35%) | 79 / 232 | 2.0 | -$14.97 | -$100.18 | -8% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 329 | 142 (43%) | 99 / 230 | 2.0 | -$13.69 | -$10.08 | -1% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 199 | 82 (41%) | 68 / 131 | 1.5 | -$10.05 | -$73.14 | -9% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 4 | 4 (100%) | 0 / 4 | 1.0 | $0.97 | $6.69 | +20% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 45 | 15 (33%) | 16 / 29 | 1.5 | -$5.89 | -$13.12 | -8% |

*Model accuracy vs Kalshi's prices on the same 35,189 readings (excluding the final minute): V1 **+0.4%**, V2 **+1.2%**, 3-exchange price (V3/V4) **-0.6%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

⛔ **HALTED** — equity $389.72 fell below stop $394.02 (peak $525.36)

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $389.72 | $525.36 | $394.02 | 0 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 1363 | 1235 (91%) | -$377.39 | -7% | 250,759 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.1%** over 48,676 readings from 1917 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 8371 | 3% | 4% | 5% |
| 10–20% | 3710 | 15% | 17% | 15% |
| 20–30% | 4061 | 25% | 26% | 26% |
| 30–40% | 4477 | 35% | 37% | 39% |
| 40–50% | 4806 | 45% | 48% | 51% |
| 50–60% | 4729 | 55% | 59% | 59% |
| 60–70% | 4152 | 65% | 71% | 72% |
| 70–80% | 3473 | 75% | 80% | 83% |
| 80–90% | 3257 | 85% | 88% | 89% |
| 90–100% | 7640 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 655 | 294 (45%) | 43¢ | 52% | $50.04 | +2% |
| 10–20¢ | 369 | 148 (40%) | 41¢ | 55% | -$79.10 | -5% |
| 20¢+ | 22 | 8 (36%) | 39¢ | 66% | -$10.19 | -11% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1415 | 655 (46%) | 45¢ | 54% | -$25.67 | -0% |
| 5–10 min | 274 | 102 (37%) | 36¢ | 46% | -$5.05 | -0% |
| 2–5 min | 60 | 27 (45%) | 34¢ | 46% | $60.74 | +29% |
| 1–2 min | 6 | 2 (33%) | 44¢ | 63% | -$6.82 | -25% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 278 | 45 (16%) | 18¢ | 28% | -$82.05 | -15% |
| Toss-up (25–75¢) | 1348 | 628 (47%) | 45¢ | 54% | $44.16 | +1% |
| Favorite (75–95¢) | 131 | 115 (88%) | 82¢ | 90% | $65.01 | +6% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 207 | 91 (44%) | 42¢ | 54% | -$1.94 | -0% |
| ETH | 203 | 90 (44%) | 46¢ | 55% | -$55.78 | -6% |
| HYPE | 200 | 86 (43%) | 43¢ | 52% | -$21.73 | -2% |
| XRP | 195 | 88 (45%) | 44¢ | 53% | -$11.28 | -1% |
| BTC | 195 | 100 (51%) | 49¢ | 58% | $18.61 | +2% |
| ZEC | 193 | 78 (40%) | 39¢ | 49% | -$9.32 | -1% |
| DOGE | 192 | 78 (41%) | 42¢ | 51% | -$48.75 | -6% |
| NEAR | 188 | 84 (45%) | 43¢ | 51% | $4.31 | +1% |
| SOL | 184 | 93 (51%) | 41¢ | 50% | $153.00 | +20% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/30 5:47:21 AM | BTC | DOWN | 12.7 min | 69¢ | 79% | 8¢ | Open | — |
| 9/30 5:47:01 AM | SOL | UP | 13.0 min | 39¢ | 50% | 10¢ | Open | — |
| 9/30 5:46:52 AM | DOGE | DOWN | 13.1 min | 63¢ | 85% | 21¢ | Open | — |
| 9/30 5:46:13 AM | BNB | DOWN | 13.8 min | 49¢ | 61% | 10¢ | Open | — |
| 9/30 5:40:28 AM | NEAR | DOWN | 4.5 min | 69¢ | 80% | 10¢ | ✅ Won | $2.95 |
| 9/30 5:37:34 AM | BTC | UP | 7.4 min | 29¢ | 42% | 11¢ | ✅ Won | $6.95 |
| 9/30 5:37:06 AM | ZEC | DOWN | 7.9 min | 36¢ | 60% | 22¢ | ❌ Lost | -$3.77 |
| 9/30 5:36:50 AM | ETH | DOWN | 8.2 min | 29¢ | 43% | 12¢ | ❌ Lost | -$3.05 |
| 9/30 5:35:52 AM | DOGE | DOWN | 9.1 min | 36¢ | 53% | 15¢ | ❌ Lost | -$3.77 |
| 9/30 5:31:26 AM | XRP | UP | 13.6 min | 25¢ | 43% | 16¢ | ✅ Won | $7.36 |
| 9/30 5:31:26 AM | HYPE | UP | 13.6 min | 28¢ | 38% | 8¢ | ❌ Lost | -$2.95 |
| 9/30 5:31:12 AM | SOL | UP | 13.8 min | 27¢ | 39% | 11¢ | ✅ Won | $7.16 |
| 9/30 5:31:07 AM | BNB | DOWN | 13.9 min | 42¢ | 58% | 14¢ | ❌ Lost | -$4.38 |
| 9/30 5:26:50 AM | BTC | DOWN | 3.1 min | 29¢ | 41% | 10¢ | ❌ Lost | -$3.05 |
| 9/30 5:23:54 AM | ETH | DOWN | 6.1 min | 18¢ | 32% | 13¢ | ❌ Lost | -$1.91 |
| 9/30 5:20:02 AM | XRP | UP | 10.0 min | 24¢ | 34% | 9¢ | ✅ Won | $7.47 |
| 9/30 5:20:02 AM | SOL | UP | 10.0 min | 21¢ | 33% | 10¢ | ✅ Won | $7.78 |
| 9/30 5:19:47 AM | BNB | UP | 10.2 min | 24¢ | 34% | 9¢ | ❌ Lost | -$2.53 |
| 9/30 5:18:57 AM | ZEC | DOWN | 11.1 min | 53¢ | 71% | 16¢ | ❌ Lost | -$5.48 |
| 9/30 5:18:36 AM | HYPE | DOWN | 11.4 min | 53¢ | 66% | 11¢ | ❌ Lost | -$5.48 |
| 9/30 5:18:04 AM | DOGE | DOWN | 11.9 min | 37¢ | 47% | 8¢ | ❌ Lost | -$3.87 |
| 9/30 5:05:03 AM | NEAR | DOWN | 9.9 min | 30¢ | 45% | 13¢ | ❌ Lost | -$3.15 |
| 9/30 5:03:17 AM | HYPE | DOWN | 11.7 min | 45¢ | 61% | 15¢ | ✅ Won | $5.32 |
| 9/30 5:01:15 AM | BNB | DOWN | 13.7 min | 67¢ | 79% | 10¢ | ✅ Won | $3.14 |
| 9/30 4:57:05 AM | BTC | UP | 2.9 min | 63¢ | 76% | 11¢ | ✅ Won | $3.53 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
