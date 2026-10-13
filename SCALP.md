# Range-Scalp Bot

*Updated Tue Oct 13 10:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14526 | 12557 | 1969 (27) | 1 | $-4729.11 | -5.2% |
| **+10¢** | 10990 | 8705 | 2285 (39) | 1 | $-4439.17 | -6.4% |
| **+15¢** | 9239 | 6795 | 2444 (57) | 1 | $-3952.72 | -6.8% |
| **+20¢** | 8222 | 5678 | 2544 (72) | 1 | $-3399.15 | -6.6% |
| **+10¢ (15¢ stop)** | 17826 | 17777 | 49 (29) | 0 | $-6939.89 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 10:36 | +10 stop | DOGE | DOWN | 0.56 | 0.85 | 2.63 |
| 10-13 10:36 | +20 | DOGE | DOWN | 0.56 | 0.85 | 2.63 |
| 10-13 10:36 | +15 | DOGE | DOWN | 0.56 | 0.85 | 2.63 |
| 10-13 10:36 | +10 | DOGE | DOWN | 0.56 | 0.85 | 2.63 |
| 10-13 10:36 | +5 | DOGE | DOWN | 0.56 | 0.85 | 2.63 |
| 10-13 10:36 | +5 | HYPE | DOWN | 0.54 | 0.59 | 0.15 |
| 10-13 10:36 | +5 | SOL | DOWN | 0.51 | 0.63 | 0.85 |
| 10-13 10:35 | +10 stop | ZEC | DOWN | 0.54 | 0.71 | 1.37 |
| 10-13 10:35 | +10 stop | XRP | DOWN | 0.67 | 0.52 | -1.84 |
| 10-13 10:35 | +20 | XRP | DOWN | 0.67 | 0.87 | 1.76 |
| 10-13 10:35 | +15 | XRP | DOWN | 0.67 | 0.85 | 1.55 |
| 10-13 10:35 | +10 | XRP | DOWN | 0.67 | 0.85 | 1.55 |
| 10-13 10:35 | +5 | XRP | DOWN | 0.67 | 0.76 | 0.61 |
| 10-13 10:35 | +5 | HYPE | DOWN | 0.65 | 0.71 | 0.26 |
| 10-13 10:35 | +5 | SOL | DOWN | 0.63 | 0.69 | 0.28 |
| 10-13 10:35 | +10 stop | NEAR | UP | 0.63 | 0.40 | -2.64 |
| 10-13 10:33 | +10 stop | SOL | DOWN | 0.70 | 0.51 | -2.23 |
| 10-13 10:33 | +15 | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 10-13 10:33 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-13 10:33 | +5 | SOL | DOWN | 0.70 | 0.77 | 0.42 |
| 10-13 10:32 | +10 stop | ZEC | DOWN | 0.61 | 0.44 | -2.05 |
| 10-13 10:32 | +10 stop | HYPE | DOWN | 0.65 | 0.81 | 1.33 |
| 10-13 10:31 | +10 stop | ZEC | UP | 0.58 | 0.39 | -2.29 |
| 10-13 10:31 | +10 stop | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-13 10:31 | +10 stop | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 10-13 10:31 | +10 stop | NEAR | UP | 0.63 | 0.31 | -3.52 |
| 10-13 10:31 | +20 | NEAR | UP | 0.63 | open |  |
| 10-13 10:31 | +15 | NEAR | UP | 0.63 | open |  |
| 10-13 10:31 | +10 | NEAR | UP | 0.63 | open |  |
| 10-13 10:31 | +5 | NEAR | UP | 0.63 | open |  |
| 10-13 10:31 | +10 stop | SOL | DOWN | 0.64 | 0.78 | 1.10 |
| 10-13 10:31 | +20 | SOL | DOWN | 0.64 | 0.86 | 1.94 |
| 10-13 10:31 | +15 | SOL | DOWN | 0.64 | 0.81 | 1.42 |
| 10-13 10:31 | +10 | SOL | DOWN | 0.64 | 0.78 | 1.10 |
| 10-13 10:31 | +5 | SOL | DOWN | 0.64 | 0.71 | 0.38 |
| 10-13 10:31 | +10 stop | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 10-13 10:31 | +20 | BNB | DOWN | 0.71 | 0.92 | 1.85 |
| 10-13 10:31 | +15 | BNB | DOWN | 0.71 | 0.88 | 1.47 |
| 10-13 10:31 | +10 | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 10-13 10:31 | +5 | BNB | DOWN | 0.71 | 0.77 | 0.32 |
