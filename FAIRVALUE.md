# Fair-Value Bot

*Updated Tue Sep 29, 1:07 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1299 | $121.18 | +2% | $139.52 / -$18.34 |
| 4¢+ ← live bot | 1256 | $319.61 | +6% | $246.21 / $73.40 |
| 6¢+ | 1151 | $319.11 | +7% | $335.17 / -$16.06 |
| 8¢+ | 993 | $369.62 | +9% | $340.69 / $28.93 |
| 10¢+ | 835 | $291.09 | +9% | $175.39 / $115.70 |
| 15¢+ | 501 | $337.54 | +20% | $164.44 / $173.10 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1275 | 1266 | 600 (47%) | 44¢ | 53% | $191.18 | +3% | +5.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 864 | 374 (43%) | 276 / 588 | 8.6 | -$43.45 | -$229.73 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 733 | 241 (33%) | 333 / 400 | 7.3 | -$55.90 | -$325.64 | -12% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 184 | 59 (32%) | 51 / 133 | 2.0 | -$14.97 | -$124.69 | -17% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 197 | 81 (41%) | 67 / 130 | 2.0 | -$13.69 | -$36.52 | -4% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 108 | 49 (45%) | 38 / 70 | 1.5 | -$10.05 | -$13.98 | -3% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 74 | 34 (46%) | 27 / 47 | 1.5 | -$20.08 | -$35.54 | -5% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 23 | 8 (35%) | 10 / 13 | 1.6 | -$5.79 | -$10.38 | -11% |

