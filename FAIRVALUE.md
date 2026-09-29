# Fair-Value Bot

*Updated Tue Sep 29, 4:36 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟡 **Promising, unproven.** An edge of **8¢+** is profitable so far, but not consistently yet (needs both halves positive and the model beating the market).

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1425 | $142.51 | +2% | $88.50 / $54.01 |
| 4¢+ | 1381 | $267.24 | +4% | $258.26 / $8.98 |
| 6¢+ | 1271 | $256.19 | +5% | $297.81 / -$41.62 |
| 8¢+ ← live bot | 1102 | $361.41 | +8% | $365.90 / -$4.49 |
| 10¢+ | 934 | $349.74 | +10% | $287.93 / $61.81 |
| 15¢+ | 565 | $357.15 | +19% | $253.13 / $104.02 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1391 | 1389 | 646 (47%) | 45¢ | 53% | $62.07 | +1% | +4.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 8 | 6 | 6 / 0 | $5.77 | $6.19 | $0.42 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 987 | 420 (43%) | 317 / 670 | 8.6 | -$43.45 | -$358.84 | -8% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 843 | 284 (34%) | 375 / 468 | 7.3 | -$55.90 | -$329.85 | -10% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 212 | 67 (32%) | 58 / 154 | 2.0 | -$14.97 | -$162.11 | -19% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 225 | 94 (42%) | 72 / 153 | 2.0 | -$13.69 | -$40.73 | -4% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 125 | 52 (42%) | 44 / 81 | 1.5 | -$10.05 | -$47.70 | -9% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 27 | 11 (41%) | 11 / 16 | 1.6 | -$5.79 | $2.54 | +2% |

