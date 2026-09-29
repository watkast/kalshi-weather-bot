# Fair-Value Bot

*Updated Mon Sep 28, 8:40 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 4¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **4¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **4¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 788 | $179.90 | +5% | $246.87 / -$66.97 |
| 4¢+ ← live bot | 759 | $378.43 | +11% | $267.79 / $110.64 |
| 6¢+ | 704 | $361.89 | +12% | $223.90 / $137.99 |
| 8¢+ | 624 | $355.04 | +15% | $145.98 / $209.06 |
| 10¢+ | 536 | $266.46 | +13% | $130.90 / $135.56 |
| 15¢+ | 329 | $228.38 | +21% | $111.80 / $116.58 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 781 | 773 | 394 (51%) | 45¢ | 53% | $372.65 | +10% | +7.4¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 4¢ edge, no limit per window) | 371 | 168 (45%) | 106 / 265 | 8.4 | -$37.76 | -$48.26 | -3% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 332 | 119 (36%) | 140 / 192 | 7.5 | -$55.90 | -$128.87 | -10% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 80 | 29 (36%) | 31 / 49 | 2.0 | -$14.97 | -$8.89 | -3% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 76% of orders | 85 | 32 (38%) | 28 / 57 | 2.0 | -$13.69 | -$57.22 | -15% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 28 | 12 (43%) | 9 / 19 | 1.5 | -$10.05 | -$15.84 | -13% |

