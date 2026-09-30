# Fair-Value Bot

*Updated Wed Sep 30, 7:25 AM MT. Paper money. Kalshi's 15-minute crypto up/down markets: every 2 seconds the bot works out the fair chance of UP from the live Coinbase price, the target price, time left and recent volatility, then buys whichever side is at least 8¢ cheaper than fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Gold & Silver version](METALS.md)

## Current strategy

🟢 **Trade small.** Buying when the edge is **15¢+** made money in both halves of the data, and the model predicts better than Kalshi's prices.

1. **Every 2 seconds**, compute the fair chance of UP for each 15-minute crypto market.
2. **Buy** whichever side's price is at least **15¢ below** that fair chance after fees, priced 5¢–95¢, with 30 sec–14 min left. 10 contracts, one trade per window.
3. **Hold** to the close.

**Which edge threshold works best?** (replayed from the 30-second shadow log)

| Buy when edge is | Trades | P&L | Return | Earlier / later half |
|---|---|---|---|---|
| 2¢+ | 1956 | $161.08 | +2% | $63.08 / $98.00 |
| 4¢+ | 1904 | $327.11 | +4% | $311.16 / $15.95 |
| 6¢+ | 1763 | $244.25 | +3% | $344.28 / -$100.03 |
| 8¢+ ← live bot | 1535 | $395.69 | +6% | $316.05 / $79.64 |
| 10¢+ | 1308 | $417.07 | +8% | $224.98 / $192.09 |
| 15¢+ | 807 | $574.84 | +21% | $221.20 / $353.64 |

## Live bot results

| Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return | Avg price move 3 min after buying |
|---|---|---|---|---|---|---|---|
| 1806 | 1797 | 802 (45%) | 43¢ | 53% | $16.38 | +0% | +3.1¢ |

*If the model is right, the win rate should land near the model's average chance, above the average price paid. "Price move 3 min after buying" shows whether the market moved toward the model's number soon after we bought — an early sign of real skill.*

## Active management vs holding

| Bets | Sold early | Take profit / cut loss | Hold-to-close P&L | Active P&L | Difference |
|---|---|---|---|---|---|
| 416 | 271 | 170 / 101 | -$39.92 | $70.20 | $110.12 |

*Same bets, two ways: held to the close, or re-priced every 2 seconds and sold whenever the bid (after fee) beat the model's value by 3¢+.*

## Versions head to head

*All four run side by side on the same markets, compared from when all of them were running (9/28 9:35 AM MT). 10 contracts per trade. From Sep 28 ~11:45 AM MT every buy is priced against Kalshi's live order book (earlier trades used the quoted price, which was often out of date).*

|  | What's different | Settled | Won | UP / DOWN | Trades per window | Worst window | P&L | Return |
|---|---|---|---|---|---|---|---|---|
| **V1** | Original (Coinbase price, 8¢ edge since Sep 29, was 4¢; no limit per window) | 1395 | 576 (41%) | 408 / 987 | 8.1 | -$43.45 | -$404.53 | -7% |
| **V2** | Trend-aware, wider swings, 50/50 with Kalshi's price | 1275 | 431 (34%) | 545 / 730 | 7.4 | -$55.90 | -$360.58 | -8% |
| **V3** | 5–10 min left only, 8¢+ edge, 3-exchange price, max 2 per window | 321 | 110 (34%) | 83 / 238 | 2.0 | -$14.97 | -$102.59 | -9% |
| **V4** | Limit orders 2¢ under the ask, 3-exchange price, max 2 per window · filled 78% of orders | 339 | 144 (42%) | 105 / 234 | 2.0 | -$13.69 | -$29.49 | -2% |
| **V5** | Trend Sniper: 6–12 min left, 25–55¢, 6¢+ edge, 1 bet per direction, take profit at 85¢ · *since it started* | 207 | 85 (41%) | 71 / 136 | 1.5 | -$10.05 | -$82.03 | -10% |
| **V6** | 60s Harvester: final minute, model 98%+ sure, buy 75–90¢ · *since it started* | 6 | 6 (100%) | 1 / 5 | 1.2 | $0.97 | $10.08 | +20% |
| **V7** | V5 signals through the risk-managed $500 account (2% bets, max 3 open, 25% peak stop) · *since it started* | 90 | 37 (41%) | 33 / 57 | 1.4 | -$20.08 | -$110.30 | -13% |
| **V8** | Trend Sniper on 1-hour markets: 20–45 min left, 25–55¢, 6¢+ edge · *since it started* | 49 | 16 (33%) | 18 / 31 | 1.5 | -$5.89 | -$17.84 | -10% |

