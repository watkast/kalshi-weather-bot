# Fair-Value Bot

*Updated Tue Sep 29, 4:32 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1066 | $105.07 | +2% | $130.29 / -$25.22 |
| 4¢+ ← live bot | 1029 | $322.13 | +7% | $165.84 / $156.29 |
| 6¢+ | 949 | $315.80 | +8% | $164.60 / $151.20 |
| 8¢+ | 818 | $322.63 | +10% | $197.12 / $125.51 |
| 10¢+ | 698 | $232.82 | +9% | $198.54 / $34.28 |
| 15¢+ | 424 | $232.92 | +16% | $173.31 / $59.61 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1043 | 1038 | 501 (48%) | 44¢ | 53% | $247.17 | +5% | +6.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 636 | 275 (43%) | 208 / 428 | 8.5 | -$37.76 | -$173.74 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 552 | 187 (34%) | 256 / 296 | 7.4 | -$55.90 | -$228.01 | -11% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 137 | 45 (33%) | 41 / 96 | 2.0 | -$14.97 | -$85.26 | -16% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 75% of orders | 145 | 60 (41%) | 52 / 93 | 2.0 | -$13.69 | -$13.65 | -2% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 72 | 33 (46%) | 25 / 47 | 1.5 | -$10.05 | -$10.00 | -3% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 40 | 19 (48%) | 14 / 26 | 1.5 | -$20.08 | -$16.62 | -4% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 10 | 3 (30%) | 4 / 6 | 1.7 | -$5.79 | -$6.69 | -18% |

