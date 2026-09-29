# Fair-Value Bot

*Updated Tue Sep 29, 5:47 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1470 | $179.29 | +3% | $94.71 / $84.58 |
| 4¢+ | 1423 | $317.22 | +5% | $311.80 / $5.42 |
| 6¢+ | 1309 | $303.55 | +5% | $299.95 / $3.60 |
| 8¢+ ← live bot | 1136 | $398.13 | +9% | $350.87 / $47.26 |
| 10¢+ | 960 | $369.94 | +10% | $289.71 / $80.23 |
| 15¢+ | 580 | $343.24 | +17% | $243.72 / $99.52 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1422 | 1420 | 659 (46%) | 44¢ | 53% | $66.17 | +1% | +4.3¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 39 | 22 | 14 / 8 | $9.87 | $7.29 | -$2.58 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1018 | 433 (43%) | 324 / 694 | 8.5 | -$43.45 | -$354.74 | -8% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 878 | 293 (33%) | 395 / 483 | 7.3 | -$55.90 | -$355.71 | -11% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 222 | 72 (32%) | 62 / 160 | 2.0 | -$14.97 | -$145.94 | -17% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 235 | 98 (42%) | 76 / 159 | 2.0 | -$13.69 | -$41.19 | -4% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 134 | 56 (42%) | 48 / 86 | 1.5 | -$10.05 | -$45.54 | -8% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 29 | 11 (38%) | 12 / 17 | 1.6 | -$5.89 | -$3.35 | -3% |