*Model accuracy vs Kalshi's prices on the same 36,457 readings (excluding the final minute): V1 **+0.5%**, V2 **+1.2%**, 3-exchange price (V3/V4) **-0.6%**.*

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
| 1403 | 1275 (91%) | -$388.13 | -7% | 251,059 |

*Checked against Kalshi's order book at the moment of each buy. If profits hold on fillable trades only, the paper results are realistic.*

## Does the model beat the market?

**✅ Yes** — accuracy vs Kalshi's prices: **+4.0%** over 50,043 readings from 1971 windows (log-loss skill; positive = model better).

| Model said UP | Readings | Model avg | Kalshi price avg | Actually UP |
|---|---|---|---|---|
| 0–10% | 8592 | 3% | 4% | 5% |
| 10–20% | 3814 | 15% | 17% | 16% |
| 20–30% | 4191 | 25% | 26% | 27% |
| 30–40% | 4574 | 35% | 37% | 40% |
| 40–50% | 4930 | 45% | 48% | 52% |
| 50–60% | 4818 | 55% | 59% | 59% |
| 60–70% | 4230 | 65% | 71% | 73% |
| 70–80% | 3559 | 75% | 80% | 84% |
| 80–90% | 3338 | 85% | 88% | 89% |
| 90–100% | 7997 | 98% | 97% | 98% |

*A well-calibrated model's 'Actually UP' matches its own average in every row.*

![Calibration](fv/charts/calibration.png)

![Cumulative P&L](fv/charts/pnl.png)

## By edge size

| Edge at buy | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 4–6¢ | 711 | 338 (48%) | 45¢ | 52% | $66.37 | +2% |
| 6–10¢ | 667 | 301 (45%) | 43¢ | 52% | $73.94 | +3% |
| 10–20¢ | 396 | 154 (39%) | 40¢ | 54% | -$117.27 | -7% |
| 20¢+ | 23 | 9 (39%) | 40¢ | 67% | -$6.66 | -7% |

*If bigger claimed edges don't do better, the model is overconfident.*

## By time left

| Time left | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| 10–14 min | 1444 | 665 (46%) | 45¢ | 54% | -$47.40 | -1% |
| 5–10 min | 280 | 105 (38%) | 36¢ | 46% | $8.66 | +1% |
| 2–5 min | 64 | 27 (42%) | 33¢ | 45% | $50.86 | +23% |
| 1–2 min | 7 | 3 (43%) | 41¢ | 60% | $0.34 | +1% |
| Under 1 min | 2 | 2 (100%) | 79¢ | 100% | $3.92 | +24% |

## By price paid

| Price | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| Underdog (5–25¢) | 291 | 47 (16%) | 18¢ | 28% | -$84.86 | -15% |
| Toss-up (25–75¢) | 1372 | 637 (46%) | 45¢ | 54% | $33.22 | +1% |
| Favorite (75–95¢) | 134 | 118 (88%) | 82¢ | 90% | $68.02 | +6% |

## By coin

| Coin | Trades | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|
| BNB | 213 | 92 (43%) | 42¢ | 53% | -$11.80 | -1% |
| ETH | 208 | 94 (45%) | 45¢ | 55% | -$36.18 | -4% |
| HYPE | 204 | 87 (43%) | 43¢ | 53% | -$28.40 | -3% |
| BTC | 200 | 103 (52%) | 49¢ | 58% | $21.01 | +2% |
| XRP | 198 | 89 (45%) | 44¢ | 53% | -$8.15 | -1% |
| ZEC | 197 | 78 (40%) | 39¢ | 49% | -$21.09 | -3% |
| DOGE | 197 | 79 (40%) | 41¢ | 51% | -$55.22 | -7% |
| NEAR | 192 | 84 (44%) | 43¢ | 51% | -$6.53 | -1% |
| SOL | 188 | 96 (51%) | 41¢ | 50% | $162.74 | +20% |

## Latest trades

