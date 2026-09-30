# Fair-Value Bot

*Updated Wed Sep 30, 7:04 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1947 | $152.43 | +2% | $85.43 / $67.00 |
| 4¢+ | 1895 | $317.32 | +4% | $295.71 / $21.61 |
| 6¢+ | 1754 | $268.35 | +4% | $325.37 / -$57.02 |
| 8¢+ ← live bot | 1528 | $417.07 | +7% | $315.81 / $101.26 |
| 10¢+ | 1302 | $436.86 | +9% | $225.80 / $211.06 |
| 15¢+ | 804 | $580.13 | +21% | $215.68 / $364.45 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1794 | 1789 | 799 (45%) | 43¢ | 53% | $15.76 | +0% | +3.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 408 | 268 | 167 / 101 | -$40.54 | $80.36 | $120.90 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1387 | 573 (41%) | 405 / 982 | 8.1 | -$43.45 | -$405.15 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1266 | 424 (33%) | 538 / 728 | 7.4 | -$55.90 | -$398.63 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 319 | 110 (34%) | 83 / 236 | 2.0 | -$14.97 | -$99.04 | -8% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 337 | 143 (42%) | 104 / 233 | 2.0 | -$13.69 | -$29.90 | -2% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 205 | 84 (41%) | 70 / 135 | 1.5 | -$10.05 | -$82.75 | -10% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 6 | 6 (100%) | 1 / 5 | 1.2 | $0.97 | $10.08 | +20% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 49 | 16 (33%) | 18 / 31 | 1.5 | -$5.89 | -$17.84 | -10% |

