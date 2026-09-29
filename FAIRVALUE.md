# Fair-Value Bot

*Updated Mon Sep 28, 8:09 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **8¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **8¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 770 | $104.74 | +3% | $206.74 / -$102.00 |
| 4¢+ ← live bot | 741 | $305.24 | +9% | $231.22 / $74.02 |
| 6¢+ | 689 | $301.69 | +10% | $211.50 / $90.19 |
| 8¢+ | 615 | $332.43 | +14% | $145.98 / $186.45 |
| 10¢+ | 532 | $251.61 | +12% | $119.63 / $131.98 |
| 15¢+ | 328 | $222.76 | +20% | $111.80 / $110.96 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 764 | 755 | 382 (51%) | 45¢ | 53% | $319.01 | +9% | +7.3¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 353 | 156 (44%) | 101 / 252 | 8.4 | -$37.76 | -$101.90 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 315 | 113 (36%) | 128 / 187 | 7.5 | -$55.90 | -$141.14 | -11% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 76 | 27 (36%) | 29 / 47 | 1.9 | -$14.97 | -$19.05 | -7% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 81 | 31 (38%) | 25 / 56 | 2.0 | -$13.69 | -$52.65 | -15% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 24 | 10 (42%) | 7 / 17 | 1.4 | -$10.05 | -$14.80 | -14% |

