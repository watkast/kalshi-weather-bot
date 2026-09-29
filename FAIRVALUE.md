# Fair-Value Bot

*Updated Tue Sep 29, 11:26 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1236 | $35.77 | +1% | $169.74 / -$133.97 |
| 4¢+ ← live bot | 1193 | $266.25 | +5% | $261.59 / $4.66 |
| 6¢+ | 1096 | $298.49 | +6% | $262.44 / $36.05 |
| 8¢+ | 948 | $357.90 | +10% | $260.58 / $97.32 |
| 10¢+ | 802 | $273.32 | +9% | $154.93 / $118.39 |
| 15¢+ | 486 | $314.80 | +19% | $170.20 / $144.60 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1214 | 1207 | 574 (48%) | 44¢ | 53% | $196.90 | +4% | +5.3¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 805 | 348 (43%) | 255 / 550 | 8.6 | -$43.45 | -$224.01 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 685 | 221 (32%) | 303 / 382 | 7.3 | -$55.90 | -$359.77 | -14% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 172 | 57 (33%) | 48 / 124 | 2.0 | -$14.97 | -$106.31 | -16% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 183 | 75 (41%) | 61 / 122 | 2.0 | -$13.69 | -$33.34 | -4% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 99 | 46 (46%) | 34 / 65 | 1.5 | -$10.05 | -$8.24 | -2% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 65 | 31 (48%) | 23 / 42 | 1.5 | -$20.08 | -$23.09 | -4% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 19 | 7 (37%) | 8 / 11 | 1.6 | -$5.79 | -$8.80 | -11% |

