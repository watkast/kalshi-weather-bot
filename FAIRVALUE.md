# Fair-Value Bot

*Updated Mon Sep 28, 11:53 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 905 | $58.47 | +1% | $151.48 / -$93.01 |
| 4¢+ ← live bot | 874 | $283.38 | +7% | $213.77 / $69.61 |
| 6¢+ | 803 | $337.17 | +10% | $225.68 / $111.49 |
| 8¢+ | 698 | $355.20 | +13% | $170.67 / $184.53 |
| 10¢+ | 601 | $289.12 | +12% | $196.33 / $92.79 |
| 15¢+ | 356 | $243.27 | +20% | $176.09 / $67.18 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 888 | 879 | 440 (50%) | 45¢ | 53% | $291.97 | +7% | +6.9¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 477 | 214 (45%) | 139 / 338 | 8.4 | -$37.76 | -$128.94 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 422 | 137 (32%) | 186 / 236 | 7.4 | -$55.90 | -$244.72 | -15% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 101 | 35 (35%) | 35 / 66 | 1.9 | -$14.97 | -$52.90 | -13% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 73% of orders | 109 | 45 (41%) | 39 / 70 | 2.0 | -$13.69 | -$25.90 | -5% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 44 | 21 (48%) | 15 / 29 | 1.5 | -$10.05 | -$7.47 | -4% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 14 | 8 (57%) | 5 / 9 | 1.6 | -$10.39 | $6.02 | +4% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 3 | 0 (0%) | 1 / 2 | 1.5 | -$5.79 | -$9.04 | -100% |

