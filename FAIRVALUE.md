# Fair-Value Bot

*Updated Wed Sep 30, 5:23 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1884 | $181.29 | +2% | $101.11 / $80.18 |
| 4¢+ | 1832 | $333.29 | +4% | $314.34 / $18.95 |
| 6¢+ | 1698 | $278.72 | +4% | $315.91 / -$37.19 |
| 8¢+ ← live bot | 1480 | $418.09 | +7% | $306.79 / $111.30 |
| 10¢+ | 1263 | $443.06 | +9% | $212.35 / $230.71 |
| 15¢+ | 781 | $552.69 | +21% | $210.98 / $341.71 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1747 | 1740 | 782 (45%) | 43¢ | 53% | $27.69 | +0% | +3.2¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 359 | 237 | 147 / 90 | -$28.61 | $58.19 | $86.80 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1338 | 556 (42%) | 384 / 954 | 8.1 | -$43.45 | -$393.22 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1214 | 405 (33%) | 504 / 710 | 7.4 | -$55.90 | -$414.87 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 307 | 104 (34%) | 75 / 232 | 2.0 | -$14.97 | -$131.40 | -11% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 325 | 140 (43%) | 97 / 228 | 2.0 | -$13.69 | -$13.71 | -1% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 195 | 80 (41%) | 66 / 129 | 1.5 | -$10.05 | -$77.25 | -10% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 4 | 4 (100%) | 0 / 4 | 1.0 | $0.97 | $6.69 | +20% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 45 | 15 (33%) | 16 / 29 | 1.5 | -$5.89 | -$13.12 | -8% |

*Model accuracy vs Kalshi's prices on the same 34,766 readings (excluding the final minute): V1 **+0.4%**, V2 **+1.2%**, 3-exchange price (V3/V4) **-0.6%**.*

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
| 1346 | 1218 (90%) | -$376.82 | -7% | 250,909 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.1%** over 48,226 readings from 1899 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 8340 | 3% | 4% | 5% |
| 10–20% | 3667 | 15% | 17% | 15% |
| 20–30% | 3986 | 25% | 26% | 26% |
| 30–40% | 4403 | 35% | 37% | 39% |
| 40–50% | 4752 | 45% | 48% | 51% |
| 50–60% | 4690 | 55% | 59% | 59% |
| 60–70% | 4132 | 65% | 71% | 72% |
| 70–80% | 3455 | 75% | 80% | 83% |
| 80–90% | 3229 | 85% | 88% | 89% |
| 90–100% | 7572 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 650 | 292 (45%) | 43¢ | 52% | $48.97 | +2% |
| 10–20¢ | 358 | 144 (40%) | 41¢ | 55% | -$81.23 | -5% |
| 20¢+ | 21 | 8 (38%) | 40¢ | 67% | -$6.42 | -7% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1407 | 653 (46%) | 45¢ | 54% | -$15.50 | -0% |
| 5–10 min | 267 | 99 (37%) | 36¢ | 46% | -$14.75 | -1% |
| 2–5 min | 58 | 26 (45%) | 33¢ | 45% | $60.84 | +31% |
| 1–2 min | 6 | 2 (33%) | 44¢ | 63% | -$6.82 | -25% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 274 | 43 (16%) | 18¢ | 27% | -$92.86 | -18% |
| Toss-up (25–75¢) | 1335 | 624 (47%) | 45¢ | 54% | $55.54 | +1% |
| Favorite (75–95¢) | 131 | 115 (88%) | 82¢ | 90% | $65.01 | +6% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 205 | 91 (44%) | 43¢ | 54% | $4.97 | +1% |
| ETH | 201 | 90 (45%) | 46¢ | 55% | -$50.82 | -5% |
| HYPE | 198 | 86 (43%) | 43¢ | 52% | -$13.30 | -2% |
| XRP | 193 | 86 (45%) | 44¢ | 53% | -$26.11 | -3% |
| BTC | 193 | 99 (51%) | 49¢ | 58% | $14.71 | +2% |
| ZEC | 191 | 78 (41%) | 39¢ | 49% | -$0.07 | -0% |
| DOGE | 190 | 78 (41%) | 42¢ | 51% | -$41.11 | -5% |
| NEAR | 187 | 83 (44%) | 43¢ | 51% | $1.36 | +0% |
| SOL | 182 | 91 (50%) | 41¢ | 50% | $138.06 | +18% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/30 5:23:54 AM | ETH | DOWN | 6.1 min | 18¢ | 32% | 13¢ | Open | — |
| 9/30 5:20:02 AM | XRP | UP | 10.0 min | 24¢ | 34% | 9¢ | Open | — |
| 9/30 5:20:02 AM | SOL | UP | 10.0 min | 21¢ | 33% | 10¢ | Open | — |
| 9/30 5:19:47 AM | BNB | UP | 10.2 min | 24¢ | 34% | 9¢ | Open | — |
| 9/30 5:18:57 AM | ZEC | DOWN | 11.1 min | 53¢ | 71% | 16¢ | Open | — |
| 9/30 5:18:36 AM | HYPE | DOWN | 11.4 min | 53¢ | 66% | 11¢ | Open | — |
| 9/30 5:18:04 AM | DOGE | DOWN | 11.9 min | 37¢ | 47% | 8¢ | Open | — |
| 9/30 5:05:03 AM | NEAR | DOWN | 9.9 min | 30¢ | 45% | 13¢ | ❌ Lost | -$3.15 |
| 9/30 5:03:17 AM | HYPE | DOWN | 11.7 min | 45¢ | 61% | 15¢ | ✅ Won | $5.32 |
| 9/30 5:01:15 AM | BNB | DOWN | 13.7 min | 67¢ | 79% | 10¢ | ✅ Won | $3.14 |
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

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
