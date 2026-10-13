# Range-Scalp Bot

*Updated Tue Oct 13 19:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14864 | 12862 | 2002 (27) | 3 | $-4773.19 | -5.1% |
| **+10¢** | 11250 | 8927 | 2323 (39) | 3 | $-4444.76 | -6.3% |
| **+15¢** | 9454 | 6969 | 2485 (57) | 3 | $-3939.16 | -6.6% |
| **+20¢** | 8412 | 5821 | 2591 (73) | 3 | $-3390.99 | -6.4% |
| **+10¢ (15¢ stop)** | 18240 | 18190 | 50 (29) | 1 | $-7070.52 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 19:39 | +10 stop | XRP | DOWN | 0.70 | open |  |
| 10-13 19:39 | +10 | XRP | DOWN | 0.70 | open |  |
| 10-13 19:39 | +5 | XRP | DOWN | 0.70 | open |  |
| 10-13 19:39 | +10 stop | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-13 19:37 | +5 | NEAR | DOWN | 0.71 | 0.80 | 0.63 |
| 10-13 19:37 | +10 stop | BTC | DOWN | 0.49 | 0.61 | 0.85 |
| 10-13 19:37 | +10 stop | BNB | DOWN | 0.45 | 0.56 | 0.74 |
| 10-13 19:36 | +10 stop | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 10-13 19:36 | +5 | ETH | DOWN | 0.70 | 0.77 | 0.42 |
| 10-13 19:36 | +10 stop | BTC | UP | 0.56 | 0.35 | -2.44 |
| 10-13 19:36 | +15 | BTC | UP | 0.56 | open |  |
| 10-13 19:36 | +10 | BTC | UP | 0.56 | open |  |
| 10-13 19:36 | +5 | BTC | UP | 0.56 | open |  |
| 10-13 19:34 | +5 | BNB | UP | 0.66 | open |  |
| 10-13 19:34 | +10 stop | HYPE | UP | 0.60 | 0.40 | -2.34 |
| 10-13 19:34 | +10 stop | NEAR | UP | 0.56 | 0.38 | -2.15 |
| 10-13 19:34 | +10 stop | SOL | DOWN | 0.58 | 0.75 | 1.38 |
| 10-13 19:34 | +20 | SOL | DOWN | 0.58 | 0.84 | 2.32 |
| 10-13 19:34 | +15 | SOL | DOWN | 0.58 | 0.75 | 1.38 |
| 10-13 19:34 | +10 | SOL | DOWN | 0.58 | 0.75 | 1.38 |
| 10-13 19:34 | +5 | SOL | DOWN | 0.58 | 0.64 | 0.25 |
| 10-13 19:33 | +10 stop | XRP | DOWN | 0.52 | 0.73 | 1.78 |
| 10-13 19:33 | +10 stop | BNB | UP | 0.58 | 0.38 | -2.32 |
| 10-13 19:33 | +10 | BNB | UP | 0.57 | open |  |
| 10-13 19:33 | +10 stop | BTC | UP | 0.58 | 0.70 | 0.91 |
| 10-13 19:33 | +20 | BTC | UP | 0.56 | open |  |
| 10-13 19:33 | +15 | BTC | UP | 0.56 | 0.72 | 1.27 |
| 10-13 19:33 | +10 | BTC | UP | 0.56 | 0.70 | 1.07 |
| 10-13 19:33 | +5 | BTC | UP | 0.56 | 0.62 | 0.25 |
| 10-13 19:33 | +5 | BNB | UP | 0.54 | 0.65 | 0.76 |
| 10-13 19:32 | +10 stop | NEAR | DOWN | 0.57 | 0.41 | -1.96 |
| 10-13 19:32 | +20 | NEAR | DOWN | 0.57 | 0.80 | 1.99 |
| 10-13 19:32 | +15 | NEAR | DOWN | 0.57 | 0.80 | 1.99 |
| 10-13 19:32 | +10 | NEAR | DOWN | 0.57 | 0.69 | 0.86 |
| 10-13 19:32 | +5 | NEAR | DOWN | 0.57 | 0.63 | 0.24 |
| 10-13 19:31 | +10 stop | HYPE | DOWN | 0.59 | 0.43 | -1.95 |
| 10-13 19:31 | +20 | HYPE | DOWN | 0.59 | 0.81 | 1.92 |
| 10-13 19:31 | +15 | HYPE | DOWN | 0.59 | 0.75 | 1.29 |
| 10-13 19:31 | +10 | HYPE | DOWN | 0.59 | 0.73 | 1.09 |
| 10-13 19:31 | +5 | HYPE | DOWN | 0.59 | 0.65 | 0.27 |
