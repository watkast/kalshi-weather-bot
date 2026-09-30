# Fair-Value Bot

*Updated Wed Sep 30, 1:55 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1758 | $247.99 | +3% | $111.63 / $136.36 |
| 4¢+ | 1710 | $365.25 | +5% | $298.88 / $66.37 |
| 6¢+ | 1582 | $302.74 | +4% | $339.10 / -$36.36 |
| 8¢+ ← live bot | 1378 | $446.06 | +8% | $356.84 / $89.22 |
| 10¢+ | 1169 | $442.53 | +10% | $299.95 / $142.58 |
| 15¢+ | 718 | $499.99 | +20% | $234.13 / $265.86 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1652 | 1645 | 755 (46%) | 44¢ | 53% | $105.23 | +1% | +3.5¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 264 | 173 | 110 / 63 | $48.93 | $52.40 | $3.47 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1243 | 529 (43%) | 363 / 880 | 8.2 | -$43.45 | -$315.68 | -6% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1112 | 377 (34%) | 454 / 658 | 7.4 | -$55.90 | -$358.28 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 281 | 98 (35%) | 72 / 209 | 2.0 | -$14.97 | -$115.91 | -11% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 299 | 132 (44%) | 90 / 209 | 2.0 | -$13.69 | $1.62 | +0% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 178 | 76 (43%) | 62 / 116 | 1.5 | -$10.05 | -$47.45 | -7% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 3 | 3 (100%) | 0 / 3 | 1.0 | $0.97 | $4.52 | +18% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 40 | 15 (38%) | 15 / 25 | 1.5 | -$5.89 | $0.78 | +1% |

