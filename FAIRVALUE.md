# Fair-Value Bot

*Updated Tue Sep 29, 6:44 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1137 | $72.95 | +1% | $147.86 / -$74.91 |
| 4¢+ ← live bot | 1096 | $297.98 | +6% | $201.31 / $96.67 |
| 6¢+ | 1006 | $307.86 | +7% | $210.39 / $97.47 |
| 8¢+ | 867 | $344.21 | +10% | $200.78 / $143.43 |
| 10¢+ | 737 | $236.76 | +8% | $158.11 / $78.65 |
| 15¢+ | 451 | $250.13 | +16% | $161.28 / $88.85 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1117 | 1108 | 528 (48%) | 44¢ | 53% | $210.23 | +4% | +5.5¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 706 | 302 (43%) | 228 / 478 | 8.5 | -$43.45 | -$210.68 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 606 | 199 (33%) | 278 / 328 | 7.3 | -$55.90 | -$296.83 | -13% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 150 | 48 (32%) | 44 / 106 | 1.9 | -$14.97 | -$94.93 | -17% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 75% of orders | 161 | 64 (40%) | 54 / 107 | 2.0 | -$13.69 | -$32.15 | -5% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 83 | 38 (46%) | 29 / 54 | 1.5 | -$10.05 | -$10.86 | -3% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 50 | 23 (46%) | 18 / 32 | 1.5 | -$20.08 | -$37.97 | -8% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 13 | 4 (31%) | 5 / 8 | 1.6 | -$5.79 | -$9.99 | -20% |

