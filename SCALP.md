# Range-Scalp Bot

*Updated Fri Oct 16 11:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19140 | 16637 | 2503 (28) | 2 | $-5736.73 | -4.8% |
| **+10¢** | 14418 | 11524 | 2894 (40) | 4 | $-5178.56 | -5.7% |
| **+15¢** | 12072 | 8961 | 3111 (59) | 4 | $-4648.63 | -6.1% |
| **+20¢** | 10708 | 7448 | 3260 (78) | 5 | $-4122.22 | -6.1% |
| **+10¢ (15¢ stop)** | 23539 | 23489 | 50 (29) | 0 | $-9090.75 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 11:11 | +10 stop | HYPE | UP | 0.60 | 0.73 | 0.99 |
| 10-16 11:11 | +20 | HYPE | UP | 0.60 | 0.88 | 2.55 |
| 10-16 11:11 | +15 | HYPE | UP | 0.60 | 0.88 | 2.55 |
| 10-16 11:11 | +10 | HYPE | UP | 0.60 | 0.73 | 0.99 |
| 10-16 11:11 | +5 | HYPE | UP | 0.59 | 0.73 | 1.09 |
| 10-16 11:10 | +10 stop | DOGE | DOWN | 0.27 | 0.54 | 2.38 |
| 10-16 11:09 | +10 stop | BNB | DOWN | 0.69 | 0.53 | -1.93 |
| 10-16 11:09 | +5 | ZEC | DOWN | 0.65 | 0.81 | 1.33 |
| 10-16 11:08 | +10 stop | ZEC | DOWN | 0.62 | 0.81 | 1.62 |
| 10-16 11:07 | +10 stop | DOGE | UP | 0.61 | 0.41 | -2.34 |
| 10-16 11:07 | +10 stop | BNB | DOWN | 0.59 | 0.44 | -1.85 |
| 10-16 11:07 | +15 | BNB | DOWN | 0.59 | open |  |
| 10-16 11:07 | +10 | BNB | DOWN | 0.58 | open |  |
| 10-16 11:07 | +10 stop | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-16 11:07 | +15 | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 10-16 11:07 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-16 11:07 | +5 | SOL | DOWN | 0.66 | 0.76 | 0.71 |
| 10-16 11:06 | +5 | XRP | DOWN | 0.65 | 0.71 | 0.29 |
| 10-16 11:06 | +10 stop | NEAR | DOWN | 0.54 | 0.32 | -2.54 |
| 10-16 11:06 | +5 | BTC | UP | 0.69 | 0.76 | 0.38 |
| 10-16 11:06 | +10 stop | ZEC | DOWN | 0.57 | 0.39 | -2.15 |
| 10-16 11:06 | +15 | ZEC | DOWN | 0.57 | 0.81 | 2.11 |
| 10-16 11:06 | +10 | ZEC | DOWN | 0.57 | 0.69 | 0.87 |
| 10-16 11:06 | +5 | ZEC | DOWN | 0.57 | 0.62 | 0.15 |
| 10-16 11:06 | +10 stop | HYPE | DOWN | 0.60 | 0.77 | 1.38 |
| 10-16 11:06 | +5 | ETH | UP | 0.66 | 0.71 | 0.19 |
| 10-16 11:05 | +10 stop | NEAR | UP | 0.61 | 0.43 | -2.20 |
| 10-16 11:05 | +10 stop | BNB | DOWN | 0.63 | 0.73 | 0.70 |
| 10-16 11:05 | +10 | BNB | DOWN | 0.63 | 0.73 | 0.70 |
| 10-16 11:05 | +5 | BNB | DOWN | 0.69 | open |  |
| 10-16 11:05 | +5 | SOL | DOWN | 0.66 | 0.72 | 0.29 |
| 10-16 11:05 | +5 | ETH | UP | 0.60 | 0.67 | 0.37 |
| 10-16 11:04 | +10 stop | DOGE | UP | 0.69 | 0.54 | -1.83 |
| 10-16 11:04 | +5 | DOGE | UP | 0.69 | 0.76 | 0.42 |
| 10-16 11:04 | +10 stop | NEAR | UP | 0.68 | 0.52 | -1.90 |
| 10-16 11:04 | +10 stop | ETH | UP | 0.59 | 0.71 | 0.88 |
| 10-16 11:04 | +5 | ETH | UP | 0.59 | 0.66 | 0.37 |
| 10-16 11:04 | +10 stop | HYPE | UP | 0.64 | 0.45 | -2.25 |
| 10-16 11:04 | +10 stop | BNB | DOWN | 0.53 | 0.63 | 0.65 |
| 10-16 11:04 | +10 | BNB | DOWN | 0.53 | 0.63 | 0.65 |
