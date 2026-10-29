# Range-Scalp Bot

*Updated Thu Oct 29 16:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39464 | 34454 | 5010 (50) | 2 | $-10951.57 | -4.4% |
| **+10¢** | 29419 | 23629 | 5790 (73) | 1 | $-9694.32 | -5.2% |
| **+15¢** | 24602 | 18380 | 6222 (100) | 1 | $-8651.09 | -5.6% |
| **+20¢** | 21831 | 15313 | 6518 (129) | 1 | $-7524.30 | -5.5% |
| **+10¢ (15¢ stop)** | 48203 | 48133 | 70 (37) | 0 | $-18273.04 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 16:54 | +10 stop | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 10-29 16:54 | +20 | DOGE | DOWN | 0.63 | 0.83 | 1.73 |
| 10-29 16:54 | +15 | DOGE | DOWN | 0.63 | 0.79 | 1.31 |
| 10-29 16:54 | +10 | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 10-29 16:54 | +5 | DOGE | DOWN | 0.63 | 0.71 | 0.48 |
| 10-29 16:54 | +10 stop | SOL | DOWN | 0.69 | 0.81 | 0.94 |
| 10-29 16:53 | +10 stop | SOL | DOWN | 0.70 | 0.55 | -1.83 |
| 10-29 16:53 | +20 | SOL | DOWN | 0.70 | 0.91 | 1.88 |
| 10-29 16:53 | +15 | SOL | DOWN | 0.70 | 0.85 | 1.26 |
| 10-29 16:53 | +10 | SOL | DOWN | 0.70 | 0.81 | 0.84 |
| 10-29 16:53 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.42 |
| 10-29 16:51 | +10 stop | HYPE | DOWN | 0.59 | 0.23 | -3.90 |
| 10-29 16:51 | +5 | HYPE | DOWN | 0.59 | open |  |
| 10-29 16:48 | +5 | HYPE | DOWN | 0.67 | 0.73 | 0.30 |
| 10-29 16:48 | +5 | NEAR | DOWN | 0.69 | 0.82 | 1.04 |
| 10-29 16:48 | +5 | DOGE | DOWN | 0.68 | 0.83 | 1.24 |
| 10-29 16:48 | +5 | SOL | DOWN | 0.59 | 0.68 | 0.57 |
| 10-29 16:47 | +5 | XRP | UP | 0.57 | open |  |
| 10-29 16:47 | +10 stop | HYPE | UP | 0.48 | 0.32 | -1.94 |
| 10-29 16:47 | +20 | HYPE | UP | 0.48 | 0.76 | 2.49 |
| 10-29 16:47 | +15 | HYPE | UP | 0.49 | 0.76 | 2.35 |
| 10-29 16:47 | +10 | HYPE | UP | 0.51 | 0.76 | 2.20 |
| 10-29 16:47 | +5 | HYPE | UP | 0.51 | 0.57 | 0.26 |
| 10-29 16:46 | +10 stop | DOGE | DOWN | 0.56 | 0.71 | 1.17 |
| 10-29 16:46 | +20 | DOGE | DOWN | 0.56 | 0.83 | 2.42 |
| 10-29 16:46 | +15 | DOGE | DOWN | 0.56 | 0.71 | 1.17 |
| 10-29 16:46 | +10 | DOGE | DOWN | 0.56 | 0.71 | 1.17 |
| 10-29 16:46 | +5 | DOGE | DOWN | 0.56 | 0.62 | 0.25 |
| 10-29 16:46 | +10 stop | XRP | UP | 0.58 | 0.42 | -2.00 |
| 10-29 16:46 | +20 | XRP | UP | 0.58 | open |  |
| 10-29 16:46 | +15 | XRP | UP | 0.58 | open |  |
| 10-29 16:46 | +10 | XRP | UP | 0.58 | open |  |
| 10-29 16:46 | +5 | XRP | UP | 0.58 | 0.67 | 0.52 |
| 10-29 16:46 | +10 stop | BNB | UP | 0.59 | 0.43 | -1.95 |
| 10-29 16:46 | +20 | BNB | UP | 0.59 | 0.79 | 1.71 |
| 10-29 16:46 | +15 | BNB | UP | 0.58 | 0.73 | 1.18 |
| 10-29 16:46 | +10 | BNB | UP | 0.58 | 0.71 | 0.97 |
| 10-29 16:46 | +5 | BNB | UP | 0.58 | 0.71 | 0.97 |
| 10-29 16:46 | +10 stop | SOL | DOWN | 0.53 | 0.68 | 1.16 |
| 10-29 16:46 | +20 | SOL | DOWN | 0.53 | 0.77 | 2.09 |
