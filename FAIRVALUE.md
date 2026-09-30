# Fair-Value Bot

*Updated Tue Sep 29, 11:13 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1659 | $259.24 | +3% | $166.25 / $92.99 |
| 4¢+ | 1611 | $342.38 | +5% | $364.23 / -$21.85 |
| 6¢+ | 1486 | $263.22 | +4% | $390.68 / -$127.46 |
| 8¢+ ← live bot | 1298 | $360.00 | +7% | $382.63 / -$22.63 |
| 10¢+ | 1106 | $387.29 | +9% | $292.16 / $95.13 |
| 15¢+ | 681 | $439.58 | +19% | $246.88 / $192.70 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1572 | 1564 | 721 (46%) | 44¢ | 53% | $90.61 | +1% | +3.9¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 183 | 130 | 82 / 48 | $34.31 | $52.97 | $18.66 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1162 | 495 (43%) | 345 / 817 | 8.3 | -$43.45 | -$330.30 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1026 | 343 (33%) | 433 / 593 | 7.3 | -$55.90 | -$372.67 | -10% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 262 | 90 (34%) | 69 / 193 | 2.0 | -$14.97 | -$123.69 | -12% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 277 | 121 (44%) | 84 / 193 | 2.0 | -$13.69 | $6.95 | +1% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 161 | 69 (43%) | 56 / 105 | 1.5 | -$10.05 | -$38.58 | -6% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 2 | 2 (100%) | 0 / 2 | 1.0 | $0.97 | $2.64 | +15% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 37 | 14 (38%) | 14 / 23 | 1.5 | -$5.89 | -$0.89 | -1% |

