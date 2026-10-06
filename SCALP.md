# Range-Scalp Bot

*Updated Tue Oct 06 11:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4975 | 4304 | 671 (7) | 3 | $-1582.68 | -5.0% |
| **+10¢** | 3818 | 3037 | 781 (11) | 2 | $-1449.39 | -6.0% |
| **+15¢** | 3208 | 2380 | 828 (14) | 5 | $-1254.81 | -6.2% |
| **+20¢** | 2873 | 2009 | 864 (19) | 6 | $-1034.00 | -5.7% |
| **+10¢ (15¢ stop)** | 6083 | 6070 | 13 (8) | 2 | $-2172.40 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 11:02 | +10 stop | BNB | UP | 0.68 | open |  |
| 10-06 11:02 | +5 | NEAR | DOWN | 0.56 | open |  |
| 10-06 11:02 | +5 | ZEC | UP | 0.71 | open |  |
| 10-06 11:02 | +5 | DOGE | UP | 0.70 | 0.77 | 0.42 |
| 10-06 11:02 | +10 stop | ETH | UP | 0.63 | 0.73 | 0.69 |
| 10-06 11:02 | +20 | ETH | UP | 0.63 | open |  |
| 10-06 11:02 | +15 | ETH | UP | 0.63 | open |  |
| 10-06 11:02 | +10 | ETH | UP | 0.64 | 0.77 | 1.00 |
| 10-06 11:02 | +5 | ETH | UP | 0.64 | 0.73 | 0.59 |
| 10-06 11:01 | +10 stop | NEAR | DOWN | 0.52 | open |  |
| 10-06 11:01 | +20 | NEAR | DOWN | 0.51 | open |  |
| 10-06 11:01 | +15 | NEAR | DOWN | 0.51 | open |  |
| 10-06 11:01 | +10 | NEAR | DOWN | 0.51 | open |  |
| 10-06 11:01 | +5 | NEAR | DOWN | 0.51 | 0.57 | 0.24 |
| 10-06 11:01 | +10 stop | BNB | DOWN | 0.67 | 0.38 | -3.23 |
| 10-06 11:01 | +20 | BNB | DOWN | 0.67 | open |  |
| 10-06 11:01 | +15 | BNB | DOWN | 0.67 | open |  |
| 10-06 11:01 | +10 | BNB | DOWN | 0.67 | open |  |
| 10-06 11:01 | +5 | BNB | DOWN | 0.67 | open |  |
| 10-06 11:01 | +10 stop | SOL | UP | 0.62 | 0.73 | 0.79 |
| 10-06 11:01 | +20 | SOL | UP | 0.62 | 0.84 | 1.93 |
| 10-06 11:01 | +15 | SOL | UP | 0.62 | 0.84 | 1.93 |
| 10-06 11:01 | +10 | SOL | UP | 0.62 | 0.73 | 0.79 |
| 10-06 11:01 | +5 | SOL | UP | 0.62 | 0.73 | 0.79 |
| 10-06 11:01 | +10 stop | BTC | UP | 0.61 | 0.74 | 0.99 |
| 10-06 11:01 | +20 | BTC | UP | 0.61 | open |  |
| 10-06 11:01 | +15 | BTC | UP | 0.61 | open |  |
| 10-06 11:01 | +10 | BTC | UP | 0.61 | 0.74 | 0.99 |
| 10-06 11:01 | +5 | BTC | UP | 0.61 | 0.74 | 0.99 |
| 10-06 11:01 | +10 stop | ZEC | UP | 0.61 | 0.74 | 0.99 |
| 10-06 11:01 | +20 | ZEC | UP | 0.61 | open |  |
| 10-06 11:01 | +15 | ZEC | UP | 0.61 | open |  |
| 10-06 11:01 | +10 | ZEC | UP | 0.61 | 0.74 | 0.99 |
| 10-06 11:01 | +5 | ZEC | UP | 0.61 | 0.70 | 0.58 |
| 10-06 11:01 | +10 stop | XRP | UP | 0.58 | 0.74 | 1.28 |
| 10-06 11:01 | +20 | XRP | UP | 0.58 | 0.79 | 1.80 |
| 10-06 11:01 | +15 | XRP | UP | 0.58 | 0.74 | 1.28 |
| 10-06 11:01 | +10 | XRP | UP | 0.58 | 0.74 | 1.28 |
| 10-06 11:01 | +5 | XRP | UP | 0.58 | 0.64 | 0.25 |
| 10-06 11:01 | +10 stop | DOGE | UP | 0.61 | 0.77 | 1.30 |
