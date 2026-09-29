# Fair-Value Bot

*Updated Tue Sep 29, 2:08 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1335 | $146.19 | +2% | $114.96 / $31.23 |
| 4¢+ ← live bot | 1292 | $328.59 | +6% | $243.66 / $84.93 |
| 6¢+ | 1186 | $344.39 | +7% | $285.12 / $59.27 |
| 8¢+ | 1027 | $403.56 | +10% | $368.67 / $34.89 |
| 10¢+ | 867 | $337.46 | +10% | $251.68 / $85.78 |
| 15¢+ | 520 | $367.90 | +21% | $220.71 / $147.19 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1310 | 1302 | 617 (47%) | 44¢ | 53% | $178.41 | +3% | +4.9¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 900 | 391 (43%) | 289 / 611 | 8.6 | -$43.45 | -$242.50 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 764 | 262 (34%) | 340 / 424 | 7.3 | -$55.90 | -$247.55 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 192 | 62 (32%) | 54 / 138 | 2.0 | -$14.97 | -$132.16 | -18% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 205 | 87 (42%) | 67 / 138 | 2.0 | -$13.69 | -$20.09 | -2% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 113 | 51 (45%) | 39 / 74 | 1.5 | -$10.05 | -$11.57 | -3% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 79 | 36 (46%) | 28 / 51 | 1.5 | -$20.08 | -$31.10 | -4% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 24 | 9 (38%) | 10 / 14 | 1.6 | -$5.79 | -$4.45 | -5% |

