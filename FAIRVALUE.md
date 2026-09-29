# Fair-Value Bot

*Updated Mon Sep 28, 9:41 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **6¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **6¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 824 | $161.03 | +4% | $204.27 / -$43.24 |
| 4¢+ ← live bot | 794 | $361.98 | +10% | $247.46 / $114.52 |
| 6¢+ | 733 | $369.31 | +12% | $239.10 / $130.21 |
| 8¢+ | 645 | $366.32 | +15% | $162.59 / $203.73 |
| 10¢+ | 556 | $286.43 | +13% | $176.97 / $109.46 |
| 15¢+ | 336 | $245.30 | +22% | $139.19 / $106.11 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 808 | 799 | 405 (51%) | 44¢ | 53% | $369.79 | +10% | +7.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 397 | 179 (45%) | 113 / 284 | 8.3 | -$37.76 | -$51.12 | -3% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 356 | 123 (35%) | 147 / 209 | 7.4 | -$55.90 | -$163.38 | -12% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 86 | 31 (36%) | 33 / 53 | 2.0 | -$14.97 | -$14.32 | -4% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 93 | 37 (40%) | 30 / 63 | 2.0 | -$13.69 | -$38.33 | -9% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 34 | 16 (47%) | 11 / 23 | 1.5 | -$10.05 | -$5.91 | -4% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 4 | 3 (75%) | 1 / 3 | 1.3 | $2.79 | $21.76 | +54% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 0 | — | 0 / 0 | — | — | — | — |