*Model accuracy vs Kalshi's prices on the same 17,051 readings (excluding the final minute): V1 **+1.0%**, V2 **+1.4%**, 3-exchange price (V3/V4) **-0.5%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $462.04 | $525.36 | $394.02 | 0 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 714 | 586 (82%) | -$194.28 | -7% | 218,150 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.4%** over 29,118 readings from 1152 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 5086 | 2% | 4% | 5% |
| 10–20% | 2310 | 15% | 16% | 16% |
| 20–30% | 2470 | 25% | 26% | 26% |
| 30–40% | 2687 | 35% | 36% | 38% |
| 40–50% | 2841 | 45% | 48% | 52% |
| 50–60% | 2843 | 55% | 59% | 61% |
| 60–70% | 2489 | 65% | 70% | 72% |
| 70–80% | 2082 | 75% | 80% | 82% |
| 80–90% | 1835 | 85% | 88% | 86% |
| 90–100% | 4475 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 579 | 287 (50%) | 45¢ | 52% | $161.22 | +6% |
| 6–10¢ | 387 | 187 (48%) | 44¢ | 53% | $124.53 | +7% |
| 10–20¢ | 133 | 52 (39%) | 42¢ | 56% | -$61.76 | -11% |
| 20¢+ | 9 | 2 (22%) | 36¢ | 65% | -$13.76 | -41% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 996 | 484 (49%) | 45¢ | 53% | $218.64 | +5% |
| 5–10 min | 101 | 39 (39%) | 37¢ | 46% | $2.93 | +1% |
| 2–5 min | 9 | 4 (44%) | 55¢ | 64% | -$10.94 | -21% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 148 | 30 (20%) | 18¢ | 27% | $10.83 | +4% |
| Toss-up (25–75¢) | 883 | 432 (49%) | 45¢ | 54% | $172.90 | +4% |
| Favorite (75–95¢) | 77 | 66 (86%) | 81¢ | 88% | $26.50 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 126 | 65 (52%) | 43¢ | 53% | $90.26 | +16% |
| XRP | 125 | 62 (50%) | 45¢ | 53% | $35.35 | +6% |
| ETH | 125 | 54 (43%) | 45¢ | 53% | -$45.23 | -8% |
| NEAR | 123 | 61 (50%) | 46¢ | 54% | $20.87 | +4% |
| HYPE | 123 | 51 (41%) | 43¢ | 52% | -$40.02 | -7% |
| SOL | 122 | 61 (50%) | 43¢ | 51% | $71.87 | +13% |
| DOGE | 122 | 57 (47%) | 43¢ | 52% | $21.44 | +4% |
| ZEC | 121 | 52 (43%) | 40¢ | 49% | $15.07 | +3% |
| BTC | 121 | 65 (54%) | 49¢ | 57% | $40.62 | +7% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 6:32:57 AM | XRP | DOWN | 12.1 min | 29¢ | 40% | 10¢ | Open | — |
| 9/29 6:32:16 AM | ZEC | DOWN | 12.7 min | 34¢ | 52% | 17¢ | Open | — |
| 9/29 6:31:52 AM | DOGE | DOWN | 13.1 min | 29¢ | 42% | 11¢ | Open | — |
| 9/29 6:31:52 AM | BTC | DOWN | 13.1 min | 36¢ | 43% | 5¢ | Open | — |
| 9/29 6:31:52 AM | NEAR | DOWN | 13.1 min | 40¢ | 50% | 9¢ | Open | — |
| 9/29 6:31:52 AM | SOL | DOWN | 13.1 min | 27¢ | 33% | 4¢ | Open | — |
| 9/29 6:31:52 AM | ETH | DOWN | 13.1 min | 31¢ | 37% | 5¢ | Open | — |
| 9/29 6:31:11 AM | HYPE | DOWN | 13.8 min | 36¢ | 43% | 5¢ | Open | — |
| 9/29 6:31:11 AM | BNB | DOWN | 13.8 min | 48¢ | 57% | 7¢ | Open | — |
| 9/29 6:19:40 AM | XRP | DOWN | 10.3 min | 64¢ | 71% | 5¢ | ✅ Won | $3.43 |
| 9/29 6:18:51 AM | HYPE | UP | 11.1 min | 88¢ | 96% | 7¢ | ❌ Lost | -$8.88 |
| 9/29 6:17:17 AM | DOGE | DOWN | 12.7 min | 14¢ | 22% | 7¢ | ✅ Won | $8.51 |
| 9/29 6:17:17 AM | BTC | DOWN | 12.7 min | 31¢ | 41% | 9¢ | ✅ Won | $6.75 |
| 9/29 6:16:15 AM | BNB | DOWN | 13.8 min | 23¢ | 35% | 10¢ | ✅ Won | $7.57 |
| 9/29 6:16:15 AM | NEAR | DOWN | 13.8 min | 36¢ | 44% | 6¢ | ✅ Won | $6.23 |
| 9/29 6:16:15 AM | ZEC | DOWN | 13.8 min | 26¢ | 44% | 17¢ | ✅ Won | $7.24 |
| 9/29 6:16:15 AM | SOL | DOWN | 13.8 min | 28¢ | 35% | 5¢ | ❌ Lost | -$3.00 |
| 9/29 6:16:15 AM | ETH | UP | 13.8 min | 82¢ | 87% | 4¢ | ✅ Won | $1.69 |
| 9/29 6:10:01 AM | BTC | UP | 5.0 min | 26¢ | 33% | 5¢ | ❌ Lost | -$2.74 |
| 9/29 6:07:26 AM | XRP | DOWN | 7.6 min | 59¢ | 67% | 6¢ | ✅ Won | $3.93 |
| 9/29 6:06:22 AM | SOL | UP | 8.6 min | 42¢ | 51% | 8¢ | ❌ Lost | -$4.38 |
| 9/29 6:03:49 AM | ETH | UP | 11.2 min | 38¢ | 47% | 7¢ | ❌ Lost | -$3.97 |
| 9/29 6:03:34 AM | HYPE | DOWN | 11.4 min | 44¢ | 52% | 6¢ | ✅ Won | $5.41 |
| 9/29 6:03:14 AM | DOGE | DOWN | 11.8 min | 36¢ | 43% | 5¢ | ✅ Won | $6.23 |
| 9/29 6:02:08 AM | NEAR | DOWN | 12.8 min | 52¢ | 59% | 6¢ | ✅ Won | $4.62 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
