# Fair-Value Bot

*Updated Tue Sep 29, 2:28 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1344 | $168.55 | +3% | $102.39 / $66.16 |
| 4¢+ ← live bot | 1301 | $339.42 | +6% | $238.94 / $100.48 |
| 6¢+ | 1195 | $352.73 | +7% | $291.71 / $61.02 |
| 8¢+ | 1036 | $410.24 | +10% | $351.59 / $58.65 |
| 10¢+ | 875 | $340.75 | +10% | $267.71 / $73.04 |
| 15¢+ | 525 | $367.97 | +21% | $223.69 / $144.28 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1320 | 1311 | 621 (47%) | 45¢ | 53% | $171.67 | +3% | +4.8¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 909 | 395 (43%) | 291 / 618 | 8.6 | -$43.45 | -$249.24 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 773 | 265 (34%) | 341 / 432 | 7.3 | -$55.90 | -$251.03 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 194 | 62 (32%) | 54 / 140 | 2.0 | -$14.97 | -$141.10 | -19% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 207 | 88 (43%) | 67 / 140 | 2.0 | -$13.69 | -$18.08 | -2% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 114 | 51 (45%) | 39 / 75 | 1.5 | -$10.05 | -$16.68 | -4% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 79 | 36 (46%) | 28 / 51 | 1.5 | -$20.08 | -$31.10 | -4% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 24 | 9 (38%) | 10 / 14 | 1.6 | -$5.79 | -$4.45 | -5% |

