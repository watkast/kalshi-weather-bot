# Fair-Value Bot

*Updated Tue Sep 29, 5:13 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1084 | $77.02 | +1% | $153.95 / -$76.93 |
| 4¢+ ← live bot | 1047 | $295.02 | +6% | $184.11 / $110.91 |
| 6¢+ | 964 | $299.23 | +7% | $189.92 / $109.31 |
| 8¢+ | 832 | $312.05 | +10% | $194.31 / $117.74 |
| 10¢+ | 710 | $224.31 | +8% | $189.34 / $34.97 |
| 15¢+ | 432 | $218.44 | +15% | $173.78 / $44.66 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1064 | 1055 | 506 (48%) | 44¢ | 53% | $228.48 | +5% | +5.9¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 653 | 280 (43%) | 215 / 438 | 8.5 | -$37.76 | -$192.43 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 564 | 188 (33%) | 258 / 306 | 7.3 | -$55.90 | -$263.95 | -12% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 140 | 46 (33%) | 41 / 99 | 1.9 | -$14.97 | -$86.42 | -16% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 149 | 61 (41%) | 53 / 96 | 2.0 | -$13.69 | -$19.24 | -3% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 76 | 35 (46%) | 26 / 50 | 1.5 | -$10.05 | -$9.26 | -3% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 44 | 21 (48%) | 15 / 29 | 1.5 | -$20.08 | -$21.84 | -5% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 11 | 3 (27%) | 4 / 7 | 1.6 | -$5.79 | -$9.53 | -24% |