*Model accuracy vs Kalshi's prices on the same 8,629 readings (excluding the final minute): V1 **+2.9%**, V2 **+3.6%**, 3-exchange price (V3/V4) **+1.2%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 361 | 233 (65%) | -$85.50 | -8% | 1,090 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.2%** over 20,090 readings from 783 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3803 | 2% | 4% | 7% |
| 10–20% | 1584 | 15% | 16% | 17% |
| 20–30% | 1801 | 25% | 26% | 26% |
| 30–40% | 1896 | 35% | 36% | 39% |
| 40–50% | 1952 | 45% | 48% | 52% |
| 50–60% | 1958 | 55% | 59% | 60% |
| 60–70% | 1698 | 65% | 71% | 68% |
| 70–80% | 1450 | 75% | 80% | 79% |
| 80–90% | 1256 | 85% | 88% | 81% |
| 90–100% | 2692 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 424 | 220 (52%) | 45¢ | 52% | $210.23 | +11% |
| 6–10¢ | 249 | 127 (51%) | 45¢ | 54% | $117.15 | +10% |
| 10–20¢ | 76 | 33 (43%) | 43¢ | 57% | -$6.46 | -2% |
| 20¢+ | 6 | 2 (33%) | 35¢ | 65% | -$1.91 | -9% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 717 | 369 (51%) | 45¢ | 54% | $324.14 | +10% |
| 5–10 min | 35 | 11 (31%) | 32¢ | 40% | -$5.96 | -5% |
| 2–5 min | 2 | 2 (100%) | 88¢ | 94% | $2.34 | +13% |
| 1–2 min | 1 | 0 (0%) | 14¢ | 72% | -$1.51 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 85 | 19 (22%) | 19¢ | 27% | $22.55 | +13% |
| Toss-up (25–75¢) | 626 | 327 (52%) | 46¢ | 54% | $292.33 | +10% |
| Favorite (75–95¢) | 44 | 36 (82%) | 80¢ | 87% | $4.13 | +1% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| XRP | 85 | 48 (56%) | 47¢ | 55% | $66.62 | +16% |
| ETH | 85 | 37 (44%) | 46¢ | 54% | -$33.39 | -8% |
| BNB | 85 | 46 (54%) | 42¢ | 52% | $86.54 | +23% |
| NEAR | 84 | 45 (54%) | 47¢ | 55% | $39.04 | +9% |
| HYPE | 84 | 38 (45%) | 42¢ | 51% | $13.50 | +4% |
| BTC | 84 | 43 (51%) | 49¢ | 57% | $3.15 | +1% |
| SOL | 83 | 45 (54%) | 44¢ | 52% | $71.67 | +19% |
| DOGE | 83 | 42 (51%) | 44¢ | 52% | $38.37 | +10% |
| ZEC | 82 | 38 (46%) | 41¢ | 50% | $33.51 | +10% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 8:08:32 PM | BTC | UP | 6.5 min | 36¢ | 42% | 5¢ | Open | — |
| 9/28 8:07:27 PM | DOGE | UP | 7.5 min | 19¢ | 26% | 6¢ | Open | — |
| 9/28 8:06:10 PM | XRP | UP | 8.8 min | 39¢ | 46% | 5¢ | Open | — |
| 9/28 8:05:08 PM | NEAR | UP | 9.8 min | 30¢ | 37% | 5¢ | Open | — |
| 9/28 8:02:25 PM | HYPE | DOWN | 12.6 min | 51¢ | 60% | 8¢ | Open | — |
| 9/28 8:01:23 PM | ZEC | DOWN | 13.6 min | 39¢ | 46% | 6¢ | Open | — |
| 9/28 8:01:15 PM | BNB | DOWN | 13.8 min | 34¢ | 41% | 5¢ | Open | — |
| 9/28 8:01:15 PM | SOL | DOWN | 13.8 min | 32¢ | 39% | 5¢ | Open | — |
| 9/28 8:01:15 PM | ETH | DOWN | 13.8 min | 38¢ | 44% | 5¢ | Open | — |
| 9/28 7:52:58 PM | SOL | DOWN | 7.0 min | 24¢ | 35% | 10¢ | ❌ Lost | -$2.53 |
| 9/28 7:51:51 PM | NEAR | UP | 8.1 min | 30¢ | 37% | 6¢ | ✅ Won | $6.85 |
| 9/28 7:50:31 PM | DOGE | DOWN | 9.5 min | 41¢ | 51% | 9¢ | ❌ Lost | -$4.26 |
| 9/28 7:48:40 PM | XRP | DOWN | 11.3 min | 35¢ | 41% | 5¢ | ❌ Lost | -$3.66 |
| 9/28 7:48:08 PM | HYPE | DOWN | 11.9 min | 20¢ | 29% | 8¢ | ❌ Lost | -$2.12 |
| 9/28 7:47:35 PM | ETH | DOWN | 12.4 min | 35¢ | 42% | 6¢ | ❌ Lost | -$3.66 |
| 9/28 7:47:35 PM | BTC | DOWN | 12.4 min | 30¢ | 38% | 6¢ | ❌ Lost | -$3.15 |
| 9/28 7:47:11 PM | ZEC | DOWN | 12.8 min | 26¢ | 33% | 5¢ | ❌ Lost | -$2.74 |
| 9/28 7:46:42 PM | BNB | DOWN | 13.3 min | 22¢ | 29% | 6¢ | ❌ Lost | -$2.33 |
| 9/28 7:37:36 PM | NEAR | UP | 7.4 min | 20¢ | 29% | 8¢ | ❌ Lost | -$2.11 |
| 9/28 7:33:04 PM | ZEC | DOWN | 11.9 min | 29¢ | 39% | 9¢ | ❌ Lost | -$3.05 |
| 9/28 7:31:53 PM | SOL | UP | 13.1 min | 51¢ | 59% | 6¢ | ✅ Won | $4.72 |
| 9/28 7:31:09 PM | BNB | DOWN | 13.8 min | 37¢ | 52% | 13¢ | ❌ Lost | -$3.87 |
| 9/28 7:31:09 PM | DOGE | DOWN | 13.8 min | 35¢ | 42% | 5¢ | ❌ Lost | -$3.66 |
| 9/28 7:31:09 PM | ETH | DOWN | 13.8 min | 31¢ | 43% | 10¢ | ❌ Lost | -$3.25 |
| 9/28 7:31:09 PM | HYPE | DOWN | 13.8 min | 36¢ | 44% | 6¢ | ❌ Lost | -$3.77 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
