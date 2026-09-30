# Fair-Value Bot

*Updated Wed Sep 30, 7:55 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1974 | $223.64 | +2% | $99.76 / $123.88 |
| 4¢+ | 1922 | $381.29 | +4% | $340.99 / $40.30 |
| 6¢+ | 1781 | $304.47 | +4% | $340.92 / -$36.45 |
| 8¢+ ← live bot | 1553 | $457.54 | +7% | $307.09 / $150.45 |
| 10¢+ | 1325 | $482.18 | +10% | $216.08 / $266.10 |
| 15¢+ | 815 | $594.76 | +22% | $213.52 / $381.24 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1821 | 1814 | 812 (45%) | 43¢ | 52% | $55.43 | +1% | +3.2¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 433 | 279 | 178 / 101 | -$0.87 | $99.88 | $100.75 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1412 | 586 (42%) | 413 / 999 | 8.1 | -$43.45 | -$365.48 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1291 | 436 (34%) | 554 / 737 | 7.4 | -$55.90 | -$357.00 | -8% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 325 | 110 (34%) | 86 / 239 | 2.0 | -$14.97 | -$108.22 | -9% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 343 | 147 (43%) | 105 / 238 | 2.0 | -$13.69 | -$13.16 | -1% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 210 | 86 (41%) | 72 / 138 | 1.5 | -$10.05 | -$81.69 | -10% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 6 | 6 (100%) | 1 / 5 | 1.2 | $0.97 | $10.08 | +20% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 49 | 16 (33%) | 18 / 31 | 1.5 | -$5.89 | -$17.84 | -10% |

*Model accuracy vs Kalshi's prices on the same 36,853 readings (excluding the final minute): V1 **+0.6%**, V2 **+1.4%**, 3-exchange price (V3/V4) **-0.4%**.*

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
| 1420 | 1292 (91%) | -$349.08 | -6% | 251,471 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.2%** over 50,475 readings from 1989 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 8762 | 3% | 4% | 4% |
| 10–20% | 3837 | 15% | 17% | 15% |
| 20–30% | 4217 | 25% | 26% | 27% |
| 30–40% | 4611 | 35% | 37% | 40% |
| 40–50% | 4972 | 45% | 48% | 52% |
| 50–60% | 4867 | 55% | 59% | 59% |
| 60–70% | 4264 | 65% | 71% | 72% |
| 70–80% | 3583 | 75% | 80% | 83% |
| 80–90% | 3353 | 85% | 88% | 89% |
| 90–100% | 8009 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 675 | 305 (45%) | 43¢ | 52% | $75.70 | +3% |
| 10–20¢ | 405 | 160 (40%) | 40¢ | 54% | -$79.98 | -5% |
| 20¢+ | 23 | 9 (39%) | 40¢ | 67% | -$6.66 | -7% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1455 | 673 (46%) | 45¢ | 54% | -$3.13 | -0% |
| 5–10 min | 286 | 107 (37%) | 36¢ | 46% | $3.44 | +0% |
| 2–5 min | 64 | 27 (42%) | 33¢ | 45% | $50.86 | +23% |
| 1–2 min | 7 | 3 (43%) | 41¢ | 60% | $0.34 | +1% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 297 | 49 (16%) | 18¢ | 28% | -$75.86 | -13% |
| Toss-up (25–75¢) | 1381 | 643 (47%) | 44¢ | 54% | $61.31 | +1% |
| Favorite (75–95¢) | 136 | 120 (88%) | 82¢ | 90% | $69.98 | +6% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 215 | 93 (43%) | 42¢ | 53% | -$7.49 | -1% |
| ETH | 210 | 95 (45%) | 45¢ | 55% | -$36.64 | -4% |
| HYPE | 206 | 89 (43%) | 42¢ | 53% | -$15.81 | -2% |
| BTC | 202 | 104 (51%) | 49¢ | 58% | $25.12 | +2% |
| XRP | 200 | 90 (45%) | 44¢ | 52% | -$1.83 | -0% |
| ZEC | 199 | 79 (40%) | 39¢ | 49% | -$18.10 | -2% |
| DOGE | 199 | 81 (41%) | 42¢ | 51% | -$47.24 | -6% |
| NEAR | 194 | 85 (44%) | 42¢ | 51% | -$3.62 | -0% |
| SOL | 189 | 96 (51%) | 41¢ | 50% | $161.04 | +20% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/30 7:48:12 AM | XRP | DOWN | 11.8 min | 27¢ | 42% | 13¢ | Open | — |
| 9/30 7:48:12 AM | BTC | DOWN | 11.8 min | 25¢ | 37% | 10¢ | Open | — |
| 9/30 7:47:05 AM | ZEC | DOWN | 12.9 min | 32¢ | 47% | 14¢ | Open | — |
| 9/30 7:46:45 AM | ETH | DOWN | 13.2 min | 34¢ | 45% | 10¢ | Open | — |
| 9/30 7:46:45 AM | HYPE | DOWN | 13.2 min | 34¢ | 49% | 14¢ | Open | — |
| 9/30 7:46:24 AM | NEAR | DOWN | 13.6 min | 49¢ | 59% | 9¢ | Open | — |
| 9/30 7:46:24 AM | BNB | DOWN | 13.6 min | 40¢ | 51% | 9¢ | Open | — |
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
| 9/30 7:21:38 AM | ETH | UP | 8.3 min | 14¢ | 28% | 13¢ | ❌ Lost | -$1.49 |
| 9/30 7:18:48 AM | NEAR | DOWN | 11.2 min | 19¢ | 28% | 8¢ | ❌ Lost | -$2.01 |
| 9/30 7:18:33 AM | BNB | UP | 11.4 min | 25¢ | 35% | 8¢ | ❌ Lost | -$2.64 |
| 9/30 7:18:13 AM | DOGE | DOWN | 11.8 min | 28¢ | 41% | 11¢ | ✅ Won | $7.05 |
| 9/30 7:17:09 AM | XRP | DOWN | 12.8 min | 26¢ | 36% | 9¢ | ✅ Won | $7.26 |
| 9/30 7:16:44 AM | HYPE | DOWN | 13.2 min | 47¢ | 62% | 13¢ | ✅ Won | $5.12 |
| 9/30 7:16:13 AM | ZEC | DOWN | 13.8 min | 45¢ | 55% | 8¢ | ❌ Lost | -$4.68 |
| 9/30 7:11:58 AM | DOGE | DOWN | 3.0 min | 7¢ | 19% | 11¢ | ❌ Lost | -$0.74 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
