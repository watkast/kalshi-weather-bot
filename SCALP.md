# Range-Scalp Bot

*Updated Wed Oct 07 21:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6838 | 5938 | 900 (10) | 4 | $-2070.01 | -4.8% |
| **+10¢** | 5189 | 4133 | 1056 (17) | 4 | $-1946.60 | -6.0% |
| **+15¢** | 4345 | 3234 | 1111 (21) | 5 | $-1623.32 | -6.0% |
| **+20¢** | 3883 | 2725 | 1158 (28) | 5 | $-1293.15 | -5.3% |
| **+10¢ (15¢ stop)** | 8292 | 8275 | 17 (10) | 0 | $-2947.48 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 21:24 | +10 stop | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-07 21:24 | +10 stop | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
| 10-07 21:24 | +10 stop | HYPE | UP | 0.67 | 0.40 | -3.07 |
| 10-07 21:23 | +10 stop | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 10-07 21:22 | +10 stop | ETH | UP | 0.57 | 0.37 | -2.35 |
| 10-07 21:22 | +10 stop | DOGE | DOWN | 0.66 | 0.82 | 1.33 |
| 10-07 21:22 | +10 | DOGE | DOWN | 0.66 | 0.82 | 1.33 |
| 10-07 21:22 | +5 | DOGE | DOWN | 0.66 | 0.72 | 0.29 |
| 10-07 21:22 | +10 stop | ZEC | DOWN | 0.68 | 0.50 | -2.13 |
| 10-07 21:22 | +10 stop | HYPE | DOWN | 0.61 | 0.45 | -1.95 |
| 10-07 21:22 | +15 | HYPE | DOWN | 0.61 | open |  |
| 10-07 21:22 | +10 | HYPE | DOWN | 0.61 | open |  |
| 10-07 21:22 | +5 | HYPE | DOWN | 0.61 | open |  |
| 10-07 21:21 | +10 stop | NEAR | DOWN | 0.69 | 0.86 | 1.46 |
| 10-07 21:21 | +20 | NEAR | DOWN | 0.69 | 0.97 | 2.66 |
| 10-07 21:21 | +15 | NEAR | DOWN | 0.69 | 0.86 | 1.45 |
| 10-07 21:21 | +10 | NEAR | DOWN | 0.69 | 0.86 | 1.45 |
| 10-07 21:21 | +5 | NEAR | DOWN | 0.69 | 0.86 | 1.45 |
| 10-07 21:20 | +5 | ZEC | DOWN | 0.68 | 0.74 | 0.30 |
| 10-07 21:20 | +5 | XRP | DOWN | 0.65 | open |  |
| 10-07 21:20 | +5 | ETH | DOWN | 0.70 | open |  |
| 10-07 21:20 | +10 stop | SOL | DOWN | 0.65 | 0.50 | -1.84 |
| 10-07 21:20 | +5 | BNB | DOWN | 0.68 | 0.73 | 0.20 |
| 10-07 21:19 | +10 stop | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-07 21:19 | +5 | ZEC | DOWN | 0.59 | 0.64 | 0.16 |
| 10-07 21:19 | +10 stop | ETH | DOWN | 0.61 | 0.41 | -2.34 |
| 10-07 21:19 | +10 stop | BTC | UP | 0.67 | 0.77 | 0.71 |
| 10-07 21:19 | +10 | BTC | UP | 0.67 | 0.77 | 0.71 |
| 10-07 21:19 | +10 stop | DOGE | DOWN | 0.65 | 0.75 | 0.73 |
| 10-07 21:19 | +10 stop | HYPE | DOWN | 0.59 | 0.79 | 1.71 |
| 10-07 21:19 | +5 | SOL | UP | 0.60 | open |  |
| 10-07 21:18 | +5 | ZEC | UP | 0.49 | 0.60 | 0.75 |
| 10-07 21:18 | +10 stop | ETH | UP | 0.55 | 0.40 | -1.85 |
| 10-07 21:18 | +5 | BTC | UP | 0.70 | 0.75 | 0.21 |
| 10-07 21:17 | +10 stop | SOL | UP | 0.67 | 0.39 | -3.10 |
| 10-07 21:17 | +20 | SOL | UP | 0.67 | open |  |
| 10-07 21:17 | +15 | SOL | UP | 0.67 | open |  |
| 10-07 21:17 | +10 | SOL | UP | 0.67 | open |  |
| 10-07 21:17 | +5 | SOL | UP | 0.66 | 0.71 | 0.19 |
| 10-07 21:17 | +10 stop | NEAR | DOWN | 0.61 | 0.74 | 0.99 |
