# Range-Scalp Bot

*Updated Wed Oct 07 04:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5939 | 5147 | 792 (9) | 0 | $-1835.82 | -4.9% |
| **+10¢** | 4527 | 3593 | 934 (16) | 0 | $-1745.43 | -6.1% |
| **+15¢** | 3801 | 2811 | 990 (20) | 0 | $-1522.53 | -6.4% |
| **+20¢** | 3395 | 2361 | 1034 (27) | 0 | $-1270.25 | -6.0% |
| **+10¢ (15¢ stop)** | 7219 | 7204 | 15 (9) | 0 | $-2543.11 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 04:14 | +10 stop | BTC | UP | 0.67 | 0.78 | 0.81 |
| 10-07 04:13 | +10 stop | BTC | DOWN | 0.35 | 0.54 | 1.56 |
| 10-07 04:12 | +10 stop | SOL | UP | 0.59 | 0.93 | 3.21 |
| 10-07 04:12 | +10 stop | DOGE | DOWN | 0.55 | 0.31 | -2.73 |
| 10-07 04:12 | +15 | DOGE | DOWN | 0.55 | yes | -5.68 |
| 10-07 04:12 | +10 | DOGE | DOWN | 0.55 | yes | -5.68 |
| 10-07 04:12 | +5 | DOGE | DOWN | 0.55 | 0.61 | 0.25 |
| 10-07 04:12 | +5 | BNB | DOWN | 0.55 | yes | -5.68 |
| 10-07 04:11 | +10 stop | ETH | UP | 0.71 | 0.92 | 1.90 |
| 10-07 04:11 | +20 | ETH | UP | 0.71 | 0.92 | 1.90 |
| 10-07 04:11 | +15 | ETH | UP | 0.71 | 0.92 | 1.90 |
| 10-07 04:11 | +10 | ETH | UP | 0.71 | 0.92 | 1.90 |
| 10-07 04:11 | +5 | ETH | UP | 0.71 | 0.77 | 0.32 |
| 10-07 04:10 | +10 stop | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-07 04:10 | +10 stop | NEAR | UP | 0.66 | 0.95 | 2.67 |
| 10-07 04:10 | +15 | NEAR | UP | 0.66 | 0.95 | 2.67 |
| 10-07 04:10 | +10 | NEAR | UP | 0.66 | 0.95 | 2.67 |
| 10-07 04:10 | +5 | NEAR | UP | 0.66 | 0.72 | 0.29 |
| 10-07 04:10 | +10 stop | SOL | DOWN | 0.50 | 0.60 | 0.65 |
| 10-07 04:09 | +10 stop | BTC | UP | 0.54 | 0.33 | -2.44 |
| 10-07 04:09 | +10 stop | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-07 04:09 | +20 | DOGE | DOWN | 0.64 | yes | -6.57 |
| 10-07 04:09 | +15 | DOGE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-07 04:09 | +10 | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-07 04:09 | +5 | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 10-07 04:09 | +5 | BNB | DOWN | 0.53 | 0.59 | 0.25 |
| 10-07 04:08 | +10 stop | NEAR | DOWN | 0.61 | 0.42 | -2.25 |
| 10-07 04:07 | +10 stop | BTC | DOWN | 0.61 | 0.75 | 1.09 |
| 10-07 04:07 | +10 stop | ETH | UP | 0.58 | 0.76 | 1.49 |
| 10-07 04:07 | +10 | ETH | UP | 0.58 | 0.76 | 1.49 |
| 10-07 04:06 | +10 stop | BTC | UP | 0.63 | 0.38 | -2.84 |
| 10-07 04:06 | +10 | BTC | UP | 0.63 | 0.78 | 1.20 |
| 10-07 04:06 | +5 | BTC | UP | 0.63 | 0.69 | 0.28 |
| 10-07 04:06 | +5 | ETH | UP | 0.67 | 0.76 | 0.61 |
| 10-07 04:06 | +10 stop | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 10-07 04:06 | +10 stop | ETH | UP | 0.60 | 0.71 | 0.78 |
| 10-07 04:06 | +20 | ETH | UP | 0.60 | 0.83 | 2.03 |
| 10-07 04:06 | +15 | ETH | UP | 0.60 | 0.76 | 1.30 |
| 10-07 04:06 | +10 | ETH | UP | 0.60 | 0.71 | 0.78 |
| 10-07 04:06 | +5 | ETH | UP | 0.61 | 0.66 | 0.17 |
