# Fair-Value Bot

*Updated Mon Sep 28, 9:11 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **6¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **6¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 806 | $183.45 | +5% | $241.10 / -$57.65 |
| 4¢+ ← live bot | 777 | $378.39 | +11% | $271.09 / $107.30 |
| 6¢+ | 721 | $385.13 | +13% | $259.30 / $125.83 |
| 8¢+ | 637 | $362.20 | +15% | $158.55 / $203.65 |
| 10¢+ | 549 | $293.54 | +14% | $176.29 / $117.25 |
| 15¢+ | 334 | $241.56 | +22% | $130.15 / $111.41 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 792 | 783 | 400 (51%) | 44¢ | 53% | $392.07 | +11% | +7.5¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 381 | 174 (46%) | 111 / 270 | 8.3 | -$37.76 | -$28.84 | -2% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 342 | 120 (35%) | 140 / 202 | 7.4 | -$55.90 | -$153.39 | -11% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 82 | 30 (37%) | 32 / 50 | 2.0 | -$14.97 | -$5.08 | -2% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 89 | 35 (39%) | 29 / 60 | 2.0 | -$13.69 | -$41.09 | -11% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 31 | 14 (45%) | 10 / 21 | 1.5 | -$10.05 | -$10.59 | -8% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 1 | 1 (100%) | 0 / 1 | 1.0 | $12.82 | $12.82 | +130% |

