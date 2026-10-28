# Range-Scalp Bot

*Updated Wed Oct 28 23:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38658 | 33730 | 4928 (48) | 1 | $-10894.92 | -4.5% |
| **+10¢** | 28831 | 23140 | 5691 (70) | 1 | $-9668.80 | -5.3% |
| **+15¢** | 24118 | 18004 | 6114 (96) | 1 | $-8630.82 | -5.7% |
| **+20¢** | 21398 | 14996 | 6402 (124) | 1 | $-7530.20 | -5.6% |
| **+10¢ (15¢ stop)** | 47281 | 47214 | 67 (35) | 0 | $-17949.21 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 23:42 | +10 stop | BTC | UP | 0.71 | 0.81 | 0.74 |
| 10-28 23:42 | +10 stop | HYPE | DOWN | 0.66 | 0.76 | 0.71 |
| 10-28 23:42 | +20 | HYPE | DOWN | 0.66 | 0.90 | 2.18 |
| 10-28 23:42 | +15 | HYPE | DOWN | 0.66 | 0.90 | 2.14 |
| 10-28 23:42 | +10 | HYPE | DOWN | 0.66 | 0.76 | 0.71 |
| 10-28 23:42 | +5 | HYPE | DOWN | 0.66 | 0.76 | 0.71 |
| 10-28 23:40 | +10 stop | BNB | UP | 0.62 | 0.73 | 0.79 |
| 10-28 23:40 | +20 | BNB | UP | 0.62 | 0.88 | 2.35 |
| 10-28 23:40 | +15 | BNB | UP | 0.62 | 0.81 | 1.62 |
| 10-28 23:40 | +10 | BNB | UP | 0.62 | 0.73 | 0.79 |
| 10-28 23:40 | +5 | BNB | UP | 0.63 | 0.73 | 0.69 |
| 10-28 23:40 | +10 stop | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 10-28 23:40 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.42 |
| 10-28 23:40 | +10 stop | BTC | DOWN | 0.68 | 0.49 | -2.24 |
| 10-28 23:40 | +10 | BTC | DOWN | 0.68 | open |  |
| 10-28 23:40 | +5 | BTC | DOWN | 0.68 | open |  |
| 10-28 23:37 | +10 stop | HYPE | DOWN | 0.60 | 0.83 | 2.03 |
| 10-28 23:36 | +10 stop | DOGE | DOWN | 0.64 | 0.88 | 2.15 |
| 10-28 23:35 | +10 stop | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
| 10-28 23:35 | +10 stop | XRP | UP | 0.60 | 0.34 | -2.93 |
| 10-28 23:35 | +10 stop | BTC | UP | 0.62 | 0.47 | -1.85 |
| 10-28 23:34 | +10 stop | SOL | UP | 0.67 | 0.50 | -2.04 |
| 10-28 23:34 | +10 stop | DOGE | UP | 0.64 | 0.44 | -2.35 |
| 10-28 23:34 | +10 stop | HYPE | UP | 0.64 | 0.46 | -2.15 |
| 10-28 23:34 | +10 stop | ETH | UP | 0.67 | 0.51 | -1.94 |
| 10-28 23:33 | +10 stop | SOL | DOWN | 0.52 | 0.31 | -2.43 |
| 10-28 23:33 | +10 stop | XRP | DOWN | 0.61 | 0.46 | -1.89 |
| 10-28 23:33 | +10 | XRP | DOWN | 0.62 | 0.82 | 1.72 |
| 10-28 23:33 | +5 | XRP | DOWN | 0.62 | 0.82 | 1.72 |
| 10-28 23:33 | +10 stop | NEAR | DOWN | 0.69 | 0.50 | -2.23 |
| 10-28 23:33 | +20 | NEAR | DOWN | 0.69 | 0.91 | 2.03 |
| 10-28 23:33 | +15 | NEAR | DOWN | 0.69 | 0.91 | 2.03 |
| 10-28 23:33 | +10 | NEAR | DOWN | 0.69 | 0.91 | 2.03 |
| 10-28 23:33 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.21 |
| 10-28 23:32 | +10 stop | HYPE | DOWN | 0.69 | 0.48 | -2.42 |
| 10-28 23:32 | +10 | HYPE | DOWN | 0.69 | 0.83 | 1.16 |
| 10-28 23:32 | +5 | HYPE | DOWN | 0.69 | 0.83 | 1.16 |
| 10-28 23:32 | +10 stop | BNB | DOWN | 0.57 | 0.42 | -1.86 |
| 10-28 23:31 | +10 stop | SOL | DOWN | 0.68 | 0.53 | -1.84 |
| 10-28 23:31 | +20 | SOL | DOWN | 0.68 | 0.91 | 2.08 |