*Model accuracy vs Kalshi's prices on the same 9,043 readings (excluding the final minute): V1 **+3.3%**, V2 **+3.8%**, 3-exchange price (V3/V4) **+1.6%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 379 | 251 (66%) | -$31.86 | -3% | 2,097 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+5.5%** over 20,540 readings from 801 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 3945 | 2% | 4% | 6% |
| 10–20% | 1647 | 15% | 16% | 16% |
| 20–30% | 1847 | 25% | 26% | 26% |
| 30–40% | 1959 | 35% | 36% | 38% |
| 40–50% | 2009 | 45% | 47% | 51% |
| 50–60% | 2005 | 55% | 59% | 58% |
| 60–70% | 1720 | 65% | 71% | 68% |
| 70–80% | 1457 | 75% | 80% | 78% |
| 80–90% | 1258 | 85% | 88% | 81% |
| 90–100% | 2693 | 98% | 97% | 96% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 436 | 229 (53%) | 45¢ | 52% | $253.96 | +12% |
| 6–10¢ | 254 | 130 (51%) | 44¢ | 54% | $129.49 | +11% |
| 10–20¢ | 77 | 33 (43%) | 42¢ | 56% | -$8.89 | -3% |
| 20¢+ | 6 | 2 (33%) | 35¢ | 65% | -$1.91 | -9% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 729 | 379 (52%) | 45¢ | 53% | $377.23 | +11% |
| 5–10 min | 41 | 13 (32%) | 32¢ | 40% | -$5.41 | -4% |
| 2–5 min | 2 | 2 (100%) | 88¢ | 94% | $2.34 | +13% |
| 1–2 min | 1 | 0 (0%) | 14¢ | 72% | -$1.51 | -100% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 87 | 19 (22%) | 19¢ | 27% | $18.11 | +11% |
| Toss-up (25–75¢) | 642 | 339 (53%) | 46¢ | 54% | $350.41 | +12% |
| Favorite (75–95¢) | 44 | 36 (82%) | 80¢ | 87% | $4.13 | +1% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| XRP | 87 | 49 (56%) | 47¢ | 55% | $69.09 | +16% |
| ETH | 87 | 39 (45%) | 46¢ | 54% | -$21.72 | -5% |
| BNB | 87 | 48 (55%) | 42¢ | 52% | $98.57 | +26% |
| NEAR | 86 | 46 (53%) | 47¢ | 55% | $41.36 | +10% |
| HYPE | 86 | 39 (45%) | 42¢ | 51% | $14.56 | +4% |
| BTC | 86 | 44 (51%) | 49¢ | 57% | $5.41 | +1% |
| SOL | 85 | 47 (55%) | 44¢ | 51% | $85.57 | +22% |
| DOGE | 85 | 43 (51%) | 44¢ | 52% | $42.80 | +11% |
| ZEC | 84 | 39 (46%) | 40¢ | 49% | $37.01 | +10% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 8:38:23 PM | SOL | DOWN | 6.6 min | 38¢ | 51% | 11¢ | Open | — |
| 9/28 8:36:21 PM | DOGE | UP | 8.7 min | 30¢ | 36% | 5¢ | Open | — |
| 9/28 8:35:49 PM | BTC | UP | 9.2 min | 41¢ | 51% | 8¢ | Open | — |
| 9/28 8:35:49 PM | HYPE | UP | 9.2 min | 22¢ | 30% | 7¢ | Open | — |
| 9/28 8:34:06 PM | BNB | UP | 10.9 min | 31¢ | 43% | 10¢ | Open | — |
| 9/28 8:31:49 PM | ETH | DOWN | 13.2 min | 38¢ | 45% | 5¢ | Open | — |
| 9/28 8:31:49 PM | XRP | DOWN | 13.2 min | 40¢ | 47% | 5¢ | Open | — |
| 9/28 8:31:13 PM | ZEC | UP | 13.8 min | 32¢ | 41% | 7¢ | Open | — |
| 9/28 8:20:39 PM | SOL | DOWN | 9.3 min | 26¢ | 35% | 7¢ | ✅ Won | $7.26 |
| 9/28 8:20:21 PM | HYPE | DOWN | 9.7 min | 35¢ | 43% | 7¢ | ✅ Won | $6.34 |
| 9/28 8:19:25 PM | ZEC | UP | 10.6 min | 23¢ | 35% | 10¢ | ❌ Lost | -$2.43 |
| 9/28 8:18:49 PM | BTC | DOWN | 11.2 min | 38¢ | 48% | 9¢ | ✅ Won | $6.03 |
| 9/28 8:16:52 PM | NEAR | DOWN | 13.1 min | 43¢ | 49% | 4¢ | ✅ Won | $5.52 |
| 9/28 8:16:23 PM | DOGE | DOWN | 13.6 min | 34¢ | 40% | 4¢ | ✅ Won | $6.44 |
| 9/28 8:16:23 PM | ETH | DOWN | 13.6 min | 42¢ | 48% | 5¢ | ✅ Won | $5.62 |
| 9/28 8:16:23 PM | XRP | DOWN | 13.6 min | 33¢ | 39% | 4¢ | ✅ Won | $6.54 |
| 9/28 8:16:14 PM | BNB | DOWN | 13.8 min | 42¢ | 48% | 4¢ | ✅ Won | $5.62 |
| 9/28 8:08:32 PM | BTC | UP | 6.5 min | 36¢ | 42% | 5¢ | ❌ Lost | -$3.77 |
| 9/28 8:07:27 PM | DOGE | UP | 7.5 min | 19¢ | 26% | 6¢ | ❌ Lost | -$2.01 |
| 9/28 8:06:10 PM | XRP | UP | 8.8 min | 39¢ | 46% | 5¢ | ❌ Lost | -$4.07 |
| 9/28 8:05:08 PM | NEAR | UP | 9.8 min | 30¢ | 37% | 5¢ | ❌ Lost | -$3.20 |
| 9/28 8:02:25 PM | HYPE | DOWN | 12.6 min | 51¢ | 60% | 8¢ | ❌ Lost | -$5.28 |
| 9/28 8:01:23 PM | ZEC | DOWN | 13.6 min | 39¢ | 46% | 6¢ | ✅ Won | $5.93 |
| 9/28 8:01:15 PM | BNB | DOWN | 13.8 min | 34¢ | 41% | 5¢ | ✅ Won | $6.41 |
| 9/28 8:01:15 PM | SOL | DOWN | 13.8 min | 32¢ | 39% | 5¢ | ✅ Won | $6.64 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
