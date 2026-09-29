# Fair-Value Bot

*Updated Tue Sep 29, 7:55 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1182 | $45.41 | +1% | $126.63 / -$81.22 |
| 4¢+ ← live bot | 1139 | $275.05 | +5% | $217.84 / $57.21 |
| 6¢+ | 1046 | $314.64 | +7% | $225.28 / $89.36 |
| 8¢+ | 903 | $364.12 | +10% | $198.91 / $165.21 |
| 10¢+ | 769 | $290.32 | +10% | $161.94 / $128.38 |
| 15¢+ | 467 | $277.80 | +18% | $163.55 / $114.25 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1162 | 1153 | 547 (47%) | 44¢ | 53% | $200.89 | +4% | +5.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 751 | 321 (43%) | 241 / 510 | 8.5 | -$43.45 | -$220.02 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 646 | 214 (33%) | 294 / 352 | 7.3 | -$55.90 | -$287.76 | -12% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 160 | 51 (32%) | 47 / 113 | 2.0 | -$14.97 | -$108.19 | -18% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 75% of orders | 171 | 68 (40%) | 56 / 115 | 2.0 | -$13.69 | -$39.27 | -5% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 89 | 40 (45%) | 31 / 58 | 1.5 | -$10.05 | -$14.64 | -4% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 55 | 25 (45%) | 20 / 35 | 1.4 | -$20.08 | -$43.95 | -8% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 15 | 5 (33%) | 6 / 9 | 1.7 | -$5.79 | -$10.65 | -18% |

