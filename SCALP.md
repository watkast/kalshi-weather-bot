# Range-Scalp Bot

*Updated Wed Oct 14 06:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15546 | 13460 | 2086 (27) | 4 | $-4931.36 | -5.0% |
| **+10¢** | 11772 | 9352 | 2420 (39) | 3 | $-4575.94 | -6.2% |
| **+15¢** | 9886 | 7290 | 2596 (58) | 3 | $-4100.60 | -6.6% |
| **+20¢** | 8788 | 6069 | 2719 (75) | 3 | $-3631.14 | -6.6% |
| **+10¢ (15¢ stop)** | 19111 | 19061 | 50 (29) | 2 | $-7374.92 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 06:12 | +10 stop | BNB | DOWN | 0.64 | open |  |
| 10-14 06:12 | +10 stop | BTC | DOWN | 0.50 | open |  |
| 10-14 06:11 | +10 stop | SOL | DOWN | 0.39 | 0.53 | 1.05 |
| 10-14 06:11 | +10 stop | ETH | UP | 0.59 | 0.77 | 1.50 |
| 10-14 06:11 | +15 | ETH | UP | 0.59 | 0.77 | 1.50 |
| 10-14 06:11 | +10 stop | SOL | UP | 0.68 | 0.42 | -2.94 |
| 10-14 06:10 | +10 stop | DOGE | UP | 0.65 | 0.87 | 1.96 |
| 10-14 06:10 | +20 | DOGE | UP | 0.65 | 0.87 | 1.96 |
| 10-14 06:10 | +15 | DOGE | UP | 0.65 | 0.87 | 1.96 |
| 10-14 06:10 | +10 | DOGE | UP | 0.65 | 0.87 | 1.94 |
| 10-14 06:10 | +10 stop | DOGE | UP | 0.43 | 0.66 | 1.96 |
| 10-14 06:10 | +20 | DOGE | UP | 0.43 | 0.66 | 1.96 |
| 10-14 06:10 | +15 | DOGE | UP | 0.43 | 0.66 | 1.96 |
| 10-14 06:10 | +10 | DOGE | UP | 0.43 | 0.66 | 1.96 |
| 10-14 06:10 | +10 stop | ETH | UP | 0.43 | 0.59 | 1.25 |
| 10-14 06:09 | +10 stop | ZEC | UP | 0.66 | 0.51 | -1.84 |
| 10-14 06:09 | +10 | ZEC | UP | 0.66 | open |  |
| 10-14 06:09 | +5 | ZEC | UP | 0.66 | 0.74 | 0.50 |
| 10-14 06:09 | +15 | ETH | UP | 0.50 | 0.66 | 1.26 |
| 10-14 06:08 | +10 stop | BNB | DOWN | 0.58 | 0.72 | 1.07 |
| 10-14 06:08 | +10 stop | ETH | UP | 0.70 | 0.53 | -1.99 |
| 10-14 06:07 | +10 stop | ZEC | UP | 0.67 | 0.79 | 0.92 |
| 10-14 06:07 | +5 | ZEC | UP | 0.67 | 0.76 | 0.61 |
| 10-14 06:07 | +10 stop | SOL | UP | 0.67 | 0.44 | -2.64 |
| 10-14 06:07 | +10 | SOL | UP | 0.67 | 0.86 | 1.65 |
| 10-14 06:06 | +10 stop | SOL | DOWN | 0.56 | 0.32 | -2.74 |
| 10-14 06:06 | +5 | SOL | DOWN | 0.56 | open |  |
| 10-14 06:06 | +10 stop | XRP | UP | 0.71 | 0.84 | 1.05 |
| 10-14 06:06 | +10 stop | DOGE | DOWN | 0.54 | 0.31 | -2.63 |
| 10-14 06:06 | +5 | DOGE | DOWN | 0.54 | open |  |
| 10-14 06:06 | +10 stop | ETH | DOWN | 0.60 | 0.44 | -1.95 |
| 10-14 06:06 | +10 stop | XRP | DOWN | 0.49 | 0.63 | 1.05 |
| 10-14 06:06 | +10 stop | HYPE | DOWN | 0.56 | 0.40 | -1.95 |
| 10-14 06:05 | +10 stop | ZEC | DOWN | 0.56 | 0.34 | -2.54 |
| 10-14 06:04 | +5 | SOL | DOWN | 0.64 | 0.81 | 1.42 |
| 10-14 06:04 | +10 stop | ETH | DOWN | 0.61 | 0.80 | 1.61 |
| 10-14 06:04 | +10 stop | BTC | DOWN | 0.67 | 0.85 | 1.55 |
| 10-14 06:04 | +10 stop | BNB | DOWN | 0.64 | 0.75 | 0.79 |
| 10-14 06:04 | +10 stop | DOGE | UP | 0.49 | 0.15 | -3.67 |
| 10-14 06:04 | +20 | DOGE | UP | 0.49 | 0.71 | 1.87 |
