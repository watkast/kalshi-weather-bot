# Fair-Value Bot

*Updated Tue Sep 29, 7:38 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1533 | $165.69 | +2% | $114.56 / $51.13 |
| 4¢+ | 1486 | $273.82 | +4% | $308.01 / -$34.19 |
| 6¢+ | 1369 | $230.43 | +4% | $305.91 / -$75.48 |
| 8¢+ ← live bot | 1192 | $340.00 | +7% | $359.68 / -$19.68 |
| 10¢+ | 1012 | $339.63 | +9% | $285.00 / $54.63 |
| 15¢+ | 616 | $358.20 | +17% | $254.66 / $103.54 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1476 | 1471 | 679 (46%) | 44¢ | 53% | $60.85 | +1% | +4.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 90 | 61 | 35 / 26 | $4.55 | -$13.85 | -$18.40 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1069 | 453 (42%) | 330 / 739 | 8.4 | -$43.45 | -$360.06 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 931 | 314 (34%) | 405 / 526 | 7.3 | -$55.90 | -$326.08 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 236 | 79 (33%) | 65 / 171 | 2.0 | -$14.97 | -$117.81 | -13% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 249 | 104 (42%) | 77 / 172 | 2.0 | -$13.69 | -$41.22 | -4% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 143 | 61 (43%) | 51 / 92 | 1.5 | -$10.05 | -$35.23 | -6% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 1 | 1 (100%) | 0 / 1 | 1.0 | $1.67 | $1.67 | +20% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 31 | 12 (39%) | 12 / 19 | 1.6 | -$5.89 | -$1.37 | -1% |

