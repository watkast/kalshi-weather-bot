# Range-Scalp Bot

*Updated Sun Oct 04 12:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2255 | 1947 | 308 (3) | 0 | $-736.07 | -5.1% |
| **+10¢** | 1758 | 1415 | 343 (4) | 0 | $-550.93 | -5.0% |
| **+15¢** | 1477 | 1113 | 364 (5) | 0 | $-464.93 | -5.0% |
| **+20¢** | 1305 | 922 | 383 (8) | 0 | $-408.04 | -5.0% |
| **+10¢ (15¢ stop)** | 2781 | 2780 | 1 (1) | 0 | $-1031.52 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 12:27 | +10 stop | SOL | UP | 0.50 | 0.73 | 1.98 |
| 10-04 12:27 | +5 | SOL | UP | 0.49 | 0.58 | 0.54 |
| 10-04 12:26 | +10 stop | DOGE | UP | 0.59 | 0.91 | 2.94 |
| 10-04 12:24 | +10 stop | BNB | DOWN | 0.62 | 0.79 | 1.41 |
| 10-04 12:23 | +10 stop | BNB | DOWN | 0.51 | 0.64 | 1.00 |
| 10-04 12:22 | +5 | SOL | UP | 0.58 | 0.64 | 0.25 |
| 10-04 12:21 | +10 stop | BNB | DOWN | 0.68 | 0.53 | -1.84 |
| 10-04 12:21 | +5 | SOL | UP | 0.55 | 0.60 | 0.15 |
| 10-04 12:20 | +10 stop | BTC | DOWN | 0.56 | 0.38 | -2.15 |
| 10-04 12:20 | +10 | BTC | DOWN | 0.56 | yes | -5.78 |
| 10-04 12:20 | +5 | BTC | DOWN | 0.56 | yes | -5.78 |
| 10-04 12:20 | +10 stop | SOL | UP | 0.55 | 0.67 | 0.86 |
| 10-04 12:20 | +5 | SOL | UP | 0.55 | 0.61 | 0.25 |
| 10-04 12:19 | +10 stop | DOGE | DOWN | 0.62 | 0.43 | -2.25 |
| 10-04 12:19 | +15 | DOGE | DOWN | 0.62 | yes | -6.37 |
| 10-04 12:19 | +10 | DOGE | DOWN | 0.62 | yes | -6.37 |
| 10-04 12:19 | +5 | ETH | UP | 0.71 | 0.78 | 0.42 |
| 10-04 12:19 | +10 stop | XRP | UP | 0.60 | 0.74 | 1.09 |
| 10-04 12:19 | +20 | XRP | UP | 0.60 | 0.86 | 2.34 |
| 10-04 12:19 | +15 | XRP | UP | 0.60 | 0.76 | 1.30 |
| 10-04 12:19 | +10 | XRP | UP | 0.60 | 0.74 | 1.09 |
| 10-04 12:19 | +5 | XRP | UP | 0.60 | 0.74 | 1.09 |
| 10-04 12:19 | +5 | DOGE | DOWN | 0.68 | yes | -6.98 |
| 10-04 12:19 | +10 stop | BTC | UP | 0.43 | 0.55 | 0.84 |
| 10-04 12:19 | +10 | BTC | UP | 0.43 | 0.55 | 0.84 |
| 10-04 12:19 | +5 | BTC | UP | 0.43 | 0.55 | 0.84 |
| 10-04 12:19 | +10 stop | BNB | DOWN | 0.70 | 0.55 | -1.86 |
| 10-04 12:19 | +15 | BNB | DOWN | 0.70 | 0.99 | 2.73 |
| 10-04 12:19 | +10 | BNB | DOWN | 0.70 | 0.81 | 0.81 |
| 10-04 12:19 | +5 | BNB | DOWN | 0.70 | 0.79 | 0.60 |
| 10-04 12:18 | +10 stop | ETH | UP | 0.70 | 0.81 | 0.84 |
| 10-04 12:18 | +20 | ETH | UP | 0.70 | 0.92 | 1.95 |
| 10-04 12:18 | +15 | ETH | UP | 0.70 | 0.87 | 1.47 |
| 10-04 12:18 | +10 | ETH | UP | 0.70 | 0.81 | 0.84 |
| 10-04 12:18 | +5 | ETH | UP | 0.71 | 0.79 | 0.53 |
| 10-04 12:18 | +10 stop | BTC | DOWN | 0.47 | 0.61 | 1.05 |
| 10-04 12:18 | +20 | BTC | DOWN | 0.47 | yes | -4.88 |
| 10-04 12:18 | +15 | BTC | DOWN | 0.47 | yes | -4.88 |
| 10-04 12:18 | +10 | BTC | DOWN | 0.47 | 0.61 | 1.05 |
| 10-04 12:18 | +5 | BTC | DOWN | 0.47 | 0.61 | 1.05 |
