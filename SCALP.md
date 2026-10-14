# Range-Scalp Bot

*Updated Wed Oct 14 01:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15262 | 13205 | 2057 (27) | 1 | $-4926.25 | -5.1% |
| **+10¢** | 11546 | 9159 | 2387 (39) | 1 | $-4597.92 | -6.3% |
| **+15¢** | 9701 | 7145 | 2556 (58) | 1 | $-4093.01 | -6.7% |
| **+20¢** | 8626 | 5954 | 2672 (74) | 1 | $-3598.63 | -6.6% |
| **+10¢ (15¢ stop)** | 18696 | 18646 | 50 (29) | 0 | $-7192.50 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 01:41 | +10 stop | BTC | DOWN | 0.62 | 0.29 | -3.62 |
| 10-14 01:41 | +20 | BTC | DOWN | 0.62 | open |  |
| 10-14 01:41 | +15 | BTC | DOWN | 0.62 | open |  |
| 10-14 01:41 | +10 | BTC | DOWN | 0.62 | open |  |
| 10-14 01:41 | +5 | BTC | DOWN | 0.62 | open |  |
| 10-14 01:39 | +10 stop | ZEC | UP | 0.71 | 0.82 | 0.84 |
| 10-14 01:39 | +10 | ZEC | UP | 0.70 | 0.82 | 0.94 |
| 10-14 01:39 | +5 | ZEC | UP | 0.70 | 0.76 | 0.32 |
| 10-14 01:37 | +5 | ZEC | UP | 0.67 | 0.78 | 0.81 |
| 10-14 01:37 | +5 | ZEC | UP | 0.46 | 0.53 | 0.34 |
| 10-14 01:36 | +10 stop | ZEC | UP | 0.67 | 0.78 | 0.81 |
| 10-14 01:36 | +20 | ZEC | UP | 0.67 | 0.94 | 2.45 |
| 10-14 01:36 | +15 | ZEC | UP | 0.67 | 0.82 | 1.23 |
| 10-14 01:36 | +10 | ZEC | UP | 0.67 | 0.78 | 0.81 |
| 10-14 01:36 | +5 | ZEC | UP | 0.67 | 0.72 | 0.19 |
| 10-14 01:35 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 10-14 01:35 | +5 | DOGE | DOWN | 0.66 | 0.75 | 0.60 |
| 10-14 01:34 | +5 | DOGE | DOWN | 0.62 | 0.68 | 0.27 |
| 10-14 01:34 | +10 stop | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 10-14 01:34 | +20 | SOL | DOWN | 0.65 | 0.86 | 1.85 |
| 10-14 01:34 | +15 | SOL | DOWN | 0.65 | 0.86 | 1.85 |
| 10-14 01:34 | +10 | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 10-14 01:34 | +5 | SOL | DOWN | 0.65 | 0.73 | 0.50 |
| 10-14 01:34 | +10 stop | ETH | DOWN | 0.59 | 0.73 | 1.09 |
| 10-14 01:34 | +10 | ETH | DOWN | 0.59 | 0.73 | 1.09 |
| 10-14 01:34 | +5 | ETH | DOWN | 0.59 | 0.68 | 0.57 |
| 10-14 01:34 | +10 stop | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-14 01:34 | +20 | BTC | DOWN | 0.68 | 0.92 | 2.16 |
| 10-14 01:34 | +15 | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-14 01:34 | +10 | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 10-14 01:34 | +5 | BTC | DOWN | 0.66 | 0.74 | 0.50 |
| 10-14 01:34 | +10 stop | DOGE | DOWN | 0.59 | 0.75 | 1.29 |
| 10-14 01:34 | +15 | DOGE | DOWN | 0.59 | 0.75 | 1.29 |
| 10-14 01:34 | +10 | DOGE | DOWN | 0.59 | 0.75 | 1.29 |
| 10-14 01:34 | +5 | DOGE | DOWN | 0.59 | 0.66 | 0.37 |
| 10-14 01:32 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-14 01:32 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 10-14 01:32 | +10 stop | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 10-14 01:32 | +20 | ETH | DOWN | 0.69 | 0.90 | 1.90 |
| 10-14 01:32 | +15 | ETH | DOWN | 0.69 | 0.84 | 1.25 |
