# Fair-Value Bot

*Updated Tue Sep 29, 3:49 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1398 | $131.96 | +2% | $86.04 / $45.92 |
| 4¢+ | 1354 | $275.77 | +4% | $258.62 / $17.15 |
| 6¢+ | 1244 | $264.30 | +5% | $281.09 / -$16.79 |
| 8¢+ ← live bot | 1077 | $384.74 | +9% | $357.36 / $27.38 |
| 10¢+ | 913 | $352.87 | +10% | $249.71 / $103.16 |
| 15¢+ | 548 | $357.06 | +19% | $232.92 / $124.14 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1372 | 1363 | 634 (47%) | 44¢ | 53% | $67.90 | +1% | +4.5¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 961 | 408 (42%) | 305 / 656 | 8.6 | -$43.45 | -$353.01 | -8% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 821 | 280 (34%) | 364 / 457 | 7.3 | -$55.90 | -$278.90 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 206 | 65 (32%) | 56 / 150 | 2.0 | -$14.97 | -$156.74 | -19% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 219 | 92 (42%) | 70 / 149 | 2.0 | -$13.69 | -$28.21 | -3% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 122 | 52 (43%) | 43 / 79 | 1.5 | -$10.05 | -$37.74 | -8% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 87 | 37 (43%) | 32 / 55 | 1.4 | -$20.08 | -$86.48 | -11% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 26 | 10 (38%) | 11 / 15 | 1.6 | -$5.79 | -$1.88 | -2% |

