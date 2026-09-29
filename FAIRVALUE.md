# Fair-Value Bot

*Updated Tue Sep 29, 3:39 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1389 | $163.57 | +2% | $95.84 / $67.73 |
| 4¢+ | 1346 | $300.87 | +5% | $256.35 / $44.52 |
| 6¢+ | 1236 | $292.03 | +6% | $294.09 / -$2.06 |
| 8¢+ ← live bot | 1070 | $403.99 | +9% | $346.26 / $57.73 |
| 10¢+ | 906 | $367.41 | +11% | $258.85 / $108.56 |
| 15¢+ | 543 | $368.56 | +20% | $234.82 / $133.74 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1363 | 1354 | 634 (47%) | 45¢ | 53% | $104.01 | +2% | +4.6¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 952 | 408 (43%) | 305 / 647 | 8.6 | -$43.45 | -$316.90 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 812 | 280 (34%) | 364 / 448 | 7.3 | -$55.90 | -$239.62 | -8% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 204 | 65 (32%) | 56 / 148 | 2.0 | -$14.97 | -$149.52 | -19% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 217 | 92 (42%) | 70 / 147 | 2.0 | -$13.69 | -$18.31 | -2% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 121 | 52 (43%) | 43 / 78 | 1.5 | -$10.05 | -$33.39 | -7% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 86 | 37 (43%) | 32 / 54 | 1.5 | -$20.08 | -$78.20 | -10% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 26 | 10 (38%) | 11 / 15 | 1.6 | -$5.79 | -$1.88 | -2% |

