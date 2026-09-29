# Fair-Value Bot

*Updated Tue Sep 29, 1:38 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1317 | $117.51 | +2% | $101.64 / $15.87 |
| 4¢+ ← live bot | 1274 | $320.66 | +5% | $241.40 / $79.26 |
| 6¢+ | 1168 | $334.28 | +7% | $300.82 / $33.46 |
| 8¢+ | 1009 | $393.83 | +10% | $361.78 / $32.05 |
| 10¢+ | 850 | $323.31 | +10% | $223.83 / $99.48 |
| 15¢+ | 510 | $370.93 | +22% | $190.06 / $180.87 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1293 | 1284 | 608 (47%) | 44¢ | 53% | $184.65 | +3% | +5.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 882 | 382 (43%) | 282 / 600 | 8.6 | -$43.45 | -$236.26 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 748 | 249 (33%) | 339 / 409 | 7.3 | -$55.90 | -$299.12 | -11% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 188 | 59 (31%) | 53 / 135 | 2.0 | -$14.97 | -$145.47 | -20% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 201 | 83 (41%) | 67 / 134 | 2.0 | -$13.69 | -$35.71 | -4% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 111 | 51 (46%) | 38 / 73 | 1.5 | -$10.05 | -$5.47 | -1% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 77 | 36 (47%) | 27 / 50 | 1.5 | -$20.08 | -$11.94 | -2% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 23 | 8 (35%) | 10 / 13 | 1.6 | -$5.79 | -$10.38 | -11% |

