# Range-Scalp Bot

*Updated Sun Oct 11 00:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11106 | 9574 | 1532 (22) | 3 | $-3778.58 | -5.4% |
| **+10¢** | 8414 | 6630 | 1784 (36) | 3 | $-3608.96 | -6.8% |
| **+15¢** | 7091 | 5204 | 1887 (52) | 3 | $-3054.83 | -6.9% |
| **+20¢** | 6313 | 4349 | 1964 (66) | 3 | $-2577.52 | -6.5% |
| **+10¢ (15¢ stop)** | 13691 | 13650 | 41 (25) | 3 | $-5502.71 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 00:00 | +10 stop | XRP | UP | 0.66 | open |  |
| 10-11 00:00 | +20 | XRP | UP | 0.66 | open |  |
| 10-11 00:00 | +15 | XRP | UP | 0.66 | open |  |
| 10-11 00:00 | +10 | XRP | UP | 0.66 | open |  |
| 10-11 00:00 | +5 | XRP | UP | 0.66 | open |  |
| 10-11 00:00 | +10 stop | NEAR | UP | 0.64 | open |  |
| 10-11 00:00 | +20 | NEAR | UP | 0.64 | open |  |
| 10-11 00:00 | +15 | NEAR | UP | 0.64 | open |  |
| 10-11 00:00 | +10 | NEAR | UP | 0.64 | open |  |
| 10-11 00:00 | +5 | NEAR | UP | 0.64 | open |  |
| 10-11 00:00 | +10 stop | BNB | UP | 0.59 | open |  |
| 10-11 00:00 | +20 | BNB | UP | 0.59 | open |  |
| 10-11 00:00 | +15 | BNB | UP | 0.59 | open |  |
| 10-11 00:00 | +10 | BNB | UP | 0.59 | open |  |
| 10-11 00:00 | +5 | BNB | UP | 0.59 | open |  |
| 10-10 23:55 | +10 stop | ETH | DOWN | 0.70 | 0.84 | 1.15 |
| 10-10 23:55 | +20 | ETH | DOWN | 0.70 | 0.91 | 1.89 |
| 10-10 23:55 | +15 | ETH | DOWN | 0.70 | 0.91 | 1.89 |
| 10-10 23:55 | +10 | ETH | DOWN | 0.70 | 0.84 | 1.15 |
| 10-10 23:55 | +5 | ETH | DOWN | 0.70 | 0.77 | 0.42 |
| 10-10 23:54 | +10 stop | BNB | UP | 0.33 | 0.54 | 1.76 |
| 10-10 23:53 | +10 stop | ZEC | DOWN | 0.57 | 0.74 | 1.38 |
| 10-10 23:53 | +10 stop | BTC | UP | 0.69 | 0.26 | -4.59 |
| 10-10 23:53 | +10 stop | DOGE | UP | 0.64 | 0.11 | -5.57 |
| 10-10 23:53 | +10 stop | XRP | DOWN | 0.71 | 0.94 | 2.11 |
| 10-10 23:53 | +10 stop | ZEC | DOWN | 0.71 | 0.53 | -2.13 |
| 10-10 23:53 | +20 | ZEC | DOWN | 0.71 | 0.95 | 2.21 |
| 10-10 23:53 | +15 | ZEC | DOWN | 0.71 | 0.89 | 1.58 |
| 10-10 23:53 | +10 | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-10 23:53 | +5 | ZEC | DOWN | 0.71 | 0.79 | 0.53 |
| 10-10 23:52 | +10 stop | SOL | UP | 0.70 | 0.82 | 0.94 |
| 10-10 23:52 | +10 stop | ETH | UP | 0.52 | 0.69 | 1.42 |
| 10-10 23:51 | +5 | DOGE | DOWN | 0.58 | 0.88 | 2.74 |
| 10-10 23:51 | +10 stop | BNB | DOWN | 0.61 | 0.45 | -1.95 |
| 10-10 23:51 | +10 stop | DOGE | DOWN | 0.56 | 0.37 | -2.25 |
| 10-10 23:50 | +10 stop | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 10-10 23:50 | +5 | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 10-10 23:50 | +5 | HYPE | UP | 0.70 | 0.75 | 0.21 |
| 10-10 23:49 | +10 stop | ETH | UP | 0.60 | 0.43 | -2.05 |
| 10-10 23:49 | +10 | ETH | UP | 0.60 | 0.76 | 1.30 |