*Model accuracy vs Kalshi's prices on the same 18,049 readings (excluding the final minute): V1 **+0.8%**, V2 **+1.2%**, 3-exchange price (V3/V4) **-0.7%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $456.06 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 759 | 631 (83%) | -$203.62 | -7% | 221,531 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.2%** over 30,188 readings from 1197 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 5233 | 2% | 4% | 5% |
| 10–20% | 2379 | 15% | 16% | 16% |
| 20–30% | 2559 | 25% | 26% | 26% |
| 30–40% | 2776 | 35% | 36% | 38% |
| 40–50% | 2958 | 45% | 48% | 52% |
| 50–60% | 2964 | 55% | 59% | 61% |
| 60–70% | 2625 | 65% | 70% | 72% |
| 70–80% | 2159 | 75% | 80% | 82% |
| 80–90% | 1889 | 85% | 88% | 86% |
| 90–100% | 4646 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 597 | 293 (49%) | 45¢ | 51% | $151.86 | +5% |
| 6–10¢ | 402 | 191 (48%) | 44¢ | 53% | $94.60 | +5% |
| 10–20¢ | 144 | 60 (42%) | 43¢ | 57% | -$35.34 | -6% |
| 20¢+ | 10 | 3 (30%) | 39¢ | 68% | -$10.23 | -25% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1035 | 499 (48%) | 45¢ | 53% | $190.01 | +4% |
| 5–10 min | 107 | 43 (40%) | 37¢ | 46% | $22.22 | +5% |
| 2–5 min | 9 | 4 (44%) | 55¢ | 64% | -$10.94 | -21% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 150 | 30 (20%) | 18¢ | 27% | $6.60 | +2% |
| Toss-up (25–75¢) | 921 | 448 (49%) | 45¢ | 54% | $180.18 | +4% |
| Favorite (75–95¢) | 82 | 69 (84%) | 81¢ | 89% | $14.11 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 131 | 67 (51%) | 43¢ | 53% | $88.14 | +15% |
| XRP | 130 | 63 (48%) | 45¢ | 53% | $27.34 | +5% |
| ETH | 130 | 57 (44%) | 45¢ | 53% | -$37.18 | -6% |
| NEAR | 128 | 63 (49%) | 47¢ | 54% | $14.91 | +2% |
| HYPE | 128 | 54 (42%) | 43¢ | 52% | -$34.37 | -6% |
| SOL | 127 | 64 (50%) | 42¢ | 50% | $82.83 | +15% |
| DOGE | 127 | 57 (45%) | 43¢ | 52% | $2.20 | +0% |
| ZEC | 126 | 55 (44%) | 41¢ | 50% | $19.01 | +4% |
| BTC | 126 | 67 (53%) | 49¢ | 57% | $38.01 | +6% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 7:47:41 AM | ZEC | DOWN | 12.3 min | 54¢ | 61% | 5¢ | Open | — |
| 9/29 7:47:41 AM | BTC | DOWN | 12.3 min | 57¢ | 72% | 13¢ | Open | — |
| 9/29 7:47:41 AM | DOGE | DOWN | 12.3 min | 58¢ | 71% | 12¢ | Open | — |
| 9/29 7:47:41 AM | BNB | DOWN | 12.3 min | 56¢ | 71% | 13¢ | Open | — |
| 9/29 7:47:41 AM | HYPE | DOWN | 12.3 min | 47¢ | 63% | 15¢ | Open | — |
| 9/29 7:47:41 AM | ETH | DOWN | 12.3 min | 56¢ | 71% | 13¢ | Open | — |
| 9/29 7:47:41 AM | XRP | DOWN | 12.3 min | 52¢ | 68% | 14¢ | Open | — |
| 9/29 7:47:13 AM | SOL | DOWN | 12.8 min | 67¢ | 73% | 4¢ | Open | — |
| 9/29 7:46:46 AM | NEAR | DOWN | 13.2 min | 40¢ | 46% | 5¢ | Open | — |
| 9/29 7:32:12 AM | HYPE | DOWN | 12.8 min | 86¢ | 93% | 6¢ | ✅ Won | $1.31 |
| 9/29 7:31:58 AM | ZEC | DOWN | 13.0 min | 87¢ | 96% | 8¢ | ❌ Lost | -$8.78 |
| 9/29 7:31:58 AM | NEAR | DOWN | 13.0 min | 85¢ | 91% | 5¢ | ❌ Lost | -$8.59 |
| 9/29 7:31:58 AM | BNB | DOWN | 13.0 min | 82¢ | 94% | 10¢ | ✅ Won | $1.69 |
| 9/29 7:31:58 AM | ETH | DOWN | 13.0 min | 79¢ | 94% | 14¢ | ✅ Won | $1.98 |
| 9/29 7:31:43 AM | DOGE | UP | 13.3 min | 19¢ | 28% | 7¢ | ❌ Lost | -$2.01 |
| 9/29 7:31:43 AM | XRP | UP | 13.3 min | 32¢ | 48% | 14¢ | ✅ Won | $6.64 |
| 9/29 7:31:04 AM | BTC | DOWN | 13.9 min | 63¢ | 88% | 23¢ | ✅ Won | $3.53 |
| 9/29 7:31:04 AM | SOL | DOWN | 13.9 min | 65¢ | 82% | 15¢ | ✅ Won | $3.34 |
| 9/29 7:24:11 AM | BTC | DOWN | 5.8 min | 27¢ | 33% | 4¢ | ✅ Won | $7.16 |
| 9/29 7:22:07 AM | SOL | DOWN | 7.9 min | 30¢ | 36% | 5¢ | ❌ Lost | -$3.13 |
| 9/29 7:17:33 AM | ZEC | DOWN | 12.4 min | 40¢ | 46% | 5¢ | ✅ Won | $5.83 |
| 9/29 7:17:33 AM | BNB | DOWN | 12.4 min | 31¢ | 46% | 13¢ | ❌ Lost | -$3.25 |
| 9/29 7:17:33 AM | HYPE | DOWN | 12.4 min | 34¢ | 42% | 6¢ | ❌ Lost | -$3.56 |
| 9/29 7:16:59 AM | DOGE | DOWN | 13.0 min | 42¢ | 51% | 8¢ | ❌ Lost | -$4.38 |
| 9/29 7:16:59 AM | XRP | DOWN | 13.0 min | 43¢ | 53% | 8¢ | ❌ Lost | -$4.48 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
