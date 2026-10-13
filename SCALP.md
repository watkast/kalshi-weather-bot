# Range-Scalp Bot

*Updated Tue Oct 13 21:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14989 | 12962 | 2027 (27) | 4 | $-4879.31 | -5.2% |
| **+10¢** | 11334 | 8984 | 2350 (39) | 5 | $-4556.36 | -6.4% |
| **+15¢** | 9524 | 7010 | 2514 (58) | 5 | $-4045.13 | -6.8% |
| **+20¢** | 8471 | 5849 | 2622 (74) | 5 | $-3514.05 | -6.6% |
| **+10¢ (15¢ stop)** | 18388 | 18338 | 50 (29) | 5 | $-7142.93 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 21:21 | +5 | HYPE | UP | 0.56 | open |  |
| 10-13 21:20 | +10 stop | DOGE | DOWN | 0.69 | open |  |
| 10-13 21:20 | +10 stop | ZEC | DOWN | 0.71 | open |  |
| 10-13 21:20 | +5 | ZEC | DOWN | 0.69 | open |  |
| 10-13 21:20 | +10 stop | HYPE | UP | 0.62 | open |  |
| 10-13 21:20 | +5 | HYPE | UP | 0.62 | 0.68 | 0.27 |
| 10-13 21:20 | +10 stop | XRP | UP | 0.55 | open |  |
| 10-13 21:20 | +10 stop | DOGE | UP | 0.53 | 0.34 | -2.24 |
| 10-13 21:20 | +5 | ZEC | UP | 0.52 | 0.64 | 0.85 |
| 10-13 21:20 | +5 | BNB | DOWN | 0.61 | 0.66 | 0.17 |
| 10-13 21:19 | +10 stop | XRP | UP | 0.52 | 0.71 | 1.57 |
| 10-13 21:19 | +5 | HYPE | UP | 0.60 | 0.73 | 0.99 |
| 10-13 21:18 | +10 stop | HYPE | DOWN | 0.49 | 0.26 | -2.66 |
| 10-13 21:18 | +20 | HYPE | DOWN | 0.49 | open |  |
| 10-13 21:18 | +15 | HYPE | DOWN | 0.49 | open |  |
| 10-13 21:18 | +10 | HYPE | DOWN | 0.49 | open |  |
| 10-13 21:18 | +5 | HYPE | DOWN | 0.49 | 0.56 | 0.30 |
| 10-13 21:17 | +5 | DOGE | DOWN | 0.67 | open |  |
| 10-13 21:17 | +5 | NEAR | UP | 0.70 | 0.77 | 0.42 |
| 10-13 21:17 | +10 stop | ZEC | UP | 0.56 | 0.37 | -2.25 |
| 10-13 21:17 | +20 | ZEC | UP | 0.56 | open |  |
| 10-13 21:17 | +15 | ZEC | UP | 0.56 | open |  |
| 10-13 21:17 | +10 | ZEC | UP | 0.56 | open |  |
| 10-13 21:17 | +5 | ZEC | UP | 0.56 | 0.63 | 0.35 |
| 10-13 21:17 | +10 stop | SOL | UP | 0.63 | 0.75 | 0.93 |
| 10-13 21:17 | +20 | SOL | UP | 0.63 | 0.83 | 1.77 |
| 10-13 21:17 | +15 | SOL | UP | 0.62 | 0.83 | 1.83 |
| 10-13 21:17 | +10 | SOL | UP | 0.61 | 0.75 | 1.09 |
| 10-13 21:17 | +5 | SOL | UP | 0.61 | 0.75 | 1.09 |
| 10-13 21:16 | +10 stop | DOGE | DOWN | 0.63 | 0.37 | -2.94 |
| 10-13 21:16 | +20 | DOGE | DOWN | 0.62 | open |  |
| 10-13 21:16 | +15 | DOGE | DOWN | 0.62 | open |  |
| 10-13 21:16 | +10 | DOGE | DOWN | 0.62 | open |  |
| 10-13 21:16 | +5 | DOGE | DOWN | 0.62 | 0.67 | 0.17 |
| 10-13 21:16 | +10 stop | BNB | DOWN | 0.69 | open |  |
| 10-13 21:16 | +20 | BNB | DOWN | 0.69 | open |  |
| 10-13 21:16 | +15 | BNB | DOWN | 0.69 | open |  |
| 10-13 21:16 | +10 | BNB | DOWN | 0.69 | open |  |
| 10-13 21:16 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 10-13 21:16 | +10 stop | XRP | DOWN | 0.63 | 0.44 | -2.25 |
