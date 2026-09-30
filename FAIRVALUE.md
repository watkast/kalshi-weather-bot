# Fair-Value Bot

*Updated Wed Sep 30, 9:06 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 2019 | $205.43 | +2% | $145.56 / $59.87 |
| 4¢+ | 1966 | $374.38 | +4% | $347.16 / $27.22 |
| 6¢+ | 1821 | $325.48 | +4% | $319.77 / $5.71 |
| 8¢+ ← live bot | 1584 | $488.51 | +8% | $300.99 / $187.52 |
| 10¢+ | 1352 | $511.58 | +10% | $214.29 / $297.29 |
| 15¢+ | 830 | $578.78 | +21% | $210.31 / $368.47 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1853 | 1848 | 828 (45%) | 43¢ | 52% | $80.84 | +1% | +3.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 467 | 301 | 192 / 109 | $24.54 | $92.72 | $68.18 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1446 | 602 (42%) | 418 / 1028 | 8.1 | -$43.45 | -$340.07 | -5% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1327 | 454 (34%) | 555 / 772 | 7.4 | -$55.90 | -$329.55 | -7% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 333 | 113 (34%) | 86 / 247 | 2.0 | -$14.97 | -$102.64 | -8% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 353 | 149 (42%) | 108 / 245 | 2.0 | -$13.69 | -$29.80 | -2% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 216 | 89 (41%) | 74 / 142 | 1.5 | -$10.05 | -$77.96 | -9% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 7 | 7 (100%) | 1 / 6 | 1.2 | $0.97 | $11.30 | +19% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 53 | 18 (34%) | 20 / 33 | 1.6 | -$5.89 | -$10.64 | -6% |

*Model accuracy vs Kalshi's prices on the same 37,863 readings (excluding the final minute): V1 **+0.7%**, V2 **+1.5%**, 3-exchange price (V3/V4) **-0.3%**.*

![Versions over the 15-minute window](fv/charts/versions.png)

*When in each window every version trades, and how those trades did. V3 only trades 5–10 minutes into the window by design.*

## Risk-managed account (V7)

⛔ **HALTED** — equity $389.72 fell below stop $394.02 (peak $525.36)

| Started with | Equity now | Peak | Stop level | Open positions | Bet size |
|---|---|---|---|---|---|
| $500.00 | $389.72 | $525.36 | $394.02 | 0 of 3 | 2% of equity |

*Trades V5's signals with the safeguards a real-money bot needs: each bet risks at most 2% of the account, at most 3 positions open, never two bets the same direction in one window, and trading halts after a 25% drop from the peak (or below $350). Every buy and sell is double-checked against the ledger — a "sell" that spends money halts everything. Full log: [fv/account_ledger.csv](fv/account_ledger.csv).*

## Could we actually buy at that price?

