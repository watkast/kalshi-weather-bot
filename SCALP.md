# Range-Scalp Bot

*Updated Sat Oct 17 07:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20612 | 17929 | 2683 (29) | 1 | $-6092.66 | -4.7% |
| **+10¢** | 15530 | 12438 | 3092 (41) | 1 | $-5400.47 | -5.5% |
| **+15¢** | 12987 | 9661 | 3326 (60) | 1 | $-4872.90 | -6.0% |
| **+20¢** | 11510 | 8025 | 3485 (79) | 1 | $-4324.66 | -6.0% |
| **+10¢ (15¢ stop)** | 25328 | 25278 | 50 (29) | 0 | $-9566.66 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 07:36 | +10 stop | BNB | UP | 0.55 | 0.72 | 1.37 |
| 10-17 07:35 | +10 stop | BNB | DOWN | 0.63 | 0.47 | -1.95 |
| 10-17 07:35 | +20 | BNB | DOWN | 0.63 | open |  |
| 10-17 07:35 | +15 | BNB | DOWN | 0.63 | open |  |
| 10-17 07:35 | +10 | BNB | DOWN | 0.63 | open |  |
| 10-17 07:35 | +5 | BNB | DOWN | 0.63 | open |  |
| 10-17 07:34 | +10 stop | ETH | UP | 0.66 | 0.79 | 1.02 |
| 10-17 07:34 | +20 | ETH | UP | 0.66 | 0.86 | 1.75 |
| 10-17 07:34 | +15 | ETH | UP | 0.66 | 0.85 | 1.65 |
| 10-17 07:34 | +10 | ETH | UP | 0.66 | 0.79 | 1.02 |
| 10-17 07:34 | +5 | ETH | UP | 0.66 | 0.71 | 0.19 |
| 10-17 07:28 | +5 | BTC | DOWN | 0.53 | 0.62 | 0.55 |
| 10-17 07:27 | +10 stop | BTC | DOWN | 0.64 | 0.49 | -1.85 |
| 10-17 07:27 | +20 | BTC | DOWN | 0.64 | yes | -6.57 |
| 10-17 07:27 | +15 | BTC | DOWN | 0.64 | yes | -6.57 |
| 10-17 07:27 | +10 | BTC | DOWN | 0.64 | yes | -6.57 |
| 10-17 07:27 | +5 | BTC | DOWN | 0.64 | 0.70 | 0.28 |
| 10-17 07:26 | +10 stop | ETH | DOWN | 0.67 | 0.33 | -3.72 |
| 10-17 07:26 | +15 | ETH | DOWN | 0.67 | yes | -6.86 |
| 10-17 07:26 | +10 | ETH | DOWN | 0.66 | yes | -6.80 |
| 10-17 07:25 | +10 stop | DOGE | DOWN | 0.68 | 0.07 | -6.36 |
| 10-17 07:25 | +20 | DOGE | DOWN | 0.68 | yes | -6.96 |
| 10-17 07:25 | +15 | DOGE | DOWN | 0.68 | yes | -7.00 |
| 10-17 07:25 | +10 | DOGE | DOWN | 0.69 | yes | -7.05 |
| 10-17 07:25 | +5 | SOL | UP | 0.68 | 0.82 | 1.13 |
| 10-17 07:25 | +10 stop | ETH | DOWN | 0.55 | 0.67 | 0.86 |
| 10-17 07:25 | +10 | ETH | DOWN | 0.55 | 0.67 | 0.86 |
| 10-17 07:24 | +5 | SOL | UP | 0.52 | 0.60 | 0.45 |
| 10-17 07:24 | +10 stop | DOGE | UP | 0.38 | 0.59 | 1.81 |
| 10-17 07:24 | +5 | DOGE | UP | 0.62 | 0.93 | 2.92 |
| 10-17 07:23 | +10 stop | SOL | UP | 0.55 | 0.67 | 0.86 |
| 10-17 07:23 | +15 | SOL | UP | 0.55 | 0.72 | 1.37 |
| 10-17 07:23 | +10 | SOL | UP | 0.55 | 0.67 | 0.86 |
| 10-17 07:23 | +5 | SOL | UP | 0.55 | 0.63 | 0.45 |
| 10-17 07:23 | +10 stop | DOGE | UP | 0.50 | 0.61 | 0.75 |
| 10-17 07:23 | +5 | DOGE | UP | 0.50 | 0.57 | 0.34 |
| 10-17 07:23 | +10 stop | ETH | UP | 0.55 | 0.39 | -1.95 |
| 10-17 07:23 | +5 | ETH | UP | 0.55 | 0.66 | 0.76 |
| 10-17 07:22 | +10 stop | XRP | UP | 0.46 | 0.56 | 0.64 |
| 10-17 07:22 | +10 stop | BTC | DOWN | 0.54 | 0.64 | 0.65 |
