# Fair-Value Bot

*Updated Tue Sep 29, 5:53 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1111 | $53.77 | +1% | $175.66 / -$121.89 |
| 4¢+ ← live bot | 1073 | $288.15 | +6% | $214.92 / $73.23 |
| 6¢+ | 985 | $287.06 | +7% | $216.50 / $70.56 |
| 8¢+ | 850 | $314.46 | +9% | $177.68 / $136.78 |
| 10¢+ | 725 | $231.45 | +8% | $172.69 / $58.76 |
| 15¢+ | 445 | $231.76 | +15% | $166.69 / $65.07 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1090 | 1081 | 512 (47%) | 44¢ | 53% | $171.65 | +3% | +5.6¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 679 | 286 (42%) | 220 / 459 | 8.5 | -$43.45 | -$249.26 | -8% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 586 | 196 (33%) | 263 / 323 | 7.3 | -$55.90 | -$259.64 | -12% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 144 | 47 (33%) | 42 / 102 | 1.9 | -$14.97 | -$89.29 | -16% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 155 | 62 (40%) | 53 / 102 | 2.0 | -$13.69 | -$33.52 | -5% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 78 | 35 (45%) | 27 / 51 | 1.5 | -$10.05 | -$17.39 | -5% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 46 | 21 (46%) | 16 / 30 | 1.5 | -$20.08 | -$40.54 | -9% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 11 | 3 (27%) | 4 / 7 | 1.6 | -$5.79 | -$9.53 | -24% |

