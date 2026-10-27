# Range-Scalp Bot

*Updated Tue Oct 27 01:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35776 | 31227 | 4549 (43) | 0 | $-9983.13 | -4.4% |
| **+10¢** | 26741 | 21478 | 5263 (65) | 0 | $-8828.99 | -5.2% |
| **+15¢** | 22384 | 16725 | 5659 (89) | 0 | $-7876.37 | -5.6% |
| **+20¢** | 19840 | 13910 | 5930 (112) | 0 | $-6936.88 | -5.6% |
| **+10¢ (15¢ stop)** | 43833 | 43770 | 63 (33) | 0 | $-16674.73 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 01:20 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-27 01:20 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-27 01:19 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 10-27 01:18 | +10 stop | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-27 01:18 | +10 | DOGE | DOWN | 0.63 | 0.73 | 0.69 |
| 10-27 01:18 | +5 | DOGE | DOWN | 0.63 | 0.70 | 0.38 |
| 10-27 01:18 | +10 stop | XRP | DOWN | 0.68 | 0.84 | 1.34 |
| 10-27 01:18 | +20 | XRP | DOWN | 0.68 | 0.93 | 2.29 |
| 10-27 01:18 | +15 | XRP | DOWN | 0.68 | 0.84 | 1.34 |
| 10-27 01:18 | +10 | XRP | DOWN | 0.68 | 0.84 | 1.34 |
| 10-27 01:18 | +5 | XRP | DOWN | 0.68 | 0.84 | 1.34 |
| 10-27 01:18 | +10 stop | SOL | DOWN | 0.53 | 0.68 | 1.16 |
| 10-27 01:18 | +10 | SOL | DOWN | 0.53 | 0.68 | 1.16 |
| 10-27 01:18 | +5 | SOL | DOWN | 0.53 | 0.59 | 0.25 |
| 10-27 01:17 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
| 10-27 01:17 | +5 | SOL | DOWN | 0.54 | 0.61 | 0.35 |
| 10-27 01:17 | +10 stop | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-27 01:17 | +20 | DOGE | DOWN | 0.67 | 0.88 | 1.86 |
| 10-27 01:17 | +15 | DOGE | DOWN | 0.67 | 0.86 | 1.65 |
| 10-27 01:17 | +10 | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-27 01:17 | +5 | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-27 01:16 | +10 stop | SOL | DOWN | 0.59 | 0.70 | 0.74 |
| 10-27 01:16 | +20 | SOL | DOWN | 0.59 | 0.80 | 1.77 |
| 10-27 01:16 | +15 | SOL | DOWN | 0.60 | 0.78 | 1.50 |
| 10-27 01:16 | +10 | SOL | DOWN | 0.57 | 0.70 | 0.97 |
| 10-27 01:16 | +5 | SOL | DOWN | 0.57 | 0.62 | 0.15 |
| 10-27 01:16 | +10 stop | BTC | DOWN | 0.66 | 0.84 | 1.54 |
| 10-27 01:16 | +20 | BTC | DOWN | 0.66 | 0.87 | 1.86 |
| 10-27 01:16 | +15 | BTC | DOWN | 0.66 | 0.84 | 1.54 |
| 10-27 01:16 | +10 | BTC | DOWN | 0.66 | 0.84 | 1.54 |
| 10-27 01:16 | +5 | BTC | DOWN | 0.66 | 0.72 | 0.29 |
| 10-27 01:16 | +10 stop | ZEC | DOWN | 0.67 | 0.80 | 1.03 |
| 10-27 01:16 | +20 | ZEC | DOWN | 0.67 | 0.91 | 2.13 |
| 10-27 01:16 | +15 | ZEC | DOWN | 0.67 | 0.82 | 1.24 |
| 10-27 01:16 | +10 | ZEC | DOWN | 0.67 | 0.80 | 1.03 |
| 10-27 01:16 | +5 | ZEC | DOWN | 0.67 | 0.76 | 0.62 |
| 10-27 01:16 | +10 stop | BNB | DOWN | 0.71 | 0.87 | 1.37 |
| 10-27 01:16 | +20 | BNB | DOWN | 0.71 | 0.91 | 1.81 |
| 10-27 01:16 | +15 | BNB | DOWN | 0.71 | 0.87 | 1.37 |
| 10-27 01:16 | +10 | BNB | DOWN | 0.71 | 0.87 | 1.37 |
