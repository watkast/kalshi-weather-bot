# Fair-Value Bot

*Updated Wed Sep 30, 2:15 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1776 | $307.72 | +4% | $72.77 / $234.95 |
| 4¢+ | 1726 | $429.66 | +5% | $270.10 / $159.56 |
| 6¢+ | 1598 | $351.79 | +5% | $333.15 / $18.64 |
| 8¢+ ← live bot | 1393 | $499.07 | +9% | $350.36 / $148.71 |
| 10¢+ | 1184 | $516.02 | +11% | $281.22 / $234.80 |
| 15¢+ | 730 | $565.20 | +22% | $224.05 / $341.15 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1658 | 1658 | 763 (46%) | 44¢ | 53% | $131.28 | +2% | +3.5¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 277 | 183 | 117 / 66 | $74.98 | $79.35 | $4.37 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1256 | 537 (43%) | 366 / 890 | 8.2 | -$43.45 | -$289.63 | -5% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1125 | 380 (34%) | 466 / 659 | 7.4 | -$55.90 | -$389.61 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 285 | 102 (36%) | 72 / 213 | 2.0 | -$14.97 | -$94.99 | -9% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 303 | 135 (45%) | 90 / 213 | 2.0 | -$13.69 | $15.23 | +1% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 181 | 77 (43%) | 63 / 118 | 1.5 | -$10.05 | -$48.50 | -7% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 3 | 3 (100%) | 0 / 3 | 1.0 | $0.97 | $4.52 | +18% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 41 | 15 (37%) | 15 / 26 | 1.5 | -$5.89 | -$2.06 | -1% |

