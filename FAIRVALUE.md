# Fair-Value Bot

*Updated Wed Sep 30, 3:06 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1803 | $268.58 | +3% | $57.69 / $210.89 |
| 4¢+ | 1753 | $390.09 | +5% | $297.18 / $92.91 |
| 6¢+ | 1625 | $318.15 | +5% | $328.65 / -$10.50 |
| 8¢+ ← live bot | 1415 | $473.01 | +8% | $336.57 / $136.44 |
| 10¢+ | 1204 | $497.95 | +11% | $285.76 / $212.19 |
| 15¢+ | 741 | $559.20 | +22% | $208.03 / $351.17 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1690 | 1684 | 766 (45%) | 43¢ | 53% | $86.36 | +1% | +3.3¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 303 | 202 | 125 / 77 | $30.06 | $74.50 | $44.44 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1282 | 540 (42%) | 372 / 910 | 8.2 | -$43.45 | -$334.55 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1151 | 382 (33%) | 472 / 679 | 7.4 | -$55.90 | -$450.07 | -11% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 291 | 102 (35%) | 74 / 217 | 2.0 | -$14.97 | -$109.11 | -10% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 309 | 135 (44%) | 92 / 217 | 2.0 | -$13.69 | -$0.50 | -0% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 184 | 77 (42%) | 63 / 121 | 1.5 | -$10.05 | -$62.40 | -8% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 3 | 3 (100%) | 0 / 3 | 1.0 | $0.97 | $4.52 | +18% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 41 | 15 (37%) | 15 / 26 | 1.5 | -$5.89 | -$2.06 | -1% |

