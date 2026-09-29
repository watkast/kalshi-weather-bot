# Fair-Value Bot

*Updated Tue Sep 29, 12:27 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1272 | $104.31 | +2% | $190.88 / -$86.57 |
| 4¢+ ← live bot | 1229 | $313.27 | +6% | $297.03 / $16.24 |
| 6¢+ | 1127 | $330.70 | +7% | $317.63 / $13.07 |
| 8¢+ | 972 | $384.04 | +10% | $291.46 / $92.58 |
| 10¢+ | 819 | $286.45 | +9% | $190.78 / $95.67 |
| 15¢+ | 493 | $317.70 | +19% | $171.19 / $146.51 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1249 | 1240 | 597 (48%) | 45¢ | 53% | $246.51 | +4% | +5.3¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 838 | 371 (44%) | 267 / 571 | 8.6 | -$43.45 | -$174.40 | -4% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 708 | 228 (32%) | 312 / 396 | 7.2 | -$55.90 | -$344.39 | -13% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 178 | 59 (33%) | 49 / 129 | 2.0 | -$14.97 | -$104.06 | -15% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 191 | 81 (42%) | 65 / 126 | 2.0 | -$13.69 | -$14.86 | -2% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 104 | 49 (47%) | 37 / 67 | 1.5 | -$10.05 | $0.81 | +0% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 70 | 34 (49%) | 26 / 44 | 1.5 | -$20.08 | $3.27 | +0% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 21 | 7 (33%) | 9 / 12 | 1.6 | -$5.79 | -$14.18 | -17% |

