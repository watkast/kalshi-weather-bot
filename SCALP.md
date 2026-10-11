# Range-Scalp Bot

*Updated Sun Oct 11 23:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12645 | 10916 | 1729 (25) | 2 | $-4169.42 | -5.2% |
| **+10¢** | 9592 | 7591 | 2001 (37) | 2 | $-3904.91 | -6.5% |
| **+15¢** | 8072 | 5943 | 2129 (55) | 2 | $-3363.38 | -6.6% |
| **+20¢** | 7196 | 4976 | 2220 (69) | 2 | $-2862.00 | -6.3% |
| **+10¢ (15¢ stop)** | 15565 | 15524 | 41 (25) | 2 | $-6067.67 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 23:06 | +10 stop | NEAR | UP | 0.65 | open |  |
| 10-11 23:06 | +5 | NEAR | UP | 0.65 | open |  |
| 10-11 23:05 | +10 stop | XRP | UP | 0.63 | open |  |
| 10-11 23:05 | +10 | XRP | UP | 0.63 | open |  |
| 10-11 23:05 | +5 | XRP | UP | 0.63 | open |  |
| 10-11 23:04 | +10 stop | XRP | UP | 0.59 | 0.71 | 0.88 |
| 10-11 23:04 | +10 | XRP | UP | 0.59 | 0.71 | 0.87 |
| 10-11 23:04 | +5 | XRP | UP | 0.59 | 0.67 | 0.47 |
| 10-11 23:02 | +10 stop | NEAR | UP | 0.67 | 0.78 | 0.81 |
| 10-11 23:01 | +5 | NEAR | UP | 0.64 | 0.72 | 0.48 |
| 10-11 23:01 | +10 stop | XRP | UP | 0.61 | 0.75 | 1.09 |
| 10-11 23:01 | +20 | XRP | UP | 0.61 | open |  |
| 10-11 23:01 | +15 | XRP | UP | 0.61 | open |  |
| 10-11 23:01 | +10 | XRP | UP | 0.61 | 0.75 | 1.09 |
| 10-11 23:01 | +5 | XRP | UP | 0.61 | 0.70 | 0.58 |
| 10-11 23:01 | +10 stop | ETH | UP | 0.69 | 0.80 | 0.83 |
| 10-11 23:01 | +20 | ETH | UP | 0.69 | 0.91 | 2.03 |
| 10-11 23:01 | +15 | ETH | UP | 0.69 | 0.86 | 1.46 |
| 10-11 23:01 | +10 | ETH | UP | 0.69 | 0.80 | 0.83 |
| 10-11 23:01 | +5 | ETH | UP | 0.69 | 0.74 | 0.21 |
| 10-11 23:00 | +10 stop | NEAR | DOWN | 0.54 | 0.38 | -1.95 |
| 10-11 23:00 | +20 | NEAR | DOWN | 0.54 | open |  |
| 10-11 23:00 | +15 | NEAR | DOWN | 0.54 | open |  |
| 10-11 23:00 | +10 | NEAR | DOWN | 0.54 | open |  |
| 10-11 23:00 | +5 | NEAR | DOWN | 0.56 | 0.62 | 0.25 |
| 10-11 23:00 | +10 stop | DOGE | UP | 0.67 | 0.81 | 1.13 |
| 10-11 23:00 | +20 | DOGE | UP | 0.67 | 0.87 | 1.76 |
| 10-11 23:00 | +15 | DOGE | UP | 0.64 | 0.81 | 1.42 |
| 10-11 23:00 | +10 | DOGE | UP | 0.64 | 0.74 | 0.69 |
| 10-11 23:00 | +5 | DOGE | UP | 0.64 | 0.69 | 0.18 |
| 10-11 22:55 | +10 stop | BNB | DOWN | 0.48 | 0.59 | 0.76 |
| 10-11 22:55 | +5 | BNB | DOWN | 0.48 | 0.59 | 0.76 |
| 10-11 22:53 | +10 stop | HYPE | DOWN | 0.60 | 0.72 | 0.88 |
| 10-11 22:53 | +10 | HYPE | DOWN | 0.60 | 0.72 | 0.88 |
| 10-11 22:53 | +5 | HYPE | DOWN | 0.60 | 0.72 | 0.88 |
| 10-11 22:52 | +10 stop | BNB | DOWN | 0.50 | 0.35 | -1.84 |
| 10-11 22:52 | +10 stop | HYPE | DOWN | 0.55 | 0.67 | 0.86 |
| 10-11 22:52 | +10 | HYPE | DOWN | 0.55 | 0.67 | 0.86 |
| 10-11 22:52 | +5 | HYPE | DOWN | 0.55 | 0.67 | 0.86 |
| 10-11 22:51 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
