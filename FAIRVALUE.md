# Fair-Value Bot

*Updated Wed Sep 30, 4:23 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1848 | $211.39 | +2% | $99.96 / $111.43 |
| 4¢+ | 1797 | $350.52 | +4% | $320.98 / $29.54 |
| 6¢+ | 1668 | $287.49 | +4% | $348.55 / -$61.06 |
| 8¢+ ← live bot | 1454 | $443.82 | +8% | $320.21 / $123.61 |
| 10¢+ | 1238 | $479.26 | +10% | $256.44 / $222.82 |
| 15¢+ | 764 | $571.47 | +22% | $199.79 / $371.68 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1721 | 1717 | 777 (45%) | 43¢ | 53% | $64.18 | +1% | +3.2¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 336 | 223 | 137 / 86 | $7.88 | $66.78 | $58.90 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1315 | 551 (42%) | 380 / 935 | 8.2 | -$43.45 | -$356.73 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1189 | 396 (33%) | 489 / 700 | 7.4 | -$55.90 | -$434.61 | -10% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 299 | 103 (34%) | 75 / 224 | 2.0 | -$14.97 | -$117.82 | -10% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 317 | 138 (44%) | 93 / 224 | 2.0 | -$13.69 | -$5.56 | -0% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 189 | 78 (41%) | 64 / 125 | 1.5 | -$10.05 | -$71.34 | -9% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 3 | 3 (100%) | 0 / 3 | 1.0 | $0.97 | $4.52 | +18% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 43 | 15 (35%) | 15 / 28 | 1.5 | -$5.89 | -$7.74 | -5% |

