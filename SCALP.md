# Range-Scalp Bot

*Updated Sat Oct 10 00:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9700 | 8374 | 1326 (18) | 0 | $-3255.90 | -5.3% |
| **+10¢** | 7327 | 5776 | 1551 (30) | 0 | $-3147.98 | -6.8% |
| **+15¢** | 6178 | 4543 | 1635 (43) | 1 | $-2606.14 | -6.7% |
| **+20¢** | 5493 | 3794 | 1699 (55) | 2 | $-2174.85 | -6.3% |
| **+10¢ (15¢ stop)** | 11873 | 11838 | 35 (22) | 0 | $-4561.25 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 00:26 | +10 stop | SOL | DOWN | 0.43 | 0.60 | 1.35 |
| 10-10 00:26 | +5 | SOL | DOWN | 0.43 | 0.60 | 1.35 |
| 10-10 00:26 | +10 stop | ETH | UP | 0.69 | 0.81 | 0.94 |
| 10-10 00:26 | +15 | ETH | UP | 0.69 | 0.87 | 1.57 |
| 10-10 00:26 | +10 | ETH | UP | 0.69 | 0.81 | 0.94 |
| 10-10 00:26 | +5 | ETH | UP | 0.69 | 0.81 | 0.94 |
| 10-10 00:26 | +10 stop | HYPE | UP | 0.64 | 0.79 | 1.21 |
| 10-10 00:26 | +15 | HYPE | UP | 0.64 | 0.79 | 1.21 |
| 10-10 00:26 | +10 | HYPE | UP | 0.64 | 0.79 | 1.21 |
| 10-10 00:26 | +5 | HYPE | UP | 0.63 | 0.79 | 1.31 |
| 10-10 00:25 | +10 stop | SOL | UP | 0.55 | 0.29 | -2.93 |
| 10-10 00:25 | +15 | SOL | UP | 0.55 | 0.75 | 1.68 |
| 10-10 00:25 | +5 | SOL | UP | 0.54 | 0.64 | 0.65 |
| 10-10 00:22 | +10 stop | BTC | DOWN | 0.61 | 0.73 | 0.89 |
| 10-10 00:21 | +10 stop | BTC | DOWN | 0.54 | 0.64 | 0.65 |
| 10-10 00:20 | +10 stop | SOL | UP | 0.65 | 0.75 | 0.70 |
| 10-10 00:20 | +20 | SOL | UP | 0.65 | 0.85 | 1.75 |
| 10-10 00:20 | +15 | SOL | UP | 0.65 | 0.83 | 1.54 |
| 10-10 00:20 | +5 | SOL | UP | 0.65 | 0.75 | 0.70 |
| 10-10 00:19 | +10 stop | BTC | DOWN | 0.67 | 0.51 | -1.94 |
| 10-10 00:19 | +10 | BTC | DOWN | 0.67 | 0.88 | 1.86 |
| 10-10 00:19 | +5 | BTC | DOWN | 0.67 | 0.73 | 0.30 |
| 10-10 00:19 | +10 stop | DOGE | DOWN | 0.41 | 0.55 | 1.05 |
| 10-10 00:19 | +15 | DOGE | DOWN | 0.42 | open |  |
| 10-10 00:19 | +10 stop | ZEC | DOWN | 0.48 | 0.30 | -2.13 |
| 10-10 00:19 | +10 | ZEC | DOWN | 0.48 | yes | -4.98 |
| 10-10 00:19 | +5 | ZEC | DOWN | 0.45 | yes | -4.66 |
| 10-10 00:19 | +10 stop | SOL | DOWN | 0.71 | 0.47 | -2.73 |
| 10-10 00:19 | +10 | SOL | DOWN | 0.71 | yes | -7.25 |
| 10-10 00:18 | +5 | HYPE | UP | 0.63 | 0.76 | 1.00 |
| 10-10 00:17 | +10 stop | DOGE | UP | 0.64 | 0.39 | -2.84 |
| 10-10 00:17 | +10 | DOGE | UP | 0.64 | 0.86 | 1.94 |
| 10-10 00:17 | +5 | DOGE | UP | 0.65 | 0.70 | 0.19 |
| 10-10 00:17 | +10 stop | BNB | UP | 0.64 | 0.49 | -1.85 |
| 10-10 00:17 | +10 | BNB | UP | 0.64 | 0.82 | 1.47 |
| 10-10 00:17 | +5 | BNB | UP | 0.64 | 0.82 | 1.52 |
| 10-10 00:16 | +5 | SOL | UP | 0.55 | 0.63 | 0.45 |
| 10-10 00:16 | +10 stop | ETH | UP | 0.68 | 0.48 | -2.34 |
| 10-10 00:16 | +15 | ETH | UP | 0.68 | 0.83 | 1.24 |
| 10-10 00:16 | +10 | ETH | UP | 0.68 | 0.78 | 0.71 |
