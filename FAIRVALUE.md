# Fair-Value Bot

*Updated Tue Sep 29, 6:24 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1128 | $59.82 | +1% | $134.08 / -$74.26 |
| 4¢+ ← live bot | 1087 | $295.46 | +6% | $185.19 / $110.27 |
| 6¢+ | 998 | $295.93 | +7% | $221.79 / $74.14 |
| 8¢+ | 860 | $318.10 | +9% | $192.50 / $125.60 |
| 10¢+ | 733 | $229.42 | +8% | $166.25 / $63.17 |
| 15¢+ | 450 | $242.66 | +16% | $161.28 / $81.38 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1108 | 1099 | 521 (47%) | 44¢ | 53% | $180.69 | +4% | +5.5¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 697 | 295 (42%) | 226 / 471 | 8.5 | -$43.45 | -$240.22 | -8% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 599 | 197 (33%) | 273 / 326 | 7.3 | -$55.90 | -$297.05 | -13% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 148 | 48 (32%) | 43 / 105 | 1.9 | -$14.97 | -$86.08 | -15% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 75% of orders | 159 | 64 (40%) | 53 / 106 | 2.0 | -$13.69 | -$28.59 | -4% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 81 | 37 (46%) | 28 / 53 | 1.5 | -$10.05 | -$12.38 | -4% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 48 | 22 (46%) | 17 / 31 | 1.5 | -$20.08 | -$39.86 | -9% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 13 | 4 (31%) | 5 / 8 | 1.6 | -$5.79 | -$9.99 | -20% |

