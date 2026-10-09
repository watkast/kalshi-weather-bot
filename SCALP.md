# Range-Scalp Bot

*Updated Fri Oct 09 04:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8491 | 7342 | 1149 (13) | 1 | $-2796.36 | -5.2% |
| **+10¢** | 6430 | 5077 | 1353 (25) | 1 | $-2721.33 | -6.7% |
| **+15¢** | 5430 | 4006 | 1424 (37) | 1 | $-2199.73 | -6.5% |
| **+20¢** | 4831 | 3352 | 1479 (45) | 1 | $-1828.14 | -6.0% |
| **+10¢ (15¢ stop)** | 10329 | 10299 | 30 (19) | 1 | $-3801.92 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 04:00 | +10 stop | DOGE | UP | 0.64 | open |  |
| 10-09 04:00 | +20 | DOGE | UP | 0.64 | open |  |
| 10-09 04:00 | +15 | DOGE | UP | 0.64 | open |  |
| 10-09 04:00 | +10 | DOGE | UP | 0.64 | open |  |
| 10-09 04:00 | +5 | DOGE | UP | 0.64 | open |  |
| 10-09 03:57 | +10 stop | BTC | UP | 0.66 | 0.86 | 1.75 |
| 10-09 03:56 | +10 stop | XRP | UP | 0.66 | 0.81 | 1.23 |
| 10-09 03:56 | +20 | XRP | UP | 0.66 | 0.88 | 1.96 |
| 10-09 03:56 | +15 | XRP | UP | 0.66 | 0.81 | 1.23 |
| 10-09 03:56 | +10 | XRP | UP | 0.66 | 0.81 | 1.23 |
| 10-09 03:56 | +5 | XRP | UP | 0.66 | 0.75 | 0.60 |
| 10-09 03:56 | +10 stop | ETH | DOWN | 0.64 | 0.49 | -1.85 |
| 10-09 03:55 | +10 stop | ETH | UP | 0.44 | 0.58 | 1.04 |
| 10-09 03:55 | +10 stop | BTC | UP | 0.57 | 0.41 | -1.95 |
| 10-09 03:55 | +20 | BTC | UP | 0.57 | 0.86 | 2.63 |
| 10-09 03:55 | +15 | BTC | UP | 0.57 | 0.86 | 2.63 |
| 10-09 03:55 | +10 | BTC | UP | 0.57 | 0.86 | 2.63 |
| 10-09 03:55 | +5 | BTC | UP | 0.57 | 0.65 | 0.46 |
| 10-09 03:54 | +10 stop | ETH | DOWN | 0.68 | 0.46 | -2.54 |
| 10-09 03:54 | +5 | ETH | DOWN | 0.68 | yes | -6.96 |
| 10-09 03:53 | +10 stop | BNB | DOWN | 0.58 | 0.29 | -3.23 |
| 10-09 03:53 | +10 stop | SOL | UP | 0.69 | 0.86 | 1.46 |
| 10-09 03:53 | +15 | SOL | UP | 0.69 | 0.86 | 1.46 |
| 10-09 03:53 | +10 | SOL | UP | 0.69 | 0.86 | 1.46 |
| 10-09 03:53 | +5 | SOL | UP | 0.69 | 0.75 | 0.31 |
| 10-09 03:53 | +10 stop | NEAR | DOWN | 0.60 | 0.43 | -2.05 |
| 10-09 03:52 | +10 stop | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-09 03:52 | +10 stop | BNB | UP | 0.59 | 0.43 | -1.95 |
| 10-09 03:52 | +15 | BNB | UP | 0.59 | 0.76 | 1.40 |
| 10-09 03:52 | +10 | BNB | UP | 0.59 | 0.70 | 0.78 |
| 10-09 03:52 | +10 stop | ETH | DOWN | 0.70 | 0.81 | 0.84 |
| 10-09 03:50 | +10 stop | HYPE | UP | 0.58 | 0.21 | -4.00 |
| 10-09 03:50 | +10 stop | XRP | UP | 0.54 | 0.39 | -1.85 |
| 10-09 03:50 | +5 | ZEC | DOWN | 0.67 | 0.76 | 0.61 |
| 10-09 03:50 | +5 | HYPE | UP | 0.58 | no | -5.98 |
| 10-09 03:50 | +5 | BNB | UP | 0.71 | 0.76 | 0.22 |
| 10-09 03:49 | +10 stop | BNB | UP | 0.63 | 0.74 | 0.75 |
| 10-09 03:49 | +5 | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-09 03:49 | +10 stop | BNB | DOWN | 0.42 | 0.57 | 1.14 |
| 10-09 03:48 | +10 stop | BTC | DOWN | 0.58 | 0.71 | 0.97 |
