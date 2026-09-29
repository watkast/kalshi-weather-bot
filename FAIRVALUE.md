# Fair-Value Bot

*Updated Mon Sep 28, 10:22 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 851 | $151.98 | +4% | $170.39 / -$18.41 |
| 4¢+ ← live bot | 821 | $349.27 | +9% | $221.52 / $127.75 |
| 6¢+ | 760 | $390.04 | +12% | $239.42 / $150.62 |
| 8¢+ | 668 | $391.91 | +15% | $177.89 / $214.02 |
| 10¢+ | 576 | $304.52 | +14% | $167.44 / $137.08 |
| 15¢+ | 346 | $258.12 | +22% | $173.86 / $84.26 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 835 | 826 | 417 (50%) | 45¢ | 53% | $334.64 | +9% | +7.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 424 | 191 (45%) | 123 / 301 | 8.3 | -$37.76 | -$86.27 | -4% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 380 | 129 (34%) | 166 / 214 | 7.5 | -$55.90 | -$186.62 | -13% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 92 | 32 (35%) | 34 / 58 | 2.0 | -$14.97 | -$34.84 | -10% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 99 | 40 (40%) | 33 / 66 | 2.0 | -$13.69 | -$34.70 | -8% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 39 | 19 (49%) | 14 / 25 | 1.6 | -$10.05 | -$3.68 | -2% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 9 | 6 (67%) | 4 / 5 | 1.8 | -$4.10 | $22.12 | +25% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 2 | 0 (0%) | 1 / 1 | 2.0 | -$5.79 | -$5.79 | -100% |