| When (MT) | Coin | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/30 7:23:20 AM | BTC | UP | 6.7 min | 29¢ | 40% | 10¢ | Open | — |
| 9/30 7:21:53 AM | SOL | UP | 8.1 min | 16¢ | 28% | 11¢ | Open | — |
| 9/30 7:21:38 AM | ETH | UP | 8.3 min | 14¢ | 28% | 13¢ | Open | — |
| 9/30 7:18:48 AM | NEAR | DOWN | 11.2 min | 19¢ | 28% | 8¢ | Open | — |
| 9/30 7:18:33 AM | BNB | UP | 11.4 min | 25¢ | 35% | 8¢ | Open | — |
| 9/30 7:18:13 AM | DOGE | DOWN | 11.8 min | 28¢ | 41% | 11¢ | Open | — |
| 9/30 7:17:09 AM | XRP | DOWN | 12.8 min | 26¢ | 36% | 9¢ | Open | — |
| 9/30 7:16:44 AM | HYPE | DOWN | 13.2 min | 47¢ | 62% | 13¢ | Open | — |
| 9/30 7:16:13 AM | ZEC | DOWN | 13.8 min | 45¢ | 55% | 8¢ | Open | — |
| 9/30 7:11:58 AM | DOGE | DOWN | 3.0 min | 7¢ | 19% | 11¢ | ❌ Lost | -$0.74 |
| 9/30 7:10:54 AM | NEAR | DOWN | 4.1 min | 21¢ | 33% | 11¢ | ❌ Lost | -$2.22 |
| 9/30 7:08:39 AM | ETH | UP | 6.3 min | 42¢ | 53% | 9¢ | ✅ Won | $5.62 |
| 9/30 7:04:05 AM | BNB | DOWN | 10.9 min | 51¢ | 61% | 8¢ | ❌ Lost | -$5.32 |
| 9/30 7:03:28 AM | ZEC | DOWN | 11.5 min | 50¢ | 65% | 13¢ | ❌ Lost | -$5.18 |
| 9/30 7:03:08 AM | XRP | UP | 11.9 min | 29¢ | 39% | 8¢ | ✅ Won | $6.95 |
| 9/30 7:03:01 AM | BTC | UP | 12.0 min | 26¢ | 35% | 8¢ | ✅ Won | $7.26 |
| 9/30 7:02:52 AM | HYPE | DOWN | 12.1 min | 56¢ | 71% | 13¢ | ❌ Lost | -$5.75 |
| 9/30 6:53:45 AM | XRP | DOWN | 6.2 min | 18¢ | 29% | 10¢ | ❌ Lost | -$1.91 |
| 9/30 6:49:22 AM | HYPE | DOWN | 10.6 min | 23¢ | 43% | 18¢ | ❌ Lost | -$2.47 |
| 9/30 6:49:22 AM | BTC | DOWN | 10.6 min | 15¢ | 28% | 13¢ | ❌ Lost | -$1.59 |
| 9/30 6:49:22 AM | ETH | DOWN | 10.6 min | 26¢ | 40% | 13¢ | ❌ Lost | -$2.74 |
| 9/30 6:48:48 AM | BNB | DOWN | 11.2 min | 35¢ | 49% | 12¢ | ❌ Lost | -$3.71 |
| 9/30 6:47:18 AM | NEAR | UP | 12.7 min | 19¢ | 31% | 11¢ | ❌ Lost | -$2.01 |
| 9/30 6:47:11 AM | DOGE | UP | 12.8 min | 32¢ | 46% | 12¢ | ❌ Lost | -$3.36 |
| 9/30 6:46:16 AM | ZEC | DOWN | 13.7 min | 29¢ | 41% | 10¢ | ❌ Lost | -$3.05 |

## How the model works

- **Fair chance of UP** = how likely the price is to finish at or above the target, assuming it moves randomly with the volatility of the last hour (weighted toward the last 15 minutes).
- **Final minute:** Kalshi settles on a 60-second average, so once that minute starts the bot averages its own price samples the same way and only models the part still to come.
- **Safety margins:** a small allowance for Coinbase vs Kalshi's index, a volatility floor, and no trades under 5¢ or over 95¢ where small model errors matter most.

## Raw data

- [fv/trades.csv](fv/trades.csv) — every paper trade
- `fv/obs/` — model vs market every 30 seconds for every market (shadow log)
- [fv/status.json](fv/status.json) — bot health