*Model accuracy vs Kalshi's prices on the same 22,963 readings (excluding the final minute): V1 **+1.2%**, V2 **+1.7%**, 3-exchange price (V3/V4) **-0.1%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $421.82 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 960 | 832 (87%) | -$300.50 | -8% | 234,677 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.7%** over 35,516 readings from 1404 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 6222 | 2% | 4% | 5% |
| 10–20% | 2729 | 15% | 16% | 15% |
| 20–30% | 2969 | 25% | 26% | 25% |
| 30–40% | 3334 | 35% | 36% | 37% |
| 40–50% | 3583 | 45% | 48% | 51% |
| 50–60% | 3515 | 55% | 59% | 60% |
| 60–70% | 3075 | 65% | 70% | 72% |
| 70–80% | 2480 | 75% | 80% | 82% |
| 80–90% | 2211 | 85% | 88% | 86% |
| 90–100% | 5398 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 698 | 336 (48%) | 45¢ | 52% | $105.50 | +3% |
| 6–10¢ | 470 | 223 (47%) | 44¢ | 53% | $76.95 | +4% |
| 10–20¢ | 174 | 71 (41%) | 43¢ | 57% | -$68.88 | -9% |
| 20¢+ | 12 | 4 (33%) | 40¢ | 68% | -$9.56 | -19% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1178 | 565 (48%) | 45¢ | 54% | $121.09 | +2% |
| 5–10 min | 163 | 63 (39%) | 38¢ | 46% | -$13.16 | -2% |
| 2–5 min | 11 | 5 (45%) | 48¢ | 55% | -$3.52 | -7% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 178 | 33 (19%) | 18¢ | 27% | -$16.80 | -5% |
| Toss-up (25–75¢) | 1067 | 508 (48%) | 45¢ | 54% | $98.32 | +2% |
| Favorite (75–95¢) | 109 | 93 (85%) | 82¢ | 89% | $22.49 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 154 | 77 (50%) | 44¢ | 54% | $66.97 | +10% |
| XRP | 153 | 72 (47%) | 46¢ | 54% | -$2.25 | -0% |
| ETH | 152 | 67 (44%) | 46¢ | 54% | -$55.04 | -8% |
| NEAR | 150 | 73 (49%) | 45¢ | 53% | $30.43 | +4% |
| SOL | 149 | 75 (50%) | 42¢ | 50% | $98.17 | +15% |
| ZEC | 149 | 65 (44%) | 41¢ | 50% | $9.32 | +1% |
| DOGE | 149 | 65 (44%) | 44¢ | 52% | -$25.55 | -4% |
| HYPE | 149 | 65 (44%) | 43¢ | 52% | -$19.61 | -3% |
| BTC | 149 | 75 (50%) | 49¢ | 57% | $1.57 | +0% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 3:37:45 PM | SOL | DOWN | 7.2 min | 24¢ | 32% | 6¢ | Open | — |
| 9/29 3:35:17 PM | XRP | DOWN | 9.7 min | 25¢ | 34% | 7¢ | Open | — |
| 9/29 3:34:04 PM | ETH | DOWN | 10.9 min | 31¢ | 43% | 11¢ | Open | — |
| 9/29 3:33:04 PM | BTC | DOWN | 11.9 min | 36¢ | 43% | 5¢ | Open | — |
| 9/29 3:32:42 PM | DOGE | DOWN | 12.3 min | 47¢ | 56% | 7¢ | Open | — |
| 9/29 3:31:39 PM | ZEC | DOWN | 13.3 min | 32¢ | 38% | 4¢ | Open | — |
| 9/29 3:31:25 PM | BNB | DOWN | 13.6 min | 56¢ | 63% | 5¢ | Open | — |
| 9/29 3:31:19 PM | NEAR | DOWN | 13.7 min | 50¢ | 57% | 5¢ | Open | — |
| 9/29 3:31:11 PM | HYPE | DOWN | 13.8 min | 45¢ | 53% | 6¢ | Open | — |
| 9/29 3:20:48 PM | XRP | DOWN | 9.2 min | 93¢ | 97% | 4¢ | ✅ Won | $0.68 |
| 9/29 3:20:15 PM | ZEC | UP | 9.8 min | 37¢ | 46% | 8¢ | ❌ Lost | -$3.86 |
| 9/29 3:20:13 PM | BNB | UP | 9.8 min | 13¢ | 27% | 13¢ | ❌ Lost | -$1.38 |
| 9/29 3:20:04 PM | NEAR | UP | 9.9 min | 16¢ | 22% | 5¢ | ❌ Lost | -$1.70 |
| 9/29 3:16:14 PM | ETH | DOWN | 13.8 min | 67¢ | 73% | 4¢ | ✅ Won | $3.14 |
| 9/29 3:16:13 PM | BTC | DOWN | 13.8 min | 65¢ | 75% | 9¢ | ✅ Won | $3.34 |
| 9/29 3:16:13 PM | DOGE | UP | 13.8 min | 32¢ | 46% | 13¢ | ❌ Lost | -$3.36 |
| 9/29 3:05:00 PM | NEAR | DOWN | 10.0 min | 93¢ | 98% | 4¢ | ✅ Won | $0.63 |
| 9/29 3:04:56 PM | HYPE | DOWN | 10.1 min | 64¢ | 70% | 4¢ | ❌ Lost | -$6.52 |
| 9/29 3:03:35 PM | ZEC | DOWN | 11.4 min | 85¢ | 91% | 5¢ | ✅ Won | $1.41 |
| 9/29 3:03:24 PM | XRP | DOWN | 11.6 min | 89¢ | 94% | 4¢ | ❌ Lost | -$8.97 |
| 9/29 3:02:48 PM | SOL | DOWN | 12.2 min | 85¢ | 91% | 5¢ | ✅ Won | $1.41 |
| 9/29 3:02:06 PM | ETH | DOWN | 12.9 min | 72¢ | 78% | 5¢ | ✅ Won | $2.66 |
| 9/29 3:01:53 PM | DOGE | UP | 13.1 min | 35¢ | 48% | 12¢ | ✅ Won | $6.34 |
| 9/29 3:01:07 PM | BTC | DOWN | 13.9 min | 59¢ | 65% | 5¢ | ✅ Won | $3.93 |
| 9/29 3:01:07 PM | BNB | DOWN | 13.9 min | 52¢ | 61% | 7¢ | ✅ Won | $4.62 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
