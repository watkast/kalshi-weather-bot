# Range-Scalp Bot

*Updated Fri Oct 23 11:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30277 | 26371 | 3906 (39) | 3 | $-8831.24 | -4.6% |
| **+10¢** | 22690 | 18171 | 4519 (56) | 3 | $-7891.90 | -5.5% |
| **+15¢** | 18995 | 14135 | 4860 (79) | 3 | $-7118.17 | -6.0% |
| **+20¢** | 16816 | 11725 | 5091 (102) | 3 | $-6397.22 | -6.1% |
| **+10¢ (15¢ stop)** | 37140 | 37081 | 59 (32) | 1 | $-14041.15 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 11:57 | +10 stop | BNB | UP | 0.61 | open |  |
| 10-23 11:57 | +10 stop | BNB | DOWN | 0.70 | 0.35 | -3.81 |
| 10-23 11:55 | +10 stop | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-23 11:55 | +10 | BTC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-23 11:55 | +5 | BTC | DOWN | 0.70 | 0.79 | 0.63 |
| 10-23 11:55 | +10 | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-23 11:55 | +5 | DOGE | DOWN | 0.71 | 0.77 | 0.32 |
| 10-23 11:55 | +10 stop | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-23 11:55 | +20 | DOGE | DOWN | 0.70 | 0.93 | 2.14 |
| 10-23 11:55 | +15 | DOGE | DOWN | 0.70 | 0.89 | 1.68 |
| 10-23 11:54 | +10 | BTC | DOWN | 0.52 | 0.64 | 0.85 |
| 10-23 11:54 | +5 | BTC | DOWN | 0.52 | 0.64 | 0.85 |
| 10-23 11:54 | +10 stop | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 10-23 11:54 | +10 | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 10-23 11:54 | +5 | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 10-23 11:54 | +10 stop | XRP | DOWN | 0.51 | 0.31 | -2.33 |
| 10-23 11:54 | +5 | XRP | DOWN | 0.51 | 0.69 | 1.47 |
| 10-23 11:53 | +10 stop | BTC | DOWN | 0.71 | 0.54 | -2.03 |
| 10-23 11:53 | +10 stop | BNB | UP | 0.60 | 0.38 | -2.54 |
| 10-23 11:52 | +10 stop | ETH | UP | 0.62 | 0.26 | -3.91 |
| 10-23 11:52 | +10 stop | XRP | UP | 0.65 | 0.40 | -2.83 |
| 10-23 11:49 | +10 stop | DOGE | UP | 0.56 | 0.37 | -2.25 |
| 10-23 11:48 | +10 stop | BTC | UP | 0.60 | 0.44 | -1.95 |
| 10-23 11:47 | +10 stop | BNB | UP | 0.63 | 0.73 | 0.69 |
| 10-23 11:47 | +10 stop | ETH | UP | 0.65 | 0.79 | 1.12 |
| 10-23 11:47 | +10 stop | NEAR | UP | 0.68 | 0.79 | 0.82 |
| 10-23 11:47 | +10 stop | SOL | UP | 0.70 | 0.82 | 0.94 |
| 10-23 11:47 | +10 stop | ZEC | UP | 0.70 | 0.80 | 0.73 |
| 10-23 11:47 | +20 | ZEC | UP | 0.70 | 0.91 | 1.90 |
| 10-23 11:47 | +15 | ZEC | UP | 0.70 | 0.86 | 1.36 |
| 10-23 11:47 | +10 | ZEC | UP | 0.71 | 0.83 | 0.95 |
| 10-23 11:47 | +5 | ZEC | UP | 0.71 | 0.76 | 0.22 |
| 10-23 11:46 | +5 | BTC | DOWN | 0.62 | 0.75 | 0.99 |
| 10-23 11:46 | +10 stop | ETH | DOWN | 0.60 | 0.41 | -2.24 |
| 10-23 11:46 | +20 | ETH | DOWN | 0.60 | 0.84 | 2.13 |
| 10-23 11:46 | +15 | ETH | DOWN | 0.60 | 0.78 | 1.50 |
| 10-23 11:46 | +10 | ETH | DOWN | 0.60 | 0.73 | 0.99 |
| 10-23 11:46 | +5 | ETH | DOWN | 0.60 | 0.73 | 0.99 |
| 10-23 11:46 | +10 stop | XRP | DOWN | 0.54 | 0.28 | -2.93 |
| 10-23 11:46 | +20 | XRP | DOWN | 0.54 | 0.82 | 2.51 |