*Model accuracy vs Kalshi's prices on the same 23,854 readings (excluding the final minute): V1 **+0.8%**, V2 **+1.2%**, 3-exchange price (V3/V4) **-0.4%**.*

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
| 995 | 867 (87%) | -$342.44 | -9% | 235,506 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.4%** over 36,479 readings from 1440 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 6322 | 2% | 4% | 5% |
| 10–20% | 2823 | 15% | 16% | 15% |
| 20–30% | 3040 | 25% | 26% | 25% |
| 30–40% | 3382 | 35% | 36% | 38% |
| 40–50% | 3629 | 45% | 48% | 51% |
| 50–60% | 3576 | 55% | 59% | 60% |
| 60–70% | 3166 | 65% | 70% | 73% |
| 70–80% | 2584 | 75% | 80% | 83% |
| 80–90% | 2324 | 85% | 88% | 87% |
| 90–100% | 5633 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 486 | 230 (47%) | 44¢ | 53% | $69.77 | +3% |
| 10–20¢ | 179 | 73 (41%) | 43¢ | 57% | -$68.56 | -9% |
| 20¢+ | 13 | 5 (38%) | 41¢ | 69% | -$5.51 | -10% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1205 | 576 (48%) | 46¢ | 54% | $84.48 | +1% |
| 5–10 min | 168 | 63 (38%) | 38¢ | 46% | -$23.56 | -4% |
| 2–5 min | 14 | 6 (43%) | 41¢ | 50% | $1.55 | +3% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 185 | 33 (18%) | 18¢ | 27% | -$27.41 | -8% |
| Toss-up (25–75¢) | 1089 | 514 (47%) | 45¢ | 54% | $54.07 | +1% |
| Favorite (75–95¢) | 115 | 99 (86%) | 82¢ | 89% | $35.41 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| XRP | 157 | 75 (48%) | 46¢ | 53% | $10.98 | +1% |
| BNB | 157 | 77 (49%) | 44¢ | 54% | $52.93 | +7% |
| ETH | 156 | 69 (44%) | 46¢ | 55% | -$54.80 | -7% |
| NEAR | 154 | 73 (47%) | 45¢ | 53% | $16.49 | +2% |
| SOL | 153 | 77 (50%) | 42¢ | 50% | $104.28 | +16% |
| ZEC | 153 | 65 (42%) | 41¢ | 50% | -$5.20 | -1% |
| DOGE | 153 | 66 (43%) | 44¢ | 53% | -$36.62 | -5% |
| HYPE | 153 | 66 (43%) | 44¢ | 53% | -$31.07 | -4% |
| BTC | 153 | 78 (51%) | 49¢ | 57% | $5.08 | +1% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 4:34:54 PM | BNB | UP | 10.1 min | 22¢ | 32% | 9¢ | Open | — |
| 9/29 4:34:37 PM | HYPE | DOWN | 10.4 min | 33¢ | 43% | 9¢ | Open | — |
| 9/29 4:26:58 PM | XRP | DOWN | 3.0 min | 31¢ | 41% | 9¢ | ✅ Won | $6.75 |
| 9/29 4:26:55 PM | ETH | UP | 3.1 min | 7¢ | 27% | 19¢ | ❌ Lost | -$0.75 |
| 9/29 4:26:12 PM | ZEC | UP | 3.8 min | 9¢ | 19% | 10¢ | ❌ Lost | -$0.93 |
| 9/29 4:23:54 PM | DOGE | UP | 6.1 min | 13¢ | 24% | 10¢ | ❌ Lost | -$1.38 |
| 9/29 4:23:14 PM | NEAR | UP | 6.8 min | 17¢ | 28% | 10¢ | ❌ Lost | -$1.84 |
| 9/29 4:22:35 PM | SOL | UP | 7.4 min | 19¢ | 30% | 10¢ | ❌ Lost | -$2.01 |
| 9/29 4:19:46 PM | HYPE | DOWN | 10.2 min | 58¢ | 84% | 25¢ | ✅ Won | $4.05 |
| 9/29 4:16:35 PM | BTC | DOWN | 13.4 min | 80¢ | 89% | 8¢ | ✅ Won | $1.88 |
| 9/29 4:03:12 PM | BNB | DOWN | 11.8 min | 11¢ | 17% | 5¢ | ❌ Lost | -$1.17 |
| 9/29 4:01:34 PM | NEAR | DOWN | 13.4 min | 33¢ | 39% | 5¢ | ❌ Lost | -$3.46 |
| 9/29 4:01:34 PM | ZEC | DOWN | 13.4 min | 38¢ | 48% | 8¢ | ❌ Lost | -$3.96 |
| 9/29 4:01:16 PM | BTC | UP | 13.7 min | 68¢ | 76% | 6¢ | ✅ Won | $3.04 |
| 9/29 4:01:14 PM | HYPE | DOWN | 13.8 min | 37¢ | 44% | 5¢ | ❌ Lost | -$3.87 |
| 9/29 4:01:07 PM | DOGE | UP | 13.9 min | 77¢ | 86% | 7¢ | ✅ Won | $2.17 |
| 9/29 4:01:07 PM | XRP | UP | 13.9 min | 76¢ | 82% | 5¢ | ✅ Won | $2.27 |
| 9/29 4:01:07 PM | SOL | UP | 13.9 min | 65¢ | 80% | 13¢ | ✅ Won | $3.34 |
| 9/29 4:01:07 PM | ETH | UP | 13.9 min | 77¢ | 86% | 7¢ | ✅ Won | $2.17 |
| 9/29 3:49:25 PM | NEAR | DOWN | 10.6 min | 33¢ | 39% | 4¢ | ❌ Lost | -$3.46 |
| 9/29 3:47:07 PM | DOGE | DOWN | 12.9 min | 68¢ | 75% | 5¢ | ❌ Lost | -$6.98 |
| 9/29 3:46:53 PM | SOL | UP | 13.1 min | 26¢ | 31% | 4¢ | ✅ Won | $7.31 |
| 9/29 3:46:22 PM | XRP | UP | 13.6 min | 30¢ | 38% | 6¢ | ✅ Won | $6.85 |
| 9/29 3:46:18 PM | HYPE | DOWN | 13.7 min | 68¢ | 74% | 5¢ | ❌ Lost | -$6.96 |
| 9/29 3:46:04 PM | ETH | DOWN | 13.9 min | 78¢ | 86% | 7¢ | ✅ Won | $2.07 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
