# Range-Scalp Bot

*Updated Mon Oct 05 01:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3052 | 2614 | 438 (3) | 1 | $-1144.52 | -5.9% |
| **+10¢** | 2369 | 1873 | 496 (4) | 2 | $-1003.58 | -6.7% |
| **+15¢** | 1998 | 1475 | 523 (5) | 2 | $-874.13 | -7.0% |
| **+20¢** | 1783 | 1238 | 545 (10) | 2 | $-744.29 | -6.6% |
| **+10¢ (15¢ stop)** | 3821 | 3820 | 1 (1) | 2 | $-1541.30 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 01:01 | +10 stop | XRP | DOWN | 0.67 | open |  |
| 10-05 01:01 | +20 | XRP | DOWN | 0.67 | open |  |
| 10-05 01:01 | +15 | XRP | DOWN | 0.67 | open |  |
| 10-05 01:01 | +10 | XRP | DOWN | 0.67 | open |  |
| 10-05 01:01 | +5 | XRP | DOWN | 0.67 | 0.72 | 0.19 |
| 10-05 01:01 | +10 stop | DOGE | DOWN | 0.61 | open |  |
| 10-05 01:01 | +20 | DOGE | DOWN | 0.61 | open |  |
| 10-05 01:01 | +15 | DOGE | DOWN | 0.61 | open |  |
| 10-05 01:01 | +10 | DOGE | DOWN | 0.61 | open |  |
| 10-05 01:01 | +5 | DOGE | DOWN | 0.61 | open |  |
| 10-05 00:57 | +10 stop | NEAR | DOWN | 0.51 | 0.35 | -1.94 |
| 10-05 00:57 | +15 | NEAR | DOWN | 0.51 | yes | -5.28 |
| 10-05 00:57 | +10 | NEAR | DOWN | 0.51 | yes | -5.28 |
| 10-05 00:57 | +5 | NEAR | DOWN | 0.51 | 0.56 | 0.14 |
| 10-05 00:55 | +10 stop | BTC | DOWN | 0.38 | 0.54 | 1.25 |
| 10-05 00:55 | +5 | BTC | DOWN | 0.38 | 0.54 | 1.25 |
| 10-05 00:54 | +10 stop | ZEC | UP | 0.62 | 0.46 | -1.95 |
| 10-05 00:54 | +20 | ZEC | UP | 0.63 | 0.89 | 2.36 |
| 10-05 00:54 | +15 | ZEC | UP | 0.63 | 0.89 | 2.36 |
| 10-05 00:54 | +10 | ZEC | UP | 0.63 | 0.75 | 0.89 |
| 10-05 00:54 | +5 | ZEC | UP | 0.63 | 0.68 | 0.17 |
| 10-05 00:54 | +10 stop | HYPE | UP | 0.62 | 0.80 | 1.51 |
| 10-05 00:54 | +10 stop | ETH | UP | 0.50 | 0.78 | 2.49 |
| 10-05 00:52 | +10 stop | NEAR | UP | 0.62 | 0.31 | -3.46 |
| 10-05 00:52 | +10 stop | SOL | DOWN | 0.68 | 0.50 | -2.14 |
| 10-05 00:52 | +10 stop | ETH | UP | 0.63 | 0.78 | 1.20 |
| 10-05 00:51 | +10 stop | BTC | UP | 0.65 | 0.80 | 1.22 |
| 10-05 00:51 | +5 | BTC | UP | 0.65 | 0.74 | 0.60 |
| 10-05 00:51 | +10 stop | BTC | DOWN | 0.40 | 0.54 | 1.05 |
| 10-05 00:51 | +5 | BTC | DOWN | 0.40 | 0.54 | 1.05 |
| 10-05 00:50 | +10 stop | NEAR | UP | 0.64 | 0.78 | 1.10 |
| 10-05 00:50 | +5 | SOL | DOWN | 0.60 | 0.71 | 0.78 |
| 10-05 00:49 | +10 stop | BNB | UP | 0.62 | 0.78 | 1.30 |
| 10-05 00:48 | +10 stop | ETH | UP | 0.66 | 0.77 | 0.81 |
| 10-05 00:48 | +10 stop | SOL | UP | 0.52 | 0.36 | -1.95 |
| 10-05 00:48 | +20 | SOL | UP | 0.52 | 0.73 | 1.78 |
| 10-05 00:48 | +15 | SOL | UP | 0.52 | 0.73 | 1.78 |
| 10-05 00:48 | +10 | SOL | UP | 0.52 | 0.73 | 1.78 |
| 10-05 00:48 | +5 | SOL | UP | 0.52 | 0.57 | 0.14 |
| 10-05 00:48 | +5 | BTC | DOWN | 0.50 | 0.57 | 0.34 |
