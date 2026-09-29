# Fair-Value Bot

*Updated Tue Sep 29, 7:35 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1173 | $48.55 | +1% | $136.85 / -$88.30 |
| 4¢+ ← live bot | 1131 | $278.83 | +5% | $224.91 / $53.92 |
| 6¢+ | 1039 | $312.00 | +7% | $204.79 / $107.21 |
| 8¢+ | 896 | $354.72 | +10% | $214.95 / $139.77 |
| 10¢+ | 762 | $278.07 | +10% | $172.31 / $105.76 |
| 15¢+ | 464 | $269.06 | +17% | $154.93 / $114.13 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1153 | 1144 | 541 (47%) | 44¢ | 52% | $201.78 | +4% | +5.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 742 | 315 (42%) | 239 / 503 | 8.5 | -$43.45 | -$219.13 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 637 | 211 (33%) | 289 / 348 | 7.3 | -$55.90 | -$290.97 | -12% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 158 | 49 (31%) | 47 / 111 | 2.0 | -$14.97 | -$111.67 | -19% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 75% of orders | 169 | 66 (39%) | 56 / 113 | 2.0 | -$13.69 | -$43.31 | -6% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 87 | 39 (45%) | 30 / 57 | 1.5 | -$10.05 | -$14.52 | -4% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 54 | 24 (44%) | 19 / 35 | 1.5 | -$20.08 | -$56.09 | -11% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 15 | 5 (33%) | 6 / 9 | 1.7 | -$5.79 | -$10.65 | -18% |

