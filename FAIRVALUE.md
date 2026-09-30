# Fair-Value Bot

*Updated Wed Sep 30, 12:34 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1713 | $302.97 | +4% | $157.47 / $145.50 |
| 4¢+ | 1665 | $391.24 | +5% | $350.33 / $40.91 |
| 6¢+ | 1539 | $321.00 | +5% | $378.62 / -$57.62 |
| 8¢+ ← live bot | 1341 | $441.14 | +8% | $391.12 / $50.02 |
| 10¢+ | 1141 | $439.93 | +10% | $293.58 / $146.35 |
| 15¢+ | 703 | $460.77 | +19% | $258.60 / $202.17 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1613 | 1608 | 744 (46%) | 44¢ | 53% | $133.19 | +2% | +3.8¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 227 | 154 | 100 / 54 | $76.89 | $72.24 | -$4.65 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1206 | 518 (43%) | 356 / 850 | 8.3 | -$43.45 | -$287.72 | -5% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1075 | 359 (33%) | 450 / 625 | 7.4 | -$55.90 | -$392.37 | -10% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 274 | 96 (35%) | 70 / 204 | 2.0 | -$14.97 | -$103.17 | -10% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 289 | 129 (45%) | 89 / 200 | 2.0 | -$13.69 | $18.24 | +1% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 170 | 73 (43%) | 59 / 111 | 1.5 | -$10.05 | -$41.99 | -6% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 3 | 3 (100%) | 0 / 3 | 1.0 | $0.97 | $4.52 | +18% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 39 | 14 (36%) | 15 / 24 | 1.6 | -$5.89 | -$6.48 | -4% |

