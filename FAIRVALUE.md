# Fair-Value Bot

*Updated Tue Sep 29, 12:23 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 923 | $98.08 | +2% | $144.11 / -$46.03 |
| 4¢+ ← live bot | 892 | $297.11 | +7% | $202.92 / $94.19 |
| 6¢+ | 819 | $326.64 | +9% | $222.90 / $103.74 |
| 8¢+ | 709 | $337.22 | +12% | $192.45 / $144.77 |
| 10¢+ | 608 | $269.97 | +12% | $205.55 / $64.42 |
| 15¢+ | 360 | $230.88 | +19% | $172.69 / $58.19 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 906 | 897 | 449 (50%) | 45¢ | 53% | $306.21 | +7% | +7.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 495 | 223 (45%) | 148 / 347 | 8.4 | -$37.76 | -$114.70 | -5% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 437 | 145 (33%) | 194 / 243 | 7.4 | -$55.90 | -$222.63 | -13% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 105 | 35 (33%) | 35 / 70 | 1.9 | -$14.97 | -$65.37 | -16% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 73% of orders | 113 | 47 (42%) | 41 / 72 | 2.0 | -$13.69 | -$21.28 | -4% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 47 | 22 (47%) | 16 / 31 | 1.5 | -$10.05 | -$11.55 | -6% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 17 | 9 (53%) | 6 / 11 | 1.5 | -$10.39 | -$0.56 | -0% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 4 | 0 (0%) | 1 / 3 | 1.3 | -$5.79 | -$11.78 | -100% |

