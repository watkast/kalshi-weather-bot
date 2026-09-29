# Fair-Value Bot

*Updated Tue Sep 29, 3:21 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **4¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1021 | $141.55 | +3% | $149.93 / -$8.38 |
| 4¢+ ← live bot | 988 | $343.77 | +8% | $175.36 / $168.41 |
| 6¢+ | 910 | $319.77 | +8% | $190.04 / $129.73 |
| 8¢+ | 783 | $304.69 | +10% | $192.96 / $111.73 |
| 10¢+ | 668 | $217.48 | +9% | $202.35 / $15.13 |
| 15¢+ | 401 | $210.26 | +16% | $191.81 / $18.45 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1004 | 996 | 491 (49%) | 45¢ | 53% | $297.43 | +6% | +6.5¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 594 | 265 (45%) | 195 / 399 | 8.5 | -$37.76 | -$123.48 | -4% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 517 | 178 (34%) | 237 / 280 | 7.4 | -$55.90 | -$196.43 | -10% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 127 | 42 (33%) | 38 / 89 | 2.0 | -$14.97 | -$89.02 | -17% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 75% of orders | 135 | 57 (42%) | 50 / 85 | 2.0 | -$13.69 | -$0.29 | -0% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 66 | 31 (47%) | 24 / 42 | 1.6 | -$10.05 | -$5.14 | -2% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 34 | 17 (50%) | 13 / 21 | 1.5 | -$19.37 | $4.27 | +1% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 10 | 3 (30%) | 4 / 6 | 1.7 | -$5.79 | -$6.69 | -18% |

