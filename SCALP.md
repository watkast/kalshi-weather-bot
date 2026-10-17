# Range-Scalp Bot

*Updated Sat Oct 17 11:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20912 | 18198 | 2714 (29) | 5 | $-6116.23 | -4.6% |
| **+10¢** | 15737 | 12610 | 3127 (41) | 6 | $-5417.81 | -5.5% |
| **+15¢** | 13154 | 9787 | 3367 (61) | 7 | $-4903.66 | -5.9% |
| **+20¢** | 11660 | 8135 | 3525 (80) | 8 | $-4324.10 | -5.9% |
| **+10¢ (15¢ stop)** | 25697 | 25647 | 50 (29) | 2 | $-9791.98 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 11:52 | +10 stop | ZEC | DOWN | 0.49 | open |  |
| 10-17 11:52 | +10 stop | SOL | DOWN | 0.68 | open |  |
| 10-17 11:52 | +5 | BTC | UP | 0.53 | 0.58 | 0.14 |
| 10-17 11:50 | +10 stop | XRP | DOWN | 0.67 | 0.79 | 0.92 |
| 10-17 11:49 | +10 stop | BNB | DOWN | 0.64 | 0.77 | 1.00 |
| 10-17 11:49 | +5 | ETH | DOWN | 0.70 | 0.78 | 0.52 |
| 10-17 11:49 | +10 stop | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-17 11:49 | +10 stop | DOGE | UP | 0.65 | 0.49 | -1.94 |
| 10-17 11:49 | +20 | DOGE | UP | 0.65 | open |  |
| 10-17 11:49 | +15 | DOGE | UP | 0.65 | open |  |
| 10-17 11:49 | +10 | DOGE | UP | 0.65 | open |  |
| 10-17 11:49 | +5 | DOGE | UP | 0.65 | open |  |
| 10-17 11:49 | +15 | ZEC | UP | 0.64 | open |  |
| 10-17 11:49 | +5 | ZEC | UP | 0.64 | open |  |
| 10-17 11:49 | +10 stop | NEAR | DOWN | 0.64 | 0.41 | -2.64 |
| 10-17 11:48 | +5 | XRP | UP | 0.63 | open |  |
| 10-17 11:48 | +10 stop | ZEC | UP | 0.63 | 0.43 | -2.35 |
| 10-17 11:48 | +10 | ZEC | UP | 0.64 | open |  |
| 10-17 11:48 | +5 | ZEC | UP | 0.63 | 0.70 | 0.38 |
| 10-17 11:47 | +10 stop | ETH | DOWN | 0.59 | 0.70 | 0.73 |
| 10-17 11:47 | +5 | ETH | DOWN | 0.59 | 0.67 | 0.47 |
| 10-17 11:47 | +10 stop | XRP | UP | 0.63 | 0.44 | -2.22 |
| 10-17 11:47 | +20 | XRP | UP | 0.63 | open |  |
| 10-17 11:47 | +15 | XRP | UP | 0.63 | open |  |
| 10-17 11:47 | +10 | XRP | UP | 0.63 | open |  |
| 10-17 11:47 | +5 | XRP | UP | 0.63 | 0.68 | 0.20 |
| 10-17 11:47 | +10 stop | NEAR | UP | 0.60 | 0.41 | -2.24 |
| 10-17 11:47 | +20 | NEAR | UP | 0.60 | open |  |
| 10-17 11:47 | +15 | NEAR | UP | 0.60 | 0.75 | 1.19 |
| 10-17 11:47 | +10 | NEAR | UP | 0.60 | 0.75 | 1.19 |
| 10-17 11:47 | +5 | NEAR | UP | 0.60 | 0.68 | 0.47 |
| 10-17 11:47 | +10 stop | BNB | UP | 0.58 | 0.38 | -2.35 |
| 10-17 11:47 | +20 | BNB | UP | 0.58 | open |  |
| 10-17 11:47 | +15 | BNB | UP | 0.58 | open |  |
| 10-17 11:47 | +10 | BNB | UP | 0.59 | open |  |
| 10-17 11:47 | +5 | BNB | UP | 0.59 | open |  |
| 10-17 11:47 | +10 stop | ZEC | UP | 0.53 | 0.65 | 0.86 |
| 10-17 11:47 | +20 | ZEC | UP | 0.53 | open |  |
| 10-17 11:47 | +15 | ZEC | UP | 0.53 | 0.70 | 1.37 |
| 10-17 11:47 | +10 | ZEC | UP | 0.55 | 0.65 | 0.66 |
