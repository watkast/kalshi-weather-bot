# Fair-Value Bot

*Updated Wed Sep 30, 1:14 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1731 | $308.24 | +4% | $147.86 / $160.38 |
| 4¢+ | 1683 | $404.62 | +5% | $355.11 / $49.51 |
| 6¢+ | 1556 | $344.97 | +5% | $362.50 / -$17.53 |
| 8¢+ ← live bot | 1357 | $468.01 | +9% | $382.76 / $85.25 |
| 10¢+ | 1156 | $464.47 | +10% | $303.54 / $160.93 |
| 15¢+ | 714 | $506.75 | +20% | $239.91 / $266.84 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1629 | 1622 | 751 (46%) | 44¢ | 53% | $135.54 | +2% | +3.8¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 241 | 165 | 106 / 59 | $79.24 | $91.32 | $12.08 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1220 | 525 (43%) | 361 / 859 | 8.2 | -$43.45 | -$285.37 | -5% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1089 | 369 (34%) | 451 / 638 | 7.4 | -$55.90 | -$359.82 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 277 | 98 (35%) | 70 / 207 | 2.0 | -$14.97 | -$103.14 | -10% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 293 | 131 (45%) | 90 / 203 | 2.0 | -$13.69 | $14.08 | +1% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 175 | 76 (43%) | 61 / 114 | 1.5 | -$10.05 | -$35.56 | -5% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 3 | 3 (100%) | 0 / 3 | 1.0 | $0.97 | $4.52 | +18% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 40 | 15 (38%) | 15 / 25 | 1.5 | -$5.89 | $0.78 | +1% |

