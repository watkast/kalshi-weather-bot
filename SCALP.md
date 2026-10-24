# Range-Scalp Bot

*Updated Sat Oct 24 13:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32067 | 27954 | 4113 (40) | 0 | $-9196.68 | -4.6% |
| **+10¢** | 23996 | 19240 | 4756 (58) | 1 | $-8208.96 | -5.4% |
| **+15¢** | 20089 | 14973 | 5116 (81) | 1 | $-7363.79 | -5.8% |
| **+20¢** | 17795 | 12439 | 5356 (103) | 2 | $-6549.05 | -5.9% |
| **+10¢ (15¢ stop)** | 39396 | 39337 | 59 (32) | 0 | $-15078.98 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 13:27 | +10 | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 10-24 13:27 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
| 10-24 13:25 | +5 | ETH | DOWN | 0.55 | 0.60 | 0.15 |
| 10-24 13:25 | +10 stop | ETH | DOWN | 0.57 | 0.69 | 0.87 |
| 10-24 13:25 | +20 | ETH | DOWN | 0.55 | 0.78 | 1.99 |
| 10-24 13:25 | +15 | ETH | DOWN | 0.55 | 0.71 | 1.27 |
| 10-24 13:25 | +10 | ETH | DOWN | 0.55 | 0.69 | 1.07 |
| 10-24 13:25 | +5 | ETH | DOWN | 0.55 | 0.64 | 0.55 |
| 10-24 13:24 | +10 stop | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-24 13:24 | +10 stop | XRP | DOWN | 0.56 | 0.76 | 1.69 |
| 10-24 13:24 | +5 | XRP | DOWN | 0.56 | 0.63 | 0.35 |
| 10-24 13:21 | +10 stop | XRP | UP | 0.54 | 0.30 | -2.73 |
| 10-24 13:21 | +10 stop | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 10-24 13:21 | +10 stop | NEAR | DOWN | 0.62 | 0.77 | 1.20 |
| 10-24 13:21 | +20 | NEAR | DOWN | 0.62 | 0.83 | 1.83 |
| 10-24 13:21 | +15 | NEAR | DOWN | 0.62 | 0.77 | 1.20 |
| 10-24 13:21 | +10 | NEAR | DOWN | 0.62 | 0.77 | 1.20 |
| 10-24 13:21 | +5 | NEAR | DOWN | 0.62 | 0.67 | 0.17 |
| 10-24 13:21 | +10 stop | ZEC | DOWN | 0.71 | 0.92 | 1.91 |
| 10-24 13:21 | +5 | ZEC | DOWN | 0.69 | 0.77 | 0.52 |
| 10-24 13:20 | +10 stop | XRP | DOWN | 0.71 | 0.51 | -2.33 |
| 10-24 13:20 | +20 | XRP | DOWN | 0.71 | 0.92 | 1.93 |
| 10-24 13:20 | +15 | XRP | DOWN | 0.70 | 0.87 | 1.48 |
| 10-24 13:20 | +10 | XRP | DOWN | 0.69 | 0.87 | 1.57 |
| 10-24 13:20 | +5 | XRP | DOWN | 0.69 | 0.76 | 0.42 |
| 10-24 13:18 | +10 stop | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 10-24 13:18 | +10 | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 10-24 13:18 | +5 | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 10-24 13:17 | +10 stop | ZEC | UP | 0.52 | 0.23 | -3.21 |
| 10-24 13:17 | +20 | ZEC | UP | 0.52 | open |  |
| 10-24 13:17 | +15 | ZEC | UP | 0.52 | open |  |
| 10-24 13:17 | +10 | ZEC | UP | 0.52 | open |  |
| 10-24 13:17 | +5 | ZEC | UP | 0.52 | 0.58 | 0.24 |
| 10-24 13:17 | +10 stop | NEAR | UP | 0.58 | 0.26 | -3.52 |
| 10-24 13:16 | +10 stop | ETH | DOWN | 0.57 | 0.69 | 0.87 |
| 10-24 13:16 | +20 | ETH | DOWN | 0.57 | 0.85 | 2.53 |
| 10-24 13:16 | +15 | ETH | DOWN | 0.57 | 0.76 | 1.59 |
| 10-24 13:16 | +10 | ETH | DOWN | 0.57 | 0.69 | 0.87 |
| 10-24 13:16 | +5 | ETH | DOWN | 0.58 | 0.69 | 0.78 |
| 10-24 13:16 | +10 stop | DOGE | DOWN | 0.65 | 0.79 | 1.16 |