*Model accuracy vs Kalshi's prices on the same 9,862 readings (excluding the final minute): V1 **+3.0%**, V2 **+3.2%**, 3-exchange price (V3/V4) **+1.3%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $521.76 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 405 | 277 (68%) | -$34.72 | -3% | 33,747 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.4%** over 21,422 readings from 837 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3989 | 2% | 4% | 6% |
| 10–20% | 1706 | 15% | 16% | 16% |
| 20–30% | 1900 | 25% | 26% | 26% |
| 30–40% | 2065 | 35% | 36% | 39% |
| 40–50% | 2099 | 45% | 47% | 52% |
| 50–60% | 2108 | 55% | 59% | 59% |
| 60–70% | 1818 | 65% | 70% | 68% |
| 70–80% | 1536 | 75% | 80% | 79% |
| 80–90% | 1314 | 85% | 88% | 82% |
| 90–100% | 2887 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 446 | 233 (52%) | 45¢ | 52% | $244.20 | +12% |
| 6–10¢ | 266 | 135 (51%) | 44¢ | 53% | $131.34 | +11% |
| 10–20¢ | 81 | 35 (43%) | 42¢ | 56% | -$3.84 | -1% |
| 20¢+ | 6 | 2 (33%) | 35¢ | 65% | -$1.91 | -9% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 747 | 384 (51%) | 45¢ | 53% | $353.52 | +10% |
| 5–10 min | 48 | 18 (38%) | 33¢ | 42% | $14.33 | +9% |
| 2–5 min | 2 | 2 (100%) | 88¢ | 94% | $2.34 | +13% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 89 | 20 (22%) | 19¢ | 27% | $23.28 | +13% |
| Toss-up (25–75¢) | 664 | 347 (52%) | 45¢ | 54% | $340.41 | +11% |
| Favorite (75–95¢) | 46 | 38 (83%) | 80¢ | 87% | $6.10 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 91 | 49 (54%) | 42¢ | 52% | $94.86 | +24% |
| XRP | 90 | 49 (54%) | 46¢ | 54% | $57.59 | +13% |
| ETH | 90 | 39 (43%) | 46¢ | 53% | -$34.11 | -8% |
| HYPE | 89 | 41 (46%) | 42¢ | 51% | $22.80 | +6% |
| SOL | 88 | 47 (53%) | 43¢ | 51% | $73.47 | +19% |
| NEAR | 88 | 48 (55%) | 48¢ | 56% | $43.33 | +10% |
| DOGE | 88 | 46 (52%) | 44¢ | 52% | $58.51 | +15% |
| BTC | 88 | 46 (52%) | 49¢ | 57% | $17.58 | +4% |
| ZEC | 87 | 40 (46%) | 40¢ | 49% | $35.76 | +10% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 9:37:38 PM | XRP | UP | 7.3 min | 66¢ | 76% | 8¢ | Open | — |
| 9/28 9:35:29 PM | DOGE | UP | 9.5 min | 41¢ | 51% | 9¢ | Open | — |
| 9/28 9:33:43 PM | ZEC | UP | 11.3 min | 27¢ | 33% | 5¢ | Open | — |
| 9/28 9:32:51 PM | SOL | DOWN | 12.1 min | 67¢ | 78% | 10¢ | Open | — |
| 9/28 9:32:15 PM | NEAR | DOWN | 12.7 min | 59¢ | 68% | 8¢ | Open | — |
| 9/28 9:31:58 PM | ETH | DOWN | 13.0 min | 68¢ | 75% | 5¢ | Open | — |
| 9/28 9:31:58 PM | HYPE | DOWN | 13.0 min | 66¢ | 75% | 8¢ | Open | — |
| 9/28 9:31:47 PM | BTC | DOWN | 13.2 min | 72¢ | 78% | 4¢ | Open | — |
| 9/28 9:31:36 PM | BNB | DOWN | 13.4 min | 70¢ | 80% | 8¢ | Open | — |
| 9/28 9:19:08 PM | ZEC | DOWN | 10.8 min | 31¢ | 40% | 8¢ | ❌ Lost | -$3.21 |
| 9/28 9:18:30 PM | DOGE | UP | 11.5 min | 65¢ | 76% | 9¢ | ✅ Won | $3.34 |
| 9/28 9:16:52 PM | HYPE | DOWN | 13.1 min | 45¢ | 56% | 9¢ | ❌ Lost | -$4.68 |
| 9/28 9:16:45 PM | XRP | DOWN | 13.2 min | 42¢ | 50% | 6¢ | ❌ Lost | -$4.38 |
| 9/28 9:16:45 PM | ETH | DOWN | 13.2 min | 54¢ | 62% | 6¢ | ❌ Lost | -$5.58 |
| 9/28 9:16:45 PM | SOL | DOWN | 13.2 min | 45¢ | 52% | 5¢ | ❌ Lost | -$4.68 |
| 9/28 9:16:14 PM | BNB | DOWN | 13.8 min | 45¢ | 52% | 5¢ | ❌ Lost | -$4.68 |
| 9/28 9:08:47 PM | NEAR | DOWN | 6.2 min | 91¢ | 97% | 5¢ | ✅ Won | $0.86 |
| 9/28 9:08:17 PM | XRP | DOWN | 6.7 min | 28¢ | 41% | 11¢ | ❌ Lost | -$2.95 |
| 9/28 9:07:21 PM | DOGE | DOWN | 7.7 min | 43¢ | 52% | 7¢ | ✅ Won | $5.52 |
| 9/28 9:03:43 PM | ZEC | UP | 11.3 min | 45¢ | 51% | 4¢ | ❌ Lost | -$4.68 |
| 9/28 9:03:12 PM | BTC | DOWN | 11.8 min | 34¢ | 41% | 6¢ | ✅ Won | $6.44 |
| 9/28 9:01:52 PM | HYPE | DOWN | 13.1 min | 46¢ | 58% | 10¢ | ✅ Won | $5.22 |
| 9/28 9:01:52 PM | SOL | DOWN | 13.1 min | 33¢ | 41% | 7¢ | ❌ Lost | -$3.45 |
| 9/28 9:01:25 PM | ETH | DOWN | 13.6 min | 27¢ | 33% | 4¢ | ❌ Lost | -$2.84 |
| 9/28 9:01:16 PM | BNB | DOWN | 13.7 min | 24¢ | 35% | 9¢ | ❌ Lost | -$2.53 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
