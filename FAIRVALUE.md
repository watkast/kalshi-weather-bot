# Fair-Value Bot

*Updated Mon Sep 28, 10:52 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 869 | $144.02 | +4% | $166.01 / -$21.99 |
| 4¢+ ← live bot | 838 | $353.82 | +9% | $217.91 / $135.91 |
| 6¢+ | 773 | $382.50 | +12% | $216.45 / $166.05 |
| 8¢+ | 675 | $389.13 | +15% | $190.13 / $199.00 |
| 10¢+ | 581 | $303.24 | +13% | $181.75 / $121.49 |
| 15¢+ | 347 | $257.16 | +22% | $173.86 / $83.30 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 852 | 843 | 426 (51%) | 45¢ | 53% | $337.44 | +9% | +7.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 441 | 200 (45%) | 128 / 313 | 8.3 | -$37.76 | -$83.47 | -4% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 393 | 129 (33%) | 173 / 220 | 7.4 | -$55.90 | -$220.83 | -15% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 96 | 35 (36%) | 35 / 61 | 2.0 | -$14.97 | -$30.44 | -8% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 103 | 41 (40%) | 36 / 67 | 2.0 | -$13.69 | -$37.05 | -8% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 40 | 19 (48%) | 14 / 26 | 1.5 | -$10.05 | -$6.83 | -4% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 10 | 6 (60%) | 4 / 6 | 1.7 | -$10.39 | $11.73 | +12% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 2 | 0 (0%) | 1 / 1 | 2.0 | -$5.79 | -$5.79 | -100% |

*Model accuracy vs Kalshi's prices on the same 10,916 readings (excluding the final minute): V1 **+2.9%**, V2 **+2.7%**, 3-exchange price (V3/V4) **+1.4%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $511.73 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 449 | 321 (71%) | -$67.07 | -4% | 80,308 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.4%** over 22,545 readings from 882 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4198 | 2% | 4% | 6% |
| 10–20% | 1829 | 15% | 16% | 16% |
| 20–30% | 1998 | 25% | 26% | 25% |
| 30–40% | 2187 | 35% | 36% | 38% |
| 40–50% | 2243 | 45% | 47% | 50% |
| 50–60% | 2229 | 55% | 59% | 58% |
| 60–70% | 1889 | 65% | 70% | 68% |
| 70–80% | 1578 | 75% | 80% | 79% |
| 80–90% | 1368 | 85% | 88% | 82% |
| 90–100% | 3026 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 468 | 243 (52%) | 46¢ | 52% | $223.71 | +10% |
| 6–10¢ | 283 | 144 (51%) | 45¢ | 54% | $120.55 | +9% |
| 10–20¢ | 85 | 37 (44%) | 42¢ | 56% | $0.57 | +0% |
| 20¢+ | 7 | 2 (29%) | 38¢ | 66% | -$7.39 | -27% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 778 | 397 (51%) | 45¢ | 54% | $307.25 | +8% |
| 5–10 min | 59 | 26 (44%) | 37¢ | 45% | $33.46 | +15% |
| 2–5 min | 4 | 2 (50%) | 56¢ | 63% | -$2.87 | -13% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 93 | 20 (22%) | 19¢ | 27% | $14.67 | +8% |
| Toss-up (25–75¢) | 699 | 363 (52%) | 46¢ | 54% | $309.21 | +9% |
| Favorite (75–95¢) | 51 | 43 (84%) | 81¢ | 88% | $13.56 | +3% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 96 | 53 (55%) | 43¢ | 52% | $105.60 | +25% |
| XRP | 95 | 50 (53%) | 46¢ | 54% | $47.02 | +10% |
| ETH | 95 | 43 (45%) | 47¢ | 55% | -$28.49 | -6% |
| HYPE | 94 | 43 (46%) | 44¢ | 52% | $6.60 | +2% |
| SOL | 93 | 48 (52%) | 44¢ | 52% | $58.08 | +14% |
| NEAR | 93 | 50 (54%) | 48¢ | 55% | $40.30 | +9% |
| BTC | 93 | 50 (54%) | 49¢ | 58% | $25.27 | +5% |
| ZEC | 92 | 41 (45%) | 40¢ | 49% | $24.16 | +6% |
| DOGE | 92 | 48 (52%) | 44¢ | 52% | $58.90 | +14% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 10:52:11 PM | NEAR | UP | 7.8 min | 30¢ | 36% | 4¢ | Open | — |
| 9/28 10:52:03 PM | HYPE | DOWN | 8.0 min | 82¢ | 88% | 5¢ | Open | — |
| 9/28 10:51:46 PM | DOGE | DOWN | 8.2 min | 67¢ | 82% | 14¢ | Open | — |
| 9/28 10:48:37 PM | XRP | DOWN | 11.4 min | 84¢ | 89% | 4¢ | Open | — |
| 9/28 10:48:02 PM | BTC | DOWN | 11.9 min | 74¢ | 80% | 4¢ | Open | — |
| 9/28 10:47:11 PM | BNB | UP | 12.8 min | 22¢ | 27% | 4¢ | Open | — |
| 9/28 10:46:51 PM | SOL | UP | 13.1 min | 32¢ | 38% | 4¢ | Open | — |
| 9/28 10:46:51 PM | ETH | DOWN | 13.1 min | 57¢ | 63% | 4¢ | Open | — |
| 9/28 10:46:44 PM | ZEC | DOWN | 13.2 min | 61¢ | 73% | 11¢ | Open | — |
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
| 9/28 10:17:48 PM | HYPE | UP | 12.2 min | 82¢ | 91% | 8¢ | ✅ Won | $1.69 |
| 9/28 10:17:48 PM | ETH | UP | 12.2 min | 78¢ | 84% | 4¢ | ✅ Won | $2.07 |
| 9/28 10:17:41 PM | SOL | DOWN | 12.3 min | 24¢ | 37% | 12¢ | ❌ Lost | -$2.53 |
| 9/28 10:17:32 PM | BTC | UP | 12.4 min | 70¢ | 76% | 5¢ | ✅ Won | $2.85 |
| 9/28 10:17:24 PM | BNB | DOWN | 12.6 min | 25¢ | 45% | 19¢ | ❌ Lost | -$2.61 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
