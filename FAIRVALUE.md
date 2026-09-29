# Fair-Value Bot

*Updated Tue Sep 29, 1:54 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 976 | $72.94 | +2% | $126.66 / -$53.72 |
| 4¢+ ← live bot | 944 | $288.22 | +7% | $178.10 / $110.12 |
| 6¢+ | 868 | $297.50 | +8% | $203.65 / $93.85 |
| 8¢+ | 748 | $299.27 | +10% | $200.76 / $98.51 |
| 10¢+ | 640 | $201.67 | +8% | $203.97 / -$2.30 |
| 15¢+ | 384 | $196.18 | +15% | $189.09 / $7.09 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 959 | 951 | 467 (49%) | 45¢ | 53% | $259.67 | +6% | +6.5¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 549 | 241 (44%) | 170 / 379 | 8.4 | -$37.76 | -$161.24 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 485 | 166 (34%) | 229 / 256 | 7.5 | -$55.90 | -$185.57 | -10% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 117 | 37 (32%) | 36 / 81 | 1.9 | -$14.97 | -$94.56 | -20% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 74% of orders | 125 | 53 (42%) | 47 / 78 | 2.0 | -$13.69 | $2.75 | +1% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 57 | 25 (44%) | 20 / 37 | 1.5 | -$10.05 | -$23.32 | -10% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 26 | 12 (46%) | 9 / 17 | 1.5 | -$19.37 | -$25.05 | -10% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 6 | 1 (17%) | 2 / 4 | 1.5 | -$5.79 | -$10.00 | -50% |

