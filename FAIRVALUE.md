# Fair-Value Bot

*Updated Wed Sep 30, 12:14 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1695 | $254.65 | +3% | $162.27 / $92.38 |
| 4¢+ | 1647 | $359.09 | +5% | $350.64 / $8.45 |
| 6¢+ | 1521 | $265.82 | +4% | $390.04 / -$124.22 |
| 8¢+ ← live bot | 1325 | $380.34 | +7% | $377.54 / $2.80 |
| 10¢+ | 1129 | $398.74 | +9% | $307.15 / $91.59 |
| 15¢+ | 698 | $449.46 | +19% | $251.68 / $197.78 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1599 | 1594 | 734 (46%) | 44¢ | 53% | $90.00 | +1% | +3.8¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 213 | 143 | 90 / 53 | $33.70 | $37.83 | $4.13 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1192 | 508 (43%) | 353 / 839 | 8.3 | -$43.45 | -$330.91 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1061 | 351 (33%) | 445 / 616 | 7.4 | -$55.90 | -$417.43 | -11% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 270 | 93 (34%) | 70 / 200 | 2.0 | -$14.97 | -$117.65 | -11% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 285 | 126 (44%) | 89 / 196 | 2.0 | -$13.69 | $7.73 | +1% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 167 | 73 (44%) | 57 / 110 | 1.5 | -$10.05 | -$29.89 | -4% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 3 | 3 (100%) | 0 / 3 | 1.0 | $0.97 | $4.52 | +18% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 39 | 14 (36%) | 15 / 24 | 1.6 | -$5.89 | -$6.48 | -4% |