*Model accuracy vs Kalshi's prices on the same 30,823 readings (excluding the final minute): V1 **+0.8%**, V2 **+1.3%**, 3-exchange price (V3/V4) **-0.3%**.*

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
| 1214 | 1086 (89%) | -$271.32 | -6% | 246,720 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.4%** over 43,968 readings from 1728 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 7748 | 3% | 4% | 5% |
| 10–20% | 3384 | 15% | 17% | 16% |
| 20–30% | 3701 | 25% | 26% | 26% |
| 30–40% | 4102 | 35% | 37% | 39% |
| 40–50% | 4412 | 45% | 48% | 50% |
| 50–60% | 4286 | 55% | 59% | 58% |
| 60–70% | 3791 | 65% | 71% | 71% |
| 70–80% | 3142 | 75% | 80% | 82% |
| 80–90% | 2828 | 85% | 88% | 87% |
| 90–100% | 6574 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 589 | 279 (47%) | 44¢ | 53% | $132.56 | +5% |
| 10–20¢ | 290 | 121 (42%) | 42¢ | 56% | -$52.00 | -4% |
| 20¢+ | 18 | 6 (33%) | 39¢ | 67% | -$13.74 | -19% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1332 | 634 (48%) | 45¢ | 54% | $92.06 | +1% |
| 5–10 min | 228 | 92 (40%) | 38¢ | 47% | $32.94 | +4% |
| 2–5 min | 41 | 15 (37%) | 32¢ | 44% | $12.78 | +9% |
| 1–2 min | 5 | 1 (20%) | 36¢ | 57% | -$8.51 | -46% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 234 | 40 (17%) | 18¢ | 27% | -$50.04 | -11% |
| Toss-up (25–75¢) | 1248 | 594 (48%) | 45¢ | 54% | $128.04 | +2% |
| Favorite (75–95¢) | 126 | 110 (87%) | 82¢ | 90% | $55.19 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 186 | 87 (47%) | 43¢ | 54% | $39.57 | +5% |
| ETH | 185 | 83 (45%) | 46¢ | 55% | -$51.06 | -6% |
| XRP | 180 | 84 (47%) | 45¢ | 54% | -$5.88 | -1% |
| HYPE | 180 | 82 (46%) | 43¢ | 53% | $13.21 | +2% |
| ZEC | 178 | 76 (43%) | 40¢ | 50% | $12.58 | +2% |
| BTC | 178 | 92 (52%) | 50¢ | 58% | $7.85 | +1% |
| NEAR | 175 | 80 (46%) | 44¢ | 52% | $11.37 | +1% |
| DOGE | 174 | 73 (42%) | 42¢ | 51% | -$30.86 | -4% |
| SOL | 172 | 87 (51%) | 41¢ | 50% | $136.41 | +19% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/30 12:33:13 AM | DOGE | DOWN | 11.8 min | 65¢ | 76% | 10¢ | Open | — |
| 9/30 12:32:15 AM | BNB | UP | 12.8 min | 31¢ | 45% | 13¢ | Open | — |
| 9/30 12:31:54 AM | HYPE | DOWN | 13.1 min | 74¢ | 86% | 10¢ | Open | — |
| 9/30 12:31:17 AM | ETH | DOWN | 13.7 min | 67¢ | 79% | 10¢ | Open | — |
| 9/30 12:31:17 AM | BTC | DOWN | 13.7 min | 62¢ | 72% | 9¢ | Open | — |
| 9/30 12:20:32 AM | ZEC | DOWN | 9.5 min | 41¢ | 54% | 11¢ | ✅ Won | $5.73 |
| 9/30 12:20:32 AM | HYPE | DOWN | 9.5 min | 50¢ | 60% | 8¢ | ✅ Won | $4.82 |
| 9/30 12:18:47 AM | NEAR | DOWN | 11.2 min | 19¢ | 30% | 10¢ | ❌ Lost | -$2.00 |
| 9/30 12:18:15 AM | BTC | DOWN | 11.8 min | 53¢ | 64% | 9¢ | ✅ Won | $4.52 |
| 9/30 12:17:32 AM | BNB | DOWN | 12.4 min | 40¢ | 54% | 12¢ | ✅ Won | $5.80 |
| 9/30 12:17:11 AM | DOGE | DOWN | 12.8 min | 25¢ | 36% | 10¢ | ✅ Won | $7.34 |
| 9/30 12:16:42 AM | XRP | DOWN | 13.3 min | 35¢ | 47% | 10¢ | ✅ Won | $6.34 |
| 9/30 12:16:42 AM | SOL | DOWN | 13.3 min | 39¢ | 49% | 8¢ | ✅ Won | $5.93 |
| 9/30 12:16:19 AM | ETH | DOWN | 13.7 min | 54¢ | 73% | 17¢ | ✅ Won | $4.42 |
| 9/30 12:08:19 AM | ZEC | UP | 6.7 min | 16¢ | 28% | 11¢ | ❌ Lost | -$1.70 |
| 9/30 12:06:41 AM | BNB | UP | 8.3 min | 31¢ | 44% | 11¢ | ❌ Lost | -$3.25 |
| 9/30 12:03:13 AM | SOL | UP | 11.8 min | 34¢ | 47% | 11¢ | ❌ Lost | -$3.58 |
| 9/30 12:02:56 AM | HYPE | DOWN | 12.1 min | 46¢ | 60% | 11¢ | ✅ Won | $5.19 |
| 9/30 12:02:21 AM | ETH | DOWN | 12.7 min | 62¢ | 73% | 9¢ | ✅ Won | $3.63 |
| 9/29 11:59:08 PM | XRP | DOWN | 0.9 min | 72¢ | 100% | 26¢ | ✅ Won | $2.61 |
| 9/29 11:59:08 PM | HYPE | DOWN | 0.9 min | 86¢ | 100% | 13¢ | ✅ Won | $1.31 |
| 9/29 11:52:48 PM | DOGE | UP | 7.2 min | 13¢ | 28% | 14¢ | ❌ Lost | -$1.38 |
| 9/29 11:51:17 PM | NEAR | DOWN | 8.7 min | 43¢ | 54% | 9¢ | ✅ Won | $5.52 |
| 9/29 11:51:10 PM | BNB | UP | 8.8 min | 16¢ | 31% | 14¢ | ❌ Lost | -$1.70 |
| 9/29 11:35:36 PM | ETH | DOWN | 9.4 min | 32¢ | 42% | 9¢ | ❌ Lost | -$3.36 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
