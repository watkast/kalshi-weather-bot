# Fair-Value Bot

*Updated Tue Sep 29, 6:47 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **10¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **10¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1506 | $170.32 | +2% | $148.92 / $21.40 |
| 4¢+ | 1459 | $296.39 | +4% | $331.68 / -$35.29 |
| 6¢+ | 1343 | $268.15 | +5% | $350.29 / -$82.14 |
| 8¢+ ← live bot | 1169 | $359.52 | +8% | $353.32 / $6.20 |
| 10¢+ | 992 | $363.71 | +10% | $267.72 / $95.99 |
| 15¢+ | 602 | $354.69 | +17% | $252.85 / $101.84 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1451 | 1449 | 673 (46%) | 44¢ | 53% | $88.83 | +1% | +4.2¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 68 | 44 | 30 / 14 | $32.53 | $4.05 | -$28.48 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1047 | 447 (43%) | 327 / 720 | 8.4 | -$43.45 | -$332.08 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 907 | 304 (34%) | 395 / 512 | 7.3 | -$55.90 | -$358.37 | -11% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 230 | 76 (33%) | 63 / 167 | 2.0 | -$14.97 | -$129.52 | -15% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 243 | 101 (42%) | 76 / 167 | 2.0 | -$13.69 | -$40.25 | -4% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 140 | 59 (42%) | 50 / 90 | 1.5 | -$10.05 | -$41.82 | -7% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 30 | 12 (40%) | 12 / 18 | 1.6 | -$5.89 | $3.81 | +3% |

