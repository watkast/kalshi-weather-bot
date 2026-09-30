# Fair-Value Bot

*Updated Wed Sep 30, 6:04 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1911 | $179.92 | +2% | $87.96 / $91.96 |
| 4¢+ | 1859 | $349.14 | +4% | $290.79 / $58.35 |
| 6¢+ | 1721 | $293.62 | +4% | $311.52 / -$17.90 |
| 8¢+ ← live bot | 1500 | $435.14 | +7% | $291.13 / $144.01 |
| 10¢+ | 1281 | $428.41 | +9% | $201.67 / $226.74 |
| 15¢+ | 792 | $560.89 | +21% | $215.22 / $345.67 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1765 | 1762 | 791 (45%) | 43¢ | 53% | $31.09 | +0% | +3.2¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 381 | 255 | 159 / 96 | -$25.21 | $78.40 | $103.61 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1360 | 565 (42%) | 392 / 968 | 8.1 | -$43.45 | -$389.82 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1239 | 412 (33%) | 519 / 720 | 7.4 | -$55.90 | -$417.49 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 313 | 109 (35%) | 80 / 233 | 2.0 | -$14.97 | -$94.82 | -8% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 331 | 142 (43%) | 101 / 230 | 2.0 | -$13.69 | -$15.15 | -1% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 200 | 83 (42%) | 68 / 132 | 1.5 | -$10.05 | -$69.00 | -9% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 4 | 4 (100%) | 0 / 4 | 1.0 | $0.97 | $6.69 | +20% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 47 | 15 (32%) | 17 / 30 | 1.5 | -$5.89 | -$19.01 | -11% |

