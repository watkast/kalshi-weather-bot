# Fair-Value Bot

*Updated Tue Sep 29, 12:13 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 914 | $107.79 | +2% | $121.59 / -$13.80 |
| 4¢+ ← live bot | 883 | $315.06 | +8% | $187.48 / $127.58 |
| 6¢+ | 812 | $328.65 | +9% | $226.28 / $102.37 |
| 8¢+ | 704 | $346.01 | +12% | $182.57 / $163.44 |
| 10¢+ | 605 | $277.97 | +12% | $204.40 / $73.57 |
| 15¢+ | 359 | $234.13 | +19% | $173.97 / $60.16 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 897 | 888 | 446 (50%) | 45¢ | 53% | $319.66 | +8% | +7.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 486 | 220 (45%) | 145 / 341 | 8.4 | -$37.76 | -$101.25 | -4% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 431 | 141 (33%) | 190 / 241 | 7.4 | -$55.90 | -$230.25 | -14% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 103 | 35 (34%) | 35 / 68 | 1.9 | -$14.97 | -$59.59 | -15% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 73% of orders | 111 | 47 (42%) | 41 / 70 | 2.0 | -$13.69 | -$11.98 | -2% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 46 | 22 (48%) | 16 / 30 | 1.5 | -$10.05 | -$7.17 | -4% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 16 | 9 (56%) | 6 / 10 | 1.6 | -$10.39 | $9.50 | +6% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 4 | 0 (0%) | 1 / 3 | 1.3 | -$5.79 | -$11.78 | -100% |