*Model accuracy vs Kalshi's prices on the same 20,085 readings (excluding the final minute): V1 **+1.3%**, V2 **+1.5%**, 3-exchange price (V3/V4) **-0.0%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $503.29 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 846 | 718 (85%) | -$158.00 | -5% | 226,064 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.7%** over 32,404 readings from 1287 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 5733 | 2% | 4% | 5% |
| 10–20% | 2549 | 15% | 16% | 16% |
| 20–30% | 2717 | 25% | 26% | 26% |
| 30–40% | 2991 | 35% | 36% | 39% |
| 40–50% | 3211 | 45% | 48% | 53% |
| 50–60% | 3148 | 55% | 59% | 61% |
| 60–70% | 2799 | 65% | 70% | 73% |
| 70–80% | 2277 | 75% | 80% | 83% |
| 80–90% | 1995 | 85% | 88% | 86% |
| 90–100% | 4984 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 635 | 316 (50%) | 45¢ | 52% | $195.26 | +7% |
| 6–10¢ | 438 | 213 (49%) | 45¢ | 54% | $112.28 | +6% |
| 10–20¢ | 157 | 65 (41%) | 43¢ | 57% | -$50.80 | -7% |
| 20¢+ | 10 | 3 (30%) | 39¢ | 68% | -$10.23 | -25% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1095 | 536 (49%) | 45¢ | 54% | $220.37 | +4% |
| 5–10 min | 132 | 55 (42%) | 38¢ | 47% | $30.06 | +6% |
| 2–5 min | 11 | 5 (45%) | 48¢ | 55% | -$3.52 | -7% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 163 | 32 (20%) | 18¢ | 27% | $2.29 | +1% |
| Toss-up (25–75¢) | 976 | 477 (49%) | 45¢ | 54% | $203.31 | +4% |
| Favorite (75–95¢) | 101 | 88 (87%) | 82¢ | 89% | $40.91 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 141 | 74 (52%) | 44¢ | 54% | $96.82 | +15% |
| XRP | 140 | 70 (50%) | 45¢ | 53% | $42.69 | +6% |
| ETH | 140 | 62 (44%) | 46¢ | 54% | -$40.41 | -6% |
| SOL | 137 | 70 (51%) | 42¢ | 51% | $98.09 | +16% |
| NEAR | 137 | 68 (50%) | 46¢ | 54% | $29.58 | +5% |
| HYPE | 137 | 60 (44%) | 44¢ | 53% | -$19.43 | -3% |
| ZEC | 136 | 60 (44%) | 42¢ | 51% | $11.34 | +2% |
| DOGE | 136 | 61 (45%) | 44¢ | 52% | -$5.10 | -1% |
| BTC | 136 | 72 (53%) | 49¢ | 57% | $32.93 | +5% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 12:22:22 PM | SOL | DOWN | 7.6 min | 26¢ | 32% | 5¢ | Open | — |
| 9/29 12:21:42 PM | DOGE | DOWN | 8.3 min | 21¢ | 28% | 6¢ | Open | — |
| 9/29 12:21:17 PM | BTC | DOWN | 8.7 min | 38¢ | 44% | 4¢ | Open | — |
| 9/29 12:20:27 PM | ETH | DOWN | 9.5 min | 49¢ | 55% | 4¢ | Open | — |
| 9/29 12:20:20 PM | NEAR | DOWN | 9.7 min | 30¢ | 38% | 6¢ | Open | — |
| 9/29 12:18:06 PM | ZEC | UP | 11.9 min | 36¢ | 42% | 4¢ | Open | — |
| 9/29 12:16:33 PM | XRP | DOWN | 13.4 min | 38¢ | 44% | 5¢ | Open | — |
| 9/29 12:16:28 PM | BNB | DOWN | 13.5 min | 30¢ | 40% | 9¢ | Open | — |
| 9/29 12:16:09 PM | HYPE | DOWN | 13.8 min | 33¢ | 48% | 13¢ | Open | — |
| 9/29 12:02:33 PM | HYPE | DOWN | 12.4 min | 24¢ | 31% | 5¢ | ❌ Lost | -$2.53 |
| 9/29 12:02:03 PM | NEAR | DOWN | 12.9 min | 24¢ | 31% | 6¢ | ❌ Lost | -$2.53 |
| 9/29 12:01:49 PM | DOGE | UP | 13.2 min | 84¢ | 93% | 8¢ | ✅ Won | $1.50 |
| 9/29 12:01:20 PM | BNB | UP | 13.7 min | 91¢ | 97% | 6¢ | ✅ Won | $0.85 |
| 9/29 12:01:20 PM | ETH | UP | 13.7 min | 89¢ | 99% | 9¢ | ✅ Won | $1.03 |
| 9/29 12:01:20 PM | BTC | UP | 13.7 min | 89¢ | 99% | 9¢ | ✅ Won | $1.03 |
| 9/29 12:01:20 PM | XRP | UP | 13.7 min | 89¢ | 96% | 6¢ | ✅ Won | $1.03 |
| 9/29 12:01:20 PM | ZEC | UP | 13.7 min | 91¢ | 98% | 6¢ | ✅ Won | $0.85 |
| 9/29 12:01:20 PM | SOL | UP | 13.7 min | 88¢ | 96% | 7¢ | ✅ Won | $1.12 |
| 9/29 11:52:12 AM | ZEC | DOWN | 7.8 min | 76¢ | 82% | 4¢ | ✅ Won | $2.27 |
| 9/29 11:49:27 AM | XRP | DOWN | 10.6 min | 70¢ | 77% | 5¢ | ✅ Won | $2.85 |
| 9/29 11:49:26 AM | DOGE | UP | 10.6 min | 20¢ | 26% | 5¢ | ❌ Lost | -$2.13 |
| 9/29 11:46:13 AM | BNB | DOWN | 13.8 min | 49¢ | 58% | 7¢ | ✅ Won | $4.92 |
| 9/29 11:46:13 AM | NEAR | DOWN | 13.8 min | 45¢ | 51% | 5¢ | ✅ Won | $5.33 |
| 9/29 11:46:13 AM | BTC | DOWN | 13.8 min | 51¢ | 57% | 4¢ | ✅ Won | $4.72 |
| 9/29 11:46:13 AM | SOL | DOWN | 13.8 min | 45¢ | 58% | 11¢ | ✅ Won | $5.32 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
