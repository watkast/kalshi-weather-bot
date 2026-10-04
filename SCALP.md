# Range-Scalp Bot

*Updated Sun Oct 04 17:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2522 | 2171 | 351 (3) | 0 | $-852.73 | -5.3% |
| **+10¢** | 1979 | 1587 | 392 (4) | 0 | $-661.92 | -5.3% |
| **+15¢** | 1658 | 1246 | 412 (5) | 0 | $-542.77 | -5.2% |
| **+20¢** | 1475 | 1043 | 432 (9) | 0 | $-455.24 | -4.9% |
| **+10¢ (15¢ stop)** | 3133 | 3132 | 1 (1) | 0 | $-1150.17 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 16:55 | +10 stop | BTC | UP | 0.59 | 0.83 | 2.13 |
| 10-04 16:54 | +10 stop | XRP | UP | 0.60 | 0.70 | 0.68 |
| 10-04 16:51 | +10 stop | XRP | UP | 0.70 | 0.83 | 1.05 |
| 10-04 16:50 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 10-04 16:50 | +10 stop | ETH | UP | 0.69 | 0.79 | 0.73 |
| 10-04 16:50 | +10 stop | DOGE | UP | 0.67 | 0.80 | 1.02 |
| 10-04 16:50 | +10 stop | XRP | UP | 0.71 | 0.50 | -2.43 |
| 10-04 16:50 | +10 stop | BNB | UP | 0.51 | 0.33 | -2.09 |
| 10-04 16:50 | +10 | BNB | UP | 0.51 | no | -5.28 |
| 10-04 16:50 | +5 | BNB | UP | 0.51 | no | -5.28 |
| 10-04 16:49 | +10 | BNB | DOWN | 0.52 | 0.66 | 1.06 |
| 10-04 16:49 | +5 | BNB | DOWN | 0.52 | 0.66 | 1.07 |
| 10-04 16:47 | +10 stop | XRP | DOWN | 0.65 | 0.50 | -1.84 |
| 10-04 16:47 | +10 | XRP | DOWN | 0.65 | 0.99 | 3.22 |
| 10-04 16:47 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 10-04 16:47 | +10 stop | HYPE | UP | 0.67 | 0.78 | 0.81 |
| 10-04 16:47 | +20 | HYPE | UP | 0.67 | 0.88 | 1.86 |
| 10-04 16:47 | +15 | HYPE | UP | 0.67 | 0.86 | 1.65 |
| 10-04 16:47 | +10 | HYPE | UP | 0.67 | 0.78 | 0.81 |
| 10-04 16:47 | +5 | HYPE | UP | 0.67 | 0.78 | 0.81 |
| 10-04 16:47 | +10 stop | ZEC | DOWN | 0.54 | 0.30 | -2.68 |
| 10-04 16:47 | +20 | ZEC | DOWN | 0.54 | yes | -5.53 |
| 10-04 16:47 | +15 | ZEC | DOWN | 0.53 | yes | -5.48 |
| 10-04 16:47 | +10 | ZEC | DOWN | 0.53 | yes | -5.48 |
| 10-04 16:47 | +5 | ZEC | DOWN | 0.53 | yes | -5.48 |
| 10-04 16:47 | +10 stop | BTC | DOWN | 0.61 | 0.37 | -2.74 |
| 10-04 16:47 | +20 | BTC | DOWN | 0.61 | yes | -6.27 |
| 10-04 16:47 | +15 | BTC | DOWN | 0.61 | yes | -6.27 |
| 10-04 16:47 | +10 | BTC | DOWN | 0.61 | yes | -6.27 |
| 10-04 16:47 | +5 | BTC | DOWN | 0.61 | yes | -6.27 |
| 10-04 16:46 | +10 stop | SOL | DOWN | 0.71 | 0.41 | -3.31 |
| 10-04 16:46 | +20 | SOL | DOWN | 0.71 | yes | -7.24 |
| 10-04 16:46 | +15 | SOL | DOWN | 0.71 | yes | -7.24 |
| 10-04 16:46 | +10 | SOL | DOWN | 0.71 | yes | -7.24 |
| 10-04 16:46 | +5 | SOL | DOWN | 0.71 | yes | -7.24 |
| 10-04 16:45 | +10 stop | BNB | DOWN | 0.70 | 0.47 | -2.63 |
| 10-04 16:45 | +20 | BNB | DOWN | 0.70 | 0.95 | 2.33 |
| 10-04 16:45 | +15 | BNB | DOWN | 0.69 | 0.85 | 1.36 |
| 10-04 16:45 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-04 16:45 | +5 | BNB | DOWN | 0.69 | 0.78 | 0.62 |
