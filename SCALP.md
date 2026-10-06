# Range-Scalp Bot

*Updated Tue Oct 06 12:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5065 | 4385 | 680 (7) | 2 | $-1587.93 | -5.0% |
| **+10¢** | 3880 | 3088 | 792 (11) | 2 | $-1459.32 | -6.0% |
| **+15¢** | 3260 | 2422 | 838 (14) | 2 | $-1248.24 | -6.1% |
| **+20¢** | 2921 | 2047 | 874 (19) | 2 | $-1019.05 | -5.6% |
| **+10¢ (15¢ stop)** | 6200 | 6187 | 13 (8) | 0 | $-2234.98 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 12:13 | +10 stop | ETH | DOWN | 0.43 | 0.62 | 1.55 |
| 10-06 12:11 | +10 stop | DOGE | DOWN | 0.53 | 0.22 | -3.41 |
| 10-06 12:11 | +10 stop | ETH | DOWN | 0.55 | 0.36 | -2.25 |
| 10-06 12:10 | +10 stop | DOGE | UP | 0.62 | 0.42 | -2.35 |
| 10-06 12:08 | +10 stop | ETH | UP | 0.68 | 0.51 | -2.04 |
| 10-06 12:08 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-06 12:08 | +20 | XRP | DOWN | 0.64 | 0.85 | 1.84 |
| 10-06 12:08 | +15 | XRP | DOWN | 0.64 | 0.80 | 1.31 |
| 10-06 12:08 | +10 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-06 12:08 | +5 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-06 12:08 | +5 | DOGE | DOWN | 0.65 | open |  |
| 10-06 12:07 | +5 | ETH | DOWN | 0.61 | open |  |
| 10-06 12:07 | +10 stop | SOL | UP | 0.68 | 0.80 | 0.92 |
| 10-06 12:07 | +10 stop | DOGE | DOWN | 0.64 | 0.49 | -1.85 |
| 10-06 12:07 | +15 | DOGE | DOWN | 0.64 | open |  |
| 10-06 12:07 | +10 | DOGE | DOWN | 0.64 | open |  |
| 10-06 12:07 | +5 | DOGE | DOWN | 0.64 | 0.70 | 0.28 |
| 10-06 12:07 | +10 stop | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-06 12:07 | +10 | BTC | UP | 0.70 | 0.82 | 0.94 |
| 10-06 12:07 | +5 | BTC | UP | 0.70 | 0.79 | 0.63 |
| 10-06 12:07 | +10 stop | ETH | DOWN | 0.62 | 0.39 | -2.64 |
| 10-06 12:07 | +15 | ETH | DOWN | 0.64 | open |  |
| 10-06 12:07 | +10 | ETH | DOWN | 0.66 | open |  |
| 10-06 12:07 | +5 | ETH | DOWN | 0.54 | 0.60 | 0.25 |
| 10-06 12:06 | +10 stop | SOL | DOWN | 0.54 | 0.35 | -2.24 |
| 10-06 12:06 | +10 stop | BTC | UP | 0.59 | 0.73 | 1.09 |
| 10-06 12:06 | +10 | BTC | UP | 0.59 | 0.73 | 1.09 |
| 10-06 12:06 | +5 | BTC | UP | 0.59 | 0.73 | 1.09 |
| 10-06 12:05 | +5 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-06 12:05 | +5 | XRP | DOWN | 0.71 | 0.80 | 0.63 |
| 10-06 12:04 | +10 stop | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 10-06 12:04 | +5 | ZEC | DOWN | 0.55 | 0.68 | 0.96 |
| 10-06 12:04 | +10 stop | ZEC | DOWN | 0.56 | 0.68 | 0.86 |
| 10-06 12:03 | +5 | SOL | UP | 0.65 | 0.71 | 0.29 |
| 10-06 12:03 | +10 stop | ETH | UP | 0.59 | 0.29 | -3.31 |
| 10-06 12:02 | +10 stop | XRP | UP | 0.67 | 0.44 | -2.64 |
| 10-06 12:02 | +10 stop | SOL | UP | 0.60 | 0.40 | -2.34 |
| 10-06 12:02 | +20 | SOL | UP | 0.60 | 0.80 | 1.71 |
| 10-06 12:02 | +15 | SOL | UP | 0.60 | 0.75 | 1.19 |
| 10-06 12:02 | +10 | SOL | UP | 0.60 | 0.71 | 0.78 |