*Model accuracy vs Kalshi's prices on the same 24,970 readings (excluding the final minute): V1 **+1.0%**, V2 **+1.3%**, 3-exchange price (V3/V4) **-0.2%**.*

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
| 1026 | 898 (88%) | -$338.34 | -8% | 238,671 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.6%** over 37,685 readings from 1485 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 6633 | 2% | 4% | 5% |
| 10–20% | 2912 | 15% | 16% | 15% |
| 20–30% | 3152 | 25% | 26% | 26% |
| 30–40% | 3507 | 35% | 36% | 38% |
| 40–50% | 3761 | 45% | 48% | 52% |
| 50–60% | 3658 | 55% | 59% | 60% |
| 60–70% | 3229 | 65% | 70% | 73% |
| 70–80% | 2645 | 75% | 80% | 83% |
| 80–90% | 2371 | 85% | 88% | 87% |
| 90–100% | 5817 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 502 | 236 (47%) | 44¢ | 53% | $56.59 | +2% |
| 10–20¢ | 193 | 80 (41%) | 42¢ | 57% | -$47.82 | -6% |
| 20¢+ | 14 | 5 (36%) | 41¢ | 68% | -$8.97 | -15% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1221 | 582 (48%) | 46¢ | 54% | $72.61 | +1% |
| 5–10 min | 178 | 70 (39%) | 38¢ | 46% | $4.73 | +1% |
| 2–5 min | 17 | 6 (35%) | 37¢ | 47% | -$5.09 | -8% |
| 1–2 min | 4 | 1 (25%) | 39¢ | 61% | -$6.08 | -38% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 192 | 35 (18%) | 18¢ | 27% | -$20.55 | -6% |
| Toss-up (25–75¢) | 1111 | 523 (47%) | 45¢ | 54% | $47.83 | +1% |
| Favorite (75–95¢) | 117 | 101 (86%) | 82¢ | 89% | $38.89 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| XRP | 161 | 77 (48%) | 46¢ | 53% | $13.02 | +2% |
| BNB | 161 | 79 (49%) | 44¢ | 54% | $55.90 | +8% |
| ETH | 160 | 70 (44%) | 46¢ | 55% | -$61.87 | -8% |
| NEAR | 158 | 74 (47%) | 45¢ | 53% | $8.90 | +1% |
| ZEC | 157 | 67 (43%) | 41¢ | 50% | $0.13 | +0% |
| BTC | 157 | 80 (51%) | 49¢ | 57% | $5.59 | +1% |
| HYPE | 156 | 67 (43%) | 44¢ | 53% | -$32.56 | -5% |
| SOL | 155 | 78 (50%) | 42¢ | 50% | $108.83 | +16% |
| DOGE | 155 | 67 (43%) | 44¢ | 52% | -$31.77 | -5% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 5:46:42 PM | SOL | DOWN | 13.3 min | 23¢ | 32% | 8¢ | Open | — |
| 9/29 5:46:14 PM | BNB | DOWN | 13.8 min | 31¢ | 58% | 26¢ | Open | — |
| 9/29 5:35:35 PM | ETH | DOWN | 9.4 min | 75¢ | 86% | 9¢ | ✅ Won | $2.36 |
| 9/29 5:35:15 PM | BTC | DOWN | 9.7 min | 66¢ | 78% | 11¢ | ✅ Won | $3.24 |
| 9/29 5:35:15 PM | XRP | DOWN | 9.7 min | 88¢ | 97% | 9¢ | ✅ Won | $1.12 |
| 9/29 5:34:42 PM | ZEC | DOWN | 10.3 min | 60¢ | 71% | 9¢ | ✅ Won | $3.79 |
| 9/29 5:20:09 PM | DOGE | UP | 9.8 min | 15¢ | 27% | 11¢ | ❌ Lost | -$1.59 |
| 9/29 5:19:54 PM | XRP | UP | 10.1 min | 25¢ | 38% | 11¢ | ❌ Lost | -$2.64 |
| 9/29 5:19:22 PM | SOL | UP | 10.6 min | 32¢ | 42% | 8¢ | ❌ Lost | -$3.33 |
| 9/29 5:16:46 PM | ZEC | DOWN | 13.2 min | 51¢ | 62% | 9¢ | ✅ Won | $4.72 |
| 9/29 5:16:36 PM | BNB | DOWN | 13.4 min | 50¢ | 63% | 11¢ | ✅ Won | $4.82 |
| 9/29 5:16:13 PM | NEAR | DOWN | 13.8 min | 45¢ | 57% | 10¢ | ✅ Won | $5.32 |
| 9/29 5:11:44 PM | ZEC | DOWN | 3.3 min | 11¢ | 24% | 12¢ | ❌ Lost | -$1.17 |
| 9/29 5:03:28 PM | XRP | DOWN | 11.5 min | 32¢ | 43% | 9¢ | ❌ Lost | -$3.39 |
| 9/29 5:02:49 PM | BTC | UP | 12.2 min | 69¢ | 85% | 14¢ | ✅ Won | $2.95 |
| 9/29 5:02:14 PM | NEAR | DOWN | 12.8 min | 47¢ | 58% | 9¢ | ❌ Lost | -$4.88 |
| 9/29 5:01:18 PM | HYPE | DOWN | 13.7 min | 49¢ | 60% | 9¢ | ❌ Lost | -$5.08 |
| 9/29 5:01:05 PM | ETH | DOWN | 13.9 min | 41¢ | 53% | 10¢ | ❌ Lost | -$4.27 |
| 9/29 5:01:03 PM | BNB | DOWN | 13.9 min | 59¢ | 69% | 9¢ | ❌ Lost | -$6.06 |
| 9/29 4:55:02 PM | BTC | DOWN | 5.0 min | 33¢ | 44% | 9¢ | ❌ Lost | -$3.46 |
| 9/29 4:54:30 PM | XRP | DOWN | 5.5 min | 29¢ | 42% | 11¢ | ✅ Won | $6.95 |
| 9/29 4:54:13 PM | ETH | DOWN | 5.8 min | 16¢ | 30% | 13¢ | ❌ Lost | -$1.70 |
| 9/29 4:52:09 PM | HYPE | DOWN | 7.8 min | 28¢ | 40% | 11¢ | ✅ Won | $7.05 |
| 9/29 4:48:05 PM | BNB | DOWN | 11.9 min | 33¢ | 47% | 12¢ | ❌ Lost | -$3.46 |
| 9/29 4:47:12 PM | NEAR | DOWN | 12.8 min | 44¢ | 55% | 10¢ | ❌ Lost | -$4.57 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