*Model accuracy vs Kalshi's prices on the same 36,251 readings (excluding the final minute): V1 **+0.5%**, V2 **+1.2%**, 3-exchange price (V3/V4) **-0.6%**.*

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
| 1395 | 1267 (91%) | -$388.75 | -7% | 251,238 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.0%** over 49,819 readings from 1962 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 8592 | 3% | 4% | 5% |
| 10–20% | 3814 | 15% | 17% | 16% |
| 20–30% | 4180 | 25% | 26% | 27% |
| 30–40% | 4545 | 35% | 37% | 39% |
| 40–50% | 4886 | 45% | 48% | 51% |
| 50–60% | 4801 | 55% | 59% | 59% |
| 60–70% | 4213 | 65% | 71% | 73% |
| 70–80% | 3537 | 75% | 80% | 84% |
| 80–90% | 3307 | 85% | 88% | 89% |
| 90–100% | 7944 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 663 | 298 (45%) | 43¢ | 52% | $59.43 | +2% |
| 10–20¢ | 392 | 154 (39%) | 40¢ | 54% | -$103.38 | -6% |
| 20¢+ | 23 | 9 (39%) | 40¢ | 67% | -$6.66 | -7% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1439 | 663 (46%) | 45¢ | 54% | -$45.36 | -1% |
| 5–10 min | 279 | 104 (37%) | 36¢ | 46% | $3.04 | +0% |
| 2–5 min | 62 | 27 (44%) | 34¢ | 46% | $53.82 | +25% |
| 1–2 min | 7 | 3 (43%) | 41¢ | 60% | $0.34 | +1% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 289 | 47 (16%) | 18¢ | 28% | -$81.90 | -15% |
| Toss-up (25–75¢) | 1366 | 634 (46%) | 45¢ | 54% | $29.64 | +0% |
| Favorite (75–95¢) | 134 | 118 (88%) | 82¢ | 90% | $68.02 | +6% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 212 | 92 (43%) | 42¢ | 53% | -$6.48 | -1% |
| ETH | 207 | 93 (45%) | 45¢ | 55% | -$41.80 | -4% |
| HYPE | 203 | 87 (43%) | 42¢ | 52% | -$22.65 | -3% |
| BTC | 199 | 102 (51%) | 49¢ | 58% | $13.75 | +1% |
| XRP | 197 | 88 (45%) | 44¢ | 53% | -$15.10 | -2% |
| ZEC | 196 | 78 (40%) | 39¢ | 49% | -$15.91 | -2% |
| DOGE | 196 | 79 (40%) | 42¢ | 51% | -$54.48 | -6% |
| NEAR | 191 | 84 (44%) | 43¢ | 51% | -$4.31 | -1% |
| SOL | 188 | 96 (51%) | 41¢ | 50% | $162.74 | +20% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/30 7:04:05 AM | BNB | DOWN | 10.9 min | 51¢ | 61% | 8¢ | Open | — |
| 9/30 7:03:28 AM | ZEC | DOWN | 11.5 min | 50¢ | 65% | 13¢ | Open | — |
| 9/30 7:03:08 AM | XRP | UP | 11.9 min | 29¢ | 39% | 8¢ | Open | — |
| 9/30 7:03:01 AM | BTC | UP | 12.0 min | 26¢ | 35% | 8¢ | Open | — |
| 9/30 7:02:52 AM | HYPE | DOWN | 12.1 min | 56¢ | 71% | 13¢ | Open | — |
| 9/30 6:53:45 AM | XRP | DOWN | 6.2 min | 18¢ | 29% | 10¢ | ❌ Lost | -$1.91 |
| 9/30 6:49:22 AM | HYPE | DOWN | 10.6 min | 23¢ | 43% | 18¢ | ❌ Lost | -$2.47 |
| 9/30 6:49:22 AM | BTC | DOWN | 10.6 min | 15¢ | 28% | 13¢ | ❌ Lost | -$1.59 |
| 9/30 6:49:22 AM | ETH | DOWN | 10.6 min | 26¢ | 40% | 13¢ | ❌ Lost | -$2.74 |
| 9/30 6:48:48 AM | BNB | DOWN | 11.2 min | 35¢ | 49% | 12¢ | ❌ Lost | -$3.71 |
| 9/30 6:47:18 AM | NEAR | UP | 12.7 min | 19¢ | 31% | 11¢ | ❌ Lost | -$2.01 |
| 9/30 6:47:11 AM | DOGE | UP | 12.8 min | 32¢ | 46% | 12¢ | ❌ Lost | -$3.36 |
| 9/30 6:46:16 AM | ZEC | DOWN | 13.7 min | 29¢ | 41% | 10¢ | ❌ Lost | -$3.05 |
| 9/30 6:34:36 AM | BNB | DOWN | 10.4 min | 5¢ | 16% | 11¢ | ❌ Lost | -$0.54 |
| 9/30 6:34:18 AM | ZEC | DOWN | 10.7 min | 5¢ | 15% | 9¢ | ❌ Lost | -$0.59 |
| 9/30 6:31:15 AM | BTC | UP | 13.7 min | 90¢ | 100% | 9¢ | ✅ Won | $0.93 |
| 9/30 6:31:15 AM | SOL | UP | 13.7 min | 89¢ | 100% | 10¢ | ✅ Won | $1.03 |
| 9/30 6:31:15 AM | ETH | UP | 13.7 min | 89¢ | 100% | 10¢ | ✅ Won | $1.05 |
| 9/30 6:28:43 AM | ETH | UP | 1.3 min | 27¢ | 39% | 11¢ | ✅ Won | $7.16 |
| 9/30 6:23:12 AM | XRP | UP | 6.8 min | 18¢ | 32% | 13¢ | ❌ Lost | -$1.91 |
| 9/30 6:18:26 AM | BNB | UP | 11.6 min | 26¢ | 39% | 11¢ | ❌ Lost | -$2.78 |
| 9/30 6:18:10 AM | HYPE | DOWN | 11.8 min | 57¢ | 71% | 13¢ | ❌ Lost | -$5.88 |
| 9/30 6:17:49 AM | DOGE | UP | 12.2 min | 22¢ | 32% | 8¢ | ❌ Lost | -$2.34 |
| 9/30 6:17:35 AM | BTC | DOWN | 12.4 min | 70¢ | 82% | 10¢ | ❌ Lost | -$7.15 |
| 9/30 6:17:12 AM | SOL | UP | 12.8 min | 29¢ | 39% | 9¢ | ✅ Won | $6.95 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
