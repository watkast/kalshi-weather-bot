# Fair-Value Bot

*Updated Tue Sep 29, 8:08 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **10¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **10¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1551 | $155.50 | +2% | $127.13 / $28.37 |
| 4¢+ | 1504 | $261.54 | +4% | $338.52 / -$76.98 |
| 6¢+ | 1387 | $235.20 | +4% | $306.36 / -$71.16 |
| 8¢+ ← live bot | 1210 | $350.84 | +7% | $340.23 / $10.61 |
| 10¢+ | 1029 | $352.35 | +9% | $285.22 / $67.13 |
| 15¢+ | 625 | $351.55 | +16% | $257.25 / $94.30 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1495 | 1487 | 687 (46%) | 44¢ | 53% | $63.83 | +1% | +4.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 106 | 77 | 46 / 31 | $7.53 | $3.96 | -$3.57 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1085 | 461 (42%) | 334 / 751 | 8.4 | -$43.45 | -$357.08 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 946 | 320 (34%) | 412 / 534 | 7.3 | -$55.90 | -$320.61 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 240 | 81 (34%) | 66 / 174 | 2.0 | -$14.97 | -$115.27 | -12% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 253 | 107 (42%) | 78 / 175 | 2.0 | -$13.69 | -$31.60 | -3% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 146 | 62 (42%) | 52 / 94 | 1.5 | -$10.05 | -$39.54 | -7% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 1 | 1 (100%) | 0 / 1 | 1.0 | $1.67 | $1.67 | +20% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 32 | 12 (38%) | 12 / 20 | 1.5 | -$5.89 | -$5.03 | -4% |