*Model accuracy vs Kalshi's prices on the same 25,860 readings (excluding the final minute): V1 **+0.3%**, V2 **+0.9%**, 3-exchange price (V3/V4) **-0.9%**.*

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
| 1055 | 927 (88%) | -$315.68 | -7% | 240,976 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.1%** over 38,647 readings from 1521 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 6766 | 3% | 4% | 5% |
| 10–20% | 2962 | 15% | 16% | 15% |
| 20–30% | 3206 | 25% | 26% | 27% |
| 30–40% | 3580 | 35% | 36% | 39% |
| 40–50% | 3837 | 45% | 48% | 52% |
| 50–60% | 3753 | 55% | 59% | 60% |
| 60–70% | 3354 | 65% | 70% | 72% |
| 70–80% | 2779 | 75% | 80% | 83% |
| 80–90% | 2453 | 85% | 88% | 87% |
| 90–100% | 5957 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 514 | 241 (47%) | 44¢ | 53% | $58.40 | +2% |
| 10–20¢ | 209 | 89 (43%) | 42¢ | 56% | -$23.72 | -3% |
| 20¢+ | 15 | 5 (33%) | 40¢ | 68% | -$12.22 | -20% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1238 | 589 (48%) | 45¢ | 54% | $72.16 | +1% |
| 5–10 min | 186 | 74 (40%) | 38¢ | 47% | $11.72 | +2% |
| 2–5 min | 21 | 9 (43%) | 36¢ | 47% | $11.03 | +14% |
| 1–2 min | 4 | 1 (25%) | 39¢ | 61% | -$6.08 | -38% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 201 | 38 (19%) | 18¢ | 27% | -$10.43 | -3% |
| Toss-up (25–75¢) | 1130 | 533 (47%) | 45¢ | 54% | $58.58 | +1% |
| Favorite (75–95¢) | 118 | 102 (86%) | 82¢ | 89% | $40.68 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| XRP | 165 | 79 (48%) | 45¢ | 53% | $16.36 | +2% |
| BNB | 165 | 81 (49%) | 44¢ | 54% | $63.20 | +8% |
| ETH | 164 | 72 (44%) | 46¢ | 55% | -$60.52 | -8% |
| BTC | 161 | 81 (50%) | 49¢ | 58% | -$8.95 | -1% |
| ZEC | 160 | 69 (43%) | 41¢ | 50% | $6.30 | +1% |
| SOL | 159 | 81 (51%) | 42¢ | 50% | $126.00 | +18% |
| NEAR | 159 | 74 (47%) | 45¢ | 53% | $6.99 | +1% |
| HYPE | 159 | 68 (43%) | 43¢ | 52% | -$33.41 | -5% |
| DOGE | 157 | 68 (43%) | 44¢ | 52% | -$27.14 | -4% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 6:46:55 PM | BNB | DOWN | 13.1 min | 54¢ | 70% | 14¢ | Open | — |
| 9/29 6:46:06 PM | ETH | DOWN | 13.9 min | 66¢ | 79% | 11¢ | Open | — |
| 9/29 6:40:59 PM | XRP | DOWN | 4.0 min | 45¢ | 55% | 8¢ | ✅ Won | $5.32 |
| 9/29 6:39:07 PM | ZEC | DOWN | 5.9 min | 46¢ | 63% | 15¢ | ✅ Won | $5.22 |
| 9/29 6:38:07 PM | BTC | DOWN | 6.9 min | 81¢ | 91% | 9¢ | ✅ Won | $1.79 |
| 9/29 6:36:54 PM | SOL | DOWN | 8.1 min | 60¢ | 73% | 11¢ | ✅ Won | $3.83 |
| 9/29 6:34:02 PM | DOGE | DOWN | 10.9 min | 27¢ | 39% | 11¢ | ✅ Won | $7.16 |
| 9/29 6:31:52 PM | BNB | DOWN | 13.1 min | 35¢ | 51% | 14¢ | ❌ Lost | -$3.68 |
| 9/29 6:31:36 PM | ETH | DOWN | 13.4 min | 64¢ | 79% | 13¢ | ✅ Won | $3.43 |
| 9/29 6:27:09 PM | SOL | UP | 2.8 min | 16¢ | 36% | 19¢ | ✅ Won | $8.30 |
| 9/29 6:24:39 PM | HYPE | DOWN | 5.3 min | 52¢ | 65% | 11¢ | ❌ Lost | -$5.38 |
| 9/29 6:21:23 PM | BNB | UP | 8.6 min | 23¢ | 34% | 9¢ | ✅ Won | $7.57 |
| 9/29 6:18:06 PM | BTC | DOWN | 11.9 min | 72¢ | 82% | 9¢ | ❌ Lost | -$7.35 |
| 9/29 6:17:50 PM | ETH | DOWN | 12.2 min | 55¢ | 66% | 9¢ | ❌ Lost | -$5.68 |
| 9/29 6:17:15 PM | ZEC | DOWN | 12.8 min | 36¢ | 46% | 9¢ | ❌ Lost | -$3.77 |
| 9/29 6:16:28 PM | XRP | DOWN | 13.5 min | 41¢ | 54% | 11¢ | ❌ Lost | -$4.27 |
| 9/29 6:10:48 PM | ZEC | DOWN | 4.2 min | 51¢ | 63% | 10¢ | ✅ Won | $4.72 |
| 9/29 6:04:47 PM | XRP | DOWN | 10.2 min | 51¢ | 62% | 9¢ | ✅ Won | $4.72 |
| 9/29 6:03:26 PM | SOL | DOWN | 11.6 min | 24¢ | 35% | 10¢ | ✅ Won | $7.47 |
| 9/29 6:03:26 PM | HYPE | DOWN | 11.6 min | 36¢ | 48% | 11¢ | ✅ Won | $6.23 |
| 9/29 6:03:26 PM | ETH | DOWN | 11.6 min | 35¢ | 47% | 10¢ | ✅ Won | $6.34 |
| 9/29 6:03:13 PM | BTC | UP | 11.8 min | 66¢ | 78% | 11¢ | ❌ Lost | -$6.76 |
| 9/29 6:01:04 PM | BNB | DOWN | 13.9 min | 32¢ | 48% | 14¢ | ✅ Won | $6.66 |
| 9/29 5:57:01 PM | BTC | DOWN | 3.0 min | 21¢ | 32% | 10¢ | ❌ Lost | -$2.22 |
| 9/29 5:51:21 PM | HYPE | DOWN | 8.7 min | 16¢ | 26% | 9¢ | ❌ Lost | -$1.70 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
