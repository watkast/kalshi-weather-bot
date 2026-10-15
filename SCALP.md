# Range-Scalp Bot

*Updated Thu Oct 15 11:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17419 | 15119 | 2300 (28) | 3 | $-5319.60 | -4.8% |
| **+10¢** | 13159 | 10496 | 2663 (40) | 4 | $-4836.76 | -5.8% |
| **+15¢** | 11051 | 8192 | 2859 (59) | 7 | $-4289.41 | -6.2% |
| **+20¢** | 9822 | 6829 | 2993 (77) | 7 | $-3735.61 | -6.1% |
| **+10¢ (15¢ stop)** | 21434 | 21384 | 50 (29) | 0 | $-8291.11 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 11:37 | +10 stop | DOGE | UP | 0.70 | 0.54 | -1.93 |
| 10-15 11:37 | +5 | DOGE | UP | 0.70 | 0.77 | 0.42 |
| 10-15 11:36 | +10 stop | ETH | UP | 0.64 | 0.74 | 0.69 |
| 10-15 11:36 | +10 stop | SOL | UP | 0.68 | 0.80 | 0.92 |
| 10-15 11:36 | +10 | SOL | UP | 0.68 | 0.80 | 0.92 |
| 10-15 11:36 | +5 | SOL | UP | 0.68 | 0.77 | 0.61 |
| 10-15 11:35 | +10 stop | BTC | UP | 0.64 | 0.81 | 1.42 |
| 10-15 11:35 | +10 stop | XRP | UP | 0.62 | 0.76 | 1.10 |
| 10-15 11:35 | +20 | XRP | UP | 0.62 | 0.87 | 2.25 |
| 10-15 11:35 | +15 | XRP | UP | 0.62 | 0.78 | 1.30 |
| 10-15 11:35 | +10 | XRP | UP | 0.62 | 0.76 | 1.10 |
| 10-15 11:35 | +5 | XRP | UP | 0.62 | 0.76 | 1.10 |
| 10-15 11:34 | +10 stop | HYPE | UP | 0.56 | 0.72 | 1.23 |
| 10-15 11:34 | +10 stop | ETH | UP | 0.70 | 0.49 | -2.43 |
| 10-15 11:34 | +10 stop | DOGE | DOWN | 0.54 | 0.30 | -2.73 |
| 10-15 11:33 | +10 stop | SOL | UP | 0.60 | 0.70 | 0.68 |
| 10-15 11:33 | +10 | SOL | UP | 0.60 | 0.70 | 0.68 |
| 10-15 11:33 | +5 | SOL | UP | 0.60 | 0.70 | 0.68 |
| 10-15 11:33 | +10 stop | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 10-15 11:33 | +10 | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 10-15 11:33 | +5 | NEAR | UP | 0.66 | 0.72 | 0.29 |
| 10-15 11:33 | +10 stop | ZEC | UP | 0.60 | 0.74 | 1.12 |
| 10-15 11:32 | +10 stop | ETH | UP | 0.69 | 0.54 | -1.83 |
| 10-15 11:32 | +10 stop | BTC | UP | 0.66 | 0.50 | -1.94 |
| 10-15 11:32 | +10 stop | HYPE | UP | 0.65 | 0.49 | -1.94 |
| 10-15 11:32 | +10 stop | DOGE | UP | 0.67 | 0.48 | -2.24 |
| 10-15 11:32 | +10 | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 10-15 11:32 | +5 | DOGE | UP | 0.67 | 0.75 | 0.50 |
| 10-15 11:32 | +5 | ETH | UP | 0.71 | 0.79 | 0.53 |
| 10-15 11:31 | +10 stop | ZEC | DOWN | 0.58 | 0.29 | -3.26 |
| 10-15 11:31 | +20 | ZEC | DOWN | 0.58 | open |  |
| 10-15 11:31 | +15 | ZEC | DOWN | 0.58 | open |  |
| 10-15 11:31 | +10 | ZEC | DOWN | 0.58 | open |  |
| 10-15 11:31 | +5 | ZEC | DOWN | 0.58 | open |  |
| 10-15 11:31 | +10 stop | DOGE | DOWN | 0.57 | 0.68 | 0.80 |
| 10-15 11:31 | +20 | DOGE | DOWN | 0.57 | open |  |
| 10-15 11:31 | +15 | DOGE | DOWN | 0.57 | open |  |
| 10-15 11:31 | +10 | DOGE | DOWN | 0.57 | 0.68 | 0.76 |
| 10-15 11:31 | +5 | DOGE | DOWN | 0.56 | 0.68 | 0.86 |
| 10-15 11:31 | +10 stop | ETH | DOWN | 0.57 | 0.33 | -2.74 |
