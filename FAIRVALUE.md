# Fair-Value Bot

*Updated Mon Sep 28, 11:22 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 887 | $77.45 | +2% | $156.24 / -$78.79 |
| 4¢+ ← live bot | 856 | $290.10 | +7% | $224.71 / $65.39 |
| 6¢+ | 790 | $343.78 | +10% | $214.12 / $129.66 |
| 8¢+ | 689 | $356.84 | +13% | $182.64 / $174.20 |
| 10¢+ | 593 | $288.69 | +13% | $206.21 / $82.48 |
| 15¢+ | 354 | $246.98 | +21% | $169.86 / $77.12 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 870 | 861 | 430 (50%) | 45¢ | 53% | $289.25 | +7% | +7.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 459 | 204 (44%) | 132 / 327 | 8.3 | -$37.76 | -$131.66 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 410 | 133 (32%) | 177 / 233 | 7.5 | -$55.90 | -$244.24 | -16% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 100 | 35 (35%) | 35 / 65 | 2.0 | -$14.97 | -$51.62 | -13% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 107 | 44 (41%) | 38 / 69 | 2.0 | -$13.69 | -$26.50 | -6% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 43 | 21 (49%) | 15 / 28 | 1.5 | -$10.05 | -$3.62 | -2% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 13 | 8 (62%) | 5 / 8 | 1.6 | -$10.39 | $15.80 | +12% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 3 | 0 (0%) | 1 / 2 | 1.5 | -$5.79 | -$9.04 | -100% |

*Model accuracy vs Kalshi's prices on the same 11,330 readings (excluding the final minute): V1 **+2.2%**, V2 **+2.3%**, 3-exchange price (V3/V4) **+0.7%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

