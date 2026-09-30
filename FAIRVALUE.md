# Fair-Value Bot

*Updated Tue Sep 29, 7:58 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1542 | $160.49 | +2% | $101.38 / $59.11 |
| 4¢+ | 1495 | $266.45 | +4% | $331.65 / -$65.20 |
| 6¢+ | 1378 | $221.31 | +4% | $301.69 / -$80.38 |
| 8¢+ ← live bot | 1201 | $340.57 | +7% | $363.83 / -$23.26 |
| 10¢+ | 1020 | $340.01 | +9% | $272.61 / $67.40 |
| 15¢+ | 619 | $354.59 | +17% | $262.13 / $92.46 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1487 | 1479 | 683 (46%) | 44¢ | 53% | $61.26 | +1% | +4.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 98 | 69 | 42 / 27 | $4.96 | $0.52 | -$4.44 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1077 | 457 (42%) | 332 / 745 | 8.4 | -$43.45 | -$359.65 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 937 | 316 (34%) | 409 / 528 | 7.3 | -$55.90 | -$330.75 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 238 | 80 (34%) | 66 / 172 | 2.0 | -$14.97 | -$118.99 | -13% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 251 | 105 (42%) | 78 / 173 | 2.0 | -$13.69 | -$40.50 | -4% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 146 | 62 (42%) | 52 / 94 | 1.5 | -$10.05 | -$39.54 | -7% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 1 | 1 (100%) | 0 / 1 | 1.0 | $1.67 | $1.67 | +20% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 31 | 12 (39%) | 12 / 19 | 1.6 | -$5.89 | -$1.37 | -1% |

