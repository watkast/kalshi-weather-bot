# Range-Scalp Bot

*Updated Fri Oct 16 17:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19564 | 17000 | 2564 (29) | 3 | $-5904.16 | -4.8% |
| **+10¢** | 14751 | 11789 | 2962 (41) | 3 | $-5306.83 | -5.7% |
| **+15¢** | 12347 | 9162 | 3185 (60) | 3 | $-4786.87 | -6.2% |
| **+20¢** | 10958 | 7621 | 3337 (79) | 3 | $-4238.54 | -6.2% |
| **+10¢ (15¢ stop)** | 24059 | 24009 | 50 (29) | 0 | $-9198.71 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 17:51 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.82 |
| 10-16 17:49 | +5 | DOGE | DOWN | 0.71 | 0.76 | 0.22 |
| 10-16 17:48 | +10 stop | HYPE | DOWN | 0.55 | 0.65 | 0.66 |
| 10-16 17:48 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
| 10-16 17:48 | +10 stop | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 10-16 17:48 | +5 | BNB | DOWN | 0.71 | 0.77 | 0.33 |
| 10-16 17:48 | +10 stop | DOGE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-16 17:48 | +20 | DOGE | DOWN | 0.60 | 0.81 | 1.82 |
| 10-16 17:48 | +15 | DOGE | DOWN | 0.60 | 0.76 | 1.30 |
| 10-16 17:48 | +10 | DOGE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-16 17:48 | +5 | DOGE | DOWN | 0.60 | 0.67 | 0.37 |
| 10-16 17:47 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 10-16 17:47 | +20 | SOL | DOWN | 0.61 | 0.81 | 1.72 |
| 10-16 17:47 | +15 | SOL | DOWN | 0.61 | 0.78 | 1.40 |
| 10-16 17:47 | +10 | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 10-16 17:47 | +5 | SOL | DOWN | 0.61 | 0.68 | 0.37 |
| 10-16 17:47 | +10 stop | BNB | DOWN | 0.61 | 0.73 | 0.89 |
| 10-16 17:47 | +20 | BNB | DOWN | 0.61 | 0.82 | 1.82 |
| 10-16 17:47 | +15 | BNB | DOWN | 0.61 | 0.77 | 1.30 |
| 10-16 17:47 | +10 | BNB | DOWN | 0.61 | 0.73 | 0.89 |
| 10-16 17:47 | +5 | BNB | DOWN | 0.61 | 0.66 | 0.17 |
| 10-16 17:47 | +10 stop | BTC | DOWN | 0.62 | 0.76 | 1.10 |
| 10-16 17:47 | +20 | BTC | DOWN | 0.62 | 0.84 | 1.93 |
| 10-16 17:47 | +15 | BTC | DOWN | 0.62 | 0.78 | 1.30 |
| 10-16 17:47 | +10 | BTC | DOWN | 0.62 | 0.76 | 1.10 |
| 10-16 17:47 | +5 | BTC | DOWN | 0.62 | 0.71 | 0.58 |
| 10-16 17:46 | +10 stop | XRP | DOWN | 0.58 | 0.72 | 1.07 |
| 10-16 17:46 | +20 | XRP | DOWN | 0.59 | 0.79 | 1.71 |
| 10-16 17:46 | +15 | XRP | DOWN | 0.59 | 0.77 | 1.50 |
| 10-16 17:46 | +10 | XRP | DOWN | 0.59 | 0.72 | 0.98 |
| 10-16 17:46 | +5 | XRP | DOWN | 0.59 | 0.65 | 0.27 |
| 10-16 17:46 | +10 stop | NEAR | DOWN | 0.64 | 0.77 | 1.00 |
| 10-16 17:46 | +20 | NEAR | DOWN | 0.64 | 0.84 | 1.73 |
| 10-16 17:46 | +15 | NEAR | DOWN | 0.64 | 0.79 | 1.21 |
| 10-16 17:46 | +10 | NEAR | DOWN | 0.64 | 0.77 | 1.00 |
| 10-16 17:46 | +5 | NEAR | DOWN | 0.64 | 0.71 | 0.38 |
| 10-16 17:46 | +10 stop | ZEC | UP | 0.51 | 0.32 | -2.23 |
| 10-16 17:46 | +20 | ZEC | UP | 0.51 | open |  |
| 10-16 17:46 | +15 | ZEC | UP | 0.51 | open |  |
| 10-16 17:46 | +10 | ZEC | UP | 0.51 | open |  |
