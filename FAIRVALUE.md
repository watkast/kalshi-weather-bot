# Fair-Value Bot

*Updated Tue Sep 29, 5:26 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1452 | $153.92 | +2% | $108.71 / $45.21 |
| 4¢+ | 1407 | $290.94 | +4% | $288.48 / $2.46 |
| 6¢+ | 1295 | $281.82 | +5% | $289.93 / -$8.11 |
| 8¢+ ← live bot | 1124 | $375.27 | +8% | $363.72 / $11.55 |
| 10¢+ | 954 | $354.84 | +10% | $294.38 / $60.46 |
| 15¢+ | 579 | $337.11 | +17% | $247.49 / $89.62 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1416 | 1410 | 652 (46%) | 44¢ | 53% | $48.36 | +1% | +4.2¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 29 | 17 | 10 / 7 | -$7.94 | -$2.04 | $5.90 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1008 | 426 (42%) | 321 / 687 | 8.5 | -$43.45 | -$372.55 | -8% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 863 | 291 (34%) | 382 / 481 | 7.3 | -$55.90 | -$320.17 | -10% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 218 | 70 (32%) | 60 / 158 | 2.0 | -$14.97 | -$145.88 | -17% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 231 | 96 (42%) | 74 / 157 | 2.0 | -$13.69 | -$44.91 | -4% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 131 | 55 (42%) | 46 / 85 | 1.5 | -$10.05 | -$43.58 | -8% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 29 | 11 (38%) | 12 / 17 | 1.6 | -$5.89 | -$3.35 | -3% |

*Model accuracy vs Kalshi's prices on the same 24,520 readings (excluding the final minute): V1 **+0.7%**, V2 **+1.1%**, 3-exchange price (V3/V4) **-0.6%**.*

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
| 1016 | 888 (87%) | -$356.15 | -9% | 237,111 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.3%** over 37,199 readings from 1467 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 6352 | 2% | 4% | 5% |
| 10–20% | 2845 | 15% | 16% | 15% |
| 20–30% | 3107 | 25% | 26% | 27% |
| 30–40% | 3465 | 35% | 36% | 39% |
| 40–50% | 3731 | 45% | 48% | 52% |
| 50–60% | 3641 | 55% | 59% | 60% |
| 60–70% | 3225 | 65% | 70% | 73% |
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
| 6–10¢ | 497 | 232 (47%) | 44¢ | 53% | $47.93 | +2% |
| 10–20¢ | 188 | 77 (41%) | 42¢ | 57% | -$56.97 | -7% |
| 20¢+ | 14 | 5 (36%) | 41¢ | 68% | -$8.97 | -15% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1215 | 578 (48%) | 46¢ | 54% | $59.93 | +1% |
| 5–10 min | 174 | 67 (39%) | 37¢ | 46% | -$0.40 | -0% |
| 2–5 min | 17 | 6 (35%) | 37¢ | 47% | -$5.09 | -8% |
| 1–2 min | 4 | 1 (25%) | 39¢ | 61% | -$6.08 | -38% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 191 | 35 (18%) | 18¢ | 27% | -$18.96 | -5% |
| Toss-up (25–75¢) | 1104 | 518 (47%) | 45¢ | 54% | $31.91 | +1% |
| Favorite (75–95¢) | 115 | 99 (86%) | 82¢ | 89% | $35.41 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 160 | 78 (49%) | 44¢ | 54% | $51.08 | +7% |
| XRP | 159 | 76 (48%) | 45¢ | 53% | $14.54 | +2% |
| ETH | 159 | 69 (43%) | 46¢ | 54% | -$64.23 | -9% |
| NEAR | 157 | 73 (46%) | 45¢ | 53% | $3.58 | +0% |
| HYPE | 156 | 67 (43%) | 44¢ | 53% | -$32.56 | -5% |
| BTC | 156 | 79 (51%) | 49¢ | 57% | $2.35 | +0% |
| ZEC | 155 | 65 (42%) | 41¢ | 50% | -$8.38 | -1% |
| SOL | 154 | 78 (51%) | 42¢ | 50% | $112.16 | +17% |
| DOGE | 154 | 67 (44%) | 44¢ | 53% | -$30.18 | -4% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 5:20:09 PM | DOGE | UP | 9.8 min | 15¢ | 27% | 11¢ | Open | — |
| 9/29 5:19:54 PM | XRP | UP | 10.1 min | 25¢ | 38% | 11¢ | Open | — |
| 9/29 5:19:22 PM | SOL | UP | 10.6 min | 32¢ | 42% | 8¢ | Open | — |
| 9/29 5:16:46 PM | ZEC | DOWN | 13.2 min | 51¢ | 62% | 9¢ | Open | — |
| 9/29 5:16:36 PM | BNB | DOWN | 13.4 min | 50¢ | 63% | 11¢ | Open | — |
| 9/29 5:16:13 PM | NEAR | DOWN | 13.8 min | 45¢ | 57% | 10¢ | Open | — |
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
| 9/29 4:43:27 PM | ETH | DOWN | 1.5 min | 33¢ | 48% | 13¢ | ❌ Lost | -$3.46 |
| 9/29 4:43:21 PM | BTC | DOWN | 1.6 min | 21¢ | 32% | 10¢ | ❌ Lost | -$2.22 |
| 9/29 4:41:05 PM | ZEC | DOWN | 3.9 min | 19¢ | 35% | 14¢ | ❌ Lost | -$2.01 |
| 9/29 4:39:49 PM | SOL | UP | 5.2 min | 20¢ | 30% | 9¢ | ✅ Won | $7.88 |
| 9/29 4:39:23 PM | NEAR | DOWN | 5.6 min | 33¢ | 57% | 22¢ | ❌ Lost | -$3.46 |
| 9/29 4:39:13 PM | DOGE | UP | 5.8 min | 34¢ | 48% | 12¢ | ✅ Won | $6.44 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