*Model accuracy vs Kalshi's prices on the same 35,405 readings (excluding the final minute): V1 **+0.5%**, V2 **+1.2%**, 3-exchange price (V3/V4) **-0.5%**.*

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
| 1368 | 1240 (91%) | -$373.42 | -7% | 250,594 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.1%** over 48,910 readings from 1926 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 8475 | 3% | 4% | 5% |
| 10–20% | 3748 | 15% | 17% | 15% |
| 20–30% | 4095 | 25% | 26% | 26% |
| 30–40% | 4490 | 35% | 37% | 39% |
| 40–50% | 4822 | 45% | 48% | 51% |
| 50–60% | 4740 | 55% | 59% | 59% |
| 60–70% | 4161 | 65% | 71% | 72% |
| 70–80% | 3475 | 75% | 80% | 83% |
| 80–90% | 3260 | 85% | 88% | 89% |
| 90–100% | 7644 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 657 | 295 (45%) | 43¢ | 52% | $48.92 | +2% |
| 10–20¢ | 371 | 149 (40%) | 41¢ | 55% | -$77.54 | -5% |
| 20¢+ | 23 | 9 (39%) | 40¢ | 67% | -$6.66 | -7% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1419 | 658 (46%) | 45¢ | 54% | -$18.34 | -0% |
| 5–10 min | 274 | 102 (37%) | 36¢ | 46% | -$5.05 | -0% |
| 2–5 min | 61 | 27 (44%) | 34¢ | 46% | $57.38 | +27% |
| 1–2 min | 6 | 2 (33%) | 44¢ | 63% | -$6.82 | -25% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 278 | 45 (16%) | 18¢ | 28% | -$82.05 | -15% |
| Toss-up (25–75¢) | 1353 | 631 (47%) | 45¢ | 54% | $48.13 | +1% |
| Favorite (75–95¢) | 131 | 115 (88%) | 82¢ | 90% | $65.01 | +6% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 208 | 92 (44%) | 42¢ | 54% | $2.98 | +0% |
| ETH | 203 | 90 (44%) | 46¢ | 55% | -$55.78 | -6% |
| HYPE | 200 | 86 (43%) | 43¢ | 52% | -$21.73 | -2% |
| BTC | 196 | 101 (52%) | 49¢ | 58% | $21.56 | +2% |
| XRP | 195 | 88 (45%) | 44¢ | 53% | -$11.28 | -1% |
| ZEC | 193 | 78 (40%) | 39¢ | 49% | -$9.32 | -1% |
| DOGE | 193 | 79 (41%) | 42¢ | 51% | -$45.22 | -5% |
| NEAR | 189 | 84 (44%) | 43¢ | 51% | $0.95 | +0% |
| SOL | 185 | 93 (50%) | 41¢ | 50% | $148.93 | +19% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/30 6:01:46 AM | ZEC | DOWN | 13.2 min | 28¢ | 38% | 9¢ | Open | — |
| 9/30 6:01:26 AM | NEAR | DOWN | 13.6 min | 31¢ | 45% | 13¢ | Open | — |
| 9/30 6:01:19 AM | HYPE | DOWN | 13.7 min | 24¢ | 40% | 14¢ | Open | — |
| 9/30 5:56:13 AM | NEAR | DOWN | 3.8 min | 32¢ | 44% | 10¢ | ❌ Lost | -$3.36 |
| 9/30 5:47:21 AM | BTC | DOWN | 12.7 min | 69¢ | 79% | 8¢ | ✅ Won | $2.95 |
| 9/30 5:47:01 AM | SOL | UP | 13.0 min | 39¢ | 50% | 10¢ | ❌ Lost | -$4.07 |
| 9/30 5:46:52 AM | DOGE | DOWN | 13.1 min | 63¢ | 85% | 21¢ | ✅ Won | $3.53 |
| 9/30 5:46:13 AM | BNB | DOWN | 13.8 min | 49¢ | 61% | 10¢ | ✅ Won | $4.92 |
| 9/30 5:40:28 AM | NEAR | DOWN | 4.5 min | 69¢ | 80% | 10¢ | ✅ Won | $2.95 |
| 9/30 5:37:34 AM | BTC | UP | 7.4 min | 29¢ | 42% | 11¢ | ✅ Won | $6.95 |
| 9/30 5:37:06 AM | ZEC | DOWN | 7.9 min | 36¢ | 60% | 22¢ | ❌ Lost | -$3.77 |
| 9/30 5:36:50 AM | ETH | DOWN | 8.2 min | 29¢ | 43% | 12¢ | ❌ Lost | -$3.05 |
| 9/30 5:35:52 AM | DOGE | DOWN | 9.1 min | 36¢ | 53% | 15¢ | ❌ Lost | -$3.77 |
| 9/30 5:31:26 AM | XRP | UP | 13.6 min | 25¢ | 43% | 16¢ | ✅ Won | $7.36 |
| 9/30 5:31:26 AM | HYPE | UP | 13.6 min | 28¢ | 38% | 8¢ | ❌ Lost | -$2.95 |
| 9/30 5:31:12 AM | SOL | UP | 13.8 min | 27¢ | 39% | 11¢ | ✅ Won | $7.16 |
| 9/30 5:31:07 AM | BNB | DOWN | 13.9 min | 42¢ | 58% | 14¢ | ❌ Lost | -$4.38 |
| 9/30 5:26:50 AM | BTC | DOWN | 3.1 min | 29¢ | 41% | 10¢ | ❌ Lost | -$3.05 |
| 9/30 5:23:54 AM | ETH | DOWN | 6.1 min | 18¢ | 32% | 13¢ | ❌ Lost | -$1.91 |
| 9/30 5:20:02 AM | XRP | UP | 10.0 min | 24¢ | 34% | 9¢ | ✅ Won | $7.47 |
| 9/30 5:20:02 AM | SOL | UP | 10.0 min | 21¢ | 33% | 10¢ | ✅ Won | $7.78 |
| 9/30 5:19:47 AM | BNB | UP | 10.2 min | 24¢ | 34% | 9¢ | ❌ Lost | -$2.53 |
| 9/30 5:18:57 AM | ZEC | DOWN | 11.1 min | 53¢ | 71% | 16¢ | ❌ Lost | -$5.48 |
| 9/30 5:18:36 AM | HYPE | DOWN | 11.4 min | 53¢ | 66% | 11¢ | ❌ Lost | -$5.48 |
| 9/30 5:18:04 AM | DOGE | DOWN | 11.9 min | 37¢ | 47% | 8¢ | ❌ Lost | -$3.87 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
