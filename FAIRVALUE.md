# Fair-Value Bot

*Updated Tue Sep 29, 12:37 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1281 | $83.88 | +1% | $179.09 / -$95.21 |
| 4¢+ ← live bot | 1238 | $306.00 | +5% | $282.26 / $23.74 |
| 6¢+ | 1134 | $326.64 | +7% | $330.69 / -$4.05 |
| 8¢+ | 979 | $376.26 | +10% | $300.34 / $75.92 |
| 10¢+ | 824 | $288.39 | +9% | $188.87 / $99.52 |
| 15¢+ | 496 | $323.34 | +19% | $160.53 / $162.81 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1257 | 1249 | 597 (48%) | 45¢ | 53% | $215.00 | +4% | +5.2¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 847 | 371 (44%) | 268 / 579 | 8.6 | -$43.45 | -$205.91 | -5% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 715 | 231 (32%) | 316 / 399 | 7.2 | -$55.90 | -$340.06 | -13% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 180 | 59 (33%) | 49 / 131 | 2.0 | -$14.97 | -$112.20 | -16% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 193 | 81 (42%) | 65 / 128 | 2.0 | -$13.69 | -$21.44 | -3% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 105 | 49 (47%) | 37 / 68 | 1.5 | -$10.05 | -$4.01 | -1% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 71 | 34 (48%) | 26 / 45 | 1.5 | -$20.08 | -$6.42 | -1% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 21 | 7 (33%) | 9 / 12 | 1.6 | -$5.79 | -$14.18 | -17% |

