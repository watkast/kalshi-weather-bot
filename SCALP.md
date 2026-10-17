# Range-Scalp Bot

*Updated Sat Oct 17 16:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21189 | 18445 | 2744 (29) | 2 | $-6162.29 | -4.6% |
| **+10¢** | 15950 | 12780 | 3170 (41) | 2 | $-5501.02 | -5.5% |
| **+15¢** | 13333 | 9918 | 3415 (61) | 4 | $-4999.38 | -6.0% |
| **+20¢** | 11819 | 8242 | 3577 (80) | 5 | $-4426.75 | -6.0% |
| **+10¢ (15¢ stop)** | 26025 | 25975 | 50 (29) | 2 | $-9896.93 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 16:03 | +10 stop | BNB | DOWN | 0.64 | open |  |
| 10-17 16:03 | +10 stop | SOL | UP | 0.64 | 0.79 | 1.21 |
| 10-17 16:03 | +20 | SOL | UP | 0.64 | open |  |
| 10-17 16:03 | +15 | SOL | UP | 0.64 | 0.79 | 1.21 |
| 10-17 16:03 | +10 | SOL | UP | 0.64 | 0.79 | 1.21 |
| 10-17 16:03 | +5 | SOL | UP | 0.64 | 0.79 | 1.21 |
| 10-17 16:03 | +10 stop | ETH | UP | 0.66 | 0.79 | 1.02 |
| 10-17 16:03 | +20 | ETH | UP | 0.66 | open |  |
| 10-17 16:03 | +15 | ETH | UP | 0.66 | open |  |
| 10-17 16:03 | +10 | ETH | UP | 0.66 | 0.79 | 1.02 |
| 10-17 16:03 | +5 | ETH | UP | 0.66 | 0.79 | 1.02 |
| 10-17 16:02 | +5 | DOGE | UP | 0.68 | open |  |
| 10-17 16:02 | +10 stop | HYPE | UP | 0.61 | 0.73 | 0.89 |
| 10-17 16:02 | +20 | HYPE | UP | 0.61 | open |  |
| 10-17 16:02 | +15 | HYPE | UP | 0.61 | open |  |
| 10-17 16:02 | +10 | HYPE | UP | 0.61 | 0.73 | 0.89 |
| 10-17 16:02 | +5 | HYPE | UP | 0.61 | 0.73 | 0.89 |
| 10-17 16:01 | +10 stop | DOGE | UP | 0.64 | open |  |
| 10-17 16:01 | +20 | DOGE | UP | 0.64 | open |  |
| 10-17 16:01 | +15 | DOGE | UP | 0.64 | open |  |
| 10-17 16:01 | +10 | DOGE | UP | 0.64 | open |  |
| 10-17 16:01 | +5 | DOGE | UP | 0.64 | 0.71 | 0.38 |
| 10-17 16:00 | +10 stop | BNB | UP | 0.68 | 0.52 | -1.94 |
| 10-17 16:00 | +20 | BNB | UP | 0.68 | open |  |
| 10-17 16:00 | +15 | BNB | UP | 0.68 | open |  |
| 10-17 16:00 | +10 | BNB | UP | 0.68 | open |  |
| 10-17 16:00 | +5 | BNB | UP | 0.68 | open |  |
| 10-17 15:47 | +10 stop | ZEC | DOWN | 0.67 | 0.78 | 0.86 |
| 10-17 15:47 | +20 | ZEC | DOWN | 0.67 | 0.91 | 2.23 |
| 10-17 15:47 | +15 | ZEC | DOWN | 0.67 | 0.84 | 1.44 |
| 10-17 15:47 | +10 | ZEC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-17 15:47 | +5 | ZEC | DOWN | 0.64 | 0.73 | 0.59 |
| 10-17 15:47 | +10 stop | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 10-17 15:47 | +20 | XRP | DOWN | 0.66 | 0.88 | 1.96 |
| 10-17 15:47 | +15 | XRP | DOWN | 0.65 | 0.81 | 1.33 |
| 10-17 15:47 | +10 | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 10-17 15:47 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 10-17 15:46 | +10 stop | HYPE | DOWN | 0.71 | 0.89 | 1.58 |
| 10-17 15:46 | +20 | HYPE | DOWN | 0.71 | 0.91 | 1.82 |
| 10-17 15:46 | +15 | HYPE | DOWN | 0.71 | 0.89 | 1.58 |
