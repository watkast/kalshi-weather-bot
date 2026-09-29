# Fair-Value Bot

*Updated Tue Sep 29, 12:57 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1290 | $115.75 | +2% | $158.64 / -$42.89 |
| 4¢+ ← live bot | 1247 | $316.97 | +6% | $270.41 / $46.56 |
| 6¢+ | 1142 | $324.09 | +7% | $335.78 / -$11.69 |
| 8¢+ | 985 | $358.40 | +9% | $316.86 / $41.54 |
| 10¢+ | 827 | $279.56 | +9% | $196.44 / $83.12 |
| 15¢+ | 498 | $319.54 | +19% | $166.56 / $152.98 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1266 | 1257 | 597 (47%) | 44¢ | 53% | $186.97 | +3% | +5.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 855 | 371 (43%) | 268 / 587 | 8.6 | -$43.45 | -$233.94 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 724 | 239 (33%) | 324 / 400 | 7.2 | -$55.90 | -$303.46 | -11% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 182 | 59 (32%) | 49 / 133 | 2.0 | -$14.97 | -$119.52 | -17% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 195 | 81 (42%) | 65 / 130 | 2.0 | -$13.69 | -$30.34 | -4% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 106 | 49 (46%) | 37 / 69 | 1.5 | -$10.05 | -$7.47 | -2% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 72 | 34 (47%) | 26 / 46 | 1.5 | -$20.08 | -$16.10 | -2% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 21 | 7 (33%) | 9 / 12 | 1.6 | -$5.79 | -$14.18 | -17% |

