# Fair-Value Bot

*Updated Tue Sep 29, 9:29 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1596 | $190.61 | +2% | $180.58 / $10.03 |
| 4¢+ | 1549 | $261.04 | +4% | $382.70 / -$121.66 |
| 6¢+ | 1429 | $230.70 | +4% | $372.12 / -$141.42 |
| 8¢+ ← live bot | 1249 | $352.68 | +7% | $355.04 / -$2.36 |
| 10¢+ | 1067 | $372.75 | +9% | $258.56 / $114.19 |
| 15¢+ | 651 | $379.95 | +17% | $226.28 / $153.67 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1527 | 1524 | 702 (46%) | 44¢ | 53% | $76.43 | +1% | +4.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 143 | 106 | 67 / 39 | $20.13 | $31.13 | $11.00 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1122 | 476 (42%) | 338 / 784 | 8.4 | -$43.45 | -$344.48 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 985 | 331 (34%) | 422 / 563 | 7.4 | -$55.90 | -$331.34 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 250 | 86 (34%) | 67 / 183 | 2.0 | -$14.97 | -$108.80 | -11% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 263 | 114 (43%) | 78 / 185 | 2.0 | -$13.69 | -$6.97 | -1% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 153 | 67 (44%) | 53 / 100 | 1.5 | -$10.05 | -$25.67 | -4% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 2 | 2 (100%) | 0 / 2 | 1.0 | $0.97 | $2.64 | +15% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 33 | 12 (36%) | 12 / 21 | 1.5 | -$5.89 | -$8.18 | -6% |

*Model accuracy vs Kalshi's prices on the same 28,096 readings (excluding the final minute): V1 **+0.2%**, V2 **+0.9%**, 3-exchange price (V3/V4) **-1.0%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

