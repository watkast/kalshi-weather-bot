# Fair-Value Bot

*Updated Wed Sep 30, 9:16 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 2028 | $205.67 | +2% | $146.42 / $59.25 |
| 4¢+ | 1975 | $377.86 | +4% | $347.02 / $30.84 |
| 6¢+ | 1830 | $327.05 | +4% | $331.56 / -$4.51 |
| 8¢+ ← live bot | 1592 | $494.25 | +8% | $291.08 / $203.17 |
| 10¢+ | 1358 | $501.87 | +10% | $205.99 / $295.88 |
| 15¢+ | 834 | $578.62 | +20% | $206.09 / $372.53 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1858 | 1857 | 831 (45%) | 43¢ | 52% | $73.51 | +1% | +3.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 476 | 307 | 195 / 112 | $17.21 | $87.12 | $69.91 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1455 | 605 (42%) | 418 / 1037 | 8.1 | -$43.45 | -$347.40 | -5% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1333 | 455 (34%) | 555 / 778 | 7.4 | -$55.90 | -$329.28 | -7% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 335 | 113 (34%) | 86 / 249 | 2.0 | -$14.97 | -$109.08 | -9% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 355 | 150 (42%) | 109 / 246 | 2.0 | -$13.69 | -$28.49 | -2% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 217 | 89 (41%) | 74 / 143 | 1.5 | -$10.05 | -$82.64 | -10% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 7 | 7 (100%) | 1 / 6 | 1.2 | $0.97 | $11.30 | +19% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 53 | 18 (34%) | 20 / 33 | 1.6 | -$5.89 | -$10.64 | -6% |

