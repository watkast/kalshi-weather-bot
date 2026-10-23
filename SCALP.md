# Range-Scalp Bot

*Updated Fri Oct 23 15:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30511 | 26581 | 3930 (39) | 1 | $-8868.73 | -4.6% |
| **+10¢** | 22832 | 18287 | 4545 (56) | 3 | $-7928.45 | -5.5% |
| **+15¢** | 19108 | 14220 | 4888 (79) | 3 | $-7142.40 | -6.0% |
| **+20¢** | 16922 | 11801 | 5121 (102) | 3 | $-6415.96 | -6.0% |
| **+10¢ (15¢ stop)** | 37392 | 37333 | 59 (32) | 0 | $-14138.59 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 14:57 | +10 stop | BTC | UP | 0.53 | 0.34 | -2.24 |
| 10-23 14:57 | +10 stop | ETH | UP | 0.68 | 0.51 | -2.04 |
| 10-23 14:57 | +10 stop | NEAR | UP | 0.71 | 0.52 | -2.23 |
| 10-23 14:57 | +5 | NEAR | UP | 0.71 | 0.76 | 0.22 |
| 10-23 14:57 | +10 stop | ZEC | DOWN | 0.54 | 0.65 | 0.79 |
| 10-23 14:57 | +10 stop | XRP | DOWN | 0.54 | 0.35 | -2.24 |
| 10-23 14:56 | +10 stop | ETH | UP | 0.62 | 0.47 | -1.85 |
| 10-23 14:56 | +10 stop | BTC | UP | 0.59 | 0.36 | -2.64 |
| 10-23 14:55 | +10 stop | BNB | DOWN | 0.67 | 0.77 | 0.72 |
| 10-23 14:55 | +20 | BNB | DOWN | 0.67 | 0.92 | 2.29 |
| 10-23 14:55 | +15 | BNB | DOWN | 0.67 | 0.92 | 2.29 |
| 10-23 14:55 | +10 | BNB | DOWN | 0.67 | 0.77 | 0.72 |
| 10-23 14:55 | +5 | BNB | DOWN | 0.67 | 0.73 | 0.31 |
| 10-23 14:55 | +10 stop | XRP | UP | 0.59 | 0.44 | -1.85 |
| 10-23 14:53 | +10 stop | BNB | UP | 0.66 | 0.79 | 1.02 |
| 10-23 14:53 | +5 | BNB | UP | 0.66 | 0.79 | 1.02 |
| 10-23 14:52 | +10 stop | BNB | UP | 0.52 | 0.65 | 0.92 |
| 10-23 14:52 | +5 | XRP | DOWN | 0.56 | 0.85 | 2.64 |
| 10-23 14:51 | +10 stop | XRP | DOWN | 0.56 | 0.36 | -2.35 |
| 10-23 14:51 | +10 | XRP | DOWN | 0.56 | 0.85 | 2.63 |
| 10-23 14:51 | +10 stop | BTC | DOWN | 0.49 | 0.26 | -2.62 |
| 10-23 14:51 | +5 | XRP | DOWN | 0.52 | 0.58 | 0.24 |
| 10-23 14:51 | +5 | NEAR | UP | 0.59 | 0.66 | 0.37 |
| 10-23 14:51 | +10 stop | DOGE | UP | 0.62 | 0.72 | 0.68 |
| 10-23 14:50 | +10 stop | XRP | DOWN | 0.48 | 0.60 | 0.85 |
| 10-23 14:50 | +10 | XRP | DOWN | 0.48 | 0.60 | 0.85 |
| 10-23 14:50 | +5 | XRP | DOWN | 0.49 | 0.54 | 0.14 |
| 10-23 14:50 | +10 stop | NEAR | UP | 0.60 | 0.76 | 1.30 |
| 10-23 14:50 | +5 | NEAR | UP | 0.60 | 0.66 | 0.27 |
| 10-23 14:50 | +5 | SOL | UP | 0.57 | 0.65 | 0.48 |
| 10-23 14:50 | +10 stop | XRP | DOWN | 0.50 | 0.61 | 0.75 |
| 10-23 14:50 | +20 | XRP | DOWN | 0.50 | 0.85 | 3.23 |
| 10-23 14:50 | +15 | XRP | DOWN | 0.50 | 0.85 | 3.23 |
| 10-23 14:50 | +10 | XRP | DOWN | 0.50 | 0.61 | 0.75 |
| 10-23 14:50 | +5 | XRP | DOWN | 0.50 | 0.61 | 0.75 |
| 10-23 14:49 | +10 stop | NEAR | UP | 0.51 | 0.63 | 0.86 |
| 10-23 14:49 | +10 stop | BNB | UP | 0.54 | 0.64 | 0.65 |
| 10-23 14:49 | +5 | SOL | UP | 0.53 | 0.58 | 0.14 |
| 10-23 14:49 | +10 stop | ZEC | UP | 0.65 | 0.83 | 1.54 |
| 10-23 14:48 | +5 | ETH | DOWN | 0.61 | 0.71 | 0.68 |