*Model accuracy vs Kalshi's prices on the same 21,192 readings (excluding the final minute): V1 **+1.2%**, V2 **+1.5%**, 3-exchange price (V3/V4) **-0.3%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $488.08 | $525.36 | $394.02 | 0 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 890 | 762 (86%) | -$219.86 | -6% | 233,390 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.6%** over 33,601 readings from 1332 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 5822 | 2% | 4% | 5% |
| 10–20% | 2603 | 15% | 16% | 15% |
| 20–30% | 2784 | 25% | 26% | 26% |
| 30–40% | 3090 | 35% | 36% | 38% |
| 40–50% | 3349 | 45% | 48% | 52% |
| 50–60% | 3326 | 55% | 59% | 61% |
| 60–70% | 2934 | 65% | 70% | 72% |
| 70–80% | 2372 | 75% | 80% | 82% |
| 80–90% | 2104 | 85% | 88% | 85% |
| 90–100% | 5217 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 662 | 321 (48%) | 45¢ | 51% | $144.11 | +5% |
| 6–10¢ | 451 | 217 (48%) | 44¢ | 53% | $100.04 | +5% |
| 10–20¢ | 160 | 66 (41%) | 43¢ | 57% | -$54.19 | -8% |
| 20¢+ | 11 | 4 (36%) | 40¢ | 68% | -$5.31 | -12% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1125 | 545 (48%) | 45¢ | 54% | $186.29 | +4% |
| 5–10 min | 146 | 57 (39%) | 38¢ | 46% | $2.28 | +0% |
| 2–5 min | 11 | 5 (45%) | 48¢ | 55% | -$3.52 | -7% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 171 | 33 (19%) | 18¢ | 27% | -$3.66 | -1% |
| Toss-up (25–75¢) | 1011 | 487 (48%) | 45¢ | 54% | $155.61 | +3% |
| Favorite (75–95¢) | 102 | 88 (86%) | 82¢ | 89% | $32.70 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 146 | 75 (51%) | 44¢ | 54% | $83.57 | +13% |
| XRP | 145 | 71 (49%) | 45¢ | 53% | $33.29 | +5% |
| ETH | 144 | 63 (44%) | 45¢ | 54% | -$47.18 | -7% |
| SOL | 142 | 72 (51%) | 42¢ | 50% | $100.40 | +16% |
| NEAR | 142 | 68 (48%) | 45¢ | 53% | $16.00 | +2% |
| HYPE | 142 | 63 (44%) | 43¢ | 52% | -$7.58 | -1% |
| ZEC | 141 | 62 (44%) | 41¢ | 50% | $13.93 | +2% |
| DOGE | 141 | 62 (44%) | 44¢ | 52% | -$20.63 | -3% |
| BTC | 141 | 72 (51%) | 49¢ | 57% | $12.85 | +2% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 1:38:14 PM | XRP | UP | 6.8 min | 38¢ | 45% | 5¢ | Open | — |
| 9/29 1:32:49 PM | ETH | UP | 12.2 min | 70¢ | 76% | 4¢ | Open | — |
| 9/29 1:32:43 PM | SOL | UP | 12.3 min | 73¢ | 85% | 11¢ | Open | — |
| 9/29 1:32:15 PM | BTC | UP | 12.8 min | 63¢ | 70% | 5¢ | Open | — |
| 9/29 1:31:53 PM | ZEC | DOWN | 13.1 min | 39¢ | 45% | 4¢ | Open | — |
| 9/29 1:31:22 PM | BNB | DOWN | 13.6 min | 48¢ | 59% | 9¢ | Open | — |
| 9/29 1:31:09 PM | NEAR | DOWN | 13.8 min | 43¢ | 51% | 6¢ | Open | — |
| 9/29 1:31:09 PM | HYPE | DOWN | 13.8 min | 48¢ | 61% | 11¢ | Open | — |
| 9/29 1:31:09 PM | DOGE | DOWN | 13.8 min | 46¢ | 66% | 19¢ | Open | — |
| 9/29 1:24:49 PM | SOL | DOWN | 5.2 min | 34¢ | 50% | 15¢ | ✅ Won | $6.44 |
| 9/29 1:20:27 PM | NEAR | UP | 9.5 min | 16¢ | 22% | 4¢ | ❌ Lost | -$1.70 |
| 9/29 1:20:09 PM | ETH | DOWN | 9.8 min | 47¢ | 53% | 4¢ | ✅ Won | $5.12 |
| 9/29 1:18:22 PM | BTC | UP | 11.6 min | 64¢ | 70% | 4¢ | ❌ Lost | -$6.57 |
| 9/29 1:16:57 PM | ZEC | DOWN | 13.0 min | 69¢ | 75% | 4¢ | ✅ Won | $2.95 |
| 9/29 1:16:57 PM | DOGE | DOWN | 13.0 min | 65¢ | 77% | 10¢ | ✅ Won | $3.34 |
| 9/29 1:16:39 PM | XRP | DOWN | 13.3 min | 52¢ | 58% | 4¢ | ❌ Lost | -$5.38 |
| 9/29 1:16:04 PM | BNB | DOWN | 13.9 min | 62¢ | 75% | 11¢ | ❌ Lost | -$6.37 |
| 9/29 1:16:04 PM | HYPE | DOWN | 13.9 min | 52¢ | 62% | 8¢ | ✅ Won | $4.62 |
| 9/29 1:05:57 PM | ETH | DOWN | 9.1 min | 27¢ | 36% | 8¢ | ❌ Lost | -$2.84 |
| 9/29 1:05:13 PM | DOGE | UP | 9.8 min | 81¢ | 86% | 4¢ | ❌ Lost | -$8.21 |
| 9/29 1:03:02 PM | ZEC | DOWN | 12.0 min | 30¢ | 37% | 5¢ | ✅ Won | $6.85 |
| 9/29 1:03:02 PM | NEAR | DOWN | 12.0 min | 27¢ | 33% | 5¢ | ❌ Lost | -$2.84 |
| 9/29 1:02:59 PM | HYPE | DOWN | 12.0 min | 33¢ | 39% | 4¢ | ✅ Won | $6.54 |
| 9/29 1:02:09 PM | BNB | DOWN | 12.8 min | 38¢ | 48% | 8¢ | ❌ Lost | -$3.97 |
| 9/29 1:01:11 PM | SOL | UP | 13.8 min | 52¢ | 63% | 9¢ | ✅ Won | $4.65 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
