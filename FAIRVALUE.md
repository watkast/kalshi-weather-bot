# Fair-Value Bot

*Updated Tue Sep 29, 6:04 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1120 | $41.88 | +1% | $157.27 / -$115.39 |
| 4¢+ ← live bot | 1080 | $277.81 | +6% | $203.30 / $74.51 |
| 6¢+ | 991 | $277.86 | +7% | $227.15 / $50.71 |
| 8¢+ | 855 | $304.42 | +9% | $185.54 / $118.88 |
| 10¢+ | 729 | $223.73 | +8% | $165.88 / $57.85 |
| 15¢+ | 447 | $229.63 | +15% | $165.62 / $64.01 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1096 | 1090 | 515 (47%) | 44¢ | 53% | $158.56 | +3% | +5.5¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 688 | 289 (42%) | 223 / 465 | 8.5 | -$43.45 | -$262.35 | -8% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 590 | 197 (33%) | 264 / 326 | 7.3 | -$55.90 | -$260.10 | -12% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 146 | 47 (32%) | 42 / 104 | 1.9 | -$14.97 | -$91.18 | -16% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 157 | 62 (39%) | 53 / 104 | 2.0 | -$13.69 | -$39.19 | -6% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 78 | 35 (45%) | 27 / 51 | 1.5 | -$10.05 | -$17.39 | -5% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 46 | 21 (46%) | 16 / 30 | 1.5 | -$20.08 | -$40.54 | -9% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 13 | 4 (31%) | 5 / 8 | 1.6 | -$5.79 | -$9.99 | -20% |

