# Fair-Value Bot

*Updated Wed Sep 30, 8:05 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1983 | $232.04 | +2% | $119.43 / $112.61 |
| 4¢+ | 1931 | $396.61 | +4% | $343.83 / $52.78 |
| 6¢+ | 1790 | $315.05 | +4% | $337.50 / -$22.45 |
| 8¢+ ← live bot | 1561 | $469.29 | +8% | $297.70 / $171.59 |
| 10¢+ | 1331 | $486.27 | +10% | $218.08 / $268.19 |
| 15¢+ | 820 | $588.56 | +21% | $205.04 / $383.52 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1829 | 1821 | 815 (45%) | 43¢ | 52% | $60.19 | +1% | +3.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 440 | 282 | 181 / 101 | $3.89 | $94.68 | $90.79 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1419 | 589 (42%) | 413 / 1006 | 8.1 | -$43.45 | -$360.72 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1299 | 440 (34%) | 554 / 745 | 7.4 | -$55.90 | -$354.28 | -7% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 327 | 110 (34%) | 86 / 241 | 2.0 | -$14.97 | -$113.80 | -9% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 345 | 148 (43%) | 105 / 240 | 2.0 | -$13.69 | -$12.66 | -1% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 211 | 87 (41%) | 72 / 139 | 1.5 | -$10.05 | -$76.74 | -9% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 6 | 6 (100%) | 1 / 5 | 1.2 | $0.97 | $10.08 | +20% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 51 | 17 (33%) | 19 / 32 | 1.5 | -$5.89 | -$15.36 | -8% |

