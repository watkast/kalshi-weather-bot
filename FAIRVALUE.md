# Fair-Value Bot

*Updated Tue Sep 29, 3:52 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **4¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1039 | $121.59 | +2% | $118.80 / $2.79 |
| 4¢+ ← live bot | 1005 | $319.33 | +7% | $146.42 / $172.91 |
| 6¢+ | 927 | $301.65 | +8% | $193.35 / $108.30 |
| 8¢+ | 799 | $287.46 | +9% | $201.72 / $85.74 |
| 10¢+ | 680 | $204.82 | +8% | $199.69 / $5.13 |
| 15¢+ | 409 | $210.12 | +15% | $196.30 / $13.82 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1022 | 1013 | 493 (49%) | 45¢ | 53% | $257.04 | +6% | +6.2¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 611 | 267 (44%) | 195 / 416 | 8.5 | -$37.76 | -$163.87 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 529 | 179 (34%) | 237 / 292 | 7.3 | -$55.90 | -$224.65 | -11% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 131 | 44 (34%) | 38 / 93 | 2.0 | -$14.97 | -$78.71 | -15% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 139 | 58 (42%) | 50 / 89 | 2.0 | -$13.69 | -$8.97 | -2% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 68 | 32 (47%) | 24 / 44 | 1.5 | -$10.05 | -$3.58 | -1% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 36 | 18 (50%) | 13 / 23 | 1.5 | -$19.37 | $8.01 | +2% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 10 | 3 (30%) | 4 / 6 | 1.7 | -$5.79 | -$6.69 | -18% |

