# Range-Scalp Bot

*Updated Thu Oct 15 05:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17126 | 14868 | 2258 (28) | 3 | $-5216.54 | -4.8% |
| **+10¢** | 12945 | 10328 | 2617 (40) | 4 | $-4731.76 | -5.8% |
| **+15¢** | 10867 | 8055 | 2812 (59) | 5 | $-4222.51 | -6.2% |
| **+20¢** | 9654 | 6707 | 2947 (77) | 5 | $-3709.46 | -6.1% |
| **+10¢ (15¢ stop)** | 21057 | 21007 | 50 (29) | 0 | $-8129.52 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 04:58 | +10 stop | DOGE | DOWN | 0.59 | 0.84 | 2.23 |
| 10-15 04:58 | +15 | DOGE | DOWN | 0.59 | 0.84 | 2.23 |
| 10-15 04:58 | +10 | DOGE | DOWN | 0.59 | 0.84 | 2.23 |
| 10-15 04:58 | +5 | DOGE | DOWN | 0.59 | 0.84 | 2.23 |
| 10-15 04:57 | +10 stop | BNB | UP | 0.64 | 0.77 | 1.00 |
| 10-15 04:57 | +10 | BNB | UP | 0.64 | 0.77 | 1.00 |
| 10-15 04:57 | +5 | ETH | DOWN | 0.62 | open |  |
| 10-15 04:56 | +10 stop | BNB | DOWN | 0.37 | 0.51 | 1.05 |
| 10-15 04:56 | +20 | BNB | DOWN | 0.37 | open |  |
| 10-15 04:56 | +15 | BNB | DOWN | 0.37 | open |  |
| 10-15 04:56 | +10 | BNB | DOWN | 0.37 | 0.51 | 1.05 |
| 10-15 04:56 | +10 stop | ZEC | UP | 0.65 | 0.83 | 1.54 |
| 10-15 04:56 | +5 | ZEC | UP | 0.65 | 0.70 | 0.19 |
| 10-15 04:56 | +10 stop | ETH | DOWN | 0.67 | 0.29 | -4.11 |
| 10-15 04:56 | +5 | ETH | DOWN | 0.66 | 0.73 | 0.40 |
| 10-15 04:55 | +10 stop | BTC | UP | 0.62 | 0.73 | 0.79 |
| 10-15 04:54 | +10 stop | BNB | UP | 0.70 | 0.55 | -1.83 |
| 10-15 04:54 | +5 | BNB | UP | 0.69 | 0.77 | 0.52 |
| 10-15 04:54 | +10 stop | DOGE | UP | 0.70 | 0.52 | -2.13 |
| 10-15 04:54 | +10 stop | ETH | UP | 0.71 | 0.21 | -5.27 |
| 10-15 04:54 | +10 stop | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 10-15 04:54 | +10 | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 10-15 04:54 | +5 | SOL | DOWN | 0.61 | 0.79 | 1.53 |
| 10-15 04:53 | +5 | BNB | DOWN | 0.54 | 0.61 | 0.35 |
| 10-15 04:52 | +5 | ZEC | DOWN | 0.66 | 0.71 | 0.19 |
| 10-15 04:52 | +10 stop | SOL | DOWN | 0.63 | 0.79 | 1.31 |
| 10-15 04:52 | +10 | SOL | DOWN | 0.63 | 0.79 | 1.31 |
| 10-15 04:52 | +5 | SOL | DOWN | 0.63 | 0.79 | 1.31 |
| 10-15 04:52 | +10 stop | BNB | DOWN | 0.58 | 0.40 | -2.14 |
| 10-15 04:52 | +5 | BNB | DOWN | 0.58 | 0.63 | 0.15 |
| 10-15 04:51 | +5 | SOL | DOWN | 0.71 | 0.77 | 0.32 |
| 10-15 04:50 | +10 stop | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-15 04:50 | +10 stop | ZEC | DOWN | 0.70 | 0.49 | -2.43 |
| 10-15 04:50 | +10 stop | ETH | DOWN | 0.59 | 0.34 | -2.83 |
| 10-15 04:50 | +10 stop | DOGE | DOWN | 0.57 | 0.41 | -1.95 |
| 10-15 04:48 | +10 stop | SOL | UP | 0.58 | 0.34 | -2.74 |
| 10-15 04:48 | +10 stop | ZEC | UP | 0.63 | 0.47 | -1.94 |
| 10-15 04:48 | +10 stop | BTC | UP | 0.63 | 0.76 | 1.00 |
| 10-15 04:48 | +10 stop | HYPE | UP | 0.64 | 0.82 | 1.52 |
| 10-15 04:47 | +10 stop | NEAR | DOWN | 0.61 | 0.74 | 0.99 |
