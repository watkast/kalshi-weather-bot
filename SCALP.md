# Range-Scalp Bot

*Updated Thu Oct 22 23:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29416 | 25603 | 3813 (39) | 4 | $-8687.43 | -4.7% |
| **+10¢** | 22057 | 17640 | 4417 (55) | 4 | $-7850.69 | -5.7% |
| **+15¢** | 18468 | 13726 | 4742 (78) | 4 | $-7027.81 | -6.1% |
| **+20¢** | 16345 | 11374 | 4971 (100) | 4 | $-6370.46 | -6.2% |
| **+10¢ (15¢ stop)** | 36115 | 36056 | 59 (32) | 0 | $-13643.55 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 23:13 | +10 stop | DOGE | UP | 0.48 | 0.72 | 2.07 |
| 10-22 23:12 | +10 stop | ETH | DOWN | 0.58 | 0.84 | 2.32 |
| 10-22 23:12 | +15 | ETH | DOWN | 0.58 | 0.84 | 2.32 |
| 10-22 23:12 | +10 | ETH | DOWN | 0.58 | 0.84 | 2.32 |
| 10-22 23:12 | +5 | ETH | DOWN | 0.57 | 0.65 | 0.46 |
| 10-22 23:11 | +10 stop | DOGE | DOWN | 0.62 | 0.44 | -2.15 |
| 10-22 23:11 | +5 | DOGE | DOWN | 0.62 | open |  |
| 10-22 23:10 | +10 stop | BTC | UP | 0.51 | 0.66 | 1.16 |
| 10-22 23:10 | +20 | BTC | UP | 0.51 | 0.71 | 1.67 |
| 10-22 23:10 | +15 | BTC | UP | 0.51 | 0.66 | 1.16 |
| 10-22 23:10 | +10 | BTC | UP | 0.52 | 0.66 | 1.06 |
| 10-22 23:10 | +5 | BTC | UP | 0.52 | 0.66 | 1.06 |
| 10-22 23:10 | +10 stop | ETH | UP | 0.38 | 0.59 | 1.76 |
| 10-22 23:09 | +10 stop | DOGE | UP | 0.67 | 0.30 | -4.01 |
| 10-22 23:09 | +10 stop | ETH | UP | 0.64 | 0.76 | 0.90 |
| 10-22 23:08 | +10 stop | DOGE | UP | 0.53 | 0.65 | 0.86 |
| 10-22 23:08 | +10 stop | BNB | UP | 0.53 | 0.28 | -2.83 |
| 10-22 23:07 | +10 stop | BNB | DOWN | 0.62 | 0.34 | -3.13 |
| 10-22 23:06 | +10 stop | BTC | UP | 0.64 | 0.74 | 0.69 |
| 10-22 23:06 | +15 | BTC | UP | 0.64 | 0.83 | 1.63 |
| 10-22 23:06 | +10 | BTC | UP | 0.64 | 0.74 | 0.69 |
| 10-22 23:06 | +5 | BTC | UP | 0.64 | 0.71 | 0.38 |
| 10-22 23:05 | +10 stop | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 10-22 23:05 | +10 stop | ETH | UP | 0.54 | 0.71 | 1.37 |
| 10-22 23:04 | +10 stop | XRP | DOWN | 0.54 | 0.32 | -2.56 |
| 10-22 23:04 | +10 stop | DOGE | DOWN | 0.54 | 0.30 | -2.73 |
| 10-22 23:04 | +10 stop | ZEC | UP | 0.67 | 0.80 | 1.02 |
| 10-22 23:04 | +5 | ZEC | UP | 0.67 | 0.72 | 0.19 |
| 10-22 23:04 | +10 stop | SOL | UP | 0.54 | 0.75 | 1.78 |
| 10-22 23:03 | +10 stop | BNB | DOWN | 0.65 | 0.50 | -1.84 |
| 10-22 23:03 | +10 stop | BTC | UP | 0.57 | 0.72 | 1.17 |
| 10-22 23:03 | +20 | BTC | UP | 0.57 | 0.83 | 2.32 |
| 10-22 23:03 | +15 | BTC | UP | 0.57 | 0.72 | 1.17 |
| 10-22 23:03 | +10 | BTC | UP | 0.57 | 0.72 | 1.17 |
| 10-22 23:03 | +5 | BTC | UP | 0.57 | 0.72 | 1.17 |
| 10-22 23:03 | +10 stop | NEAR | UP | 0.66 | 0.80 | 1.12 |
| 10-22 23:02 | +10 stop | DOGE | DOWN | 0.70 | 0.49 | -2.43 |
| 10-22 23:02 | +20 | DOGE | DOWN | 0.70 | open |  |
| 10-22 23:02 | +15 | DOGE | DOWN | 0.70 | open |  |
| 10-22 23:02 | +10 | DOGE | DOWN | 0.70 | open |  |
