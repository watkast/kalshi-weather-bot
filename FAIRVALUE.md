# Fair-Value Bot

*Updated Tue Sep 29, 4:56 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1434 | $170.81 | +2% | $84.44 / $86.37 |
| 4¢+ | 1390 | $296.77 | +5% | $280.69 / $16.08 |
| 6¢+ | 1279 | $285.74 | +5% | $281.48 / $4.26 |
| 8¢+ ← live bot | 1110 | $377.44 | +9% | $362.82 / $14.62 |
| 10¢+ | 942 | $354.46 | +10% | $287.76 / $66.70 |
| 15¢+ | 571 | $344.88 | +18% | $253.26 / $91.62 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1403 | 1397 | 649 (46%) | 44¢ | 53% | $69.45 | +1% | +4.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 16 | 11 | 9 / 2 | $13.15 | $2.00 | -$11.15 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 995 | 423 (43%) | 320 / 675 | 8.6 | -$43.45 | -$351.46 | -8% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 852 | 288 (34%) | 380 / 472 | 7.3 | -$55.90 | -$316.94 | -10% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 214 | 69 (32%) | 60 / 154 | 2.0 | -$14.97 | -$146.55 | -18% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 227 | 96 (42%) | 74 / 153 | 2.0 | -$13.69 | -$25.81 | -3% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 127 | 53 (42%) | 45 / 82 | 1.5 | -$10.05 | -$44.93 | -9% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 27 | 11 (41%) | 11 / 16 | 1.6 | -$5.79 | $2.54 | +2% |

