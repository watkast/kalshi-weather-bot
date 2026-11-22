# Range-Scalp Bot

*Updated Sun Nov 22 14:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68854 | 60092 | 8762 (142) | 1 | $-18459.97 | -4.3% |
| **+10¢** | 51378 | 41144 | 10234 (186) | 3 | $-17101.78 | -5.3% |
| **+15¢** | 43056 | 32022 | 11034 (237) | 4 | $-15359.87 | -5.7% |
| **+20¢** | 38332 | 26739 | 11593 (295) | 5 | $-13662.19 | -5.7% |
| **+10¢ (15¢ stop)** | 83819 | 83634 | 185 (116) | 1 | $-30847.59 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 14:57 | +10 stop | XRP | DOWN | 0.35 | 0.56 | 1.76 |
| 11-22 14:56 | +10 stop | DOGE | UP | 0.59 | open |  |
| 11-22 14:56 | +15 | DOGE | UP | 0.57 | open |  |
| 11-22 14:56 | +10 | DOGE | UP | 0.58 | open |  |
| 11-22 14:56 | +5 | DOGE | UP | 0.58 | 0.66 | 0.46 |
| 11-22 14:56 | +10 stop | XRP | UP | 0.71 | 0.45 | -2.93 |
| 11-22 14:56 | +5 | XRP | UP | 0.71 | open |  |
| 11-22 14:55 | +5 | ZEC | UP | 0.67 | 0.73 | 0.30 |
| 11-22 14:54 | +10 stop | ZEC | UP | 0.49 | 0.65 | 1.26 |
| 11-22 14:54 | +15 | ZEC | UP | 0.49 | 0.65 | 1.26 |
| 11-22 14:54 | +10 | ZEC | UP | 0.49 | 0.65 | 1.26 |
| 11-22 14:54 | +5 | ZEC | UP | 0.49 | 0.55 | 0.24 |
| 11-22 14:54 | +10 | ETH | UP | 0.56 | 0.76 | 1.69 |
| 11-22 14:54 | +5 | ETH | UP | 0.56 | 0.63 | 0.35 |
| 11-22 14:54 | +10 stop | BTC | UP | 0.57 | 0.40 | -2.05 |
| 11-22 14:54 | +10 | BTC | UP | 0.57 | 0.78 | 1.79 |
| 11-22 14:54 | +5 | BTC | UP | 0.57 | 0.62 | 0.15 |
| 11-22 14:54 | +20 | XRP | DOWN | 0.70 | open |  |
| 11-22 14:54 | +15 | XRP | DOWN | 0.70 | open |  |
| 11-22 14:54 | +10 | XRP | DOWN | 0.71 | open |  |
| 11-22 14:54 | +5 | XRP | DOWN | 0.71 | 0.77 | 0.32 |
| 11-22 14:54 | +10 stop | DOGE | DOWN | 0.59 | 0.72 | 0.98 |
| 11-22 14:54 | +20 | DOGE | DOWN | 0.59 | open |  |
| 11-22 14:54 | +15 | DOGE | DOWN | 0.59 | 0.74 | 1.19 |
| 11-22 14:54 | +10 | DOGE | DOWN | 0.59 | 0.72 | 0.98 |
| 11-22 14:54 | +5 | DOGE | DOWN | 0.59 | 0.72 | 0.98 |
| 11-22 14:53 | +10 stop | ETH | UP | 0.67 | 0.52 | -1.84 |
| 11-22 14:53 | +5 | BNB | UP | 0.69 | 0.78 | 0.62 |
| 11-22 14:53 | +10 stop | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-22 14:53 | +10 | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-22 14:53 | +5 | BTC | DOWN | 0.57 | 0.63 | 0.25 |
| 11-22 14:52 | +10 stop | ETH | DOWN | 0.70 | 0.54 | -1.93 |
| 11-22 14:51 | +5 | XRP | DOWN | 0.71 | 0.79 | 0.53 |
| 11-22 14:51 | +5 | HYPE | DOWN | 0.51 | 0.60 | 0.53 |
| 11-22 14:51 | +10 stop | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-22 14:51 | +20 | ZEC | DOWN | 0.67 | open |  |
| 11-22 14:51 | +15 | ZEC | DOWN | 0.67 | 0.86 | 1.66 |
| 11-22 14:51 | +10 | ZEC | DOWN | 0.67 | 0.77 | 0.72 |
| 11-22 14:51 | +5 | ZEC | DOWN | 0.67 | 0.75 | 0.51 |
| 11-22 14:50 | +10 stop | BNB | UP | 0.56 | 0.78 | 1.89 |
