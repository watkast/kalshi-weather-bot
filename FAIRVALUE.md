# Fair-Value Bot

*Updated Tue Sep 29, 1:14 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **6¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **6¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 949 | $99.80 | +2% | $121.95 / -$22.15 |
| 4¢+ ← live bot | 917 | $312.43 | +7% | $180.04 / $132.39 |
| 6¢+ | 842 | $319.15 | +9% | $217.85 / $101.30 |
| 8¢+ | 728 | $315.94 | +11% | $200.50 / $115.44 |
| 10¢+ | 624 | $241.13 | +10% | $206.13 / $35.00 |
| 15¢+ | 371 | $205.29 | +16% | $181.40 / $23.89 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 933 | 924 | 457 (49%) | 45¢ | 53% | $304.03 | +7% | +6.8¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 522 | 231 (44%) | 158 / 364 | 8.4 | -$37.76 | -$116.88 | -5% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 462 | 153 (33%) | 210 / 252 | 7.5 | -$55.90 | -$228.96 | -13% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 111 | 36 (32%) | 36 / 75 | 1.9 | -$14.97 | -$79.55 | -18% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 73% of orders | 119 | 49 (41%) | 43 / 76 | 2.0 | -$13.69 | -$17.00 | -3% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 51 | 23 (45%) | 17 / 34 | 1.5 | -$10.05 | -$17.16 | -8% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 20 | 10 (50%) | 6 / 14 | 1.4 | -$10.39 | -$4.59 | -2% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 6 | 1 (17%) | 2 / 4 | 1.5 | -$5.79 | -$10.00 | -50% |