*Model accuracy vs Kalshi's prices on the same 9,448 readings (excluding the final minute): V1 **+3.0%**, V2 **+3.4%**, 3-exchange price (V3/V4) **+1.4%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $512.82 | $512.82 | $384.62 | 0 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 389 | 261 (67%) | -$12.44 | -1% | 6,577 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.4%** over 20,981 readings from 819 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3968 | 2% | 4% | 6% |
| 10–20% | 1692 | 15% | 16% | 16% |
| 20–30% | 1888 | 25% | 26% | 26% |
| 30–40% | 2022 | 35% | 36% | 39% |
| 40–50% | 2076 | 45% | 47% | 52% |
| 50–60% | 2062 | 55% | 59% | 59% |
| 60–70% | 1769 | 65% | 71% | 68% |
| 70–80% | 1494 | 75% | 80% | 79% |
| 80–90% | 1281 | 85% | 88% | 81% |
| 90–100% | 2729 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 440 | 231 (52%) | 45¢ | 52% | $253.78 | +12% |
| 6–10¢ | 258 | 133 (52%) | 44¢ | 53% | $146.31 | +12% |
| 10–20¢ | 79 | 34 (43%) | 42¢ | 56% | -$6.11 | -2% |
| 20¢+ | 6 | 2 (33%) | 35¢ | 65% | -$1.91 | -9% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 734 | 381 (52%) | 45¢ | 53% | $379.23 | +11% |
| 5–10 min | 45 | 16 (36%) | 32¢ | 40% | $10.90 | +7% |
| 2–5 min | 2 | 2 (100%) | 88¢ | 94% | $2.34 | +13% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 88 | 20 (23%) | 19¢ | 27% | $25.81 | +15% |
| Toss-up (25–75¢) | 650 | 343 (53%) | 46¢ | 54% | $361.02 | +12% |
| Favorite (75–95¢) | 45 | 37 (82%) | 80¢ | 87% | $5.24 | +1% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 89 | 49 (55%) | 42¢ | 52% | $102.07 | +26% |
| XRP | 88 | 49 (56%) | 47¢ | 54% | $64.92 | +15% |
| ETH | 88 | 39 (44%) | 46¢ | 54% | -$25.69 | -6% |
| NEAR | 87 | 47 (54%) | 48¢ | 55% | $42.47 | +10% |
| HYPE | 87 | 40 (46%) | 42¢ | 50% | $22.26 | +6% |
| BTC | 87 | 45 (52%) | 49¢ | 57% | $11.14 | +3% |
| SOL | 86 | 47 (55%) | 44¢ | 51% | $81.60 | +21% |
| DOGE | 86 | 44 (51%) | 44¢ | 52% | $49.65 | +13% |
| ZEC | 85 | 40 (47%) | 40¢ | 49% | $43.65 | +12% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 9:08:47 PM | NEAR | DOWN | 6.2 min | 91¢ | 97% | 5¢ | Open | — |
| 9/28 9:08:17 PM | XRP | DOWN | 6.7 min | 28¢ | 41% | 11¢ | Open | — |
| 9/28 9:07:21 PM | DOGE | DOWN | 7.7 min | 43¢ | 52% | 7¢ | Open | — |
| 9/28 9:03:43 PM | ZEC | UP | 11.3 min | 45¢ | 51% | 4¢ | Open | — |
| 9/28 9:03:12 PM | BTC | DOWN | 11.8 min | 34¢ | 41% | 6¢ | Open | — |
| 9/28 9:01:52 PM | HYPE | DOWN | 13.1 min | 46¢ | 58% | 10¢ | Open | — |
| 9/28 9:01:52 PM | SOL | DOWN | 13.1 min | 33¢ | 41% | 7¢ | Open | — |
| 9/28 9:01:25 PM | ETH | DOWN | 13.6 min | 27¢ | 33% | 4¢ | Open | — |
| 9/28 9:01:16 PM | BNB | DOWN | 13.7 min | 24¢ | 35% | 9¢ | Open | — |
| 9/28 8:46:12 PM | BNB | DOWN | 13.8 min | 31¢ | 42% | 10¢ | ❌ Lost | -$3.25 |
| 9/28 8:43:22 PM | NEAR | DOWN | 1.6 min | 88¢ | 94% | 5¢ | ✅ Won | $1.11 |
| 9/28 8:38:23 PM | SOL | DOWN | 6.6 min | 38¢ | 51% | 11¢ | ❌ Lost | -$3.97 |
| 9/28 8:36:21 PM | DOGE | UP | 8.7 min | 30¢ | 36% | 5¢ | ✅ Won | $6.85 |
| 9/28 8:35:49 PM | BTC | UP | 9.2 min | 41¢ | 51% | 8¢ | ✅ Won | $5.73 |
| 9/28 8:35:49 PM | HYPE | UP | 9.2 min | 22¢ | 30% | 7¢ | ✅ Won | $7.70 |
| 9/28 8:34:06 PM | BNB | UP | 10.9 min | 31¢ | 43% | 10¢ | ✅ Won | $6.75 |
| 9/28 8:31:49 PM | ETH | DOWN | 13.2 min | 38¢ | 45% | 5¢ | ❌ Lost | -$3.97 |
| 9/28 8:31:49 PM | XRP | DOWN | 13.2 min | 40¢ | 47% | 5¢ | ❌ Lost | -$4.17 |
| 9/28 8:31:13 PM | ZEC | UP | 13.8 min | 32¢ | 41% | 7¢ | ✅ Won | $6.64 |
| 9/28 8:20:39 PM | SOL | DOWN | 9.3 min | 26¢ | 35% | 7¢ | ✅ Won | $7.26 |
| 9/28 8:20:21 PM | HYPE | DOWN | 9.7 min | 35¢ | 43% | 7¢ | ✅ Won | $6.34 |
| 9/28 8:19:25 PM | ZEC | UP | 10.6 min | 23¢ | 35% | 10¢ | ❌ Lost | -$2.43 |
| 9/28 8:18:49 PM | BTC | DOWN | 11.2 min | 38¢ | 48% | 9¢ | ✅ Won | $6.03 |
| 9/28 8:16:52 PM | NEAR | DOWN | 13.1 min | 43¢ | 49% | 4¢ | ✅ Won | $5.52 |
| 9/28 8:16:23 PM | DOGE | DOWN | 13.6 min | 34¢ | 40% | 4¢ | ✅ Won | $6.44 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