*Model accuracy vs Kalshi's prices on the same 38,063 readings (excluding the final minute): V1 **+0.6%**, V2 **+1.4%**, 3-exchange price (V3/V4) **-0.4%**.*

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
| 1463 | 1335 (91%) | -$331.00 | -6% | 251,740 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.2%** over 51,793 readings from 2043 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 8965 | 3% | 4% | 4% |
| 10–20% | 3914 | 15% | 16% | 15% |
| 20–30% | 4318 | 25% | 26% | 26% |
| 30–40% | 4735 | 35% | 37% | 39% |
| 40–50% | 5127 | 45% | 48% | 51% |
| 50–60% | 5076 | 55% | 59% | 59% |
| 60–70% | 4428 | 65% | 71% | 72% |
| 70–80% | 3678 | 75% | 80% | 83% |
| 80–90% | 3412 | 85% | 88% | 89% |
| 90–100% | 8140 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 691 | 311 (45%) | 42¢ | 52% | $70.78 | +2% |
| 10–20¢ | 431 | 172 (40%) | 40¢ | 54% | -$62.16 | -3% |
| 20¢+ | 24 | 10 (42%) | 41¢ | 67% | -$1.48 | -1% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1485 | 685 (46%) | 45¢ | 54% | $2.71 | +0% |
| 5–10 min | 296 | 112 (38%) | 36¢ | 46% | $11.53 | +1% |
| 2–5 min | 67 | 29 (43%) | 34¢ | 46% | $55.01 | +23% |
| 1–2 min | 7 | 3 (43%) | 41¢ | 60% | $0.34 | +1% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 303 | 49 (16%) | 18¢ | 28% | -$89.71 | -15% |
| Toss-up (25–75¢) | 1418 | 662 (47%) | 44¢ | 54% | $93.24 | +1% |
| Favorite (75–95¢) | 136 | 120 (88%) | 82¢ | 90% | $69.98 | +6% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 220 | 94 (43%) | 42¢ | 53% | -$18.66 | -2% |
| ETH | 215 | 97 (45%) | 45¢ | 55% | -$38.14 | -4% |
| HYPE | 211 | 92 (44%) | 43¢ | 53% | -$10.72 | -1% |
| BTC | 207 | 104 (50%) | 48¢ | 57% | $11.42 | +1% |
| XRP | 205 | 93 (45%) | 43¢ | 52% | $11.61 | +1% |
| ZEC | 204 | 82 (40%) | 39¢ | 49% | -$10.44 | -1% |
| DOGE | 203 | 82 (40%) | 42¢ | 51% | -$53.32 | -6% |
| NEAR | 199 | 88 (44%) | 42¢ | 51% | $5.06 | +1% |
| SOL | 193 | 99 (51%) | 41¢ | 50% | $176.70 | +22% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/30 9:16:29 AM | BNB | DOWN | 13.5 min | 42¢ | 57% | 14¢ | Open | — |
| 9/30 9:11:34 AM | NEAR | DOWN | 3.4 min | 41¢ | 51% | 9¢ | ✅ Won | $5.73 |
| 9/30 9:10:22 AM | ZEC | DOWN | 4.6 min | 52¢ | 62% | 9¢ | ✅ Won | $4.62 |
| 9/30 9:09:16 AM | BTC | DOWN | 5.7 min | 24¢ | 34% | 9¢ | ❌ Lost | -$2.53 |
| 9/30 9:09:16 AM | HYPE | DOWN | 5.7 min | 71¢ | 83% | 11¢ | ❌ Lost | -$7.25 |
| 9/30 9:04:53 AM | SOL | DOWN | 10.1 min | 38¢ | 50% | 10¢ | ✅ Won | $6.03 |
| 9/30 9:04:00 AM | XRP | DOWN | 11.0 min | 29¢ | 41% | 11¢ | ❌ Lost | -$3.05 |
| 9/30 9:04:00 AM | DOGE | DOWN | 11.0 min | 31¢ | 45% | 13¢ | ❌ Lost | -$3.20 |
| 9/30 9:03:19 AM | ETH | DOWN | 11.7 min | 45¢ | 57% | 10¢ | ❌ Lost | -$4.68 |
| 9/30 9:02:07 AM | BNB | DOWN | 12.9 min | 28¢ | 38% | 8¢ | ❌ Lost | -$3.00 |
| 9/30 8:54:24 AM | NEAR | DOWN | 5.6 min | 19¢ | 34% | 13¢ | ❌ Lost | -$2.01 |
| 9/30 8:52:02 AM | DOGE | DOWN | 8.0 min | 20¢ | 35% | 14¢ | ❌ Lost | -$2.12 |
| 9/30 8:52:02 AM | ZEC | DOWN | 8.0 min | 41¢ | 54% | 11¢ | ✅ Won | $5.73 |
| 9/30 8:50:55 AM | SOL | DOWN | 9.1 min | 29¢ | 39% | 9¢ | ❌ Lost | -$3.05 |
| 9/30 8:49:59 AM | BTC | DOWN | 10.0 min | 22¢ | 31% | 8¢ | ❌ Lost | -$2.33 |
| 9/30 8:49:43 AM | ETH | DOWN | 10.3 min | 23¢ | 37% | 12¢ | ❌ Lost | -$2.43 |
| 9/30 8:47:47 AM | HYPE | DOWN | 12.2 min | 23¢ | 38% | 13¢ | ❌ Lost | -$2.43 |
| 9/30 8:47:47 AM | BNB | DOWN | 12.2 min | 28¢ | 41% | 11¢ | ❌ Lost | -$2.95 |
| 9/30 8:47:47 AM | XRP | DOWN | 12.2 min | 34¢ | 44% | 8¢ | ❌ Lost | -$3.55 |
| 9/30 8:41:06 AM | BNB | DOWN | 3.9 min | 60¢ | 76% | 14¢ | ❌ Lost | -$6.20 |
| 9/30 8:37:32 AM | SOL | DOWN | 7.5 min | 30¢ | 43% | 12¢ | ✅ Won | $6.85 |
| 9/30 8:37:32 AM | ETH | DOWN | 7.5 min | 63¢ | 78% | 14¢ | ✅ Won | $3.55 |
| 9/30 8:36:32 AM | DOGE | DOWN | 8.4 min | 58¢ | 70% | 10¢ | ✅ Won | $4.02 |
| 9/30 8:34:42 AM | HYPE | UP | 10.3 min | 64¢ | 77% | 11¢ | ✅ Won | $3.43 |
| 9/30 8:34:42 AM | NEAR | UP | 10.3 min | 53¢ | 73% | 18¢ | ✅ Won | $4.52 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