*Model accuracy vs Kalshi's prices on the same 33,916 readings (excluding the final minute): V1 **+0.6%**, V2 **+1.1%**, 3-exchange price (V3/V4) **-0.5%**.*

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
| 1323 | 1195 (90%) | -$340.33 | -6% | 250,759 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.2%** over 47,313 readings from 1863 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 8193 | 3% | 4% | 5% |
| 10–20% | 3642 | 15% | 17% | 15% |
| 20–30% | 3950 | 25% | 26% | 25% |
| 30–40% | 4328 | 35% | 37% | 38% |
| 40–50% | 4660 | 45% | 48% | 50% |
| 50–60% | 4606 | 55% | 59% | 58% |
| 60–70% | 4057 | 65% | 71% | 72% |
| 70–80% | 3378 | 75% | 80% | 83% |
| 80–90% | 3137 | 85% | 88% | 89% |
| 90–100% | 7362 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 644 | 292 (45%) | 43¢ | 52% | $64.78 | +2% |
| 10–20¢ | 342 | 140 (41%) | 41¢ | 55% | -$55.03 | -4% |
| 20¢+ | 20 | 7 (35%) | 39¢ | 67% | -$11.94 | -15% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1395 | 651 (47%) | 45¢ | 54% | $10.28 | +0% |
| 5–10 min | 261 | 99 (38%) | 36¢ | 46% | $8.01 | +1% |
| 2–5 min | 53 | 23 (43%) | 33¢ | 45% | $48.79 | +27% |
| 1–2 min | 6 | 2 (33%) | 44¢ | 63% | -$6.82 | -25% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 269 | 43 (16%) | 18¢ | 27% | -$83.97 | -16% |
| Toss-up (25–75¢) | 1317 | 619 (47%) | 45¢ | 54% | $83.14 | +1% |
| Favorite (75–95¢) | 131 | 115 (88%) | 82¢ | 90% | $65.01 | +6% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 201 | 90 (45%) | 42¢ | 54% | $13.94 | +2% |
| ETH | 198 | 90 (45%) | 46¢ | 55% | -$42.17 | -4% |
| HYPE | 194 | 85 (44%) | 43¢ | 52% | -$5.57 | -1% |
| XRP | 191 | 85 (45%) | 44¢ | 53% | -$28.49 | -3% |
| ZEC | 190 | 78 (41%) | 39¢ | 49% | $3.93 | +1% |
| BTC | 190 | 98 (52%) | 49¢ | 58% | $14.47 | +1% |
| DOGE | 188 | 78 (41%) | 42¢ | 51% | -$35.22 | -4% |
| NEAR | 184 | 83 (45%) | 43¢ | 51% | $10.75 | +1% |
| SOL | 181 | 90 (50%) | 41¢ | 50% | $132.54 | +17% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/30 4:21:24 AM | BNB | DOWN | 8.6 min | 37¢ | 47% | 8¢ | Open | — |
| 9/30 4:19:22 AM | NEAR | DOWN | 10.6 min | 34¢ | 49% | 13¢ | Open | — |
| 9/30 4:18:31 AM | ZEC | DOWN | 11.5 min | 38¢ | 51% | 11¢ | Open | — |
| 9/30 4:16:10 AM | HYPE | DOWN | 13.8 min | 55¢ | 73% | 16¢ | Open | — |
| 9/30 4:11:14 AM | SOL | UP | 3.8 min | 30¢ | 40% | 8¢ | ✅ Won | $6.85 |
| 9/30 4:10:18 AM | XRP | UP | 4.7 min | 29¢ | 40% | 9¢ | ❌ Lost | -$3.05 |
| 9/30 4:06:07 AM | ETH | DOWN | 8.9 min | 29¢ | 39% | 9¢ | ❌ Lost | -$3.05 |
| 9/30 4:04:36 AM | DOGE | DOWN | 10.4 min | 32¢ | 43% | 9¢ | ❌ Lost | -$3.36 |
| 9/30 4:03:42 AM | NEAR | DOWN | 11.3 min | 29¢ | 40% | 9¢ | ❌ Lost | -$3.05 |
| 9/30 4:01:23 AM | ZEC | DOWN | 13.6 min | 23¢ | 36% | 12¢ | ❌ Lost | -$2.43 |
| 9/30 4:01:10 AM | BNB | DOWN | 13.8 min | 31¢ | 49% | 16¢ | ❌ Lost | -$3.25 |
| 9/30 4:01:10 AM | HYPE | DOWN | 13.8 min | 34¢ | 54% | 19¢ | ✅ Won | $6.44 |
| 9/30 3:55:52 AM | XRP | DOWN | 4.1 min | 34¢ | 44% | 9¢ | ✅ Won | $6.44 |
| 9/30 3:55:19 AM | DOGE | DOWN | 4.7 min | 51¢ | 64% | 11¢ | ✅ Won | $4.72 |
| 9/30 3:55:04 AM | ETH | DOWN | 4.9 min | 30¢ | 45% | 14¢ | ✅ Won | $6.85 |
| 9/30 3:53:47 AM | ZEC | DOWN | 6.2 min | 10¢ | 20% | 10¢ | ❌ Lost | -$1.03 |
| 9/30 3:53:27 AM | BTC | DOWN | 6.5 min | 34¢ | 47% | 11¢ | ❌ Lost | -$3.56 |
| 9/30 3:53:05 AM | BNB | UP | 6.9 min | 6¢ | 18% | 11¢ | ❌ Lost | -$0.70 |
| 9/30 3:53:05 AM | HYPE | DOWN | 6.9 min | 25¢ | 36% | 10¢ | ❌ Lost | -$2.64 |
| 9/30 3:32:02 AM | HYPE | DOWN | 13.0 min | 33¢ | 47% | 12¢ | ❌ Lost | -$3.46 |
| 9/30 3:31:53 AM | ETH | UP | 13.1 min | 63¢ | 74% | 10¢ | ✅ Won | $3.53 |
| 9/30 3:31:45 AM | DOGE | UP | 13.2 min | 76¢ | 87% | 10¢ | ✅ Won | $2.27 |
| 9/30 3:31:39 AM | SOL | UP | 13.3 min | 72¢ | 84% | 11¢ | ✅ Won | $2.65 |
| 9/30 3:31:38 AM | BTC | UP | 13.4 min | 76¢ | 90% | 13¢ | ✅ Won | $2.27 |
| 9/30 3:31:06 AM | BNB | DOWN | 13.9 min | 44¢ | 61% | 15¢ | ❌ Lost | -$4.58 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
