# Range-Scalp Bot

*Updated Tue Oct 13 21:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14971 | 12946 | 2025 (27) | 6 | $-4877.41 | -5.2% |
| **+10¢** | 11326 | 8979 | 2347 (39) | 6 | $-4543.95 | -6.4% |
| **+15¢** | 9516 | 7006 | 2510 (58) | 6 | $-4029.07 | -6.7% |
| **+20¢** | 8462 | 5844 | 2618 (74) | 7 | $-3500.42 | -6.6% |
| **+10¢ (15¢ stop)** | 18373 | 18323 | 50 (29) | 3 | $-7135.37 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 21:10 | +5 | XRP | UP | 0.70 | open |  |
| 10-13 21:10 | +10 stop | BTC | DOWN | 0.63 | open |  |
| 10-13 21:10 | +15 | BTC | DOWN | 0.63 | open |  |
| 10-13 21:10 | +10 | BTC | DOWN | 0.63 | open |  |
| 10-13 21:10 | +5 | BTC | DOWN | 0.63 | open |  |
| 10-13 21:10 | +5 | DOGE | DOWN | 0.70 | open |  |
| 10-13 21:09 | +10 stop | SOL | DOWN | 0.71 | 0.55 | -1.93 |
| 10-13 21:09 | +10 stop | ZEC | UP | 0.65 | 0.80 | 1.23 |
| 10-13 21:09 | +15 | ZEC | UP | 0.65 | 0.80 | 1.23 |
| 10-13 21:09 | +10 | ZEC | UP | 0.65 | 0.80 | 1.23 |
| 10-13 21:09 | +5 | ZEC | UP | 0.65 | 0.80 | 1.23 |
| 10-13 21:09 | +10 stop | DOGE | DOWN | 0.67 | open |  |
| 10-13 21:09 | +5 | DOGE | DOWN | 0.67 | 0.72 | 0.19 |
| 10-13 21:09 | +10 stop | XRP | UP | 0.60 | open |  |
| 10-13 21:09 | +15 | XRP | UP | 0.60 | open |  |
| 10-13 21:09 | +10 | XRP | UP | 0.60 | open |  |
| 10-13 21:09 | +5 | XRP | UP | 0.60 | 0.65 | 0.17 |
| 10-13 21:08 | +5 | DOGE | UP | 0.45 | 0.58 | 0.94 |
| 10-13 21:07 | +10 stop | BNB | DOWN | 0.71 | 0.87 | 1.38 |
| 10-13 21:07 | +10 | BNB | DOWN | 0.71 | 0.87 | 1.38 |
| 10-13 21:07 | +5 | BNB | DOWN | 0.71 | 0.77 | 0.33 |
| 10-13 21:07 | +5 | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 10-13 21:07 | +10 stop | SOL | DOWN | 0.54 | 0.67 | 0.96 |
| 10-13 21:06 | +10 stop | DOGE | UP | 0.69 | 0.42 | -3.03 |
| 10-13 21:06 | +10 | DOGE | UP | 0.69 | open |  |
| 10-13 21:06 | +5 | DOGE | UP | 0.69 | 0.74 | 0.21 |
| 10-13 21:05 | +10 stop | ZEC | UP | 0.60 | 0.76 | 1.30 |
| 10-13 21:04 | +10 stop | ETH | DOWN | 0.64 | 0.77 | 1.02 |
| 10-13 21:04 | +15 | ETH | DOWN | 0.64 | 0.81 | 1.44 |
| 10-13 21:04 | +10 | ETH | DOWN | 0.64 | 0.77 | 1.02 |
| 10-13 21:04 | +5 | ETH | DOWN | 0.64 | 0.69 | 0.20 |
| 10-13 21:04 | +5 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-13 21:03 | +10 stop | ZEC | DOWN | 0.55 | 0.40 | -1.86 |
| 10-13 21:03 | +5 | ETH | DOWN | 0.68 | 0.73 | 0.21 |
| 10-13 21:03 | +10 stop | SOL | DOWN | 0.54 | 0.66 | 0.86 |
| 10-13 21:03 | +10 stop | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-13 21:03 | +20 | BNB | DOWN | 0.67 | 0.87 | 1.76 |
| 10-13 21:03 | +15 | BNB | DOWN | 0.67 | 0.87 | 1.76 |
| 10-13 21:03 | +10 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-13 21:03 | +5 | BNB | DOWN | 0.67 | 0.72 | 0.19 |
