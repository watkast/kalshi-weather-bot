# Range-Scalp Bot

*Updated Tue Oct 13 18:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14780 | 12791 | 1989 (27) | 0 | $-4726.80 | -5.1% |
| **+10¢** | 11184 | 8875 | 2309 (39) | 0 | $-4408.20 | -6.3% |
| **+15¢** | 9402 | 6929 | 2473 (57) | 1 | $-3927.65 | -6.7% |
| **+20¢** | 8363 | 5786 | 2577 (73) | 2 | $-3378.68 | -6.4% |
| **+10¢ (15¢ stop)** | 18132 | 18082 | 50 (29) | 0 | $-7016.87 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 18:29 | +15 | XRP | UP | 0.32 | 0.55 | 1.96 |
| 10-13 18:29 | +10 stop | XRP | UP | 0.43 | 0.55 | 0.84 |
| 10-13 18:29 | +10 | XRP | UP | 0.43 | 0.55 | 0.84 |
| 10-13 18:29 | +5 | XRP | UP | 0.42 | 0.55 | 0.89 |
| 10-13 18:28 | +10 stop | XRP | UP | 0.45 | 0.57 | 0.84 |
| 10-13 18:28 | +20 | XRP | UP | 0.45 | open |  |
| 10-13 18:28 | +15 | XRP | UP | 0.44 | 0.63 | 1.55 |
| 10-13 18:28 | +10 | XRP | UP | 0.44 | 0.57 | 0.94 |
| 10-13 18:28 | +5 | XRP | UP | 0.44 | 0.57 | 0.94 |
| 10-13 18:26 | +10 stop | SOL | DOWN | 0.55 | 0.68 | 0.96 |
| 10-13 18:26 | +20 | SOL | DOWN | 0.55 | open |  |
| 10-13 18:26 | +15 | SOL | DOWN | 0.55 | open |  |
| 10-13 18:26 | +10 | SOL | DOWN | 0.55 | 0.68 | 0.96 |
| 10-13 18:21 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-13 18:21 | +15 | SOL | DOWN | 0.64 | 0.84 | 1.73 |
| 10-13 18:21 | +10 | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-13 18:21 | +20 | BTC | DOWN | 0.69 | 0.91 | 1.98 |
| 10-13 18:21 | +15 | BTC | DOWN | 0.69 | 0.87 | 1.57 |
| 10-13 18:21 | +20 | ETH | DOWN | 0.71 | 0.94 | 2.05 |
| 10-13 18:21 | +10 stop | BTC | DOWN | 0.70 | 0.87 | 1.47 |
| 10-13 18:21 | +10 | BTC | DOWN | 0.70 | 0.87 | 1.47 |
| 10-13 18:21 | +5 | BTC | DOWN | 0.69 | 0.76 | 0.42 |
| 10-13 18:20 | +10 stop | DOGE | DOWN | 0.70 | 0.87 | 1.47 |
| 10-13 18:20 | +15 | DOGE | DOWN | 0.70 | 0.87 | 1.47 |
| 10-13 18:20 | +10 | DOGE | DOWN | 0.70 | 0.87 | 1.47 |
| 10-13 18:20 | +5 | DOGE | DOWN | 0.70 | 0.77 | 0.42 |
| 10-13 18:20 | +5 | ZEC | DOWN | 0.66 | 0.77 | 0.79 |
| 10-13 18:19 | +15 | ETH | DOWN | 0.57 | 0.74 | 1.38 |
| 10-13 18:19 | +10 stop | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-13 18:19 | +10 | ZEC | DOWN | 0.67 | 0.77 | 0.72 |
| 10-13 18:19 | +10 stop | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 10-13 18:19 | +10 | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 10-13 18:19 | +5 | ZEC | DOWN | 0.59 | 0.66 | 0.37 |
| 10-13 18:19 | +10 stop | XRP | DOWN | 0.59 | 0.77 | 1.50 |
| 10-13 18:19 | +10 | XRP | DOWN | 0.59 | 0.77 | 1.50 |
| 10-13 18:19 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 10-13 18:18 | +5 | HYPE | DOWN | 0.58 | 0.63 | 0.15 |
| 10-13 18:18 | +5 | BNB | DOWN | 0.60 | 0.75 | 1.19 |
| 10-13 18:18 | +5 | SOL | UP | 0.61 | 0.77 | 1.30 |
| 10-13 18:17 | +5 | HYPE | DOWN | 0.56 | 0.61 | 0.15 |
