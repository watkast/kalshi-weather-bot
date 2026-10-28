# Range-Scalp Bot

*Updated Wed Oct 28 03:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37486 | 32721 | 4765 (45) | 1 | $-10468.74 | -4.4% |
| **+10¢** | 27990 | 22473 | 5517 (67) | 1 | $-9334.00 | -5.3% |
| **+15¢** | 23419 | 17495 | 5924 (91) | 1 | $-8290.52 | -5.6% |
| **+20¢** | 20761 | 14562 | 6199 (116) | 2 | $-7243.43 | -5.6% |
| **+10¢ (15¢ stop)** | 45916 | 45851 | 65 (34) | 0 | $-17482.42 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 03:13 | +10 stop | SOL | DOWN | 0.54 | 0.77 | 1.99 |
| 10-28 03:13 | +10 stop | SOL | DOWN | 0.69 | 0.50 | -2.23 |
| 10-28 03:13 | +20 | SOL | DOWN | 0.69 | open |  |
| 10-28 03:13 | +15 | SOL | DOWN | 0.66 | 0.82 | 1.33 |
| 10-28 03:13 | +10 | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 10-28 03:13 | +5 | SOL | DOWN | 0.66 | 0.77 | 0.81 |
| 10-28 03:12 | +10 stop | DOGE | UP | 0.65 | 0.78 | 1.01 |
| 10-28 03:08 | +10 stop | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-28 03:08 | +5 | ZEC | DOWN | 0.65 | 0.74 | 0.60 |
| 10-28 03:08 | +10 stop | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 10-28 03:08 | +20 | SOL | DOWN | 0.66 | 0.86 | 1.75 |
| 10-28 03:08 | +15 | SOL | DOWN | 0.66 | 0.84 | 1.54 |
| 10-28 03:08 | +10 | SOL | DOWN | 0.66 | 0.84 | 1.54 |
| 10-28 03:08 | +5 | SOL | DOWN | 0.67 | 0.73 | 0.30 |
| 10-28 03:07 | +10 stop | ZEC | DOWN | 0.50 | 0.63 | 0.95 |
| 10-28 03:07 | +5 | ZEC | DOWN | 0.50 | 0.63 | 0.95 |
| 10-28 03:06 | +10 stop | ZEC | UP | 0.52 | 0.35 | -2.04 |
| 10-28 03:06 | +10 stop | NEAR | DOWN | 0.64 | 0.79 | 1.21 |
| 10-28 03:06 | +20 | NEAR | DOWN | 0.64 | 0.86 | 1.94 |
| 10-28 03:06 | +15 | NEAR | DOWN | 0.64 | 0.79 | 1.21 |
| 10-28 03:06 | +10 | NEAR | DOWN | 0.64 | 0.79 | 1.23 |
| 10-28 03:06 | +5 | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 10-28 03:06 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 10-28 03:06 | +20 | XRP | DOWN | 0.70 | 0.92 | 2.04 |
| 10-28 03:06 | +15 | XRP | DOWN | 0.70 | 0.85 | 1.26 |
| 10-28 03:06 | +10 | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 10-28 03:06 | +5 | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 10-28 03:06 | +10 stop | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-28 03:06 | +10 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-28 03:06 | +5 | BTC | DOWN | 0.61 | 0.69 | 0.48 |
| 10-28 03:05 | +10 stop | DOGE | UP | 0.65 | 0.50 | -1.84 |
| 10-28 03:04 | +10 stop | DOGE | UP | 0.54 | 0.65 | 0.76 |
| 10-28 03:03 | +5 | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 10-28 03:02 | +5 | NEAR | DOWN | 0.59 | 0.65 | 0.27 |
| 10-28 03:02 | +10 stop | DOGE | DOWN | 0.65 | 0.48 | -2.04 |
| 10-28 03:02 | +20 | DOGE | DOWN | 0.65 | open |  |
| 10-28 03:02 | +15 | DOGE | DOWN | 0.65 | open |  |
| 10-28 03:02 | +10 | DOGE | DOWN | 0.65 | open |  |
| 10-28 03:02 | +5 | DOGE | DOWN | 0.66 | open |  |
| 10-28 03:01 | +10 stop | ETH | DOWN | 0.67 | 0.83 | 1.34 |
