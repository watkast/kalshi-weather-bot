# Fair-Value Bot

*Updated Tue Sep 29, 6:27 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **10¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **10¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1488 | $185.19 | +3% | $128.90 / $56.29 |
| 4¢+ | 1441 | $299.02 | +5% | $339.96 / -$40.94 |
| 6¢+ | 1327 | $268.70 | +5% | $324.08 / -$55.38 |
| 8¢+ ← live bot | 1153 | $378.37 | +8% | $340.05 / $38.32 |
| 10¢+ | 976 | $379.40 | +10% | $286.76 / $92.64 |
| 15¢+ | 589 | $352.25 | +18% | $247.05 / $105.20 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1442 | 1435 | 665 (46%) | 44¢ | 53% | $76.34 | +1% | +4.2¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 54 | 31 | 22 / 9 | $20.04 | -$2.01 | -$22.05 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1033 | 439 (42%) | 325 / 708 | 8.5 | -$43.45 | -$344.57 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 894 | 299 (33%) | 395 / 499 | 7.3 | -$55.90 | -$353.23 | -11% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 226 | 74 (33%) | 62 / 164 | 2.0 | -$14.97 | -$134.28 | -15% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 239 | 100 (42%) | 76 / 163 | 2.0 | -$13.69 | -$34.56 | -3% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 137 | 58 (42%) | 49 / 88 | 1.5 | -$10.05 | -$38.36 | -7% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 30 | 12 (40%) | 12 / 18 | 1.6 | -$5.89 | $3.81 | +3% |

