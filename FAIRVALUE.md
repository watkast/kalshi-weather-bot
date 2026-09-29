# Fair-Value Bot

*Updated Tue Sep 29, 7:25 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1164 | $69.19 | +1% | $146.05 / -$76.86 |
| 4¢+ ← live bot | 1122 | $294.16 | +6% | $229.39 / $64.77 |
| 6¢+ | 1030 | $322.82 | +7% | $210.67 / $112.15 |
| 8¢+ | 887 | $366.03 | +11% | $210.69 / $155.34 |
| 10¢+ | 755 | $269.66 | +9% | $160.99 / $108.67 |
| 15¢+ | 459 | $263.03 | +17% | $152.64 / $110.39 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1144 | 1135 | 538 (47%) | 44¢ | 53% | $206.34 | +4% | +5.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 733 | 312 (43%) | 238 / 495 | 8.5 | -$43.45 | -$214.57 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 630 | 209 (33%) | 287 / 343 | 7.3 | -$55.90 | -$286.36 | -12% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 156 | 49 (31%) | 47 / 109 | 1.9 | -$14.97 | -$106.81 | -18% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 75% of orders | 167 | 66 (40%) | 56 / 111 | 2.0 | -$13.69 | -$34.31 | -5% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 86 | 39 (45%) | 30 / 56 | 1.5 | -$10.05 | -$11.88 | -3% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 53 | 24 (45%) | 19 / 34 | 1.5 | -$20.08 | -$47.14 | -9% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 15 | 5 (33%) | 6 / 9 | 1.7 | -$5.79 | -$10.65 | -18% |

