# Fair-Value Bot

*Updated Tue Sep 29, 3:19 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1380 | $165.00 | +3% | $101.49 / $63.51 |
| 4¢+ | 1337 | $297.56 | +5% | $244.23 / $53.33 |
| 6¢+ | 1229 | $294.34 | +6% | $286.17 / $8.17 |
| 8¢+ ← live bot | 1065 | $400.98 | +9% | $335.78 / $65.20 |
| 10¢+ | 902 | $367.93 | +11% | $257.08 / $110.85 |
| 15¢+ | 542 | $371.09 | +20% | $234.82 / $136.27 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1350 | 1347 | 631 (47%) | 45¢ | 53% | $107.15 | +2% | +4.6¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 945 | 405 (43%) | 301 / 644 | 8.6 | -$43.45 | -$313.76 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 807 | 278 (34%) | 361 / 446 | 7.3 | -$55.90 | -$240.46 | -8% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 202 | 64 (32%) | 55 / 147 | 2.0 | -$14.97 | -$149.53 | -19% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 215 | 91 (42%) | 69 / 146 | 2.0 | -$13.69 | -$17.63 | -2% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 120 | 52 (43%) | 42 / 78 | 1.5 | -$10.05 | -$29.53 | -6% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 85 | 37 (44%) | 31 / 54 | 1.5 | -$20.08 | -$69.71 | -9% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 26 | 10 (38%) | 11 / 15 | 1.6 | -$5.79 | -$1.88 | -2% |

