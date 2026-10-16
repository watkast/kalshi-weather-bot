# Range-Scalp Bot

*Updated Fri Oct 16 12:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19232 | 16709 | 2523 (29) | 3 | $-5814.96 | -4.8% |
| **+10¢** | 14502 | 11585 | 2917 (41) | 2 | $-5246.44 | -5.8% |
| **+15¢** | 12137 | 8998 | 3139 (60) | 4 | $-4757.54 | -6.2% |
| **+20¢** | 10767 | 7476 | 3291 (79) | 4 | $-4242.48 | -6.3% |
| **+10¢ (15¢ stop)** | 23658 | 23608 | 50 (29) | 0 | $-9115.72 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 12:42 | +10 stop | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 10-16 12:42 | +10 | XRP | DOWN | 0.69 | 0.86 | 1.46 |
| 10-16 12:42 | +5 | XRP | DOWN | 0.69 | 0.77 | 0.52 |
| 10-16 12:42 | +15 | DOGE | UP | 0.52 | open |  |
| 10-16 12:41 | +10 stop | BTC | DOWN | 0.70 | 0.93 | 2.10 |
| 10-16 12:41 | +20 | BTC | DOWN | 0.71 | 0.93 | 2.00 |
| 10-16 12:41 | +15 | BTC | DOWN | 0.71 | 0.93 | 2.00 |
| 10-16 12:41 | +10 | BTC | DOWN | 0.71 | 0.93 | 2.00 |
| 10-16 12:41 | +5 | BTC | DOWN | 0.71 | 0.93 | 2.00 |
| 10-16 12:41 | +10 stop | DOGE | UP | 0.58 | 0.19 | -4.19 |
| 10-16 12:41 | +5 | DOGE | UP | 0.58 | 0.67 | 0.56 |
| 10-16 12:41 | +10 stop | ETH | DOWN | 0.54 | 0.69 | 1.17 |
| 10-16 12:41 | +20 | ETH | DOWN | 0.54 | 0.94 | 3.75 |
| 10-16 12:41 | +15 | ETH | DOWN | 0.54 | 0.69 | 1.17 |
| 10-16 12:41 | +10 | ETH | DOWN | 0.54 | 0.69 | 1.17 |
| 10-16 12:41 | +10 stop | DOGE | UP | 0.43 | 0.62 | 1.55 |
| 10-16 12:41 | +5 | DOGE | UP | 0.43 | 0.62 | 1.55 |
| 10-16 12:40 | +10 stop | BTC | DOWN | 0.51 | 0.76 | 2.19 |
| 10-16 12:40 | +20 | BTC | DOWN | 0.51 | 0.76 | 2.19 |
| 10-16 12:40 | +15 | BTC | DOWN | 0.51 | 0.76 | 2.19 |
| 10-16 12:40 | +10 | BTC | DOWN | 0.51 | 0.76 | 2.19 |
| 10-16 12:40 | +5 | BTC | DOWN | 0.52 | 0.57 | 0.14 |
| 10-16 12:40 | +10 stop | BNB | DOWN | 0.59 | 0.80 | 1.81 |
| 10-16 12:39 | +5 | ZEC | DOWN | 0.66 | open |  |
| 10-16 12:38 | +10 stop | DOGE | DOWN | 0.67 | 0.47 | -2.34 |
| 10-16 12:38 | +10 | DOGE | DOWN | 0.68 | 0.80 | 0.94 |
| 10-16 12:38 | +5 | DOGE | DOWN | 0.67 | 0.73 | 0.30 |
| 10-16 12:38 | +10 stop | ZEC | UP | 0.49 | 0.67 | 1.46 |
| 10-16 12:38 | +10 | ZEC | UP | 0.49 | 0.67 | 1.46 |
| 10-16 12:38 | +10 stop | NEAR | UP | 0.69 | 0.50 | -2.23 |
| 10-16 12:38 | +20 | NEAR | UP | 0.68 | 0.88 | 1.76 |
| 10-16 12:38 | +15 | NEAR | UP | 0.68 | 0.87 | 1.66 |
| 10-16 12:38 | +10 | NEAR | UP | 0.68 | 0.87 | 1.66 |
| 10-16 12:38 | +5 | NEAR | UP | 0.68 | 0.73 | 0.20 |
| 10-16 12:38 | +5 | ZEC | UP | 0.52 | 0.57 | 0.14 |
| 10-16 12:37 | +10 stop | DOGE | DOWN | 0.49 | 0.63 | 1.05 |
| 10-16 12:37 | +10 | DOGE | DOWN | 0.49 | 0.63 | 1.05 |
| 10-16 12:37 | +5 | DOGE | DOWN | 0.49 | 0.63 | 1.05 |
| 10-16 12:37 | +10 stop | ZEC | UP | 0.52 | 0.63 | 0.75 |
| 10-16 12:37 | +20 | ZEC | UP | 0.52 | 0.81 | 2.61 |
