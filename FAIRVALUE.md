# Fair-Value Bot

*Updated Tue Sep 29, 4:26 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1416 | $135.18 | +2% | $88.97 / $46.21 |
| 4¢+ | 1372 | $266.17 | +4% | $251.62 / $14.55 |
| 6¢+ | 1262 | $262.02 | +5% | $299.10 / -$37.08 |
| 8¢+ ← live bot | 1093 | $370.30 | +8% | $361.80 / $8.50 |
| 10¢+ | 925 | $359.43 | +10% | $273.47 / $85.96 |
| 15¢+ | 557 | $360.00 | +19% | $252.21 / $107.79 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1387 | 1381 | 643 (47%) | 45¢ | 53% | $56.30 | +1% | +4.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 979 | 417 (43%) | 312 / 667 | 8.6 | -$43.45 | -$364.61 | -8% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 834 | 284 (34%) | 366 / 468 | 7.3 | -$55.90 | -$306.96 | -10% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 210 | 66 (31%) | 57 / 153 | 2.0 | -$14.97 | -$163.54 | -20% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 223 | 93 (42%) | 71 / 152 | 2.0 | -$13.69 | -$41.58 | -4% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 124 | 52 (42%) | 43 / 81 | 1.5 | -$10.05 | -$44.04 | -9% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 89 | 37 (42%) | 32 / 57 | 1.4 | -$20.08 | -$102.61 | -12% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 27 | 11 (41%) | 11 / 16 | 1.6 | -$5.79 | $2.54 | +2% |

