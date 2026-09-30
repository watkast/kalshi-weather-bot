# Fair-Value Bot

*Updated Wed Sep 30, 5:13 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1875 | $183.81 | +2% | $94.52 / $89.29 |
| 4¢+ | 1823 | $328.10 | +4% | $327.48 / $0.62 |
| 6¢+ | 1692 | $268.79 | +4% | $307.45 / -$38.66 |
| 8¢+ ← live bot | 1477 | $414.21 | +7% | $304.43 / $109.78 |
| 10¢+ | 1260 | $443.84 | +9% | $217.03 / $226.81 |
| 15¢+ | 779 | $556.71 | +21% | $206.26 / $350.45 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1740 | 1737 | 780 (45%) | 43¢ | 53% | $22.38 | +0% | +3.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 356 | 234 | 144 / 90 | -$33.92 | $51.81 | $85.73 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1335 | 554 (41%) | 384 / 951 | 8.1 | -$43.45 | -$398.53 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1208 | 404 (33%) | 498 / 710 | 7.4 | -$55.90 | -$408.20 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 305 | 103 (34%) | 75 / 230 | 2.0 | -$14.97 | -$135.00 | -12% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 323 | 140 (43%) | 96 / 227 | 2.0 | -$13.69 | -$6.32 | -0% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 195 | 80 (41%) | 66 / 129 | 1.5 | -$10.05 | -$77.25 | -10% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 3 | 3 (100%) | 0 / 3 | 1.0 | $0.97 | $4.52 | +18% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 45 | 15 (33%) | 16 / 29 | 1.5 | -$5.89 | -$13.12 | -8% |

