# Fair-Value Bot

*Updated Tue Sep 29, 11:47 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1254 | $68.25 | +1% | $181.84 / -$113.59 |
| 4¢+ ← live bot | 1211 | $290.69 | +5% | $287.05 / $3.64 |
| 6¢+ | 1112 | $315.30 | +7% | $292.49 / $22.81 |
| 8¢+ | 961 | $379.44 | +10% | $247.61 / $131.83 |
| 10¢+ | 812 | $284.25 | +9% | $166.18 / $118.07 |
| 15¢+ | 491 | $316.73 | +19% | $175.67 / $141.06 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1228 | 1223 | 583 (48%) | 44¢ | 53% | $215.46 | +4% | +5.3¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 821 | 357 (43%) | 259 / 562 | 8.6 | -$43.45 | -$205.45 | -5% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 698 | 225 (32%) | 310 / 388 | 7.3 | -$55.90 | -$347.39 | -13% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 176 | 59 (34%) | 49 / 127 | 2.0 | -$14.97 | -$99.94 | -14% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 187 | 78 (42%) | 62 / 125 | 2.0 | -$13.69 | -$19.92 | -2% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 101 | 48 (48%) | 35 / 66 | 1.5 | -$10.05 | $2.60 | +1% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 67 | 33 (49%) | 24 / 43 | 1.5 | -$20.08 | $6.59 | +1% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 19 | 7 (37%) | 8 / 11 | 1.6 | -$5.79 | -$8.80 | -11% |

