# Range-Scalp Bot

*Updated Thu Oct 29 19:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39619 | 34593 | 5026 (50) | 5 | $-10973.92 | -4.4% |
| **+10¢** | 29528 | 23714 | 5814 (73) | 4 | $-9746.43 | -5.2% |
| **+15¢** | 24688 | 18436 | 6252 (100) | 4 | $-8735.73 | -5.6% |
| **+20¢** | 21908 | 15359 | 6549 (129) | 4 | $-7613.49 | -5.5% |
| **+10¢ (15¢ stop)** | 48389 | 48319 | 70 (37) | 0 | $-18359.88 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 18:52 | +10 stop | ZEC | UP | 0.67 | 0.80 | 1.02 |
| 10-29 18:52 | +10 stop | BNB | UP | 0.63 | 0.74 | 0.79 |
| 10-29 18:52 | +15 | BNB | UP | 0.63 | 0.86 | 2.04 |
| 10-29 18:52 | +10 | BNB | UP | 0.63 | 0.74 | 0.79 |
| 10-29 18:52 | +10 stop | ZEC | UP | 0.53 | 0.63 | 0.65 |
| 10-29 18:50 | +5 | ETH | UP | 0.70 | 0.83 | 1.05 |
| 10-29 18:50 | +10 stop | BNB | UP | 0.63 | 0.75 | 0.89 |
| 10-29 18:50 | +10 stop | ZEC | UP | 0.50 | 0.70 | 1.67 |
| 10-29 18:50 | +10 stop | DOGE | UP | 0.65 | 0.79 | 1.12 |
| 10-29 18:50 | +10 stop | ETH | UP | 0.66 | 0.83 | 1.44 |
| 10-29 18:49 | +5 | DOGE | DOWN | 0.59 | open |  |
| 10-29 18:49 | +10 stop | BTC | UP | 0.64 | 0.78 | 1.10 |
| 10-29 18:49 | +10 stop | SOL | UP | 0.59 | 0.70 | 0.78 |
| 10-29 18:49 | +5 | SOL | UP | 0.59 | 0.70 | 0.78 |
| 10-29 18:49 | +10 stop | XRP | UP | 0.70 | 0.81 | 0.84 |
| 10-29 18:49 | +5 | BNB | DOWN | 0.66 | open |  |
| 10-29 18:49 | +10 stop | NEAR | DOWN | 0.57 | 0.39 | -2.15 |
| 10-29 18:49 | +10 | NEAR | DOWN | 0.57 | open |  |
| 10-29 18:49 | +5 | NEAR | DOWN | 0.57 | open |  |
| 10-29 18:48 | +5 | BNB | DOWN | 0.61 | 0.68 | 0.37 |
| 10-29 18:48 | +10 stop | SOL | DOWN | 0.66 | 0.41 | -2.83 |
| 10-29 18:48 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
| 10-29 18:48 | +5 | BTC | DOWN | 0.62 | open |  |
| 10-29 18:47 | +10 stop | BNB | DOWN | 0.66 | 0.39 | -2.98 |
| 10-29 18:47 | +10 stop | XRP | DOWN | 0.56 | 0.32 | -2.73 |
| 10-29 18:47 | +10 stop | ZEC | DOWN | 0.62 | 0.40 | -2.54 |
| 10-29 18:47 | +20 | ZEC | DOWN | 0.62 | open |  |
| 10-29 18:47 | +15 | ZEC | DOWN | 0.62 | open |  |
| 10-29 18:47 | +10 | ZEC | DOWN | 0.62 | open |  |
| 10-29 18:47 | +5 | ZEC | DOWN | 0.62 | open |  |
| 10-29 18:47 | +10 stop | ETH | DOWN | 0.60 | 0.44 | -1.95 |
| 10-29 18:47 | +10 stop | BTC | DOWN | 0.54 | 0.38 | -1.95 |
| 10-29 18:47 | +20 | BTC | DOWN | 0.54 | open |  |
| 10-29 18:47 | +15 | BTC | DOWN | 0.54 | open |  |
| 10-29 18:47 | +10 | BTC | DOWN | 0.54 | open |  |
| 10-29 18:47 | +5 | BTC | DOWN | 0.54 | 0.62 | 0.45 |
| 10-29 18:47 | +5 | BNB | DOWN | 0.58 | 0.64 | 0.25 |
| 10-29 18:46 | +10 stop | DOGE | DOWN | 0.68 | 0.50 | -2.14 |
| 10-29 18:46 | +20 | DOGE | DOWN | 0.68 | open |  |
| 10-29 18:46 | +15 | DOGE | DOWN | 0.68 | open |  |
