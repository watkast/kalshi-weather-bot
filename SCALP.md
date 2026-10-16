# Range-Scalp Bot

*Updated Fri Oct 16 03:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18591 | 16148 | 2443 (28) | 3 | $-5640.32 | -4.8% |
| **+10¢** | 14024 | 11198 | 2826 (40) | 3 | $-5092.63 | -5.8% |
| **+15¢** | 11759 | 8717 | 3042 (59) | 4 | $-4604.65 | -6.2% |
| **+20¢** | 10442 | 7259 | 3183 (78) | 5 | $-4022.86 | -6.1% |
| **+10¢ (15¢ stop)** | 22903 | 22853 | 50 (29) | 2 | $-8843.75 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 03:06 | +10 stop | BNB | UP | 0.64 | 0.76 | 0.90 |
| 10-16 03:06 | +10 stop | ZEC | UP | 0.70 | open |  |
| 10-16 03:05 | +10 stop | ZEC | UP | 0.55 | 0.67 | 0.84 |
| 10-16 03:05 | +10 stop | BNB | DOWN | 0.58 | 0.33 | -2.84 |
| 10-16 03:05 | +15 | BNB | DOWN | 0.58 | open |  |
| 10-16 03:05 | +10 | BNB | DOWN | 0.59 | open |  |
| 10-16 03:05 | +5 | BNB | DOWN | 0.59 | open |  |
| 10-16 03:04 | +10 stop | NEAR | DOWN | 0.55 | open |  |
| 10-16 03:04 | +10 stop | DOGE | UP | 0.71 | 0.83 | 0.95 |
| 10-16 03:04 | +20 | DOGE | UP | 0.71 | open |  |
| 10-16 03:04 | +15 | DOGE | UP | 0.71 | 0.86 | 1.26 |
| 10-16 03:04 | +10 | DOGE | UP | 0.71 | 0.83 | 0.95 |
| 10-16 03:04 | +5 | DOGE | UP | 0.71 | 0.76 | 0.22 |
| 10-16 03:03 | +10 stop | HYPE | UP | 0.60 | 0.72 | 0.88 |
| 10-16 03:03 | +10 stop | XRP | UP | 0.67 | 0.79 | 0.92 |
| 10-16 03:03 | +10 stop | BTC | UP | 0.66 | 0.78 | 0.91 |
| 10-16 03:03 | +10 | BTC | UP | 0.66 | 0.78 | 0.91 |
| 10-16 03:03 | +5 | BTC | UP | 0.66 | 0.72 | 0.29 |
| 10-16 03:02 | +10 stop | XRP | UP | 0.70 | 0.55 | -1.83 |
| 10-16 03:02 | +20 | XRP | UP | 0.70 | open |  |
| 10-16 03:02 | +15 | XRP | UP | 0.71 | open |  |
| 10-16 03:02 | +10 | XRP | UP | 0.71 | 0.81 | 0.74 |
| 10-16 03:02 | +5 | XRP | UP | 0.71 | 0.79 | 0.53 |
| 10-16 03:02 | +10 stop | NEAR | UP | 0.56 | 0.38 | -2.15 |
| 10-16 03:02 | +20 | NEAR | UP | 0.56 | open |  |
| 10-16 03:02 | +15 | NEAR | UP | 0.56 | open |  |
| 10-16 03:02 | +10 | NEAR | UP | 0.56 | open |  |
| 10-16 03:02 | +5 | NEAR | UP | 0.56 | open |  |
| 10-16 03:01 | +10 stop | SOL | UP | 0.68 | 0.82 | 1.13 |
| 10-16 03:01 | +20 | SOL | UP | 0.68 | 0.88 | 1.76 |
| 10-16 03:01 | +15 | SOL | UP | 0.68 | 0.87 | 1.66 |
| 10-16 03:01 | +10 | SOL | UP | 0.68 | 0.82 | 1.13 |
| 10-16 03:01 | +5 | SOL | UP | 0.68 | 0.73 | 0.20 |
| 10-16 03:01 | +10 stop | ETH | UP | 0.64 | 0.75 | 0.79 |
| 10-16 03:01 | +20 | ETH | UP | 0.64 | 0.84 | 1.73 |
| 10-16 03:01 | +15 | ETH | UP | 0.64 | 0.84 | 1.73 |
| 10-16 03:01 | +10 | ETH | UP | 0.64 | 0.75 | 0.79 |
| 10-16 03:01 | +5 | ETH | UP | 0.64 | 0.69 | 0.18 |
| 10-16 03:01 | +10 stop | HYPE | UP | 0.62 | 0.47 | -1.85 |
| 10-16 03:01 | +20 | HYPE | UP | 0.62 | 0.84 | 1.93 |
