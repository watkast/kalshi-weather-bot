# Fair-Value Bot

*Updated Tue Sep 29, 12:43 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **6¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **6¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 932 | $90.48 | +2% | $132.55 / -$42.07 |
| 4¢+ ← live bot | 901 | $317.98 | +8% | $187.88 / $130.10 |
| 6¢+ | 828 | $341.72 | +10% | $204.70 / $137.02 |
| 8¢+ | 716 | $337.13 | +12% | $184.36 / $152.77 |
| 10¢+ | 614 | $270.61 | +11% | $200.24 / $70.37 |
| 15¢+ | 363 | $229.01 | +19% | $178.92 / $50.09 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 915 | 906 | 452 (50%) | 45¢ | 53% | $321.12 | +8% | +7.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 504 | 226 (45%) | 157 / 347 | 8.4 | -$37.76 | -$99.79 | -4% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 446 | 148 (33%) | 203 / 243 | 7.4 | -$55.90 | -$219.64 | -13% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 107 | 35 (33%) | 36 / 71 | 1.9 | -$14.97 | -$74.48 | -18% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 74% of orders | 115 | 48 (42%) | 43 / 72 | 2.0 | -$13.69 | -$16.15 | -3% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 50 | 23 (46%) | 17 / 33 | 1.5 | -$10.05 | -$14.21 | -7% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 19 | 10 (53%) | 6 / 13 | 1.5 | -$10.39 | $5.73 | +3% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 4 | 0 (0%) | 1 / 3 | 1.3 | -$5.79 | -$11.78 | -100% |