*Model accuracy vs Kalshi's prices on the same 11,944 readings (excluding the final minute): V1 **+2.1%**, V2 **+2.2%**, 3-exchange price (V3/V4) **+0.7%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $509.50 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 494 | 366 (74%) | -$84.85 | -5% | 132,434 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.0%** over 23,654 readings from 927 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4457 | 2% | 4% | 6% |
| 10–20% | 1915 | 15% | 16% | 17% |
| 20–30% | 2057 | 25% | 26% | 26% |
| 30–40% | 2262 | 35% | 36% | 40% |
| 40–50% | 2320 | 45% | 47% | 52% |
| 50–60% | 2314 | 55% | 59% | 60% |
| 60–70% | 2004 | 65% | 70% | 70% |
| 70–80% | 1655 | 75% | 80% | 80% |
| 80–90% | 1432 | 85% | 88% | 83% |
| 90–100% | 3238 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 493 | 255 (52%) | 46¢ | 52% | $215.99 | +9% |
| 6–10¢ | 294 | 149 (51%) | 45¢ | 54% | $126.24 | +9% |
| 10–20¢ | 94 | 40 (43%) | 43¢ | 57% | -$15.18 | -4% |
| 20¢+ | 7 | 2 (29%) | 38¢ | 66% | -$7.39 | -27% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 818 | 415 (51%) | 45¢ | 54% | $299.79 | +8% |
| 5–10 min | 63 | 27 (43%) | 38¢ | 47% | $21.83 | +9% |
| 2–5 min | 5 | 3 (60%) | 62¢ | 70% | -$1.56 | -5% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 101 | 21 (21%) | 19¢ | 27% | $7.65 | +4% |
| Toss-up (25–75¢) | 728 | 375 (52%) | 46¢ | 54% | $295.25 | +9% |
| Favorite (75–95¢) | 59 | 50 (85%) | 81¢ | 88% | $16.76 | +3% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 101 | 54 (53%) | 43¢ | 53% | $91.21 | +20% |
| XRP | 100 | 53 (53%) | 47¢ | 54% | $47.08 | +10% |
| ETH | 100 | 44 (44%) | 47¢ | 55% | -$44.99 | -9% |
| HYPE | 99 | 45 (45%) | 44¢ | 52% | $1.90 | +0% |
| SOL | 98 | 52 (53%) | 44¢ | 51% | $77.73 | +18% |
| NEAR | 98 | 50 (51%) | 47¢ | 54% | $25.60 | +5% |
| BTC | 98 | 54 (55%) | 50¢ | 58% | $34.77 | +7% |
| ZEC | 97 | 43 (44%) | 40¢ | 49% | $22.37 | +5% |
| DOGE | 97 | 51 (53%) | 44¢ | 53% | $63.99 | +14% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 12:05:22 AM | DOGE | DOWN | 9.6 min | 21¢ | 31% | 9¢ | Open | — |
| 9/29 12:04:37 AM | SOL | UP | 10.4 min | 71¢ | 84% | 12¢ | Open | — |
| 9/29 12:04:37 AM | BTC | UP | 10.4 min | 79¢ | 88% | 8¢ | Open | — |
| 9/29 12:04:37 AM | XRP | UP | 10.4 min | 72¢ | 82% | 9¢ | Open | — |
| 9/29 12:04:01 AM | ETH | DOWN | 11.0 min | 23¢ | 33% | 9¢ | Open | — |
| 9/29 12:03:29 AM | HYPE | DOWN | 11.5 min | 27¢ | 42% | 13¢ | Open | — |
| 9/29 12:02:08 AM | ZEC | DOWN | 12.8 min | 43¢ | 50% | 5¢ | Open | — |
| 9/29 12:01:51 AM | BNB | DOWN | 13.1 min | 42¢ | 49% | 5¢ | Open | — |
| 9/29 12:01:19 AM | NEAR | DOWN | 13.7 min | 43¢ | 57% | 12¢ | Open | — |
| 9/28 11:50:07 PM | NEAR | DOWN | 9.9 min | 32¢ | 49% | 16¢ | ❌ Lost | -$3.33 |
| 9/28 11:49:00 PM | BTC | UP | 11.0 min | 38¢ | 45% | 5¢ | ✅ Won | $6.03 |
| 9/28 11:48:40 PM | BNB | DOWN | 11.3 min | 44¢ | 58% | 12¢ | ❌ Lost | -$4.62 |
| 9/28 11:48:21 PM | ETH | DOWN | 11.6 min | 58¢ | 65% | 5¢ | ❌ Lost | -$5.98 |
| 9/28 11:47:53 PM | ZEC | UP | 12.1 min | 28¢ | 34% | 5¢ | ✅ Won | $7.05 |
| 9/28 11:47:25 PM | HYPE | UP | 12.6 min | 21¢ | 27% | 5¢ | ✅ Won | $7.78 |
| 9/28 11:47:03 PM | SOL | UP | 12.9 min | 31¢ | 38% | 5¢ | ✅ Won | $6.75 |
| 9/28 11:46:21 PM | XRP | UP | 13.7 min | 26¢ | 34% | 7¢ | ✅ Won | $7.26 |
| 9/28 11:46:21 PM | DOGE | UP | 13.7 min | 31¢ | 39% | 6¢ | ✅ Won | $6.75 |
| 9/28 11:40:29 PM | BNB | DOWN | 4.5 min | 86¢ | 99% | 12¢ | ✅ Won | $1.31 |
| 9/28 11:32:47 PM | NEAR | UP | 12.2 min | 14¢ | 20% | 5¢ | ❌ Lost | -$1.49 |
| 9/28 11:32:11 PM | XRP | DOWN | 12.8 min | 85¢ | 91% | 5¢ | ✅ Won | $1.41 |
| 9/28 11:32:11 PM | DOGE | DOWN | 12.8 min | 83¢ | 88% | 4¢ | ✅ Won | $1.60 |
| 9/28 11:32:04 PM | HYPE | UP | 12.9 min | 24¢ | 32% | 6¢ | ❌ Lost | -$2.53 |
| 9/28 11:32:04 PM | ZEC | UP | 12.9 min | 18¢ | 27% | 8¢ | ❌ Lost | -$1.91 |
| 9/28 11:31:14 PM | ETH | DOWN | 13.8 min | 78¢ | 84% | 5¢ | ✅ Won | $2.07 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
