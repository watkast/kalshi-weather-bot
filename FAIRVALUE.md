# Fair-Value Bot

*Updated Tue Sep 29, 1:24 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 958 | $83.71 | +2% | $118.46 / -$34.75 |
| 4¢+ ← live bot | 926 | $294.12 | +7% | $179.79 / $114.33 |
| 6¢+ | 851 | $307.07 | +9% | $207.02 / $100.05 |
| 8¢+ | 734 | $311.30 | +11% | $199.96 / $111.34 |
| 10¢+ | 629 | $220.39 | +9% | $210.77 / $9.62 |
| 15¢+ | 375 | $188.52 | +15% | $183.47 / $5.05 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 941 | 933 | 460 (49%) | 45¢ | 53% | $293.37 | +7% | +6.7¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 531 | 234 (44%) | 163 / 368 | 8.4 | -$37.76 | -$127.54 | -5% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 470 | 158 (34%) | 217 / 253 | 7.5 | -$55.90 | -$200.22 | -11% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 113 | 36 (32%) | 36 / 77 | 1.9 | -$14.97 | -$88.30 | -20% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 74% of orders | 121 | 51 (42%) | 45 / 76 | 2.0 | -$13.69 | -$0.66 | -0% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 53 | 23 (43%) | 18 / 35 | 1.5 | -$10.05 | -$24.59 | -11% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 22 | 10 (45%) | 7 / 15 | 1.5 | -$19.37 | -$23.96 | -11% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 6 | 1 (17%) | 2 / 4 | 1.5 | -$5.79 | -$10.00 | -50% |