*Model accuracy vs Kalshi's prices on the same 11,744 readings (excluding the final minute): V1 **+2.3%**, V2 **+2.3%**, 3-exchange price (V3/V4) **+0.8%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $506.02 | $525.36 | $394.02 | 2 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 485 | 357 (74%) | -$112.54 | -7% | 118,659 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.1%** over 23,436 readings from 918 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4457 | 2% | 4% | 6% |
| 10–20% | 1915 | 15% | 16% | 17% |
| 20–30% | 2046 | 25% | 26% | 26% |
| 30–40% | 2236 | 35% | 36% | 39% |
| 40–50% | 2300 | 45% | 47% | 52% |
| 50–60% | 2287 | 55% | 59% | 59% |
| 60–70% | 1972 | 65% | 70% | 69% |
| 70–80% | 1641 | 75% | 80% | 80% |
| 80–90% | 1414 | 85% | 88% | 83% |
| 90–100% | 3168 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 488 | 251 (51%) | 46¢ | 52% | $194.36 | +8% |
| 6–10¢ | 292 | 147 (50%) | 45¢ | 54% | $112.23 | +8% |
| 10–20¢ | 92 | 40 (43%) | 43¢ | 57% | -$7.23 | -2% |
| 20¢+ | 7 | 2 (29%) | 38¢ | 66% | -$7.39 | -27% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 810 | 409 (50%) | 46¢ | 54% | $268.77 | +7% |
| 5–10 min | 62 | 27 (44%) | 38¢ | 47% | $25.16 | +10% |
| 2–5 min | 5 | 3 (60%) | 62¢ | 70% | -$1.56 | -5% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 100 | 20 (20%) | 19¢ | 27% | -$0.13 | -0% |
| Toss-up (25–75¢) | 720 | 370 (51%) | 46¢ | 54% | $275.34 | +8% |
| Favorite (75–95¢) | 59 | 50 (85%) | 81¢ | 88% | $16.76 | +3% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 100 | 54 (54%) | 43¢ | 53% | $95.83 | +22% |
| XRP | 99 | 52 (53%) | 47¢ | 55% | $39.82 | +8% |
| ETH | 99 | 44 (44%) | 47¢ | 55% | -$39.01 | -8% |
| HYPE | 98 | 44 (45%) | 44¢ | 53% | -$5.88 | -1% |
| SOL | 97 | 51 (53%) | 44¢ | 52% | $70.98 | +16% |
| NEAR | 97 | 50 (52%) | 47¢ | 55% | $28.93 | +6% |
| BTC | 97 | 53 (55%) | 50¢ | 58% | $28.74 | +6% |
| ZEC | 96 | 42 (44%) | 41¢ | 50% | $15.32 | +4% |
| DOGE | 96 | 50 (52%) | 45¢ | 53% | $57.24 | +13% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 11:50:07 PM | NEAR | DOWN | 9.9 min | 32¢ | 49% | 16¢ | Open | — |
| 9/28 11:49:00 PM | BTC | UP | 11.0 min | 38¢ | 45% | 5¢ | Open | — |
| 9/28 11:48:40 PM | BNB | DOWN | 11.3 min | 44¢ | 58% | 12¢ | Open | — |
| 9/28 11:48:21 PM | ETH | DOWN | 11.6 min | 58¢ | 65% | 5¢ | Open | — |
| 9/28 11:47:53 PM | ZEC | UP | 12.1 min | 28¢ | 34% | 5¢ | Open | — |
| 9/28 11:47:25 PM | HYPE | UP | 12.6 min | 21¢ | 27% | 5¢ | Open | — |
| 9/28 11:47:03 PM | SOL | UP | 12.9 min | 31¢ | 38% | 5¢ | Open | — |
| 9/28 11:46:21 PM | XRP | UP | 13.7 min | 26¢ | 34% | 7¢ | Open | — |
| 9/28 11:46:21 PM | DOGE | UP | 13.7 min | 31¢ | 39% | 6¢ | Open | — |
| 9/28 11:40:29 PM | BNB | DOWN | 4.5 min | 86¢ | 99% | 12¢ | ✅ Won | $1.31 |
| 9/28 11:32:47 PM | NEAR | UP | 12.2 min | 14¢ | 20% | 5¢ | ❌ Lost | -$1.49 |
| 9/28 11:32:11 PM | XRP | DOWN | 12.8 min | 85¢ | 91% | 5¢ | ✅ Won | $1.41 |
| 9/28 11:32:11 PM | DOGE | DOWN | 12.8 min | 83¢ | 88% | 4¢ | ✅ Won | $1.60 |
| 9/28 11:32:04 PM | HYPE | UP | 12.9 min | 24¢ | 32% | 6¢ | ❌ Lost | -$2.53 |
| 9/28 11:32:04 PM | ZEC | UP | 12.9 min | 18¢ | 27% | 8¢ | ❌ Lost | -$1.91 |
| 9/28 11:31:14 PM | ETH | DOWN | 13.8 min | 78¢ | 84% | 5¢ | ✅ Won | $2.07 |
| 9/28 11:31:14 PM | SOL | DOWN | 13.8 min | 81¢ | 88% | 6¢ | ✅ Won | $1.79 |
| 9/28 11:31:14 PM | BTC | DOWN | 13.8 min | 73¢ | 80% | 6¢ | ✅ Won | $2.56 |
| 9/28 11:19:46 PM | XRP | UP | 10.2 min | 81¢ | 87% | 5¢ | ✅ Won | $1.80 |
| 9/28 11:18:13 PM | NEAR | DOWN | 11.8 min | 36¢ | 48% | 11¢ | ❌ Lost | -$3.77 |
| 9/28 11:17:55 PM | HYPE | DOWN | 12.1 min | 42¢ | 56% | 12¢ | ❌ Lost | -$4.38 |
| 9/28 11:17:40 PM | ZEC | DOWN | 12.3 min | 46¢ | 58% | 10¢ | ❌ Lost | -$4.78 |
| 9/28 11:17:24 PM | SOL | UP | 12.6 min | 29¢ | 44% | 13¢ | ✅ Won | $6.95 |
| 9/28 11:17:03 PM | BTC | UP | 12.9 min | 49¢ | 60% | 9¢ | ✅ Won | $4.92 |
| 9/28 11:16:52 PM | ETH | DOWN | 13.1 min | 35¢ | 42% | 6¢ | ❌ Lost | -$3.66 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
