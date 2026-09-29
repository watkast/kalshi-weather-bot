# Fair-Value Bot

*Updated Tue Sep 29, 10:56 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1218 | $21.83 | +0% | $151.61 / -$129.78 |
| 4¢+ ← live bot | 1175 | $246.70 | +5% | $234.53 / $12.17 |
| 6¢+ | 1079 | $289.45 | +6% | $228.11 / $61.34 |
| 8¢+ | 931 | $344.68 | +9% | $232.04 / $112.64 |
| 10¢+ | 786 | $281.05 | +9% | $165.94 / $115.11 |
| 15¢+ | 477 | $310.05 | +19% | $159.41 / $150.64 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1198 | 1189 | 566 (48%) | 44¢ | 53% | $192.78 | +4% | +5.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 787 | 340 (43%) | 250 / 537 | 8.6 | -$43.45 | -$228.13 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 671 | 218 (32%) | 303 / 368 | 7.3 | -$55.90 | -$333.24 | -13% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 168 | 56 (33%) | 48 / 120 | 2.0 | -$14.97 | -$98.75 | -15% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 179 | 73 (41%) | 60 / 119 | 2.0 | -$13.69 | -$28.76 | -4% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 96 | 44 (46%) | 33 / 63 | 1.5 | -$10.05 | -$13.07 | -3% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 62 | 29 (47%) | 22 / 40 | 1.5 | -$20.08 | -$37.97 | -6% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 18 | 6 (33%) | 8 / 10 | 1.6 | -$5.79 | -$14.63 | -20% |

