# Fair-Value Bot

*Updated Tue Sep 29, 11:06 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1227 | $9.82 | +0% | $163.72 / -$153.90 |
| 4¢+ ← live bot | 1184 | $249.01 | +5% | $249.20 / -$0.19 |
| 6¢+ | 1087 | $291.83 | +6% | $242.85 / $48.98 |
| 8¢+ | 939 | $360.72 | +10% | $258.47 / $102.25 |
| 10¢+ | 793 | $286.76 | +10% | $148.33 / $138.43 |
| 15¢+ | 482 | $325.23 | +20% | $156.70 / $168.53 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1204 | 1198 | 572 (48%) | 44¢ | 53% | $204.85 | +4% | +5.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 796 | 346 (43%) | 252 / 544 | 8.6 | -$43.45 | -$216.06 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 677 | 221 (33%) | 303 / 374 | 7.3 | -$55.90 | -$328.99 | -13% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 170 | 57 (34%) | 48 / 122 | 2.0 | -$14.97 | -$98.06 | -15% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 181 | 74 (41%) | 60 / 121 | 2.0 | -$13.69 | -$32.54 | -4% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 96 | 44 (46%) | 33 / 63 | 1.5 | -$10.05 | -$13.07 | -3% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 62 | 29 (47%) | 22 / 40 | 1.5 | -$20.08 | -$37.97 | -6% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 19 | 7 (37%) | 8 / 11 | 1.6 | -$5.79 | -$8.80 | -11% |