*Model accuracy vs Kalshi's prices on the same 17,863 readings (excluding the final minute): V1 **+0.8%**, V2 **+1.2%**, 3-exchange price (V3/V4) **-0.7%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $443.92 | $525.36 | $394.02 | 0 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 750 | 622 (83%) | -$202.73 | -7% | 225,382 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.2%** over 29,984 readings from 1188 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 5134 | 2% | 4% | 5% |
| 10–20% | 2344 | 15% | 16% | 16% |
| 20–30% | 2539 | 25% | 26% | 26% |
| 30–40% | 2766 | 35% | 36% | 38% |
| 40–50% | 2952 | 45% | 48% | 52% |
| 50–60% | 2956 | 55% | 59% | 61% |
| 60–70% | 2620 | 65% | 70% | 72% |
| 70–80% | 2151 | 75% | 80% | 82% |
| 80–90% | 1886 | 85% | 88% | 86% |
| 90–100% | 4636 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 596 | 293 (49%) | 45¢ | 51% | $160.45 | +6% |
| 6–10¢ | 399 | 190 (48%) | 43¢ | 53% | $104.08 | +6% |
| 10–20¢ | 140 | 56 (40%) | 42¢ | 56% | -$48.99 | -8% |
| 20¢+ | 9 | 2 (22%) | 36¢ | 65% | -$13.76 | -41% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1026 | 493 (48%) | 45¢ | 53% | $190.90 | +4% |
| 5–10 min | 107 | 43 (40%) | 37¢ | 46% | $22.22 | +5% |
| 2–5 min | 9 | 4 (44%) | 55¢ | 64% | -$10.94 | -21% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 149 | 30 (20%) | 18¢ | 27% | $8.61 | +3% |
| Toss-up (25–75¢) | 918 | 445 (48%) | 45¢ | 54% | $166.67 | +4% |
| Favorite (75–95¢) | 77 | 66 (86%) | 81¢ | 88% | $26.50 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 130 | 66 (51%) | 43¢ | 53% | $86.45 | +15% |
| XRP | 129 | 62 (48%) | 45¢ | 53% | $20.70 | +3% |
| ETH | 129 | 56 (43%) | 45¢ | 53% | -$39.16 | -7% |
| NEAR | 127 | 63 (50%) | 46¢ | 54% | $23.50 | +4% |
| HYPE | 127 | 53 (42%) | 43¢ | 52% | -$35.68 | -6% |
| SOL | 126 | 63 (50%) | 42¢ | 50% | $79.49 | +14% |
| DOGE | 126 | 57 (45%) | 43¢ | 52% | $4.21 | +1% |
| ZEC | 125 | 55 (44%) | 40¢ | 49% | $27.79 | +5% |
| BTC | 125 | 66 (53%) | 48¢ | 57% | $34.48 | +6% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 7:32:12 AM | HYPE | DOWN | 12.8 min | 86¢ | 93% | 6¢ | Open | — |
| 9/29 7:31:58 AM | ZEC | DOWN | 13.0 min | 87¢ | 96% | 8¢ | Open | — |
| 9/29 7:31:58 AM | NEAR | DOWN | 13.0 min | 85¢ | 91% | 5¢ | Open | — |
| 9/29 7:31:58 AM | BNB | DOWN | 13.0 min | 82¢ | 94% | 10¢ | Open | — |
| 9/29 7:31:58 AM | ETH | DOWN | 13.0 min | 79¢ | 94% | 14¢ | Open | — |
| 9/29 7:31:43 AM | DOGE | UP | 13.3 min | 19¢ | 28% | 7¢ | Open | — |
| 9/29 7:31:43 AM | XRP | UP | 13.3 min | 32¢ | 48% | 14¢ | Open | — |
| 9/29 7:31:04 AM | BTC | DOWN | 13.9 min | 63¢ | 88% | 23¢ | Open | — |
| 9/29 7:31:04 AM | SOL | DOWN | 13.9 min | 65¢ | 82% | 15¢ | Open | — |
| 9/29 7:24:11 AM | BTC | DOWN | 5.8 min | 27¢ | 33% | 4¢ | ✅ Won | $7.16 |
| 9/29 7:22:07 AM | SOL | DOWN | 7.9 min | 30¢ | 36% | 5¢ | ❌ Lost | -$3.13 |
| 9/29 7:17:33 AM | ZEC | DOWN | 12.4 min | 40¢ | 46% | 5¢ | ✅ Won | $5.83 |
| 9/29 7:17:33 AM | BNB | DOWN | 12.4 min | 31¢ | 46% | 13¢ | ❌ Lost | -$3.25 |
| 9/29 7:17:33 AM | HYPE | DOWN | 12.4 min | 34¢ | 42% | 6¢ | ❌ Lost | -$3.56 |
| 9/29 7:16:59 AM | DOGE | DOWN | 13.0 min | 42¢ | 51% | 8¢ | ❌ Lost | -$4.38 |
| 9/29 7:16:59 AM | XRP | DOWN | 13.0 min | 43¢ | 53% | 8¢ | ❌ Lost | -$4.48 |
| 9/29 7:16:42 AM | ETH | UP | 13.3 min | 38¢ | 44% | 4¢ | ✅ Won | $6.03 |
| 9/29 7:16:27 AM | NEAR | DOWN | 13.6 min | 46¢ | 53% | 5¢ | ❌ Lost | -$4.78 |
| 9/29 7:05:32 AM | ETH | DOWN | 9.5 min | 37¢ | 49% | 10¢ | ✅ Won | $6.13 |
| 9/29 7:03:50 AM | XRP | UP | 11.2 min | 29¢ | 35% | 5¢ | ❌ Lost | -$3.05 |
| 9/29 7:01:38 AM | NEAR | DOWN | 13.3 min | 31¢ | 48% | 15¢ | ✅ Won | $6.75 |
| 9/29 7:01:38 AM | HYPE | DOWN | 13.3 min | 31¢ | 39% | 6¢ | ❌ Lost | -$3.25 |
| 9/29 7:01:26 AM | BTC | DOWN | 13.6 min | 60¢ | 70% | 8¢ | ❌ Lost | -$6.17 |
| 9/29 7:01:26 AM | DOGE | DOWN | 13.6 min | 66¢ | 75% | 7¢ | ❌ Lost | -$6.75 |
| 9/29 7:01:17 AM | ZEC | UP | 13.7 min | 54¢ | 61% | 5¢ | ✅ Won | $4.42 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