*Model accuracy vs Kalshi's prices on the same 24,070 readings (excluding the final minute): V1 **+0.8%**, V2 **+1.2%**, 3-exchange price (V3/V4) **-0.4%**.*

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
| 1003 | 875 (87%) | -$335.06 | -8% | 235,506 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.4%** over 36,713 readings from 1449 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 6341 | 3% | 4% | 5% |
| 10–20% | 2840 | 15% | 16% | 15% |
| 20–30% | 3091 | 25% | 26% | 27% |
| 30–40% | 3430 | 35% | 36% | 39% |
| 40–50% | 3668 | 45% | 48% | 52% |
| 50–60% | 3593 | 55% | 59% | 60% |
| 60–70% | 3174 | 65% | 70% | 73% |
| 70–80% | 2592 | 75% | 80% | 83% |
| 80–90% | 2331 | 85% | 88% | 87% |
| 90–100% | 5653 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 490 | 232 (47%) | 44¢ | 53% | $79.64 | +4% |
| 10–20¢ | 182 | 74 (41%) | 43¢ | 57% | -$67.59 | -8% |
| 20¢+ | 14 | 5 (36%) | 41¢ | 68% | -$8.97 | -15% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1207 | 577 (48%) | 46¢ | 54% | $88.69 | +2% |
| 5–10 min | 171 | 65 (38%) | 37¢ | 46% | -$12.70 | -2% |
| 2–5 min | 15 | 6 (40%) | 39¢ | 49% | -$0.46 | -1% |
| 1–2 min | 4 | 1 (25%) | 39¢ | 61% | -$6.08 | -38% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 189 | 35 (19%) | 18¢ | 27% | -$16.09 | -4% |
| Toss-up (25–75¢) | 1093 | 515 (47%) | 45¢ | 54% | $50.13 | +1% |
| Favorite (75–95¢) | 115 | 99 (86%) | 82¢ | 89% | $35.41 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 158 | 78 (49%) | 44¢ | 54% | $60.60 | +8% |
| XRP | 157 | 75 (48%) | 46¢ | 53% | $10.98 | +1% |
| ETH | 157 | 69 (44%) | 46¢ | 54% | -$58.26 | -8% |
| NEAR | 155 | 73 (47%) | 45¢ | 53% | $13.03 | +2% |
| SOL | 154 | 78 (51%) | 42¢ | 50% | $112.16 | +17% |
| ZEC | 154 | 65 (42%) | 41¢ | 50% | -$7.21 | -1% |
| DOGE | 154 | 67 (44%) | 44¢ | 53% | -$30.18 | -4% |
| HYPE | 154 | 66 (43%) | 44¢ | 53% | -$34.53 | -5% |
| BTC | 154 | 78 (51%) | 49¢ | 57% | $2.86 | +0% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 4:55:02 PM | BTC | DOWN | 5.0 min | 33¢ | 44% | 9¢ | Open | — |
| 9/29 4:54:30 PM | XRP | DOWN | 5.5 min | 29¢ | 42% | 11¢ | Open | — |
| 9/29 4:54:13 PM | ETH | DOWN | 5.8 min | 16¢ | 30% | 13¢ | Open | — |
| 9/29 4:52:09 PM | HYPE | DOWN | 7.8 min | 28¢ | 40% | 11¢ | Open | — |
| 9/29 4:48:05 PM | BNB | DOWN | 11.9 min | 33¢ | 47% | 12¢ | Open | — |
| 9/29 4:47:12 PM | NEAR | DOWN | 12.8 min | 44¢ | 55% | 10¢ | Open | — |
| 9/29 4:43:27 PM | ETH | DOWN | 1.5 min | 33¢ | 48% | 13¢ | ❌ Lost | -$3.46 |
| 9/29 4:43:21 PM | BTC | DOWN | 1.6 min | 21¢ | 32% | 10¢ | ❌ Lost | -$2.22 |
| 9/29 4:41:05 PM | ZEC | DOWN | 3.9 min | 19¢ | 35% | 14¢ | ❌ Lost | -$2.01 |
| 9/29 4:39:49 PM | SOL | UP | 5.2 min | 20¢ | 30% | 9¢ | ✅ Won | $7.88 |
| 9/29 4:39:23 PM | NEAR | DOWN | 5.6 min | 33¢ | 57% | 22¢ | ❌ Lost | -$3.46 |
| 9/29 4:39:13 PM | DOGE | UP | 5.8 min | 34¢ | 48% | 12¢ | ✅ Won | $6.44 |
| 9/29 4:34:54 PM | BNB | UP | 10.1 min | 22¢ | 32% | 9¢ | ✅ Won | $7.67 |
| 9/29 4:34:37 PM | HYPE | DOWN | 10.4 min | 33¢ | 43% | 9¢ | ❌ Lost | -$3.46 |
| 9/29 4:26:58 PM | XRP | DOWN | 3.0 min | 31¢ | 41% | 9¢ | ✅ Won | $6.75 |
| 9/29 4:26:55 PM | ETH | UP | 3.1 min | 7¢ | 27% | 19¢ | ❌ Lost | -$0.75 |
| 9/29 4:26:12 PM | ZEC | UP | 3.8 min | 9¢ | 19% | 10¢ | ❌ Lost | -$0.93 |
| 9/29 4:23:54 PM | DOGE | UP | 6.1 min | 13¢ | 24% | 10¢ | ❌ Lost | -$1.38 |
| 9/29 4:23:14 PM | NEAR | UP | 6.8 min | 17¢ | 28% | 10¢ | ❌ Lost | -$1.84 |
| 9/29 4:22:35 PM | SOL | UP | 7.4 min | 19¢ | 30% | 10¢ | ❌ Lost | -$2.01 |
| 9/29 4:19:46 PM | HYPE | DOWN | 10.2 min | 58¢ | 84% | 25¢ | ✅ Won | $4.05 |
| 9/29 4:16:35 PM | BTC | DOWN | 13.4 min | 80¢ | 89% | 8¢ | ✅ Won | $1.88 |
| 9/29 4:03:12 PM | BNB | DOWN | 11.8 min | 11¢ | 17% | 5¢ | ❌ Lost | -$1.17 |
| 9/29 4:01:34 PM | NEAR | DOWN | 13.4 min | 33¢ | 39% | 5¢ | ❌ Lost | -$3.46 |
| 9/29 4:01:34 PM | ZEC | DOWN | 13.4 min | 38¢ | 48% | 8¢ | ❌ Lost | -$3.96 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
