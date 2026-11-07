# Range-Scalp Bot

*Updated Sat Nov 07 16:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51224 | 44655 | 6569 (79) | 2 | $-14308.34 | -4.4% |
| **+10¢** | 38240 | 30583 | 7657 (105) | 1 | $-13299.05 | -5.5% |
| **+15¢** | 32014 | 23761 | 8253 (134) | 1 | $-12218.95 | -6.1% |
| **+20¢** | 28474 | 19824 | 8650 (177) | 1 | $-10782.75 | -6.0% |
| **+10¢ (15¢ stop)** | 62408 | 62305 | 103 (61) | 0 | $-23103.28 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 16:57 | +10 stop | BNB | UP | 0.64 | 0.44 | -2.35 |
| 11-07 16:57 | +5 | BNB | UP | 0.64 | open |  |
| 11-07 16:56 | +10 stop | DOGE | DOWN | 0.54 | 0.71 | 1.37 |
| 11-07 16:56 | +20 | DOGE | DOWN | 0.54 | 0.82 | 2.51 |
| 11-07 16:56 | +15 | DOGE | DOWN | 0.54 | 0.71 | 1.37 |
| 11-07 16:56 | +10 | DOGE | DOWN | 0.54 | 0.71 | 1.37 |
| 11-07 16:56 | +5 | DOGE | DOWN | 0.54 | 0.71 | 1.37 |
| 11-07 16:56 | +10 stop | ETH | DOWN | 0.62 | 0.75 | 0.99 |
| 11-07 16:56 | +15 | ETH | DOWN | 0.62 | 0.95 | 3.07 |
| 11-07 16:56 | +10 | ETH | DOWN | 0.62 | 0.75 | 0.99 |
| 11-07 16:56 | +5 | ETH | DOWN | 0.62 | 0.71 | 0.58 |
| 11-07 16:56 | +10 stop | XRP | UP | 0.69 | 0.53 | -1.93 |
| 11-07 16:56 | +20 | XRP | UP | 0.69 | open |  |
| 11-07 16:56 | +15 | XRP | UP | 0.69 | open |  |
| 11-07 16:56 | +10 | XRP | UP | 0.69 | open |  |
| 11-07 16:56 | +5 | XRP | UP | 0.69 | open |  |
| 11-07 16:55 | +10 stop | BTC | DOWN | 0.63 | 0.86 | 2.04 |
| 11-07 16:55 | +20 | BTC | DOWN | 0.63 | 0.86 | 2.04 |
| 11-07 16:55 | +15 | BTC | DOWN | 0.63 | 0.86 | 2.04 |
| 11-07 16:55 | +10 | BTC | DOWN | 0.63 | 0.86 | 2.04 |
| 11-07 16:55 | +5 | BTC | DOWN | 0.63 | 0.86 | 2.04 |
| 11-07 16:55 | +10 stop | XRP | DOWN | 0.36 | 0.67 | 2.77 |
| 11-07 16:55 | +20 | XRP | DOWN | 0.37 | 0.67 | 2.67 |
| 11-07 16:55 | +15 | XRP | DOWN | 0.38 | 0.67 | 2.57 |
| 11-07 16:55 | +10 | XRP | DOWN | 0.37 | 0.67 | 2.67 |
| 11-07 16:55 | +5 | XRP | DOWN | 0.38 | 0.67 | 2.57 |
| 11-07 16:54 | +5 | BNB | UP | 0.66 | 0.73 | 0.40 |
| 11-07 16:53 | +10 stop | BNB | UP | 0.65 | 0.79 | 1.12 |
| 11-07 16:53 | +5 | BNB | UP | 0.65 | 0.72 | 0.39 |
| 11-07 16:50 | +10 stop | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 11-07 16:49 | +5 | BNB | DOWN | 0.67 | 0.76 | 0.61 |
| 11-07 16:47 | +10 stop | BNB | DOWN | 0.70 | 0.55 | -1.83 |
| 11-07 16:47 | +20 | BNB | DOWN | 0.70 | 0.90 | 1.78 |
| 11-07 16:47 | +15 | BNB | DOWN | 0.70 | 0.90 | 1.78 |
| 11-07 16:47 | +10 | BNB | DOWN | 0.70 | 0.90 | 1.78 |
| 11-07 16:47 | +5 | BNB | DOWN | 0.70 | 0.76 | 0.27 |
| 11-07 16:46 | +10 stop | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 11-07 16:46 | +20 | ETH | DOWN | 0.65 | 0.95 | 2.78 |
| 11-07 16:46 | +15 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 11-07 16:46 | +10 | ETH | DOWN | 0.66 | 0.78 | 0.91 |
