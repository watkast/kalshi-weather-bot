# Fair-Value Bot

*Updated Tue Sep 29, 4:22 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **4¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1057 | $105.91 | +2% | $129.13 / -$23.22 |
| 4¢+ ← live bot | 1023 | $323.97 | +7% | $153.57 / $170.40 |
| 6¢+ | 944 | $314.96 | +8% | $160.64 / $154.32 |
| 8¢+ | 814 | $312.73 | +10% | $196.27 / $116.46 |
| 10¢+ | 695 | $227.99 | +9% | $192.56 / $35.43 |
| 15¢+ | 422 | $229.61 | +16% | $173.85 / $55.76 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1038 | 1031 | 499 (48%) | 44¢ | 53% | $248.78 | +5% | +6.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 629 | 273 (43%) | 204 / 425 | 8.5 | -$37.76 | -$172.13 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 543 | 186 (34%) | 249 / 294 | 7.3 | -$55.90 | -$205.53 | -10% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 135 | 45 (33%) | 40 / 95 | 2.0 | -$14.97 | -$80.08 | -15% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 75% of orders | 143 | 59 (41%) | 51 / 92 | 2.0 | -$13.69 | -$13.75 | -2% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 71 | 33 (46%) | 25 / 46 | 1.5 | -$10.05 | -$6.64 | -2% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 39 | 19 (49%) | 14 / 25 | 1.5 | -$20.08 | -$6.89 | -2% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 10 | 3 (30%) | 4 / 6 | 1.7 | -$5.79 | -$6.69 | -18% |

*Model accuracy vs Kalshi's prices on the same 15,185 readings (excluding the final minute): V1 **+1.2%**, V2 **+1.9%**, 3-exchange price (V3/V4) **-0.2%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $493.12 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 637 | 509 (80%) | -$155.73 | -7% | 193,629 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.5%** over 27,115 readings from 1071 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4738 | 2% | 4% | 6% |
| 10–20% | 2145 | 15% | 16% | 17% |
| 20–30% | 2347 | 25% | 26% | 27% |
| 30–40% | 2525 | 35% | 36% | 40% |
| 40–50% | 2646 | 45% | 48% | 53% |
| 50–60% | 2680 | 55% | 58% | 61% |
| 60–70% | 2338 | 65% | 70% | 72% |
| 70–80% | 1945 | 75% | 80% | 82% |
| 80–90% | 1706 | 85% | 88% | 85% |
| 90–100% | 4045 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 548 | 277 (51%) | 45¢ | 52% | $196.34 | +8% |
| 6–10¢ | 356 | 175 (49%) | 44¢ | 53% | $132.23 | +8% |
| 10–20¢ | 118 | 45 (38%) | 42¢ | 56% | -$66.03 | -13% |
| 20¢+ | 9 | 2 (22%) | 36¢ | 65% | -$13.76 | -41% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 928 | 459 (49%) | 45¢ | 54% | $248.47 | +6% |
| 5–10 min | 94 | 35 (37%) | 35¢ | 44% | $6.07 | +2% |
| 2–5 min | 7 | 4 (57%) | 64¢ | 72% | -$5.36 | -12% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 135 | 27 (20%) | 18¢ | 27% | $6.67 | +3% |
| Toss-up (25–75¢) | 826 | 412 (50%) | 46¢ | 54% | $214.43 | +5% |
| Favorite (75–95¢) | 70 | 60 (86%) | 81¢ | 88% | $27.68 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 117 | 60 (51%) | 43¢ | 53% | $79.86 | +15% |
| XRP | 116 | 58 (50%) | 45¢ | 53% | $35.96 | +7% |
| ETH | 116 | 49 (42%) | 45¢ | 53% | -$50.04 | -9% |
| HYPE | 115 | 49 (43%) | 43¢ | 52% | -$23.06 | -4% |
| SOL | 114 | 60 (53%) | 43¢ | 51% | $95.14 | +19% |
| NEAR | 114 | 58 (51%) | 47¢ | 54% | $28.95 | +5% |
| ZEC | 113 | 48 (42%) | 40¢ | 49% | $9.87 | +2% |
| DOGE | 113 | 54 (48%) | 44¢ | 53% | $21.44 | +4% |
| BTC | 113 | 63 (56%) | 50¢ | 58% | $50.66 | +9% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 4:19:29 AM | XRP | UP | 10.5 min | 18¢ | 27% | 8¢ | Open | — |
| 9/29 4:17:58 AM | SOL | UP | 12.0 min | 21¢ | 31% | 8¢ | Open | — |
| 9/29 4:17:58 AM | DOGE | UP | 12.0 min | 29¢ | 35% | 4¢ | Open | — |
| 9/29 4:17:51 AM | HYPE | UP | 12.1 min | 18¢ | 25% | 6¢ | Open | — |
| 9/29 4:17:43 AM | ETH | DOWN | 12.3 min | 49¢ | 56% | 5¢ | Open | — |
| 9/29 4:17:43 AM | NEAR | DOWN | 12.3 min | 24¢ | 32% | 7¢ | Open | — |
| 9/29 4:16:13 AM | BNB | DOWN | 13.8 min | 47¢ | 65% | 16¢ | Open | — |
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
| 9/29 3:47:33 AM | DOGE | DOWN | 12.4 min | 44¢ | 51% | 5¢ | ❌ Lost | -$4.58 |
| 9/29 3:47:33 AM | HYPE | DOWN | 12.4 min | 38¢ | 48% | 8¢ | ❌ Lost | -$3.97 |
| 9/29 3:46:40 AM | NEAR | DOWN | 13.3 min | 69¢ | 75% | 5¢ | ✅ Won | $2.95 |
| 9/29 3:46:34 AM | BTC | UP | 13.4 min | 62¢ | 70% | 6¢ | ✅ Won | $3.63 |
| 9/29 3:46:18 AM | BNB | DOWN | 13.7 min | 49¢ | 66% | 15¢ | ❌ Lost | -$5.08 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