⛔ **HALTED** — equity $389.72 fell below stop $394.02 (peak $525.36)

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $389.72 | $525.36 | $394.02 | 0 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 1130 | 1002 (89%) | -$328.08 | -7% | 241,386 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+3.9%** over 41,036 readings from 1611 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 7079 | 3% | 4% | 5% |
| 10–20% | 3165 | 15% | 17% | 16% |
| 20–30% | 3432 | 25% | 26% | 28% |
| 30–40% | 3849 | 35% | 37% | 39% |
| 40–50% | 4149 | 45% | 48% | 52% |
| 50–60% | 4054 | 55% | 59% | 59% |
| 60–70% | 3585 | 65% | 70% | 72% |
| 70–80% | 2932 | 75% | 80% | 82% |
| 80–90% | 2595 | 85% | 88% | 87% |
| 90–100% | 6196 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 556 | 260 (47%) | 44¢ | 53% | $83.73 | +3% |
| 10–20¢ | 242 | 99 (41%) | 42¢ | 56% | -$61.45 | -6% |
| 20¢+ | 15 | 5 (33%) | 40¢ | 68% | -$12.22 | -20% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1274 | 605 (47%) | 45¢ | 54% | $55.31 | +1% |
| 5–10 min | 206 | 82 (40%) | 37¢ | 46% | $20.89 | +3% |
| 2–5 min | 39 | 14 (36%) | 32¢ | 44% | $8.74 | +7% |
| 1–2 min | 5 | 1 (20%) | 36¢ | 57% | -$8.51 | -46% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 216 | 39 (18%) | 18¢ | 27% | -$24.91 | -6% |
| Toss-up (25–75¢) | 1189 | 560 (47%) | 45¢ | 54% | $58.78 | +1% |
| Favorite (75–95¢) | 119 | 103 (87%) | 82¢ | 89% | $42.56 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 175 | 84 (48%) | 44¢ | 54% | $45.87 | +6% |
| ETH | 174 | 76 (44%) | 46¢ | 55% | -$67.69 | -8% |
| XRP | 172 | 79 (46%) | 45¢ | 53% | -$13.87 | -2% |
| HYPE | 169 | 74 (44%) | 43¢ | 53% | -$19.37 | -3% |
| BTC | 169 | 86 (51%) | 49¢ | 58% | $4.46 | +1% |
| SOL | 167 | 85 (51%) | 41¢ | 50% | $140.62 | +20% |
| ZEC | 167 | 72 (43%) | 41¢ | 50% | $9.68 | +1% |
| NEAR | 166 | 76 (46%) | 44¢ | 52% | $5.66 | +1% |
| DOGE | 165 | 70 (42%) | 43¢ | 51% | -$28.93 | -4% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 9:22:04 PM | ETH | DOWN | 7.9 min | 81¢ | 91% | 9¢ | Open | — |
| 9/29 9:17:51 PM | ZEC | DOWN | 12.1 min | 81¢ | 93% | 11¢ | Open | — |
| 9/29 9:17:32 PM | BTC | DOWN | 12.4 min | 69¢ | 82% | 11¢ | Open | — |
| 9/29 9:12:09 PM | SOL | DOWN | 2.8 min | 12¢ | 27% | 15¢ | ❌ Lost | -$1.28 |
| 9/29 9:10:13 PM | NEAR | DOWN | 4.8 min | 14¢ | 24% | 9¢ | ❌ Lost | -$1.49 |
| 9/29 9:10:07 PM | ETH | DOWN | 4.9 min | 43¢ | 54% | 10¢ | ✅ Won | $5.52 |
| 9/29 9:08:27 PM | BTC | DOWN | 6.5 min | 52¢ | 63% | 9¢ | ✅ Won | $4.62 |
| 9/29 9:05:30 PM | HYPE | DOWN | 9.5 min | 31¢ | 41% | 8¢ | ✅ Won | $6.75 |
| 9/29 9:01:11 PM | BNB | DOWN | 13.8 min | 46¢ | 57% | 9¢ | ✅ Won | $5.22 |
| 9/29 8:56:52 PM | ETH | DOWN | 3.1 min | 12¢ | 22% | 9¢ | ❌ Lost | -$1.28 |
| 9/29 8:55:25 PM | SOL | DOWN | 4.6 min | 12¢ | 21% | 8¢ | ❌ Lost | -$1.28 |
| 9/29 8:54:07 PM | XRP | DOWN | 5.9 min | 32¢ | 44% | 10¢ | ❌ Lost | -$3.36 |
| 9/29 8:53:22 PM | BTC | DOWN | 6.6 min | 24¢ | 35% | 10¢ | ✅ Won | $7.47 |
| 9/29 8:51:29 PM | ZEC | DOWN | 8.5 min | 43¢ | 53% | 8¢ | ✅ Won | $5.52 |
| 9/29 8:50:57 PM | NEAR | DOWN | 9.0 min | 28¢ | 38% | 8¢ | ❌ Lost | -$2.95 |
| 9/29 8:48:13 PM | DOGE | DOWN | 11.8 min | 27¢ | 36% | 8¢ | ✅ Won | $7.16 |
| 9/29 8:46:40 PM | BNB | DOWN | 13.3 min | 43¢ | 54% | 9¢ | ❌ Lost | -$4.48 |
| 9/29 8:46:09 PM | HYPE | DOWN | 13.8 min | 45¢ | 56% | 9¢ | ✅ Won | $5.32 |
| 9/29 8:41:44 PM | BTC | DOWN | 3.3 min | 38¢ | 50% | 10¢ | ✅ Won | $6.03 |
| 9/29 8:40:54 PM | NEAR | DOWN | 4.1 min | 7¢ | 17% | 9¢ | ❌ Lost | -$0.76 |
| 9/29 8:39:49 PM | DOGE | DOWN | 5.2 min | 31¢ | 43% | 11¢ | ❌ Lost | -$3.22 |
| 9/29 8:32:46 PM | ETH | DOWN | 12.2 min | 48¢ | 59% | 9¢ | ❌ Lost | -$4.98 |
| 9/29 8:32:12 PM | ZEC | DOWN | 12.8 min | 33¢ | 44% | 9¢ | ❌ Lost | -$3.46 |
| 9/29 8:32:12 PM | HYPE | DOWN | 12.8 min | 28¢ | 41% | 12¢ | ❌ Lost | -$2.95 |
| 9/29 8:31:27 PM | BNB | DOWN | 13.5 min | 45¢ | 57% | 10¢ | ❌ Lost | -$4.71 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