*Model accuracy vs Kalshi's prices on the same 21,844 readings (excluding the final minute): V1 **+1.4%**, V2 **+1.7%**, 3-exchange price (V3/V4) **-0.1%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $468.92 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 917 | 789 (86%) | -$232.84 | -6% | 232,255 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.7%** over 34,307 readings from 1359 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 5962 | 2% | 4% | 5% |
| 10–20% | 2651 | 15% | 16% | 15% |
| 20–30% | 2856 | 25% | 26% | 26% |
| 30–40% | 3178 | 35% | 36% | 38% |
| 40–50% | 3444 | 45% | 48% | 51% |
| 50–60% | 3427 | 55% | 59% | 59% |
| 60–70% | 2997 | 65% | 70% | 71% |
| 70–80% | 2408 | 75% | 80% | 82% |
| 80–90% | 2127 | 85% | 88% | 85% |
| 90–100% | 5257 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 672 | 326 (49%) | 45¢ | 51% | $136.97 | +4% |
| 6–10¢ | 459 | 221 (48%) | 44¢ | 53% | $101.36 | +5% |
| 10–20¢ | 169 | 70 (41%) | 43¢ | 58% | -$61.35 | -8% |
| 20¢+ | 11 | 4 (36%) | 40¢ | 68% | -$5.31 | -12% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1148 | 556 (48%) | 45¢ | 54% | $171.92 | +3% |
| 5–10 min | 150 | 59 (39%) | 38¢ | 46% | $3.67 | +1% |
| 2–5 min | 11 | 5 (45%) | 48¢ | 55% | -$3.52 | -7% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 172 | 33 (19%) | 18¢ | 27% | -$5.67 | -2% |
| Toss-up (25–75¢) | 1035 | 499 (48%) | 45¢ | 54% | $150.01 | +3% |
| Favorite (75–95¢) | 104 | 89 (86%) | 82¢ | 89% | $27.33 | +3% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 149 | 76 (51%) | 44¢ | 54% | $79.14 | +12% |
| XRP | 148 | 71 (48%) | 45¢ | 53% | $15.70 | +2% |
| ETH | 147 | 65 (44%) | 46¢ | 54% | -$49.31 | -7% |
| SOL | 145 | 73 (50%) | 42¢ | 50% | $95.77 | +15% |
| NEAR | 145 | 71 (49%) | 45¢ | 53% | $33.49 | +5% |
| HYPE | 145 | 65 (45%) | 43¢ | 52% | -$0.80 | -0% |
| ZEC | 144 | 64 (44%) | 41¢ | 50% | $22.56 | +4% |
| DOGE | 144 | 64 (44%) | 44¢ | 53% | -$19.71 | -3% |
| BTC | 144 | 72 (50%) | 49¢ | 57% | -$5.17 | -1% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 2:23:11 PM | ETH | DOWN | 6.8 min | 14¢ | 20% | 5¢ | Open | — |
| 9/29 2:20:47 PM | BTC | DOWN | 9.2 min | 18¢ | 23% | 4¢ | Open | — |
| 9/29 2:17:12 PM | SOL | DOWN | 12.8 min | 20¢ | 29% | 8¢ | Open | — |
| 9/29 2:17:10 PM | HYPE | DOWN | 12.8 min | 30¢ | 38% | 7¢ | Open | — |
| 9/29 2:17:10 PM | XRP | DOWN | 12.8 min | 25¢ | 31% | 5¢ | Open | — |
| 9/29 2:16:40 PM | DOGE | DOWN | 13.3 min | 24¢ | 30% | 5¢ | Open | — |
| 9/29 2:16:22 PM | ZEC | DOWN | 13.6 min | 33¢ | 40% | 5¢ | Open | — |
| 9/29 2:16:08 PM | BNB | DOWN | 13.8 min | 41¢ | 68% | 25¢ | Open | — |
| 9/29 2:16:08 PM | NEAR | DOWN | 13.8 min | 32¢ | 39% | 5¢ | Open | — |
| 9/29 2:09:20 PM | BTC | UP | 5.7 min | 48¢ | 59% | 9¢ | ❌ Lost | -$4.98 |
| 9/29 2:05:25 PM | SOL | UP | 9.6 min | 50¢ | 56% | 4¢ | ✅ Won | $4.82 |
| 9/29 2:05:19 PM | ZEC | DOWN | 9.7 min | 43¢ | 51% | 6¢ | ✅ Won | $5.52 |
| 9/29 2:03:59 PM | ETH | DOWN | 11.0 min | 71¢ | 78% | 5¢ | ✅ Won | $2.75 |
| 9/29 2:02:18 PM | DOGE | DOWN | 12.7 min | 69¢ | 76% | 6¢ | ❌ Lost | -$7.05 |
| 9/29 2:02:06 PM | XRP | DOWN | 12.9 min | 75¢ | 83% | 7¢ | ❌ Lost | -$7.64 |
| 9/29 2:01:23 PM | BNB | DOWN | 13.6 min | 27¢ | 41% | 13¢ | ❌ Lost | -$2.84 |
| 9/29 2:01:08 PM | NEAR | DOWN | 13.8 min | 29¢ | 37% | 7¢ | ✅ Won | $6.95 |
| 9/29 2:01:08 PM | HYPE | DOWN | 13.8 min | 41¢ | 48% | 6¢ | ❌ Lost | -$4.27 |
| 9/29 1:47:56 PM | NEAR | DOWN | 12.1 min | 48¢ | 57% | 7¢ | ✅ Won | $5.02 |
| 9/29 1:47:55 PM | HYPE | DOWN | 12.1 min | 38¢ | 53% | 13¢ | ✅ Won | $6.03 |
| 9/29 1:47:39 PM | ZEC | UP | 12.3 min | 27¢ | 44% | 16¢ | ❌ Lost | -$2.82 |
| 9/29 1:47:39 PM | XRP | UP | 12.3 min | 58¢ | 71% | 11¢ | ❌ Lost | -$5.98 |
| 9/29 1:46:59 PM | BNB | DOWN | 13.0 min | 64¢ | 79% | 13¢ | ❌ Lost | -$6.62 |
| 9/29 1:46:32 PM | SOL | UP | 13.4 min | 19¢ | 27% | 7¢ | ❌ Lost | -$2.01 |
| 9/29 1:46:12 PM | DOGE | DOWN | 13.8 min | 71¢ | 78% | 6¢ | ✅ Won | $2.75 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
