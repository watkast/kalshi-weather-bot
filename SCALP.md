# Range-Scalp Bot

*Updated Sat Oct 10 12:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10389 | 8961 | 1428 (22) | 1 | $-3513.02 | -5.4% |
| **+10¢** | 7862 | 6199 | 1663 (35) | 2 | $-3346.65 | -6.8% |
| **+15¢** | 6631 | 4867 | 1764 (51) | 2 | $-2830.41 | -6.8% |
| **+20¢** | 5895 | 4058 | 1837 (65) | 2 | $-2397.30 | -6.5% |
| **+10¢ (15¢ stop)** | 12753 | 12715 | 38 (25) | 1 | $-4985.99 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 12:09 | +10 stop | NEAR | DOWN | 0.62 | 0.78 | 1.30 |
| 10-10 12:09 | +10 stop | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 10-10 12:09 | +20 | ETH | DOWN | 0.70 | 0.91 | 1.88 |
| 10-10 12:09 | +15 | ETH | DOWN | 0.70 | 0.91 | 1.88 |
| 10-10 12:09 | +10 | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 10-10 12:09 | +5 | ETH | DOWN | 0.70 | 0.76 | 0.32 |
| 10-10 12:09 | +10 stop | HYPE | UP | 0.62 | 0.46 | -1.95 |
| 10-10 12:08 | +10 stop | DOGE | DOWN | 0.68 | 0.51 | -1.99 |
| 10-10 12:08 | +5 | DOGE | DOWN | 0.68 | 0.76 | 0.56 |
| 10-10 12:06 | +10 stop | BTC | DOWN | 0.67 | open |  |
| 10-10 12:06 | +10 | BTC | DOWN | 0.67 | open |  |
| 10-10 12:06 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 10-10 12:05 | +10 stop | NEAR | DOWN | 0.59 | 0.44 | -1.88 |
| 10-10 12:05 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-10 12:05 | +10 stop | HYPE | DOWN | 0.62 | 0.45 | -2.05 |
| 10-10 12:04 | +5 | BTC | DOWN | 0.59 | 0.67 | 0.47 |
| 10-10 12:04 | +5 | BTC | DOWN | 0.56 | 0.68 | 0.86 |
| 10-10 12:03 | +10 stop | HYPE | DOWN | 0.61 | 0.46 | -1.85 |
| 10-10 12:03 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 10-10 12:02 | +10 stop | XRP | DOWN | 0.67 | 0.79 | 0.92 |
| 10-10 12:02 | +10 | XRP | DOWN | 0.67 | 0.79 | 0.92 |
| 10-10 12:02 | +5 | XRP | DOWN | 0.67 | 0.73 | 0.30 |
| 10-10 12:02 | +10 stop | NEAR | UP | 0.65 | 0.43 | -2.54 |
| 10-10 12:02 | +10 stop | DOGE | DOWN | 0.70 | 0.53 | -2.03 |
| 10-10 12:02 | +20 | DOGE | DOWN | 0.70 | 0.91 | 1.87 |
| 10-10 12:02 | +15 | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-10 12:02 | +10 | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-10 12:02 | +5 | DOGE | DOWN | 0.71 | 0.79 | 0.53 |
| 10-10 12:02 | +10 stop | HYPE | DOWN | 0.63 | 0.42 | -2.49 |
| 10-10 12:02 | +20 | HYPE | DOWN | 0.63 | 0.84 | 1.79 |
| 10-10 12:02 | +15 | HYPE | DOWN | 0.63 | 0.79 | 1.27 |
| 10-10 12:02 | +10 | HYPE | DOWN | 0.63 | 0.75 | 0.85 |
| 10-10 12:02 | +5 | HYPE | DOWN | 0.63 | 0.69 | 0.24 |
| 10-10 12:02 | +10 stop | NEAR | DOWN | 0.57 | 0.37 | -2.35 |
| 10-10 12:02 | +20 | NEAR | DOWN | 0.57 | 0.78 | 1.79 |
| 10-10 12:02 | +15 | NEAR | DOWN | 0.57 | 0.78 | 1.79 |
| 10-10 12:02 | +10 | NEAR | DOWN | 0.57 | 0.69 | 0.87 |
| 10-10 12:02 | +5 | NEAR | DOWN | 0.57 | 0.66 | 0.56 |
| 10-10 12:01 | +10 stop | ETH | DOWN | 0.64 | 0.79 | 1.21 |
| 10-10 12:01 | +20 | ETH | DOWN | 0.64 | 0.84 | 1.73 |