*Model accuracy vs Kalshi's prices on the same 31,219 readings (excluding the final minute): V1 **+0.8%**, V2 **+1.3%**, 3-exchange price (V3/V4) **-0.3%**.*

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
| 1228 | 1100 (90%) | -$268.97 | -5% | 246,320 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.5%** over 44,400 readings from 1746 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 7899 | 3% | 4% | 5% |
| 10–20% | 3480 | 15% | 17% | 15% |
| 20–30% | 3778 | 25% | 26% | 26% |
| 30–40% | 4153 | 35% | 37% | 39% |
| 40–50% | 4432 | 45% | 48% | 50% |
| 50–60% | 4297 | 55% | 59% | 58% |
| 60–70% | 3806 | 65% | 71% | 71% |
| 70–80% | 3148 | 75% | 80% | 82% |
| 80–90% | 2830 | 85% | 88% | 87% |
| 90–100% | 6577 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 595 | 281 (47%) | 44¢ | 53% | $122.81 | +5% |
| 10–20¢ | 296 | 125 (42%) | 42¢ | 56% | -$41.70 | -3% |
| 20¢+ | 20 | 7 (35%) | 39¢ | 67% | -$11.94 | -15% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1339 | 638 (48%) | 45¢ | 54% | $96.83 | +2% |
| 5–10 min | 231 | 92 (40%) | 38¢ | 47% | $18.62 | +2% |
| 2–5 min | 44 | 17 (39%) | 32¢ | 44% | $22.99 | +16% |
| 1–2 min | 6 | 2 (33%) | 44¢ | 63% | -$6.82 | -25% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 239 | 42 (18%) | 18¢ | 27% | -$40.10 | -9% |
| Toss-up (25–75¢) | 1256 | 598 (48%) | 45¢ | 54% | $118.76 | +2% |
| Favorite (75–95¢) | 127 | 111 (87%) | 82¢ | 90% | $56.88 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 188 | 87 (46%) | 43¢ | 54% | $33.89 | +4% |
| ETH | 187 | 84 (45%) | 46¢ | 55% | -$55.17 | -6% |
| HYPE | 182 | 83 (46%) | 43¢ | 53% | $14.15 | +2% |
| XRP | 181 | 84 (46%) | 46¢ | 54% | -$11.46 | -1% |
| BTC | 180 | 94 (52%) | 50¢ | 58% | $19.89 | +2% |
| ZEC | 179 | 76 (42%) | 40¢ | 50% | $10.46 | +1% |
| DOGE | 176 | 75 (43%) | 42¢ | 51% | -$19.92 | -3% |
| NEAR | 175 | 80 (46%) | 44¢ | 52% | $11.37 | +1% |
| SOL | 174 | 88 (51%) | 41¢ | 50% | $132.33 | +18% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/30 1:07:27 AM | SOL | UP | 7.5 min | 22¢ | 34% | 11¢ | Open | — |
| 9/30 1:05:55 AM | ZEC | UP | 9.1 min | 18¢ | 28% | 10¢ | Open | — |
| 9/30 1:04:23 AM | ETH | DOWN | 10.6 min | 34¢ | 47% | 12¢ | Open | — |
| 9/30 1:02:08 AM | DOGE | DOWN | 12.8 min | 41¢ | 54% | 10¢ | Open | — |
| 9/30 1:02:08 AM | NEAR | DOWN | 12.8 min | 55¢ | 66% | 8¢ | Open | — |
| 9/30 1:01:29 AM | BNB | DOWN | 13.5 min | 47¢ | 65% | 16¢ | Open | — |
| 9/30 1:01:21 AM | HYPE | DOWN | 13.7 min | 53¢ | 68% | 13¢ | Open | — |
| 9/30 12:56:30 AM | BTC | DOWN | 3.5 min | 15¢ | 30% | 14¢ | ✅ Won | $8.41 |
| 9/30 12:56:08 AM | SOL | UP | 3.9 min | 56¢ | 80% | 23¢ | ❌ Lost | -$5.77 |
| 9/30 12:55:56 AM | DOGE | DOWN | 4.0 min | 23¢ | 49% | 25¢ | ✅ Won | $7.57 |
| 9/30 12:55:00 AM | HYPE | UP | 5.0 min | 14¢ | 25% | 10¢ | ❌ Lost | -$1.49 |
| 9/30 12:52:29 AM | ETH | DOWN | 7.5 min | 71¢ | 81% | 8¢ | ❌ Lost | -$7.25 |
| 9/30 12:48:59 AM | ZEC | UP | 11.0 min | 20¢ | 32% | 11¢ | ❌ Lost | -$2.12 |
| 9/30 12:46:56 AM | BNB | UP | 13.1 min | 23¢ | 33% | 9¢ | ❌ Lost | -$2.43 |
| 9/30 12:43:02 AM | SOL | DOWN | 1.9 min | 82¢ | 96% | 13¢ | ✅ Won | $1.69 |
| 9/30 12:35:12 AM | XRP | DOWN | 9.8 min | 54¢ | 64% | 8¢ | ❌ Lost | -$5.58 |
| 9/30 12:33:13 AM | DOGE | DOWN | 11.8 min | 65¢ | 76% | 10¢ | ✅ Won | $3.37 |
| 9/30 12:32:15 AM | BNB | UP | 12.8 min | 31¢ | 45% | 13¢ | ❌ Lost | -$3.25 |
| 9/30 12:31:54 AM | HYPE | DOWN | 13.1 min | 74¢ | 86% | 10¢ | ✅ Won | $2.43 |
| 9/30 12:31:17 AM | ETH | DOWN | 13.7 min | 67¢ | 79% | 10¢ | ✅ Won | $3.14 |
| 9/30 12:31:17 AM | BTC | DOWN | 13.7 min | 62¢ | 72% | 9¢ | ✅ Won | $3.63 |
| 9/30 12:20:32 AM | ZEC | DOWN | 9.5 min | 41¢ | 54% | 11¢ | ✅ Won | $5.73 |
| 9/30 12:20:32 AM | HYPE | DOWN | 9.5 min | 50¢ | 60% | 8¢ | ✅ Won | $4.82 |
| 9/30 12:18:47 AM | NEAR | DOWN | 11.2 min | 19¢ | 30% | 10¢ | ❌ Lost | -$2.00 |
| 9/30 12:18:15 AM | BTC | DOWN | 11.8 min | 53¢ | 64% | 9¢ | ✅ Won | $4.52 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