*Model accuracy vs Kalshi's prices on the same 26,531 readings (excluding the final minute): V1 **+0.2%**, V2 **+1.0%**, 3-exchange price (V3/V4) **-1.0%**.*

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
| 1077 | 949 (88%) | -$343.66 | -8% | 240,827 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+3.9%** over 39,372 readings from 1548 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 6837 | 3% | 4% | 5% |
| 10–20% | 3013 | 15% | 16% | 16% |
| 20–30% | 3280 | 25% | 26% | 27% |
| 30–40% | 3655 | 35% | 36% | 39% |
| 40–50% | 3912 | 45% | 48% | 52% |
| 50–60% | 3852 | 55% | 59% | 60% |
| 60–70% | 3413 | 65% | 70% | 73% |
| 70–80% | 2832 | 75% | 80% | 83% |
| 80–90% | 2504 | 85% | 88% | 87% |
| 90–100% | 6074 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 523 | 243 (46%) | 44¢ | 53% | $42.88 | +2% |
| 10–20¢ | 222 | 93 (42%) | 42¢ | 56% | -$36.18 | -4% |
| 20¢+ | 15 | 5 (33%) | 40¢ | 68% | -$12.22 | -20% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1247 | 591 (47%) | 45¢ | 54% | $49.96 | +1% |
| 5–10 min | 194 | 76 (39%) | 38¢ | 47% | $1.84 | +0% |
| 2–5 min | 26 | 11 (42%) | 35¢ | 46% | $15.13 | +16% |
| 1–2 min | 4 | 1 (25%) | 39¢ | 61% | -$6.08 | -38% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 205 | 38 (19%) | 18¢ | 27% | -$17.31 | -4% |
| Toss-up (25–75¢) | 1148 | 539 (47%) | 45¢ | 54% | $37.48 | +1% |
| Favorite (75–95¢) | 118 | 102 (86%) | 82¢ | 89% | $40.68 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 168 | 82 (49%) | 44¢ | 54% | $58.78 | +8% |
| XRP | 167 | 79 (47%) | 45¢ | 53% | $7.81 | +1% |
| ETH | 167 | 72 (43%) | 46¢ | 55% | -$74.12 | -9% |
| ZEC | 163 | 70 (43%) | 41¢ | 50% | $6.17 | +1% |
| HYPE | 162 | 69 (43%) | 43¢ | 52% | -$35.29 | -5% |
| BTC | 162 | 82 (51%) | 49¢ | 58% | -$5.52 | -1% |
| SOL | 161 | 82 (51%) | 41¢ | 50% | $129.49 | +19% |
| NEAR | 161 | 74 (46%) | 44¢ | 52% | -$0.52 | -0% |
| DOGE | 160 | 69 (43%) | 43¢ | 52% | -$25.95 | -4% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 7:32:29 PM | XRP | DOWN | 12.5 min | 72¢ | 83% | 10¢ | Open | — |
| 9/29 7:31:41 PM | ETH | DOWN | 13.3 min | 68¢ | 85% | 15¢ | Open | — |
| 9/29 7:31:27 PM | BNB | DOWN | 13.5 min | 55¢ | 68% | 11¢ | Open | — |
| 9/29 7:31:12 PM | BTC | DOWN | 13.8 min | 62¢ | 75% | 11¢ | Open | — |
| 9/29 7:31:12 PM | ZEC | DOWN | 13.8 min | 44¢ | 57% | 11¢ | Open | — |
| 9/29 7:27:24 PM | ETH | DOWN | 2.6 min | 7¢ | 18% | 11¢ | ❌ Lost | -$0.77 |
| 9/29 7:25:10 PM | ZEC | DOWN | 4.8 min | 46¢ | 60% | 12¢ | ✅ Won | $5.22 |
| 9/29 7:21:25 PM | DOGE | DOWN | 8.6 min | 27¢ | 39% | 10¢ | ❌ Lost | -$2.85 |
| 9/29 7:21:24 PM | XRP | DOWN | 8.6 min | 39¢ | 49% | 8¢ | ❌ Lost | -$4.07 |
| 9/29 7:21:24 PM | NEAR | DOWN | 8.6 min | 50¢ | 60% | 8¢ | ❌ Lost | -$5.18 |
| 9/29 7:19:18 PM | HYPE | DOWN | 10.7 min | 43¢ | 55% | 10¢ | ✅ Won | $5.52 |
| 9/29 7:16:28 PM | BNB | DOWN | 13.5 min | 33¢ | 45% | 10¢ | ✅ Won | $6.54 |
| 9/29 7:07:26 PM | BTC | DOWN | 7.5 min | 64¢ | 76% | 10¢ | ✅ Won | $3.43 |
| 9/29 7:07:19 PM | SOL | DOWN | 7.7 min | 37¢ | 52% | 13¢ | ❌ Lost | -$3.87 |
| 9/29 7:05:21 PM | DOGE | DOWN | 9.6 min | 23¢ | 39% | 15¢ | ❌ Lost | -$2.40 |
| 9/29 7:04:58 PM | NEAR | DOWN | 10.0 min | 22¢ | 32% | 8¢ | ❌ Lost | -$2.33 |
| 9/29 7:04:33 PM | ZEC | DOWN | 10.4 min | 38¢ | 48% | 8¢ | ❌ Lost | -$3.97 |
| 9/29 7:02:24 PM | HYPE | DOWN | 12.6 min | 40¢ | 52% | 11¢ | ❌ Lost | -$4.17 |
| 9/29 7:01:26 PM | ETH | DOWN | 13.6 min | 59¢ | 70% | 10¢ | ❌ Lost | -$6.07 |
| 9/29 7:01:12 PM | BNB | DOWN | 13.8 min | 52¢ | 64% | 10¢ | ❌ Lost | -$5.38 |
| 9/29 6:57:42 PM | HYPE | DOWN | 2.3 min | 31¢ | 49% | 16¢ | ❌ Lost | -$3.23 |
| 9/29 6:57:10 PM | XRP | DOWN | 2.8 min | 43¢ | 53% | 8¢ | ❌ Lost | -$4.48 |
| 9/29 6:55:27 PM | SOL | UP | 4.5 min | 25¢ | 38% | 11¢ | ✅ Won | $7.36 |
| 9/29 6:54:28 PM | ZEC | UP | 5.5 min | 13¢ | 23% | 9¢ | ❌ Lost | -$1.38 |
| 9/29 6:52:15 PM | DOGE | UP | 7.8 min | 34¢ | 44% | 8¢ | ✅ Won | $6.44 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