*Model accuracy vs Kalshi's prices on the same 20,517 readings (excluding the final minute): V1 **+1.2%**, V2 **+1.5%**, 3-exchange price (V3/V4) **-0.2%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $483.92 | $525.36 | $394.02 | 2 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 863 | 735 (85%) | -$217.54 | -6% | 228,594 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.5%** over 32,872 readings from 1305 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 5734 | 2% | 4% | 5% |
| 10–20% | 2549 | 15% | 16% | 16% |
| 20–30% | 2717 | 25% | 26% | 26% |
| 30–40% | 3001 | 35% | 36% | 39% |
| 40–50% | 3252 | 45% | 48% | 53% |
| 50–60% | 3222 | 55% | 59% | 61% |
| 60–70% | 2872 | 65% | 70% | 73% |
| 70–80% | 2326 | 75% | 80% | 83% |
| 80–90% | 2057 | 85% | 88% | 87% |
| 90–100% | 5142 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 646 | 316 (49%) | 45¢ | 51% | $157.98 | +5% |
| 6–10¢ | 443 | 213 (48%) | 44¢ | 54% | $93.48 | +5% |
| 10–20¢ | 158 | 65 (41%) | 43¢ | 57% | -$54.26 | -8% |
| 20¢+ | 10 | 3 (30%) | 39¢ | 68% | -$10.23 | -25% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1105 | 536 (49%) | 45¢ | 54% | $183.36 | +4% |
| 5–10 min | 139 | 55 (40%) | 38¢ | 46% | $7.53 | +1% |
| 2–5 min | 11 | 5 (45%) | 48¢ | 55% | -$3.52 | -7% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 166 | 32 (19%) | 18¢ | 27% | -$4.47 | -1% |
| Toss-up (25–75¢) | 990 | 477 (48%) | 45¢ | 54% | $150.53 | +3% |
| Favorite (75–95¢) | 101 | 88 (87%) | 82¢ | 89% | $40.91 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 143 | 74 (52%) | 44¢ | 54% | $88.99 | +14% |
| XRP | 142 | 70 (49%) | 45¢ | 53% | $36.19 | +5% |
| ETH | 141 | 62 (44%) | 46¢ | 54% | -$45.49 | -7% |
| SOL | 139 | 70 (50%) | 42¢ | 50% | $91.43 | +15% |
| NEAR | 139 | 68 (49%) | 46¢ | 54% | $23.07 | +4% |
| HYPE | 139 | 60 (43%) | 44¢ | 53% | -$26.60 | -4% |
| ZEC | 138 | 60 (43%) | 42¢ | 50% | $4.83 | +1% |
| DOGE | 138 | 61 (44%) | 44¢ | 52% | -$12.40 | -2% |
| BTC | 138 | 72 (52%) | 49¢ | 57% | $26.95 | +4% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 12:52:32 PM | DOGE | UP | 7.5 min | 32¢ | 39% | 5¢ | Open | — |
| 9/29 12:50:14 PM | ZEC | UP | 9.8 min | 7¢ | 12% | 5¢ | Open | — |
| 9/29 12:49:41 PM | HYPE | UP | 10.3 min | 20¢ | 26% | 5¢ | Open | — |
| 9/29 12:49:06 PM | ETH | UP | 10.9 min | 38¢ | 44% | 5¢ | Open | — |
| 9/29 12:49:06 PM | XRP | UP | 10.9 min | 26¢ | 34% | 7¢ | Open | — |
| 9/29 12:48:36 PM | SOL | UP | 11.4 min | 20¢ | 27% | 6¢ | Open | — |
| 9/29 12:47:37 PM | BTC | UP | 12.4 min | 30¢ | 36% | 4¢ | Open | — |
| 9/29 12:47:03 PM | NEAR | UP | 12.9 min | 24¢ | 29% | 4¢ | Open | — |
| 9/29 12:46:07 PM | BNB | DOWN | 13.9 min | 49¢ | 72% | 21¢ | Open | — |
| 9/29 12:36:38 PM | BTC | DOWN | 8.3 min | 19¢ | 24% | 4¢ | ❌ Lost | -$2.01 |
| 9/29 12:36:11 PM | NEAR | DOWN | 8.8 min | 32¢ | 38% | 4¢ | ❌ Lost | -$3.36 |
| 9/29 12:34:29 PM | DOGE | DOWN | 10.5 min | 49¢ | 58% | 7¢ | ❌ Lost | -$5.08 |
| 9/29 12:34:29 PM | ZEC | DOWN | 10.5 min | 26¢ | 36% | 9¢ | ❌ Lost | -$2.74 |
| 9/29 12:34:29 PM | SOL | DOWN | 10.5 min | 38¢ | 45% | 6¢ | ❌ Lost | -$3.92 |
| 9/29 12:34:23 PM | XRP | DOWN | 10.6 min | 24¢ | 30% | 4¢ | ❌ Lost | -$2.53 |
| 9/29 12:33:39 PM | HYPE | DOWN | 11.3 min | 35¢ | 43% | 6¢ | ❌ Lost | -$3.71 |
| 9/29 12:32:24 PM | BNB | DOWN | 12.6 min | 45¢ | 56% | 10¢ | ❌ Lost | -$4.68 |
| 9/29 12:22:22 PM | SOL | DOWN | 7.6 min | 26¢ | 32% | 5¢ | ❌ Lost | -$2.74 |
| 9/29 12:21:42 PM | DOGE | DOWN | 8.3 min | 21¢ | 28% | 6¢ | ❌ Lost | -$2.22 |
| 9/29 12:21:17 PM | BTC | DOWN | 8.7 min | 38¢ | 44% | 4¢ | ❌ Lost | -$3.97 |
| 9/29 12:20:27 PM | ETH | DOWN | 9.5 min | 49¢ | 55% | 4¢ | ❌ Lost | -$5.08 |
| 9/29 12:20:20 PM | NEAR | DOWN | 9.7 min | 30¢ | 38% | 6¢ | ❌ Lost | -$3.15 |
| 9/29 12:18:06 PM | ZEC | UP | 11.9 min | 36¢ | 42% | 4¢ | ❌ Lost | -$3.77 |
| 9/29 12:16:33 PM | XRP | DOWN | 13.4 min | 38¢ | 44% | 5¢ | ❌ Lost | -$3.97 |
| 9/29 12:16:28 PM | BNB | DOWN | 13.5 min | 30¢ | 40% | 9¢ | ❌ Lost | -$3.15 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