*Model accuracy vs Kalshi's prices on the same 14,771 readings (excluding the final minute): V1 **+1.2%**, V2 **+1.9%**, 3-exchange price (V3/V4) **-0.4%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $508.02 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 619 | 491 (79%) | -$147.47 | -7% | 179,981 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.4%** over 26,674 readings from 1053 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4708 | 2% | 4% | 6% |
| 10–20% | 2125 | 15% | 16% | 17% |
| 20–30% | 2298 | 25% | 26% | 27% |
| 30–40% | 2468 | 35% | 36% | 40% |
| 40–50% | 2613 | 45% | 48% | 53% |
| 50–60% | 2645 | 55% | 59% | 61% |
| 60–70% | 2316 | 65% | 70% | 72% |
| 70–80% | 1919 | 75% | 80% | 82% |
| 80–90% | 1672 | 85% | 88% | 86% |
| 90–100% | 3910 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 538 | 274 (51%) | 46¢ | 52% | $206.46 | +8% |
| 6–10¢ | 350 | 172 (49%) | 44¢ | 53% | $123.38 | +8% |
| 10–20¢ | 116 | 45 (39%) | 42¢ | 56% | -$59.04 | -12% |
| 20¢+ | 9 | 2 (22%) | 36¢ | 65% | -$13.76 | -41% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 913 | 453 (50%) | 45¢ | 54% | $249.64 | +6% |
| 5–10 min | 91 | 35 (38%) | 36¢ | 45% | $13.16 | +4% |
| 2–5 min | 7 | 4 (57%) | 64¢ | 72% | -$5.36 | -12% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 130 | 26 (20%) | 18¢ | 27% | $6.12 | +2% |
| Toss-up (25–75¢) | 814 | 408 (50%) | 46¢ | 54% | $224.65 | +6% |
| Favorite (75–95¢) | 69 | 59 (86%) | 81¢ | 88% | $26.27 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 115 | 60 (52%) | 43¢ | 53% | $86.65 | +17% |
| XRP | 114 | 58 (51%) | 46¢ | 54% | $40.71 | +8% |
| ETH | 114 | 49 (43%) | 45¢ | 54% | -$45.61 | -9% |
| HYPE | 113 | 48 (42%) | 43¢ | 52% | -$26.87 | -5% |
| SOL | 112 | 58 (52%) | 42¢ | 50% | $87.09 | +18% |
| NEAR | 112 | 56 (50%) | 47¢ | 54% | $20.98 | +4% |
| ZEC | 111 | 48 (43%) | 40¢ | 49% | $14.94 | +3% |
| DOGE | 111 | 54 (49%) | 44¢ | 53% | $29.07 | +6% |
| BTC | 111 | 62 (56%) | 50¢ | 58% | $50.08 | +9% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 3:49:05 AM | ZEC | DOWN | 10.9 min | 26¢ | 32% | 5¢ | Open | — |
| 9/29 3:48:41 AM | SOL | UP | 11.3 min | 85¢ | 91% | 5¢ | Open | — |
| 9/29 3:48:03 AM | XRP | DOWN | 11.9 min | 18¢ | 30% | 11¢ | Open | — |
| 9/29 3:48:03 AM | ETH | DOWN | 11.9 min | 12¢ | 20% | 7¢ | Open | — |
| 9/29 3:47:33 AM | DOGE | DOWN | 12.4 min | 44¢ | 51% | 5¢ | Open | — |
| 9/29 3:47:33 AM | HYPE | DOWN | 12.4 min | 38¢ | 48% | 8¢ | Open | — |
| 9/29 3:46:40 AM | NEAR | DOWN | 13.3 min | 69¢ | 75% | 5¢ | Open | — |
| 9/29 3:46:34 AM | BTC | UP | 13.4 min | 62¢ | 70% | 6¢ | Open | — |
| 9/29 3:46:18 AM | BNB | DOWN | 13.7 min | 49¢ | 66% | 15¢ | Open | — |
| 9/29 3:34:33 AM | ETH | DOWN | 10.4 min | 12¢ | 21% | 8¢ | ❌ Lost | -$1.28 |
| 9/29 3:33:26 AM | SOL | DOWN | 11.6 min | 14¢ | 19% | 5¢ | ❌ Lost | -$1.49 |
| 9/29 3:32:36 AM | XRP | DOWN | 12.4 min | 14¢ | 21% | 6¢ | ❌ Lost | -$1.49 |
| 9/29 3:32:36 AM | NEAR | DOWN | 12.4 min | 31¢ | 39% | 6¢ | ❌ Lost | -$3.25 |
| 9/29 3:31:30 AM | ZEC | DOWN | 13.5 min | 31¢ | 43% | 11¢ | ❌ Lost | -$3.25 |
| 9/29 3:31:21 AM | HYPE | DOWN | 13.6 min | 58¢ | 65% | 5¢ | ❌ Lost | -$5.98 |
| 9/29 3:31:14 AM | DOGE | DOWN | 13.8 min | 45¢ | 58% | 11¢ | ❌ Lost | -$4.68 |
| 9/29 3:31:14 AM | BNB | DOWN | 13.8 min | 61¢ | 70% | 7¢ | ❌ Lost | -$6.27 |
| 9/29 3:22:12 AM | ZEC | DOWN | 7.8 min | 13¢ | 19% | 5¢ | ❌ Lost | -$1.38 |
| 9/29 3:20:31 AM | HYPE | DOWN | 9.5 min | 24¢ | 30% | 5¢ | ❌ Lost | -$2.53 |
| 9/29 3:20:16 AM | ETH | DOWN | 9.7 min | 33¢ | 41% | 6¢ | ❌ Lost | -$3.46 |
| 9/29 3:18:41 AM | BTC | DOWN | 11.3 min | 36¢ | 43% | 5¢ | ❌ Lost | -$3.77 |
| 9/29 3:17:44 AM | SOL | DOWN | 12.3 min | 34¢ | 41% | 5¢ | ❌ Lost | -$3.56 |
| 9/29 3:17:29 AM | NEAR | DOWN | 12.5 min | 46¢ | 53% | 6¢ | ✅ Won | $5.22 |
| 9/29 3:17:22 AM | XRP | DOWN | 12.6 min | 32¢ | 40% | 6¢ | ❌ Lost | -$3.36 |
| 9/29 3:16:31 AM | DOGE | DOWN | 13.5 min | 43¢ | 51% | 6¢ | ❌ Lost | -$4.48 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
