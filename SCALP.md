# Range-Scalp Bot

*Updated Sat Oct 10 04:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9931 | 8573 | 1358 (18) | 2 | $-3333.46 | -5.3% |
| **+10¢** | 7504 | 5920 | 1584 (30) | 2 | $-3204.08 | -6.8% |
| **+15¢** | 6334 | 4663 | 1671 (43) | 2 | $-2645.44 | -6.7% |
| **+20¢** | 5628 | 3892 | 1736 (55) | 2 | $-2209.67 | -6.3% |
| **+10¢ (15¢ stop)** | 12198 | 12163 | 35 (22) | 0 | $-4775.19 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 03:57 | +10 stop | SOL | UP | 0.68 | 0.21 | -4.98 |
| 10-10 03:55 | +10 stop | SOL | UP | 0.61 | 0.37 | -2.74 |
| 10-10 03:54 | +10 stop | NEAR | UP | 0.63 | 0.85 | 1.94 |
| 10-10 03:52 | +10 | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 10-10 03:52 | +10 stop | BTC | UP | 0.71 | 0.81 | 0.74 |
| 10-10 03:52 | +20 | BTC | UP | 0.71 | 0.92 | 1.91 |
| 10-10 03:52 | +15 | BTC | UP | 0.71 | 0.86 | 1.26 |
| 10-10 03:52 | +10 | BTC | UP | 0.71 | 0.81 | 0.74 |
| 10-10 03:52 | +5 | BTC | UP | 0.71 | 0.76 | 0.22 |
| 10-10 03:52 | +10 stop | SOL | DOWN | 0.63 | 0.48 | -1.85 |
| 10-10 03:52 | +10 stop | NEAR | DOWN | 0.62 | 0.45 | -2.10 |
| 10-10 03:52 | +10 stop | ETH | DOWN | 0.59 | 0.36 | -2.64 |
| 10-10 03:51 | +10 stop | HYPE | DOWN | 0.67 | 0.79 | 0.88 |
| 10-10 03:50 | +5 | DOGE | DOWN | 0.59 | 0.66 | 0.40 |
| 10-10 03:50 | +10 stop | BNB | UP | 0.58 | 0.75 | 1.38 |
| 10-10 03:50 | +10 stop | SOL | UP | 0.61 | 0.35 | -2.93 |
| 10-10 03:50 | +10 stop | ETH | UP | 0.65 | 0.46 | -2.24 |
| 10-10 03:50 | +20 | ETH | UP | 0.65 | 0.87 | 1.96 |
| 10-10 03:50 | +15 | ETH | UP | 0.65 | 0.87 | 1.96 |
| 10-10 03:50 | +10 | ETH | UP | 0.65 | 0.75 | 0.70 |
| 10-10 03:50 | +5 | ETH | UP | 0.65 | 0.75 | 0.70 |
| 10-10 03:50 | +10 stop | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 10-10 03:50 | +20 | DOGE | DOWN | 0.56 | 0.79 | 2.00 |
| 10-10 03:50 | +15 | DOGE | DOWN | 0.56 | 0.79 | 2.00 |
| 10-10 03:50 | +10 | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 10-10 03:50 | +5 | DOGE | DOWN | 0.55 | 0.60 | 0.15 |
| 10-10 03:50 | +5 | NEAR | UP | 0.59 | 0.85 | 2.34 |
| 10-10 03:50 | +15 | HYPE | UP | 0.60 | open |  |
| 10-10 03:50 | +10 | HYPE | UP | 0.60 | open |  |
| 10-10 03:50 | +5 | HYPE | UP | 0.60 | open |  |
| 10-10 03:48 | +10 stop | SOL | UP | 0.71 | 0.51 | -2.33 |
| 10-10 03:48 | +20 | SOL | UP | 0.71 | open |  |
| 10-10 03:48 | +15 | SOL | UP | 0.71 | open |  |
| 10-10 03:48 | +10 | SOL | UP | 0.71 | open |  |
| 10-10 03:48 | +5 | SOL | UP | 0.71 | open |  |
| 10-10 03:47 | +10 stop | HYPE | UP | 0.69 | 0.52 | -2.03 |
| 10-10 03:47 | +5 | HYPE | UP | 0.69 | 0.74 | 0.21 |
| 10-10 03:47 | +5 | NEAR | UP | 0.64 | 0.71 | 0.38 |
| 10-10 03:46 | +10 stop | NEAR | UP | 0.65 | 0.44 | -2.40 |
| 10-10 03:46 | +10 stop | BNB | UP | 0.70 | 0.52 | -2.17 |
