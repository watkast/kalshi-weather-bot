# Fair-Value Bot

*Updated Tue Sep 29, 2:15 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **6¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **6¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 985 | $92.97 | +2% | $122.93 / -$29.96 |
| 4¢+ ← live bot | 952 | $311.16 | +7% | $174.97 / $136.19 |
| 6¢+ | 876 | $320.85 | +9% | $206.48 / $114.37 |
| 8¢+ | 754 | $300.15 | +10% | $208.15 / $92.00 |
| 10¢+ | 646 | $205.94 | +8% | $214.69 / -$8.75 |
| 15¢+ | 388 | $201.54 | +16% | $186.01 / $15.53 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 969 | 960 | 470 (49%) | 45¢ | 53% | $247.66 | +6% | +6.3¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 558 | 244 (44%) | 173 / 385 | 8.5 | -$37.76 | -$173.25 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 492 | 168 (34%) | 231 / 261 | 7.5 | -$55.90 | -$196.76 | -10% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 119 | 38 (32%) | 36 / 83 | 2.0 | -$14.97 | -$92.98 | -20% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 75% of orders | 127 | 53 (42%) | 47 / 80 | 2.0 | -$13.69 | -$4.74 | -1% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 59 | 26 (44%) | 20 / 39 | 1.5 | -$10.05 | -$22.77 | -9% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 28 | 13 (46%) | 9 / 19 | 1.5 | -$19.37 | -$28.45 | -10% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 8 | 2 (25%) | 3 / 5 | 1.6 | -$5.79 | -$8.34 | -29% |

