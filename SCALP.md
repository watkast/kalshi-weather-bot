# Range-Scalp Bot

*Updated Sun Oct 11 21:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12532 | 10817 | 1715 (25) | 2 | $-4140.86 | -5.2% |
| **+10¢** | 9510 | 7523 | 1987 (37) | 3 | $-3896.61 | -6.5% |
| **+15¢** | 8008 | 5895 | 2113 (55) | 4 | $-3343.46 | -6.6% |
| **+20¢** | 7138 | 4936 | 2202 (69) | 6 | $-2833.69 | -6.3% |
| **+10¢ (15¢ stop)** | 15435 | 15394 | 41 (25) | 0 | $-6046.92 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 21:34 | +10 stop | BNB | UP | 0.70 | 0.81 | 0.84 |
| 10-11 21:33 | +10 stop | ZEC | UP | 0.69 | 0.82 | 1.05 |
| 10-11 21:33 | +20 | ZEC | UP | 0.69 | 0.90 | 1.92 |
| 10-11 21:33 | +15 | ZEC | UP | 0.69 | 0.90 | 1.92 |
| 10-11 21:33 | +10 | ZEC | UP | 0.69 | 0.82 | 1.05 |
| 10-11 21:33 | +5 | ZEC | UP | 0.69 | 0.76 | 0.43 |
| 10-11 21:33 | +5 | HYPE | UP | 0.68 | 0.74 | 0.30 |
| 10-11 21:32 | +10 stop | XRP | UP | 0.70 | 0.81 | 0.84 |
| 10-11 21:32 | +5 | XRP | UP | 0.70 | 0.81 | 0.84 |
| 10-11 21:32 | +10 stop | SOL | UP | 0.67 | 0.82 | 1.23 |
| 10-11 21:32 | +20 | SOL | UP | 0.67 | open |  |
| 10-11 21:32 | +15 | SOL | UP | 0.67 | 0.82 | 1.23 |
| 10-11 21:32 | +10 | SOL | UP | 0.67 | 0.82 | 1.23 |
| 10-11 21:32 | +5 | SOL | UP | 0.67 | 0.73 | 0.30 |
| 10-11 21:32 | +10 stop | DOGE | UP | 0.63 | 0.75 | 0.89 |
| 10-11 21:32 | +20 | DOGE | UP | 0.63 | open |  |
| 10-11 21:32 | +15 | DOGE | UP | 0.64 | 0.79 | 1.21 |
| 10-11 21:32 | +10 | DOGE | UP | 0.64 | 0.75 | 0.79 |
| 10-11 21:32 | +5 | DOGE | UP | 0.64 | 0.75 | 0.79 |
| 10-11 21:31 | +10 stop | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 10-11 21:31 | +20 | HYPE | UP | 0.67 | open |  |
| 10-11 21:31 | +15 | HYPE | UP | 0.67 | open |  |
| 10-11 21:31 | +10 | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 10-11 21:31 | +5 | HYPE | UP | 0.67 | 0.74 | 0.40 |
| 10-11 21:31 | +10 stop | BTC | UP | 0.60 | 0.71 | 0.78 |
| 10-11 21:31 | +20 | BTC | UP | 0.60 | 0.82 | 1.92 |
| 10-11 21:31 | +15 | BTC | UP | 0.60 | 0.77 | 1.40 |
| 10-11 21:31 | +10 | BTC | UP | 0.60 | 0.71 | 0.78 |
| 10-11 21:31 | +5 | BTC | UP | 0.60 | 0.68 | 0.47 |
| 10-11 21:31 | +5 | XRP | UP | 0.61 | 0.67 | 0.27 |
| 10-11 21:31 | +10 stop | BNB | DOWN | 0.55 | 0.35 | -2.34 |
| 10-11 21:31 | +20 | BNB | DOWN | 0.55 | open |  |
| 10-11 21:31 | +15 | BNB | DOWN | 0.55 | open |  |
| 10-11 21:31 | +10 | BNB | DOWN | 0.56 | open |  |
| 10-11 21:31 | +5 | BNB | DOWN | 0.56 | open |  |
| 10-11 21:31 | +10 stop | XRP | DOWN | 0.47 | 0.32 | -1.84 |
| 10-11 21:31 | +20 | XRP | DOWN | 0.47 | open |  |
| 10-11 21:31 | +15 | XRP | DOWN | 0.47 | open |  |
| 10-11 21:31 | +10 | XRP | DOWN | 0.47 | open |  |
| 10-11 21:31 | +5 | XRP | DOWN | 0.47 | 0.54 | 0.34 |