*Model accuracy vs Kalshi's prices on the same 23,188 readings (excluding the final minute): V1 **+1.0%**, V2 **+1.4%**, 3-exchange price (V3/V4) **-0.3%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $413.54 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 969 | 841 (87%) | -$336.61 | -9% | 235,281 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.5%** over 35,759 readings from 1413 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 6222 | 2% | 4% | 5% |
| 10–20% | 2735 | 15% | 16% | 16% |
| 20–30% | 2970 | 25% | 26% | 25% |
| 30–40% | 3344 | 35% | 36% | 38% |
| 40–50% | 3603 | 45% | 48% | 52% |
| 50–60% | 3540 | 55% | 59% | 60% |
| 60–70% | 3122 | 65% | 70% | 72% |
| 70–80% | 2525 | 75% | 80% | 82% |
| 80–90% | 2246 | 85% | 88% | 86% |
| 90–100% | 5452 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 703 | 336 (48%) | 45¢ | 52% | $82.69 | +3% |
| 6–10¢ | 473 | 223 (47%) | 44¢ | 53% | $66.90 | +3% |
| 10–20¢ | 175 | 71 (41%) | 43¢ | 57% | -$72.13 | -9% |
| 20¢+ | 12 | 4 (33%) | 40¢ | 68% | -$9.56 | -19% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1185 | 565 (48%) | 45¢ | 54% | $90.15 | +2% |
| 5–10 min | 165 | 63 (38%) | 38¢ | 46% | -$18.33 | -3% |
| 2–5 min | 11 | 5 (45%) | 48¢ | 55% | -$3.52 | -7% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 179 | 33 (18%) | 18¢ | 27% | -$19.33 | -6% |
| Toss-up (25–75¢) | 1075 | 508 (47%) | 45¢ | 54% | $64.74 | +1% |
| Favorite (75–95¢) | 109 | 93 (85%) | 82¢ | 89% | $22.49 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 155 | 77 (50%) | 44¢ | 54% | $61.15 | +9% |
| XRP | 154 | 72 (47%) | 46¢ | 53% | -$4.89 | -1% |
| ETH | 153 | 67 (44%) | 46¢ | 54% | -$58.29 | -8% |
| NEAR | 151 | 73 (48%) | 45¢ | 53% | $25.25 | +4% |
| SOL | 150 | 75 (50%) | 42¢ | 50% | $95.64 | +15% |
| ZEC | 150 | 65 (43%) | 41¢ | 50% | $5.96 | +1% |
| DOGE | 150 | 65 (43%) | 44¢ | 52% | -$30.43 | -4% |
| HYPE | 150 | 65 (43%) | 43¢ | 52% | -$24.29 | -4% |
| BTC | 150 | 75 (50%) | 49¢ | 57% | -$2.20 | -0% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 3:49:25 PM | NEAR | DOWN | 10.6 min | 33¢ | 39% | 4¢ | Open | — |
| 9/29 3:47:07 PM | DOGE | DOWN | 12.9 min | 68¢ | 75% | 5¢ | Open | — |
| 9/29 3:46:53 PM | SOL | UP | 13.1 min | 26¢ | 31% | 4¢ | Open | — |
| 9/29 3:46:22 PM | XRP | UP | 13.6 min | 30¢ | 38% | 6¢ | Open | — |
| 9/29 3:46:18 PM | HYPE | DOWN | 13.7 min | 68¢ | 74% | 5¢ | Open | — |
| 9/29 3:46:04 PM | ETH | DOWN | 13.9 min | 78¢ | 86% | 7¢ | Open | — |
| 9/29 3:46:04 PM | BTC | DOWN | 13.9 min | 75¢ | 92% | 16¢ | Open | — |
| 9/29 3:46:04 PM | ZEC | DOWN | 13.9 min | 61¢ | 69% | 7¢ | Open | — |
| 9/29 3:46:04 PM | BNB | DOWN | 13.9 min | 69¢ | 77% | 7¢ | Open | — |
| 9/29 3:37:45 PM | SOL | DOWN | 7.2 min | 24¢ | 32% | 6¢ | ❌ Lost | -$2.53 |
| 9/29 3:35:17 PM | XRP | DOWN | 9.7 min | 25¢ | 34% | 7¢ | ❌ Lost | -$2.64 |
| 9/29 3:34:04 PM | ETH | DOWN | 10.9 min | 31¢ | 43% | 11¢ | ❌ Lost | -$3.25 |
| 9/29 3:33:04 PM | BTC | DOWN | 11.9 min | 36¢ | 43% | 5¢ | ❌ Lost | -$3.77 |
| 9/29 3:32:42 PM | DOGE | DOWN | 12.3 min | 47¢ | 56% | 7¢ | ❌ Lost | -$4.88 |
| 9/29 3:31:39 PM | ZEC | DOWN | 13.3 min | 32¢ | 38% | 4¢ | ❌ Lost | -$3.36 |
| 9/29 3:31:25 PM | BNB | DOWN | 13.6 min | 56¢ | 63% | 5¢ | ❌ Lost | -$5.82 |
| 9/29 3:31:19 PM | NEAR | DOWN | 13.7 min | 50¢ | 57% | 5¢ | ❌ Lost | -$5.18 |
| 9/29 3:31:11 PM | HYPE | DOWN | 13.8 min | 45¢ | 53% | 6¢ | ❌ Lost | -$4.68 |
| 9/29 3:20:48 PM | XRP | DOWN | 9.2 min | 93¢ | 97% | 4¢ | ✅ Won | $0.68 |
| 9/29 3:20:15 PM | ZEC | UP | 9.8 min | 37¢ | 46% | 8¢ | ❌ Lost | -$3.86 |
| 9/29 3:20:13 PM | BNB | UP | 9.8 min | 13¢ | 27% | 13¢ | ❌ Lost | -$1.38 |
| 9/29 3:20:04 PM | NEAR | UP | 9.9 min | 16¢ | 22% | 5¢ | ❌ Lost | -$1.70 |
| 9/29 3:16:14 PM | ETH | DOWN | 13.8 min | 67¢ | 73% | 4¢ | ✅ Won | $3.14 |
| 9/29 3:16:13 PM | BTC | DOWN | 13.8 min | 65¢ | 75% | 9¢ | ✅ Won | $3.34 |
| 9/29 3:16:13 PM | DOGE | UP | 13.8 min | 32¢ | 46% | 13¢ | ❌ Lost | -$3.36 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