*Model accuracy vs Kalshi's prices on the same 20,301 readings (excluding the final minute): V1 **+1.3%**, V2 **+1.4%**, 3-exchange price (V3/V4) **-0.1%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $493.60 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 855 | 727 (85%) | -$189.51 | -6% | 228,503 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.6%** over 32,638 readings from 1296 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 5734 | 2% | 4% | 5% |
| 10–20% | 2549 | 15% | 16% | 16% |
| 20–30% | 2717 | 25% | 26% | 26% |
| 30–40% | 2998 | 35% | 36% | 39% |
| 40–50% | 3234 | 45% | 48% | 53% |
| 50–60% | 3195 | 55% | 59% | 61% |
| 60–70% | 2842 | 65% | 70% | 73% |
| 70–80% | 2302 | 75% | 80% | 83% |
| 80–90% | 2025 | 85% | 88% | 86% |
| 90–100% | 5042 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 641 | 316 (49%) | 45¢ | 52% | $173.51 | +6% |
| 6–10¢ | 440 | 213 (48%) | 44¢ | 54% | $105.98 | +5% |
| 10–20¢ | 158 | 65 (41%) | 43¢ | 57% | -$54.26 | -8% |
| 20¢+ | 10 | 3 (30%) | 39¢ | 68% | -$10.23 | -25% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1099 | 536 (49%) | 45¢ | 54% | $206.02 | +4% |
| 5–10 min | 137 | 55 (40%) | 38¢ | 46% | $12.90 | +2% |
| 2–5 min | 11 | 5 (45%) | 48¢ | 55% | -$3.52 | -7% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 164 | 32 (20%) | 18¢ | 27% | $0.07 | +0% |
| Toss-up (25–75¢) | 984 | 477 (48%) | 45¢ | 54% | $174.02 | +4% |
| Favorite (75–95¢) | 101 | 88 (87%) | 82¢ | 89% | $40.91 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 142 | 74 (52%) | 44¢ | 54% | $93.67 | +14% |
| XRP | 141 | 70 (50%) | 45¢ | 53% | $38.72 | +6% |
| ETH | 141 | 62 (44%) | 46¢ | 54% | -$45.49 | -7% |
| SOL | 138 | 70 (51%) | 42¢ | 50% | $95.35 | +16% |
| NEAR | 138 | 68 (49%) | 46¢ | 54% | $26.43 | +4% |
| HYPE | 138 | 60 (43%) | 44¢ | 53% | -$22.89 | -4% |
| ZEC | 137 | 60 (44%) | 42¢ | 51% | $7.57 | +1% |
| DOGE | 137 | 61 (45%) | 44¢ | 52% | -$7.32 | -1% |
| BTC | 137 | 72 (53%) | 49¢ | 57% | $28.96 | +4% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 12:36:38 PM | BTC | DOWN | 8.3 min | 19¢ | 24% | 4¢ | Open | — |
| 9/29 12:36:11 PM | NEAR | DOWN | 8.8 min | 32¢ | 38% | 4¢ | Open | — |
| 9/29 12:34:29 PM | DOGE | DOWN | 10.5 min | 49¢ | 58% | 7¢ | Open | — |
| 9/29 12:34:29 PM | ZEC | DOWN | 10.5 min | 26¢ | 36% | 9¢ | Open | — |
| 9/29 12:34:29 PM | SOL | DOWN | 10.5 min | 38¢ | 45% | 6¢ | Open | — |
| 9/29 12:34:23 PM | XRP | DOWN | 10.6 min | 24¢ | 30% | 4¢ | Open | — |
| 9/29 12:33:39 PM | HYPE | DOWN | 11.3 min | 35¢ | 43% | 6¢ | Open | — |
| 9/29 12:32:24 PM | BNB | DOWN | 12.6 min | 45¢ | 56% | 10¢ | Open | — |
| 9/29 12:22:22 PM | SOL | DOWN | 7.6 min | 26¢ | 32% | 5¢ | ❌ Lost | -$2.74 |
| 9/29 12:21:42 PM | DOGE | DOWN | 8.3 min | 21¢ | 28% | 6¢ | ❌ Lost | -$2.22 |
| 9/29 12:21:17 PM | BTC | DOWN | 8.7 min | 38¢ | 44% | 4¢ | ❌ Lost | -$3.97 |
| 9/29 12:20:27 PM | ETH | DOWN | 9.5 min | 49¢ | 55% | 4¢ | ❌ Lost | -$5.08 |
| 9/29 12:20:20 PM | NEAR | DOWN | 9.7 min | 30¢ | 38% | 6¢ | ❌ Lost | -$3.15 |
| 9/29 12:18:06 PM | ZEC | UP | 11.9 min | 36¢ | 42% | 4¢ | ❌ Lost | -$3.77 |
| 9/29 12:16:33 PM | XRP | DOWN | 13.4 min | 38¢ | 44% | 5¢ | ❌ Lost | -$3.97 |
| 9/29 12:16:28 PM | BNB | DOWN | 13.5 min | 30¢ | 40% | 9¢ | ❌ Lost | -$3.15 |
| 9/29 12:16:09 PM | HYPE | DOWN | 13.8 min | 33¢ | 48% | 13¢ | ❌ Lost | -$3.46 |
| 9/29 12:02:33 PM | HYPE | DOWN | 12.4 min | 24¢ | 31% | 5¢ | ❌ Lost | -$2.53 |
| 9/29 12:02:03 PM | NEAR | DOWN | 12.9 min | 24¢ | 31% | 6¢ | ❌ Lost | -$2.53 |
| 9/29 12:01:49 PM | DOGE | UP | 13.2 min | 84¢ | 93% | 8¢ | ✅ Won | $1.50 |
| 9/29 12:01:20 PM | BNB | UP | 13.7 min | 91¢ | 97% | 6¢ | ✅ Won | $0.85 |
| 9/29 12:01:20 PM | ETH | UP | 13.7 min | 89¢ | 99% | 9¢ | ✅ Won | $1.03 |
| 9/29 12:01:20 PM | BTC | UP | 13.7 min | 89¢ | 99% | 9¢ | ✅ Won | $1.03 |
| 9/29 12:01:20 PM | XRP | UP | 13.7 min | 89¢ | 96% | 6¢ | ✅ Won | $1.03 |
| 9/29 12:01:20 PM | ZEC | UP | 13.7 min | 91¢ | 98% | 6¢ | ✅ Won | $0.85 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