*Model accuracy vs Kalshi's prices on the same 34,550 readings (excluding the final minute): V1 **+0.4%**, V2 **+1.1%**, 3-exchange price (V3/V4) **-0.7%**.*

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
| 1343 | 1215 (90%) | -$382.13 | -7% | 250,759 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.1%** over 48,001 readings from 1890 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 8197 | 3% | 4% | 5% |
| 10–20% | 3642 | 15% | 17% | 15% |
| 20–30% | 3970 | 25% | 26% | 26% |
| 30–40% | 4391 | 35% | 37% | 39% |
| 40–50% | 4743 | 45% | 48% | 51% |
| 50–60% | 4679 | 55% | 59% | 59% |
| 60–70% | 4127 | 65% | 71% | 72% |
| 70–80% | 3454 | 75% | 80% | 83% |
| 80–90% | 3229 | 85% | 88% | 89% |
| 90–100% | 7569 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 650 | 292 (45%) | 43¢ | 52% | $48.97 | +2% |
| 10–20¢ | 355 | 142 (40%) | 41¢ | 55% | -$86.54 | -6% |
| 20¢+ | 21 | 8 (38%) | 40¢ | 67% | -$6.42 | -7% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1405 | 651 (46%) | 45¢ | 54% | -$23.96 | -0% |
| 5–10 min | 266 | 99 (37%) | 36¢ | 46% | -$11.60 | -1% |
| 2–5 min | 58 | 26 (45%) | 33¢ | 45% | $60.84 | +31% |
| 1–2 min | 6 | 2 (33%) | 44¢ | 63% | -$6.82 | -25% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 274 | 43 (16%) | 18¢ | 27% | -$92.86 | -18% |
| Toss-up (25–75¢) | 1332 | 622 (47%) | 45¢ | 54% | $50.23 | +1% |
| Favorite (75–95¢) | 131 | 115 (88%) | 82¢ | 90% | $65.01 | +6% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 204 | 90 (44%) | 42¢ | 54% | $1.83 | +0% |
| ETH | 201 | 90 (45%) | 46¢ | 55% | -$50.82 | -5% |
| HYPE | 197 | 85 (43%) | 43¢ | 52% | -$18.62 | -2% |
| XRP | 193 | 86 (45%) | 44¢ | 53% | -$26.11 | -3% |
| BTC | 193 | 99 (51%) | 49¢ | 58% | $14.71 | +2% |
| ZEC | 191 | 78 (41%) | 39¢ | 49% | -$0.07 | -0% |
| DOGE | 190 | 78 (41%) | 42¢ | 51% | -$41.11 | -5% |
| NEAR | 186 | 83 (45%) | 43¢ | 51% | $4.51 | +1% |
| SOL | 182 | 91 (50%) | 41¢ | 50% | $138.06 | +18% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/30 5:05:03 AM | NEAR | DOWN | 9.9 min | 30¢ | 45% | 13¢ | Open | — |
| 9/30 5:03:17 AM | HYPE | DOWN | 11.7 min | 45¢ | 61% | 15¢ | Open | — |
| 9/30 5:01:15 AM | BNB | DOWN | 13.7 min | 67¢ | 79% | 10¢ | Open | — |
| 9/30 4:57:05 AM | BTC | UP | 2.9 min | 63¢ | 76% | 11¢ | ✅ Won | $3.53 |
| 9/30 4:56:44 AM | SOL | UP | 3.3 min | 43¢ | 67% | 22¢ | ✅ Won | $5.52 |
| 9/30 4:52:36 AM | DOGE | DOWN | 7.4 min | 32¢ | 51% | 17¢ | ❌ Lost | -$3.36 |
| 9/30 4:52:22 AM | BNB | DOWN | 7.6 min | 41¢ | 57% | 14¢ | ❌ Lost | -$4.27 |
| 9/30 4:51:19 AM | ETH | DOWN | 8.7 min | 54¢ | 66% | 10¢ | ❌ Lost | -$5.58 |
| 9/30 4:49:08 AM | HYPE | DOWN | 10.8 min | 45¢ | 60% | 13¢ | ❌ Lost | -$4.68 |
| 9/30 4:47:51 AM | XRP | UP | 12.1 min | 25¢ | 36% | 10¢ | ❌ Lost | -$2.64 |
| 9/30 4:37:11 AM | DOGE | DOWN | 7.8 min | 24¢ | 38% | 13¢ | ❌ Lost | -$2.53 |
| 9/30 4:34:02 AM | BTC | DOWN | 11.0 min | 22¢ | 31% | 8¢ | ❌ Lost | -$2.33 |
| 9/30 4:33:24 AM | ETH | DOWN | 11.6 min | 19¢ | 29% | 8¢ | ❌ Lost | -$2.01 |
| 9/30 4:31:40 AM | NEAR | DOWN | 13.3 min | 26¢ | 43% | 16¢ | ❌ Lost | -$2.70 |
| 9/30 4:31:08 AM | BNB | DOWN | 13.9 min | 38¢ | 51% | 12¢ | ❌ Lost | -$3.97 |
| 9/30 4:31:08 AM | HYPE | DOWN | 13.9 min | 26¢ | 46% | 19¢ | ❌ Lost | -$2.69 |
| 9/30 4:27:55 AM | BTC | DOWN | 2.1 min | 9¢ | 19% | 10¢ | ❌ Lost | -$0.96 |
| 9/30 4:27:51 AM | XRP | UP | 2.1 min | 48¢ | 65% | 15¢ | ✅ Won | $5.02 |
| 9/30 4:26:10 AM | ETH | DOWN | 3.8 min | 10¢ | 21% | 10¢ | ❌ Lost | -$1.06 |
| 9/30 4:21:24 AM | BNB | DOWN | 8.6 min | 37¢ | 47% | 8¢ | ❌ Lost | -$3.87 |
| 9/30 4:19:22 AM | NEAR | DOWN | 10.6 min | 34¢ | 49% | 13¢ | ❌ Lost | -$3.54 |
| 9/30 4:18:31 AM | ZEC | DOWN | 11.5 min | 38¢ | 51% | 11¢ | ❌ Lost | -$4.00 |
| 9/30 4:16:10 AM | HYPE | DOWN | 13.8 min | 55¢ | 73% | 16¢ | ❌ Lost | -$5.68 |
| 9/30 4:11:14 AM | SOL | UP | 3.8 min | 30¢ | 40% | 8¢ | ✅ Won | $6.85 |
| 9/30 4:10:18 AM | XRP | UP | 4.7 min | 29¢ | 40% | 9¢ | ❌ Lost | -$3.05 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
