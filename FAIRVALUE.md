# Fair-Value Bot

*Updated Tue Sep 29, 12:54 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **6¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **6¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 940 | $111.17 | +2% | $126.68 / -$15.51 |
| 4¢+ ← live bot | 909 | $337.34 | +8% | $184.37 / $152.97 |
| 6¢+ | 835 | $345.81 | +10% | $201.32 / $144.49 |
| 8¢+ | 721 | $339.69 | +12% | $186.61 / $153.08 |
| 10¢+ | 617 | $264.27 | +11% | $199.70 / $64.57 |
| 15¢+ | 365 | $224.05 | +18% | $176.91 / $47.14 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 924 | 915 | 457 (50%) | 45¢ | 53% | $338.26 | +8% | +7.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 513 | 231 (45%) | 158 / 355 | 8.4 | -$37.76 | -$82.65 | -3% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 455 | 151 (33%) | 208 / 247 | 7.5 | -$55.90 | -$219.60 | -13% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 109 | 36 (33%) | 36 / 73 | 1.9 | -$14.97 | -$70.10 | -16% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 73% of orders | 117 | 49 (42%) | 43 / 74 | 2.0 | -$13.69 | -$11.12 | -2% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 50 | 23 (46%) | 17 / 33 | 1.5 | -$10.05 | -$14.21 | -7% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 19 | 10 (53%) | 6 / 13 | 1.5 | -$10.39 | $5.73 | +3% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 4 | 0 (0%) | 1 / 3 | 1.3 | -$5.79 | -$11.78 | -100% |