*Model accuracy vs Kalshi's prices on the same 26,746 readings (excluding the final minute): V1 **+0.2%**, V2 **+1.0%**, 3-exchange price (V3/V4) **-1.1%**.*

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
| 1085 | 957 (88%) | -$343.25 | -8% | 240,827 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+3.9%** over 39,605 readings from 1557 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 6901 | 3% | 4% | 5% |
| 10–20% | 3076 | 15% | 16% | 17% |
| 20–30% | 3321 | 25% | 26% | 28% |
| 30–40% | 3679 | 35% | 36% | 39% |
| 40–50% | 3928 | 45% | 48% | 52% |
| 50–60% | 3860 | 55% | 59% | 60% |
| 60–70% | 3418 | 65% | 70% | 73% |
| 70–80% | 2834 | 75% | 80% | 83% |
| 80–90% | 2508 | 85% | 88% | 87% |
| 90–100% | 6080 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 526 | 244 (46%) | 44¢ | 53% | $41.96 | +2% |
| 10–20¢ | 227 | 96 (42%) | 42¢ | 56% | -$34.85 | -4% |
| 20¢+ | 15 | 5 (33%) | 40¢ | 68% | -$12.22 | -20% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1252 | 594 (47%) | 45¢ | 54% | $49.02 | +1% |
| 5–10 min | 195 | 77 (39%) | 38¢ | 47% | $9.20 | +1% |
| 2–5 min | 28 | 11 (39%) | 35¢ | 46% | $9.12 | +9% |
| 1–2 min | 4 | 1 (25%) | 39¢ | 61% | -$6.08 | -38% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 206 | 38 (18%) | 18¢ | 27% | -$18.24 | -5% |
| Toss-up (25–75¢) | 1155 | 543 (47%) | 45¢ | 54% | $38.82 | +1% |
| Favorite (75–95¢) | 118 | 102 (86%) | 82¢ | 89% | $40.68 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 169 | 83 (49%) | 44¢ | 54% | $63.10 | +8% |
| XRP | 168 | 79 (47%) | 45¢ | 54% | $0.46 | +0% |
| ETH | 168 | 73 (43%) | 46¢ | 55% | -$71.08 | -9% |
| ZEC | 164 | 70 (43%) | 41¢ | 50% | $1.59 | +0% |
| HYPE | 163 | 69 (42%) | 43¢ | 52% | -$40.37 | -6% |
| BTC | 163 | 83 (51%) | 49¢ | 58% | -$1.89 | -0% |
| SOL | 162 | 83 (51%) | 41¢ | 50% | $136.85 | +20% |
| NEAR | 161 | 74 (46%) | 44¢ | 52% | -$0.52 | -0% |
| DOGE | 161 | 69 (43%) | 43¢ | 52% | -$26.88 | -4% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 7:56:50 PM | BTC | DOWN | 3.2 min | 56¢ | 71% | 13¢ | Open | — |
| 9/29 7:56:02 PM | DOGE | UP | 4.0 min | 20¢ | 30% | 9¢ | Open | — |
| 9/29 7:55:05 PM | SOL | DOWN | 4.9 min | 42¢ | 53% | 9¢ | Open | — |
| 9/29 7:54:48 PM | XRP | UP | 5.2 min | 35¢ | 52% | 15¢ | Open | — |
| 9/29 7:52:34 PM | NEAR | DOWN | 7.4 min | 58¢ | 68% | 8¢ | Open | — |
| 9/29 7:48:57 PM | HYPE | DOWN | 11.1 min | 56¢ | 71% | 14¢ | Open | — |
| 9/29 7:47:32 PM | ETH | DOWN | 12.5 min | 50¢ | 60% | 8¢ | Open | — |
| 9/29 7:46:05 PM | BNB | DOWN | 13.9 min | 44¢ | 56% | 11¢ | Open | — |
| 9/29 7:41:11 PM | HYPE | DOWN | 3.8 min | 49¢ | 62% | 11¢ | ❌ Lost | -$5.08 |
| 9/29 7:40:23 PM | DOGE | UP | 4.6 min | 9¢ | 17% | 8¢ | ❌ Lost | -$0.93 |
| 9/29 7:39:50 PM | SOL | UP | 5.2 min | 25¢ | 35% | 9¢ | ✅ Won | $7.36 |
| 9/29 7:32:29 PM | XRP | DOWN | 12.5 min | 72¢ | 83% | 10¢ | ❌ Lost | -$7.35 |
| 9/29 7:31:41 PM | ETH | DOWN | 13.3 min | 68¢ | 85% | 15¢ | ✅ Won | $3.04 |
| 9/29 7:31:27 PM | BNB | DOWN | 13.5 min | 55¢ | 68% | 11¢ | ✅ Won | $4.32 |
| 9/29 7:31:12 PM | BTC | DOWN | 13.8 min | 62¢ | 75% | 11¢ | ✅ Won | $3.63 |
| 9/29 7:31:12 PM | ZEC | DOWN | 13.8 min | 44¢ | 57% | 11¢ | ❌ Lost | -$4.58 |
| 9/29 7:27:24 PM | ETH | DOWN | 2.6 min | 7¢ | 18% | 11¢ | ❌ Lost | -$0.77 |
| 9/29 7:25:10 PM | ZEC | DOWN | 4.8 min | 46¢ | 60% | 12¢ | ✅ Won | $5.22 |
| 9/29 7:21:25 PM | DOGE | DOWN | 8.6 min | 27¢ | 39% | 10¢ | ❌ Lost | -$2.85 |
| 9/29 7:21:24 PM | XRP | DOWN | 8.6 min | 39¢ | 49% | 8¢ | ❌ Lost | -$4.07 |
| 9/29 7:21:24 PM | NEAR | DOWN | 8.6 min | 50¢ | 60% | 8¢ | ❌ Lost | -$5.18 |
| 9/29 7:19:18 PM | HYPE | DOWN | 10.7 min | 43¢ | 55% | 10¢ | ✅ Won | $5.52 |
| 9/29 7:16:28 PM | BNB | DOWN | 13.5 min | 33¢ | 45% | 10¢ | ✅ Won | $6.54 |
| 9/29 7:07:26 PM | BTC | DOWN | 7.5 min | 64¢ | 76% | 10¢ | ✅ Won | $3.43 |
| 9/29 7:07:19 PM | SOL | DOWN | 7.7 min | 37¢ | 52% | 13¢ | ❌ Lost | -$3.87 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
