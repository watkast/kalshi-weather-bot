# Range-Scalp Bot

*Updated Sat Nov 14 03:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58948 | 51429 | 7519 (106) | 1 | $-15951.81 | -4.3% |
| **+10¢** | 44046 | 35256 | 8790 (139) | 1 | $-14912.01 | -5.4% |
| **+15¢** | 36909 | 27434 | 9475 (174) | 1 | $-13530.33 | -5.8% |
| **+20¢** | 32882 | 22934 | 9948 (226) | 2 | $-11916.44 | -5.8% |
| **+10¢ (15¢ stop)** | 71775 | 71637 | 138 (82) | 1 | $-26383.07 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 03:19 | +10 stop | XRP | DOWN | 0.70 | open |  |
| 11-14 03:19 | +10 | XRP | DOWN | 0.70 | open |  |
| 11-14 03:19 | +5 | XRP | DOWN | 0.70 | open |  |
| 11-14 03:15 | +10 stop | ZEC | DOWN | 0.68 | 0.84 | 1.34 |
| 11-14 03:15 | +20 | ZEC | DOWN | 0.67 | 0.88 | 1.86 |
| 11-14 03:15 | +15 | ZEC | DOWN | 0.67 | 0.84 | 1.44 |
| 11-14 03:15 | +10 | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-14 03:15 | +5 | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-14 03:15 | +10 stop | BTC | DOWN | 0.63 | 0.80 | 1.41 |
| 11-14 03:15 | +20 | BTC | DOWN | 0.63 | 0.87 | 2.15 |
| 11-14 03:15 | +15 | BTC | DOWN | 0.63 | 0.80 | 1.41 |
| 11-14 03:15 | +10 | BTC | DOWN | 0.63 | 0.80 | 1.41 |
| 11-14 03:15 | +5 | BTC | DOWN | 0.63 | 0.69 | 0.28 |
| 11-14 03:15 | +10 stop | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-14 03:15 | +20 | XRP | DOWN | 0.66 | open |  |
| 11-14 03:15 | +15 | XRP | DOWN | 0.66 | open |  |
| 11-14 03:15 | +10 | XRP | DOWN | 0.66 | 0.77 | 0.81 |
| 11-14 03:15 | +5 | XRP | DOWN | 0.66 | 0.71 | 0.19 |
| 11-14 03:15 | +10 stop | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-14 03:15 | +20 | ETH | DOWN | 0.70 | open |  |
| 11-14 03:15 | +15 | ETH | DOWN | 0.70 | 0.87 | 1.47 |
| 11-14 03:15 | +10 | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-14 03:15 | +5 | ETH | DOWN | 0.70 | 0.78 | 0.52 |
| 11-14 03:12 | +10 stop | BNB | DOWN | 0.67 | 0.88 | 1.86 |
| 11-14 03:12 | +10 stop | BTC | DOWN | 0.68 | 0.89 | 1.87 |
| 11-14 03:12 | +20 | BTC | DOWN | 0.68 | 0.89 | 1.87 |
| 11-14 03:12 | +15 | BTC | DOWN | 0.68 | 0.89 | 1.87 |
| 11-14 03:12 | +5 | BTC | DOWN | 0.68 | 0.89 | 1.87 |
| 11-14 03:11 | +10 stop | SOL | UP | 0.70 | 0.46 | -2.73 |
| 11-14 03:11 | +10 stop | ETH | UP | 0.64 | 0.43 | -2.45 |
| 11-14 03:11 | +5 | ETH | UP | 0.64 | no | -6.57 |
| 11-14 03:11 | +10 stop | BNB | UP | 0.36 | 0.62 | 2.26 |
| 11-14 03:10 | +10 stop | SOL | UP | 0.58 | 0.74 | 1.28 |
| 11-14 03:10 | +10 stop | ETH | UP | 0.57 | 0.88 | 2.84 |
| 11-14 03:10 | +5 | ETH | UP | 0.56 | 0.88 | 2.94 |
| 11-14 03:10 | +10 stop | BNB | DOWN | 0.67 | 0.32 | -3.82 |
| 11-14 03:10 | +20 | BNB | DOWN | 0.67 | 0.88 | 1.86 |
| 11-14 03:10 | +15 | BNB | DOWN | 0.67 | 0.88 | 1.86 |
| 11-14 03:10 | +10 | BNB | DOWN | 0.68 | 0.88 | 1.77 |
| 11-14 03:10 | +5 | BNB | DOWN | 0.66 | 0.88 | 1.96 |
