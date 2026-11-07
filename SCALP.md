# Range-Scalp Bot

*Updated Sat Nov 07 19:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51385 | 44801 | 6584 (79) | 2 | $-14295.21 | -4.4% |
| **+10¢** | 38347 | 30671 | 7676 (105) | 2 | $-13302.44 | -5.5% |
| **+15¢** | 32105 | 23831 | 8274 (134) | 2 | $-12224.51 | -6.1% |
| **+20¢** | 28555 | 19882 | 8673 (177) | 2 | $-10793.47 | -6.0% |
| **+10¢ (15¢ stop)** | 62572 | 62469 | 103 (61) | 2 | $-23144.27 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 19:01 | +10 stop | BNB | DOWN | 0.57 | open |  |
| 11-07 19:01 | +20 | BNB | DOWN | 0.57 | open |  |
| 11-07 19:01 | +15 | BNB | DOWN | 0.57 | open |  |
| 11-07 19:01 | +10 | BNB | DOWN | 0.57 | open |  |
| 11-07 19:01 | +5 | BNB | DOWN | 0.57 | open |  |
| 11-07 19:01 | +10 stop | BTC | DOWN | 0.71 | open |  |
| 11-07 19:01 | +20 | BTC | DOWN | 0.71 | open |  |
| 11-07 19:01 | +15 | BTC | DOWN | 0.71 | open |  |
| 11-07 19:01 | +10 | BTC | DOWN | 0.71 | open |  |
| 11-07 19:01 | +5 | BTC | DOWN | 0.71 | open |  |
| 11-07 18:57 | +10 stop | ZEC | UP | 0.64 | 0.89 | 2.26 |
| 11-07 18:56 | +10 stop | ZEC | DOWN | 0.59 | 0.42 | -2.05 |
| 11-07 18:56 | +5 | BNB | UP | 0.65 | 0.74 | 0.60 |
| 11-07 18:56 | +10 stop | BNB | UP | 0.68 | 0.92 | 2.13 |
| 11-07 18:55 | +10 stop | BTC | DOWN | 0.65 | 0.36 | -3.23 |
| 11-07 18:55 | +20 | BTC | DOWN | 0.65 | 0.97 | 3.07 |
| 11-07 18:55 | +15 | BTC | DOWN | 0.65 | 0.84 | 1.64 |
| 11-07 18:55 | +10 | BTC | DOWN | 0.64 | 0.84 | 1.73 |
| 11-07 18:55 | +5 | BTC | DOWN | 0.64 | 0.71 | 0.38 |
| 11-07 18:54 | +5 | ZEC | DOWN | 0.71 | yes | -7.25 |
| 11-07 18:53 | +5 | XRP | UP | 0.64 | 0.78 | 1.10 |
| 11-07 18:53 | +5 | ZEC | DOWN | 0.70 | 0.76 | 0.32 |
| 11-07 18:51 | +5 | ZEC | DOWN | 0.59 | 0.65 | 0.27 |
| 11-07 18:51 | +10 stop | NEAR | DOWN | 0.65 | 0.40 | -2.83 |
| 11-07 18:51 | +10 | NEAR | DOWN | 0.65 | yes | -6.66 |
| 11-07 18:51 | +10 stop | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-07 18:51 | +10 | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-07 18:51 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 11-07 18:51 | +10 stop | ETH | DOWN | 0.56 | 0.28 | -3.13 |
| 11-07 18:51 | +15 | ETH | DOWN | 0.56 | yes | -5.78 |
| 11-07 18:51 | +10 | ETH | DOWN | 0.57 | yes | -5.88 |
| 11-07 18:51 | +5 | ETH | DOWN | 0.57 | yes | -5.88 |
| 11-07 18:51 | +5 | NEAR | DOWN | 0.68 | yes | -6.96 |
| 11-07 18:50 | +10 stop | DOGE | UP | 0.51 | 0.86 | 3.23 |
| 11-07 18:50 | +10 stop | XRP | UP | 0.68 | 0.78 | 0.71 |
| 11-07 18:50 | +20 | XRP | UP | 0.68 | 0.92 | 2.13 |
| 11-07 18:50 | +15 | XRP | UP | 0.68 | 0.92 | 2.13 |
| 11-07 18:50 | +10 | XRP | UP | 0.68 | 0.78 | 0.71 |
| 11-07 18:50 | +5 | XRP | UP | 0.68 | 0.73 | 0.20 |
| 11-07 18:50 | +10 stop | ETH | UP | 0.49 | 0.63 | 1.05 |
