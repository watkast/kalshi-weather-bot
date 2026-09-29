# Fair-Value Bot

*Updated Mon Sep 28, 10:11 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **6¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **6¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 842 | $171.57 | +4% | $181.44 / -$9.87 |
| 4¢+ ← live bot | 812 | $350.79 | +9% | $228.82 / $121.97 |
| 6¢+ | 751 | $389.50 | +12% | $249.56 / $139.94 |
| 8¢+ | 660 | $379.18 | +15% | $188.34 / $190.84 |
| 10¢+ | 568 | $302.94 | +14% | $160.66 / $142.28 |
| 15¢+ | 340 | $246.88 | +22% | $156.32 / $90.56 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 826 | 817 | 413 (51%) | 45¢ | 53% | $350.03 | +9% | +7.2¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 415 | 187 (45%) | 120 / 295 | 8.3 | -$37.76 | -$70.88 | -4% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 373 | 127 (34%) | 164 / 209 | 7.5 | -$55.90 | -$187.33 | -13% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 90 | 31 (34%) | 34 / 56 | 2.0 | -$14.97 | -$29.67 | -9% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 97 | 39 (40%) | 33 / 64 | 2.0 | -$13.69 | -$33.40 | -8% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 39 | 19 (49%) | 14 / 25 | 1.6 | -$10.05 | -$3.68 | -2% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 9 | 6 (67%) | 4 / 5 | 1.8 | -$4.10 | $22.12 | +25% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 2 | 0 (0%) | 1 / 1 | 2.0 | -$5.79 | -$5.79 | -100% |