*Model accuracy vs Kalshi's prices on the same 12,974 readings (excluding the final minute): V1 **+1.6%**, V2 **+2.3%**, 3-exchange price (V3/V4) **+0.1%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $476.04 | $525.36 | $394.02 | 2 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 539 | 411 (76%) | -$111.14 | -6% | 162,260 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.7%** over 24,751 readings from 972 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4515 | 2% | 4% | 6% |
| 10–20% | 2011 | 15% | 16% | 17% |
| 20–30% | 2165 | 25% | 26% | 27% |
| 30–40% | 2333 | 35% | 36% | 40% |
| 40–50% | 2417 | 45% | 47% | 53% |
| 50–60% | 2427 | 55% | 59% | 61% |
| 60–70% | 2120 | 65% | 70% | 71% |
| 70–80% | 1727 | 75% | 80% | 81% |
| 80–90% | 1506 | 85% | 88% | 84% |
| 90–100% | 3530 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 512 | 263 (51%) | 45¢ | 52% | $222.97 | +9% |
| 6–10¢ | 311 | 154 (50%) | 44¢ | 53% | $118.82 | +8% |
| 10–20¢ | 102 | 41 (40%) | 42¢ | 57% | -$39.44 | -9% |
| 20¢+ | 8 | 2 (25%) | 35¢ | 64% | -$8.98 | -31% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 854 | 428 (50%) | 45¢ | 53% | $291.71 | +7% |
| 5–10 min | 72 | 28 (39%) | 37¢ | 46% | $3.62 | +1% |
| 2–5 min | 5 | 3 (60%) | 62¢ | 70% | -$1.56 | -5% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 117 | 25 (21%) | 19¢ | 27% | $19.53 | +8% |
| Toss-up (25–75¢) | 755 | 384 (51%) | 46¢ | 54% | $262.83 | +7% |
| Favorite (75–95¢) | 61 | 51 (84%) | 81¢ | 88% | $11.01 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 106 | 55 (52%) | 43¢ | 52% | $80.46 | +17% |
| XRP | 105 | 54 (51%) | 46¢ | 54% | $40.43 | +8% |
| ETH | 105 | 46 (44%) | 46¢ | 54% | -$36.38 | -7% |
| HYPE | 104 | 46 (44%) | 43¢ | 52% | -$4.07 | -1% |
| SOL | 103 | 55 (53%) | 43¢ | 51% | $89.92 | +20% |
| NEAR | 103 | 51 (50%) | 46¢ | 54% | $17.18 | +3% |
| BTC | 103 | 57 (55%) | 50¢ | 58% | $41.78 | +8% |
| ZEC | 102 | 45 (44%) | 41¢ | 50% | $17.80 | +4% |
| DOGE | 102 | 51 (50%) | 44¢ | 52% | $46.25 | +10% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 1:19:44 AM | DOGE | DOWN | 10.2 min | 45¢ | 59% | 13¢ | Open | — |
| 9/29 1:18:26 AM | BNB | DOWN | 11.6 min | 35¢ | 42% | 6¢ | Open | — |
| 9/29 1:17:52 AM | ETH | UP | 12.1 min | 79¢ | 90% | 10¢ | Open | — |
| 9/29 1:17:44 AM | BTC | UP | 12.2 min | 75¢ | 86% | 9¢ | Open | — |
| 9/29 1:17:44 AM | XRP | UP | 12.2 min | 81¢ | 89% | 7¢ | Open | — |
| 9/29 1:16:49 AM | HYPE | DOWN | 13.2 min | 36¢ | 44% | 6¢ | Open | — |
| 9/29 1:16:49 AM | SOL | UP | 13.2 min | 47¢ | 54% | 5¢ | Open | — |
| 9/29 1:16:27 AM | ZEC | DOWN | 13.6 min | 46¢ | 53% | 6¢ | Open | — |
| 9/29 1:09:14 AM | NEAR | DOWN | 5.8 min | 37¢ | 49% | 10¢ | ❌ Lost | -$3.87 |
| 9/29 1:07:47 AM | XRP | UP | 7.2 min | 28¢ | 35% | 6¢ | ❌ Lost | -$2.95 |
| 9/29 1:04:23 AM | BTC | UP | 10.6 min | 26¢ | 33% | 5¢ | ❌ Lost | -$2.74 |
| 9/29 1:02:32 AM | HYPE | DOWN | 12.5 min | 54¢ | 70% | 14¢ | ❌ Lost | -$5.58 |
| 9/29 1:02:18 AM | ZEC | UP | 12.7 min | 69¢ | 77% | 7¢ | ✅ Won | $2.95 |
| 9/29 1:02:10 AM | ETH | UP | 12.8 min | 15¢ | 20% | 4¢ | ✅ Won | $8.41 |
| 9/29 1:01:56 AM | SOL | UP | 13.1 min | 17¢ | 23% | 5¢ | ✅ Won | $8.20 |
| 9/29 1:01:21 AM | BNB | DOWN | 13.6 min | 72¢ | 80% | 6¢ | ❌ Lost | -$7.35 |
| 9/29 1:01:12 AM | DOGE | DOWN | 13.8 min | 76¢ | 81% | 4¢ | ❌ Lost | -$7.73 |
| 9/29 12:51:34 AM | ETH | DOWN | 8.4 min | 15¢ | 46% | 30¢ | ❌ Lost | -$1.59 |
| 9/29 12:51:34 AM | BTC | DOWN | 8.4 min | 19¢ | 27% | 7¢ | ❌ Lost | -$2.01 |
| 9/29 12:51:34 AM | XRP | DOWN | 8.4 min | 25¢ | 36% | 9¢ | ❌ Lost | -$2.64 |
| 9/29 12:51:15 AM | ZEC | DOWN | 8.7 min | 64¢ | 76% | 10¢ | ❌ Lost | -$6.57 |
| 9/29 12:47:24 AM | DOGE | DOWN | 12.6 min | 36¢ | 43% | 5¢ | ❌ Lost | -$3.77 |
| 9/29 12:47:17 AM | HYPE | DOWN | 12.7 min | 29¢ | 40% | 10¢ | ❌ Lost | -$3.05 |
| 9/29 12:46:56 AM | BNB | DOWN | 13.1 min | 44¢ | 51% | 6¢ | ❌ Lost | -$4.58 |
| 9/29 12:46:44 AM | NEAR | DOWN | 13.3 min | 53¢ | 59% | 4¢ | ❌ Lost | -$5.44 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
