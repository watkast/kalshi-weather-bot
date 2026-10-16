# Range-Scalp Bot

*Updated Fri Oct 16 15:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19466 | 16915 | 2551 (29) | 1 | $-5867.97 | -4.8% |
| **+10¢** | 14679 | 11733 | 2946 (41) | 1 | $-5262.69 | -5.7% |
| **+15¢** | 12288 | 9118 | 3170 (60) | 0 | $-4762.88 | -6.2% |
| **+20¢** | 10901 | 7579 | 3322 (79) | 0 | $-4230.98 | -6.2% |
| **+10¢ (15¢ stop)** | 23926 | 23876 | 50 (29) | 0 | $-9155.37 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 15:49 | +5 | HYPE | DOWN | 0.71 | 0.78 | 0.42 |
| 10-16 15:49 | +10 stop | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 10-16 15:49 | +10 stop | ZEC | UP | 0.57 | 0.32 | -2.84 |
| 10-16 15:49 | +5 | ZEC | UP | 0.56 | open |  |
| 10-16 15:49 | +10 stop | BNB | DOWN | 0.60 | 0.71 | 0.78 |
| 10-16 15:49 | +5 | XRP | DOWN | 0.58 | 0.69 | 0.77 |
| 10-16 15:48 | +10 stop | DOGE | UP | 0.49 | 0.32 | -2.04 |
| 10-16 15:48 | +10 stop | HYPE | DOWN | 0.57 | 0.74 | 1.40 |
| 10-16 15:48 | +10 | HYPE | DOWN | 0.57 | 0.74 | 1.39 |
| 10-16 15:48 | +5 | HYPE | DOWN | 0.57 | 0.62 | 0.15 |
| 10-16 15:47 | +10 stop | XRP | DOWN | 0.46 | 0.59 | 0.95 |
| 10-16 15:47 | +20 | XRP | DOWN | 0.46 | 0.69 | 1.97 |
| 10-16 15:47 | +15 | XRP | DOWN | 0.46 | 0.69 | 1.97 |
| 10-16 15:47 | +10 | XRP | DOWN | 0.46 | 0.59 | 0.95 |
| 10-16 15:47 | +5 | XRP | DOWN | 0.46 | 0.54 | 0.44 |
| 10-16 15:47 | +10 | ZEC | UP | 0.67 | open |  |
| 10-16 15:47 | +5 | ZEC | UP | 0.67 | 0.75 | 0.52 |
| 10-16 15:46 | +10 stop | ZEC | UP | 0.60 | 0.70 | 0.68 |
| 10-16 15:46 | +10 | ZEC | UP | 0.57 | 0.68 | 0.76 |
| 10-16 15:46 | +5 | ZEC | UP | 0.57 | 0.68 | 0.76 |
| 10-16 15:46 | +10 stop | ZEC | DOWN | 0.44 | 0.56 | 0.84 |
| 10-16 15:46 | +20 | ZEC | DOWN | 0.44 | 0.66 | 1.86 |
| 10-16 15:46 | +15 | ZEC | DOWN | 0.45 | 0.66 | 1.75 |
| 10-16 15:46 | +10 | ZEC | DOWN | 0.45 | 0.56 | 0.73 |
| 10-16 15:46 | +5 | ZEC | DOWN | 0.45 | 0.56 | 0.71 |
| 10-16 15:46 | +10 stop | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 10-16 15:46 | +20 | NEAR | DOWN | 0.64 | 0.85 | 1.84 |
| 10-16 15:46 | +15 | NEAR | DOWN | 0.64 | 0.82 | 1.52 |
| 10-16 15:46 | +10 | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 10-16 15:46 | +5 | NEAR | DOWN | 0.64 | 0.72 | 0.46 |
| 10-16 15:46 | +10 stop | BNB | DOWN | 0.61 | 0.46 | -1.85 |
| 10-16 15:46 | +20 | BNB | DOWN | 0.61 | 0.89 | 2.56 |
| 10-16 15:46 | +15 | BNB | DOWN | 0.61 | 0.78 | 1.40 |
| 10-16 15:46 | +10 | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 10-16 15:46 | +5 | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 10-16 15:46 | +10 stop | SOL | DOWN | 0.57 | 0.42 | -1.86 |
| 10-16 15:46 | +20 | SOL | DOWN | 0.57 | 0.77 | 1.69 |
| 10-16 15:46 | +15 | SOL | DOWN | 0.57 | 0.76 | 1.59 |
| 10-16 15:46 | +10 | SOL | DOWN | 0.59 | 0.76 | 1.40 |
| 10-16 15:46 | +5 | SOL | DOWN | 0.59 | 0.64 | 0.16 |