*Model accuracy vs Kalshi's prices on the same 10,286 readings (excluding the final minute): V1 **+2.9%**, V2 **+2.8%**, 3-exchange price (V3/V4) **+1.3%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $522.12 | $525.36 | $394.02 | 0 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 423 | 295 (70%) | -$54.48 | -4% | 68,380 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.4%** over 21,874 readings from 855 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4044 | 2% | 4% | 6% |
| 10–20% | 1750 | 15% | 16% | 16% |
| 20–30% | 1944 | 25% | 26% | 26% |
| 30–40% | 2134 | 35% | 36% | 38% |
| 40–50% | 2203 | 45% | 47% | 51% |
| 50–60% | 2178 | 55% | 59% | 58% |
| 60–70% | 1857 | 65% | 70% | 68% |
| 70–80% | 1550 | 75% | 80% | 79% |
| 80–90% | 1319 | 85% | 88% | 82% |
| 90–100% | 2895 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 455 | 236 (52%) | 45¢ | 52% | $226.99 | +11% |
| 6–10¢ | 274 | 139 (51%) | 45¢ | 54% | $123.03 | +10% |
| 10–20¢ | 82 | 36 (44%) | 42¢ | 56% | $1.92 | +1% |
| 20¢+ | 6 | 2 (33%) | 35¢ | 65% | -$1.91 | -9% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 759 | 388 (51%) | 45¢ | 53% | $324.85 | +9% |
| 5–10 min | 54 | 22 (41%) | 35¢ | 44% | $23.24 | +12% |
| 2–5 min | 2 | 2 (100%) | 88¢ | 94% | $2.34 | +13% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 89 | 20 (22%) | 19¢ | 27% | $23.28 | +13% |
| Toss-up (25–75¢) | 682 | 355 (52%) | 46¢ | 54% | $320.65 | +10% |
| Favorite (75–95¢) | 46 | 38 (83%) | 80¢ | 87% | $6.10 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 93 | 51 (55%) | 42¢ | 52% | $101.71 | +25% |
| XRP | 92 | 50 (54%) | 47¢ | 54% | $56.56 | +13% |
| ETH | 92 | 41 (45%) | 46¢ | 54% | -$25.55 | -6% |
| HYPE | 91 | 41 (45%) | 42¢ | 51% | $10.72 | +3% |
| SOL | 90 | 47 (52%) | 44¢ | 52% | $61.66 | +15% |
| NEAR | 90 | 49 (54%) | 48¢ | 56% | $42.00 | +9% |
| DOGE | 90 | 47 (52%) | 44¢ | 52% | $60.00 | +15% |
| BTC | 90 | 47 (52%) | 49¢ | 57% | $14.16 | +3% |
| ZEC | 89 | 40 (45%) | 40¢ | 49% | $28.77 | +8% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 10:10:16 PM | NEAR | UP | 4.7 min | 40¢ | 46% | 4¢ | Open | — |
| 9/28 10:05:10 PM | BTC | UP | 9.8 min | 48¢ | 57% | 8¢ | Open | — |
| 9/28 10:03:52 PM | SOL | DOWN | 11.1 min | 81¢ | 89% | 7¢ | Open | — |
| 9/28 10:03:52 PM | DOGE | DOWN | 11.1 min | 74¢ | 85% | 9¢ | Open | — |
| 9/28 10:02:50 PM | XRP | UP | 12.2 min | 59¢ | 67% | 6¢ | Open | — |
| 9/28 10:01:44 PM | ZEC | DOWN | 13.2 min | 53¢ | 76% | 21¢ | Open | — |
| 9/28 10:01:30 PM | HYPE | DOWN | 13.5 min | 69¢ | 75% | 4¢ | Open | — |
| 9/28 10:01:11 PM | BNB | DOWN | 13.8 min | 60¢ | 77% | 14¢ | Open | — |
| 9/28 10:01:11 PM | ETH | DOWN | 13.8 min | 55¢ | 66% | 9¢ | Open | — |
| 9/28 9:53:14 PM | DOGE | DOWN | 6.8 min | 41¢ | 56% | 13¢ | ✅ Won | $5.76 |
| 9/28 9:52:31 PM | NEAR | DOWN | 7.5 min | 51¢ | 57% | 4¢ | ✅ Won | $4.73 |
| 9/28 9:50:12 PM | BTC | UP | 9.8 min | 59¢ | 66% | 5¢ | ❌ Lost | -$6.07 |
| 9/28 9:50:06 PM | ETH | DOWN | 9.9 min | 43¢ | 54% | 9¢ | ✅ Won | $5.52 |
| 9/28 9:49:52 PM | HYPE | DOWN | 10.1 min | 51¢ | 58% | 5¢ | ❌ Lost | -$5.32 |
| 9/28 9:47:50 PM | SOL | UP | 12.2 min | 48¢ | 54% | 4¢ | ❌ Lost | -$4.98 |
| 9/28 9:47:23 PM | BNB | DOWN | 12.6 min | 58¢ | 67% | 7¢ | ✅ Won | $4.03 |
| 9/28 9:46:29 PM | XRP | UP | 13.5 min | 41¢ | 48% | 6¢ | ❌ Lost | -$4.27 |
| 9/28 9:46:29 PM | ZEC | UP | 13.5 min | 40¢ | 47% | 5¢ | ❌ Lost | -$4.17 |
| 9/28 9:37:38 PM | XRP | UP | 7.3 min | 66¢ | 76% | 8¢ | ✅ Won | $3.24 |
| 9/28 9:35:29 PM | DOGE | UP | 9.5 min | 41¢ | 51% | 9¢ | ❌ Lost | -$4.27 |
| 9/28 9:33:43 PM | ZEC | UP | 11.3 min | 27¢ | 33% | 5¢ | ❌ Lost | -$2.82 |
| 9/28 9:32:51 PM | SOL | DOWN | 12.1 min | 67¢ | 78% | 10¢ | ❌ Lost | -$6.83 |
| 9/28 9:32:15 PM | NEAR | DOWN | 12.7 min | 59¢ | 68% | 8¢ | ❌ Lost | -$6.06 |
| 9/28 9:31:58 PM | ETH | DOWN | 13.0 min | 68¢ | 75% | 5¢ | ✅ Won | $3.04 |
| 9/28 9:31:58 PM | HYPE | DOWN | 13.0 min | 66¢ | 75% | 8¢ | ❌ Lost | -$6.76 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
