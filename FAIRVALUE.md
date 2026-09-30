# Fair-Value Bot

*Updated Tue Sep 29, 10:32 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1641 | $214.09 | +3% | $164.97 / $49.12 |
| 4¢+ | 1593 | $289.90 | +4% | $358.95 / -$69.05 |
| 6¢+ | 1470 | $231.67 | +4% | $366.28 / -$134.61 |
| 8¢+ ← live bot | 1287 | $331.09 | +6% | $361.00 / -$29.91 |
| 10¢+ | 1097 | $360.43 | +9% | $290.89 / $69.54 |
| 15¢+ | 674 | $415.26 | +18% | $252.15 / $163.11 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1550 | 1550 | 711 (46%) | 44¢ | 53% | $54.67 | +1% | +3.9¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 169 | 123 | 76 / 47 | -$1.63 | $19.57 | $21.20 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1148 | 485 (42%) | 342 / 806 | 8.3 | -$43.45 | -$366.24 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1014 | 338 (33%) | 425 / 589 | 7.3 | -$55.90 | -$373.29 | -10% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 258 | 89 (34%) | 67 / 191 | 2.0 | -$14.97 | -$115.42 | -11% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 273 | 119 (44%) | 82 / 191 | 2.0 | -$13.69 | $2.73 | +0% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 157 | 68 (43%) | 54 / 103 | 1.5 | -$10.05 | -$31.06 | -5% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 2 | 2 (100%) | 0 / 2 | 1.0 | $0.97 | $2.64 | +15% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 35 | 13 (37%) | 13 / 22 | 1.5 | -$5.89 | -$4.38 | -3% |

