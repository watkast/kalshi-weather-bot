# Fair-Value Bot

*Updated Tue Sep 29, 2:25 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **4¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 994 | $135.41 | +3% | $121.50 / $13.91 |
| 4¢+ ← live bot | 961 | $340.99 | +8% | $175.64 / $165.35 |
| 6¢+ | 885 | $336.46 | +9% | $205.21 / $131.25 |
| 8¢+ | 762 | $316.09 | +10% | $198.26 / $117.83 |
| 10¢+ | 652 | $225.26 | +9% | $214.99 / $10.27 |
| 15¢+ | 391 | $215.50 | +16% | $185.15 / $30.35 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 978 | 969 | 476 (49%) | 45¢ | 53% | $260.99 | +6% | +6.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 567 | 250 (44%) | 177 / 390 | 8.5 | -$37.76 | -$159.92 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 497 | 169 (34%) | 233 / 264 | 7.4 | -$55.90 | -$206.00 | -11% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 121 | 38 (31%) | 37 / 84 | 2.0 | -$14.97 | -$102.23 | -21% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 75% of orders | 129 | 55 (43%) | 48 / 81 | 2.0 | -$13.69 | $2.67 | +0% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 61 | 27 (44%) | 22 / 39 | 1.5 | -$10.05 | -$22.85 | -9% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 30 | 14 (47%) | 11 / 19 | 1.5 | -$19.37 | -$31.28 | -11% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 8 | 2 (25%) | 3 / 5 | 1.6 | -$5.79 | -$8.34 | -29% |

