# Range-Scalp Bot

*Updated Fri Oct 16 21:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19913 | 17318 | 2595 (29) | 3 | $-5913.37 | -4.7% |
| **+10¢** | 14997 | 11997 | 3000 (41) | 5 | $-5323.61 | -5.6% |
| **+15¢** | 12544 | 9318 | 3226 (60) | 6 | $-4810.85 | -6.1% |
| **+20¢** | 11125 | 7747 | 3378 (79) | 7 | $-4249.42 | -6.1% |
| **+10¢ (15¢ stop)** | 24474 | 24424 | 50 (29) | 1 | $-9318.90 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 21:53 | +10 stop | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-16 21:53 | +5 | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-16 21:52 | +10 stop | XRP | DOWN | 0.54 | 0.65 | 0.76 |
| 10-16 21:52 | +5 | XRP | DOWN | 0.51 | 0.65 | 1.06 |
| 10-16 21:52 | +5 | SOL | DOWN | 0.58 | 0.63 | 0.15 |
| 10-16 21:52 | +10 stop | NEAR | DOWN | 0.69 | open |  |
| 10-16 21:52 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.22 |
| 10-16 21:52 | +10 stop | SOL | DOWN | 0.53 | 0.63 | 0.65 |
| 10-16 21:52 | +5 | SOL | DOWN | 0.53 | 0.58 | 0.14 |
| 10-16 21:51 | +10 stop | XRP | UP | 0.54 | 0.37 | -2.05 |
| 10-16 21:51 | +5 | XRP | UP | 0.54 | 0.63 | 0.55 |
| 10-16 21:51 | +10 stop | SOL | UP | 0.38 | 0.55 | 1.35 |
| 10-16 21:51 | +5 | SOL | UP | 0.38 | 0.55 | 1.35 |
| 10-16 21:51 | +10 stop | ZEC | DOWN | 0.70 | 0.85 | 1.26 |
| 10-16 21:51 | +20 | ZEC | DOWN | 0.70 | 0.91 | 1.89 |
| 10-16 21:51 | +15 | ZEC | DOWN | 0.70 | 0.85 | 1.26 |
| 10-16 21:51 | +10 | ZEC | DOWN | 0.70 | 0.85 | 1.26 |
| 10-16 21:51 | +5 | ZEC | DOWN | 0.70 | 0.76 | 0.32 |
| 10-16 21:51 | +10 stop | DOGE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-16 21:51 | +15 | DOGE | DOWN | 0.58 | 0.77 | 1.57 |
| 10-16 21:51 | +10 | DOGE | DOWN | 0.58 | 0.69 | 0.75 |
| 10-16 21:51 | +5 | DOGE | DOWN | 0.58 | 0.64 | 0.23 |
| 10-16 21:51 | +5 | NEAR | DOWN | 0.48 | 0.58 | 0.64 |
| 10-16 21:51 | +10 stop | ETH | UP | 0.57 | 0.71 | 1.07 |
| 10-16 21:50 | +10 stop | BTC | UP | 0.66 | 0.50 | -1.94 |
| 10-16 21:49 | +10 stop | ETH | DOWN | 0.61 | 0.38 | -2.64 |
| 10-16 21:49 | +10 | ETH | DOWN | 0.60 | open |  |
| 10-16 21:48 | +5 | NEAR | DOWN | 0.61 | 0.69 | 0.48 |
| 10-16 21:48 | +5 | ETH | DOWN | 0.64 | open |  |
| 10-16 21:48 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 10-16 21:48 | +10 stop | HYPE | DOWN | 0.67 | 0.48 | -2.22 |
| 10-16 21:48 | +20 | HYPE | DOWN | 0.67 | open |  |
| 10-16 21:48 | +15 | HYPE | DOWN | 0.67 | open |  |
| 10-16 21:48 | +10 | HYPE | DOWN | 0.67 | open |  |
| 10-16 21:48 | +5 | HYPE | DOWN | 0.67 | open |  |
| 10-16 21:47 | +10 stop | BNB | DOWN | 0.60 | 0.73 | 0.99 |
| 10-16 21:47 | +20 | BNB | DOWN | 0.60 | open |  |
| 10-16 21:47 | +15 | BNB | DOWN | 0.60 | 0.75 | 1.19 |
| 10-16 21:47 | +10 | BNB | DOWN | 0.60 | 0.73 | 0.99 |
| 10-16 21:47 | +5 | BNB | DOWN | 0.60 | 0.66 | 0.27 |
