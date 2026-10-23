# Range-Scalp Bot

*Updated Fri Oct 23 19:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30808 | 26845 | 3963 (39) | 0 | $-8932.44 | -4.6% |
| **+10¢** | 23053 | 18472 | 4581 (57) | 0 | $-7947.65 | -5.5% |
| **+15¢** | 19285 | 14353 | 4932 (80) | 1 | $-7196.30 | -5.9% |
| **+20¢** | 17083 | 11920 | 5163 (103) | 1 | $-6421.67 | -6.0% |
| **+10¢ (15¢ stop)** | 37795 | 37736 | 59 (32) | 0 | $-14392.89 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 19:10 | +10 stop | SOL | UP | 0.64 | 0.20 | -4.69 |
| 10-23 19:09 | +10 stop | SOL | DOWN | 0.66 | 0.42 | -2.74 |
| 10-23 19:09 | +5 | SOL | DOWN | 0.66 | 0.79 | 1.02 |
| 10-23 19:05 | +10 stop | SOL | UP | 0.70 | 0.44 | -2.93 |
| 10-23 19:04 | +10 stop | SOL | UP | 0.68 | 0.43 | -2.88 |
| 10-23 19:01 | +10 stop | BTC | DOWN | 0.60 | 0.76 | 1.30 |
| 10-23 19:01 | +20 | BTC | DOWN | 0.60 | 0.86 | 2.34 |
| 10-23 19:01 | +15 | BTC | DOWN | 0.60 | 0.76 | 1.30 |
| 10-23 19:01 | +10 | BTC | DOWN | 0.60 | 0.76 | 1.30 |
| 10-23 19:01 | +5 | BTC | DOWN | 0.60 | 0.68 | 0.47 |
| 10-23 19:01 | +10 stop | SOL | DOWN | 0.68 | 0.49 | -2.24 |
| 10-23 19:01 | +20 | SOL | DOWN | 0.68 | open |  |
| 10-23 19:01 | +15 | SOL | DOWN | 0.68 | open |  |
| 10-23 19:01 | +10 | SOL | DOWN | 0.68 | 0.79 | 0.82 |
| 10-23 19:01 | +5 | SOL | DOWN | 0.68 | 0.73 | 0.20 |
| 10-23 18:58 | +10 stop | SOL | DOWN | 0.30 | 0.55 | 2.17 |
| 10-23 18:58 | +20 | SOL | DOWN | 0.30 | 0.55 | 2.17 |
| 10-23 18:58 | +15 | SOL | DOWN | 0.30 | 0.55 | 2.17 |
| 10-23 18:58 | +10 | SOL | DOWN | 0.31 | 0.55 | 2.07 |
| 10-23 18:58 | +5 | SOL | DOWN | 0.31 | 0.55 | 2.07 |
| 10-23 18:57 | +10 stop | BNB | UP | 0.70 | 0.14 | -5.84 |
| 10-23 18:57 | +20 | BNB | UP | 0.71 | no | -7.25 |
| 10-23 18:57 | +15 | BNB | UP | 0.71 | no | -7.25 |
| 10-23 18:57 | +10 | BNB | UP | 0.70 | no | -7.15 |
| 10-23 18:57 | +5 | BNB | UP | 0.70 | 0.76 | 0.32 |
| 10-23 18:54 | +10 stop | XRP | DOWN | 0.57 | 0.70 | 0.97 |
| 10-23 18:54 | +10 | XRP | DOWN | 0.57 | 0.70 | 0.97 |
| 10-23 18:54 | +5 | XRP | DOWN | 0.61 | 0.70 | 0.60 |
| 10-23 18:54 | +10 stop | BTC | DOWN | 0.59 | 0.43 | -1.95 |
| 10-23 18:54 | +10 stop | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-23 18:54 | +10 stop | ETH | DOWN | 0.65 | 0.80 | 1.22 |
| 10-23 18:53 | +10 stop | XRP | DOWN | 0.49 | 0.60 | 0.75 |
| 10-23 18:53 | +20 | XRP | DOWN | 0.50 | 0.70 | 1.68 |
| 10-23 18:53 | +15 | XRP | DOWN | 0.50 | 0.70 | 1.68 |
| 10-23 18:53 | +10 | XRP | DOWN | 0.50 | 0.60 | 0.65 |
| 10-23 18:53 | +5 | XRP | DOWN | 0.50 | 0.58 | 0.44 |
| 10-23 18:52 | +10 stop | DOGE | DOWN | 0.71 | 0.50 | -2.43 |
| 10-23 18:52 | +20 | DOGE | DOWN | 0.71 | 0.95 | 2.22 |
| 10-23 18:52 | +15 | DOGE | DOWN | 0.71 | 0.88 | 1.47 |
| 10-23 18:52 | +10 | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