*Model accuracy vs Kalshi's prices on the same 21,626 readings (excluding the final minute): V1 **+1.4%**, V2 **+1.7%**, 3-exchange price (V3/V4) **-0.0%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $468.92 | $525.36 | $394.02 | 0 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 908 | 780 (86%) | -$226.10 | -6% | 232,108 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.7%** over 34,071 readings from 1350 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 5932 | 2% | 4% | 5% |
| 10–20% | 2640 | 15% | 16% | 15% |
| 20–30% | 2839 | 25% | 26% | 26% |
| 30–40% | 3136 | 35% | 36% | 38% |
| 40–50% | 3408 | 45% | 48% | 51% |
| 50–60% | 3393 | 55% | 59% | 59% |
| 60–70% | 2979 | 65% | 70% | 71% |
| 70–80% | 2395 | 75% | 80% | 82% |
| 80–90% | 2114 | 85% | 88% | 85% |
| 90–100% | 5235 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 667 | 323 (48%) | 45¢ | 51% | $135.20 | +4% |
| 6–10¢ | 456 | 220 (48%) | 44¢ | 53% | $107.03 | +5% |
| 10–20¢ | 168 | 70 (42%) | 44¢ | 58% | -$58.51 | -8% |
| 20¢+ | 11 | 4 (36%) | 40¢ | 68% | -$5.31 | -12% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1142 | 554 (49%) | 45¢ | 54% | $184.02 | +3% |
| 5–10 min | 147 | 57 (39%) | 38¢ | 46% | -$1.69 | -0% |
| 2–5 min | 11 | 5 (45%) | 48¢ | 55% | -$3.52 | -7% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 172 | 33 (19%) | 18¢ | 27% | -$5.67 | -2% |
| Toss-up (25–75¢) | 1027 | 495 (48%) | 45¢ | 54% | $149.11 | +3% |
| Favorite (75–95¢) | 103 | 89 (86%) | 82¢ | 89% | $34.97 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 148 | 76 (51%) | 44¢ | 54% | $81.98 | +12% |
| XRP | 147 | 71 (48%) | 45¢ | 53% | $23.34 | +3% |
| ETH | 146 | 64 (44%) | 46¢ | 54% | -$52.06 | -8% |
| SOL | 144 | 72 (50%) | 42¢ | 50% | $90.95 | +14% |
| NEAR | 144 | 70 (49%) | 45¢ | 53% | $26.54 | +4% |
| HYPE | 144 | 65 (45%) | 43¢ | 52% | $3.47 | +1% |
| ZEC | 143 | 63 (44%) | 41¢ | 50% | $17.04 | +3% |
| DOGE | 143 | 64 (45%) | 44¢ | 53% | -$12.66 | -2% |
| BTC | 143 | 72 (50%) | 49¢ | 57% | -$0.19 | -0% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 2:05:25 PM | SOL | UP | 9.6 min | 50¢ | 56% | 4¢ | Open | — |
| 9/29 2:05:19 PM | ZEC | DOWN | 9.7 min | 43¢ | 51% | 6¢ | Open | — |
| 9/29 2:03:59 PM | ETH | DOWN | 11.0 min | 71¢ | 78% | 5¢ | Open | — |
| 9/29 2:02:18 PM | DOGE | DOWN | 12.7 min | 69¢ | 76% | 6¢ | Open | — |
| 9/29 2:02:06 PM | XRP | DOWN | 12.9 min | 75¢ | 83% | 7¢ | Open | — |
| 9/29 2:01:23 PM | BNB | DOWN | 13.6 min | 27¢ | 41% | 13¢ | Open | — |
| 9/29 2:01:08 PM | NEAR | DOWN | 13.8 min | 29¢ | 37% | 7¢ | Open | — |
| 9/29 2:01:08 PM | HYPE | DOWN | 13.8 min | 41¢ | 48% | 6¢ | Open | — |
| 9/29 1:47:56 PM | NEAR | DOWN | 12.1 min | 48¢ | 57% | 7¢ | ✅ Won | $5.02 |
| 9/29 1:47:55 PM | HYPE | DOWN | 12.1 min | 38¢ | 53% | 13¢ | ✅ Won | $6.03 |
| 9/29 1:47:39 PM | ZEC | UP | 12.3 min | 27¢ | 44% | 16¢ | ❌ Lost | -$2.82 |
| 9/29 1:47:39 PM | XRP | UP | 12.3 min | 58¢ | 71% | 11¢ | ❌ Lost | -$5.98 |
| 9/29 1:46:59 PM | BNB | DOWN | 13.0 min | 64¢ | 79% | 13¢ | ❌ Lost | -$6.62 |
| 9/29 1:46:32 PM | SOL | UP | 13.4 min | 19¢ | 27% | 7¢ | ❌ Lost | -$2.01 |
| 9/29 1:46:12 PM | DOGE | DOWN | 13.8 min | 71¢ | 78% | 6¢ | ✅ Won | $2.75 |
| 9/29 1:46:06 PM | BTC | DOWN | 13.9 min | 64¢ | 74% | 8¢ | ❌ Lost | -$6.57 |
| 9/29 1:46:06 PM | ETH | DOWN | 13.9 min | 76¢ | 88% | 11¢ | ✅ Won | $2.27 |
| 9/29 1:38:14 PM | XRP | UP | 6.8 min | 38¢ | 45% | 5¢ | ❌ Lost | -$3.97 |
| 9/29 1:32:49 PM | ETH | UP | 12.2 min | 70¢ | 76% | 4¢ | ❌ Lost | -$7.15 |
| 9/29 1:32:43 PM | SOL | UP | 12.3 min | 73¢ | 85% | 11¢ | ❌ Lost | -$7.44 |
| 9/29 1:32:15 PM | BTC | UP | 12.8 min | 63¢ | 70% | 5¢ | ❌ Lost | -$6.47 |
| 9/29 1:31:53 PM | ZEC | DOWN | 13.1 min | 39¢ | 45% | 4¢ | ✅ Won | $5.93 |
| 9/29 1:31:22 PM | BNB | DOWN | 13.6 min | 48¢ | 59% | 9¢ | ✅ Won | $5.03 |
| 9/29 1:31:09 PM | NEAR | DOWN | 13.8 min | 43¢ | 51% | 6¢ | ✅ Won | $5.52 |
| 9/29 1:31:09 PM | HYPE | DOWN | 13.8 min | 48¢ | 61% | 11¢ | ✅ Won | $5.02 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