*Model accuracy vs Kalshi's prices on the same 19,662 readings (excluding the final minute): V1 **+1.2%**, V2 **+1.4%**, 3-exchange price (V3/V4) **-0.2%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $506.60 | $525.36 | $394.02 | 0 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 829 | 701 (85%) | -$189.05 | -6% | 225,840 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.5%** over 31,945 readings from 1269 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 5602 | 2% | 4% | 5% |
| 10–20% | 2519 | 15% | 16% | 16% |
| 20–30% | 2680 | 25% | 26% | 26% |
| 30–40% | 2975 | 35% | 36% | 39% |
| 40–50% | 3200 | 45% | 48% | 53% |
| 50–60% | 3137 | 55% | 59% | 61% |
| 60–70% | 2785 | 65% | 70% | 72% |
| 70–80% | 2254 | 75% | 80% | 82% |
| 80–90% | 1969 | 85% | 88% | 86% |
| 90–100% | 4824 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 627 | 311 (50%) | 45¢ | 52% | $186.43 | +6% |
| 6–10¢ | 430 | 205 (48%) | 44¢ | 53% | $95.38 | +5% |
| 10–20¢ | 156 | 64 (41%) | 43¢ | 57% | -$56.12 | -8% |
| 20¢+ | 10 | 3 (30%) | 39¢ | 68% | -$10.23 | -25% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1079 | 523 (48%) | 45¢ | 54% | $191.59 | +4% |
| 5–10 min | 131 | 54 (41%) | 38¢ | 46% | $27.79 | +5% |
| 2–5 min | 11 | 5 (45%) | 48¢ | 55% | -$3.52 | -7% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 160 | 32 (20%) | 18¢ | 27% | $9.48 | +3% |
| Toss-up (25–75¢) | 970 | 471 (49%) | 45¢ | 54% | $174.75 | +4% |
| Favorite (75–95¢) | 93 | 80 (86%) | 82¢ | 89% | $31.23 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 139 | 72 (52%) | 44¢ | 54% | $91.05 | +14% |
| XRP | 138 | 68 (49%) | 45¢ | 53% | $38.81 | +6% |
| ETH | 138 | 60 (43%) | 45¢ | 54% | -$46.86 | -7% |
| HYPE | 136 | 60 (44%) | 44¢ | 53% | -$16.90 | -3% |
| SOL | 135 | 68 (50%) | 42¢ | 50% | $91.65 | +16% |
| NEAR | 135 | 67 (50%) | 46¢ | 54% | $26.78 | +4% |
| ZEC | 134 | 58 (43%) | 41¢ | 50% | $8.22 | +1% |
| DOGE | 134 | 60 (45%) | 44¢ | 52% | -$4.47 | -1% |
| BTC | 134 | 70 (52%) | 49¢ | 57% | $27.18 | +4% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 11:46:13 AM | BNB | DOWN | 13.8 min | 49¢ | 58% | 7¢ | Open | — |
| 9/29 11:46:13 AM | NEAR | DOWN | 13.8 min | 45¢ | 51% | 5¢ | Open | — |
| 9/29 11:46:13 AM | BTC | DOWN | 13.8 min | 51¢ | 57% | 4¢ | Open | — |
| 9/29 11:46:13 AM | SOL | DOWN | 13.8 min | 45¢ | 58% | 11¢ | Open | — |
| 9/29 11:46:11 AM | ETH | DOWN | 13.8 min | 44¢ | 54% | 8¢ | Open | — |
| 9/29 11:39:10 AM | BTC | DOWN | 5.8 min | 56¢ | 67% | 9¢ | ❌ Lost | -$5.78 |
| 9/29 11:34:27 AM | ZEC | UP | 10.5 min | 80¢ | 88% | 7¢ | ✅ Won | $1.88 |
| 9/29 11:33:06 AM | XRP | DOWN | 11.9 min | 37¢ | 45% | 7¢ | ✅ Won | $6.13 |
| 9/29 11:32:30 AM | NEAR | DOWN | 12.5 min | 34¢ | 42% | 6¢ | ❌ Lost | -$3.56 |
| 9/29 11:31:45 AM | SOL | DOWN | 13.2 min | 33¢ | 43% | 8¢ | ❌ Lost | -$3.46 |
| 9/29 11:31:38 AM | HYPE | DOWN | 13.3 min | 41¢ | 48% | 5¢ | ✅ Won | $5.73 |
| 9/29 11:31:38 AM | DOGE | DOWN | 13.3 min | 41¢ | 49% | 6¢ | ❌ Lost | -$4.27 |
| 9/29 11:31:32 AM | ETH | DOWN | 13.4 min | 36¢ | 47% | 9¢ | ✅ Won | $6.23 |
| 9/29 11:31:10 AM | BNB | DOWN | 13.8 min | 32¢ | 44% | 11¢ | ✅ Won | $6.64 |
| 9/29 11:25:17 AM | HYPE | UP | 4.7 min | 12¢ | 19% | 6¢ | ❌ Lost | -$1.32 |
| 9/29 11:23:49 AM | SOL | UP | 6.2 min | 12¢ | 18% | 6¢ | ❌ Lost | -$1.28 |
| 9/29 11:20:33 AM | ZEC | DOWN | 9.4 min | 51¢ | 59% | 6¢ | ❌ Lost | -$5.28 |
| 9/29 11:20:25 AM | BTC | UP | 9.6 min | 46¢ | 54% | 6¢ | ✅ Won | $5.22 |
| 9/29 11:20:18 AM | ETH | DOWN | 9.7 min | 61¢ | 69% | 7¢ | ✅ Won | $3.73 |
| 9/29 11:19:22 AM | XRP | DOWN | 10.6 min | 54¢ | 63% | 7¢ | ✅ Won | $4.42 |
| 9/29 11:18:16 AM | BNB | DOWN | 11.7 min | 63¢ | 71% | 6¢ | ✅ Won | $3.53 |
| 9/29 11:09:54 AM | BTC | DOWN | 5.1 min | 7¢ | 12% | 5¢ | ❌ Lost | -$0.78 |
| 9/29 11:08:57 AM | NEAR | UP | 6.0 min | 23¢ | 29% | 4¢ | ❌ Lost | -$2.43 |
| 9/29 11:08:03 AM | ZEC | DOWN | 7.0 min | 38¢ | 45% | 5¢ | ❌ Lost | -$3.97 |
| 9/29 11:06:23 AM | ETH | DOWN | 8.6 min | 24¢ | 34% | 9¢ | ❌ Lost | -$2.53 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
