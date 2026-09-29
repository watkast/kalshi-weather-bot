# Fair-Value Bot

*Updated Tue Sep 29, 2:59 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1362 | $170.02 | +3% | $98.09 / $71.93 |
| 4¢+ ← live bot | 1319 | $315.36 | +5% | $249.53 / $65.83 |
| 6¢+ | 1212 | $324.92 | +6% | $285.38 / $39.54 |
| 8¢+ | 1049 | $396.28 | +9% | $338.14 / $58.14 |
| 10¢+ | 887 | $351.78 | +10% | $279.51 / $72.27 |
| 15¢+ | 534 | $370.84 | +20% | $240.37 / $130.47 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1338 | 1329 | 623 (47%) | 44¢ | 53% | $128.82 | +2% | +4.7¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 927 | 397 (43%) | 295 / 632 | 8.6 | -$43.45 | -$292.09 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 789 | 269 (34%) | 348 / 441 | 7.3 | -$55.90 | -$263.81 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 198 | 63 (32%) | 55 / 143 | 2.0 | -$14.97 | -$138.14 | -18% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 211 | 89 (42%) | 67 / 144 | 2.0 | -$13.69 | -$19.94 | -2% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 117 | 51 (44%) | 40 / 77 | 1.5 | -$10.05 | -$26.39 | -6% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 82 | 36 (44%) | 29 / 53 | 1.5 | -$20.08 | -$58.26 | -8% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 24 | 9 (38%) | 10 / 14 | 1.6 | -$5.79 | -$4.45 | -5% |

