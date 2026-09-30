# Fair-Value Bot

*Updated Tue Sep 29, 8:38 PM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1569 | $193.93 | +3% | $159.32 / $34.61 |
| 4¢+ | 1522 | $265.45 | +4% | $380.70 / -$115.25 |
| 6¢+ | 1404 | $231.71 | +4% | $348.39 / -$116.68 |
| 8¢+ ← live bot | 1225 | $350.02 | +7% | $337.83 / $12.19 |
| 10¢+ | 1044 | $356.66 | +9% | $273.30 / $83.36 |
| 15¢+ | 634 | $369.33 | +17% | $251.70 / $117.63 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1506 | 1502 | 693 (46%) | 44¢ | 53% | $59.02 | +1% | +4.0¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 121 | 91 | 56 / 35 | $2.72 | $21.59 | $18.87 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1100 | 467 (42%) | 338 / 762 | 8.4 | -$43.45 | -$361.89 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 960 | 326 (34%) | 417 / 543 | 7.3 | -$55.90 | -$303.78 | -9% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 244 | 83 (34%) | 67 / 177 | 2.0 | -$14.97 | -$109.63 | -12% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 77% of orders | 257 | 110 (43%) | 78 / 179 | 2.0 | -$13.69 | -$19.88 | -2% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 149 | 64 (43%) | 53 / 96 | 1.5 | -$10.05 | -$32.41 | -5% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 1 | 1 (100%) | 0 / 1 | 1.0 | $1.67 | $1.67 | +20% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 32 | 12 (38%) | 12 / 20 | 1.5 | -$5.89 | -$5.03 | -4% |

