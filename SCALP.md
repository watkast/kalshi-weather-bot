# Range-Scalp Bot

*Updated Wed Nov 11 12:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55799 | 48665 | 7134 (94) | 0 | $-15211.94 | -4.3% |
| **+10¢** | 41691 | 33372 | 8319 (124) | 3 | $-14133.19 | -5.4% |
| **+15¢** | 34957 | 25982 | 8975 (158) | 3 | $-12902.41 | -5.9% |
| **+20¢** | 31134 | 21720 | 9414 (208) | 3 | $-11265.12 | -5.8% |
| **+10¢ (15¢ stop)** | 67972 | 67851 | 121 (73) | 3 | $-25000.01 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 12:15 | +10 stop | ETH | UP | 0.53 | open |  |
| 11-11 12:15 | +20 | ETH | UP | 0.53 | open |  |
| 11-11 12:15 | +15 | ETH | UP | 0.53 | open |  |
| 11-11 12:15 | +10 | ETH | UP | 0.53 | open |  |
| 11-11 12:15 | +5 | ETH | UP | 0.53 | 0.59 | 0.25 |
| 11-11 12:15 | +10 stop | BTC | UP | 0.58 | open |  |
| 11-11 12:15 | +20 | BTC | UP | 0.58 | open |  |
| 11-11 12:15 | +15 | BTC | UP | 0.58 | open |  |
| 11-11 12:15 | +10 | BTC | UP | 0.57 | open |  |
| 11-11 12:15 | +5 | BTC | UP | 0.57 | 0.65 | 0.46 |
| 11-11 12:15 | +10 stop | ZEC | UP | 0.54 | open |  |
| 11-11 12:15 | +20 | ZEC | UP | 0.54 | open |  |
| 11-11 12:15 | +15 | ZEC | UP | 0.54 | open |  |
| 11-11 12:15 | +10 | ZEC | UP | 0.54 | open |  |
| 11-11 12:15 | +5 | ZEC | UP | 0.53 | 0.58 | 0.14 |
| 11-11 12:12 | +10 stop | ZEC | DOWN | 0.60 | 0.79 | 1.61 |
| 11-11 12:12 | +10 stop | ZEC | UP | 0.65 | 0.30 | -3.81 |
| 11-11 12:10 | +10 stop | BNB | DOWN | 0.62 | 0.46 | -1.95 |
| 11-11 12:10 | +20 | BNB | DOWN | 0.62 | 0.93 | 2.89 |
| 11-11 12:10 | +15 | BNB | DOWN | 0.62 | 0.93 | 2.89 |
| 11-11 12:10 | +10 | BNB | DOWN | 0.62 | 0.93 | 2.89 |
| 11-11 12:10 | +5 | BNB | DOWN | 0.62 | 0.93 | 2.89 |
| 11-11 12:09 | +10 stop | DOGE | UP | 0.61 | 0.74 | 0.99 |
| 11-11 12:09 | +10 stop | ZEC | UP | 0.63 | 0.44 | -2.25 |
| 11-11 12:09 | +20 | ZEC | UP | 0.63 | no | -6.47 |
| 11-11 12:09 | +15 | ZEC | UP | 0.63 | no | -6.47 |
| 11-11 12:09 | +10 | ZEC | UP | 0.63 | no | -6.47 |
| 11-11 12:09 | +5 | ZEC | UP | 0.64 | no | -6.57 |
| 11-11 12:09 | +10 stop | NEAR | UP | 0.66 | 0.76 | 0.71 |
| 11-11 12:09 | +10 | NEAR | UP | 0.66 | 0.76 | 0.71 |
| 11-11 12:09 | +5 | NEAR | UP | 0.66 | 0.74 | 0.50 |
| 11-11 12:08 | +10 stop | DOGE | DOWN | 0.61 | 0.38 | -2.64 |
| 11-11 12:08 | +15 | DOGE | DOWN | 0.61 | 0.94 | 3.03 |
| 11-11 12:08 | +10 | DOGE | DOWN | 0.61 | 0.94 | 3.03 |
| 11-11 12:08 | +5 | DOGE | DOWN | 0.61 | 0.94 | 3.03 |
| 11-11 12:02 | +5 | SOL | DOWN | 0.68 | 0.75 | 0.40 |
| 11-11 12:02 | +5 | XRP | DOWN | 0.69 | 0.77 | 0.52 |
| 11-11 12:02 | +10 stop | BTC | DOWN | 0.64 | 0.77 | 1.00 |
| 11-11 12:02 | +20 | BTC | DOWN | 0.64 | 0.92 | 2.56 |
| 11-11 12:02 | +15 | BTC | DOWN | 0.64 | 0.92 | 2.56 |