*Model accuracy vs Kalshi's prices on the same 23,638 readings (excluding the final minute): V1 **+0.9%**, V2 **+1.3%**, 3-exchange price (V3/V4) **-0.4%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $397.41 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 987 | 859 (87%) | -$348.21 | -9% | 235,506 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.4%** over 36,245 readings from 1431 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 6255 | 2% | 4% | 5% |
| 10–20% | 2748 | 15% | 16% | 16% |
| 20–30% | 2994 | 25% | 26% | 26% |
| 30–40% | 3363 | 35% | 36% | 38% |
| 40–50% | 3613 | 45% | 48% | 52% |
| 50–60% | 3567 | 55% | 59% | 60% |
| 60–70% | 3165 | 65% | 70% | 73% |
| 70–80% | 2583 | 75% | 80% | 83% |
| 80–90% | 2324 | 85% | 88% | 87% |
| 90–100% | 5633 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 481 | 228 (47%) | 44¢ | 54% | $65.92 | +3% |
| 10–20¢ | 177 | 73 (41%) | 43¢ | 58% | -$66.43 | -8% |
| 20¢+ | 12 | 4 (33%) | 40¢ | 68% | -$9.56 | -19% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1203 | 574 (48%) | 45¢ | 54% | $78.55 | +1% |
| 5–10 min | 165 | 63 (38%) | 38¢ | 46% | -$18.33 | -3% |
| 2–5 min | 11 | 5 (45%) | 48¢ | 55% | -$3.52 | -7% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 180 | 33 (18%) | 18¢ | 27% | -$20.50 | -6% |
| Toss-up (25–75¢) | 1087 | 512 (47%) | 45¢ | 54% | $43.27 | +1% |
| Favorite (75–95¢) | 114 | 98 (86%) | 82¢ | 89% | $33.53 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 157 | 77 (49%) | 44¢ | 54% | $52.93 | +7% |
| XRP | 156 | 74 (47%) | 46¢ | 54% | $4.23 | +1% |
| ETH | 155 | 69 (45%) | 46¢ | 55% | -$54.05 | -7% |
| NEAR | 153 | 73 (48%) | 45¢ | 53% | $18.33 | +3% |
| SOL | 152 | 77 (51%) | 42¢ | 50% | $106.29 | +16% |
| ZEC | 152 | 65 (43%) | 42¢ | 50% | -$4.27 | -1% |
| DOGE | 152 | 66 (43%) | 44¢ | 53% | -$35.24 | -5% |
| HYPE | 152 | 65 (43%) | 44¢ | 52% | -$35.12 | -5% |
| BTC | 152 | 77 (51%) | 49¢ | 57% | $3.20 | +0% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 4:26:12 PM | ZEC | UP | 3.8 min | 9¢ | 19% | 10¢ | Open | — |
| 9/29 4:23:54 PM | DOGE | UP | 6.1 min | 13¢ | 24% | 10¢ | Open | — |
| 9/29 4:23:14 PM | NEAR | UP | 6.8 min | 17¢ | 28% | 10¢ | Open | — |
| 9/29 4:22:35 PM | SOL | UP | 7.4 min | 19¢ | 30% | 10¢ | Open | — |
| 9/29 4:19:46 PM | HYPE | DOWN | 10.2 min | 58¢ | 84% | 25¢ | Open | — |
| 9/29 4:16:35 PM | BTC | DOWN | 13.4 min | 80¢ | 89% | 8¢ | Open | — |
| 9/29 4:03:12 PM | BNB | DOWN | 11.8 min | 11¢ | 17% | 5¢ | ❌ Lost | -$1.17 |
| 9/29 4:01:34 PM | NEAR | DOWN | 13.4 min | 33¢ | 39% | 5¢ | ❌ Lost | -$3.46 |
| 9/29 4:01:34 PM | ZEC | DOWN | 13.4 min | 38¢ | 48% | 8¢ | ❌ Lost | -$3.96 |
| 9/29 4:01:16 PM | BTC | UP | 13.7 min | 68¢ | 76% | 6¢ | ✅ Won | $3.04 |
| 9/29 4:01:14 PM | HYPE | DOWN | 13.8 min | 37¢ | 44% | 5¢ | ❌ Lost | -$3.87 |
| 9/29 4:01:07 PM | DOGE | UP | 13.9 min | 77¢ | 86% | 7¢ | ✅ Won | $2.17 |
| 9/29 4:01:07 PM | XRP | UP | 13.9 min | 76¢ | 82% | 5¢ | ✅ Won | $2.27 |
| 9/29 4:01:07 PM | SOL | UP | 13.9 min | 65¢ | 80% | 13¢ | ✅ Won | $3.34 |
| 9/29 4:01:07 PM | ETH | UP | 13.9 min | 77¢ | 86% | 7¢ | ✅ Won | $2.17 |
| 9/29 3:49:25 PM | NEAR | DOWN | 10.6 min | 33¢ | 39% | 4¢ | ❌ Lost | -$3.46 |
| 9/29 3:47:07 PM | DOGE | DOWN | 12.9 min | 68¢ | 75% | 5¢ | ❌ Lost | -$6.98 |
| 9/29 3:46:53 PM | SOL | UP | 13.1 min | 26¢ | 31% | 4¢ | ✅ Won | $7.31 |
| 9/29 3:46:22 PM | XRP | UP | 13.6 min | 30¢ | 38% | 6¢ | ✅ Won | $6.85 |
| 9/29 3:46:18 PM | HYPE | DOWN | 13.7 min | 68¢ | 74% | 5¢ | ❌ Lost | -$6.96 |
| 9/29 3:46:04 PM | ETH | DOWN | 13.9 min | 78¢ | 86% | 7¢ | ✅ Won | $2.07 |
| 9/29 3:46:04 PM | BTC | DOWN | 13.9 min | 75¢ | 92% | 16¢ | ✅ Won | $2.36 |
| 9/29 3:46:04 PM | ZEC | DOWN | 13.9 min | 61¢ | 69% | 7¢ | ❌ Lost | -$6.27 |
| 9/29 3:46:04 PM | BNB | DOWN | 13.9 min | 69¢ | 77% | 7¢ | ❌ Lost | -$7.05 |
| 9/29 3:37:45 PM | SOL | DOWN | 7.2 min | 24¢ | 32% | 6¢ | ❌ Lost | -$2.53 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