*Model accuracy vs Kalshi's prices on the same 20,742 readings (excluding the final minute): V1 **+1.1%**, V2 **+1.4%**, 3-exchange price (V3/V4) **-0.2%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $464.48 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 872 | 744 (85%) | -$213.33 | -6% | 231,514 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.6%** over 33,115 readings from 1314 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 5777 | 2% | 4% | 5% |
| 10–20% | 2589 | 15% | 16% | 16% |
| 20–30% | 2760 | 25% | 26% | 26% |
| 30–40% | 3054 | 35% | 36% | 39% |
| 40–50% | 3286 | 45% | 48% | 53% |
| 50–60% | 3243 | 55% | 59% | 61% |
| 60–70% | 2877 | 65% | 70% | 73% |
| 70–80% | 2327 | 75% | 80% | 83% |
| 80–90% | 2057 | 85% | 88% | 87% |
| 90–100% | 5145 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 652 | 317 (49%) | 45¢ | 51% | $152.13 | +5% |
| 6–10¢ | 445 | 214 (48%) | 44¢ | 53% | $98.62 | +5% |
| 10–20¢ | 158 | 65 (41%) | 43¢ | 57% | -$54.26 | -8% |
| 20¢+ | 11 | 4 (36%) | 40¢ | 68% | -$5.31 | -12% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1112 | 539 (48%) | 45¢ | 54% | $191.63 | +4% |
| 5–10 min | 141 | 55 (39%) | 37¢ | 46% | $3.47 | +1% |
| 2–5 min | 11 | 5 (45%) | 48¢ | 55% | -$3.52 | -7% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 170 | 33 (19%) | 18¢ | 27% | -$1.96 | -1% |
| Toss-up (25–75¢) | 995 | 479 (48%) | 45¢ | 54% | $152.23 | +3% |
| Favorite (75–95¢) | 101 | 88 (87%) | 82¢ | 89% | $40.91 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 144 | 75 (52%) | 44¢ | 54% | $93.91 | +14% |
| XRP | 143 | 71 (50%) | 45¢ | 53% | $43.45 | +7% |
| ETH | 142 | 62 (44%) | 46¢ | 54% | -$49.46 | -7% |
| SOL | 140 | 70 (50%) | 42¢ | 50% | $89.31 | +15% |
| NEAR | 140 | 68 (49%) | 46¢ | 53% | $20.54 | +3% |
| HYPE | 140 | 61 (44%) | 43¢ | 52% | -$18.74 | -3% |
| ZEC | 139 | 60 (43%) | 41¢ | 50% | $4.13 | +1% |
| DOGE | 139 | 61 (44%) | 43¢ | 52% | -$15.76 | -3% |
| BTC | 139 | 72 (52%) | 49¢ | 57% | $23.80 | +3% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 1:05:57 PM | ETH | DOWN | 9.1 min | 27¢ | 36% | 8¢ | Open | — |
| 9/29 1:05:13 PM | DOGE | UP | 9.8 min | 81¢ | 86% | 4¢ | Open | — |
| 9/29 1:03:02 PM | ZEC | DOWN | 12.0 min | 30¢ | 37% | 5¢ | Open | — |
| 9/29 1:03:02 PM | NEAR | DOWN | 12.0 min | 27¢ | 33% | 5¢ | Open | — |
| 9/29 1:02:59 PM | HYPE | DOWN | 12.0 min | 33¢ | 39% | 4¢ | Open | — |
| 9/29 1:02:09 PM | BNB | DOWN | 12.8 min | 38¢ | 48% | 8¢ | Open | — |
| 9/29 1:01:11 PM | SOL | UP | 13.8 min | 52¢ | 63% | 9¢ | Open | — |
| 9/29 1:01:11 PM | BTC | UP | 13.8 min | 42¢ | 52% | 8¢ | Open | — |
| 9/29 1:01:11 PM | XRP | UP | 13.8 min | 46¢ | 54% | 6¢ | Open | — |
| 9/29 12:52:32 PM | DOGE | UP | 7.5 min | 32¢ | 39% | 5¢ | ❌ Lost | -$3.36 |
| 9/29 12:50:14 PM | ZEC | UP | 9.8 min | 7¢ | 12% | 5¢ | ❌ Lost | -$0.70 |
| 9/29 12:49:41 PM | HYPE | UP | 10.3 min | 20¢ | 26% | 5¢ | ✅ Won | $7.86 |
| 9/29 12:49:06 PM | ETH | UP | 10.9 min | 38¢ | 44% | 5¢ | ❌ Lost | -$3.97 |
| 9/29 12:49:06 PM | XRP | UP | 10.9 min | 26¢ | 34% | 7¢ | ✅ Won | $7.26 |
| 9/29 12:48:36 PM | SOL | UP | 11.4 min | 20¢ | 27% | 6¢ | ❌ Lost | -$2.12 |
| 9/29 12:47:37 PM | BTC | UP | 12.4 min | 30¢ | 36% | 4¢ | ❌ Lost | -$3.15 |
| 9/29 12:47:03 PM | NEAR | UP | 12.9 min | 24¢ | 29% | 4¢ | ❌ Lost | -$2.53 |
| 9/29 12:46:07 PM | BNB | DOWN | 13.9 min | 49¢ | 72% | 21¢ | ✅ Won | $4.92 |
| 9/29 12:36:38 PM | BTC | DOWN | 8.3 min | 19¢ | 24% | 4¢ | ❌ Lost | -$2.01 |
| 9/29 12:36:11 PM | NEAR | DOWN | 8.8 min | 32¢ | 38% | 4¢ | ❌ Lost | -$3.36 |
| 9/29 12:34:29 PM | DOGE | DOWN | 10.5 min | 49¢ | 58% | 7¢ | ❌ Lost | -$5.08 |
| 9/29 12:34:29 PM | ZEC | DOWN | 10.5 min | 26¢ | 36% | 9¢ | ❌ Lost | -$2.74 |
| 9/29 12:34:29 PM | SOL | DOWN | 10.5 min | 38¢ | 45% | 6¢ | ❌ Lost | -$3.92 |
| 9/29 12:34:23 PM | XRP | DOWN | 10.6 min | 24¢ | 30% | 4¢ | ❌ Lost | -$2.53 |
| 9/29 12:33:39 PM | HYPE | DOWN | 11.3 min | 35¢ | 43% | 6¢ | ❌ Lost | -$3.71 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