*Model accuracy vs Kalshi's prices on the same 14,348 readings (excluding the final minute): V1 **+1.3%**, V2 **+2.0%**, 3-exchange price (V3/V4) **-0.2%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $504.28 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 602 | 474 (79%) | -$107.08 | -5% | 169,544 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.5%** over 26,233 readings from 1035 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4707 | 2% | 4% | 6% |
| 10–20% | 2114 | 15% | 16% | 17% |
| 20–30% | 2290 | 25% | 26% | 27% |
| 30–40% | 2455 | 35% | 36% | 40% |
| 40–50% | 2580 | 45% | 47% | 52% |
| 50–60% | 2591 | 55% | 58% | 60% |
| 60–70% | 2266 | 65% | 70% | 71% |
| 70–80% | 1855 | 75% | 80% | 82% |
| 80–90% | 1595 | 85% | 87% | 85% |
| 90–100% | 3780 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 531 | 273 (51%) | 46¢ | 52% | $219.95 | +9% |
| 6–10¢ | 342 | 171 (50%) | 44¢ | 53% | $142.35 | +9% |
| 10–20¢ | 114 | 45 (39%) | 42¢ | 56% | -$51.11 | -10% |
| 20¢+ | 9 | 2 (22%) | 36¢ | 65% | -$13.76 | -41% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 899 | 451 (50%) | 45¢ | 54% | $282.66 | +7% |
| 5–10 min | 88 | 35 (40%) | 36¢ | 45% | $20.53 | +6% |
| 2–5 min | 7 | 4 (57%) | 64¢ | 72% | -$5.36 | -12% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 125 | 26 (21%) | 19¢ | 27% | $14.29 | +6% |
| Toss-up (25–75¢) | 802 | 406 (51%) | 46¢ | 54% | $256.87 | +7% |
| Favorite (75–95¢) | 69 | 59 (86%) | 81¢ | 88% | $26.27 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 113 | 59 (52%) | 43¢ | 53% | $88.30 | +18% |
| XRP | 112 | 58 (52%) | 46¢ | 54% | $45.56 | +9% |
| ETH | 112 | 49 (44%) | 46¢ | 54% | -$40.87 | -8% |
| HYPE | 111 | 48 (43%) | 43¢ | 52% | -$18.36 | -4% |
| SOL | 110 | 58 (53%) | 43¢ | 51% | $92.14 | +19% |
| NEAR | 110 | 55 (50%) | 47¢ | 54% | $19.01 | +4% |
| BTC | 110 | 62 (56%) | 50¢ | 58% | $53.85 | +10% |
| ZEC | 109 | 48 (44%) | 41¢ | 50% | $19.57 | +4% |
| DOGE | 109 | 54 (50%) | 44¢ | 53% | $38.23 | +8% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 3:20:31 AM | HYPE | DOWN | 9.5 min | 24¢ | 30% | 5¢ | Open | — |
| 9/29 3:20:16 AM | ETH | DOWN | 9.7 min | 33¢ | 41% | 6¢ | Open | — |
| 9/29 3:18:41 AM | BTC | DOWN | 11.3 min | 36¢ | 43% | 5¢ | Open | — |
| 9/29 3:17:44 AM | SOL | DOWN | 12.3 min | 34¢ | 41% | 5¢ | Open | — |
| 9/29 3:17:29 AM | NEAR | DOWN | 12.5 min | 46¢ | 53% | 6¢ | Open | — |
| 9/29 3:17:22 AM | XRP | DOWN | 12.6 min | 32¢ | 40% | 6¢ | Open | — |
| 9/29 3:16:31 AM | DOGE | DOWN | 13.5 min | 43¢ | 51% | 6¢ | Open | — |
| 9/29 3:16:16 AM | BNB | DOWN | 13.7 min | 52¢ | 61% | 8¢ | Open | — |
| 9/29 3:08:51 AM | NEAR | UP | 6.1 min | 17¢ | 25% | 7¢ | ✅ Won | $8.20 |
| 9/29 3:06:22 AM | DOGE | DOWN | 8.6 min | 80¢ | 86% | 5¢ | ✅ Won | $1.88 |
| 9/29 3:05:07 AM | BTC | UP | 9.9 min | 25¢ | 36% | 10¢ | ❌ Lost | -$2.64 |
| 9/29 3:04:20 AM | XRP | UP | 10.7 min | 31¢ | 37% | 5¢ | ❌ Lost | -$3.25 |
| 9/29 3:03:51 AM | SOL | UP | 11.2 min | 17¢ | 25% | 7¢ | ❌ Lost | -$1.80 |
| 9/29 3:03:28 AM | ZEC | UP | 11.5 min | 28¢ | 36% | 6¢ | ✅ Won | $7.05 |
| 9/29 3:03:02 AM | HYPE | DOWN | 11.9 min | 71¢ | 77% | 4¢ | ✅ Won | $2.75 |
| 9/29 3:01:20 AM | BNB | DOWN | 13.7 min | 52¢ | 64% | 9¢ | ✅ Won | $4.59 |
| 9/29 3:01:03 AM | ETH | UP | 13.9 min | 31¢ | 40% | 8¢ | ❌ Lost | -$3.25 |
| 9/29 2:54:50 AM | BTC | UP | 5.2 min | 19¢ | 27% | 7¢ | ❌ Lost | -$2.01 |
| 9/29 2:54:27 AM | ZEC | UP | 5.5 min | 24¢ | 31% | 6¢ | ❌ Lost | -$2.53 |
| 9/29 2:52:31 AM | HYPE | UP | 7.5 min | 15¢ | 25% | 9¢ | ❌ Lost | -$1.59 |
| 9/29 2:52:25 AM | SOL | UP | 7.6 min | 27¢ | 37% | 8¢ | ✅ Won | $7.16 |
| 9/29 2:52:25 AM | ETH | UP | 7.6 min | 15¢ | 26% | 10¢ | ❌ Lost | -$1.59 |
| 9/29 2:51:55 AM | XRP | DOWN | 8.1 min | 34¢ | 41% | 5¢ | ❌ Lost | -$3.55 |
| 9/29 2:51:55 AM | DOGE | DOWN | 8.1 min | 16¢ | 24% | 7¢ | ❌ Lost | -$1.70 |
| 9/29 2:51:55 AM | BNB | DOWN | 8.1 min | 56¢ | 66% | 8¢ | ✅ Won | $4.22 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
