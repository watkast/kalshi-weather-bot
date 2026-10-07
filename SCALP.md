# Range-Scalp Bot

*Updated Wed Oct 07 03:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5892 | 5103 | 789 (9) | 1 | $-1843.62 | -5.0% |
| **+10¢** | 4488 | 3558 | 930 (16) | 4 | $-1769.60 | -6.3% |
| **+15¢** | 3768 | 2782 | 986 (20) | 3 | $-1554.18 | -6.6% |
| **+20¢** | 3365 | 2336 | 1029 (27) | 4 | $-1299.79 | -6.2% |
| **+10¢ (15¢ stop)** | 7158 | 7143 | 15 (9) | 3 | $-2539.17 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 03:35 | +5 | NEAR | UP | 0.56 | 0.67 | 0.76 |
| 10-07 03:34 | +5 | NEAR | UP | 0.58 | 0.67 | 0.56 |
| 10-07 03:33 | +10 stop | SOL | UP | 0.67 | open |  |
| 10-07 03:33 | +10 stop | ETH | UP | 0.69 | open |  |
| 10-07 03:33 | +10 | ETH | UP | 0.69 | open |  |
| 10-07 03:33 | +5 | ETH | UP | 0.69 | 0.74 | 0.21 |
| 10-07 03:32 | +5 | BTC | UP | 0.63 | 0.69 | 0.28 |
| 10-07 03:32 | +10 stop | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 10-07 03:32 | +10 | DOGE | UP | 0.66 | 0.78 | 0.89 |
| 10-07 03:32 | +10 stop | HYPE | UP | 0.68 | 0.78 | 0.71 |
| 10-07 03:32 | +10 | HYPE | UP | 0.68 | 0.78 | 0.71 |
| 10-07 03:32 | +5 | HYPE | UP | 0.68 | 0.78 | 0.71 |
| 10-07 03:32 | +10 stop | NEAR | DOWN | 0.43 | 0.26 | -2.02 |
| 10-07 03:32 | +20 | NEAR | DOWN | 0.43 | open |  |
| 10-07 03:32 | +15 | NEAR | DOWN | 0.43 | open |  |
| 10-07 03:32 | +10 | NEAR | DOWN | 0.43 | open |  |
| 10-07 03:32 | +5 | NEAR | DOWN | 0.43 | 0.52 | 0.54 |
| 10-07 03:32 | +5 | DOGE | UP | 0.70 | 0.75 | 0.21 |
| 10-07 03:32 | +10 stop | SOL | UP | 0.66 | 0.50 | -1.94 |
| 10-07 03:32 | +10 stop | ZEC | UP | 0.62 | open |  |
| 10-07 03:32 | +20 | ZEC | UP | 0.63 | open |  |
| 10-07 03:32 | +15 | ZEC | UP | 0.63 | open |  |
| 10-07 03:32 | +10 | ZEC | UP | 0.63 | open |  |
| 10-07 03:32 | +5 | ZEC | UP | 0.63 | 0.69 | 0.28 |
| 10-07 03:31 | +10 stop | SOL | DOWN | 0.57 | 0.38 | -2.25 |
| 10-07 03:31 | +20 | SOL | DOWN | 0.57 | open |  |
| 10-07 03:31 | +15 | SOL | DOWN | 0.57 | open |  |
| 10-07 03:31 | +10 | SOL | DOWN | 0.57 | open |  |
| 10-07 03:31 | +5 | SOL | DOWN | 0.57 | open |  |
| 10-07 03:31 | +10 stop | BTC | UP | 0.61 | 0.71 | 0.68 |
| 10-07 03:31 | +20 | BTC | UP | 0.61 | 0.81 | 1.72 |
| 10-07 03:31 | +15 | BTC | UP | 0.61 | 0.76 | 1.20 |
| 10-07 03:31 | +10 | BTC | UP | 0.61 | 0.71 | 0.68 |
| 10-07 03:31 | +5 | BTC | UP | 0.61 | 0.67 | 0.27 |
| 10-07 03:31 | +10 stop | BNB | UP | 0.60 | 0.70 | 0.68 |
| 10-07 03:31 | +20 | BNB | UP | 0.60 | 0.80 | 1.71 |
| 10-07 03:31 | +15 | BNB | UP | 0.60 | 0.75 | 1.19 |
| 10-07 03:31 | +10 | BNB | UP | 0.60 | 0.70 | 0.68 |
| 10-07 03:31 | +5 | BNB | UP | 0.60 | 0.70 | 0.68 |
| 10-07 03:31 | +10 stop | DOGE | UP | 0.56 | 0.66 | 0.66 |