*Model accuracy vs Kalshi's prices on the same 18,771 readings (excluding the final minute): V1 **+1.1%**, V2 **+1.4%**, 3-exchange price (V3/V4) **-0.3%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $462.04 | $525.36 | $394.02 | 0 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 795 | 667 (84%) | -$211.73 | -7% | 220,165 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.5%** over 30,982 readings from 1233 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 5461 | 2% | 4% | 5% |
| 10–20% | 2425 | 15% | 16% | 16% |
| 20–30% | 2600 | 25% | 26% | 26% |
| 30–40% | 2852 | 35% | 36% | 39% |
| 40–50% | 3033 | 45% | 48% | 52% |
| 50–60% | 3027 | 55% | 59% | 60% |
| 60–70% | 2673 | 65% | 70% | 72% |
| 70–80% | 2201 | 75% | 80% | 82% |
| 80–90% | 1932 | 85% | 88% | 86% |
| 90–100% | 4778 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 614 | 304 (50%) | 45¢ | 52% | $164.20 | +6% |
| 6–10¢ | 412 | 196 (48%) | 44¢ | 53% | $91.38 | +5% |
| 10–20¢ | 153 | 63 (41%) | 43¢ | 57% | -$52.57 | -8% |
| 20¢+ | 10 | 3 (30%) | 39¢ | 68% | -$10.23 | -25% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1060 | 510 (48%) | 45¢ | 54% | $158.21 | +3% |
| 5–10 min | 118 | 51 (43%) | 38¢ | 47% | $45.91 | +10% |
| 2–5 min | 9 | 4 (44%) | 55¢ | 64% | -$10.94 | -21% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 154 | 31 (20%) | 18¢ | 27% | $9.08 | +3% |
| Toss-up (25–75¢) | 945 | 458 (48%) | 45¢ | 54% | $158.56 | +4% |
| Favorite (75–95¢) | 90 | 77 (86%) | 82¢ | 89% | $25.14 | +3% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 135 | 69 (51%) | 44¢ | 54% | $80.84 | +13% |
| XRP | 134 | 65 (49%) | 45¢ | 53% | $25.68 | +4% |
| ETH | 134 | 58 (43%) | 45¢ | 54% | -$47.43 | -8% |
| NEAR | 132 | 66 (50%) | 47¢ | 55% | $24.03 | +4% |
| HYPE | 132 | 57 (43%) | 44¢ | 53% | -$28.67 | -5% |
| SOL | 131 | 67 (51%) | 42¢ | 50% | $95.13 | +17% |
| DOGE | 131 | 59 (45%) | 43¢ | 52% | $1.40 | +0% |
| ZEC | 130 | 57 (44%) | 41¢ | 50% | $19.31 | +4% |
| BTC | 130 | 68 (52%) | 49¢ | 57% | $22.49 | +3% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 10:55:14 AM | NEAR | UP | 4.8 min | 12¢ | 17% | 4¢ | Open | — |
| 9/29 10:52:07 AM | ZEC | DOWN | 7.9 min | 36¢ | 48% | 11¢ | Open | — |
| 9/29 10:52:00 AM | BTC | UP | 8.0 min | 38¢ | 46% | 6¢ | Open | — |
| 9/29 10:46:51 AM | SOL | DOWN | 13.2 min | 51¢ | 60% | 7¢ | Open | — |
| 9/29 10:46:34 AM | XRP | DOWN | 13.4 min | 44¢ | 50% | 4¢ | Open | — |
| 9/29 10:46:17 AM | BNB | DOWN | 13.7 min | 63¢ | 79% | 15¢ | Open | — |
| 9/29 10:46:06 AM | HYPE | DOWN | 13.9 min | 79¢ | 85% | 4¢ | Open | — |
| 9/29 10:46:06 AM | ETH | DOWN | 13.9 min | 67¢ | 75% | 6¢ | Open | — |
| 9/29 10:46:06 AM | DOGE | DOWN | 13.9 min | 76¢ | 84% | 7¢ | Open | — |
| 9/29 10:39:30 AM | NEAR | DOWN | 5.5 min | 14¢ | 20% | 5¢ | ✅ Won | $8.51 |
| 9/29 10:39:28 AM | ZEC | UP | 5.5 min | 30¢ | 37% | 5¢ | ❌ Lost | -$3.17 |
| 9/29 10:38:44 AM | ETH | DOWN | 6.2 min | 50¢ | 56% | 4¢ | ✅ Won | $4.82 |
| 9/29 10:38:40 AM | BNB | DOWN | 6.3 min | 63¢ | 71% | 6¢ | ✅ Won | $3.53 |
| 9/29 10:38:26 AM | DOGE | DOWN | 6.5 min | 45¢ | 57% | 10¢ | ✅ Won | $5.32 |
| 9/29 10:37:05 AM | SOL | DOWN | 7.9 min | 31¢ | 39% | 7¢ | ✅ Won | $6.77 |
| 9/29 10:36:52 AM | BTC | UP | 8.1 min | 45¢ | 51% | 5¢ | ❌ Lost | -$4.68 |
| 9/29 10:36:35 AM | HYPE | DOWN | 8.4 min | 85¢ | 91% | 4¢ | ✅ Won | $1.37 |
| 9/29 10:36:13 AM | XRP | DOWN | 8.8 min | 77¢ | 83% | 5¢ | ✅ Won | $2.15 |
| 9/29 8:21:45 AM | NEAR | UP | 8.2 min | 94¢ | 99% | 4¢ | ✅ Won | $0.56 |
| 9/29 8:20:10 AM | DOGE | DOWN | 9.8 min | 14¢ | 21% | 6¢ | ❌ Lost | -$1.49 |
| 9/29 8:18:13 AM | HYPE | DOWN | 11.8 min | 19¢ | 27% | 7¢ | ❌ Lost | -$2.01 |
| 9/29 8:17:28 AM | XRP | DOWN | 12.5 min | 30¢ | 36% | 5¢ | ❌ Lost | -$3.15 |
| 9/29 8:17:12 AM | BNB | DOWN | 12.8 min | 61¢ | 72% | 9¢ | ❌ Lost | -$6.27 |
| 9/29 8:17:02 AM | BTC | DOWN | 12.9 min | 62¢ | 70% | 6¢ | ❌ Lost | -$6.37 |
| 9/29 8:16:52 AM | SOL | UP | 13.1 min | 33¢ | 40% | 5¢ | ✅ Won | $6.56 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