*Model accuracy vs Kalshi's prices on the same 32,305 readings (excluding the final minute): V1 **+0.9%**, V2 **+1.3%**, 3-exchange price (V3/V4) **-0.1%**.*

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
| 1264 | 1136 (90%) | -$273.23 | -5% | 249,182 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.6%** over 45,567 readings from 1791 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 8095 | 3% | 4% | 5% |
| 10–20% | 3538 | 15% | 17% | 15% |
| 20–30% | 3863 | 25% | 26% | 26% |
| 30–40% | 4255 | 35% | 37% | 38% |
| 40–50% | 4534 | 45% | 48% | 50% |
| 50–60% | 4432 | 55% | 59% | 58% |
| 60–70% | 3891 | 65% | 71% | 71% |
| 70–80% | 3198 | 75% | 80% | 82% |
| 80–90% | 2896 | 85% | 88% | 88% |
| 90–100% | 6865 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 612 | 286 (47%) | 43¢ | 53% | $115.66 | +4% |
| 10–20¢ | 315 | 132 (42%) | 42¢ | 56% | -$38.81 | -3% |
| 20¢+ | 20 | 7 (35%) | 39¢ | 67% | -$11.94 | -15% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1360 | 644 (47%) | 45¢ | 54% | $74.77 | +1% |
| 5–10 min | 245 | 98 (40%) | 37¢ | 46% | $39.98 | +4% |
| 2–5 min | 45 | 17 (38%) | 32¢ | 44% | $19.43 | +13% |
| 1–2 min | 6 | 2 (33%) | 44¢ | 63% | -$6.82 | -25% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 250 | 43 (17%) | 18¢ | 27% | -$49.66 | -10% |
| Toss-up (25–75¢) | 1281 | 609 (48%) | 45¢ | 54% | $124.06 | +2% |
| Favorite (75–95¢) | 127 | 111 (87%) | 82¢ | 90% | $56.88 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 193 | 90 (47%) | 43¢ | 54% | $39.52 | +5% |
| ETH | 192 | 87 (45%) | 46¢ | 55% | -$46.05 | -5% |
| HYPE | 186 | 84 (45%) | 43¢ | 53% | $12.09 | +1% |
| XRP | 184 | 84 (46%) | 45¢ | 54% | -$18.32 | -2% |
| BTC | 184 | 95 (52%) | 49¢ | 58% | $15.28 | +2% |
| ZEC | 183 | 76 (42%) | 40¢ | 50% | -$2.87 | -0% |
| DOGE | 180 | 76 (42%) | 42¢ | 51% | -$21.62 | -3% |
| NEAR | 179 | 83 (46%) | 43¢ | 52% | $26.81 | +3% |
| SOL | 177 | 88 (50%) | 41¢ | 50% | $126.44 | +17% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/30 2:09:44 AM | HYPE | UP | 5.3 min | 9¢ | 19% | 9¢ | ❌ Lost | -$1.00 |
| 9/30 2:05:38 AM | NEAR | DOWN | 9.4 min | 25¢ | 36% | 9¢ | ✅ Won | $7.36 |
| 9/30 2:05:36 AM | BTC | DOWN | 9.4 min | 72¢ | 82% | 8¢ | ✅ Won | $2.65 |
| 9/30 2:04:59 AM | XRP | UP | 10.0 min | 32¢ | 42% | 8¢ | ❌ Lost | -$3.36 |
| 9/30 2:03:44 AM | BNB | DOWN | 11.2 min | 68¢ | 80% | 11¢ | ✅ Won | $3.04 |
| 9/30 2:03:13 AM | ETH | DOWN | 11.8 min | 71¢ | 81% | 9¢ | ✅ Won | $2.75 |
| 9/30 1:55:05 AM | BTC | UP | 4.9 min | 34¢ | 45% | 9¢ | ❌ Lost | -$3.56 |
| 9/30 1:51:25 AM | ETH | DOWN | 8.6 min | 33¢ | 47% | 12¢ | ✅ Won | $6.54 |
| 9/30 1:51:03 AM | DOGE | DOWN | 8.9 min | 20¢ | 32% | 10¢ | ✅ Won | $7.88 |
| 9/30 1:50:39 AM | BNB | DOWN | 9.3 min | 50¢ | 60% | 8¢ | ✅ Won | $4.82 |
| 9/30 1:50:13 AM | NEAR | DOWN | 9.8 min | 28¢ | 40% | 10¢ | ✅ Won | $7.05 |
| 9/30 1:48:52 AM | HYPE | DOWN | 11.1 min | 32¢ | 47% | 13¢ | ❌ Lost | -$3.36 |
| 9/30 1:46:52 AM | ZEC | DOWN | 13.1 min | 46¢ | 59% | 11¢ | ❌ Lost | -$4.76 |
| 9/30 1:38:41 AM | BTC | DOWN | 6.3 min | 9¢ | 18% | 8¢ | ❌ Lost | -$0.96 |
| 9/30 1:38:41 AM | SOL | DOWN | 6.3 min | 10¢ | 19% | 8¢ | ❌ Lost | -$1.03 |
| 9/30 1:38:07 AM | XRP | DOWN | 6.9 min | 12¢ | 24% | 11¢ | ❌ Lost | -$1.28 |
| 9/30 1:36:09 AM | DOGE | DOWN | 8.8 min | 19¢ | 34% | 14¢ | ❌ Lost | -$2.01 |
| 9/30 1:35:30 AM | BNB | DOWN | 9.5 min | 43¢ | 56% | 12¢ | ❌ Lost | -$4.47 |
| 9/30 1:34:36 AM | ETH | DOWN | 10.4 min | 38¢ | 51% | 12¢ | ❌ Lost | -$3.97 |
| 9/30 1:34:36 AM | ZEC | DOWN | 10.4 min | 34¢ | 45% | 9¢ | ❌ Lost | -$3.56 |
| 9/30 1:17:56 AM | XRP | DOWN | 12.1 min | 21¢ | 31% | 8¢ | ❌ Lost | -$2.22 |
| 9/30 1:16:53 AM | ETH | DOWN | 13.1 min | 25¢ | 40% | 14¢ | ❌ Lost | -$2.64 |
| 9/30 1:16:53 AM | ZEC | DOWN | 13.1 min | 30¢ | 44% | 13¢ | ❌ Lost | -$3.15 |
| 9/30 1:16:34 AM | SOL | DOWN | 13.4 min | 24¢ | 37% | 12¢ | ❌ Lost | -$2.53 |
| 9/30 1:16:28 AM | NEAR | DOWN | 13.5 min | 31¢ | 41% | 8¢ | ❌ Lost | -$3.25 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