*Model accuracy vs Kalshi's prices on the same 19,221 readings (excluding the final minute): V1 **+1.1%**, V2 **+1.3%**, 3-exchange price (V3/V4) **-0.3%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $476.92 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 813 | 685 (84%) | -$207.61 | -7% | 221,531 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.4%** over 31,468 readings from 1251 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 5510 | 2% | 4% | 5% |
| 10–20% | 2461 | 15% | 16% | 16% |
| 20–30% | 2649 | 25% | 26% | 26% |
| 30–40% | 2910 | 35% | 36% | 39% |
| 40–50% | 3128 | 45% | 48% | 53% |
| 50–60% | 3085 | 55% | 59% | 61% |
| 60–70% | 2729 | 65% | 70% | 73% |
| 70–80% | 2230 | 75% | 80% | 82% |
| 80–90% | 1960 | 85% | 88% | 86% |
| 90–100% | 4806 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 622 | 309 (50%) | 45¢ | 52% | $185.05 | +6% |
| 6–10¢ | 420 | 199 (47%) | 44¢ | 53% | $84.84 | +4% |
| 10–20¢ | 155 | 63 (41%) | 43¢ | 57% | -$62.76 | -9% |
| 20¢+ | 10 | 3 (30%) | 39¢ | 68% | -$10.23 | -25% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1069 | 516 (48%) | 45¢ | 54% | $168.32 | +3% |
| 5–10 min | 126 | 52 (41%) | 37¢ | 46% | $31.18 | +6% |
| 2–5 min | 10 | 5 (50%) | 51¢ | 59% | -$2.20 | -4% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 158 | 32 (20%) | 18¢ | 27% | $12.08 | +4% |
| Toss-up (25–75¢) | 957 | 463 (48%) | 45¢ | 54% | $155.47 | +3% |
| Favorite (75–95¢) | 92 | 79 (86%) | 82¢ | 89% | $29.35 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 137 | 70 (51%) | 44¢ | 54% | $80.88 | +13% |
| XRP | 136 | 66 (49%) | 45¢ | 53% | $28.26 | +4% |
| ETH | 136 | 58 (43%) | 45¢ | 54% | -$56.82 | -9% |
| NEAR | 134 | 67 (50%) | 46¢ | 54% | $30.34 | +5% |
| HYPE | 134 | 59 (44%) | 44¢ | 53% | -$21.31 | -3% |
| SOL | 133 | 68 (51%) | 42¢ | 50% | $96.39 | +17% |
| DOGE | 133 | 60 (45%) | 44¢ | 52% | -$0.20 | -0% |
| ZEC | 132 | 57 (43%) | 41¢ | 50% | $11.62 | +2% |
| BTC | 132 | 69 (52%) | 49¢ | 57% | $27.74 | +4% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 11:25:17 AM | HYPE | UP | 4.7 min | 12¢ | 19% | 6¢ | Open | — |
| 9/29 11:23:49 AM | SOL | UP | 6.2 min | 12¢ | 18% | 6¢ | Open | — |
| 9/29 11:20:33 AM | ZEC | DOWN | 9.4 min | 51¢ | 59% | 6¢ | Open | — |
| 9/29 11:20:25 AM | BTC | UP | 9.6 min | 46¢ | 54% | 6¢ | Open | — |
| 9/29 11:20:18 AM | ETH | DOWN | 9.7 min | 61¢ | 69% | 7¢ | Open | — |
| 9/29 11:19:22 AM | XRP | DOWN | 10.6 min | 54¢ | 63% | 7¢ | Open | — |
| 9/29 11:18:16 AM | BNB | DOWN | 11.7 min | 63¢ | 71% | 6¢ | Open | — |
| 9/29 11:09:54 AM | BTC | DOWN | 5.1 min | 7¢ | 12% | 5¢ | ❌ Lost | -$0.78 |
| 9/29 11:08:57 AM | NEAR | UP | 6.0 min | 23¢ | 29% | 4¢ | ❌ Lost | -$2.43 |
| 9/29 11:08:03 AM | ZEC | DOWN | 7.0 min | 38¢ | 45% | 5¢ | ❌ Lost | -$3.97 |
| 9/29 11:06:23 AM | ETH | DOWN | 8.6 min | 24¢ | 34% | 9¢ | ❌ Lost | -$2.53 |
| 9/29 11:05:06 AM | SOL | DOWN | 9.9 min | 33¢ | 43% | 8¢ | ❌ Lost | -$3.46 |
| 9/29 11:05:06 AM | DOGE | DOWN | 9.9 min | 37¢ | 46% | 7¢ | ❌ Lost | -$3.87 |
| 9/29 11:04:30 AM | XRP | DOWN | 10.5 min | 27¢ | 35% | 7¢ | ❌ Lost | -$2.84 |
| 9/29 11:01:57 AM | BNB | UP | 13.1 min | 33¢ | 40% | 5¢ | ✅ Won | $6.51 |
| 9/29 11:01:35 AM | HYPE | UP | 13.4 min | 44¢ | 51% | 5¢ | ✅ Won | $5.42 |
| 9/29 10:55:14 AM | NEAR | UP | 4.8 min | 12¢ | 17% | 4¢ | ✅ Won | $8.74 |
| 9/29 10:52:07 AM | ZEC | DOWN | 7.9 min | 36¢ | 48% | 11¢ | ❌ Lost | -$3.72 |
| 9/29 10:52:00 AM | BTC | UP | 8.0 min | 38¢ | 46% | 6¢ | ✅ Won | $6.03 |
| 9/29 10:46:51 AM | SOL | DOWN | 13.2 min | 51¢ | 60% | 7¢ | ✅ Won | $4.72 |
| 9/29 10:46:34 AM | XRP | DOWN | 13.4 min | 44¢ | 50% | 4¢ | ✅ Won | $5.42 |
| 9/29 10:46:17 AM | BNB | DOWN | 13.7 min | 63¢ | 79% | 15¢ | ❌ Lost | -$6.47 |
| 9/29 10:46:06 AM | HYPE | DOWN | 13.9 min | 79¢ | 85% | 4¢ | ✅ Won | $1.94 |
| 9/29 10:46:06 AM | ETH | DOWN | 13.9 min | 67¢ | 75% | 6¢ | ❌ Lost | -$6.86 |
| 9/29 10:46:06 AM | DOGE | DOWN | 13.9 min | 76¢ | 84% | 7¢ | ✅ Won | $2.27 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
