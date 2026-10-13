# Range-Scalp Bot

*Updated Tue Oct 13 21:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15006 | 12978 | 2028 (27) | 3 | $-4876.43 | -5.2% |
| **+10¢** | 11351 | 8998 | 2353 (39) | 3 | $-4559.87 | -6.4% |
| **+15¢** | 9540 | 7022 | 2518 (58) | 3 | $-4052.48 | -6.8% |
| **+20¢** | 8485 | 5860 | 2625 (74) | 3 | $-3507.49 | -6.6% |
| **+10¢ (15¢ stop)** | 18415 | 18365 | 50 (29) | 0 | $-7145.94 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 21:36 | +10 stop | ZEC | UP | 0.67 | 0.82 | 1.23 |
| 10-13 21:36 | +15 | ZEC | UP | 0.67 | 0.82 | 1.23 |
| 10-13 21:36 | +10 | ZEC | UP | 0.67 | 0.82 | 1.23 |
| 10-13 21:36 | +5 | ZEC | UP | 0.67 | 0.73 | 0.30 |
| 10-13 21:35 | +10 stop | BNB | UP | 0.69 | 0.79 | 0.73 |
| 10-13 21:35 | +20 | BNB | UP | 0.69 | 0.96 | 2.50 |
| 10-13 21:35 | +15 | BNB | UP | 0.69 | 0.96 | 2.50 |
| 10-13 21:35 | +10 | BNB | UP | 0.69 | 0.79 | 0.73 |
| 10-13 21:35 | +5 | BNB | UP | 0.69 | 0.75 | 0.31 |
| 10-13 21:35 | +10 stop | SOL | UP | 0.67 | 0.81 | 1.13 |
| 10-13 21:32 | +10 stop | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 10-13 21:32 | +20 | ZEC | UP | 0.69 | 0.94 | 2.32 |
| 10-13 21:32 | +15 | ZEC | UP | 0.69 | 0.85 | 1.36 |
| 10-13 21:32 | +10 | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 10-13 21:32 | +5 | ZEC | UP | 0.69 | 0.77 | 0.52 |
| 10-13 21:31 | +10 stop | BTC | UP | 0.55 | 0.70 | 1.17 |
| 10-13 21:31 | +20 | BTC | UP | 0.55 | 0.76 | 1.79 |
| 10-13 21:31 | +15 | BTC | UP | 0.55 | 0.70 | 1.17 |
| 10-13 21:31 | +10 | BTC | UP | 0.55 | 0.70 | 1.17 |
| 10-13 21:31 | +5 | BTC | UP | 0.55 | 0.70 | 1.17 |
| 10-13 21:31 | +10 stop | XRP | UP | 0.69 | 0.82 | 1.04 |
| 10-13 21:31 | +20 | XRP | UP | 0.69 | 0.91 | 1.95 |
| 10-13 21:31 | +15 | XRP | UP | 0.69 | 0.86 | 1.46 |
| 10-13 21:31 | +10 | XRP | UP | 0.69 | 0.82 | 1.04 |
| 10-13 21:31 | +5 | XRP | UP | 0.69 | 0.77 | 0.52 |
| 10-13 21:31 | +10 stop | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 10-13 21:31 | +20 | DOGE | UP | 0.65 | 0.88 | 2.06 |
| 10-13 21:31 | +15 | DOGE | UP | 0.65 | 0.84 | 1.64 |
| 10-13 21:31 | +10 | DOGE | UP | 0.65 | 0.75 | 0.70 |
| 10-13 21:31 | +5 | DOGE | UP | 0.65 | 0.73 | 0.50 |
| 10-13 21:31 | +10 stop | ETH | DOWN | 0.55 | 0.26 | -3.22 |
| 10-13 21:31 | +20 | ETH | DOWN | 0.55 | open |  |
| 10-13 21:31 | +15 | ETH | DOWN | 0.55 | open |  |
| 10-13 21:31 | +10 | ETH | DOWN | 0.54 | open |  |
| 10-13 21:31 | +5 | ETH | DOWN | 0.54 | open |  |
| 10-13 21:31 | +10 stop | SOL | DOWN | 0.45 | 0.27 | -2.12 |
| 10-13 21:31 | +20 | SOL | DOWN | 0.45 | open |  |
| 10-13 21:31 | +15 | SOL | DOWN | 0.45 | open |  |
| 10-13 21:31 | +10 | SOL | DOWN | 0.45 | open |  |
| 10-13 21:31 | +5 | SOL | DOWN | 0.45 | open |  |