*Model accuracy vs Kalshi's prices on the same 30,405 readings (excluding the final minute): V1 **+0.5%**, V2 **+1.1%**, 3-exchange price (V3/V4) **-0.6%**.*

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
| 1200 | 1072 (89%) | -$314.51 | -7% | 245,790 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.2%** over 43,516 readings from 1710 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 7595 | 3% | 4% | 5% |
| 10–20% | 3359 | 15% | 17% | 16% |
| 20–30% | 3656 | 25% | 26% | 27% |
| 30–40% | 4053 | 35% | 37% | 39% |
| 40–50% | 4346 | 45% | 48% | 51% |
| 50–60% | 4236 | 55% | 59% | 59% |
| 60–70% | 3758 | 65% | 71% | 72% |
| 70–80% | 3124 | 75% | 80% | 83% |
| 80–90% | 2820 | 85% | 88% | 88% |
| 90–100% | 6569 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 583 | 274 (47%) | 44¢ | 53% | $108.32 | +4% |
| 10–20¢ | 282 | 116 (41%) | 42¢ | 56% | -$70.95 | -6% |
| 20¢+ | 18 | 6 (33%) | 39¢ | 67% | -$13.74 | -19% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1322 | 626 (47%) | 45¢ | 54% | $54.47 | +1% |
| 5–10 min | 224 | 90 (40%) | 38¢ | 47% | $27.34 | +3% |
| 2–5 min | 41 | 15 (37%) | 32¢ | 44% | $12.78 | +9% |
| 1–2 min | 5 | 1 (20%) | 36¢ | 57% | -$8.51 | -46% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 232 | 40 (17%) | 18¢ | 27% | -$46.34 | -10% |
| Toss-up (25–75¢) | 1236 | 584 (47%) | 45¢ | 54% | $81.15 | +1% |
| Favorite (75–95¢) | 126 | 110 (87%) | 82¢ | 90% | $55.19 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 184 | 86 (47%) | 43¢ | 54% | $37.02 | +4% |
| ETH | 183 | 81 (44%) | 46¢ | 55% | -$59.11 | -7% |
| XRP | 179 | 83 (46%) | 46¢ | 54% | -$12.22 | -1% |
| HYPE | 178 | 80 (45%) | 43¢ | 53% | $3.20 | +0% |
| BTC | 177 | 91 (51%) | 50¢ | 58% | $3.33 | +0% |
| ZEC | 176 | 75 (43%) | 41¢ | 50% | $8.55 | +1% |
| NEAR | 174 | 80 (46%) | 44¢ | 52% | $13.37 | +2% |
| DOGE | 173 | 72 (42%) | 42¢ | 51% | -$38.20 | -5% |
| SOL | 170 | 86 (51%) | 41¢ | 50% | $134.06 | +18% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/30 12:08:19 AM | ZEC | UP | 6.7 min | 16¢ | 28% | 11¢ | Open | — |
| 9/30 12:06:41 AM | BNB | UP | 8.3 min | 31¢ | 44% | 11¢ | Open | — |
| 9/30 12:03:13 AM | SOL | UP | 11.8 min | 34¢ | 47% | 11¢ | Open | — |
| 9/30 12:02:56 AM | HYPE | DOWN | 12.1 min | 46¢ | 60% | 11¢ | Open | — |
| 9/30 12:02:21 AM | ETH | DOWN | 12.7 min | 62¢ | 73% | 9¢ | Open | — |
| 9/29 11:59:08 PM | XRP | DOWN | 0.9 min | 72¢ | 100% | 26¢ | ✅ Won | $2.61 |
| 9/29 11:59:08 PM | HYPE | DOWN | 0.9 min | 86¢ | 100% | 13¢ | ✅ Won | $1.31 |
| 9/29 11:52:48 PM | DOGE | UP | 7.2 min | 13¢ | 28% | 14¢ | ❌ Lost | -$1.38 |
| 9/29 11:51:17 PM | NEAR | DOWN | 8.7 min | 43¢ | 54% | 9¢ | ✅ Won | $5.52 |
| 9/29 11:51:10 PM | BNB | UP | 8.8 min | 16¢ | 31% | 14¢ | ❌ Lost | -$1.70 |
| 9/29 11:35:36 PM | ETH | DOWN | 9.4 min | 32¢ | 42% | 9¢ | ❌ Lost | -$3.36 |
| 9/29 11:34:42 PM | ZEC | DOWN | 10.3 min | 21¢ | 33% | 11¢ | ❌ Lost | -$2.22 |
| 9/29 11:33:09 PM | DOGE | UP | 11.8 min | 65¢ | 86% | 19¢ | ✅ Won | $3.34 |
| 9/29 11:33:01 PM | BTC | UP | 12.0 min | 70¢ | 81% | 10¢ | ✅ Won | $2.85 |
| 9/29 11:32:39 PM | XRP | UP | 12.3 min | 76¢ | 89% | 11¢ | ✅ Won | $2.27 |
| 9/29 11:32:39 PM | SOL | UP | 12.3 min | 72¢ | 86% | 13¢ | ✅ Won | $2.65 |
| 9/29 11:32:06 PM | HYPE | DOWN | 12.9 min | 17¢ | 35% | 17¢ | ❌ Lost | -$1.80 |
| 9/29 11:31:42 PM | NEAR | DOWN | 13.3 min | 17¢ | 28% | 10¢ | ❌ Lost | -$1.80 |
| 9/29 11:31:23 PM | BNB | DOWN | 13.6 min | 32¢ | 47% | 14¢ | ❌ Lost | -$3.36 |
| 9/29 11:18:52 PM | XRP | DOWN | 11.1 min | 36¢ | 50% | 12¢ | ❌ Lost | -$3.77 |
| 9/29 11:18:44 PM | HYPE | DOWN | 11.2 min | 47¢ | 60% | 11¢ | ✅ Won | $5.10 |
| 9/29 11:18:23 PM | BNB | DOWN | 11.6 min | 61¢ | 78% | 15¢ | ❌ Lost | -$6.27 |
| 9/29 11:18:23 PM | DOGE | DOWN | 11.6 min | 24¢ | 39% | 14¢ | ❌ Lost | -$2.53 |
| 9/29 11:18:23 PM | NEAR | DOWN | 11.6 min | 29¢ | 39% | 8¢ | ❌ Lost | -$3.05 |
| 9/29 11:18:08 PM | ZEC | DOWN | 11.8 min | 37¢ | 56% | 18¢ | ❌ Lost | -$3.83 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