*Model accuracy vs Kalshi's prices on the same 22,738 readings (excluding the final minute): V1 **+1.0%**, V2 **+1.5%**, 3-exchange price (V3/V4) **-0.4%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $430.31 | $525.36 | $394.02 | 0 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 953 | 825 (87%) | -$297.36 | -8% | 234,324 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.5%** over 35,273 readings from 1395 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 6067 | 2% | 4% | 5% |
| 10–20% | 2705 | 15% | 16% | 16% |
| 20–30% | 2938 | 25% | 26% | 26% |
| 30–40% | 3310 | 35% | 36% | 38% |
| 40–50% | 3575 | 45% | 48% | 51% |
| 50–60% | 3514 | 55% | 59% | 60% |
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
| 4–6¢ | 695 | 334 (48%) | 45¢ | 51% | $103.38 | +3% |
| 6–10¢ | 468 | 222 (47%) | 44¢ | 53% | $77.47 | +4% |
| 10–20¢ | 172 | 71 (41%) | 43¢ | 58% | -$64.14 | -8% |
| 20¢+ | 12 | 4 (33%) | 40¢ | 68% | -$9.56 | -19% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1175 | 563 (48%) | 45¢ | 54% | $117.97 | +2% |
| 5–10 min | 159 | 62 (39%) | 38¢ | 46% | -$6.90 | -1% |
| 2–5 min | 11 | 5 (45%) | 48¢ | 55% | -$3.52 | -7% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 176 | 33 (19%) | 18¢ | 27% | -$13.72 | -4% |
| Toss-up (25–75¢) | 1063 | 506 (48%) | 45¢ | 54% | $99.06 | +2% |
| Favorite (75–95¢) | 108 | 92 (85%) | 82¢ | 89% | $21.81 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 153 | 77 (50%) | 44¢ | 55% | $68.35 | +10% |
| XRP | 152 | 71 (47%) | 45¢ | 53% | -$2.93 | -0% |
| ETH | 151 | 66 (44%) | 46¢ | 54% | -$58.18 | -8% |
| SOL | 149 | 75 (50%) | 42¢ | 50% | $98.17 | +15% |
| NEAR | 149 | 73 (49%) | 45¢ | 53% | $32.13 | +5% |
| HYPE | 149 | 65 (44%) | 43¢ | 52% | -$19.61 | -3% |
| ZEC | 148 | 65 (44%) | 42¢ | 50% | $13.18 | +2% |
| DOGE | 148 | 65 (44%) | 44¢ | 52% | -$22.19 | -3% |
| BTC | 148 | 74 (50%) | 49¢ | 57% | -$1.77 | -0% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 3:16:14 PM | ETH | DOWN | 13.8 min | 67¢ | 73% | 4¢ | Open | — |
| 9/29 3:16:13 PM | BTC | DOWN | 13.8 min | 65¢ | 75% | 9¢ | Open | — |
| 9/29 3:16:13 PM | DOGE | UP | 13.8 min | 32¢ | 46% | 13¢ | Open | — |
| 9/29 3:05:00 PM | NEAR | DOWN | 10.0 min | 93¢ | 98% | 4¢ | ✅ Won | $0.63 |
| 9/29 3:04:56 PM | HYPE | DOWN | 10.1 min | 64¢ | 70% | 4¢ | ❌ Lost | -$6.52 |
| 9/29 3:03:35 PM | ZEC | DOWN | 11.4 min | 85¢ | 91% | 5¢ | ✅ Won | $1.41 |
| 9/29 3:03:24 PM | XRP | DOWN | 11.6 min | 89¢ | 94% | 4¢ | ❌ Lost | -$8.97 |
| 9/29 3:02:48 PM | SOL | DOWN | 12.2 min | 85¢ | 91% | 5¢ | ✅ Won | $1.41 |
| 9/29 3:02:06 PM | ETH | DOWN | 12.9 min | 72¢ | 78% | 5¢ | ✅ Won | $2.66 |
| 9/29 3:01:53 PM | DOGE | UP | 13.1 min | 35¢ | 48% | 12¢ | ✅ Won | $6.34 |
| 9/29 3:01:07 PM | BTC | DOWN | 13.9 min | 59¢ | 65% | 5¢ | ✅ Won | $3.93 |
| 9/29 3:01:07 PM | BNB | DOWN | 13.9 min | 52¢ | 61% | 7¢ | ✅ Won | $4.62 |
| 9/29 2:52:53 PM | BTC | UP | 7.1 min | 57¢ | 64% | 5¢ | ❌ Lost | -$5.88 |
| 9/29 2:48:35 PM | NEAR | DOWN | 11.4 min | 31¢ | 42% | 10¢ | ❌ Lost | -$3.25 |
| 9/29 2:48:23 PM | ZEC | DOWN | 11.6 min | 38¢ | 47% | 7¢ | ❌ Lost | -$3.97 |
| 9/29 2:48:18 PM | DOGE | UP | 11.7 min | 26¢ | 35% | 8¢ | ❌ Lost | -$2.74 |
| 9/29 2:47:54 PM | HYPE | DOWN | 12.1 min | 45¢ | 52% | 5¢ | ❌ Lost | -$4.68 |
| 9/29 2:47:28 PM | BNB | DOWN | 12.5 min | 56¢ | 67% | 10¢ | ❌ Lost | -$5.78 |
| 9/29 2:46:51 PM | SOL | UP | 13.1 min | 30¢ | 37% | 5¢ | ✅ Won | $6.86 |
| 9/29 2:46:23 PM | ETH | UP | 13.6 min | 36¢ | 43% | 5¢ | ❌ Lost | -$3.77 |
| 9/29 2:46:19 PM | XRP | UP | 13.7 min | 38¢ | 46% | 6¢ | ❌ Lost | -$3.97 |
| 9/29 2:38:19 PM | NEAR | DOWN | 6.7 min | 52¢ | 58% | 4¢ | ✅ Won | $4.62 |
| 9/29 2:37:47 PM | BTC | UP | 7.2 min | 26¢ | 32% | 4¢ | ✅ Won | $7.26 |
| 9/29 2:36:58 PM | ETH | DOWN | 8.0 min | 61¢ | 68% | 5¢ | ❌ Lost | -$6.27 |
| 9/29 2:36:18 PM | HYPE | DOWN | 8.7 min | 43¢ | 50% | 5¢ | ❌ Lost | -$4.48 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
