# Range-Scalp Bot

*Updated Sun Oct 11 21:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12549 | 10832 | 1717 (25) | 3 | $-4144.21 | -5.2% |
| **+10¢** | 9523 | 7533 | 1990 (37) | 3 | $-3901.87 | -6.5% |
| **+15¢** | 8018 | 5902 | 2116 (55) | 4 | $-3348.81 | -6.7% |
| **+20¢** | 7146 | 4941 | 2205 (69) | 6 | $-2839.62 | -6.3% |
| **+10¢ (15¢ stop)** | 15456 | 15415 | 41 (25) | 1 | $-6061.46 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 21:56 | +10 stop | SOL | UP | 0.69 | open |  |
| 10-11 21:56 | +5 | SOL | UP | 0.69 | open |  |
| 10-11 21:55 | +10 stop | XRP | DOWN | 0.47 | 0.57 | 0.64 |
| 10-11 21:55 | +10 stop | BTC | UP | 0.56 | 0.41 | -1.85 |
| 10-11 21:54 | +10 stop | DOGE | UP | 0.69 | 0.43 | -2.93 |
| 10-11 21:54 | +5 | DOGE | UP | 0.58 | 0.68 | 0.66 |
| 10-11 21:53 | +5 | DOGE | DOWN | 0.46 | 0.55 | 0.54 |
| 10-11 21:53 | +10 stop | XRP | UP | 0.66 | 0.77 | 0.81 |
| 10-11 21:52 | +10 stop | DOGE | DOWN | 0.56 | 0.40 | -1.95 |
| 10-11 21:52 | +15 | DOGE | DOWN | 0.56 | 0.76 | 1.69 |
| 10-11 21:52 | +10 | DOGE | DOWN | 0.56 | 0.76 | 1.69 |
| 10-11 21:52 | +5 | DOGE | DOWN | 0.56 | 0.61 | 0.15 |
| 10-11 21:52 | +10 stop | SOL | DOWN | 0.50 | 0.28 | -2.53 |
| 10-11 21:52 | +10 | SOL | DOWN | 0.50 | open |  |
| 10-11 21:52 | +5 | SOL | DOWN | 0.50 | 0.59 | 0.55 |
| 10-11 21:52 | +10 stop | NEAR | UP | 0.63 | 0.79 | 1.32 |
| 10-11 21:52 | +10 stop | BNB | DOWN | 0.51 | 0.30 | -2.43 |
| 10-11 21:52 | +20 | BNB | DOWN | 0.51 | 0.76 | 2.19 |
| 10-11 21:52 | +15 | BNB | DOWN | 0.51 | 0.76 | 2.19 |
| 10-11 21:52 | +10 | BNB | DOWN | 0.51 | 0.76 | 2.19 |
| 10-11 21:52 | +5 | BNB | DOWN | 0.51 | 0.76 | 2.19 |
| 10-11 21:51 | +5 | XRP | DOWN | 0.63 | open |  |
| 10-11 21:51 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 10-11 21:51 | +20 | ETH | DOWN | 0.65 | open |  |
| 10-11 21:51 | +15 | ETH | DOWN | 0.65 | open |  |
| 10-11 21:51 | +10 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 10-11 21:51 | +5 | ETH | DOWN | 0.65 | 0.74 | 0.60 |
| 10-11 21:51 | +10 stop | NEAR | UP | 0.63 | 0.44 | -2.24 |
| 10-11 21:50 | +10 stop | XRP | DOWN | 0.62 | 0.33 | -3.23 |
| 10-11 21:50 | +10 | XRP | DOWN | 0.62 | open |  |
| 10-11 21:50 | +10 stop | BTC | DOWN | 0.71 | 0.55 | -1.93 |
| 10-11 21:50 | +20 | BTC | DOWN | 0.71 | open |  |
| 10-11 21:50 | +15 | BTC | DOWN | 0.71 | open |  |
| 10-11 21:50 | +10 | BTC | DOWN | 0.71 | open |  |
| 10-11 21:50 | +5 | BTC | DOWN | 0.71 | open |  |
| 10-11 21:49 | +5 | XRP | DOWN | 0.66 | 0.71 | 0.19 |
| 10-11 21:49 | +10 stop | NEAR | DOWN | 0.58 | 0.39 | -2.25 |
| 10-11 21:47 | +5 | HYPE | DOWN | 0.68 | 0.73 | 0.23 |
| 10-11 21:47 | +10 stop | NEAR | UP | 0.68 | 0.47 | -2.45 |
| 10-11 21:47 | +20 | NEAR | UP | 0.68 | 0.89 | 1.86 |