*Model accuracy vs Kalshi's prices on the same 15,815 readings (excluding the final minute): V1 **+1.1%**, V2 **+1.7%**, 3-exchange price (V3/V4) **-0.3%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $478.17 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 661 | 533 (81%) | -$176.03 | -7% | 207,695 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.5%** over 27,789 readings from 1098 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4966 | 2% | 4% | 6% |
| 10–20% | 2217 | 15% | 16% | 16% |
| 20–30% | 2392 | 25% | 26% | 26% |
| 30–40% | 2586 | 35% | 36% | 39% |
| 40–50% | 2696 | 45% | 48% | 53% |
| 50–60% | 2729 | 55% | 59% | 61% |
| 60–70% | 2380 | 65% | 70% | 72% |
| 70–80% | 1984 | 75% | 80% | 82% |
| 80–90% | 1738 | 85% | 88% | 86% |
| 90–100% | 4101 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 563 | 281 (50%) | 45¢ | 52% | $179.05 | +7% |
| 6–10¢ | 362 | 176 (49%) | 44¢ | 53% | $124.16 | +8% |
| 10–20¢ | 121 | 47 (39%) | 42¢ | 56% | -$60.97 | -11% |
| 20¢+ | 9 | 2 (22%) | 36¢ | 65% | -$13.76 | -41% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 950 | 466 (49%) | 45¢ | 53% | $233.75 | +5% |
| 5–10 min | 95 | 35 (37%) | 35¢ | 44% | $3.33 | +1% |
| 2–5 min | 8 | 4 (50%) | 59¢ | 67% | -$8.20 | -17% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 141 | 27 (19%) | 19¢ | 27% | -$6.58 | -2% |
| Toss-up (25–75¢) | 843 | 418 (50%) | 45¢ | 54% | $205.97 | +5% |
| Favorite (75–95¢) | 71 | 61 (86%) | 81¢ | 88% | $29.09 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 120 | 62 (52%) | 43¢ | 53% | $85.83 | +16% |
| XRP | 119 | 58 (49%) | 45¢ | 53% | $27.44 | +5% |
| ETH | 119 | 51 (43%) | 45¢ | 53% | -$42.54 | -8% |
| HYPE | 118 | 50 (42%) | 43¢ | 52% | -$22.97 | -4% |
| NEAR | 117 | 59 (50%) | 47¢ | 54% | $25.28 | +4% |
| SOL | 116 | 60 (52%) | 42¢ | 50% | $89.42 | +18% |
| DOGE | 116 | 54 (47%) | 44¢ | 52% | $12.81 | +2% |
| ZEC | 115 | 49 (43%) | 40¢ | 49% | $7.72 | +2% |
| BTC | 115 | 63 (55%) | 49¢ | 57% | $45.49 | +8% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 5:03:42 AM | BTC | UP | 11.3 min | 30¢ | 42% | 10¢ | Open | — |
| 9/29 5:03:42 AM | SOL | UP | 11.3 min | 31¢ | 47% | 14¢ | Open | — |
| 9/29 5:02:32 AM | ZEC | DOWN | 12.4 min | 72¢ | 80% | 6¢ | Open | — |
| 9/29 5:02:26 AM | HYPE | UP | 12.6 min | 53¢ | 65% | 10¢ | Open | — |
| 9/29 5:02:12 AM | BNB | DOWN | 12.8 min | 54¢ | 64% | 8¢ | Open | — |
| 9/29 5:01:50 AM | ETH | UP | 13.2 min | 72¢ | 83% | 10¢ | Open | — |
| 9/29 5:01:42 AM | XRP | DOWN | 13.3 min | 39¢ | 47% | 6¢ | Open | — |
| 9/29 5:01:42 AM | DOGE | DOWN | 13.3 min | 41¢ | 56% | 13¢ | Open | — |
| 9/29 5:01:06 AM | NEAR | DOWN | 13.9 min | 39¢ | 48% | 7¢ | Open | — |
| 9/29 4:51:36 AM | BTC | DOWN | 8.4 min | 26¢ | 32% | 4¢ | ❌ Lost | -$2.74 |
| 9/29 4:47:24 AM | ETH | UP | 12.6 min | 44¢ | 51% | 6¢ | ✅ Won | $5.42 |
| 9/29 4:47:09 AM | HYPE | UP | 12.8 min | 50¢ | 63% | 11¢ | ✅ Won | $4.82 |
| 9/29 4:47:00 AM | XRP | DOWN | 13.0 min | 29¢ | 36% | 6¢ | ❌ Lost | -$3.05 |
| 9/29 4:46:26 AM | DOGE | DOWN | 13.6 min | 32¢ | 43% | 10¢ | ❌ Lost | -$3.36 |
| 9/29 4:46:26 AM | ZEC | DOWN | 13.6 min | 34¢ | 40% | 5¢ | ❌ Lost | -$3.56 |
| 9/29 4:46:19 AM | NEAR | DOWN | 13.7 min | 47¢ | 59% | 11¢ | ❌ Lost | -$4.88 |
| 9/29 4:46:11 AM | SOL | DOWN | 13.8 min | 33¢ | 40% | 6¢ | ❌ Lost | -$3.46 |
| 9/29 4:46:11 AM | BNB | DOWN | 13.8 min | 38¢ | 46% | 6¢ | ❌ Lost | -$3.97 |
| 9/29 4:40:57 AM | ETH | UP | 4.0 min | 27¢ | 35% | 6¢ | ❌ Lost | -$2.84 |
| 9/29 4:34:39 AM | HYPE | UP | 10.3 min | 27¢ | 33% | 5¢ | ❌ Lost | -$2.82 |
| 9/29 4:33:54 AM | ZEC | DOWN | 11.1 min | 85¢ | 90% | 5¢ | ✅ Won | $1.41 |
| 9/29 4:32:32 AM | BTC | UP | 12.4 min | 23¢ | 29% | 5¢ | ❌ Lost | -$2.43 |
| 9/29 4:32:32 AM | DOGE | UP | 12.4 min | 21¢ | 28% | 6¢ | ❌ Lost | -$2.22 |
| 9/29 4:31:47 AM | NEAR | DOWN | 13.2 min | 61¢ | 67% | 4¢ | ✅ Won | $3.73 |
| 9/29 4:31:19 AM | BNB | DOWN | 13.7 min | 50¢ | 60% | 8¢ | ✅ Won | $4.82 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
