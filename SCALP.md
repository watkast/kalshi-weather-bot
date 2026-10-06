# Range-Scalp Bot

*Updated Tue Oct 06 17:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5252 | 4552 | 700 (7) | 3 | $-1621.18 | -4.9% |
| **+10¢** | 4015 | 3198 | 817 (12) | 2 | $-1493.49 | -5.9% |
| **+15¢** | 3363 | 2497 | 866 (15) | 2 | $-1299.51 | -6.2% |
| **+20¢** | 3010 | 2110 | 900 (22) | 2 | $-1026.10 | -5.4% |
| **+10¢ (15¢ stop)** | 6419 | 6404 | 15 (9) | 0 | $-2343.97 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 17:27 | +10 stop | HYPE | DOWN | 0.57 | 0.32 | -2.84 |
| 10-06 17:27 | +20 | HYPE | DOWN | 0.57 | open |  |
| 10-06 17:27 | +15 | HYPE | DOWN | 0.57 | open |  |
| 10-06 17:27 | +10 | HYPE | DOWN | 0.57 | open |  |
| 10-06 17:27 | +5 | HYPE | DOWN | 0.57 | open |  |
| 10-06 17:26 | +10 stop | BNB | DOWN | 0.60 | 0.72 | 0.88 |
| 10-06 17:25 | +10 stop | ETH | UP | 0.64 | 0.76 | 0.90 |
| 10-06 17:24 | +10 stop | SOL | UP | 0.62 | 0.82 | 1.72 |
| 10-06 17:24 | +10 stop | XRP | UP | 0.71 | 0.86 | 1.29 |
| 10-06 17:24 | +10 stop | BTC | DOWN | 0.52 | 0.36 | -1.95 |
| 10-06 17:24 | +10 stop | XRP | DOWN | 0.43 | 0.57 | 1.04 |
| 10-06 17:23 | +10 stop | ETH | DOWN | 0.71 | 0.56 | -1.83 |
| 10-06 17:23 | +5 | SOL | DOWN | 0.70 | open |  |
| 10-06 17:22 | +5 | ZEC | UP | 0.70 | 0.76 | 0.33 |
| 10-06 17:22 | +10 | NEAR | UP | 0.64 | 0.75 | 0.79 |
| 10-06 17:22 | +10 stop | HYPE | DOWN | 0.70 | 0.83 | 1.05 |
| 10-06 17:22 | +10 | HYPE | DOWN | 0.70 | 0.83 | 1.06 |
| 10-06 17:22 | +5 | HYPE | DOWN | 0.68 | 0.75 | 0.40 |
| 10-06 17:22 | +10 stop | XRP | DOWN | 0.65 | 0.77 | 0.91 |
| 10-06 17:22 | +10 stop | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-06 17:21 | +10 stop | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-06 17:21 | +15 | DOGE | UP | 0.69 | 0.84 | 1.25 |
| 10-06 17:21 | +10 | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-06 17:21 | +5 | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 10-06 17:21 | +10 stop | SOL | DOWN | 0.68 | 0.53 | -1.84 |
| 10-06 17:21 | +10 stop | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 10-06 17:21 | +10 | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 10-06 17:21 | +5 | ZEC | UP | 0.68 | 0.74 | 0.30 |
| 10-06 17:21 | +10 stop | NEAR | UP | 0.69 | 0.81 | 0.94 |
| 10-06 17:21 | +20 | NEAR | UP | 0.69 | 0.92 | 2.09 |
| 10-06 17:21 | +5 | NEAR | UP | 0.69 | 0.75 | 0.31 |
| 10-06 17:20 | +10 stop | ETH | DOWN | 0.56 | 0.72 | 1.27 |
| 10-06 17:20 | +5 | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 10-06 17:19 | +10 stop | XRP | DOWN | 0.62 | 0.44 | -2.15 |
| 10-06 17:19 | +10 stop | DOGE | UP | 0.59 | 0.74 | 1.19 |
| 10-06 17:19 | +5 | HYPE | DOWN | 0.63 | 0.69 | 0.24 |
| 10-06 17:19 | +5 | SOL | DOWN | 0.47 | 0.56 | 0.54 |
| 10-06 17:18 | +10 stop | NEAR | DOWN | 0.56 | 0.29 | -3.03 |
| 10-06 17:18 | +10 stop | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-06 17:18 | +10 stop | ZEC | UP | 0.53 | 0.63 | 0.65 |