*Model accuracy vs Kalshi's prices on the same 13,804 readings (excluding the final minute): V1 **+1.4%**, V2 **+2.1%**, 3-exchange price (V3/V4) **-0.1%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $468.73 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 575 | 447 (78%) | -$143.52 | -7% | 166,853 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.5%** over 25,653 readings from 1008 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4629 | 2% | 4% | 6% |
| 10–20% | 2053 | 15% | 16% | 17% |
| 20–30% | 2216 | 25% | 26% | 27% |
| 30–40% | 2402 | 35% | 36% | 40% |
| 40–50% | 2545 | 45% | 47% | 53% |
| 50–60% | 2544 | 55% | 59% | 60% |
| 60–70% | 2222 | 65% | 70% | 71% |
| 70–80% | 1821 | 75% | 80% | 81% |
| 80–90% | 1573 | 85% | 88% | 85% |
| 90–100% | 3648 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 523 | 269 (51%) | 46¢ | 52% | $219.71 | +9% |
| 6–10¢ | 327 | 162 (50%) | 45¢ | 54% | $112.19 | +7% |
| 10–20¢ | 110 | 43 (39%) | 43¢ | 57% | -$57.15 | -12% |
| 20¢+ | 9 | 2 (22%) | 36¢ | 65% | -$13.76 | -41% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 885 | 441 (50%) | 45¢ | 54% | $256.29 | +6% |
| 5–10 min | 75 | 30 (40%) | 37¢ | 46% | $10.46 | +4% |
| 2–5 min | 7 | 4 (57%) | 64¢ | 72% | -$5.36 | -12% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 117 | 25 (21%) | 19¢ | 27% | $19.53 | +8% |
| Toss-up (25–75¢) | 785 | 394 (50%) | 46¢ | 54% | $218.00 | +6% |
| Favorite (75–95¢) | 67 | 57 (85%) | 80¢ | 88% | $23.46 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 110 | 57 (52%) | 43¢ | 52% | $82.13 | +17% |
| XRP | 109 | 57 (52%) | 46¢ | 54% | $49.71 | +10% |
| ETH | 109 | 48 (44%) | 46¢ | 54% | -$40.65 | -8% |
| HYPE | 108 | 46 (43%) | 43¢ | 52% | -$23.35 | -5% |
| SOL | 107 | 56 (52%) | 43¢ | 51% | $83.05 | +17% |
| NEAR | 107 | 53 (50%) | 47¢ | 55% | $12.10 | +2% |
| BTC | 107 | 61 (57%) | 50¢ | 58% | $54.48 | +10% |
| ZEC | 106 | 46 (43%) | 41¢ | 50% | $8.61 | +2% |
| DOGE | 106 | 52 (49%) | 44¢ | 53% | $34.91 | +7% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 2:21:06 AM | ZEC | DOWN | 8.9 min | 34¢ | 47% | 12¢ | Open | — |
| 9/29 2:18:26 AM | SOL | UP | 11.6 min | 61¢ | 70% | 8¢ | Open | — |
| 9/29 2:18:26 AM | ETH | UP | 11.6 min | 52¢ | 62% | 8¢ | Open | — |
| 9/29 2:18:17 AM | BTC | UP | 11.7 min | 58¢ | 65% | 5¢ | Open | — |
| 9/29 2:18:08 AM | BNB | DOWN | 11.9 min | 25¢ | 40% | 14¢ | Open | — |
| 9/29 2:17:49 AM | DOGE | UP | 12.2 min | 67¢ | 74% | 5¢ | Open | — |
| 9/29 2:17:49 AM | XRP | UP | 12.2 min | 72¢ | 81% | 8¢ | Open | — |
| 9/29 2:16:47 AM | NEAR | UP | 13.2 min | 90¢ | 97% | 6¢ | Open | — |
| 9/29 2:16:47 AM | HYPE | UP | 13.2 min | 60¢ | 73% | 11¢ | Open | — |
| 9/29 2:02:08 AM | HYPE | DOWN | 12.8 min | 37¢ | 56% | 18¢ | ❌ Lost | -$3.87 |
| 9/29 2:02:08 AM | SOL | DOWN | 12.8 min | 35¢ | 44% | 7¢ | ✅ Won | $6.33 |
| 9/29 2:01:53 AM | XRP | DOWN | 13.1 min | 39¢ | 51% | 11¢ | ✅ Won | $5.93 |
| 9/29 2:01:34 AM | DOGE | UP | 13.4 min | 58¢ | 66% | 6¢ | ❌ Lost | -$5.98 |
| 9/29 2:01:34 AM | ZEC | UP | 13.4 min | 42¢ | 57% | 13¢ | ❌ Lost | -$4.38 |
| 9/29 2:01:17 AM | BNB | DOWN | 13.7 min | 34¢ | 42% | 6¢ | ✅ Won | $6.42 |
| 9/29 2:01:17 AM | BTC | UP | 13.7 min | 77¢ | 85% | 7¢ | ✅ Won | $2.17 |
| 9/29 2:01:17 AM | NEAR | DOWN | 13.7 min | 54¢ | 62% | 7¢ | ✅ Won | $4.44 |
| 9/29 2:01:17 AM | ETH | UP | 13.7 min | 76¢ | 83% | 6¢ | ✅ Won | $2.27 |
| 9/29 1:55:08 AM | SOL | UP | 4.9 min | 55¢ | 69% | 12¢ | ❌ Lost | -$5.68 |
| 9/29 1:52:14 AM | XRP | UP | 7.8 min | 40¢ | 47% | 5¢ | ❌ Lost | -$4.17 |
| 9/29 1:51:43 AM | DOGE | DOWN | 8.3 min | 41¢ | 54% | 11¢ | ✅ Won | $5.69 |
| 9/29 1:50:30 AM | BTC | DOWN | 9.5 min | 45¢ | 51% | 4¢ | ✅ Won | $5.32 |
| 9/29 1:49:33 AM | ETH | UP | 10.4 min | 55¢ | 63% | 6¢ | ❌ Lost | -$5.68 |
| 9/29 1:48:11 AM | NEAR | DOWN | 11.8 min | 37¢ | 49% | 10¢ | ❌ Lost | -$3.86 |
| 9/29 1:47:51 AM | BNB | DOWN | 12.2 min | 47¢ | 53% | 5¢ | ✅ Won | $5.12 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
