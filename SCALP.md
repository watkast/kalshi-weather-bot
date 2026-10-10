# Range-Scalp Bot

*Updated Sat Oct 10 03:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9895 | 8541 | 1354 (18) | 2 | $-3330.39 | -5.3% |
| **+10¢** | 7475 | 5895 | 1580 (30) | 2 | $-3200.81 | -6.8% |
| **+15¢** | 6309 | 4643 | 1666 (43) | 2 | $-2644.81 | -6.7% |
| **+20¢** | 5606 | 3875 | 1731 (55) | 3 | $-2215.17 | -6.3% |
| **+10¢ (15¢ stop)** | 12152 | 12117 | 35 (22) | 0 | $-4745.75 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 03:28 | +10 stop | HYPE | UP | 0.64 | 0.76 | 0.90 |
| 10-10 03:28 | +20 | HYPE | UP | 0.64 | 0.94 | 2.76 |
| 10-10 03:28 | +15 | HYPE | UP | 0.64 | 0.94 | 2.76 |
| 10-10 03:28 | +10 | HYPE | UP | 0.64 | 0.76 | 0.90 |
| 10-10 03:28 | +5 | HYPE | UP | 0.64 | 0.76 | 0.90 |
| 10-10 03:27 | +10 stop | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-10 03:26 | +10 stop | BTC | UP | 0.55 | 0.68 | 0.96 |
| 10-10 03:26 | +15 | BTC | UP | 0.55 | 0.70 | 1.17 |
| 10-10 03:26 | +10 | BTC | UP | 0.55 | 0.68 | 0.96 |
| 10-10 03:26 | +5 | BTC | UP | 0.55 | 0.64 | 0.55 |
| 10-10 03:25 | +5 | BTC | UP | 0.68 | 0.73 | 0.20 |
| 10-10 03:25 | +10 stop | HYPE | UP | 0.70 | 0.81 | 0.84 |
| 10-10 03:24 | +10 stop | BTC | DOWN | 0.48 | 0.26 | -2.52 |
| 10-10 03:24 | +10 stop | DOGE | DOWN | 0.56 | 0.67 | 0.76 |
| 10-10 03:22 | +5 | DOGE | UP | 0.52 | open |  |
| 10-10 03:22 | +5 | HYPE | UP | 0.58 | 0.67 | 0.56 |
| 10-10 03:21 | +10 stop | DOGE | UP | 0.63 | 0.48 | -1.85 |
| 10-10 03:21 | +15 | DOGE | UP | 0.63 | open |  |
| 10-10 03:21 | +10 | DOGE | UP | 0.63 | open |  |
| 10-10 03:21 | +5 | DOGE | UP | 0.63 | 0.69 | 0.28 |
| 10-10 03:21 | +5 | ETH | DOWN | 0.69 | 0.77 | 0.52 |
| 10-10 03:21 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-10 03:21 | +10 stop | HYPE | UP | 0.58 | 0.40 | -2.13 |
| 10-10 03:21 | +20 | HYPE | UP | 0.58 | 0.81 | 2.03 |
| 10-10 03:21 | +15 | HYPE | UP | 0.57 | 0.73 | 1.28 |
| 10-10 03:21 | +10 | HYPE | UP | 0.57 | 0.67 | 0.66 |
| 10-10 03:21 | +5 | HYPE | UP | 0.57 | 0.62 | 0.15 |
| 10-10 03:20 | +10 stop | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 10-10 03:20 | +10 stop | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 10-10 03:20 | +15 | ETH | DOWN | 0.64 | 0.87 | 2.05 |
| 10-10 03:20 | +5 | NEAR | DOWN | 0.58 | 0.63 | 0.15 |
| 10-10 03:19 | +5 | BTC | UP | 0.57 | 0.62 | 0.15 |
| 10-10 03:19 | +10 stop | XRP | DOWN | 0.70 | 0.84 | 1.15 |
| 10-10 03:19 | +20 | XRP | DOWN | 0.70 | 0.91 | 1.93 |
| 10-10 03:19 | +15 | XRP | DOWN | 0.70 | 0.87 | 1.47 |
| 10-10 03:19 | +10 | XRP | DOWN | 0.70 | 0.84 | 1.15 |
| 10-10 03:19 | +5 | XRP | DOWN | 0.70 | 0.79 | 0.63 |
| 10-10 03:19 | +10 stop | NEAR | DOWN | 0.54 | 0.66 | 0.86 |
| 10-10 03:19 | +20 | NEAR | DOWN | 0.54 | 0.74 | 1.68 |
| 10-10 03:19 | +15 | NEAR | DOWN | 0.54 | 0.70 | 1.27 |