🟢 **Trading**

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $515.80 | $525.36 | $394.02 | 1 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 467 | 339 (73%) | -$115.26 | -7% | 107,535 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.0%** over 22,986 readings from 900 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 4271 | 2% | 4% | 6% |
| 10–20% | 1891 | 15% | 16% | 18% |
| 20–30% | 2033 | 25% | 26% | 26% |
| 30–40% | 2227 | 35% | 36% | 39% |
| 40–50% | 2287 | 45% | 47% | 51% |
| 50–60% | 2273 | 55% | 59% | 59% |
| 60–70% | 1947 | 65% | 70% | 69% |
| 70–80% | 1612 | 75% | 80% | 80% |
| 80–90% | 1381 | 85% | 88% | 83% |
| 90–100% | 3064 | 98% | 97% | 97% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 479 | 245 (51%) | 46¢ | 52% | $193.15 | +9% |
| 6–10¢ | 288 | 145 (50%) | 45¢ | 54% | $106.05 | +8% |
| 10–20¢ | 87 | 38 (44%) | 42¢ | 56% | -$2.56 | -1% |
| 20¢+ | 7 | 2 (29%) | 38¢ | 66% | -$7.39 | -27% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 793 | 400 (50%) | 45¢ | 54% | $267.36 | +7% |
| 5–10 min | 62 | 27 (44%) | 38¢ | 47% | $25.16 | +10% |
| 2–5 min | 4 | 2 (50%) | 56¢ | 63% | -$2.87 | -13% |
| 1–2 min | 2 | 1 (50%) | 51¢ | 83% | -$0.40 | -4% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 97 | 20 (21%) | 19¢ | 27% | $5.80 | +3% |
| Toss-up (25–75¢) | 711 | 366 (51%) | 46¢ | 54% | $276.67 | +8% |
| Favorite (75–95¢) | 53 | 44 (83%) | 81¢ | 88% | $6.78 | +2% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 98 | 53 (54%) | 42¢ | 52% | $99.39 | +23% |
| XRP | 97 | 50 (52%) | 46¢ | 54% | $36.61 | +8% |
| ETH | 97 | 43 (44%) | 47¢ | 54% | -$37.42 | -8% |
| HYPE | 96 | 44 (46%) | 44¢ | 53% | $1.03 | +0% |
| SOL | 95 | 49 (52%) | 43¢ | 51% | $62.24 | +15% |
| NEAR | 95 | 50 (53%) | 47¢ | 55% | $34.19 | +7% |
| BTC | 95 | 51 (54%) | 50¢ | 58% | $21.26 | +4% |
| ZEC | 94 | 42 (45%) | 41¢ | 50% | $22.01 | +6% |
| DOGE | 94 | 48 (51%) | 44¢ | 52% | $49.94 | +12% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 11:19:46 PM | XRP | UP | 10.2 min | 81¢ | 87% | 5¢ | Open | — |
| 9/28 11:18:13 PM | NEAR | DOWN | 11.8 min | 36¢ | 48% | 11¢ | Open | — |
| 9/28 11:17:55 PM | HYPE | DOWN | 12.1 min | 42¢ | 56% | 12¢ | Open | — |
| 9/28 11:17:40 PM | ZEC | DOWN | 12.3 min | 46¢ | 58% | 10¢ | Open | — |
| 9/28 11:17:24 PM | SOL | UP | 12.6 min | 29¢ | 44% | 13¢ | Open | — |
| 9/28 11:17:03 PM | BTC | UP | 12.9 min | 49¢ | 60% | 9¢ | Open | — |
| 9/28 11:16:52 PM | ETH | DOWN | 13.1 min | 35¢ | 42% | 6¢ | Open | — |
| 9/28 11:16:32 PM | DOGE | UP | 13.4 min | 41¢ | 53% | 10¢ | Open | — |
| 9/28 11:16:11 PM | BNB | DOWN | 13.8 min | 47¢ | 53% | 4¢ | Open | — |
| 9/28 11:04:44 PM | ZEC | DOWN | 10.2 min | 57¢ | 68% | 9¢ | ❌ Lost | -$5.88 |
| 9/28 11:03:53 PM | BTC | UP | 11.1 min | 63¢ | 72% | 7¢ | ✅ Won | $3.53 |
| 9/28 11:03:18 PM | HYPE | DOWN | 11.7 min | 71¢ | 79% | 6¢ | ❌ Lost | -$7.29 |
| 9/28 11:03:18 PM | XRP | DOWN | 11.7 min | 18¢ | 27% | 8¢ | ❌ Lost | -$1.91 |
| 9/28 11:02:06 PM | SOL | DOWN | 12.9 min | 24¢ | 29% | 4¢ | ❌ Lost | -$2.53 |
| 9/28 11:02:06 PM | DOGE | DOWN | 12.9 min | 20¢ | 25% | 4¢ | ❌ Lost | -$2.10 |
| 9/28 11:01:25 PM | NEAR | DOWN | 13.6 min | 28¢ | 37% | 8¢ | ❌ Lost | -$2.95 |
| 9/28 11:01:25 PM | ETH | DOWN | 13.6 min | 29¢ | 35% | 4¢ | ❌ Lost | -$3.05 |
| 9/28 11:01:16 PM | BNB | DOWN | 13.7 min | 37¢ | 43% | 4¢ | ❌ Lost | -$3.88 |
| 9/28 10:52:11 PM | NEAR | UP | 7.8 min | 30¢ | 36% | 4¢ | ❌ Lost | -$3.16 |
| 9/28 10:52:03 PM | HYPE | DOWN | 8.0 min | 82¢ | 88% | 5¢ | ✅ Won | $1.72 |
| 9/28 10:51:46 PM | DOGE | DOWN | 8.2 min | 67¢ | 82% | 14¢ | ❌ Lost | -$6.86 |
| 9/28 10:48:37 PM | XRP | DOWN | 11.4 min | 84¢ | 89% | 4¢ | ❌ Lost | -$8.50 |
| 9/28 10:48:02 PM | BTC | DOWN | 11.9 min | 74¢ | 80% | 4¢ | ❌ Lost | -$7.54 |
| 9/28 10:47:11 PM | BNB | UP | 12.8 min | 22¢ | 27% | 4¢ | ❌ Lost | -$2.33 |
| 9/28 10:46:51 PM | SOL | UP | 13.1 min | 32¢ | 38% | 4¢ | ✅ Won | $6.69 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
