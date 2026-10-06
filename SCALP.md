# Range-Scalp Bot

*Updated Tue Oct 06 22:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5540 | 4805 | 735 (9) | 2 | $-1666.95 | -4.8% |
| **+10¢** | 4235 | 3369 | 866 (15) | 2 | $-1581.07 | -5.9% |
| **+15¢** | 3550 | 2632 | 918 (19) | 2 | $-1373.76 | -6.2% |
| **+20¢** | 3173 | 2219 | 954 (26) | 2 | $-1091.88 | -5.5% |
| **+10¢ (15¢ stop)** | 6751 | 6736 | 15 (9) | 0 | $-2407.66 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 22:13 | +10 stop | ETH | DOWN | 0.63 | 0.92 | 2.67 |
| 10-06 22:13 | +20 | ETH | DOWN | 0.63 | 0.92 | 2.67 |
| 10-06 22:13 | +15 | ETH | DOWN | 0.63 | 0.92 | 2.67 |
| 10-06 22:13 | +10 | ETH | DOWN | 0.63 | 0.92 | 2.67 |
| 10-06 22:13 | +5 | ETH | DOWN | 0.63 | 0.71 | 0.48 |
| 10-06 22:11 | +10 stop | BTC | UP | 0.68 | 0.10 | -6.07 |
| 10-06 22:07 | +10 stop | DOGE | UP | 0.70 | 0.87 | 1.47 |
| 10-06 22:04 | +10 stop | BTC | UP | 0.63 | 0.87 | 2.15 |
| 10-06 22:03 | +10 stop | DOGE | UP | 0.71 | 0.54 | -2.03 |
| 10-06 22:03 | +10 stop | XRP | UP | 0.62 | 0.74 | 0.89 |
| 10-06 22:02 | +10 stop | SOL | UP | 0.62 | 0.75 | 0.99 |
| 10-06 22:02 | +20 | SOL | UP | 0.62 | 0.84 | 1.93 |
| 10-06 22:02 | +15 | SOL | UP | 0.62 | 0.84 | 1.93 |
| 10-06 22:02 | +10 | SOL | UP | 0.62 | 0.75 | 0.99 |
| 10-06 22:02 | +5 | SOL | UP | 0.62 | 0.69 | 0.38 |
| 10-06 22:02 | +10 stop | DOGE | DOWN | 0.62 | 0.44 | -2.15 |
| 10-06 22:02 | +10 | DOGE | DOWN | 0.62 | open |  |
| 10-06 22:02 | +5 | DOGE | DOWN | 0.62 | open |  |
| 10-06 22:02 | +5 | BTC | DOWN | 0.61 | 0.90 | 2.69 |
| 10-06 22:02 | +10 | ZEC | UP | 0.71 | 0.84 | 1.05 |
| 10-06 22:02 | +5 | ZEC | UP | 0.71 | 0.78 | 0.42 |
| 10-06 22:02 | +10 stop | ETH | DOWN | 0.47 | 0.59 | 0.85 |
| 10-06 22:02 | +10 stop | DOGE | DOWN | 0.51 | 0.62 | 0.75 |
| 10-06 22:02 | +20 | DOGE | DOWN | 0.51 | open |  |
| 10-06 22:02 | +15 | DOGE | DOWN | 0.51 | open |  |
| 10-06 22:02 | +10 | DOGE | DOWN | 0.51 | 0.62 | 0.75 |
| 10-06 22:02 | +5 | DOGE | DOWN | 0.51 | 0.62 | 0.75 |
| 10-06 22:01 | +10 stop | NEAR | UP | 0.53 | 0.33 | -2.34 |
| 10-06 22:01 | +20 | NEAR | UP | 0.53 | open |  |
| 10-06 22:01 | +15 | NEAR | UP | 0.52 | open |  |
| 10-06 22:01 | +10 | NEAR | UP | 0.53 | open |  |
| 10-06 22:01 | +5 | NEAR | UP | 0.53 | open |  |
| 10-06 22:01 | +10 stop | BTC | DOWN | 0.60 | 0.34 | -2.93 |
| 10-06 22:01 | +20 | BTC | DOWN | 0.60 | 0.90 | 2.79 |
| 10-06 22:01 | +15 | BTC | DOWN | 0.60 | 0.90 | 2.79 |
| 10-06 22:01 | +10 | BTC | DOWN | 0.60 | 0.90 | 2.79 |
| 10-06 22:01 | +5 | BTC | DOWN | 0.60 | 0.66 | 0.27 |
| 10-06 22:01 | +10 stop | ETH | UP | 0.56 | 0.40 | -1.95 |
| 10-06 22:01 | +20 | ETH | UP | 0.59 | 0.83 | 2.13 |
| 10-06 22:01 | +15 | ETH | UP | 0.59 | 0.83 | 2.13 |