*Model accuracy vs Kalshi's prices on the same 29,574 readings (excluding the final minute): V1 **+0.5%**, V2 **+1.1%**, 3-exchange price (V3/V4) **-0.6%**.*

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
| 1170 | 1042 (89%) | -$313.90 | -7% | 244,038 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.2%** over 42,622 readings from 1674 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 7476 | 3% | 4% | 5% |
| 10–20% | 3323 | 15% | 17% | 16% |
| 20–30% | 3604 | 25% | 26% | 27% |
| 30–40% | 3997 | 35% | 37% | 39% |
| 40–50% | 4286 | 45% | 48% | 51% |
| 50–60% | 4172 | 55% | 59% | 59% |
| 60–70% | 3679 | 65% | 70% | 72% |
| 70–80% | 3009 | 75% | 80% | 82% |
| 80–90% | 2690 | 85% | 88% | 87% |
| 90–100% | 6386 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 574 | 270 (47%) | 44¢ | 53% | $106.84 | +4% |
| 10–20¢ | 263 | 108 (41%) | 42¢ | 56% | -$67.74 | -6% |
| 20¢+ | 16 | 5 (31%) | 39¢ | 67% | -$14.86 | -23% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1299 | 617 (47%) | 45¢ | 54% | $64.21 | +1% |
| 5–10 min | 219 | 88 (40%) | 38¢ | 47% | $22.13 | +3% |
| 2–5 min | 41 | 15 (37%) | 32¢ | 44% | $12.78 | +9% |
| 1–2 min | 5 | 1 (20%) | 36¢ | 57% | -$8.51 | -46% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 222 | 39 (18%) | 18¢ | 27% | -$37.28 | -9% |
| Toss-up (25–75¢) | 1220 | 576 (47%) | 45¢ | 54% | $79.48 | +1% |
| Favorite (75–95¢) | 122 | 106 (87%) | 82¢ | 89% | $48.41 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| ETH | 180 | 80 (44%) | 46¢ | 55% | -$56.11 | -7% |
| BNB | 180 | 86 (48%) | 43¢ | 54% | $49.84 | +6% |
| XRP | 175 | 80 (46%) | 45¢ | 53% | -$15.31 | -2% |
| BTC | 175 | 89 (51%) | 49¢ | 58% | -$0.74 | -0% |
| HYPE | 174 | 78 (45%) | 43¢ | 53% | $0.81 | +0% |
| ZEC | 173 | 74 (43%) | 41¢ | 50% | $6.19 | +1% |
| NEAR | 170 | 78 (46%) | 44¢ | 52% | $6.57 | +1% |
| DOGE | 169 | 71 (42%) | 43¢ | 52% | -$35.30 | -5% |
| SOL | 168 | 85 (51%) | 41¢ | 50% | $134.66 | +19% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 11:05:53 PM | NEAR | DOWN | 9.1 min | 37¢ | 49% | 10¢ | Open | — |
| 9/29 11:04:54 PM | ETH | DOWN | 10.1 min | 35¢ | 49% | 13¢ | Open | — |
| 9/29 11:04:25 PM | HYPE | DOWN | 10.6 min | 21¢ | 35% | 13¢ | Open | — |
| 9/29 11:04:10 PM | DOGE | DOWN | 10.8 min | 22¢ | 31% | 8¢ | Open | — |
| 9/29 11:02:59 PM | ZEC | DOWN | 12.0 min | 15¢ | 24% | 8¢ | Open | — |
| 9/29 11:02:45 PM | XRP | UP | 12.2 min | 79¢ | 91% | 11¢ | Open | — |
| 9/29 11:01:21 PM | BTC | UP | 13.6 min | 87¢ | 98% | 10¢ | Open | — |
| 9/29 11:01:12 PM | BNB | DOWN | 13.8 min | 14¢ | 37% | 23¢ | Open | — |
| 9/29 10:50:32 PM | BTC | DOWN | 9.5 min | 76¢ | 87% | 10¢ | ✅ Won | $2.27 |
| 9/29 10:49:27 PM | DOGE | DOWN | 10.6 min | 52¢ | 64% | 10¢ | ✅ Won | $4.62 |
| 9/29 10:48:39 PM | ZEC | DOWN | 11.3 min | 31¢ | 42% | 9¢ | ✅ Won | $6.77 |
| 9/29 10:47:39 PM | ETH | DOWN | 12.3 min | 47¢ | 57% | 8¢ | ✅ Won | $5.12 |
| 9/29 10:47:39 PM | NEAR | DOWN | 12.3 min | 38¢ | 49% | 9¢ | ✅ Won | $6.03 |
| 9/29 10:46:30 PM | HYPE | DOWN | 13.5 min | 41¢ | 51% | 8¢ | ✅ Won | $5.73 |
| 9/29 10:46:02 PM | BNB | DOWN | 14.0 min | 50¢ | 62% | 10¢ | ✅ Won | $4.82 |
| 9/29 10:37:51 PM | HYPE | DOWN | 7.2 min | 47¢ | 61% | 12¢ | ✅ Won | $5.12 |
| 9/29 10:36:14 PM | ETH | DOWN | 8.8 min | 40¢ | 50% | 9¢ | ✅ Won | $5.83 |
| 9/29 10:36:14 PM | BNB | UP | 8.8 min | 32¢ | 44% | 11¢ | ❌ Lost | -$3.36 |
| 9/29 10:35:56 PM | NEAR | DOWN | 9.1 min | 51¢ | 61% | 8¢ | ❌ Lost | -$5.27 |
| 9/29 10:35:36 PM | XRP | UP | 9.4 min | 22¢ | 33% | 9¢ | ❌ Lost | -$2.33 |
| 9/29 10:34:17 PM | BTC | DOWN | 10.7 min | 64¢ | 75% | 9¢ | ✅ Won | $3.43 |
| 9/29 10:33:34 PM | ZEC | UP | 11.4 min | 27¢ | 38% | 10¢ | ❌ Lost | -$2.84 |
| 9/29 10:21:06 PM | ZEC | DOWN | 8.9 min | 17¢ | 26% | 8¢ | ❌ Lost | -$1.80 |
| 9/29 10:21:06 PM | NEAR | DOWN | 8.9 min | 38¢ | 54% | 15¢ | ❌ Lost | -$3.97 |
| 9/29 10:20:38 PM | ETH | DOWN | 9.4 min | 38¢ | 53% | 13¢ | ✅ Won | $6.03 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