*Model accuracy vs Kalshi's prices on the same 37,053 readings (excluding the final minute): V1 **+0.6%**, V2 **+1.4%**, 3-exchange price (V3/V4) **-0.4%**.*

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
| 1427 | 1299 (91%) | -$344.32 | -6% | 251,679 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.1%** over 50,693 readings from 1998 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 8778 | 3% | 4% | 4% |
| 10–20% | 3843 | 15% | 17% | 15% |
| 20–30% | 4236 | 25% | 26% | 27% |
| 30–40% | 4624 | 35% | 37% | 40% |
| 40–50% | 5008 | 45% | 48% | 51% |
| 50–60% | 4924 | 55% | 59% | 59% |
| 60–70% | 4305 | 65% | 71% | 72% |
| 70–80% | 3600 | 75% | 80% | 83% |
| 80–90% | 3357 | 85% | 88% | 89% |
| 90–100% | 8018 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 678 | 306 (45%) | 43¢ | 52% | $72.86 | +2% |
| 10–20¢ | 409 | 162 (40%) | 40¢ | 54% | -$72.38 | -4% |
| 20¢+ | 23 | 9 (39%) | 40¢ | 67% | -$6.66 | -7% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1462 | 676 (46%) | 45¢ | 54% | $1.63 | +0% |
| 5–10 min | 286 | 107 (37%) | 36¢ | 46% | $3.44 | +0% |
| 2–5 min | 64 | 27 (42%) | 33¢ | 45% | $50.86 | +23% |
| 1–2 min | 7 | 3 (43%) | 41¢ | 60% | $0.34 | +1% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 297 | 49 (16%) | 18¢ | 28% | -$75.86 | -13% |
| Toss-up (25–75¢) | 1388 | 646 (47%) | 44¢ | 54% | $66.07 | +1% |
| Favorite (75–95¢) | 136 | 120 (88%) | 82¢ | 90% | $69.98 | +6% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 216 | 93 (43%) | 42¢ | 53% | -$11.69 | -1% |
| ETH | 211 | 95 (45%) | 45¢ | 55% | -$40.20 | -4% |
| HYPE | 207 | 90 (43%) | 42¢ | 53% | -$9.37 | -1% |
| BTC | 203 | 104 (51%) | 49¢ | 58% | $22.48 | +2% |
| XRP | 201 | 91 (45%) | 44¢ | 52% | $5.33 | +1% |
| ZEC | 200 | 79 (40%) | 39¢ | 49% | -$21.46 | -3% |
| DOGE | 199 | 81 (41%) | 42¢ | 51% | -$47.24 | -6% |
| NEAR | 195 | 86 (44%) | 43¢ | 51% | $1.30 | +0% |
| SOL | 189 | 96 (51%) | 41¢ | 50% | $161.04 | +20% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/30 8:04:10 AM | BNB | DOWN | 10.8 min | 46¢ | 69% | 21¢ | Open | — |
| 9/30 8:04:10 AM | SOL | DOWN | 10.8 min | 40¢ | 52% | 11¢ | Open | — |
| 9/30 8:02:55 AM | NEAR | DOWN | 12.1 min | 43¢ | 55% | 10¢ | Open | — |
| 9/30 8:02:08 AM | BTC | UP | 12.8 min | 27¢ | 37% | 8¢ | Open | — |
| 9/30 8:01:39 AM | DOGE | UP | 13.3 min | 46¢ | 58% | 10¢ | Open | — |
| 9/30 8:01:23 AM | ZEC | DOWN | 13.6 min | 32¢ | 53% | 19¢ | Open | — |
| 9/30 8:01:23 AM | XRP | DOWN | 13.6 min | 38¢ | 51% | 11¢ | Open | — |
| 9/30 8:01:23 AM | ETH | DOWN | 13.6 min | 42¢ | 55% | 11¢ | Open | — |
| 9/30 7:48:12 AM | XRP | DOWN | 11.8 min | 27¢ | 42% | 13¢ | ✅ Won | $7.16 |
| 9/30 7:48:12 AM | BTC | DOWN | 11.8 min | 25¢ | 37% | 10¢ | ❌ Lost | -$2.64 |
| 9/30 7:47:05 AM | ZEC | DOWN | 12.9 min | 32¢ | 47% | 14¢ | ❌ Lost | -$3.36 |
| 9/30 7:46:45 AM | ETH | DOWN | 13.2 min | 34¢ | 45% | 10¢ | ❌ Lost | -$3.56 |
| 9/30 7:46:45 AM | HYPE | DOWN | 13.2 min | 34¢ | 49% | 14¢ | ✅ Won | $6.44 |
| 9/30 7:46:24 AM | NEAR | DOWN | 13.6 min | 49¢ | 59% | 9¢ | ✅ Won | $4.92 |
| 9/30 7:46:24 AM | BNB | DOWN | 13.6 min | 40¢ | 51% | 9¢ | ❌ Lost | -$4.20 |
| 9/30 7:37:34 AM | DOGE | DOWN | 7.4 min | 90¢ | 99% | 8¢ | ✅ Won | $0.93 |
| 9/30 7:36:30 AM | ETH | DOWN | 8.5 min | 89¢ | 98% | 8¢ | ✅ Won | $1.03 |
| 9/30 7:35:49 AM | XRP | UP | 9.2 min | 9¢ | 21% | 12¢ | ❌ Lost | -$0.94 |
| 9/30 7:34:32 AM | BTC | DOWN | 10.4 min | 27¢ | 43% | 15¢ | ✅ Won | $7.16 |
| 9/30 7:34:32 AM | NEAR | DOWN | 10.4 min | 49¢ | 59% | 8¢ | ✅ Won | $4.92 |
| 9/30 7:32:01 AM | ZEC | DOWN | 13.0 min | 22¢ | 41% | 18¢ | ✅ Won | $7.67 |
| 9/30 7:31:17 AM | HYPE | DOWN | 13.7 min | 24¢ | 38% | 13¢ | ✅ Won | $7.47 |
| 9/30 7:31:17 AM | BNB | DOWN | 13.7 min | 29¢ | 42% | 12¢ | ✅ Won | $6.95 |
| 9/30 7:23:20 AM | BTC | UP | 6.7 min | 29¢ | 40% | 10¢ | ❌ Lost | -$3.05 |
| 9/30 7:21:53 AM | SOL | UP | 8.1 min | 16¢ | 28% | 11¢ | ❌ Lost | -$1.70 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
