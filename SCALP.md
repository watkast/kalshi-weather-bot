# Range-Scalp Bot

*Updated Sun Oct 11 10:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11817 | 10192 | 1625 (24) | 1 | $-3975.91 | -5.3% |
| **+10¢** | 8957 | 7069 | 1888 (37) | 3 | $-3779.93 | -6.7% |
| **+15¢** | 7542 | 5538 | 2004 (54) | 3 | $-3243.37 | -6.8% |
| **+20¢** | 6720 | 4637 | 2083 (67) | 3 | $-2720.98 | -6.4% |
| **+10¢ (15¢ stop)** | 14530 | 14489 | 41 (25) | 1 | $-5739.73 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 10:42 | +5 | NEAR | UP | 0.60 | open |  |
| 10-11 10:42 | +10 stop | NEAR | UP | 0.58 | open |  |
| 10-11 10:42 | +15 | NEAR | UP | 0.58 | open |  |
| 10-11 10:42 | +10 | NEAR | UP | 0.58 | open |  |
| 10-11 10:42 | +5 | NEAR | UP | 0.58 | 0.64 | 0.25 |
| 10-11 10:40 | +10 stop | NEAR | UP | 0.51 | 0.64 | 0.95 |
| 10-11 10:38 | +10 stop | NEAR | DOWN | 0.67 | 0.49 | -2.14 |
| 10-11 10:34 | +10 stop | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-11 10:34 | +10 | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-11 10:34 | +5 | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-11 10:34 | +10 stop | NEAR | DOWN | 0.67 | 0.48 | -2.24 |
| 10-11 10:32 | +10 stop | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-11 10:32 | +20 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 10-11 10:32 | +15 | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 10-11 10:32 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-11 10:32 | +5 | SOL | DOWN | 0.67 | 0.74 | 0.40 |
| 10-11 10:32 | +5 | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 10-11 10:32 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-11 10:32 | +20 | BTC | DOWN | 0.64 | 0.85 | 1.84 |
| 10-11 10:32 | +15 | BTC | DOWN | 0.64 | 0.79 | 1.21 |
| 10-11 10:32 | +10 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-11 10:32 | +5 | BTC | DOWN | 0.64 | 0.71 | 0.38 |
| 10-11 10:32 | +5 | NEAR | UP | 0.58 | 0.64 | 0.26 |
| 10-11 10:32 | +10 stop | ZEC | DOWN | 0.71 | 0.85 | 1.16 |
| 10-11 10:32 | +20 | ZEC | DOWN | 0.71 | 0.91 | 1.83 |
| 10-11 10:32 | +15 | ZEC | DOWN | 0.71 | 0.91 | 1.73 |
| 10-11 10:32 | +10 | ZEC | DOWN | 0.71 | 0.85 | 1.16 |
| 10-11 10:32 | +5 | ZEC | DOWN | 0.71 | 0.85 | 1.16 |
| 10-11 10:32 | +5 | ETH | DOWN | 0.69 | 0.76 | 0.42 |
| 10-11 10:31 | +5 | BNB | DOWN | 0.68 | 0.77 | 0.61 |
| 10-11 10:31 | +10 stop | DOGE | DOWN | 0.55 | 0.77 | 1.89 |
| 10-11 10:31 | +20 | DOGE | DOWN | 0.54 | 0.77 | 1.97 |
| 10-11 10:31 | +15 | DOGE | DOWN | 0.54 | 0.77 | 1.97 |
| 10-11 10:31 | +10 | DOGE | DOWN | 0.54 | 0.77 | 1.97 |
| 10-11 10:31 | +5 | DOGE | DOWN | 0.54 | 0.60 | 0.23 |
| 10-11 10:31 | +10 stop | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 10-11 10:31 | +20 | ETH | DOWN | 0.59 | 0.85 | 2.34 |
| 10-11 10:31 | +15 | ETH | DOWN | 0.59 | 0.76 | 1.40 |
| 10-11 10:31 | +10 | ETH | DOWN | 0.59 | 0.76 | 1.40 |
| 10-11 10:31 | +5 | ETH | DOWN | 0.59 | 0.67 | 0.47 |