*Model accuracy vs Kalshi's prices on the same 31,867 readings (excluding the final minute): V1 **+0.7%**, V2 **+1.3%**, 3-exchange price (V3/V4) **-0.4%**.*

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
| 1251 | 1123 (90%) | -$299.28 | -6% | 248,024 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.3%** over 45,093 readings from 1773 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 7941 | 3% | 4% | 5% |
| 10–20% | 3505 | 15% | 17% | 15% |
| 20–30% | 3821 | 25% | 26% | 26% |
| 30–40% | 4200 | 35% | 37% | 38% |
| 40–50% | 4480 | 45% | 48% | 50% |
| 50–60% | 4370 | 55% | 59% | 58% |
| 60–70% | 3861 | 65% | 71% | 72% |
| 70–80% | 3192 | 75% | 80% | 82% |
| 80–90% | 2888 | 85% | 88% | 88% |
| 90–100% | 6835 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 605 | 282 (47%) | 43¢ | 53% | $106.00 | +4% |
| 10–20¢ | 309 | 128 (41%) | 42¢ | 56% | -$55.20 | -4% |
| 20¢+ | 20 | 7 (35%) | 39¢ | 67% | -$11.94 | -15% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1355 | 642 (47%) | 45¢ | 54% | $80.46 | +1% |
| 5–10 min | 238 | 92 (39%) | 37¢ | 46% | $4.68 | +1% |
| 2–5 min | 44 | 17 (39%) | 32¢ | 44% | $22.99 | +16% |
| 1–2 min | 6 | 2 (33%) | 44¢ | 63% | -$6.82 | -25% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 248 | 42 (17%) | 18¢ | 27% | -$56.54 | -12% |
| Toss-up (25–75¢) | 1270 | 602 (47%) | 45¢ | 54% | $104.89 | +2% |
| Favorite (75–95¢) | 127 | 111 (87%) | 82¢ | 90% | $56.88 | +5% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 191 | 88 (46%) | 43¢ | 54% | $31.66 | +4% |
| ETH | 190 | 85 (45%) | 46¢ | 55% | -$55.34 | -6% |
| HYPE | 184 | 84 (46%) | 43¢ | 53% | $16.45 | +2% |
| XRP | 183 | 84 (46%) | 45¢ | 54% | -$14.96 | -2% |
| ZEC | 182 | 76 (42%) | 40¢ | 50% | $1.89 | +0% |
| BTC | 182 | 94 (52%) | 49¢ | 58% | $16.19 | +2% |
| DOGE | 179 | 75 (42%) | 42¢ | 51% | -$29.50 | -4% |
| SOL | 177 | 88 (50%) | 41¢ | 50% | $126.44 | +17% |
| NEAR | 177 | 81 (46%) | 44¢ | 52% | $12.40 | +2% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/30 1:55:05 AM | BTC | UP | 4.9 min | 34¢ | 45% | 9¢ | Open | — |
| 9/30 1:51:25 AM | ETH | DOWN | 8.6 min | 33¢ | 47% | 12¢ | Open | — |
| 9/30 1:51:03 AM | DOGE | DOWN | 8.9 min | 20¢ | 32% | 10¢ | Open | — |
| 9/30 1:50:39 AM | BNB | DOWN | 9.3 min | 50¢ | 60% | 8¢ | Open | — |
| 9/30 1:50:13 AM | NEAR | DOWN | 9.8 min | 28¢ | 40% | 10¢ | Open | — |
| 9/30 1:48:52 AM | HYPE | DOWN | 11.1 min | 32¢ | 47% | 13¢ | Open | — |
| 9/30 1:46:52 AM | ZEC | DOWN | 13.1 min | 46¢ | 59% | 11¢ | Open | — |
| 9/30 1:38:41 AM | BTC | DOWN | 6.3 min | 9¢ | 18% | 8¢ | ❌ Lost | -$0.96 |
| 9/30 1:38:41 AM | SOL | DOWN | 6.3 min | 10¢ | 19% | 8¢ | ❌ Lost | -$1.03 |
| 9/30 1:38:07 AM | XRP | DOWN | 6.9 min | 12¢ | 24% | 11¢ | ❌ Lost | -$1.28 |
| 9/30 1:36:09 AM | DOGE | DOWN | 8.8 min | 19¢ | 34% | 14¢ | ❌ Lost | -$2.01 |
| 9/30 1:35:30 AM | BNB | DOWN | 9.5 min | 43¢ | 56% | 12¢ | ❌ Lost | -$4.47 |
| 9/30 1:34:36 AM | ETH | DOWN | 10.4 min | 38¢ | 51% | 12¢ | ❌ Lost | -$3.97 |
| 9/30 1:34:36 AM | ZEC | DOWN | 10.4 min | 34¢ | 45% | 9¢ | ❌ Lost | -$3.56 |
| 9/30 1:17:56 AM | XRP | DOWN | 12.1 min | 21¢ | 31% | 8¢ | ❌ Lost | -$2.22 |
| 9/30 1:16:53 AM | ETH | DOWN | 13.1 min | 25¢ | 40% | 14¢ | ❌ Lost | -$2.64 |
| 9/30 1:16:53 AM | ZEC | DOWN | 13.1 min | 30¢ | 44% | 13¢ | ❌ Lost | -$3.15 |
| 9/30 1:16:34 AM | SOL | DOWN | 13.4 min | 24¢ | 37% | 12¢ | ❌ Lost | -$2.53 |
| 9/30 1:16:28 AM | NEAR | DOWN | 13.5 min | 31¢ | 41% | 8¢ | ❌ Lost | -$3.25 |
| 9/30 1:16:27 AM | BTC | DOWN | 13.6 min | 26¢ | 36% | 9¢ | ❌ Lost | -$2.74 |
| 9/30 1:16:09 AM | DOGE | DOWN | 13.8 min | 31¢ | 41% | 9¢ | ❌ Lost | -$3.25 |
| 9/30 1:16:09 AM | HYPE | DOWN | 13.8 min | 21¢ | 31% | 9¢ | ❌ Lost | -$2.22 |
| 9/30 1:16:09 AM | BNB | DOWN | 13.8 min | 27¢ | 41% | 13¢ | ❌ Lost | -$2.84 |
| 9/30 1:07:27 AM | SOL | UP | 7.5 min | 22¢ | 34% | 11¢ | ❌ Lost | -$2.33 |
| 9/30 1:05:55 AM | ZEC | UP | 9.1 min | 18¢ | 28% | 10¢ | ❌ Lost | -$1.86 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
