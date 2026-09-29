# Fair-Value Bot

*Updated Tue Sep 29, 6:54 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1146 | $49.92 | +1% | $153.56 / -$103.64 |
| 4¢+ ← live bot | 1105 | $286.52 | +6% | $209.01 / $77.51 |
| 6¢+ | 1014 | $299.92 | +7% | $187.20 / $112.72 |
| 8¢+ | 874 | $341.25 | +10% | $209.07 / $132.18 |
| 10¢+ | 743 | $244.90 | +9% | $146.01 / $98.89 |
| 15¢+ | 453 | $254.27 | +17% | $159.69 / $94.58 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1126 | 1117 | 531 (48%) | 44¢ | 53% | $207.79 | +4% | +5.5¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 715 | 305 (43%) | 228 / 487 | 8.5 | -$43.45 | -$213.12 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 614 | 202 (33%) | 278 / 336 | 7.3 | -$55.90 | -$296.93 | -13% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 152 | 48 (32%) | 44 / 108 | 1.9 | -$14.97 | -$100.52 | -17% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 75% of orders | 163 | 65 (40%) | 54 / 109 | 2.0 | -$13.69 | -$30.24 | -4% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 83 | 38 (46%) | 29 / 54 | 1.5 | -$10.05 | -$10.86 | -3% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 50 | 23 (46%) | 18 / 32 | 1.5 | -$20.08 | -$37.97 | -8% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 13 | 4 (31%) | 5 / 8 | 1.6 | -$5.79 | -$9.99 | -20% |