*Model accuracy vs Kalshi's prices on the same 22,294 readings (excluding the final minute): V1 **+1.1%**, V2 **+1.5%**, 3-exchange price (V3/V4) **-0.3%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $441.76 | $525.36 | $394.02 | 2 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 935 | 807 (86%) | -$275.69 | -8% | 233,924 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.5%** over 34,793 readings from 1377 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 5972 | 2% | 4% | 5% |
| 10–20% | 2655 | 15% | 16% | 15% |
| 20–30% | 2882 | 25% | 26% | 26% |
| 30–40% | 3242 | 35% | 36% | 38% |
| 40–50% | 3506 | 45% | 48% | 51% |
| 50–60% | 3465 | 55% | 59% | 60% |
| 60–70% | 3044 | 65% | 70% | 72% |
| 70–80% | 2462 | 75% | 80% | 82% |
| 80–90% | 2191 | 85% | 88% | 86% |
| 90–100% | 5374 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 684 | 328 (48%) | 45¢ | 51% | $116.30 | +4% |
| 6–10¢ | 462 | 221 (48%) | 44¢ | 53% | $92.56 | +4% |
| 10–20¢ | 171 | 70 (41%) | 43¢ | 58% | -$70.48 | -9% |
| 20¢+ | 12 | 4 (33%) | 40¢ | 68% | -$9.56 | -19% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1159 | 556 (48%) | 45¢ | 54% | $134.39 | +2% |
| 5–10 min | 157 | 61 (39%) | 38¢ | 46% | -$1.65 | -0% |
| 2–5 min | 11 | 5 (45%) | 48¢ | 55% | -$3.52 | -7% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 176 | 33 (19%) | 18¢ | 27% | -$13.72 | -4% |
| Toss-up (25–75¢) | 1049 | 501 (48%) | 45¢ | 54% | $115.21 | +2% |
| Favorite (75–95¢) | 104 | 89 (86%) | 82¢ | 89% | $27.33 | +3% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 151 | 76 (50%) | 44¢ | 54% | $69.51 | +10% |
| XRP | 150 | 71 (47%) | 45¢ | 53% | $10.01 | +1% |
| ETH | 149 | 65 (44%) | 46¢ | 54% | -$57.07 | -8% |
| SOL | 147 | 73 (50%) | 42¢ | 50% | $89.90 | +14% |
| NEAR | 147 | 72 (49%) | 45¢ | 53% | $34.75 | +5% |
| HYPE | 147 | 65 (44%) | 43¢ | 52% | -$8.41 | -1% |
| ZEC | 146 | 64 (44%) | 41¢ | 50% | $15.74 | +3% |
| DOGE | 146 | 64 (44%) | 44¢ | 53% | -$25.79 | -4% |
| BTC | 146 | 73 (50%) | 48¢ | 57% | $0.18 | +0% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 2:52:53 PM | BTC | UP | 7.1 min | 57¢ | 64% | 5¢ | Open | — |
| 9/29 2:48:35 PM | NEAR | DOWN | 11.4 min | 31¢ | 42% | 10¢ | Open | — |
| 9/29 2:48:23 PM | ZEC | DOWN | 11.6 min | 38¢ | 47% | 7¢ | Open | — |
| 9/29 2:48:18 PM | DOGE | UP | 11.7 min | 26¢ | 35% | 8¢ | Open | — |
| 9/29 2:47:54 PM | HYPE | DOWN | 12.1 min | 45¢ | 52% | 5¢ | Open | — |
| 9/29 2:47:28 PM | BNB | DOWN | 12.5 min | 56¢ | 67% | 10¢ | Open | — |
| 9/29 2:46:51 PM | SOL | UP | 13.1 min | 30¢ | 37% | 5¢ | Open | — |
| 9/29 2:46:23 PM | ETH | UP | 13.6 min | 36¢ | 43% | 5¢ | Open | — |
| 9/29 2:46:19 PM | XRP | UP | 13.7 min | 38¢ | 46% | 6¢ | Open | — |
| 9/29 2:38:19 PM | NEAR | DOWN | 6.7 min | 52¢ | 58% | 4¢ | ✅ Won | $4.62 |
| 9/29 2:37:47 PM | BTC | UP | 7.2 min | 26¢ | 32% | 4¢ | ✅ Won | $7.26 |
| 9/29 2:36:58 PM | ETH | DOWN | 8.0 min | 61¢ | 68% | 5¢ | ❌ Lost | -$6.27 |
| 9/29 2:36:18 PM | HYPE | DOWN | 8.7 min | 43¢ | 50% | 5¢ | ❌ Lost | -$4.48 |
| 9/29 2:35:34 PM | XRP | UP | 9.4 min | 29¢ | 35% | 5¢ | ❌ Lost | -$3.05 |
| 9/29 2:33:13 PM | SOL | UP | 11.8 min | 36¢ | 51% | 13¢ | ❌ Lost | -$3.75 |
| 9/29 2:32:36 PM | ZEC | DOWN | 12.4 min | 32¢ | 38% | 5¢ | ❌ Lost | -$3.36 |
| 9/29 2:31:53 PM | DOGE | UP | 13.1 min | 34¢ | 42% | 6¢ | ❌ Lost | -$3.55 |
| 9/29 2:31:15 PM | BNB | DOWN | 13.7 min | 52¢ | 64% | 10¢ | ❌ Lost | -$5.38 |
| 9/29 2:23:11 PM | ETH | DOWN | 6.8 min | 14¢ | 20% | 5¢ | ❌ Lost | -$1.49 |
| 9/29 2:20:47 PM | BTC | DOWN | 9.2 min | 18¢ | 23% | 4¢ | ❌ Lost | -$1.91 |
| 9/29 2:17:12 PM | SOL | DOWN | 12.8 min | 20¢ | 29% | 8¢ | ❌ Lost | -$2.12 |
| 9/29 2:17:10 PM | HYPE | DOWN | 12.8 min | 30¢ | 38% | 7¢ | ❌ Lost | -$3.13 |
| 9/29 2:17:10 PM | XRP | DOWN | 12.8 min | 25¢ | 31% | 5¢ | ❌ Lost | -$2.64 |
| 9/29 2:16:40 PM | DOGE | DOWN | 13.3 min | 24¢ | 30% | 5¢ | ❌ Lost | -$2.53 |
| 9/29 2:16:22 PM | ZEC | DOWN | 13.6 min | 33¢ | 40% | 5¢ | ❌ Lost | -$3.46 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