*Model accuracy vs Kalshi's prices on the same 25,410 readings (excluding the final minute): V1 **+0.9%**, V2 **+1.1%**, 3-exchange price (V3/V4) **-0.4%**.*

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
| 1041 | 913 (88%) | -$328.17 | -8% | 241,028 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.5%** over 38,161 readings from 1503 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 6697 | 2% | 4% | 5% |
| 10–20% | 2919 | 15% | 16% | 15% |
| 20–30% | 3163 | 25% | 26% | 26% |
| 30–40% | 3532 | 35% | 36% | 38% |
| 40–50% | 3788 | 45% | 48% | 52% |
| 50–60% | 3698 | 55% | 59% | 60% |
| 60–70% | 3309 | 65% | 70% | 73% |
| 70–80% | 2736 | 75% | 80% | 83% |
| 80–90% | 2435 | 85% | 88% | 87% |
| 90–100% | 5884 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 508 | 238 (47%) | 44¢ | 53% | $60.52 | +3% |
| 10–20¢ | 201 | 84 (42%) | 42¢ | 56% | -$38.33 | -4% |
| 20¢+ | 15 | 5 (33%) | 40¢ | 68% | -$12.22 | -20% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1231 | 587 (48%) | 45¢ | 54% | $86.32 | +1% |
| 5–10 min | 181 | 70 (39%) | 37¢ | 46% | -$1.31 | -0% |
| 2–5 min | 19 | 7 (37%) | 37¢ | 47% | -$2.59 | -4% |
| 1–2 min | 4 | 1 (25%) | 39¢ | 61% | -$6.08 | -38% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 199 | 36 (18%) | 18¢ | 27% | -$26.30 | -7% |
| Toss-up (25–75¢) | 1119 | 528 (47%) | 45¢ | 54% | $63.75 | +1% |
| Favorite (75–95¢) | 117 | 101 (86%) | 82¢ | 89% | $38.89 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| XRP | 163 | 78 (48%) | 45¢ | 53% | $15.31 | +2% |
| BNB | 163 | 80 (49%) | 44¢ | 54% | $59.31 | +8% |
| ETH | 162 | 71 (44%) | 46¢ | 54% | -$58.27 | -8% |
| NEAR | 159 | 74 (47%) | 45¢ | 53% | $6.99 | +1% |
| BTC | 159 | 80 (50%) | 49¢ | 57% | -$3.39 | -0% |
| ZEC | 158 | 68 (43%) | 41¢ | 50% | $4.85 | +1% |
| HYPE | 158 | 68 (43%) | 43¢ | 52% | -$28.03 | -4% |
| SOL | 157 | 79 (50%) | 42¢ | 50% | $113.87 | +17% |
| DOGE | 156 | 67 (43%) | 44¢ | 52% | -$34.30 | -5% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 6:27:09 PM | SOL | UP | 2.8 min | 16¢ | 36% | 19¢ | Open | — |
| 9/29 6:24:39 PM | HYPE | DOWN | 5.3 min | 52¢ | 65% | 11¢ | Open | — |
| 9/29 6:21:23 PM | BNB | UP | 8.6 min | 23¢ | 34% | 9¢ | Open | — |
| 9/29 6:18:06 PM | BTC | DOWN | 11.9 min | 72¢ | 82% | 9¢ | Open | — |
| 9/29 6:17:50 PM | ETH | DOWN | 12.2 min | 55¢ | 66% | 9¢ | Open | — |
| 9/29 6:17:15 PM | ZEC | DOWN | 12.8 min | 36¢ | 46% | 9¢ | Open | — |
| 9/29 6:16:28 PM | XRP | DOWN | 13.5 min | 41¢ | 54% | 11¢ | Open | — |
| 9/29 6:10:48 PM | ZEC | DOWN | 4.2 min | 51¢ | 63% | 10¢ | ✅ Won | $4.72 |
| 9/29 6:04:47 PM | XRP | DOWN | 10.2 min | 51¢ | 62% | 9¢ | ✅ Won | $4.72 |
| 9/29 6:03:26 PM | SOL | DOWN | 11.6 min | 24¢ | 35% | 10¢ | ✅ Won | $7.47 |
| 9/29 6:03:26 PM | HYPE | DOWN | 11.6 min | 36¢ | 48% | 11¢ | ✅ Won | $6.23 |
| 9/29 6:03:26 PM | ETH | DOWN | 11.6 min | 35¢ | 47% | 10¢ | ✅ Won | $6.34 |
| 9/29 6:03:13 PM | BTC | UP | 11.8 min | 66¢ | 78% | 11¢ | ❌ Lost | -$6.76 |
| 9/29 6:01:04 PM | BNB | DOWN | 13.9 min | 32¢ | 48% | 14¢ | ✅ Won | $6.66 |
| 9/29 5:57:01 PM | BTC | DOWN | 3.0 min | 21¢ | 32% | 10¢ | ❌ Lost | -$2.22 |
| 9/29 5:51:21 PM | HYPE | DOWN | 8.7 min | 16¢ | 26% | 9¢ | ❌ Lost | -$1.70 |
| 9/29 5:50:47 PM | NEAR | DOWN | 9.2 min | 18¢ | 27% | 8¢ | ❌ Lost | -$1.91 |
| 9/29 5:50:33 PM | XRP | DOWN | 9.4 min | 23¢ | 35% | 11¢ | ❌ Lost | -$2.43 |
| 9/29 5:48:52 PM | ETH | DOWN | 11.1 min | 26¢ | 39% | 11¢ | ❌ Lost | -$2.74 |
| 9/29 5:47:33 PM | DOGE | DOWN | 12.4 min | 24¢ | 36% | 10¢ | ❌ Lost | -$2.53 |
| 9/29 5:46:42 PM | SOL | DOWN | 13.3 min | 23¢ | 32% | 8¢ | ❌ Lost | -$2.43 |
| 9/29 5:46:14 PM | BNB | DOWN | 13.8 min | 31¢ | 58% | 26¢ | ❌ Lost | -$3.25 |
| 9/29 5:35:35 PM | ETH | DOWN | 9.4 min | 75¢ | 86% | 9¢ | ✅ Won | $2.36 |
| 9/29 5:35:15 PM | BTC | DOWN | 9.7 min | 66¢ | 78% | 11¢ | ✅ Won | $3.24 |
| 9/29 5:35:15 PM | XRP | DOWN | 9.7 min | 88¢ | 97% | 9¢ | ✅ Won | $1.12 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