*Model accuracy vs Kalshi's prices on the same 10,493 readings (excluding the final minute): V1 **+2.8%**, V2 **+2.8%**, 3-exchange price (V3/V4) **+1.2%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $522.12 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 432 | 304 (70%) | -$69.87 | -5% | 72,054 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.3%** over 22,099 readings from 864 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4069 | 2% | 4% | 6% |
| 10–20% | 1795 | 15% | 16% | 16% |
| 20–30% | 1974 | 25% | 26% | 26% |
| 30–40% | 2168 | 35% | 36% | 38% |
| 40–50% | 2226 | 45% | 47% | 51% |
| 50–60% | 2203 | 55% | 59% | 58% |
| 60–70% | 1867 | 65% | 70% | 68% |
| 70–80% | 1555 | 75% | 80% | 79% |
| 80–90% | 1326 | 85% | 88% | 82% |
| 90–100% | 2916 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 458 | 236 (52%) | 45¢ | 52% | $209.70 | +10% |
| 6–10¢ | 278 | 142 (51%) | 45¢ | 54% | $126.62 | +10% |
| 10–20¢ | 83 | 37 (45%) | 42¢ | 56% | $5.71 | +2% |
| 20¢+ | 7 | 2 (29%) | 38¢ | 66% | -$7.39 | -27% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 766 | 391 (51%) | 45¢ | 54% | $308.61 | +9% |
| 5–10 min | 55 | 23 (42%) | 35¢ | 44% | $28.26 | +14% |
| 2–5 min | 3 | 2 (67%) | 72¢ | 78% | -$1.83 | -8% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 89 | 20 (22%) | 19¢ | 27% | $23.28 | +13% |
| Toss-up (25–75¢) | 690 | 358 (52%) | 46¢ | 54% | $303.47 | +9% |
| Favorite (75–95¢) | 47 | 39 (83%) | 80¢ | 87% | $7.89 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 94 | 52 (55%) | 42¢ | 52% | $105.50 | +25% |
| XRP | 93 | 50 (54%) | 47¢ | 55% | $50.49 | +11% |
| ETH | 93 | 41 (44%) | 46¢ | 54% | -$31.23 | -7% |
| HYPE | 92 | 41 (45%) | 43¢ | 51% | $3.67 | +1% |
| SOL | 91 | 48 (53%) | 44¢ | 52% | $63.45 | +15% |
| NEAR | 91 | 49 (54%) | 48¢ | 56% | $37.83 | +8% |
| DOGE | 91 | 48 (53%) | 44¢ | 52% | $62.46 | +15% |
| BTC | 91 | 48 (53%) | 49¢ | 57% | $19.18 | +4% |
| ZEC | 90 | 40 (44%) | 40¢ | 49% | $23.29 | +6% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 10:21:48 PM | ZEC | DOWN | 8.2 min | 31¢ | 38% | 5¢ | Open | — |
| 9/28 10:19:51 PM | XRP | DOWN | 10.1 min | 23¢ | 29% | 4¢ | Open | — |
| 9/28 10:19:00 PM | DOGE | DOWN | 11.0 min | 34¢ | 43% | 8¢ | Open | — |
| 9/28 10:17:48 PM | HYPE | UP | 12.2 min | 82¢ | 91% | 8¢ | Open | — |
| 9/28 10:17:48 PM | ETH | UP | 12.2 min | 78¢ | 84% | 4¢ | Open | — |
| 9/28 10:17:41 PM | SOL | DOWN | 12.3 min | 24¢ | 37% | 12¢ | Open | — |
| 9/28 10:17:32 PM | BTC | UP | 12.4 min | 70¢ | 76% | 5¢ | Open | — |
| 9/28 10:17:24 PM | BNB | DOWN | 12.6 min | 25¢ | 45% | 19¢ | Open | — |
| 9/28 10:17:07 PM | NEAR | DOWN | 12.9 min | 39¢ | 47% | 7¢ | Open | — |
| 9/28 10:10:16 PM | NEAR | UP | 4.7 min | 40¢ | 46% | 4¢ | ❌ Lost | -$4.17 |
| 9/28 10:05:10 PM | BTC | UP | 9.8 min | 48¢ | 57% | 8¢ | ✅ Won | $5.02 |
| 9/28 10:03:52 PM | SOL | DOWN | 11.1 min | 81¢ | 89% | 7¢ | ✅ Won | $1.79 |
| 9/28 10:03:52 PM | DOGE | DOWN | 11.1 min | 74¢ | 85% | 9¢ | ✅ Won | $2.46 |
| 9/28 10:02:50 PM | XRP | UP | 12.2 min | 59¢ | 67% | 6¢ | ❌ Lost | -$6.07 |
| 9/28 10:01:44 PM | ZEC | DOWN | 13.2 min | 53¢ | 76% | 21¢ | ❌ Lost | -$5.48 |
| 9/28 10:01:30 PM | HYPE | DOWN | 13.5 min | 69¢ | 75% | 4¢ | ❌ Lost | -$7.05 |
| 9/28 10:01:11 PM | BNB | DOWN | 13.8 min | 60¢ | 77% | 14¢ | ✅ Won | $3.79 |
| 9/28 10:01:11 PM | ETH | DOWN | 13.8 min | 55¢ | 66% | 9¢ | ❌ Lost | -$5.68 |
| 9/28 9:53:14 PM | DOGE | DOWN | 6.8 min | 41¢ | 56% | 13¢ | ✅ Won | $5.76 |
| 9/28 9:52:31 PM | NEAR | DOWN | 7.5 min | 51¢ | 57% | 4¢ | ✅ Won | $4.73 |
| 9/28 9:50:12 PM | BTC | UP | 9.8 min | 59¢ | 66% | 5¢ | ❌ Lost | -$6.07 |
| 9/28 9:50:06 PM | ETH | DOWN | 9.9 min | 43¢ | 54% | 9¢ | ✅ Won | $5.52 |
| 9/28 9:49:52 PM | HYPE | DOWN | 10.1 min | 51¢ | 58% | 5¢ | ❌ Lost | -$5.32 |
| 9/28 9:47:50 PM | SOL | UP | 12.2 min | 48¢ | 54% | 4¢ | ❌ Lost | -$4.98 |
| 9/28 9:47:23 PM | BNB | DOWN | 12.6 min | 58¢ | 67% | 7¢ | ✅ Won | $4.03 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
