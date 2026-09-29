# Fair-Value Bot

*Updated Mon Sep 28, 11:02 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 878 | $115.29 | +3% | $168.94 / -$53.65 |
| 4¢+ ← live bot | 847 | $330.26 | +8% | $226.68 / $103.58 |
| 6¢+ | 782 | $364.25 | +11% | $217.55 / $146.70 |
| 8¢+ | 682 | $383.47 | +14% | $189.20 / $194.27 |
| 10¢+ | 588 | $302.85 | +13% | $200.33 / $102.52 |
| 15¢+ | 351 | $258.60 | +22% | $174.40 / $84.20 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 857 | 852 | 429 (50%) | 45¢ | 53% | $315.31 | +8% | +7.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 450 | 203 (45%) | 131 / 319 | 8.3 | -$37.76 | -$105.60 | -5% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 402 | 131 (33%) | 175 / 227 | 7.4 | -$55.90 | -$236.75 | -15% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 98 | 35 (36%) | 35 / 63 | 2.0 | -$14.97 | -$40.58 | -10% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 105 | 43 (41%) | 37 / 68 | 2.0 | -$13.69 | -$29.71 | -6% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 41 | 19 (46%) | 14 / 27 | 1.5 | -$10.05 | -$10.80 | -6% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 11 | 6 (55%) | 4 / 7 | 1.6 | -$10.39 | $1.81 | +2% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 3 | 0 (0%) | 1 / 2 | 1.5 | -$5.79 | -$9.04 | -100% |