*Model accuracy vs Kalshi's prices on the same 12,149 readings (excluding the final minute): V1 **+2.0%**, V2 **+2.2%**, 3-exchange price (V3/V4) **+0.6%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $499.44 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 503 | 375 (75%) | -$98.30 | -6% | 144,735 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.9%** over 23,870 readings from 936 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4457 | 2% | 4% | 6% |
| 10–20% | 1915 | 15% | 16% | 17% |
| 20–30% | 2064 | 25% | 26% | 27% |
| 30–40% | 2264 | 35% | 36% | 40% |
| 40–50% | 2328 | 45% | 47% | 52% |
| 50–60% | 2336 | 55% | 59% | 60% |
| 60–70% | 2035 | 65% | 70% | 70% |
| 70–80% | 1675 | 75% | 80% | 80% |
| 80–90% | 1455 | 85% | 88% | 84% |
| 90–100% | 3341 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 495 | 255 (52%) | 46¢ | 52% | $207.13 | +9% |
| 6–10¢ | 298 | 151 (51%) | 45¢ | 54% | $126.22 | +9% |
| 10–20¢ | 97 | 41 (42%) | 43¢ | 57% | -$19.75 | -5% |
| 20¢+ | 7 | 2 (29%) | 38¢ | 66% | -$7.39 | -27% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 826 | 418 (51%) | 46¢ | 54% | $288.56 | +7% |
| 5–10 min | 64 | 27 (42%) | 38¢ | 46% | $19.61 | +8% |
| 2–5 min | 5 | 3 (60%) | 62¢ | 70% | -$1.56 | -5% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 103 | 21 (20%) | 19¢ | 27% | $3.00 | +1% |
| Toss-up (25–75¢) | 734 | 377 (51%) | 46¢ | 54% | $284.47 | +8% |
| Favorite (75–95¢) | 60 | 51 (85%) | 81¢ | 88% | $18.74 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 102 | 54 (53%) | 43¢ | 53% | $86.83 | +19% |
| XRP | 101 | 54 (53%) | 47¢ | 55% | $49.73 | +10% |
| ETH | 101 | 44 (44%) | 47¢ | 55% | -$47.42 | -10% |
| HYPE | 100 | 45 (45%) | 44¢ | 52% | -$0.94 | -0% |
| SOL | 99 | 53 (54%) | 44¢ | 52% | $80.48 | +18% |
| NEAR | 99 | 50 (51%) | 47¢ | 54% | $21.12 | +4% |
| BTC | 99 | 55 (56%) | 50¢ | 58% | $36.75 | +7% |
| ZEC | 98 | 43 (44%) | 40¢ | 49% | $17.89 | +4% |
| DOGE | 98 | 51 (52%) | 44¢ | 52% | $61.77 | +14% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 12:22:15 AM | NEAR | UP | 7.7 min | 13¢ | 20% | 6¢ | Open | — |
| 9/29 12:19:33 AM | DOGE | UP | 10.4 min | 13¢ | 20% | 6¢ | Open | — |
| 9/29 12:19:22 AM | ZEC | UP | 10.6 min | 14¢ | 20% | 5¢ | Open | — |
| 9/29 12:18:38 AM | SOL | UP | 11.4 min | 10¢ | 17% | 7¢ | Open | — |
| 9/29 12:18:38 AM | HYPE | UP | 11.4 min | 11¢ | 22% | 10¢ | Open | — |
| 9/29 12:18:04 AM | BNB | UP | 11.9 min | 18¢ | 24% | 5¢ | Open | — |
| 9/29 12:17:55 AM | ETH | UP | 12.1 min | 18¢ | 26% | 7¢ | Open | — |
| 9/29 12:17:55 AM | XRP | UP | 12.1 min | 14¢ | 23% | 8¢ | Open | — |
| 9/29 12:16:26 AM | BTC | UP | 13.6 min | 32¢ | 39% | 6¢ | Open | — |
| 9/29 12:05:22 AM | DOGE | DOWN | 9.6 min | 21¢ | 31% | 9¢ | ❌ Lost | -$2.22 |
| 9/29 12:04:37 AM | SOL | UP | 10.4 min | 71¢ | 84% | 12¢ | ✅ Won | $2.75 |
| 9/29 12:04:37 AM | BTC | UP | 10.4 min | 79¢ | 88% | 8¢ | ✅ Won | $1.98 |
| 9/29 12:04:37 AM | XRP | UP | 10.4 min | 72¢ | 82% | 9¢ | ✅ Won | $2.65 |
| 9/29 12:04:01 AM | ETH | DOWN | 11.0 min | 23¢ | 33% | 9¢ | ❌ Lost | -$2.43 |
| 9/29 12:03:29 AM | HYPE | DOWN | 11.5 min | 27¢ | 42% | 13¢ | ❌ Lost | -$2.84 |
| 9/29 12:02:08 AM | ZEC | DOWN | 12.8 min | 43¢ | 50% | 5¢ | ❌ Lost | -$4.48 |
| 9/29 12:01:51 AM | BNB | DOWN | 13.1 min | 42¢ | 49% | 5¢ | ❌ Lost | -$4.38 |
| 9/29 12:01:19 AM | NEAR | DOWN | 13.7 min | 43¢ | 57% | 12¢ | ❌ Lost | -$4.48 |
| 9/28 11:50:07 PM | NEAR | DOWN | 9.9 min | 32¢ | 49% | 16¢ | ❌ Lost | -$3.33 |
| 9/28 11:49:00 PM | BTC | UP | 11.0 min | 38¢ | 45% | 5¢ | ✅ Won | $6.03 |
| 9/28 11:48:40 PM | BNB | DOWN | 11.3 min | 44¢ | 58% | 12¢ | ❌ Lost | -$4.62 |
| 9/28 11:48:21 PM | ETH | DOWN | 11.6 min | 58¢ | 65% | 5¢ | ❌ Lost | -$5.98 |
| 9/28 11:47:53 PM | ZEC | UP | 12.1 min | 28¢ | 34% | 5¢ | ✅ Won | $7.05 |
| 9/28 11:47:25 PM | HYPE | UP | 12.6 min | 21¢ | 27% | 5¢ | ✅ Won | $7.78 |
| 9/28 11:47:03 PM | SOL | UP | 12.9 min | 31¢ | 38% | 5¢ | ✅ Won | $6.75 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
