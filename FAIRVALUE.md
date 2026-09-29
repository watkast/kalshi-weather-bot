# Fair-Value Bot

*Updated Tue Sep 29, 3:01 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **4¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1012 | $146.07 | +3% | $145.29 / $0.78 |
| 4¢+ ← live bot | 979 | $346.74 | +8% | $170.46 / $176.28 |
| 6¢+ | 902 | $324.36 | +8% | $196.07 / $128.29 |
| 8¢+ | 777 | $305.39 | +10% | $190.37 / $115.02 |
| 10¢+ | 663 | $214.38 | +8% | $194.96 / $19.42 |
| 15¢+ | 398 | $209.86 | +16% | $196.08 / $13.78 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 989 | 987 | 486 (49%) | 45¢ | 53% | $283.90 | +6% | +6.5¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 585 | 260 (44%) | 189 / 396 | 8.5 | -$37.76 | -$137.01 | -5% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 508 | 171 (34%) | 235 / 273 | 7.4 | -$55.90 | -$224.22 | -12% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 125 | 40 (32%) | 38 / 87 | 2.0 | -$14.97 | -$100.58 | -20% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 75% of orders | 133 | 56 (42%) | 49 / 84 | 2.0 | -$13.69 | -$2.10 | -0% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 64 | 29 (45%) | 23 / 41 | 1.6 | -$10.05 | -$14.18 | -5% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 32 | 15 (47%) | 12 / 20 | 1.5 | -$19.37 | -$20.14 | -6% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 9 | 2 (22%) | 4 / 5 | 1.5 | -$5.79 | -$12.92 | -39% |

