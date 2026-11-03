# Range-Scalp Bot

*Updated Tue Nov 03 03:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45499 | 39616 | 5883 (69) | 2 | $-13137.82 | -4.6% |
| **+10¢** | 33963 | 27147 | 6816 (91) | 2 | $-12016.36 | -5.6% |
| **+15¢** | 28414 | 21079 | 7335 (119) | 2 | $-11044.25 | -6.2% |
| **+20¢** | 25234 | 17553 | 7681 (154) | 3 | $-9795.89 | -6.2% |
| **+10¢ (15¢ stop)** | 55521 | 55432 | 89 (53) | 0 | $-20940.53 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 03:09 | +10 stop | ETH | UP | 0.70 | 0.83 | 1.05 |
| 11-03 03:07 | +10 stop | BTC | UP | 0.70 | 0.81 | 0.84 |
| 11-03 03:07 | +10 | BTC | UP | 0.70 | 0.81 | 0.84 |
| 11-03 03:07 | +5 | BTC | UP | 0.70 | 0.75 | 0.21 |
| 11-03 03:07 | +10 stop | HYPE | UP | 0.66 | 0.81 | 1.23 |
| 11-03 03:07 | +10 stop | DOGE | UP | 0.71 | 0.86 | 1.26 |
| 11-03 03:07 | +15 | DOGE | UP | 0.71 | 0.86 | 1.26 |
| 11-03 03:07 | +10 stop | BTC | UP | 0.54 | 0.65 | 0.76 |
| 11-03 03:07 | +15 | BTC | UP | 0.54 | 0.69 | 1.17 |
| 11-03 03:07 | +10 | BTC | UP | 0.54 | 0.65 | 0.76 |
| 11-03 03:07 | +5 | BTC | UP | 0.51 | 0.65 | 1.06 |
| 11-03 03:07 | +10 stop | HYPE | UP | 0.49 | 0.59 | 0.65 |
| 11-03 03:06 | +10 stop | ETH | DOWN | 0.64 | 0.43 | -2.45 |
| 11-03 03:06 | +20 | ETH | DOWN | 0.64 | open |  |
| 11-03 03:06 | +15 | ETH | DOWN | 0.65 | open |  |
| 11-03 03:06 | +10 | ETH | DOWN | 0.64 | open |  |
| 11-03 03:06 | +5 | ETH | DOWN | 0.67 | open |  |
| 11-03 03:06 | +10 stop | BNB | UP | 0.71 | 0.86 | 1.26 |
| 11-03 03:06 | +10 stop | XRP | DOWN | 0.63 | 0.43 | -2.35 |
| 11-03 03:06 | +20 | XRP | DOWN | 0.64 | open |  |
| 11-03 03:06 | +15 | XRP | DOWN | 0.64 | open |  |
| 11-03 03:06 | +10 | XRP | DOWN | 0.65 | open |  |
| 11-03 03:06 | +5 | XRP | DOWN | 0.65 | open |  |
| 11-03 03:06 | +10 stop | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 11-03 03:06 | +5 | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 11-03 03:06 | +10 stop | SOL | UP | 0.66 | 0.76 | 0.71 |
| 11-03 03:05 | +10 stop | BNB | DOWN | 0.43 | 0.54 | 0.74 |
| 11-03 03:05 | +10 stop | HYPE | DOWN | 0.68 | 0.49 | -2.28 |
| 11-03 03:05 | +10 stop | DOGE | DOWN | 0.70 | 0.45 | -2.83 |
| 11-03 03:04 | +10 stop | SOL | DOWN | 0.63 | 0.37 | -2.94 |
| 11-03 03:04 | +5 | ZEC | UP | 0.67 | 0.79 | 0.92 |
| 11-03 03:04 | +10 stop | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 11-03 03:04 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-03 03:03 | +10 stop | DOGE | UP | 0.53 | 0.32 | -2.44 |
| 11-03 03:03 | +20 | DOGE | UP | 0.53 | 0.78 | 2.19 |
| 11-03 03:03 | +15 | DOGE | UP | 0.53 | 0.71 | 1.47 |
| 11-03 03:03 | +10 | DOGE | UP | 0.53 | 0.71 | 1.47 |
| 11-03 03:03 | +5 | DOGE | UP | 0.53 | 0.58 | 0.14 |
| 11-03 03:03 | +10 stop | XRP | DOWN | 0.57 | 0.67 | 0.66 |
| 11-03 03:03 | +10 | XRP | DOWN | 0.58 | 0.70 | 0.87 |
