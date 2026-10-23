# Range-Scalp Bot

*Updated Fri Oct 23 05:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29798 | 25940 | 3858 (39) | 0 | $-8778.20 | -4.7% |
| **+10¢** | 22337 | 17872 | 4465 (55) | 0 | $-7894.83 | -5.6% |
| **+15¢** | 18707 | 13913 | 4794 (78) | 0 | $-7056.29 | -6.0% |
| **+20¢** | 16559 | 11536 | 5023 (101) | 0 | $-6361.46 | -6.1% |
| **+10¢ (15¢ stop)** | 36574 | 36515 | 59 (32) | 0 | $-13782.48 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 05:06 | +10 stop | NEAR | UP | 0.68 | 0.80 | 0.92 |
| 10-23 05:06 | +20 | NEAR | UP | 0.68 | 0.94 | 2.37 |
| 10-23 05:06 | +15 | NEAR | UP | 0.68 | 0.84 | 1.34 |
| 10-23 05:06 | +10 | NEAR | UP | 0.68 | 0.80 | 0.92 |
| 10-23 05:06 | +5 | NEAR | UP | 0.68 | 0.80 | 0.92 |
| 10-23 05:05 | +5 | DOGE | UP | 0.67 | 0.82 | 1.23 |
| 10-23 05:05 | +10 stop | SOL | UP | 0.71 | 0.82 | 0.84 |
| 10-23 05:05 | +20 | SOL | UP | 0.71 | 0.93 | 2.01 |
| 10-23 05:05 | +15 | SOL | UP | 0.71 | 0.90 | 1.71 |
| 10-23 05:05 | +10 | SOL | UP | 0.71 | 0.82 | 0.84 |
| 10-23 05:05 | +5 | SOL | UP | 0.71 | 0.82 | 0.84 |
| 10-23 05:01 | +10 stop | DOGE | UP | 0.63 | 0.82 | 1.62 |
| 10-23 05:01 | +20 | DOGE | UP | 0.63 | 0.85 | 1.94 |
| 10-23 05:01 | +15 | DOGE | UP | 0.63 | 0.82 | 1.62 |
| 10-23 05:01 | +10 | DOGE | UP | 0.63 | 0.82 | 1.62 |
| 10-23 05:01 | +5 | DOGE | UP | 0.63 | 0.70 | 0.38 |
| 10-23 05:00 | +10 stop | XRP | UP | 0.70 | 0.80 | 0.73 |
| 10-23 05:00 | +20 | XRP | UP | 0.70 | 0.91 | 1.93 |
| 10-23 05:00 | +15 | XRP | UP | 0.70 | 0.91 | 1.93 |
| 10-23 05:00 | +10 | XRP | UP | 0.70 | 0.80 | 0.75 |
| 10-23 05:00 | +5 | XRP | UP | 0.70 | 0.79 | 0.65 |
| 10-23 04:57 | +10 stop | DOGE | UP | 0.17 | 0.57 | 3.72 |
| 10-23 04:57 | +10 stop | SOL | UP | 0.19 | 0.58 | 3.61 |
| 10-23 04:57 | +10 stop | HYPE | DOWN | 0.71 | 0.94 | 2.14 |
| 10-23 04:55 | +10 stop | HYPE | UP | 0.61 | 0.38 | -2.64 |
| 10-23 04:55 | +10 stop | DOGE | DOWN | 0.61 | 0.44 | -2.05 |
| 10-23 04:55 | +10 stop | SOL | DOWN | 0.54 | 0.37 | -2.00 |
| 10-23 04:55 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-23 04:55 | +10 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-23 04:54 | +10 stop | HYPE | UP | 0.49 | 0.65 | 1.26 |
| 10-23 04:54 | +10 stop | XRP | UP | 0.49 | 0.61 | 0.85 |
| 10-23 04:54 | +15 | XRP | UP | 0.49 | no | -5.08 |
| 10-23 04:54 | +10 | XRP | UP | 0.49 | 0.61 | 0.85 |
| 10-23 04:54 | +10 stop | DOGE | UP | 0.55 | 0.67 | 0.86 |
| 10-23 04:52 | +10 stop | HYPE | UP | 0.51 | 0.62 | 0.71 |
| 10-23 04:52 | +10 stop | DOGE | DOWN | 0.60 | 0.31 | -3.22 |
| 10-23 04:52 | +10 | DOGE | DOWN | 0.60 | 0.81 | 1.82 |
| 10-23 04:52 | +5 | DOGE | DOWN | 0.60 | 0.81 | 1.82 |
| 10-23 04:51 | +10 stop | SOL | DOWN | 0.48 | 0.25 | -2.62 |
| 10-23 04:51 | +10 | SOL | DOWN | 0.48 | 0.81 | 3.01 |