*Model accuracy vs Kalshi's prices on the same 14,137 readings (excluding the final minute): V1 **+1.3%**, V2 **+2.0%**, 3-exchange price (V3/V4) **-0.2%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $479.87 | $525.36 | $394.02 | 0 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 593 | 465 (78%) | -$120.61 | -6% | 168,323 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.5%** over 26,004 readings from 1026 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4644 | 2% | 4% | 6% |
| 10–20% | 2074 | 15% | 16% | 17% |
| 20–30% | 2249 | 25% | 26% | 27% |
| 30–40% | 2423 | 35% | 36% | 40% |
| 40–50% | 2558 | 45% | 47% | 53% |
| 50–60% | 2575 | 55% | 58% | 60% |
| 60–70% | 2259 | 65% | 70% | 71% |
| 70–80% | 1853 | 75% | 80% | 82% |
| 80–90% | 1595 | 85% | 87% | 85% |
| 90–100% | 3774 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 528 | 271 (51%) | 46¢ | 52% | $218.57 | +9% |
| 6–10¢ | 336 | 168 (50%) | 45¢ | 54% | $130.20 | +8% |
| 10–20¢ | 114 | 45 (39%) | 42¢ | 56% | -$51.11 | -10% |
| 20¢+ | 9 | 2 (22%) | 36¢ | 65% | -$13.76 | -41% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 893 | 448 (50%) | 45¢ | 54% | $276.57 | +7% |
| 5–10 min | 85 | 33 (39%) | 36¢ | 45% | $13.09 | +4% |
| 2–5 min | 7 | 4 (57%) | 64¢ | 72% | -$5.36 | -12% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 123 | 25 (20%) | 19¢ | 27% | $7.89 | +3% |
| Toss-up (25–75¢) | 796 | 403 (51%) | 46¢ | 54% | $251.62 | +7% |
| Favorite (75–95¢) | 68 | 58 (85%) | 81¢ | 88% | $24.39 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 112 | 58 (52%) | 43¢ | 52% | $83.71 | +17% |
| XRP | 111 | 58 (52%) | 46¢ | 54% | $48.81 | +9% |
| ETH | 111 | 49 (44%) | 46¢ | 54% | -$37.62 | -7% |
| HYPE | 110 | 47 (43%) | 43¢ | 52% | -$21.11 | -4% |
| SOL | 109 | 58 (53%) | 43¢ | 51% | $93.94 | +19% |
| NEAR | 109 | 54 (50%) | 47¢ | 55% | $10.81 | +2% |
| BTC | 109 | 62 (57%) | 50¢ | 58% | $56.49 | +10% |
| ZEC | 108 | 47 (44%) | 41¢ | 50% | $12.52 | +3% |
| DOGE | 108 | 53 (49%) | 44¢ | 52% | $36.35 | +7% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 3:01:20 AM | BNB | DOWN | 13.7 min | 52¢ | 64% | 9¢ | Open | — |
| 9/29 3:01:03 AM | ETH | UP | 13.9 min | 31¢ | 40% | 8¢ | Open | — |
| 9/29 2:54:50 AM | BTC | UP | 5.2 min | 19¢ | 27% | 7¢ | ❌ Lost | -$2.01 |
| 9/29 2:54:27 AM | ZEC | UP | 5.5 min | 24¢ | 31% | 6¢ | ❌ Lost | -$2.53 |
| 9/29 2:52:31 AM | HYPE | UP | 7.5 min | 15¢ | 25% | 9¢ | ❌ Lost | -$1.59 |
| 9/29 2:52:25 AM | SOL | UP | 7.6 min | 27¢ | 37% | 8¢ | ✅ Won | $7.16 |
| 9/29 2:52:25 AM | ETH | UP | 7.6 min | 15¢ | 26% | 10¢ | ❌ Lost | -$1.59 |
| 9/29 2:51:55 AM | XRP | DOWN | 8.1 min | 34¢ | 41% | 5¢ | ❌ Lost | -$3.55 |
| 9/29 2:51:55 AM | DOGE | DOWN | 8.1 min | 16¢ | 24% | 7¢ | ❌ Lost | -$1.70 |
| 9/29 2:51:55 AM | BNB | DOWN | 8.1 min | 56¢ | 66% | 8¢ | ✅ Won | $4.22 |
| 9/29 2:51:45 AM | NEAR | DOWN | 8.2 min | 21¢ | 26% | 4¢ | ❌ Lost | -$2.22 |
| 9/29 2:21:06 AM | ZEC | DOWN | 8.9 min | 34¢ | 47% | 12¢ | ✅ Won | $6.44 |
| 9/29 2:18:26 AM | SOL | UP | 11.6 min | 61¢ | 70% | 8¢ | ✅ Won | $3.73 |
| 9/29 2:18:26 AM | ETH | UP | 11.6 min | 52¢ | 62% | 8¢ | ✅ Won | $4.62 |
| 9/29 2:18:17 AM | BTC | UP | 11.7 min | 58¢ | 65% | 5¢ | ✅ Won | $4.02 |
| 9/29 2:18:08 AM | BNB | DOWN | 11.9 min | 25¢ | 40% | 14¢ | ❌ Lost | -$2.64 |
| 9/29 2:17:49 AM | DOGE | UP | 12.2 min | 67¢ | 74% | 5¢ | ✅ Won | $3.14 |
| 9/29 2:17:49 AM | XRP | UP | 12.2 min | 72¢ | 81% | 8¢ | ✅ Won | $2.65 |
| 9/29 2:16:47 AM | NEAR | UP | 13.2 min | 90¢ | 97% | 6¢ | ✅ Won | $0.93 |
| 9/29 2:16:47 AM | HYPE | UP | 13.2 min | 60¢ | 73% | 11¢ | ✅ Won | $3.83 |
| 9/29 2:02:08 AM | HYPE | DOWN | 12.8 min | 37¢ | 56% | 18¢ | ❌ Lost | -$3.87 |
| 9/29 2:02:08 AM | SOL | DOWN | 12.8 min | 35¢ | 44% | 7¢ | ✅ Won | $6.33 |
| 9/29 2:01:53 AM | XRP | DOWN | 13.1 min | 39¢ | 51% | 11¢ | ✅ Won | $5.93 |
| 9/29 2:01:34 AM | DOGE | UP | 13.4 min | 58¢ | 66% | 6¢ | ❌ Lost | -$5.98 |
| 9/29 2:01:34 AM | ZEC | UP | 13.4 min | 42¢ | 57% | 13¢ | ❌ Lost | -$4.38 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