*Model accuracy vs Kalshi's prices on the same 29,158 readings (excluding the final minute): V1 **+0.3%**, V2 **+0.9%**, 3-exchange price (V3/V4) **-0.9%**.*

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
| 1156 | 1028 (89%) | -$349.84 | -8% | 243,082 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.0%** over 42,179 readings from 1656 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 7353 | 3% | 4% | 5% |
| 10–20% | 3274 | 15% | 17% | 16% |
| 20–30% | 3542 | 25% | 26% | 27% |
| 30–40% | 3930 | 35% | 37% | 40% |
| 40–50% | 4209 | 45% | 48% | 52% |
| 50–60% | 4130 | 55% | 59% | 59% |
| 60–70% | 3667 | 65% | 70% | 72% |
| 70–80% | 3004 | 75% | 80% | 82% |
| 80–90% | 2685 | 85% | 88% | 87% |
| 90–100% | 6385 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 563 | 262 (47%) | 44¢ | 53% | $77.28 | +3% |
| 10–20¢ | 260 | 106 (41%) | 42¢ | 56% | -$74.12 | -7% |
| 20¢+ | 16 | 5 (31%) | 39¢ | 67% | -$14.86 | -23% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1291 | 610 (47%) | 45¢ | 54% | $30.53 | +1% |
| 5–10 min | 213 | 85 (40%) | 38¢ | 47% | $19.87 | +2% |
| 2–5 min | 41 | 15 (37%) | 32¢ | 44% | $12.78 | +9% |
| 1–2 min | 5 | 1 (20%) | 36¢ | 57% | -$8.51 | -46% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 221 | 39 (18%) | 18¢ | 27% | -$34.95 | -8% |
| Toss-up (25–75¢) | 1208 | 567 (47%) | 45¢ | 54% | $43.48 | +1% |
| Favorite (75–95¢) | 121 | 105 (87%) | 82¢ | 89% | $46.14 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| ETH | 178 | 78 (44%) | 46¢ | 55% | -$67.06 | -8% |
| BNB | 178 | 85 (48%) | 43¢ | 54% | $48.38 | +6% |
| XRP | 174 | 80 (46%) | 45¢ | 53% | -$12.98 | -2% |
| BTC | 173 | 87 (50%) | 49¢ | 58% | -$6.44 | -1% |
| HYPE | 172 | 76 (44%) | 43¢ | 53% | -$10.04 | -1% |
| ZEC | 171 | 73 (43%) | 41¢ | 50% | $2.26 | +0% |
| SOL | 168 | 85 (51%) | 41¢ | 50% | $134.66 | +19% |
| NEAR | 168 | 77 (46%) | 44¢ | 52% | $5.81 | +1% |
| DOGE | 168 | 70 (42%) | 43¢ | 51% | -$39.92 | -5% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 10:21:06 PM | ZEC | DOWN | 8.9 min | 17¢ | 26% | 8¢ | ❌ Lost | -$1.80 |
| 9/29 10:21:06 PM | NEAR | DOWN | 8.9 min | 38¢ | 54% | 15¢ | ❌ Lost | -$3.97 |
| 9/29 10:20:38 PM | ETH | DOWN | 9.4 min | 38¢ | 53% | 13¢ | ✅ Won | $6.03 |
| 9/29 10:19:47 PM | XRP | UP | 10.2 min | 63¢ | 81% | 16¢ | ✅ Won | $3.53 |
| 9/29 10:19:47 PM | SOL | UP | 10.2 min | 58¢ | 72% | 12¢ | ❌ Lost | -$5.96 |
| 9/29 10:19:47 PM | BTC | UP | 10.2 min | 57¢ | 75% | 16¢ | ❌ Lost | -$5.88 |
| 9/29 10:18:11 PM | HYPE | DOWN | 11.8 min | 29¢ | 40% | 10¢ | ❌ Lost | -$3.05 |
| 9/29 10:16:16 PM | BNB | DOWN | 13.7 min | 26¢ | 37% | 10¢ | ❌ Lost | -$2.74 |
| 9/29 10:16:16 PM | DOGE | DOWN | 13.7 min | 36¢ | 51% | 14¢ | ❌ Lost | -$3.77 |
| 9/29 10:10:43 PM | BTC | DOWN | 4.3 min | 17¢ | 33% | 15¢ | ❌ Lost | -$1.80 |
| 9/29 10:08:26 PM | ETH | DOWN | 6.5 min | 21¢ | 30% | 8¢ | ❌ Lost | -$2.21 |
| 9/29 10:04:11 PM | HYPE | DOWN | 10.8 min | 33¢ | 43% | 9¢ | ✅ Won | $6.54 |
| 9/29 10:02:39 PM | XRP | DOWN | 12.3 min | 25¢ | 37% | 11¢ | ❌ Lost | -$2.64 |
| 9/29 10:02:39 PM | ZEC | DOWN | 12.3 min | 23¢ | 39% | 15¢ | ❌ Lost | -$2.43 |
| 9/29 10:02:39 PM | BNB | DOWN | 12.3 min | 17¢ | 28% | 10¢ | ❌ Lost | -$1.80 |
| 9/29 10:02:39 PM | DOGE | DOWN | 12.3 min | 25¢ | 49% | 23¢ | ❌ Lost | -$2.64 |
| 9/29 9:40:06 PM | HYPE | DOWN | 4.9 min | 40¢ | 53% | 12¢ | ✅ Won | $5.84 |
| 9/29 9:39:25 PM | NEAR | DOWN | 5.6 min | 57¢ | 70% | 11¢ | ✅ Won | $4.12 |
| 9/29 9:35:53 PM | ZEC | DOWN | 9.1 min | 48¢ | 61% | 11¢ | ❌ Lost | -$4.98 |
| 9/29 9:34:26 PM | ETH | DOWN | 10.6 min | 48¢ | 58% | 8¢ | ❌ Lost | -$4.98 |
| 9/29 9:33:58 PM | DOGE | DOWN | 11.0 min | 44¢ | 57% | 11¢ | ❌ Lost | -$4.58 |
| 9/29 9:32:56 PM | BTC | DOWN | 12.1 min | 60¢ | 74% | 12¢ | ❌ Lost | -$6.17 |
| 9/29 9:31:22 PM | BNB | UP | 13.6 min | 28¢ | 43% | 14¢ | ✅ Won | $7.05 |
| 9/29 9:22:04 PM | ETH | DOWN | 7.9 min | 81¢ | 91% | 9¢ | ✅ Won | $1.79 |
| 9/29 9:17:51 PM | ZEC | DOWN | 12.1 min | 81¢ | 93% | 11¢ | ✅ Won | $1.79 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
