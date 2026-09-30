# Fair-Value Bot

*Updated Wed Sep 30, 6:24 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1920 | $182.03 | +2% | $83.85 / $98.18 |
| 4¢+ | 1868 | $360.56 | +4% | $290.87 / $69.69 |
| 6¢+ | 1729 | $290.33 | +4% | $313.84 / -$23.51 |
| 8¢+ ← live bot | 1507 | $428.72 | +7% | $297.40 / $131.32 |
| 10¢+ | 1286 | $435.20 | +9% | $198.95 / $236.25 |
| 15¢+ | 794 | $562.75 | +21% | $211.56 / $351.19 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1775 | 1769 | 794 (45%) | 43¢ | 53% | $40.67 | +1% | +3.2¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 388 | 261 | 162 / 99 | -$15.63 | $87.13 | $102.76 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1367 | 568 (42%) | 395 / 972 | 8.1 | -$43.45 | -$380.24 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1247 | 415 (33%) | 523 / 724 | 7.4 | -$55.90 | -$412.79 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 315 | 110 (35%) | 81 / 234 | 2.0 | -$14.97 | -$93.52 | -8% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 333 | 143 (43%) | 102 / 231 | 2.0 | -$13.69 | -$14.14 | -1% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 202 | 84 (42%) | 69 / 133 | 1.5 | -$10.05 | -$70.12 | -9% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 4 | 4 (100%) | 0 / 4 | 1.0 | $0.97 | $6.69 | +20% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 47 | 15 (32%) | 17 / 30 | 1.5 | -$5.89 | -$19.01 | -11% |

*Model accuracy vs Kalshi's prices on the same 35,621 readings (excluding the final minute): V1 **+0.5%**, V2 **+1.2%**, 3-exchange price (V3/V4) **-0.5%**.*

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
| 1375 | 1247 (91%) | -$363.84 | -7% | 250,429 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.1%** over 49,135 readings from 1935 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 8528 | 3% | 4% | 5% |
| 10–20% | 3765 | 15% | 17% | 15% |
| 20–30% | 4111 | 25% | 26% | 26% |
| 30–40% | 4504 | 35% | 37% | 39% |
| 40–50% | 4857 | 45% | 48% | 51% |
| 50–60% | 4761 | 55% | 59% | 59% |
| 60–70% | 4187 | 65% | 71% | 73% |
| 70–80% | 3492 | 75% | 80% | 84% |
| 80–90% | 3265 | 85% | 88% | 89% |
| 90–100% | 7665 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 659 | 296 (45%) | 43¢ | 52% | $54.48 | +2% |
| 10–20¢ | 376 | 151 (40%) | 41¢ | 55% | -$73.52 | -5% |
| 20¢+ | 23 | 9 (39%) | 40¢ | 67% | -$6.66 | -7% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1422 | 659 (46%) | 45¢ | 54% | -$17.11 | -0% |
| 5–10 min | 277 | 104 (38%) | 36¢ | 46% | $6.86 | +1% |
| 2–5 min | 62 | 27 (44%) | 34¢ | 46% | $53.82 | +25% |
| 1–2 min | 6 | 2 (33%) | 44¢ | 63% | -$6.82 | -25% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 281 | 47 (17%) | 18¢ | 28% | -$68.54 | -13% |
| Toss-up (25–75¢) | 1357 | 632 (47%) | 45¢ | 54% | $44.20 | +1% |
| Favorite (75–95¢) | 131 | 115 (88%) | 82¢ | 90% | $65.01 | +6% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 209 | 92 (44%) | 42¢ | 54% | $0.55 | +0% |
| ETH | 204 | 91 (45%) | 45¢ | 55% | -$47.27 | -5% |
| HYPE | 201 | 87 (43%) | 42¢ | 52% | -$14.30 | -2% |
| BTC | 196 | 101 (52%) | 49¢ | 58% | $21.56 | +2% |
| XRP | 195 | 88 (45%) | 44¢ | 53% | -$11.28 | -1% |
| ZEC | 194 | 78 (40%) | 39¢ | 49% | -$12.27 | -2% |
| DOGE | 194 | 79 (41%) | 42¢ | 51% | -$48.78 | -6% |
| NEAR | 190 | 84 (44%) | 43¢ | 51% | -$2.30 | -0% |
| SOL | 186 | 94 (51%) | 41¢ | 50% | $154.76 | +20% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/30 6:23:12 AM | XRP | UP | 6.8 min | 18¢ | 32% | 13¢ | Open | — |
| 9/30 6:18:26 AM | BNB | UP | 11.6 min | 26¢ | 39% | 11¢ | Open | — |
| 9/30 6:18:10 AM | HYPE | DOWN | 11.8 min | 57¢ | 71% | 13¢ | Open | — |
| 9/30 6:17:49 AM | DOGE | UP | 12.2 min | 22¢ | 32% | 8¢ | Open | — |
| 9/30 6:17:35 AM | BTC | DOWN | 12.4 min | 70¢ | 82% | 10¢ | Open | — |
| 9/30 6:17:12 AM | SOL | UP | 12.8 min | 29¢ | 39% | 9¢ | Open | — |
| 9/30 6:10:45 AM | DOGE | DOWN | 4.2 min | 34¢ | 47% | 11¢ | ❌ Lost | -$3.56 |
| 9/30 6:09:13 AM | SOL | UP | 5.8 min | 40¢ | 52% | 10¢ | ✅ Won | $5.83 |
| 9/30 6:09:13 AM | ETH | UP | 5.8 min | 14¢ | 24% | 9¢ | ✅ Won | $8.51 |
| 9/30 6:05:36 AM | BNB | UP | 9.4 min | 23¢ | 39% | 15¢ | ❌ Lost | -$2.43 |
| 9/30 6:01:46 AM | ZEC | DOWN | 13.2 min | 28¢ | 38% | 9¢ | ❌ Lost | -$2.95 |
| 9/30 6:01:26 AM | NEAR | DOWN | 13.6 min | 31¢ | 45% | 13¢ | ❌ Lost | -$3.25 |
| 9/30 6:01:19 AM | HYPE | DOWN | 13.7 min | 24¢ | 40% | 14¢ | ✅ Won | $7.43 |
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

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