*Model accuracy vs Kalshi's prices on the same 18,996 readings (excluding the final minute): V1 **+1.2%**, V2 **+1.6%**, 3-exchange price (V3/V4) **-0.2%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $462.04 | $525.36 | $394.02 | 2 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 804 | 676 (84%) | -$199.66 | -6% | 219,404 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.5%** over 31,225 readings from 1242 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 5509 | 2% | 4% | 5% |
| 10–20% | 2458 | 15% | 16% | 16% |
| 20–30% | 2643 | 25% | 26% | 26% |
| 30–40% | 2884 | 35% | 36% | 39% |
| 40–50% | 3076 | 45% | 48% | 52% |
| 50–60% | 3050 | 55% | 59% | 60% |
| 60–70% | 2684 | 65% | 70% | 72% |
| 70–80% | 2204 | 75% | 80% | 82% |
| 80–90% | 1934 | 85% | 88% | 86% |
| 90–100% | 4783 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 617 | 307 (50%) | 45¢ | 52% | $180.30 | +6% |
| 6–10¢ | 416 | 199 (48%) | 44¢ | 53% | $97.54 | +5% |
| 10–20¢ | 155 | 63 (41%) | 43¢ | 57% | -$62.76 | -9% |
| 20¢+ | 10 | 3 (30%) | 39¢ | 68% | -$10.23 | -25% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1066 | 514 (48%) | 45¢ | 54% | $159.23 | +3% |
| 5–10 min | 120 | 52 (43%) | 38¢ | 47% | $48.22 | +10% |
| 2–5 min | 10 | 5 (50%) | 51¢ | 59% | -$2.20 | -4% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 155 | 32 (21%) | 18¢ | 27% | $17.82 | +6% |
| Toss-up (25–75¢) | 951 | 461 (48%) | 45¢ | 54% | $157.68 | +4% |
| Favorite (75–95¢) | 92 | 79 (86%) | 82¢ | 89% | $29.35 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 136 | 69 (51%) | 44¢ | 54% | $74.37 | +12% |
| XRP | 135 | 66 (49%) | 45¢ | 53% | $31.10 | +5% |
| ETH | 135 | 58 (43%) | 45¢ | 54% | -$54.29 | -9% |
| NEAR | 133 | 67 (50%) | 46¢ | 54% | $32.77 | +5% |
| HYPE | 133 | 58 (44%) | 44¢ | 53% | -$26.73 | -4% |
| SOL | 132 | 68 (52%) | 42¢ | 51% | $99.85 | +17% |
| DOGE | 132 | 60 (45%) | 44¢ | 52% | $3.67 | +1% |
| ZEC | 131 | 57 (44%) | 41¢ | 50% | $15.59 | +3% |
| BTC | 131 | 69 (53%) | 49¢ | 57% | $28.52 | +4% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 11:06:23 AM | ETH | DOWN | 8.6 min | 24¢ | 34% | 9¢ | Open | — |
| 9/29 11:05:06 AM | SOL | DOWN | 9.9 min | 33¢ | 43% | 8¢ | Open | — |
| 9/29 11:05:06 AM | DOGE | DOWN | 9.9 min | 37¢ | 46% | 7¢ | Open | — |
| 9/29 11:04:30 AM | XRP | DOWN | 10.5 min | 27¢ | 35% | 7¢ | Open | — |
| 9/29 11:01:57 AM | BNB | UP | 13.1 min | 33¢ | 40% | 5¢ | Open | — |
| 9/29 11:01:35 AM | HYPE | UP | 13.4 min | 44¢ | 51% | 5¢ | Open | — |
| 9/29 10:55:14 AM | NEAR | UP | 4.8 min | 12¢ | 17% | 4¢ | ✅ Won | $8.74 |
| 9/29 10:52:07 AM | ZEC | DOWN | 7.9 min | 36¢ | 48% | 11¢ | ❌ Lost | -$3.72 |
| 9/29 10:52:00 AM | BTC | UP | 8.0 min | 38¢ | 46% | 6¢ | ✅ Won | $6.03 |
| 9/29 10:46:51 AM | SOL | DOWN | 13.2 min | 51¢ | 60% | 7¢ | ✅ Won | $4.72 |
| 9/29 10:46:34 AM | XRP | DOWN | 13.4 min | 44¢ | 50% | 4¢ | ✅ Won | $5.42 |
| 9/29 10:46:17 AM | BNB | DOWN | 13.7 min | 63¢ | 79% | 15¢ | ❌ Lost | -$6.47 |
| 9/29 10:46:06 AM | HYPE | DOWN | 13.9 min | 79¢ | 85% | 4¢ | ✅ Won | $1.94 |
| 9/29 10:46:06 AM | ETH | DOWN | 13.9 min | 67¢ | 75% | 6¢ | ❌ Lost | -$6.86 |
| 9/29 10:46:06 AM | DOGE | DOWN | 13.9 min | 76¢ | 84% | 7¢ | ✅ Won | $2.27 |
| 9/29 10:39:30 AM | NEAR | DOWN | 5.5 min | 14¢ | 20% | 5¢ | ✅ Won | $8.51 |
| 9/29 10:39:28 AM | ZEC | UP | 5.5 min | 30¢ | 37% | 5¢ | ❌ Lost | -$3.17 |
| 9/29 10:38:44 AM | ETH | DOWN | 6.2 min | 50¢ | 56% | 4¢ | ✅ Won | $4.82 |
| 9/29 10:38:40 AM | BNB | DOWN | 6.3 min | 63¢ | 71% | 6¢ | ✅ Won | $3.53 |
| 9/29 10:38:26 AM | DOGE | DOWN | 6.5 min | 45¢ | 57% | 10¢ | ✅ Won | $5.32 |
| 9/29 10:37:05 AM | SOL | DOWN | 7.9 min | 31¢ | 39% | 7¢ | ✅ Won | $6.77 |
| 9/29 10:36:52 AM | BTC | UP | 8.1 min | 45¢ | 51% | 5¢ | ❌ Lost | -$4.68 |
| 9/29 10:36:35 AM | HYPE | DOWN | 8.4 min | 85¢ | 91% | 4¢ | ✅ Won | $1.37 |
| 9/29 10:36:13 AM | XRP | DOWN | 8.8 min | 77¢ | 83% | 5¢ | ✅ Won | $2.15 |
| 9/29 8:21:45 AM | NEAR | UP | 8.2 min | 94¢ | 99% | 4¢ | ✅ Won | $0.56 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
