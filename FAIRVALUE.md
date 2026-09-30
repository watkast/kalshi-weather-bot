# Fair-Value Bot

*Updated Wed Sep 30, 8:46 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 2010 | $236.21 | +2% | $148.69 / $87.52 |
| 4¢+ | 1957 | $404.45 | +4% | $348.65 / $55.80 |
| 6¢+ | 1813 | $346.08 | +4% | $321.80 / $24.28 |
| 8¢+ ← live bot | 1577 | $501.76 | +8% | $311.17 / $190.59 |
| 10¢+ | 1347 | $516.14 | +10% | $224.35 / $291.79 |
| 15¢+ | 828 | $575.67 | +20% | $212.11 / $363.56 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1839 | 1839 | 827 (45%) | 43¢ | 53% | $95.98 | +1% | +3.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 458 | 300 | 192 / 108 | $39.68 | $106.17 | $66.49 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1437 | 601 (42%) | 418 / 1019 | 8.1 | -$43.45 | -$324.93 | -5% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1318 | 453 (34%) | 555 / 763 | 7.4 | -$55.90 | -$297.15 | -6% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 331 | 113 (34%) | 86 / 245 | 2.0 | -$14.97 | -$97.26 | -8% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 351 | 149 (42%) | 108 / 243 | 2.0 | -$13.69 | -$20.80 | -1% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 215 | 89 (41%) | 74 / 141 | 1.5 | -$10.05 | -$75.01 | -9% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 6 | 6 (100%) | 1 / 5 | 1.2 | $0.97 | $10.08 | +20% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 51 | 17 (33%) | 19 / 32 | 1.5 | -$5.89 | -$15.36 | -8% |

*Model accuracy vs Kalshi's prices on the same 37,656 readings (excluding the final minute): V1 **+0.7%**, V2 **+1.6%**, 3-exchange price (V3/V4) **-0.3%**.*

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
| 1445 | 1317 (91%) | -$308.53 | -5% | 251,059 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.3%** over 51,350 readings from 2025 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 8953 | 3% | 4% | 4% |
| 10–20% | 3905 | 15% | 16% | 15% |
| 20–30% | 4307 | 25% | 26% | 26% |
| 30–40% | 4710 | 35% | 37% | 39% |
| 40–50% | 5084 | 45% | 48% | 51% |
| 50–60% | 4992 | 55% | 59% | 58% |
| 60–70% | 4358 | 65% | 71% | 72% |
| 70–80% | 3625 | 75% | 80% | 83% |
| 80–90% | 3375 | 85% | 88% | 89% |
| 90–100% | 8041 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 683 | 308 (45%) | 43¢ | 52% | $68.86 | +2% |
| 10–20¢ | 421 | 171 (41%) | 40¢ | 54% | -$37.77 | -2% |
| 20¢+ | 24 | 10 (42%) | 41¢ | 67% | -$1.48 | -1% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1475 | 684 (46%) | 45¢ | 54% | $24.30 | +0% |
| 5–10 min | 290 | 111 (38%) | 36¢ | 46% | $22.76 | +2% |
| 2–5 min | 65 | 27 (42%) | 33¢ | 46% | $44.66 | +20% |
| 1–2 min | 7 | 3 (43%) | 41¢ | 60% | $0.34 | +1% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 297 | 49 (16%) | 18¢ | 28% | -$75.86 | -13% |
| Toss-up (25–75¢) | 1406 | 658 (47%) | 44¢ | 54% | $101.86 | +2% |
| Favorite (75–95¢) | 136 | 120 (88%) | 82¢ | 90% | $69.98 | +6% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 218 | 94 (43%) | 42¢ | 53% | -$12.71 | -1% |
| ETH | 213 | 97 (46%) | 45¢ | 55% | -$31.03 | -3% |
| HYPE | 209 | 92 (44%) | 43¢ | 53% | -$1.04 | -0% |
| BTC | 205 | 104 (51%) | 48¢ | 58% | $16.28 | +2% |
| XRP | 203 | 93 (46%) | 43¢ | 52% | $18.21 | +2% |
| ZEC | 202 | 80 (40%) | 39¢ | 49% | -$20.79 | -3% |
| DOGE | 201 | 82 (41%) | 42¢ | 51% | -$48.00 | -6% |
| NEAR | 197 | 87 (44%) | 43¢ | 51% | $1.34 | +0% |
| SOL | 191 | 98 (51%) | 41¢ | 50% | $173.72 | +22% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
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
| 9/30 8:04:10 AM | SOL | DOWN | 10.8 min | 40¢ | 52% | 11¢ | ✅ Won | $5.83 |
| 9/30 8:02:55 AM | NEAR | DOWN | 12.1 min | 43¢ | 55% | 10¢ | ❌ Lost | -$4.48 |
| 9/30 8:02:08 AM | BTC | UP | 12.8 min | 27¢ | 37% | 8¢ | ❌ Lost | -$2.84 |
| 9/30 8:01:39 AM | DOGE | UP | 13.3 min | 46¢ | 58% | 10¢ | ❌ Lost | -$4.78 |
| 9/30 8:01:23 AM | ZEC | DOWN | 13.6 min | 32¢ | 53% | 19¢ | ❌ Lost | -$3.41 |
| 9/30 8:01:23 AM | XRP | DOWN | 13.6 min | 38¢ | 51% | 11¢ | ✅ Won | $6.03 |
| 9/30 8:01:23 AM | ETH | DOWN | 13.6 min | 42¢ | 55% | 11¢ | ✅ Won | $5.62 |
| 9/30 7:48:12 AM | XRP | DOWN | 11.8 min | 27¢ | 42% | 13¢ | ✅ Won | $7.16 |
| 9/30 7:48:12 AM | BTC | DOWN | 11.8 min | 25¢ | 37% | 10¢ | ❌ Lost | -$2.64 |
| 9/30 7:47:05 AM | ZEC | DOWN | 12.9 min | 32¢ | 47% | 14¢ | ❌ Lost | -$3.36 |
| 9/30 7:46:45 AM | ETH | DOWN | 13.2 min | 34¢ | 45% | 10¢ | ❌ Lost | -$3.56 |
| 9/30 7:46:45 AM | HYPE | DOWN | 13.2 min | 34¢ | 49% | 14¢ | ✅ Won | $6.44 |
| 9/30 7:46:24 AM | NEAR | DOWN | 13.6 min | 49¢ | 59% | 9¢ | ✅ Won | $4.92 |
| 9/30 7:46:24 AM | BNB | DOWN | 13.6 min | 40¢ | 51% | 9¢ | ❌ Lost | -$4.20 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
