# Range-Scalp Bot

*Updated Sat Oct 03 03:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 134 | 114 | 20 (1) | 4 | $-51.86 | -6.0% |
| **+10¢** | 114 | 94 | 20 (1) | 4 | $-16.82 | -2.3% |
| **+15¢** | 88 | 67 | 21 (1) | 5 | $-23.28 | -4.2% |
| **+20¢** | 295 | 207 | 88 (2) | 7 | $-94.86 | -5.1% |
| **+10¢ (15¢ stop)** | 190 | 190 | 0 (0) | 3 | $-87.37 | -7.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 03:36 | +5 | HYPE | DOWN | 0.62 | open |  |
| 10-03 03:36 | +10 stop | NEAR | DOWN | 0.60 | open |  |
| 10-03 03:35 | +10 stop | HYPE | DOWN | 0.60 | open |  |
| 10-03 03:35 | +10 stop | NEAR | UP | 0.57 | 0.42 | -1.86 |
| 10-03 03:34 | +5 | ETH | DOWN | 0.65 | 0.82 | 1.43 |
| 10-03 03:34 | +10 stop | ZEC | DOWN | 0.66 | 0.78 | 0.86 |
| 10-03 03:34 | +20 | ZEC | DOWN | 0.64 | 0.84 | 1.74 |
| 10-03 03:34 | +15 | ZEC | DOWN | 0.64 | 0.84 | 1.74 |
| 10-03 03:34 | +10 | ZEC | DOWN | 0.64 | 0.75 | 0.80 |
| 10-03 03:34 | +5 | ZEC | DOWN | 0.64 | 0.72 | 0.49 |
| 10-03 03:34 | +10 stop | BNB | UP | 0.70 | open |  |
| 10-03 03:33 | +10 stop | ETH | DOWN | 0.66 | 0.82 | 1.33 |
| 10-03 03:33 | +10 | ETH | DOWN | 0.66 | 0.82 | 1.33 |
| 10-03 03:33 | +5 | ETH | DOWN | 0.66 | 0.73 | 0.40 |
| 10-03 03:33 | +10 stop | NEAR | DOWN | 0.64 | 0.43 | -2.45 |
| 10-03 03:32 | +10 stop | BNB | UP | 0.63 | 0.78 | 1.20 |
| 10-03 03:32 | +5 | SOL | UP | 0.68 | 0.78 | 0.71 |
| 10-03 03:31 | +10 stop | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 10-03 03:31 | +20 | ETH | DOWN | 0.69 | open |  |
| 10-03 03:31 | +15 | ETH | DOWN | 0.69 | open |  |
| 10-03 03:31 | +10 | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 10-03 03:31 | +5 | ETH | DOWN | 0.69 | 0.78 | 0.62 |
| 10-03 03:31 | +10 stop | ZEC | DOWN | 0.69 | 0.81 | 0.96 |
| 10-03 03:31 | +10 | ZEC | DOWN | 0.69 | 0.81 | 0.96 |
| 10-03 03:31 | +5 | ZEC | DOWN | 0.69 | 0.75 | 0.33 |
| 10-03 03:31 | +10 stop | DOGE | DOWN | 0.53 | 0.38 | -1.85 |
| 10-03 03:31 | +20 | DOGE | DOWN | 0.53 | open |  |
| 10-03 03:31 | +15 | DOGE | DOWN | 0.53 | open |  |
| 10-03 03:31 | +10 | DOGE | DOWN | 0.53 | open |  |
| 10-03 03:31 | +5 | DOGE | DOWN | 0.53 | open |  |
| 10-03 03:31 | +10 stop | XRP | UP | 0.62 | 0.76 | 1.10 |
| 10-03 03:31 | +20 | XRP | UP | 0.62 | open |  |
| 10-03 03:31 | +15 | XRP | UP | 0.61 | 0.81 | 1.71 |
| 10-03 03:31 | +10 | XRP | UP | 0.61 | 0.76 | 1.19 |
| 10-03 03:31 | +5 | XRP | UP | 0.61 | 0.76 | 1.19 |
| 10-03 03:31 | +10 stop | SOL | UP | 0.62 | 0.78 | 1.30 |
| 10-03 03:31 | +20 | SOL | UP | 0.62 | 0.82 | 1.72 |
| 10-03 03:31 | +15 | SOL | UP | 0.62 | 0.78 | 1.30 |
| 10-03 03:31 | +10 | SOL | UP | 0.62 | 0.78 | 1.30 |
| 10-03 03:31 | +5 | SOL | UP | 0.62 | 0.69 | 0.38 |