*Model accuracy vs Kalshi's prices on the same 11,123 readings (excluding the final minute): V1 **+2.7%**, V2 **+2.5%**, 3-exchange price (V3/V4) **+1.1%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $501.81 | $525.36 | $394.02 | 0 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 458 | 330 (72%) | -$89.20 | -6% | 84,628 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.3%** over 22,770 readings from 891 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4259 | 2% | 4% | 6% |
| 10–20% | 1871 | 15% | 16% | 17% |
| 20–30% | 2022 | 25% | 26% | 26% |
| 30–40% | 2199 | 35% | 36% | 38% |
| 40–50% | 2260 | 45% | 47% | 51% |
| 50–60% | 2247 | 55% | 59% | 59% |
| 60–70% | 1910 | 65% | 70% | 68% |
| 70–80% | 1592 | 75% | 80% | 79% |
| 80–90% | 1374 | 85% | 88% | 83% |
| 90–100% | 3036 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 475 | 245 (52%) | 46¢ | 52% | $204.71 | +9% |
| 6–10¢ | 283 | 144 (51%) | 45¢ | 54% | $120.55 | +9% |
| 10–20¢ | 87 | 38 (44%) | 42¢ | 56% | -$2.56 | -1% |
| 20¢+ | 7 | 2 (29%) | 38¢ | 66% | -$7.39 | -27% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 784 | 399 (51%) | 46¢ | 54% | $293.42 | +8% |
| 5–10 min | 62 | 27 (44%) | 38¢ | 47% | $25.16 | +10% |
| 2–5 min | 4 | 2 (50%) | 56¢ | 63% | -$2.87 | -13% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 94 | 20 (21%) | 19¢ | 27% | $12.34 | +7% |
| Toss-up (25–75¢) | 705 | 365 (52%) | 46¢ | 54% | $296.19 | +9% |
| Favorite (75–95¢) | 53 | 44 (83%) | 81¢ | 88% | $6.78 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 97 | 53 (55%) | 42¢ | 52% | $103.27 | +24% |
| XRP | 96 | 50 (52%) | 46¢ | 54% | $38.52 | +8% |
| ETH | 96 | 43 (45%) | 47¢ | 55% | -$34.37 | -7% |
| HYPE | 95 | 44 (46%) | 44¢ | 52% | $8.32 | +2% |
| SOL | 94 | 49 (52%) | 44¢ | 52% | $64.77 | +15% |
| NEAR | 94 | 50 (53%) | 48¢ | 55% | $37.14 | +8% |
| BTC | 94 | 50 (53%) | 50¢ | 58% | $17.73 | +4% |
| ZEC | 93 | 42 (45%) | 41¢ | 50% | $27.89 | +7% |
| DOGE | 93 | 48 (52%) | 44¢ | 53% | $52.04 | +12% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 11:02:06 PM | SOL | DOWN | 12.9 min | 24¢ | 29% | 4¢ | Open | — |
| 9/28 11:02:06 PM | DOGE | DOWN | 12.9 min | 20¢ | 25% | 4¢ | Open | — |
| 9/28 11:01:25 PM | NEAR | DOWN | 13.6 min | 28¢ | 37% | 8¢ | Open | — |
| 9/28 11:01:25 PM | ETH | DOWN | 13.6 min | 29¢ | 35% | 4¢ | Open | — |
| 9/28 11:01:16 PM | BNB | DOWN | 13.7 min | 37¢ | 43% | 4¢ | Open | — |
| 9/28 10:52:11 PM | NEAR | UP | 7.8 min | 30¢ | 36% | 4¢ | ❌ Lost | -$3.16 |
| 9/28 10:52:03 PM | HYPE | DOWN | 8.0 min | 82¢ | 88% | 5¢ | ✅ Won | $1.72 |
| 9/28 10:51:46 PM | DOGE | DOWN | 8.2 min | 67¢ | 82% | 14¢ | ❌ Lost | -$6.86 |
| 9/28 10:48:37 PM | XRP | DOWN | 11.4 min | 84¢ | 89% | 4¢ | ❌ Lost | -$8.50 |
| 9/28 10:48:02 PM | BTC | DOWN | 11.9 min | 74¢ | 80% | 4¢ | ❌ Lost | -$7.54 |
| 9/28 10:47:11 PM | BNB | UP | 12.8 min | 22¢ | 27% | 4¢ | ❌ Lost | -$2.33 |
| 9/28 10:46:51 PM | SOL | UP | 13.1 min | 32¢ | 38% | 4¢ | ✅ Won | $6.69 |
| 9/28 10:46:51 PM | ETH | DOWN | 13.1 min | 57¢ | 63% | 4¢ | ❌ Lost | -$5.88 |
| 9/28 10:46:44 PM | ZEC | DOWN | 13.2 min | 61¢ | 73% | 11¢ | ✅ Won | $3.73 |
| 9/28 10:41:21 PM | XRP | UP | 3.6 min | 10¢ | 16% | 5¢ | ❌ Lost | -$1.04 |
| 9/28 10:38:50 PM | NEAR | DOWN | 6.2 min | 33¢ | 40% | 6¢ | ✅ Won | $6.54 |
| 9/28 10:38:04 PM | HYPE | DOWN | 6.9 min | 87¢ | 93% | 6¢ | ✅ Won | $1.24 |
| 9/28 10:35:31 PM | ETH | DOWN | 9.5 min | 93¢ | 98% | 5¢ | ✅ Won | $0.67 |
| 9/28 10:32:34 PM | BTC | DOWN | 12.4 min | 66¢ | 73% | 6¢ | ✅ Won | $3.24 |
| 9/28 10:31:39 PM | ZEC | DOWN | 13.3 min | 57¢ | 64% | 6¢ | ✅ Won | $4.12 |
| 9/28 10:31:39 PM | BNB | DOWN | 13.3 min | 71¢ | 82% | 9¢ | ✅ Won | $2.71 |
| 9/28 10:31:30 PM | SOL | UP | 13.5 min | 27¢ | 38% | 9¢ | ❌ Lost | -$2.84 |
| 9/28 10:21:48 PM | ZEC | DOWN | 8.2 min | 31¢ | 38% | 5¢ | ❌ Lost | -$3.25 |
| 9/28 10:19:51 PM | XRP | DOWN | 10.1 min | 23¢ | 29% | 4¢ | ❌ Lost | -$2.43 |
| 9/28 10:19:00 PM | DOGE | DOWN | 11.0 min | 34¢ | 43% | 8¢ | ❌ Lost | -$3.56 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