*Model accuracy vs Kalshi's prices on the same 32,962 readings (excluding the final minute): V1 **+0.8%**, V2 **+1.1%**, 3-exchange price (V3/V4) **-0.3%**.*

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
| 1290 | 1162 (90%) | -$318.15 | -6% | 250,292 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.5%** over 46,269 readings from 1818 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 8151 | 3% | 4% | 5% |
| 10–20% | 3618 | 15% | 17% | 15% |
| 20–30% | 3925 | 25% | 26% | 26% |
| 30–40% | 4278 | 35% | 37% | 38% |
| 40–50% | 4559 | 45% | 48% | 50% |
| 50–60% | 4474 | 55% | 59% | 58% |
| 60–70% | 3942 | 65% | 71% | 71% |
| 70–80% | 3283 | 75% | 80% | 83% |
| 80–90% | 3006 | 85% | 88% | 88% |
| 90–100% | 7033 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 627 | 288 (46%) | 43¢ | 52% | $89.71 | +3% |
| 10–20¢ | 326 | 133 (41%) | 41¢ | 55% | -$57.78 | -4% |
| 20¢+ | 20 | 7 (35%) | 39¢ | 67% | -$11.94 | -15% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1376 | 646 (47%) | 45¢ | 54% | $47.39 | +1% |
| 5–10 min | 253 | 98 (39%) | 36¢ | 46% | $22.05 | +2% |
| 2–5 min | 47 | 18 (38%) | 33¢ | 45% | $19.82 | +12% |
| 1–2 min | 6 | 2 (33%) | 44¢ | 63% | -$6.82 | -25% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 265 | 43 (16%) | 18¢ | 27% | -$78.01 | -15% |
| Toss-up (25–75¢) | 1290 | 610 (47%) | 45¢ | 54% | $103.90 | +2% |
| Favorite (75–95¢) | 129 | 113 (88%) | 82¢ | 90% | $60.47 | +6% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 196 | 90 (46%) | 43¢ | 54% | $30.71 | +4% |
| ETH | 195 | 88 (45%) | 46¢ | 55% | -$49.50 | -5% |
| HYPE | 189 | 84 (44%) | 43¢ | 52% | $3.95 | +0% |
| XRP | 187 | 84 (45%) | 45¢ | 53% | -$24.97 | -3% |
| BTC | 187 | 96 (51%) | 49¢ | 58% | $12.72 | +1% |
| ZEC | 186 | 77 (41%) | 40¢ | 49% | $2.03 | +0% |
| DOGE | 183 | 76 (42%) | 42¢ | 51% | -$29.90 | -4% |
| NEAR | 182 | 83 (46%) | 43¢ | 51% | $18.28 | +2% |
| SOL | 179 | 88 (49%) | 41¢ | 50% | $123.04 | +16% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/30 3:03:39 AM | ZEC | DOWN | 11.3 min | 17¢ | 27% | 9¢ | Open | — |
| 9/30 3:02:52 AM | NEAR | DOWN | 12.1 min | 43¢ | 53% | 8¢ | Open | — |
| 9/30 3:02:05 AM | XRP | DOWN | 12.9 min | 41¢ | 52% | 10¢ | Open | — |
| 9/30 3:01:09 AM | DOGE | DOWN | 13.8 min | 53¢ | 66% | 11¢ | Open | — |
| 9/30 3:01:09 AM | HYPE | DOWN | 13.8 min | 43¢ | 53% | 9¢ | Open | — |
| 9/30 3:01:09 AM | BNB | DOWN | 13.8 min | 41¢ | 58% | 16¢ | Open | — |
| 9/30 2:51:50 AM | ETH | DOWN | 8.2 min | 27¢ | 42% | 13¢ | ❌ Lost | -$2.84 |
| 9/30 2:51:23 AM | ZEC | DOWN | 8.6 min | 9¢ | 18% | 8¢ | ❌ Lost | -$0.98 |
| 9/30 2:49:09 AM | HYPE | DOWN | 10.8 min | 8¢ | 21% | 13¢ | ❌ Lost | -$0.82 |
| 9/30 2:48:16 AM | BTC | DOWN | 11.7 min | 24¢ | 35% | 9¢ | ❌ Lost | -$2.53 |
| 9/30 2:47:17 AM | XRP | DOWN | 12.7 min | 19¢ | 29% | 9¢ | ❌ Lost | -$2.01 |
| 9/30 2:46:40 AM | DOGE | DOWN | 13.3 min | 35¢ | 45% | 8¢ | ❌ Lost | -$3.66 |
| 9/30 2:46:27 AM | NEAR | DOWN | 13.5 min | 36¢ | 47% | 10¢ | ❌ Lost | -$3.77 |
| 9/30 2:46:08 AM | BNB | DOWN | 13.8 min | 24¢ | 40% | 14¢ | ❌ Lost | -$2.53 |
| 9/30 2:41:16 AM | BTC | DOWN | 3.7 min | 79¢ | 89% | 9¢ | ✅ Won | $1.98 |
| 9/30 2:39:46 AM | HYPE | DOWN | 5.2 min | 43¢ | 60% | 15¢ | ❌ Lost | -$4.48 |
| 9/30 2:38:16 AM | SOL | UP | 6.7 min | 17¢ | 27% | 9¢ | ❌ Lost | -$1.81 |
| 9/30 2:36:08 AM | ZEC | UP | 8.9 min | 13¢ | 22% | 8¢ | ❌ Lost | -$1.38 |
| 9/30 2:34:31 AM | NEAR | UP | 10.5 min | 20¢ | 29% | 8¢ | ❌ Lost | -$2.12 |
| 9/30 2:34:17 AM | XRP | UP | 10.7 min | 23¢ | 33% | 9¢ | ❌ Lost | -$2.43 |
| 9/30 2:33:42 AM | DOGE | UP | 11.3 min | 14¢ | 25% | 10¢ | ❌ Lost | -$1.49 |
| 9/30 2:32:50 AM | BNB | UP | 12.2 min | 21¢ | 30% | 8¢ | ❌ Lost | -$2.22 |
| 9/30 2:31:12 AM | ETH | DOWN | 13.8 min | 83¢ | 92% | 8¢ | ✅ Won | $1.61 |
| 9/30 2:26:07 AM | SOL | DOWN | 3.9 min | 15¢ | 29% | 13¢ | ❌ Lost | -$1.59 |
| 9/30 2:20:05 AM | BTC | DOWN | 9.9 min | 19¢ | 30% | 10¢ | ❌ Lost | -$2.01 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