*Model accuracy vs Kalshi's prices on the same 27,421 readings (excluding the final minute): V1 **+0.2%**, V2 **+1.0%**, 3-exchange price (V3/V4) **-0.9%**.*

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
| 1108 | 980 (88%) | -$345.49 | -8% | 240,840 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+3.9%** over 40,316 readings from 1584 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 7009 | 3% | 4% | 5% |
| 10–20% | 3134 | 15% | 17% | 16% |
| 20–30% | 3382 | 25% | 26% | 28% |
| 30–40% | 3757 | 35% | 36% | 39% |
| 40–50% | 4035 | 45% | 48% | 52% |
| 50–60% | 3956 | 55% | 59% | 59% |
| 60–70% | 3486 | 65% | 70% | 72% |
| 70–80% | 2878 | 75% | 80% | 82% |
| 80–90% | 2546 | 85% | 88% | 87% |
| 90–100% | 6133 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 539 | 251 (47%) | 44¢ | 53% | $50.80 | +2% |
| 10–20¢ | 237 | 99 (42%) | 42¢ | 56% | -$45.93 | -4% |
| 20¢+ | 15 | 5 (33%) | 40¢ | 68% | -$12.22 | -20% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1266 | 602 (48%) | 46¢ | 54% | $58.19 | +1% |
| 5–10 min | 199 | 78 (39%) | 38¢ | 46% | $6.06 | +1% |
| 2–5 min | 32 | 12 (38%) | 35¢ | 46% | $3.28 | +3% |
| 1–2 min | 5 | 1 (20%) | 36¢ | 57% | -$8.51 | -46% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 210 | 38 (18%) | 18¢ | 27% | -$26.29 | -6% |
| Toss-up (25–75¢) | 1173 | 552 (47%) | 45¢ | 54% | $42.75 | +1% |
| Favorite (75–95¢) | 119 | 103 (87%) | 82¢ | 89% | $42.56 | +4% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 172 | 83 (48%) | 44¢ | 54% | $49.84 | +6% |
| XRP | 171 | 79 (46%) | 45¢ | 53% | -$10.51 | -1% |
| ETH | 171 | 75 (44%) | 46¢ | 55% | -$66.95 | -8% |
| HYPE | 166 | 72 (43%) | 44¢ | 53% | -$28.49 | -4% |
| BTC | 166 | 83 (50%) | 49¢ | 58% | -$13.66 | -2% |
| SOL | 165 | 85 (52%) | 41¢ | 50% | $143.18 | +20% |
| ZEC | 165 | 71 (43%) | 41¢ | 50% | $7.62 | +1% |
| NEAR | 163 | 76 (47%) | 44¢ | 52% | $10.86 | +1% |
| DOGE | 163 | 69 (42%) | 43¢ | 52% | -$32.87 | -5% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 8:32:46 PM | ETH | DOWN | 12.2 min | 48¢ | 59% | 9¢ | Open | — |
| 9/29 8:32:12 PM | ZEC | DOWN | 12.8 min | 33¢ | 44% | 9¢ | Open | — |
| 9/29 8:32:12 PM | HYPE | DOWN | 12.8 min | 28¢ | 41% | 12¢ | Open | — |
| 9/29 8:31:27 PM | BNB | DOWN | 13.5 min | 45¢ | 57% | 10¢ | Open | — |
| 9/29 8:25:14 PM | BTC | UP | 4.8 min | 34¢ | 47% | 12¢ | ❌ Lost | -$3.56 |
| 9/29 8:21:39 PM | SOL | UP | 8.3 min | 11¢ | 20% | 8¢ | ❌ Lost | -$1.17 |
| 9/29 8:21:10 PM | XRP | UP | 8.8 min | 22¢ | 33% | 9¢ | ❌ Lost | -$2.33 |
| 9/29 8:19:00 PM | HYPE | DOWN | 11.0 min | 68¢ | 80% | 10¢ | ✅ Won | $3.04 |
| 9/29 8:18:59 PM | ETH | DOWN | 11.0 min | 73¢ | 83% | 9¢ | ✅ Won | $2.56 |
| 9/29 8:16:06 PM | BNB | DOWN | 13.9 min | 45¢ | 65% | 18¢ | ❌ Lost | -$4.68 |
| 9/29 8:13:01 PM | BTC | DOWN | 2.0 min | 23¢ | 38% | 13¢ | ❌ Lost | -$2.43 |
| 9/29 8:04:43 PM | ZEC | DOWN | 10.3 min | 38¢ | 50% | 11¢ | ✅ Won | $6.03 |
| 9/29 8:04:26 PM | SOL | UP | 10.6 min | 80¢ | 89% | 8¢ | ✅ Won | $1.88 |
| 9/29 8:03:11 PM | DOGE | DOWN | 11.8 min | 37¢ | 47% | 9¢ | ❌ Lost | -$3.87 |
| 9/29 8:03:11 PM | XRP | DOWN | 11.8 min | 48¢ | 59% | 10¢ | ❌ Lost | -$4.98 |
| 9/29 8:02:19 PM | HYPE | DOWN | 12.7 min | 52¢ | 63% | 9¢ | ✅ Won | $4.62 |
| 9/29 8:02:18 PM | ETH | DOWN | 12.7 min | 31¢ | 41% | 9¢ | ❌ Lost | -$3.25 |
| 9/29 8:01:14 PM | NEAR | DOWN | 13.8 min | 25¢ | 38% | 11¢ | ✅ Won | $7.36 |
| 9/29 8:01:03 PM | BNB | DOWN | 13.9 min | 39¢ | 57% | 17¢ | ❌ Lost | -$4.03 |
| 9/29 7:56:50 PM | BTC | DOWN | 3.2 min | 56¢ | 71% | 13¢ | ❌ Lost | -$5.78 |
| 9/29 7:56:02 PM | DOGE | UP | 4.0 min | 20¢ | 30% | 9¢ | ❌ Lost | -$2.12 |
| 9/29 7:55:05 PM | SOL | DOWN | 4.9 min | 42¢ | 53% | 9¢ | ✅ Won | $5.62 |
| 9/29 7:54:48 PM | XRP | UP | 5.2 min | 35¢ | 52% | 15¢ | ❌ Lost | -$3.66 |
| 9/29 7:52:34 PM | NEAR | DOWN | 7.4 min | 58¢ | 68% | 8¢ | ✅ Won | $4.02 |
| 9/29 7:48:57 PM | HYPE | DOWN | 11.1 min | 56¢ | 71% | 14¢ | ✅ Won | $4.22 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