*Model accuracy vs Kalshi's prices on the same 13,388 readings (excluding the final minute): V1 **+1.3%**, V2 **+2.2%**, 3-exchange price (V3/V4) **-0.2%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $474.95 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 557 | 429 (77%) | -$144.84 | -7% | 162,260 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.4%** over 25,201 readings from 990 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4533 | 2% | 4% | 6% |
| 10–20% | 2022 | 15% | 16% | 17% |
| 20–30% | 2187 | 25% | 26% | 27% |
| 30–40% | 2365 | 35% | 36% | 40% |
| 40–50% | 2480 | 45% | 47% | 53% |
| 50–60% | 2474 | 55% | 59% | 61% |
| 60–70% | 2190 | 65% | 70% | 71% |
| 70–80% | 1791 | 75% | 80% | 81% |
| 80–90% | 1549 | 85% | 88% | 84% |
| 90–100% | 3610 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 518 | 266 (51%) | 46¢ | 52% | $216.85 | +9% |
| 6–10¢ | 321 | 158 (49%) | 44¢ | 54% | $102.78 | +7% |
| 10–20¢ | 104 | 41 (39%) | 43¢ | 57% | -$50.98 | -11% |
| 20¢+ | 8 | 2 (25%) | 35¢ | 64% | -$8.98 | -31% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 871 | 434 (50%) | 45¢ | 54% | $256.13 | +6% |
| 5–10 min | 72 | 28 (39%) | 37¢ | 46% | $3.62 | +1% |
| 2–5 min | 6 | 4 (67%) | 65¢ | 73% | $0.32 | +1% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 117 | 25 (21%) | 19¢ | 27% | $19.53 | +8% |
| Toss-up (25–75¢) | 769 | 387 (50%) | 46¢ | 54% | $221.12 | +6% |
| Favorite (75–95¢) | 65 | 55 (85%) | 81¢ | 88% | $19.02 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 108 | 55 (51%) | 43¢ | 53% | $70.59 | +15% |
| XRP | 107 | 56 (52%) | 46¢ | 54% | $47.95 | +9% |
| ETH | 107 | 47 (44%) | 46¢ | 54% | -$37.24 | -7% |
| HYPE | 106 | 46 (43%) | 43¢ | 52% | -$14.70 | -3% |
| SOL | 105 | 55 (52%) | 43¢ | 51% | $82.40 | +18% |
| NEAR | 105 | 52 (50%) | 47¢ | 55% | $11.52 | +2% |
| BTC | 105 | 59 (56%) | 50¢ | 58% | $46.99 | +9% |
| ZEC | 104 | 46 (44%) | 41¢ | 50% | $16.96 | +4% |
| DOGE | 104 | 51 (49%) | 44¢ | 52% | $35.20 | +7% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 1:52:14 AM | XRP | UP | 7.8 min | 40¢ | 47% | 5¢ | Open | — |
| 9/29 1:51:43 AM | DOGE | DOWN | 8.3 min | 41¢ | 54% | 11¢ | Open | — |
| 9/29 1:50:30 AM | BTC | DOWN | 9.5 min | 45¢ | 51% | 4¢ | Open | — |
| 9/29 1:49:33 AM | ETH | UP | 10.4 min | 55¢ | 63% | 6¢ | Open | — |
| 9/29 1:48:11 AM | NEAR | DOWN | 11.8 min | 37¢ | 49% | 10¢ | Open | — |
| 9/29 1:47:51 AM | BNB | DOWN | 12.2 min | 47¢ | 53% | 5¢ | Open | — |
| 9/29 1:47:51 AM | ZEC | DOWN | 12.2 min | 38¢ | 48% | 8¢ | Open | — |
| 9/29 1:46:54 AM | HYPE | DOWN | 13.1 min | 46¢ | 78% | 30¢ | Open | — |
| 9/29 1:34:24 AM | SOL | DOWN | 10.6 min | 25¢ | 35% | 9¢ | ❌ Lost | -$2.64 |
| 9/29 1:33:14 AM | BTC | UP | 11.8 min | 70¢ | 76% | 5¢ | ✅ Won | $2.85 |
| 9/29 1:32:41 AM | HYPE | DOWN | 12.3 min | 67¢ | 81% | 12¢ | ❌ Lost | -$6.86 |
| 9/29 1:32:10 AM | BNB | DOWN | 12.8 min | 60¢ | 70% | 8¢ | ❌ Lost | -$6.21 |
| 9/29 1:32:10 AM | DOGE | DOWN | 12.8 min | 62¢ | 72% | 8¢ | ❌ Lost | -$6.37 |
| 9/29 1:31:41 AM | ZEC | DOWN | 13.3 min | 59¢ | 67% | 6¢ | ❌ Lost | -$6.07 |
| 9/29 1:31:31 AM | NEAR | DOWN | 13.5 min | 74¢ | 80% | 5¢ | ❌ Lost | -$7.54 |
| 9/29 1:31:31 AM | ETH | UP | 13.5 min | 27¢ | 35% | 7¢ | ❌ Lost | -$2.84 |
| 9/29 1:31:14 AM | XRP | UP | 13.8 min | 41¢ | 51% | 8¢ | ✅ Won | $5.73 |
| 9/29 1:25:23 AM | NEAR | DOWN | 4.6 min | 80¢ | 87% | 6¢ | ✅ Won | $1.88 |
| 9/29 1:19:44 AM | DOGE | DOWN | 10.2 min | 45¢ | 59% | 13¢ | ❌ Lost | -$4.68 |
| 9/29 1:18:26 AM | BNB | DOWN | 11.6 min | 35¢ | 42% | 6¢ | ❌ Lost | -$3.66 |
| 9/29 1:17:52 AM | ETH | UP | 12.1 min | 79¢ | 90% | 10¢ | ✅ Won | $1.98 |
| 9/29 1:17:44 AM | BTC | UP | 12.2 min | 75¢ | 86% | 9¢ | ✅ Won | $2.36 |
| 9/29 1:17:44 AM | XRP | UP | 12.2 min | 81¢ | 89% | 7¢ | ✅ Won | $1.79 |
| 9/29 1:16:49 AM | HYPE | DOWN | 13.2 min | 36¢ | 44% | 6¢ | ❌ Lost | -$3.77 |
| 9/29 1:16:49 AM | SOL | UP | 13.2 min | 47¢ | 54% | 5¢ | ❌ Lost | -$4.88 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
