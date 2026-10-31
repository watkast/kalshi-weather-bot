# Range-Scalp Bot

*Updated Sat Oct 31 15:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42436 | 37018 | 5418 (59) | 1 | $-11912.97 | -4.5% |
| **+10¢** | 31639 | 25367 | 6272 (81) | 2 | $-10704.00 | -5.4% |
| **+15¢** | 26460 | 19697 | 6763 (109) | 2 | $-9800.24 | -5.9% |
| **+20¢** | 23500 | 16411 | 7089 (141) | 2 | $-8671.66 | -5.9% |
| **+10¢ (15¢ stop)** | 51748 | 51669 | 79 (44) | 0 | $-19550.32 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 15:57 | +10 stop | BTC | UP | 0.51 | 0.64 | 0.95 |
| 10-31 15:56 | +10 stop | ETH | UP | 0.60 | 0.25 | -3.81 |
| 10-31 15:54 | +10 stop | BTC | DOWN | 0.51 | 0.31 | -2.33 |
| 10-31 15:53 | +10 stop | NEAR | UP | 0.54 | 0.77 | 1.99 |
| 10-31 15:52 | +10 stop | SOL | UP | 0.54 | 0.70 | 1.27 |
| 10-31 15:52 | +10 | ETH | DOWN | 0.62 | 0.73 | 0.79 |
| 10-31 15:52 | +5 | ETH | DOWN | 0.62 | 0.73 | 0.79 |
| 10-31 15:50 | +10 stop | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 10-31 15:50 | +10 | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 10-31 15:50 | +5 | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 10-31 15:50 | +10 stop | SOL | DOWN | 0.61 | 0.44 | -2.05 |
| 10-31 15:50 | +10 stop | BTC | DOWN | 0.66 | 0.50 | -1.94 |
| 10-31 15:50 | +10 | BTC | DOWN | 0.66 | 0.83 | 1.44 |
| 10-31 15:50 | +5 | BTC | DOWN | 0.66 | 0.83 | 1.44 |
| 10-31 15:50 | +5 | ZEC | DOWN | 0.67 | 0.81 | 1.14 |
| 10-31 15:49 | +10 stop | ETH | DOWN | 0.65 | 0.43 | -2.54 |
| 10-31 15:49 | +10 stop | XRP | UP | 0.68 | 0.79 | 0.82 |
| 10-31 15:49 | +15 | XRP | UP | 0.68 | 0.86 | 1.55 |
| 10-31 15:49 | +10 | XRP | UP | 0.68 | 0.79 | 0.82 |
| 10-31 15:49 | +5 | XRP | UP | 0.68 | 0.77 | 0.61 |
| 10-31 15:48 | +10 stop | BNB | DOWN | 0.64 | 0.87 | 2.05 |
| 10-31 15:48 | +10 | BNB | DOWN | 0.64 | 0.87 | 2.05 |
| 10-31 15:48 | +5 | BNB | DOWN | 0.64 | 0.69 | 0.18 |
| 10-31 15:48 | +10 stop | SOL | UP | 0.68 | 0.53 | -1.84 |
| 10-31 15:48 | +10 stop | ETH | UP | 0.57 | 0.39 | -2.15 |
| 10-31 15:48 | +10 stop | NEAR | DOWN | 0.66 | 0.51 | -1.84 |
| 10-31 15:48 | +10 | NEAR | DOWN | 0.66 | open |  |
| 10-31 15:48 | +5 | NEAR | DOWN | 0.66 | open |  |
| 10-31 15:48 | +5 | SOL | UP | 0.68 | 0.73 | 0.20 |
| 10-31 15:47 | +5 | ZEC | DOWN | 0.60 | 0.66 | 0.27 |
| 10-31 15:46 | +10 stop | BTC | DOWN | 0.58 | 0.71 | 0.97 |
| 10-31 15:46 | +20 | BTC | DOWN | 0.58 | 0.83 | 2.22 |
| 10-31 15:46 | +15 | BTC | DOWN | 0.58 | 0.83 | 2.22 |
| 10-31 15:46 | +10 | BTC | DOWN | 0.58 | 0.71 | 0.97 |
| 10-31 15:46 | +5 | BTC | DOWN | 0.59 | 0.65 | 0.27 |
| 10-31 15:46 | +10 stop | XRP | UP | 0.56 | 0.70 | 1.07 |
| 10-31 15:46 | +20 | XRP | UP | 0.56 | 0.77 | 1.79 |
| 10-31 15:46 | +15 | XRP | UP | 0.56 | 0.74 | 1.48 |
| 10-31 15:46 | +10 | XRP | UP | 0.56 | 0.70 | 1.07 |
| 10-31 15:46 | +5 | XRP | UP | 0.56 | 0.70 | 1.07 |