*Model accuracy vs Kalshi's prices on the same 16,642 readings (excluding the final minute): V1 **+0.9%**, V2 **+1.5%**, 3-exchange price (V3/V4) **-0.6%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $459.47 | $525.36 | $394.02 | 0 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 696 | 568 (82%) | -$245.95 | -10% | 216,360 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.3%** over 28,682 readings from 1134 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4995 | 2% | 4% | 6% |
| 10–20% | 2238 | 15% | 16% | 16% |
| 20–30% | 2419 | 25% | 26% | 26% |
| 30–40% | 2639 | 35% | 36% | 39% |
| 40–50% | 2784 | 45% | 48% | 53% |
| 50–60% | 2807 | 55% | 59% | 61% |
| 60–70% | 2458 | 65% | 70% | 73% |
| 70–80% | 2061 | 75% | 80% | 83% |
| 80–90% | 1820 | 85% | 88% | 86% |
| 90–100% | 4461 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 573 | 283 (49%) | 45¢ | 52% | $150.99 | +6% |
| 6–10¢ | 378 | 181 (48%) | 44¢ | 53% | $102.52 | +6% |
| 10–20¢ | 130 | 49 (38%) | 42¢ | 56% | -$81.19 | -14% |
| 20¢+ | 9 | 2 (22%) | 36¢ | 65% | -$13.76 | -41% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 981 | 472 (48%) | 45¢ | 53% | $163.78 | +4% |
| 5–10 min | 99 | 38 (38%) | 37¢ | 46% | $3.38 | +1% |
| 2–5 min | 8 | 4 (50%) | 59¢ | 67% | -$8.20 | -17% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 145 | 27 (19%) | 18¢ | 27% | -$13.66 | -5% |
| Toss-up (25–75¢) | 870 | 423 (49%) | 45¢ | 54% | $138.53 | +3% |
| Favorite (75–95¢) | 75 | 65 (87%) | 81¢ | 88% | $33.69 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 124 | 63 (51%) | 43¢ | 53% | $78.07 | +14% |
| XRP | 123 | 60 (49%) | 45¢ | 53% | $27.99 | +5% |
| ETH | 123 | 53 (43%) | 45¢ | 53% | -$42.95 | -7% |
| NEAR | 121 | 59 (49%) | 46¢ | 54% | $10.02 | +2% |
| HYPE | 121 | 50 (41%) | 43¢ | 52% | -$36.55 | -7% |
| SOL | 120 | 61 (51%) | 43¢ | 51% | $79.25 | +15% |
| DOGE | 120 | 55 (46%) | 44¢ | 52% | $6.70 | +1% |
| ZEC | 119 | 50 (42%) | 41¢ | 49% | -$0.58 | -0% |
| BTC | 119 | 64 (54%) | 49¢ | 57% | $36.61 | +6% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 6:03:49 AM | ETH | UP | 11.2 min | 38¢ | 47% | 7¢ | Open | — |
| 9/29 6:03:34 AM | HYPE | DOWN | 11.4 min | 44¢ | 52% | 6¢ | Open | — |
| 9/29 6:03:14 AM | DOGE | DOWN | 11.8 min | 36¢ | 43% | 5¢ | Open | — |
| 9/29 6:02:08 AM | NEAR | DOWN | 12.8 min | 52¢ | 59% | 6¢ | Open | — |
| 9/29 6:01:24 AM | BNB | DOWN | 13.6 min | 52¢ | 72% | 18¢ | Open | — |
| 9/29 6:01:24 AM | ZEC | DOWN | 13.6 min | 15¢ | 23% | 7¢ | Open | — |
| 9/29 5:51:42 AM | XRP | UP | 8.3 min | 91¢ | 97% | 5¢ | ✅ Won | $0.82 |
| 9/29 5:51:16 AM | ETH | UP | 8.7 min | 80¢ | 98% | 17¢ | ✅ Won | $1.88 |
| 9/29 5:50:11 AM | SOL | UP | 9.8 min | 88¢ | 98% | 10¢ | ✅ Won | $1.12 |
| 9/29 5:47:16 AM | BTC | DOWN | 12.7 min | 26¢ | 33% | 5¢ | ❌ Lost | -$2.74 |
| 9/29 5:46:54 AM | DOGE | DOWN | 13.1 min | 26¢ | 34% | 7¢ | ❌ Lost | -$2.74 |
| 9/29 5:46:39 AM | NEAR | DOWN | 13.3 min | 40¢ | 47% | 6¢ | ❌ Lost | -$4.17 |
| 9/29 5:46:32 AM | ZEC | DOWN | 13.4 min | 18¢ | 28% | 10¢ | ❌ Lost | -$1.89 |
| 9/29 5:46:24 AM | HYPE | DOWN | 13.6 min | 21¢ | 28% | 5¢ | ❌ Lost | -$2.22 |
| 9/29 5:46:24 AM | BNB | DOWN | 13.6 min | 30¢ | 45% | 14¢ | ❌ Lost | -$3.15 |
| 9/29 5:32:58 AM | BTC | UP | 12.0 min | 92¢ | 97% | 5¢ | ✅ Won | $0.78 |
| 9/29 5:32:48 AM | ETH | DOWN | 12.2 min | 11¢ | 19% | 8¢ | ❌ Lost | -$1.17 |
| 9/29 5:32:48 AM | NEAR | DOWN | 12.2 min | 17¢ | 28% | 10¢ | ❌ Lost | -$1.80 |
| 9/29 5:31:57 AM | ZEC | DOWN | 13.0 min | 42¢ | 52% | 8¢ | ❌ Lost | -$4.38 |
| 9/29 5:31:57 AM | SOL | DOWN | 13.0 min | 32¢ | 40% | 7¢ | ❌ Lost | -$3.36 |
| 9/29 5:31:38 AM | XRP | DOWN | 13.4 min | 25¢ | 32% | 6¢ | ❌ Lost | -$2.64 |
| 9/29 5:31:23 AM | DOGE | DOWN | 13.6 min | 29¢ | 38% | 8¢ | ❌ Lost | -$3.05 |
| 9/29 5:31:16 AM | BNB | DOWN | 13.7 min | 30¢ | 48% | 17¢ | ❌ Lost | -$3.15 |
| 9/29 5:21:38 AM | BTC | DOWN | 8.3 min | 36¢ | 51% | 13¢ | ❌ Lost | -$3.77 |
| 9/29 5:19:39 AM | ETH | DOWN | 10.3 min | 36¢ | 42% | 4¢ | ❌ Lost | -$3.77 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