*Model accuracy vs Kalshi's prices on the same 12,558 readings (excluding the final minute): V1 **+1.9%**, V2 **+2.3%**, 3-exchange price (V3/V4) **+0.4%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $505.73 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 521 | 393 (75%) | -$66.25 | -4% | 156,328 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.9%** over 24,315 readings from 954 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4511 | 2% | 4% | 6% |
| 10–20% | 1986 | 15% | 16% | 17% |
| 20–30% | 2132 | 25% | 26% | 26% |
| 30–40% | 2308 | 35% | 36% | 40% |
| 40–50% | 2367 | 45% | 47% | 52% |
| 50–60% | 2383 | 55% | 59% | 60% |
| 60–70% | 2085 | 65% | 70% | 70% |
| 70–80% | 1707 | 75% | 80% | 81% |
| 80–90% | 1470 | 85% | 88% | 84% |
| 90–100% | 3366 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 503 | 261 (52%) | 46¢ | 52% | $238.15 | +10% |
| 6–10¢ | 306 | 153 (50%) | 44¢ | 53% | $130.92 | +9% |
| 10–20¢ | 99 | 41 (41%) | 42¢ | 56% | -$23.42 | -5% |
| 20¢+ | 7 | 2 (29%) | 38¢ | 66% | -$7.39 | -27% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 842 | 425 (50%) | 45¢ | 53% | $316.97 | +8% |
| 5–10 min | 66 | 28 (42%) | 38¢ | 46% | $23.25 | +9% |
| 2–5 min | 5 | 3 (60%) | 62¢ | 70% | -$1.56 | -5% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 113 | 23 (20%) | 19¢ | 27% | $6.52 | +3% |
| Toss-up (25–75¢) | 742 | 383 (52%) | 46¢ | 54% | $313.00 | +9% |
| Favorite (75–95¢) | 60 | 51 (85%) | 81¢ | 88% | $18.74 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 104 | 55 (53%) | 42¢ | 52% | $92.39 | +20% |
| XRP | 103 | 54 (52%) | 46¢ | 54% | $46.02 | +9% |
| ETH | 103 | 45 (44%) | 46¢ | 54% | -$43.20 | -9% |
| HYPE | 102 | 46 (45%) | 43¢ | 52% | $4.56 | +1% |
| SOL | 101 | 54 (53%) | 43¢ | 51% | $86.30 | +19% |
| NEAR | 101 | 51 (50%) | 46¢ | 54% | $26.49 | +5% |
| BTC | 101 | 57 (56%) | 50¢ | 58% | $46.53 | +9% |
| ZEC | 100 | 44 (44%) | 40¢ | 49% | $21.42 | +5% |
| DOGE | 100 | 51 (51%) | 44¢ | 52% | $57.75 | +13% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 12:51:34 AM | ETH | DOWN | 8.4 min | 15¢ | 46% | 30¢ | Open | — |
| 9/29 12:51:34 AM | BTC | DOWN | 8.4 min | 19¢ | 27% | 7¢ | Open | — |
| 9/29 12:51:34 AM | XRP | DOWN | 8.4 min | 25¢ | 36% | 9¢ | Open | — |
| 9/29 12:51:15 AM | ZEC | DOWN | 8.7 min | 64¢ | 76% | 10¢ | Open | — |
| 9/29 12:47:24 AM | DOGE | DOWN | 12.6 min | 36¢ | 43% | 5¢ | Open | — |
| 9/29 12:47:17 AM | HYPE | DOWN | 12.7 min | 29¢ | 40% | 10¢ | Open | — |
| 9/29 12:46:56 AM | BNB | DOWN | 13.1 min | 44¢ | 51% | 6¢ | Open | — |
| 9/29 12:46:44 AM | NEAR | DOWN | 13.3 min | 53¢ | 59% | 4¢ | Open | — |
| 9/29 12:46:18 AM | SOL | DOWN | 13.7 min | 44¢ | 50% | 4¢ | Open | — |
| 9/29 12:35:39 AM | ZEC | DOWN | 9.3 min | 48¢ | 55% | 5¢ | ✅ Won | $5.02 |
| 9/29 12:32:38 AM | ETH | DOWN | 12.3 min | 37¢ | 44% | 5¢ | ❌ Lost | -$3.87 |
| 9/29 12:32:38 AM | NEAR | DOWN | 12.3 min | 31¢ | 39% | 6¢ | ✅ Won | $6.75 |
| 9/29 12:32:30 AM | BTC | UP | 12.5 min | 67¢ | 74% | 5¢ | ✅ Won | $3.14 |
| 9/29 12:31:41 AM | SOL | DOWN | 13.3 min | 30¢ | 37% | 6¢ | ✅ Won | $6.85 |
| 9/29 12:31:25 AM | BNB | DOWN | 13.6 min | 24¢ | 40% | 15¢ | ❌ Lost | -$2.53 |
| 9/29 12:31:25 AM | DOGE | DOWN | 13.6 min | 25¢ | 36% | 10¢ | ❌ Lost | -$2.64 |
| 9/29 12:31:25 AM | HYPE | DOWN | 13.6 min | 32¢ | 39% | 5¢ | ✅ Won | $6.64 |
| 9/29 12:31:25 AM | XRP | DOWN | 13.6 min | 21¢ | 31% | 9¢ | ❌ Lost | -$2.22 |
| 9/29 12:22:15 AM | NEAR | UP | 7.7 min | 13¢ | 20% | 6¢ | ❌ Lost | -$1.38 |
| 9/29 12:19:33 AM | DOGE | UP | 10.4 min | 13¢ | 20% | 6¢ | ❌ Lost | -$1.38 |
| 9/29 12:19:22 AM | ZEC | UP | 10.6 min | 14¢ | 20% | 5¢ | ❌ Lost | -$1.49 |
| 9/29 12:18:38 AM | SOL | UP | 11.4 min | 10¢ | 17% | 7¢ | ❌ Lost | -$1.03 |
| 9/29 12:18:38 AM | HYPE | UP | 11.4 min | 11¢ | 22% | 10¢ | ❌ Lost | -$1.14 |
| 9/29 12:18:04 AM | BNB | UP | 11.9 min | 18¢ | 24% | 5¢ | ✅ Won | $8.09 |
| 9/29 12:17:55 AM | ETH | UP | 12.1 min | 18¢ | 26% | 7¢ | ✅ Won | $8.09 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