*Model accuracy vs Kalshi's prices on the same 12,767 readings (excluding the final minute): V1 **+1.7%**, V2 **+2.2%**, 3-exchange price (V3/V4) **+0.3%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $495.41 | $525.36 | $394.02 | 2 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 530 | 402 (76%) | -$100.48 | -5% | 160,774 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.8%** over 24,535 readings from 963 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4511 | 2% | 4% | 6% |
| 10–20% | 1986 | 15% | 16% | 17% |
| 20–30% | 2136 | 25% | 26% | 27% |
| 30–40% | 2316 | 35% | 36% | 40% |
| 40–50% | 2400 | 45% | 47% | 53% |
| 50–60% | 2418 | 55% | 59% | 61% |
| 60–70% | 2104 | 65% | 70% | 71% |
| 70–80% | 1712 | 75% | 80% | 81% |
| 80–90% | 1487 | 85% | 88% | 84% |
| 90–100% | 3465 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 507 | 261 (51%) | 46¢ | 52% | $219.78 | +9% |
| 6–10¢ | 309 | 153 (50%) | 44¢ | 53% | $123.22 | +9% |
| 10–20¢ | 100 | 41 (41%) | 42¢ | 56% | -$29.99 | -7% |
| 20¢+ | 8 | 2 (25%) | 35¢ | 64% | -$8.98 | -31% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 847 | 425 (50%) | 45¢ | 53% | $295.55 | +7% |
| 5–10 min | 70 | 28 (40%) | 37¢ | 46% | $10.44 | +4% |
| 2–5 min | 5 | 3 (60%) | 62¢ | 70% | -$1.56 | -5% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 115 | 23 (20%) | 19¢ | 27% | $2.92 | +1% |
| Toss-up (25–75¢) | 749 | 383 (51%) | 46¢ | 54% | $282.37 | +8% |
| Favorite (75–95¢) | 60 | 51 (85%) | 81¢ | 88% | $18.74 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 105 | 55 (52%) | 42¢ | 52% | $87.81 | +19% |
| XRP | 104 | 54 (52%) | 46¢ | 54% | $43.38 | +9% |
| ETH | 104 | 45 (43%) | 46¢ | 54% | -$44.79 | -9% |
| HYPE | 103 | 46 (45%) | 43¢ | 52% | $1.51 | +0% |
| SOL | 102 | 54 (53%) | 43¢ | 51% | $81.72 | +18% |
| NEAR | 102 | 51 (50%) | 46¢ | 54% | $21.05 | +4% |
| BTC | 102 | 57 (56%) | 50¢ | 58% | $44.52 | +8% |
| ZEC | 101 | 44 (44%) | 41¢ | 49% | $14.85 | +3% |
| DOGE | 101 | 51 (50%) | 44¢ | 52% | $53.98 | +12% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 1:09:14 AM | NEAR | DOWN | 5.8 min | 37¢ | 49% | 10¢ | Open | — |
| 9/29 1:07:47 AM | XRP | UP | 7.2 min | 28¢ | 35% | 6¢ | Open | — |
| 9/29 1:04:23 AM | BTC | UP | 10.6 min | 26¢ | 33% | 5¢ | Open | — |
| 9/29 1:02:32 AM | HYPE | DOWN | 12.5 min | 54¢ | 70% | 14¢ | Open | — |
| 9/29 1:02:18 AM | ZEC | UP | 12.7 min | 69¢ | 77% | 7¢ | Open | — |
| 9/29 1:02:10 AM | ETH | UP | 12.8 min | 15¢ | 20% | 4¢ | Open | — |
| 9/29 1:01:56 AM | SOL | UP | 13.1 min | 17¢ | 23% | 5¢ | Open | — |
| 9/29 1:01:21 AM | BNB | DOWN | 13.6 min | 72¢ | 80% | 6¢ | Open | — |
| 9/29 1:01:12 AM | DOGE | DOWN | 13.8 min | 76¢ | 81% | 4¢ | Open | — |
| 9/29 12:51:34 AM | ETH | DOWN | 8.4 min | 15¢ | 46% | 30¢ | ❌ Lost | -$1.59 |
| 9/29 12:51:34 AM | BTC | DOWN | 8.4 min | 19¢ | 27% | 7¢ | ❌ Lost | -$2.01 |
| 9/29 12:51:34 AM | XRP | DOWN | 8.4 min | 25¢ | 36% | 9¢ | ❌ Lost | -$2.64 |
| 9/29 12:51:15 AM | ZEC | DOWN | 8.7 min | 64¢ | 76% | 10¢ | ❌ Lost | -$6.57 |
| 9/29 12:47:24 AM | DOGE | DOWN | 12.6 min | 36¢ | 43% | 5¢ | ❌ Lost | -$3.77 |
| 9/29 12:47:17 AM | HYPE | DOWN | 12.7 min | 29¢ | 40% | 10¢ | ❌ Lost | -$3.05 |
| 9/29 12:46:56 AM | BNB | DOWN | 13.1 min | 44¢ | 51% | 6¢ | ❌ Lost | -$4.58 |
| 9/29 12:46:44 AM | NEAR | DOWN | 13.3 min | 53¢ | 59% | 4¢ | ❌ Lost | -$5.44 |
| 9/29 12:46:18 AM | SOL | DOWN | 13.7 min | 44¢ | 50% | 4¢ | ❌ Lost | -$4.58 |
| 9/29 12:35:39 AM | ZEC | DOWN | 9.3 min | 48¢ | 55% | 5¢ | ✅ Won | $5.02 |
| 9/29 12:32:38 AM | ETH | DOWN | 12.3 min | 37¢ | 44% | 5¢ | ❌ Lost | -$3.87 |
| 9/29 12:32:38 AM | NEAR | DOWN | 12.3 min | 31¢ | 39% | 6¢ | ✅ Won | $6.75 |
| 9/29 12:32:30 AM | BTC | UP | 12.5 min | 67¢ | 74% | 5¢ | ✅ Won | $3.14 |
| 9/29 12:31:41 AM | SOL | DOWN | 13.3 min | 30¢ | 37% | 6¢ | ✅ Won | $6.85 |
| 9/29 12:31:25 AM | BNB | DOWN | 13.6 min | 24¢ | 40% | 15¢ | ❌ Lost | -$2.53 |
| 9/29 12:31:25 AM | DOGE | DOWN | 13.6 min | 25¢ | 36% | 10¢ | ❌ Lost | -$2.64 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