*Model accuracy vs Kalshi's prices on the same 17,258 readings (excluding the final minute): V1 **+1.0%**, V2 **+1.4%**, 3-exchange price (V3/V4) **-0.4%**.*

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
| 723 | 595 (82%) | -$196.72 | -7% | 220,753 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.4%** over 29,334 readings from 1161 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 5097 | 2% | 4% | 5% |
| 10–20% | 2314 | 15% | 16% | 16% |
| 20–30% | 2479 | 25% | 26% | 26% |
| 30–40% | 2692 | 35% | 36% | 38% |
| 40–50% | 2864 | 45% | 48% | 52% |
| 50–60% | 2872 | 55% | 59% | 61% |
| 60–70% | 2518 | 65% | 70% | 72% |
| 70–80% | 2094 | 75% | 80% | 82% |
| 80–90% | 1847 | 85% | 88% | 86% |
| 90–100% | 4557 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 583 | 288 (49%) | 45¢ | 52% | $157.59 | +6% |
| 6–10¢ | 390 | 188 (48%) | 44¢ | 53% | $122.33 | +7% |
| 10–20¢ | 135 | 53 (39%) | 42¢ | 56% | -$58.37 | -10% |
| 20¢+ | 9 | 2 (22%) | 36¢ | 65% | -$13.76 | -41% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1005 | 487 (48%) | 45¢ | 53% | $216.20 | +5% |
| 5–10 min | 101 | 39 (39%) | 37¢ | 46% | $2.93 | +1% |
| 2–5 min | 9 | 4 (44%) | 55¢ | 64% | -$10.94 | -21% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 148 | 30 (20%) | 18¢ | 27% | $10.83 | +4% |
| Toss-up (25–75¢) | 892 | 435 (49%) | 45¢ | 54% | $170.46 | +4% |
| Favorite (75–95¢) | 77 | 66 (86%) | 81¢ | 88% | $26.50 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 127 | 65 (51%) | 43¢ | 53% | $85.28 | +15% |
| XRP | 126 | 62 (49%) | 45¢ | 53% | $32.30 | +5% |
| ETH | 126 | 54 (43%) | 45¢ | 53% | -$48.48 | -8% |
| NEAR | 124 | 62 (50%) | 46¢ | 54% | $26.70 | +5% |
| HYPE | 124 | 52 (42%) | 43¢ | 52% | -$33.79 | -6% |
| SOL | 123 | 61 (50%) | 42¢ | 51% | $69.03 | +13% |
| DOGE | 123 | 57 (46%) | 43¢ | 52% | $18.39 | +3% |
| ZEC | 122 | 53 (43%) | 40¢ | 49% | $21.51 | +4% |
| BTC | 122 | 65 (53%) | 49¢ | 57% | $36.85 | +6% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 6:52:47 AM | HYPE | DOWN | 7.2 min | 49¢ | 62% | 11¢ | Open | — |
| 9/29 6:50:45 AM | SOL | UP | 9.2 min | 28¢ | 34% | 4¢ | Open | — |
| 9/29 6:50:10 AM | ETH | UP | 9.8 min | 27¢ | 35% | 7¢ | Open | — |
| 9/29 6:49:06 AM | BNB | UP | 10.9 min | 21¢ | 26% | 4¢ | Open | — |
| 9/29 6:49:06 AM | BTC | UP | 10.9 min | 32¢ | 38% | 4¢ | Open | — |
| 9/29 6:47:58 AM | ZEC | DOWN | 12.0 min | 38¢ | 44% | 4¢ | Open | — |
| 9/29 6:47:13 AM | NEAR | DOWN | 12.8 min | 50¢ | 62% | 11¢ | Open | — |
| 9/29 6:46:49 AM | DOGE | UP | 13.2 min | 29¢ | 36% | 5¢ | Open | — |
| 9/29 6:46:31 AM | XRP | UP | 13.5 min | 39¢ | 46% | 6¢ | Open | — |
| 9/29 6:32:57 AM | XRP | DOWN | 12.1 min | 29¢ | 40% | 10¢ | ❌ Lost | -$3.05 |
| 9/29 6:32:16 AM | ZEC | DOWN | 12.7 min | 34¢ | 52% | 17¢ | ✅ Won | $6.44 |
| 9/29 6:31:52 AM | DOGE | DOWN | 13.1 min | 29¢ | 42% | 11¢ | ❌ Lost | -$3.05 |
| 9/29 6:31:52 AM | BTC | DOWN | 13.1 min | 36¢ | 43% | 5¢ | ❌ Lost | -$3.77 |
| 9/29 6:31:52 AM | NEAR | DOWN | 13.1 min | 40¢ | 50% | 9¢ | ✅ Won | $5.83 |
| 9/29 6:31:52 AM | SOL | DOWN | 13.1 min | 27¢ | 33% | 4¢ | ❌ Lost | -$2.84 |
| 9/29 6:31:52 AM | ETH | DOWN | 13.1 min | 31¢ | 37% | 5¢ | ❌ Lost | -$3.25 |
| 9/29 6:31:11 AM | HYPE | DOWN | 13.8 min | 36¢ | 43% | 5¢ | ✅ Won | $6.23 |
| 9/29 6:31:11 AM | BNB | DOWN | 13.8 min | 48¢ | 57% | 7¢ | ❌ Lost | -$4.98 |
| 9/29 6:19:40 AM | XRP | DOWN | 10.3 min | 64¢ | 71% | 5¢ | ✅ Won | $3.43 |
| 9/29 6:18:51 AM | HYPE | UP | 11.1 min | 88¢ | 96% | 7¢ | ❌ Lost | -$8.88 |
| 9/29 6:17:17 AM | DOGE | DOWN | 12.7 min | 14¢ | 22% | 7¢ | ✅ Won | $8.51 |
| 9/29 6:17:17 AM | BTC | DOWN | 12.7 min | 31¢ | 41% | 9¢ | ✅ Won | $6.75 |
| 9/29 6:16:15 AM | BNB | DOWN | 13.8 min | 23¢ | 35% | 10¢ | ✅ Won | $7.57 |
| 9/29 6:16:15 AM | NEAR | DOWN | 13.8 min | 36¢ | 44% | 6¢ | ✅ Won | $6.23 |
| 9/29 6:16:15 AM | ZEC | DOWN | 13.8 min | 26¢ | 44% | 17¢ | ✅ Won | $7.24 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
