# Range-Scalp Bot

*Updated Tue Oct 06 09:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4865 | 4208 | 657 (7) | 0 | $-1540.30 | -5.0% |
| **+10¢** | 3738 | 2972 | 766 (11) | 1 | $-1425.61 | -6.1% |
| **+15¢** | 3139 | 2327 | 812 (14) | 3 | $-1237.92 | -6.3% |
| **+20¢** | 2811 | 1964 | 847 (19) | 4 | $-1023.65 | -5.8% |
| **+10¢ (15¢ stop)** | 5953 | 5940 | 13 (8) | 1 | $-2122.87 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 09:31 | +10 stop | HYPE | DOWN | 0.52 | open |  |
| 10-06 09:31 | +20 | HYPE | DOWN | 0.52 | open |  |
| 10-06 09:31 | +15 | HYPE | DOWN | 0.52 | open |  |
| 10-06 09:31 | +10 | HYPE | DOWN | 0.52 | open |  |
| 10-06 09:31 | +5 | HYPE | DOWN | 0.52 | 0.58 | 0.24 |
| 10-06 09:31 | +10 stop | NEAR | UP | 0.69 | 0.80 | 0.83 |
| 10-06 09:31 | +20 | NEAR | UP | 0.69 | open |  |
| 10-06 09:31 | +15 | NEAR | UP | 0.69 | open |  |
| 10-06 09:31 | +10 | NEAR | UP | 0.69 | 0.80 | 0.83 |
| 10-06 09:31 | +5 | NEAR | UP | 0.69 | 0.77 | 0.52 |
| 10-06 09:31 | +10 stop | SOL | UP | 0.67 | 0.77 | 0.71 |
| 10-06 09:31 | +20 | SOL | UP | 0.67 | open |  |
| 10-06 09:31 | +15 | SOL | UP | 0.67 | open |  |
| 10-06 09:31 | +10 | SOL | UP | 0.67 | 0.77 | 0.71 |
| 10-06 09:31 | +5 | SOL | UP | 0.67 | 0.74 | 0.40 |
| 10-06 09:30 | +10 stop | BTC | UP | 0.70 | 0.83 | 1.05 |
| 10-06 09:30 | +20 | BTC | UP | 0.70 | open |  |
| 10-06 09:30 | +15 | BTC | UP | 0.70 | 0.88 | 1.57 |
| 10-06 09:30 | +10 | BTC | UP | 0.70 | 0.83 | 1.05 |
| 10-06 09:30 | +5 | BTC | UP | 0.70 | 0.75 | 0.21 |
| 10-06 09:27 | +10 stop | DOGE | DOWN | 0.69 | 0.79 | 0.74 |
| 10-06 09:27 | +5 | DOGE | DOWN | 0.69 | 0.79 | 0.74 |
| 10-06 09:26 | +10 stop | XRP | DOWN | 0.62 | 0.30 | -3.52 |
| 10-06 09:26 | +20 | XRP | DOWN | 0.62 | 0.83 | 1.83 |
| 10-06 09:26 | +15 | XRP | DOWN | 0.62 | 0.83 | 1.83 |
| 10-06 09:26 | +10 | XRP | DOWN | 0.62 | 0.83 | 1.83 |
| 10-06 09:26 | +5 | XRP | DOWN | 0.62 | 0.83 | 1.83 |
| 10-06 09:26 | +10 stop | DOGE | DOWN | 0.62 | 0.41 | -2.44 |
| 10-06 09:26 | +20 | DOGE | DOWN | 0.62 | 0.99 | 3.53 |
| 10-06 09:26 | +15 | DOGE | DOWN | 0.62 | 0.79 | 1.41 |
| 10-06 09:26 | +10 | DOGE | DOWN | 0.62 | 0.79 | 1.41 |
| 10-06 09:26 | +5 | DOGE | DOWN | 0.62 | 0.68 | 0.27 |
| 10-06 09:26 | +10 stop | HYPE | UP | 0.22 | 0.62 | 3.70 |
| 10-06 09:26 | +10 | HYPE | UP | 0.22 | 0.62 | 3.70 |
| 10-06 09:25 | +10 stop | HYPE | DOWN | 0.56 | 0.38 | -2.15 |
| 10-06 09:25 | +5 | HYPE | DOWN | 0.56 | 0.84 | 2.52 |
| 10-06 09:23 | +5 | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-06 09:23 | +10 stop | HYPE | UP | 0.51 | 0.35 | -1.94 |
| 10-06 09:23 | +20 | HYPE | UP | 0.51 | no | -5.28 |
| 10-06 09:23 | +15 | HYPE | UP | 0.51 | no | -5.28 |