*Model accuracy vs Kalshi's prices on the same 13,597 readings (excluding the final minute): V1 **+1.3%**, V2 **+2.1%**, 3-exchange price (V3/V4) **-0.2%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $471.56 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 566 | 438 (77%) | -$156.85 | -8% | 164,056 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.5%** over 25,428 readings from 999 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4564 | 2% | 4% | 6% |
| 10–20% | 2027 | 15% | 16% | 17% |
| 20–30% | 2198 | 25% | 26% | 27% |
| 30–40% | 2383 | 35% | 36% | 40% |
| 40–50% | 2528 | 45% | 47% | 53% |
| 50–60% | 2531 | 55% | 59% | 60% |
| 60–70% | 2207 | 65% | 70% | 71% |
| 70–80% | 1807 | 75% | 80% | 81% |
| 80–90% | 1553 | 85% | 88% | 84% |
| 90–100% | 3630 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 522 | 268 (51%) | 46¢ | 52% | $217.44 | +9% |
| 6–10¢ | 322 | 158 (49%) | 44¢ | 54% | $98.81 | +7% |
| 10–20¢ | 107 | 42 (39%) | 43¢ | 57% | -$54.83 | -12% |
| 20¢+ | 9 | 2 (22%) | 36¢ | 65% | -$13.76 | -41% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 876 | 435 (50%) | 45¢ | 54% | $242.96 | +6% |
| 5–10 min | 75 | 30 (40%) | 37¢ | 46% | $10.46 | +4% |
| 2–5 min | 7 | 4 (57%) | 64¢ | 72% | -$5.36 | -12% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 117 | 25 (21%) | 19¢ | 27% | $19.53 | +8% |
| Toss-up (25–75¢) | 778 | 390 (50%) | 46¢ | 54% | $209.11 | +6% |
| Favorite (75–95¢) | 65 | 55 (85%) | 81¢ | 88% | $19.02 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 109 | 56 (51%) | 43¢ | 53% | $75.71 | +16% |
| XRP | 108 | 56 (52%) | 46¢ | 54% | $43.78 | +8% |
| ETH | 108 | 47 (44%) | 46¢ | 54% | -$42.92 | -8% |
| HYPE | 107 | 46 (43%) | 43¢ | 52% | -$19.48 | -4% |
| SOL | 106 | 55 (52%) | 43¢ | 51% | $76.72 | +16% |
| NEAR | 106 | 52 (49%) | 47¢ | 55% | $7.66 | +1% |
| BTC | 106 | 60 (57%) | 50¢ | 58% | $52.31 | +10% |
| ZEC | 105 | 46 (44%) | 41¢ | 50% | $12.99 | +3% |
| DOGE | 105 | 52 (50%) | 44¢ | 52% | $40.89 | +9% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 2:02:08 AM | HYPE | DOWN | 12.8 min | 37¢ | 56% | 18¢ | Open | — |
| 9/29 2:02:08 AM | SOL | DOWN | 12.8 min | 35¢ | 44% | 7¢ | Open | — |
| 9/29 2:01:53 AM | XRP | DOWN | 13.1 min | 39¢ | 51% | 11¢ | Open | — |
| 9/29 2:01:34 AM | DOGE | UP | 13.4 min | 58¢ | 66% | 6¢ | Open | — |
| 9/29 2:01:34 AM | ZEC | UP | 13.4 min | 42¢ | 57% | 13¢ | Open | — |
| 9/29 2:01:17 AM | BNB | DOWN | 13.7 min | 34¢ | 42% | 6¢ | Open | — |
| 9/29 2:01:17 AM | BTC | UP | 13.7 min | 77¢ | 85% | 7¢ | Open | — |
| 9/29 2:01:17 AM | NEAR | DOWN | 13.7 min | 54¢ | 62% | 7¢ | Open | — |
| 9/29 2:01:17 AM | ETH | UP | 13.7 min | 76¢ | 83% | 6¢ | Open | — |
| 9/29 1:55:08 AM | SOL | UP | 4.9 min | 55¢ | 69% | 12¢ | ❌ Lost | -$5.68 |
| 9/29 1:52:14 AM | XRP | UP | 7.8 min | 40¢ | 47% | 5¢ | ❌ Lost | -$4.17 |
| 9/29 1:51:43 AM | DOGE | DOWN | 8.3 min | 41¢ | 54% | 11¢ | ✅ Won | $5.69 |
| 9/29 1:50:30 AM | BTC | DOWN | 9.5 min | 45¢ | 51% | 4¢ | ✅ Won | $5.32 |
| 9/29 1:49:33 AM | ETH | UP | 10.4 min | 55¢ | 63% | 6¢ | ❌ Lost | -$5.68 |
| 9/29 1:48:11 AM | NEAR | DOWN | 11.8 min | 37¢ | 49% | 10¢ | ❌ Lost | -$3.86 |
| 9/29 1:47:51 AM | BNB | DOWN | 12.2 min | 47¢ | 53% | 5¢ | ✅ Won | $5.12 |
| 9/29 1:47:51 AM | ZEC | DOWN | 12.2 min | 38¢ | 48% | 8¢ | ❌ Lost | -$3.97 |
| 9/29 1:46:54 AM | HYPE | DOWN | 13.1 min | 46¢ | 78% | 30¢ | ❌ Lost | -$4.78 |
| 9/29 1:34:24 AM | SOL | DOWN | 10.6 min | 25¢ | 35% | 9¢ | ❌ Lost | -$2.64 |
| 9/29 1:33:14 AM | BTC | UP | 11.8 min | 70¢ | 76% | 5¢ | ✅ Won | $2.85 |
| 9/29 1:32:41 AM | HYPE | DOWN | 12.3 min | 67¢ | 81% | 12¢ | ❌ Lost | -$6.86 |
| 9/29 1:32:10 AM | BNB | DOWN | 12.8 min | 60¢ | 70% | 8¢ | ❌ Lost | -$6.21 |
| 9/29 1:32:10 AM | DOGE | DOWN | 12.8 min | 62¢ | 72% | 8¢ | ❌ Lost | -$6.37 |
| 9/29 1:31:41 AM | ZEC | DOWN | 13.3 min | 59¢ | 67% | 6¢ | ❌ Lost | -$6.07 |
| 9/29 1:31:31 AM | NEAR | DOWN | 13.5 min | 74¢ | 80% | 5¢ | ❌ Lost | -$7.54 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