| Trades checked | 10+ contracts available at our price | P&L (fillable trades only) | Return (fillable only) | Typical contracts available |
|---|---|---|---|---|
| 1454 | 1326 (91%) | -$323.67 | -6% | 251,583 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.3%** over 51,575 readings from 2034 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 8955 | 3% | 4% | 4% |
| 10–20% | 3905 | 15% | 16% | 15% |
| 20–30% | 4307 | 25% | 26% | 26% |
| 30–40% | 4717 | 35% | 37% | 39% |
| 40–50% | 5106 | 45% | 48% | 51% |
| 50–60% | 5030 | 55% | 59% | 59% |
| 60–70% | 4390 | 65% | 71% | 72% |
| 70–80% | 3662 | 75% | 80% | 83% |
| 80–90% | 3395 | 85% | 88% | 89% |
| 90–100% | 8108 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 686 | 308 (45%) | 43¢ | 52% | $59.93 | +2% |
| 10–20¢ | 427 | 172 (40%) | 40¢ | 54% | -$43.98 | -2% |
| 20¢+ | 24 | 10 (42%) | 41¢ | 67% | -$1.48 | -1% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1480 | 684 (46%) | 45¢ | 54% | $10.61 | +0% |
| 5–10 min | 294 | 112 (38%) | 36¢ | 46% | $21.31 | +2% |
| 2–5 min | 65 | 27 (42%) | 33¢ | 46% | $44.66 | +20% |
| 1–2 min | 7 | 3 (43%) | 41¢ | 60% | $0.34 | +1% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 302 | 49 (16%) | 18¢ | 28% | -$87.18 | -15% |
| Toss-up (25–75¢) | 1410 | 659 (47%) | 44¢ | 54% | $98.04 | +2% |
| Favorite (75–95¢) | 136 | 120 (88%) | 82¢ | 90% | $69.98 | +6% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 219 | 94 (43%) | 42¢ | 53% | -$15.66 | -2% |
| ETH | 214 | 97 (45%) | 45¢ | 55% | -$33.46 | -3% |
| HYPE | 210 | 92 (44%) | 42¢ | 53% | -$3.47 | -0% |
| BTC | 206 | 104 (50%) | 48¢ | 57% | $13.95 | +1% |
| XRP | 204 | 93 (46%) | 43¢ | 52% | $14.66 | +2% |
| ZEC | 203 | 81 (40%) | 39¢ | 49% | -$15.06 | -2% |
| DOGE | 202 | 82 (41%) | 42¢ | 51% | -$50.12 | -6% |
| NEAR | 198 | 87 (44%) | 42¢ | 51% | -$0.67 | -0% |
| SOL | 192 | 98 (51%) | 41¢ | 50% | $170.67 | +21% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/30 9:04:53 AM | SOL | DOWN | 10.1 min | 38¢ | 50% | 10¢ | Open | — |
| 9/30 9:04:00 AM | XRP | DOWN | 11.0 min | 29¢ | 41% | 11¢ | Open | — |
| 9/30 9:04:00 AM | DOGE | DOWN | 11.0 min | 31¢ | 45% | 13¢ | Open | — |
| 9/30 9:03:19 AM | ETH | DOWN | 11.7 min | 45¢ | 57% | 10¢ | Open | — |
| 9/30 9:02:07 AM | BNB | DOWN | 12.9 min | 28¢ | 38% | 8¢ | Open | — |
| 9/30 8:54:24 AM | NEAR | DOWN | 5.6 min | 19¢ | 34% | 13¢ | ❌ Lost | -$2.01 |
| 9/30 8:52:02 AM | DOGE | DOWN | 8.0 min | 20¢ | 35% | 14¢ | ❌ Lost | -$2.12 |
| 9/30 8:52:02 AM | ZEC | DOWN | 8.0 min | 41¢ | 54% | 11¢ | ✅ Won | $5.73 |
| 9/30 8:50:55 AM | SOL | DOWN | 9.1 min | 29¢ | 39% | 9¢ | ❌ Lost | -$3.05 |
| 9/30 8:49:59 AM | BTC | DOWN | 10.0 min | 22¢ | 31% | 8¢ | ❌ Lost | -$2.33 |
| 9/30 8:49:43 AM | ETH | DOWN | 10.3 min | 23¢ | 37% | 12¢ | ❌ Lost | -$2.43 |
| 9/30 8:47:47 AM | HYPE | DOWN | 12.2 min | 23¢ | 38% | 13¢ | ❌ Lost | -$2.43 |
| 9/30 8:47:47 AM | BNB | DOWN | 12.2 min | 28¢ | 41% | 11¢ | ❌ Lost | -$2.95 |
| 9/30 8:47:47 AM | XRP | DOWN | 12.2 min | 34¢ | 44% | 8¢ | ❌ Lost | -$3.55 |
| 9/30 8:41:06 AM | BNB | DOWN | 3.9 min | 60¢ | 76% | 14¢ | ❌ Lost | -$6.20 |
| 9/30 8:37:32 AM | SOL | DOWN | 7.5 min | 30¢ | 43% | 12¢ | ✅ Won | $6.85 |
| 9/30 8:37:32 AM | ETH | DOWN | 7.5 min | 63¢ | 78% | 14¢ | ✅ Won | $3.55 |
| 9/30 8:36:32 AM | DOGE | DOWN | 8.4 min | 58¢ | 70% | 10¢ | ✅ Won | $4.02 |
| 9/30 8:34:42 AM | HYPE | UP | 10.3 min | 64¢ | 77% | 11¢ | ✅ Won | $3.43 |
| 9/30 8:34:42 AM | NEAR | UP | 10.3 min | 53¢ | 73% | 18¢ | ✅ Won | $4.52 |
| 9/30 8:33:56 AM | XRP | DOWN | 11.1 min | 30¢ | 42% | 11¢ | ✅ Won | $6.85 |
| 9/30 8:33:21 AM | ZEC | DOWN | 11.6 min | 57¢ | 68% | 9¢ | ✅ Won | $4.08 |
| 9/30 8:32:42 AM | BTC | UP | 12.3 min | 32¢ | 47% | 14¢ | ❌ Lost | -$3.36 |
| 9/30 8:06:23 AM | HYPE | DOWN | 8.6 min | 49¢ | 65% | 14¢ | ✅ Won | $4.90 |
| 9/30 8:04:10 AM | BNB | DOWN | 10.8 min | 46¢ | 69% | 21¢ | ✅ Won | $5.18 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