*Model accuracy vs Kalshi's prices on the same 12,356 readings (excluding the final minute): V1 **+2.0%**, V2 **+2.3%**, 3-exchange price (V3/V4) **+0.5%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $505.73 | $525.36 | $394.02 | 0 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 512 | 384 (75%) | -$83.39 | -5% | 149,809 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.9%** over 24,095 readings from 945 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4496 | 2% | 4% | 6% |
| 10–20% | 1970 | 15% | 16% | 17% |
| 20–30% | 2120 | 25% | 26% | 27% |
| 30–40% | 2298 | 35% | 36% | 40% |
| 40–50% | 2352 | 45% | 47% | 52% |
| 50–60% | 2347 | 55% | 59% | 60% |
| 60–70% | 2038 | 65% | 70% | 70% |
| 70–80% | 1676 | 75% | 80% | 80% |
| 80–90% | 1455 | 85% | 88% | 84% |
| 90–100% | 3343 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 498 | 257 (52%) | 46¢ | 52% | $220.37 | +9% |
| 6–10¢ | 303 | 152 (50%) | 44¢ | 53% | $129.03 | +9% |
| 10–20¢ | 98 | 41 (42%) | 42¢ | 56% | -$20.89 | -5% |
| 20¢+ | 7 | 2 (29%) | 38¢ | 66% | -$7.39 | -27% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 834 | 421 (50%) | 45¢ | 53% | $304.85 | +8% |
| 5–10 min | 65 | 27 (42%) | 37¢ | 46% | $18.23 | +7% |
| 2–5 min | 5 | 3 (60%) | 62¢ | 70% | -$1.56 | -5% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 111 | 23 (21%) | 19¢ | 27% | $11.27 | +5% |
| Toss-up (25–75¢) | 735 | 378 (51%) | 46¢ | 54% | $291.11 | +8% |
| Favorite (75–95¢) | 60 | 51 (85%) | 81¢ | 88% | $18.74 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 103 | 55 (53%) | 43¢ | 52% | $94.92 | +21% |
| XRP | 102 | 54 (53%) | 47¢ | 54% | $48.24 | +10% |
| ETH | 102 | 45 (44%) | 46¢ | 54% | -$39.33 | -8% |
| HYPE | 101 | 45 (45%) | 43¢ | 52% | -$2.08 | -0% |
| SOL | 100 | 53 (53%) | 44¢ | 51% | $79.45 | +18% |
| NEAR | 100 | 50 (50%) | 46¢ | 54% | $19.74 | +4% |
| BTC | 100 | 56 (56%) | 50¢ | 58% | $43.39 | +8% |
| ZEC | 99 | 43 (43%) | 40¢ | 49% | $16.40 | +4% |
| DOGE | 99 | 51 (52%) | 44¢ | 52% | $60.39 | +13% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 12:35:39 AM | ZEC | DOWN | 9.3 min | 48¢ | 55% | 5¢ | Open | — |
| 9/29 12:32:38 AM | ETH | DOWN | 12.3 min | 37¢ | 44% | 5¢ | Open | — |
| 9/29 12:32:38 AM | NEAR | DOWN | 12.3 min | 31¢ | 39% | 6¢ | Open | — |
| 9/29 12:32:30 AM | BTC | UP | 12.5 min | 67¢ | 74% | 5¢ | Open | — |
| 9/29 12:31:41 AM | SOL | DOWN | 13.3 min | 30¢ | 37% | 6¢ | Open | — |
| 9/29 12:31:25 AM | BNB | DOWN | 13.6 min | 24¢ | 40% | 15¢ | Open | — |
| 9/29 12:31:25 AM | DOGE | DOWN | 13.6 min | 25¢ | 36% | 10¢ | Open | — |
| 9/29 12:31:25 AM | HYPE | DOWN | 13.6 min | 32¢ | 39% | 5¢ | Open | — |
| 9/29 12:31:25 AM | XRP | DOWN | 13.6 min | 21¢ | 31% | 9¢ | Open | — |
| 9/29 12:22:15 AM | NEAR | UP | 7.7 min | 13¢ | 20% | 6¢ | ❌ Lost | -$1.38 |
| 9/29 12:19:33 AM | DOGE | UP | 10.4 min | 13¢ | 20% | 6¢ | ❌ Lost | -$1.38 |
| 9/29 12:19:22 AM | ZEC | UP | 10.6 min | 14¢ | 20% | 5¢ | ❌ Lost | -$1.49 |
| 9/29 12:18:38 AM | SOL | UP | 11.4 min | 10¢ | 17% | 7¢ | ❌ Lost | -$1.03 |
| 9/29 12:18:38 AM | HYPE | UP | 11.4 min | 11¢ | 22% | 10¢ | ❌ Lost | -$1.14 |
| 9/29 12:18:04 AM | BNB | UP | 11.9 min | 18¢ | 24% | 5¢ | ✅ Won | $8.09 |
| 9/29 12:17:55 AM | ETH | UP | 12.1 min | 18¢ | 26% | 7¢ | ✅ Won | $8.09 |
| 9/29 12:17:55 AM | XRP | UP | 12.1 min | 14¢ | 23% | 8¢ | ❌ Lost | -$1.49 |
| 9/29 12:16:26 AM | BTC | UP | 13.6 min | 32¢ | 39% | 6¢ | ✅ Won | $6.64 |
| 9/29 12:05:22 AM | DOGE | DOWN | 9.6 min | 21¢ | 31% | 9¢ | ❌ Lost | -$2.22 |
| 9/29 12:04:37 AM | SOL | UP | 10.4 min | 71¢ | 84% | 12¢ | ✅ Won | $2.75 |
| 9/29 12:04:37 AM | BTC | UP | 10.4 min | 79¢ | 88% | 8¢ | ✅ Won | $1.98 |
| 9/29 12:04:37 AM | XRP | UP | 10.4 min | 72¢ | 82% | 9¢ | ✅ Won | $2.65 |
| 9/29 12:04:01 AM | ETH | DOWN | 11.0 min | 23¢ | 33% | 9¢ | ❌ Lost | -$2.43 |
| 9/29 12:03:29 AM | HYPE | DOWN | 11.5 min | 27¢ | 42% | 13¢ | ❌ Lost | -$2.84 |
| 9/29 12:02:08 AM | ZEC | DOWN | 12.8 min | 43¢ | 50% | 5¢ | ❌ Lost | -$4.48 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