*Model accuracy vs Kalshi's prices on the same 16,853 readings (excluding the final minute): V1 **+0.9%**, V2 **+1.3%**, 3-exchange price (V3/V4) **-0.5%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $460.15 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 705 | 577 (82%) | -$223.82 | -9% | 216,479 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.3%** over 28,902 readings from 1143 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 5033 | 2% | 4% | 6% |
| 10–20% | 2269 | 15% | 16% | 16% |
| 20–30% | 2451 | 25% | 26% | 26% |
| 30–40% | 2675 | 35% | 36% | 38% |
| 40–50% | 2830 | 45% | 48% | 52% |
| 50–60% | 2829 | 55% | 59% | 61% |
| 60–70% | 2467 | 65% | 70% | 72% |
| 70–80% | 2067 | 75% | 80% | 82% |
| 80–90% | 1820 | 85% | 88% | 86% |
| 90–100% | 4461 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 576 | 285 (49%) | 45¢ | 52% | $159.10 | +6% |
| 6–10¢ | 383 | 184 (48%) | 44¢ | 53% | $111.92 | +6% |
| 10–20¢ | 131 | 50 (38%) | 42¢ | 57% | -$76.57 | -13% |
| 20¢+ | 9 | 2 (22%) | 36¢ | 65% | -$13.76 | -41% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 987 | 477 (48%) | 45¢ | 53% | $189.10 | +4% |
| 5–10 min | 101 | 39 (39%) | 37¢ | 46% | $2.93 | +1% |
| 2–5 min | 9 | 4 (44%) | 55¢ | 64% | -$10.94 | -21% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 146 | 28 (19%) | 18¢ | 27% | -$5.25 | -2% |
| Toss-up (25–75¢) | 878 | 428 (49%) | 45¢ | 54% | $152.25 | +4% |
| Favorite (75–95¢) | 75 | 65 (87%) | 81¢ | 88% | $33.69 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 125 | 64 (51%) | 43¢ | 53% | $82.69 | +15% |
| XRP | 124 | 61 (49%) | 45¢ | 53% | $31.92 | +6% |
| ETH | 124 | 53 (43%) | 45¢ | 53% | -$46.92 | -8% |
| NEAR | 122 | 60 (49%) | 46¢ | 54% | $14.64 | +3% |
| HYPE | 122 | 51 (42%) | 43¢ | 52% | -$31.14 | -6% |
| SOL | 121 | 61 (50%) | 43¢ | 51% | $74.87 | +14% |
| DOGE | 121 | 56 (46%) | 44¢ | 52% | $12.93 | +2% |
| ZEC | 120 | 51 (42%) | 40¢ | 49% | $7.83 | +2% |
| BTC | 120 | 64 (53%) | 49¢ | 57% | $33.87 | +6% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 6:19:40 AM | XRP | DOWN | 10.3 min | 64¢ | 71% | 5¢ | Open | — |
| 9/29 6:18:51 AM | HYPE | UP | 11.1 min | 88¢ | 96% | 7¢ | Open | — |
| 9/29 6:17:17 AM | DOGE | DOWN | 12.7 min | 14¢ | 22% | 7¢ | Open | — |
| 9/29 6:17:17 AM | BTC | DOWN | 12.7 min | 31¢ | 41% | 9¢ | Open | — |
| 9/29 6:16:15 AM | BNB | DOWN | 13.8 min | 23¢ | 35% | 10¢ | Open | — |
| 9/29 6:16:15 AM | NEAR | DOWN | 13.8 min | 36¢ | 44% | 6¢ | Open | — |
| 9/29 6:16:15 AM | ZEC | DOWN | 13.8 min | 26¢ | 44% | 17¢ | Open | — |
| 9/29 6:16:15 AM | SOL | DOWN | 13.8 min | 28¢ | 35% | 5¢ | Open | — |
| 9/29 6:16:15 AM | ETH | UP | 13.8 min | 82¢ | 87% | 4¢ | Open | — |
| 9/29 6:10:01 AM | BTC | UP | 5.0 min | 26¢ | 33% | 5¢ | ❌ Lost | -$2.74 |
| 9/29 6:07:26 AM | XRP | DOWN | 7.6 min | 59¢ | 67% | 6¢ | ✅ Won | $3.93 |
| 9/29 6:06:22 AM | SOL | UP | 8.6 min | 42¢ | 51% | 8¢ | ❌ Lost | -$4.38 |
| 9/29 6:03:49 AM | ETH | UP | 11.2 min | 38¢ | 47% | 7¢ | ❌ Lost | -$3.97 |
| 9/29 6:03:34 AM | HYPE | DOWN | 11.4 min | 44¢ | 52% | 6¢ | ✅ Won | $5.41 |
| 9/29 6:03:14 AM | DOGE | DOWN | 11.8 min | 36¢ | 43% | 5¢ | ✅ Won | $6.23 |
| 9/29 6:02:08 AM | NEAR | DOWN | 12.8 min | 52¢ | 59% | 6¢ | ✅ Won | $4.62 |
| 9/29 6:01:24 AM | BNB | DOWN | 13.6 min | 52¢ | 72% | 18¢ | ✅ Won | $4.62 |
| 9/29 6:01:24 AM | ZEC | DOWN | 13.6 min | 15¢ | 23% | 7¢ | ✅ Won | $8.41 |
| 9/29 5:51:42 AM | XRP | UP | 8.3 min | 91¢ | 97% | 5¢ | ✅ Won | $0.82 |
| 9/29 5:51:16 AM | ETH | UP | 8.7 min | 80¢ | 98% | 17¢ | ✅ Won | $1.88 |
| 9/29 5:50:11 AM | SOL | UP | 9.8 min | 88¢ | 98% | 10¢ | ✅ Won | $1.12 |
| 9/29 5:47:16 AM | BTC | DOWN | 12.7 min | 26¢ | 33% | 5¢ | ❌ Lost | -$2.74 |
| 9/29 5:46:54 AM | DOGE | DOWN | 13.1 min | 26¢ | 34% | 7¢ | ❌ Lost | -$2.74 |
| 9/29 5:46:39 AM | NEAR | DOWN | 13.3 min | 40¢ | 47% | 6¢ | ❌ Lost | -$4.17 |
| 9/29 5:46:32 AM | ZEC | DOWN | 13.4 min | 18¢ | 28% | 10¢ | ❌ Lost | -$1.89 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
