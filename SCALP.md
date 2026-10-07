# Range-Scalp Bot

*Updated Wed Oct 07 06:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6074 | 5268 | 806 (9) | 3 | $-1849.38 | -4.8% |
| **+10¢** | 4629 | 3683 | 946 (16) | 4 | $-1724.50 | -5.9% |
| **+15¢** | 3889 | 2888 | 1001 (20) | 4 | $-1471.36 | -6.0% |
| **+20¢** | 3475 | 2429 | 1046 (27) | 4 | $-1208.65 | -5.5% |
| **+10¢ (15¢ stop)** | 7368 | 7353 | 15 (9) | 2 | $-2525.66 | -5.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 06:27 | +5 | XRP | DOWN | 0.23 | 0.59 | 3.33 |
| 10-07 06:26 | +10 stop | XRP | DOWN | 0.24 | 0.59 | 3.20 |
| 10-07 06:26 | +5 | DOGE | DOWN | 0.63 | open |  |
| 10-07 06:26 | +10 stop | SOL | DOWN | 0.69 | open |  |
| 10-07 06:26 | +10 stop | HYPE | DOWN | 0.32 | 0.60 | 2.47 |
| 10-07 06:25 | +10 stop | XRP | UP | 0.63 | 0.47 | -1.95 |
| 10-07 06:25 | +10 stop | DOGE | DOWN | 0.66 | open |  |
| 10-07 06:25 | +20 | DOGE | DOWN | 0.66 | open |  |
| 10-07 06:25 | +15 | DOGE | DOWN | 0.66 | open |  |
| 10-07 06:25 | +10 | DOGE | DOWN | 0.66 | open |  |
| 10-07 06:25 | +5 | DOGE | DOWN | 0.66 | 0.71 | 0.22 |
| 10-07 06:24 | +10 | HYPE | UP | 0.63 | 0.74 | 0.79 |
| 10-07 06:24 | +5 | HYPE | UP | 0.63 | 0.72 | 0.58 |
| 10-07 06:24 | +10 stop | HYPE | UP | 0.63 | 0.46 | -2.05 |
| 10-07 06:24 | +10 stop | XRP | DOWN | 0.52 | 0.37 | -1.85 |
| 10-07 06:24 | +20 | XRP | DOWN | 0.52 | open |  |
| 10-07 06:24 | +15 | XRP | DOWN | 0.52 | open |  |
| 10-07 06:24 | +10 | XRP | DOWN | 0.52 | open |  |
| 10-07 06:24 | +5 | XRP | DOWN | 0.53 | 0.58 | 0.14 |
| 10-07 06:24 | +10 stop | SOL | UP | 0.58 | 0.68 | 0.66 |
| 10-07 06:22 | +10 stop | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-07 06:22 | +20 | DOGE | DOWN | 0.66 | 0.86 | 1.75 |
| 10-07 06:22 | +15 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-07 06:22 | +10 | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-07 06:22 | +5 | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-07 06:22 | +10 stop | SOL | DOWN | 0.59 | 0.81 | 1.92 |
| 10-07 06:20 | +10 stop | NEAR | UP | 0.68 | 0.84 | 1.34 |
| 10-07 06:20 | +10 | NEAR | UP | 0.68 | 0.84 | 1.34 |
| 10-07 06:20 | +5 | NEAR | UP | 0.68 | 0.73 | 0.20 |
| 10-07 06:19 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-07 06:19 | +5 | ZEC | UP | 0.60 | 0.68 | 0.47 |
| 10-07 06:18 | +10 stop | SOL | DOWN | 0.52 | 0.66 | 1.06 |
| 10-07 06:18 | +10 stop | NEAR | UP | 0.63 | 0.74 | 0.79 |
| 10-07 06:18 | +20 | NEAR | UP | 0.62 | 0.84 | 1.93 |
| 10-07 06:18 | +15 | NEAR | UP | 0.61 | 0.84 | 1.98 |
| 10-07 06:18 | +10 | NEAR | UP | 0.61 | 0.74 | 0.94 |
| 10-07 06:18 | +5 | NEAR | UP | 0.61 | 0.74 | 0.94 |
| 10-07 06:17 | +5 | DOGE | DOWN | 0.67 | 0.72 | 0.19 |
| 10-07 06:17 | +10 stop | ZEC | UP | 0.56 | 0.68 | 0.86 |
| 10-07 06:17 | +20 | ZEC | UP | 0.56 | 0.78 | 1.89 |