*Model accuracy vs Kalshi's prices on the same 16,436 readings (excluding the final minute): V1 **+0.9%**, V2 **+1.5%**, 3-exchange price (V3/V4) **-0.5%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $459.47 | $525.36 | $394.02 | 0 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 687 | 559 (81%) | -$232.86 | -9% | 213,648 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.3%** over 28,464 readings from 1125 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4995 | 2% | 4% | 6% |
| 10–20% | 2238 | 15% | 16% | 16% |
| 20–30% | 2419 | 25% | 26% | 26% |
| 30–40% | 2639 | 35% | 36% | 39% |
| 40–50% | 2784 | 45% | 48% | 53% |
| 50–60% | 2804 | 55% | 59% | 61% |
| 60–70% | 2441 | 65% | 70% | 72% |
| 70–80% | 2029 | 75% | 80% | 82% |
| 80–90% | 1786 | 85% | 88% | 86% |
| 90–100% | 4329 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 569 | 282 (50%) | 45¢ | 52% | $159.30 | +6% |
| 6–10¢ | 375 | 180 (48%) | 44¢ | 53% | $106.03 | +6% |
| 10–20¢ | 128 | 48 (38%) | 42¢ | 56% | -$79.92 | -14% |
| 20¢+ | 9 | 2 (22%) | 36¢ | 65% | -$13.76 | -41% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 975 | 472 (48%) | 45¢ | 53% | $180.69 | +4% |
| 5–10 min | 96 | 35 (36%) | 35¢ | 44% | -$0.44 | -0% |
| 2–5 min | 8 | 4 (50%) | 59¢ | 67% | -$8.20 | -17% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 143 | 27 (19%) | 18¢ | 27% | -$9.55 | -3% |
| Toss-up (25–75¢) | 866 | 423 (49%) | 45¢ | 54% | $151.33 | +4% |
| Favorite (75–95¢) | 72 | 62 (86%) | 81¢ | 88% | $29.87 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 123 | 63 (51%) | 43¢ | 53% | $81.22 | +15% |
| XRP | 122 | 59 (48%) | 45¢ | 52% | $27.17 | +5% |
| ETH | 122 | 52 (43%) | 45¢ | 53% | -$44.83 | -8% |
| NEAR | 120 | 59 (49%) | 46¢ | 54% | $14.19 | +2% |
| HYPE | 120 | 50 (42%) | 43¢ | 52% | -$34.33 | -6% |
| SOL | 119 | 60 (50%) | 42¢ | 50% | $78.13 | +15% |
| DOGE | 119 | 55 (46%) | 44¢ | 52% | $9.44 | +2% |
| ZEC | 118 | 50 (42%) | 41¢ | 50% | $1.31 | +0% |
| BTC | 118 | 64 (54%) | 49¢ | 57% | $39.35 | +7% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 5:51:42 AM | XRP | UP | 8.3 min | 91¢ | 97% | 5¢ | Open | — |
| 9/29 5:51:16 AM | ETH | UP | 8.7 min | 80¢ | 98% | 17¢ | Open | — |
| 9/29 5:50:11 AM | SOL | UP | 9.8 min | 88¢ | 98% | 10¢ | Open | — |
| 9/29 5:47:16 AM | BTC | DOWN | 12.7 min | 26¢ | 33% | 5¢ | Open | — |
| 9/29 5:46:54 AM | DOGE | DOWN | 13.1 min | 26¢ | 34% | 7¢ | Open | — |
| 9/29 5:46:39 AM | NEAR | DOWN | 13.3 min | 40¢ | 47% | 6¢ | Open | — |
| 9/29 5:46:32 AM | ZEC | DOWN | 13.4 min | 18¢ | 28% | 10¢ | Open | — |
| 9/29 5:46:24 AM | HYPE | DOWN | 13.6 min | 21¢ | 28% | 5¢ | Open | — |
| 9/29 5:46:24 AM | BNB | DOWN | 13.6 min | 30¢ | 45% | 14¢ | Open | — |
| 9/29 5:32:58 AM | BTC | UP | 12.0 min | 92¢ | 97% | 5¢ | ✅ Won | $0.78 |
| 9/29 5:32:48 AM | ETH | DOWN | 12.2 min | 11¢ | 19% | 8¢ | ❌ Lost | -$1.17 |
| 9/29 5:32:48 AM | NEAR | DOWN | 12.2 min | 17¢ | 28% | 10¢ | ❌ Lost | -$1.80 |
| 9/29 5:31:57 AM | ZEC | DOWN | 13.0 min | 42¢ | 52% | 8¢ | ❌ Lost | -$4.38 |
| 9/29 5:31:57 AM | SOL | DOWN | 13.0 min | 32¢ | 40% | 7¢ | ❌ Lost | -$3.36 |
| 9/29 5:31:38 AM | XRP | DOWN | 13.4 min | 25¢ | 32% | 6¢ | ❌ Lost | -$2.64 |
| 9/29 5:31:23 AM | DOGE | DOWN | 13.6 min | 29¢ | 38% | 8¢ | ❌ Lost | -$3.05 |
| 9/29 5:31:16 AM | BNB | DOWN | 13.7 min | 30¢ | 48% | 17¢ | ❌ Lost | -$3.15 |
| 9/29 5:21:38 AM | BTC | DOWN | 8.3 min | 36¢ | 51% | 13¢ | ❌ Lost | -$3.77 |
| 9/29 5:19:39 AM | ETH | DOWN | 10.3 min | 36¢ | 42% | 4¢ | ❌ Lost | -$3.77 |
| 9/29 5:19:19 AM | XRP | DOWN | 10.7 min | 34¢ | 40% | 4¢ | ❌ Lost | -$3.56 |
| 9/29 5:17:22 AM | ZEC | DOWN | 12.6 min | 45¢ | 52% | 5¢ | ❌ Lost | -$4.68 |
| 9/29 5:16:54 AM | HYPE | DOWN | 13.1 min | 57¢ | 64% | 6¢ | ❌ Lost | -$5.88 |
| 9/29 5:16:54 AM | DOGE | DOWN | 13.1 min | 59¢ | 70% | 10¢ | ❌ Lost | -$6.05 |
| 9/29 5:16:54 AM | NEAR | DOWN | 13.1 min | 50¢ | 61% | 9¢ | ❌ Lost | -$5.18 |
| 9/29 5:16:54 AM | SOL | DOWN | 13.1 min | 45¢ | 56% | 9¢ | ❌ Lost | -$4.68 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