*Model accuracy vs Kalshi's prices on the same 26,971 readings (excluding the final minute): V1 **+0.1%**, V2 **+1.0%**, 3-exchange price (V3/V4) **-1.0%**.*

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
| 1093 | 965 (88%) | -$340.68 | -8% | 239,045 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+3.9%** over 39,848 readings from 1566 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 6933 | 3% | 4% | 5% |
| 10–20% | 3091 | 15% | 16% | 16% |
| 20–30% | 3337 | 25% | 26% | 28% |
| 30–40% | 3711 | 35% | 36% | 39% |
| 40–50% | 3979 | 45% | 48% | 52% |
| 50–60% | 3907 | 55% | 59% | 60% |
| 60–70% | 3446 | 65% | 70% | 72% |
| 70–80% | 2848 | 75% | 80% | 83% |
| 80–90% | 2514 | 85% | 88% | 87% |
| 90–100% | 6082 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 530 | 247 (47%) | 44¢ | 53% | $54.30 | +2% |
| 10–20¢ | 231 | 97 (42%) | 42¢ | 56% | -$44.62 | -4% |
| 20¢+ | 15 | 5 (33%) | 40¢ | 68% | -$12.22 | -20% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1255 | 596 (47%) | 45¢ | 54% | $53.51 | +1% |
| 5–10 min | 197 | 78 (40%) | 38¢ | 47% | $9.56 | +1% |
| 2–5 min | 31 | 12 (39%) | 35¢ | 46% | $6.84 | +6% |
| 1–2 min | 4 | 1 (25%) | 39¢ | 61% | -$6.08 | -38% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 207 | 38 (18%) | 18¢ | 27% | -$20.36 | -5% |
| Toss-up (25–75¢) | 1162 | 547 (47%) | 45¢ | 54% | $43.51 | +1% |
| Favorite (75–95¢) | 118 | 102 (86%) | 82¢ | 89% | $40.68 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 170 | 83 (49%) | 44¢ | 54% | $58.55 | +8% |
| XRP | 169 | 79 (47%) | 45¢ | 54% | -$3.20 | -0% |
| ETH | 169 | 74 (44%) | 46¢ | 55% | -$66.26 | -8% |
| ZEC | 164 | 70 (43%) | 41¢ | 50% | $1.59 | +0% |
| HYPE | 164 | 70 (43%) | 43¢ | 53% | -$36.15 | -5% |
| BTC | 164 | 83 (51%) | 50¢ | 58% | -$7.67 | -1% |
| SOL | 163 | 84 (52%) | 41¢ | 50% | $142.47 | +20% |
| NEAR | 162 | 75 (46%) | 45¢ | 53% | $3.50 | +0% |
| DOGE | 162 | 69 (43%) | 43¢ | 52% | -$29.00 | -4% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 8:04:43 PM | ZEC | DOWN | 10.3 min | 38¢ | 50% | 11¢ | Open | — |
| 9/29 8:04:26 PM | SOL | UP | 10.6 min | 80¢ | 89% | 8¢ | Open | — |
| 9/29 8:03:11 PM | DOGE | DOWN | 11.8 min | 37¢ | 47% | 9¢ | Open | — |
| 9/29 8:03:11 PM | XRP | DOWN | 11.8 min | 48¢ | 59% | 10¢ | Open | — |
| 9/29 8:02:19 PM | HYPE | DOWN | 12.7 min | 52¢ | 63% | 9¢ | Open | — |
| 9/29 8:02:18 PM | ETH | DOWN | 12.7 min | 31¢ | 41% | 9¢ | Open | — |
| 9/29 8:01:14 PM | NEAR | DOWN | 13.8 min | 25¢ | 38% | 11¢ | Open | — |
| 9/29 8:01:03 PM | BNB | DOWN | 13.9 min | 39¢ | 57% | 17¢ | Open | — |
| 9/29 7:56:50 PM | BTC | DOWN | 3.2 min | 56¢ | 71% | 13¢ | ❌ Lost | -$5.78 |
| 9/29 7:56:02 PM | DOGE | UP | 4.0 min | 20¢ | 30% | 9¢ | ❌ Lost | -$2.12 |
| 9/29 7:55:05 PM | SOL | DOWN | 4.9 min | 42¢ | 53% | 9¢ | ✅ Won | $5.62 |
| 9/29 7:54:48 PM | XRP | UP | 5.2 min | 35¢ | 52% | 15¢ | ❌ Lost | -$3.66 |
| 9/29 7:52:34 PM | NEAR | DOWN | 7.4 min | 58¢ | 68% | 8¢ | ✅ Won | $4.02 |
| 9/29 7:48:57 PM | HYPE | DOWN | 11.1 min | 56¢ | 71% | 14¢ | ✅ Won | $4.22 |
| 9/29 7:47:32 PM | ETH | DOWN | 12.5 min | 50¢ | 60% | 8¢ | ✅ Won | $4.82 |
| 9/29 7:46:05 PM | BNB | DOWN | 13.9 min | 44¢ | 56% | 11¢ | ❌ Lost | -$4.55 |
| 9/29 7:41:11 PM | HYPE | DOWN | 3.8 min | 49¢ | 62% | 11¢ | ❌ Lost | -$5.08 |
| 9/29 7:40:23 PM | DOGE | UP | 4.6 min | 9¢ | 17% | 8¢ | ❌ Lost | -$0.93 |
| 9/29 7:39:50 PM | SOL | UP | 5.2 min | 25¢ | 35% | 9¢ | ✅ Won | $7.36 |
| 9/29 7:32:29 PM | XRP | DOWN | 12.5 min | 72¢ | 83% | 10¢ | ❌ Lost | -$7.35 |
| 9/29 7:31:41 PM | ETH | DOWN | 13.3 min | 68¢ | 85% | 15¢ | ✅ Won | $3.04 |
| 9/29 7:31:27 PM | BNB | DOWN | 13.5 min | 55¢ | 68% | 11¢ | ✅ Won | $4.32 |
| 9/29 7:31:12 PM | BTC | DOWN | 13.8 min | 62¢ | 75% | 11¢ | ✅ Won | $3.63 |
| 9/29 7:31:12 PM | ZEC | DOWN | 13.8 min | 44¢ | 57% | 11¢ | ❌ Lost | -$4.58 |
| 9/29 7:27:24 PM | ETH | DOWN | 2.6 min | 7¢ | 18% | 11¢ | ❌ Lost | -$0.77 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