*Model accuracy vs Kalshi's prices on the same 15,397 readings (excluding the final minute): V1 **+1.3%**, V2 **+1.9%**, 3-exchange price (V3/V4) **-0.2%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $483.39 | $525.36 | $394.02 | 0 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 644 | 516 (80%) | -$157.34 | -7% | 199,015 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.6%** over 27,340 readings from 1080 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4868 | 2% | 4% | 6% |
| 10–20% | 2173 | 15% | 16% | 16% |
| 20–30% | 2360 | 25% | 26% | 26% |
| 30–40% | 2539 | 35% | 36% | 39% |
| 40–50% | 2661 | 45% | 48% | 53% |
| 50–60% | 2682 | 55% | 58% | 61% |
| 60–70% | 2345 | 65% | 70% | 72% |
| 70–80% | 1955 | 75% | 80% | 82% |
| 80–90% | 1709 | 85% | 88% | 85% |
| 90–100% | 4048 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 551 | 278 (50%) | 45¢ | 52% | $196.30 | +8% |
| 6–10¢ | 359 | 175 (49%) | 44¢ | 53% | $125.54 | +8% |
| 10–20¢ | 119 | 46 (39%) | 42¢ | 56% | -$60.91 | -12% |
| 20¢+ | 9 | 2 (22%) | 36¢ | 65% | -$13.76 | -41% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 935 | 461 (49%) | 45¢ | 53% | $246.86 | +6% |
| 5–10 min | 94 | 35 (37%) | 35¢ | 44% | $6.07 | +2% |
| 2–5 min | 7 | 4 (57%) | 64¢ | 72% | -$5.36 | -12% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 139 | 27 (19%) | 18¢ | 27% | -$1.93 | -1% |
| Toss-up (25–75¢) | 829 | 414 (50%) | 46¢ | 54% | $221.42 | +6% |
| Favorite (75–95¢) | 70 | 60 (86%) | 81¢ | 88% | $27.68 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 118 | 61 (52%) | 43¢ | 53% | $84.98 | +16% |
| XRP | 117 | 58 (50%) | 45¢ | 53% | $34.05 | +6% |
| ETH | 117 | 50 (43%) | 45¢ | 53% | -$45.12 | -8% |
| HYPE | 116 | 49 (42%) | 43¢ | 52% | -$24.97 | -5% |
| SOL | 115 | 60 (52%) | 43¢ | 51% | $92.88 | +18% |
| NEAR | 115 | 58 (50%) | 47¢ | 54% | $26.43 | +5% |
| DOGE | 114 | 54 (47%) | 44¢ | 52% | $18.39 | +4% |
| ZEC | 113 | 48 (42%) | 40¢ | 49% | $9.87 | +2% |
| BTC | 113 | 63 (56%) | 50¢ | 58% | $50.66 | +9% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 4:32:32 AM | BTC | UP | 12.4 min | 23¢ | 29% | 5¢ | Open | — |
| 9/29 4:32:32 AM | DOGE | UP | 12.4 min | 21¢ | 28% | 6¢ | Open | — |
| 9/29 4:31:47 AM | NEAR | DOWN | 13.2 min | 61¢ | 67% | 4¢ | Open | — |
| 9/29 4:31:19 AM | BNB | DOWN | 13.7 min | 50¢ | 60% | 8¢ | Open | — |
| 9/29 4:31:19 AM | XRP | UP | 13.7 min | 34¢ | 41% | 5¢ | Open | — |
| 9/29 4:19:29 AM | XRP | UP | 10.5 min | 18¢ | 27% | 8¢ | ❌ Lost | -$1.91 |
| 9/29 4:17:58 AM | SOL | UP | 12.0 min | 21¢ | 31% | 8¢ | ❌ Lost | -$2.26 |
| 9/29 4:17:58 AM | DOGE | UP | 12.0 min | 29¢ | 35% | 4¢ | ❌ Lost | -$3.05 |
| 9/29 4:17:51 AM | HYPE | UP | 12.1 min | 18¢ | 25% | 6¢ | ❌ Lost | -$1.91 |
| 9/29 4:17:43 AM | ETH | DOWN | 12.3 min | 49¢ | 56% | 5¢ | ✅ Won | $4.92 |
| 9/29 4:17:43 AM | NEAR | DOWN | 12.3 min | 24¢ | 32% | 7¢ | ❌ Lost | -$2.52 |
| 9/29 4:16:13 AM | BNB | DOWN | 13.8 min | 47¢ | 65% | 16¢ | ✅ Won | $5.12 |
| 9/29 4:06:11 AM | DOGE | UP | 8.8 min | 29¢ | 35% | 5¢ | ❌ Lost | -$3.05 |
| 9/29 4:05:39 AM | ZEC | DOWN | 9.3 min | 22¢ | 32% | 9¢ | ❌ Lost | -$2.33 |
| 9/29 4:05:31 AM | BNB | UP | 9.5 min | 16¢ | 23% | 5¢ | ❌ Lost | -$1.71 |
| 9/29 4:03:32 AM | ETH | UP | 11.5 min | 30¢ | 36% | 4¢ | ❌ Lost | -$3.15 |
| 9/29 4:02:42 AM | HYPE | UP | 12.3 min | 21¢ | 31% | 9¢ | ✅ Won | $7.78 |
| 9/29 4:01:42 AM | BTC | UP | 13.3 min | 29¢ | 35% | 5¢ | ❌ Lost | -$3.05 |
| 9/29 4:01:21 AM | NEAR | DOWN | 13.6 min | 48¢ | 56% | 6¢ | ✅ Won | $5.02 |
| 9/29 4:01:13 AM | SOL | UP | 13.8 min | 32¢ | 38% | 4¢ | ✅ Won | $6.64 |
| 9/29 4:01:13 AM | XRP | UP | 13.8 min | 27¢ | 34% | 6¢ | ❌ Lost | -$2.84 |
| 9/29 3:49:05 AM | ZEC | DOWN | 10.9 min | 26¢ | 32% | 5¢ | ❌ Lost | -$2.74 |
| 9/29 3:48:41 AM | SOL | UP | 11.3 min | 85¢ | 91% | 5¢ | ✅ Won | $1.41 |
| 9/29 3:48:03 AM | XRP | DOWN | 11.9 min | 18¢ | 30% | 11¢ | ❌ Lost | -$1.91 |
| 9/29 3:48:03 AM | ETH | DOWN | 11.9 min | 12¢ | 20% | 7¢ | ❌ Lost | -$1.28 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