*Model accuracy vs Kalshi's prices on the same 17,656 readings (excluding the final minute): V1 **+0.9%**, V2 **+1.3%**, 3-exchange price (V3/V4) **-0.6%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $452.87 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 741 | 613 (83%) | -$198.17 | -7% | 221,531 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.3%** over 29,768 readings from 1179 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 5128 | 2% | 4% | 5% |
| 10–20% | 2343 | 15% | 16% | 15% |
| 20–30% | 2531 | 25% | 26% | 26% |
| 30–40% | 2753 | 35% | 36% | 38% |
| 40–50% | 2925 | 45% | 48% | 52% |
| 50–60% | 2927 | 55% | 59% | 61% |
| 60–70% | 2561 | 65% | 70% | 72% |
| 70–80% | 2119 | 75% | 80% | 82% |
| 80–90% | 1867 | 85% | 88% | 86% |
| 90–100% | 4614 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 591 | 290 (49%) | 45¢ | 51% | $149.34 | +5% |
| 6–10¢ | 396 | 190 (48%) | 43¢ | 53% | $116.50 | +7% |
| 10–20¢ | 139 | 56 (40%) | 42¢ | 56% | -$45.74 | -8% |
| 20¢+ | 9 | 2 (22%) | 36¢ | 65% | -$13.76 | -41% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1019 | 491 (48%) | 45¢ | 53% | $199.49 | +4% |
| 5–10 min | 105 | 42 (40%) | 37¢ | 46% | $18.19 | +5% |
| 2–5 min | 9 | 4 (44%) | 55¢ | 64% | -$10.94 | -21% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 149 | 30 (20%) | 18¢ | 27% | $8.61 | +3% |
| Toss-up (25–75¢) | 909 | 442 (49%) | 45¢ | 54% | $171.23 | +4% |
| Favorite (75–95¢) | 77 | 66 (86%) | 81¢ | 88% | $26.50 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 129 | 66 (51%) | 43¢ | 53% | $89.70 | +16% |
| XRP | 128 | 62 (48%) | 45¢ | 53% | $25.18 | +4% |
| ETH | 128 | 55 (43%) | 45¢ | 53% | -$45.19 | -8% |
| NEAR | 126 | 63 (50%) | 46¢ | 54% | $28.28 | +5% |
| HYPE | 126 | 53 (42%) | 43¢ | 52% | -$32.12 | -6% |
| SOL | 125 | 63 (50%) | 42¢ | 50% | $82.62 | +15% |
| DOGE | 125 | 57 (46%) | 43¢ | 52% | $8.59 | +2% |
| ZEC | 124 | 54 (44%) | 40¢ | 49% | $21.96 | +4% |
| BTC | 124 | 65 (52%) | 49¢ | 57% | $27.32 | +4% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 7:24:11 AM | BTC | DOWN | 5.8 min | 27¢ | 33% | 4¢ | Open | — |
| 9/29 7:22:07 AM | SOL | DOWN | 7.9 min | 30¢ | 36% | 5¢ | Open | — |
| 9/29 7:17:33 AM | ZEC | DOWN | 12.4 min | 40¢ | 46% | 5¢ | Open | — |
| 9/29 7:17:33 AM | BNB | DOWN | 12.4 min | 31¢ | 46% | 13¢ | Open | — |
| 9/29 7:17:33 AM | HYPE | DOWN | 12.4 min | 34¢ | 42% | 6¢ | Open | — |
| 9/29 7:16:59 AM | DOGE | DOWN | 13.0 min | 42¢ | 51% | 8¢ | Open | — |
| 9/29 7:16:59 AM | XRP | DOWN | 13.0 min | 43¢ | 53% | 8¢ | Open | — |
| 9/29 7:16:42 AM | ETH | UP | 13.3 min | 38¢ | 44% | 4¢ | Open | — |
| 9/29 7:16:27 AM | NEAR | DOWN | 13.6 min | 46¢ | 53% | 5¢ | Open | — |
| 9/29 7:05:32 AM | ETH | DOWN | 9.5 min | 37¢ | 49% | 10¢ | ✅ Won | $6.13 |
| 9/29 7:03:50 AM | XRP | UP | 11.2 min | 29¢ | 35% | 5¢ | ❌ Lost | -$3.05 |
| 9/29 7:01:38 AM | NEAR | DOWN | 13.3 min | 31¢ | 48% | 15¢ | ✅ Won | $6.75 |
| 9/29 7:01:38 AM | HYPE | DOWN | 13.3 min | 31¢ | 39% | 6¢ | ❌ Lost | -$3.25 |
| 9/29 7:01:26 AM | BTC | DOWN | 13.6 min | 60¢ | 70% | 8¢ | ❌ Lost | -$6.17 |
| 9/29 7:01:26 AM | DOGE | DOWN | 13.6 min | 66¢ | 75% | 7¢ | ❌ Lost | -$6.75 |
| 9/29 7:01:17 AM | ZEC | UP | 13.7 min | 54¢ | 61% | 5¢ | ✅ Won | $4.42 |
| 9/29 7:01:17 AM | BNB | UP | 13.7 min | 32¢ | 43% | 9¢ | ✅ Won | $6.64 |
| 9/29 7:01:17 AM | SOL | UP | 13.7 min | 33¢ | 44% | 9¢ | ✅ Won | $6.54 |
| 9/29 6:52:47 AM | HYPE | DOWN | 7.2 min | 49¢ | 62% | 11¢ | ✅ Won | $4.92 |
| 9/29 6:50:45 AM | SOL | UP | 9.2 min | 28¢ | 34% | 4¢ | ✅ Won | $7.05 |
| 9/29 6:50:10 AM | ETH | UP | 9.8 min | 27¢ | 35% | 7¢ | ❌ Lost | -$2.84 |
| 9/29 6:49:06 AM | BNB | UP | 10.9 min | 21¢ | 26% | 4¢ | ❌ Lost | -$2.22 |
| 9/29 6:49:06 AM | BTC | UP | 10.9 min | 32¢ | 38% | 4¢ | ❌ Lost | -$3.36 |
| 9/29 6:47:58 AM | ZEC | DOWN | 12.0 min | 38¢ | 44% | 4¢ | ❌ Lost | -$3.97 |
| 9/29 6:47:13 AM | NEAR | DOWN | 12.8 min | 50¢ | 62% | 11¢ | ❌ Lost | -$5.17 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
