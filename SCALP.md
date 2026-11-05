# Range-Scalp Bot

*Updated Thu Nov 05 01:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47814 | 41635 | 6179 (73) | 0 | $-13782.73 | -4.6% |
| **+10¢** | 35727 | 28556 | 7171 (98) | 0 | $-12614.26 | -5.6% |
| **+15¢** | 29935 | 22212 | 7723 (126) | 1 | $-11553.70 | -6.2% |
| **+20¢** | 26598 | 18510 | 8088 (166) | 1 | $-10187.34 | -6.1% |
| **+10¢ (15¢ stop)** | 58304 | 58211 | 93 (56) | 0 | $-21697.74 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 01:16 | +10 stop | NEAR | DOWN | 0.62 | 0.75 | 0.99 |
| 11-05 01:16 | +20 | NEAR | DOWN | 0.62 | open |  |
| 11-05 01:16 | +15 | NEAR | DOWN | 0.62 | open |  |
| 11-05 01:16 | +10 | NEAR | DOWN | 0.62 | 0.75 | 0.99 |
| 11-05 01:16 | +5 | NEAR | DOWN | 0.62 | 0.75 | 0.99 |
| 11-05 01:14 | +10 stop | BTC | DOWN | 0.29 | 0.57 | 2.47 |
| 11-05 01:14 | +15 | BTC | DOWN | 0.30 | 0.57 | 2.37 |
| 11-05 01:14 | +10 | BTC | DOWN | 0.29 | 0.57 | 2.47 |
| 11-05 01:13 | +10 stop | NEAR | UP | 0.68 | 0.91 | 2.17 |
| 11-05 01:12 | +10 stop | DOGE | UP | 0.48 | 0.17 | -3.38 |
| 11-05 01:12 | +20 | DOGE | UP | 0.48 | no | -4.98 |
| 11-05 01:12 | +15 | DOGE | UP | 0.48 | no | -4.98 |
| 11-05 01:12 | +10 | DOGE | UP | 0.48 | no | -4.98 |
| 11-05 01:12 | +5 | DOGE | UP | 0.48 | 0.57 | 0.54 |
| 11-05 01:12 | +10 stop | ZEC | UP | 0.25 | 0.60 | 3.19 |
| 11-05 01:12 | +20 | ZEC | UP | 0.25 | 0.60 | 3.19 |
| 11-05 01:12 | +15 | ZEC | UP | 0.25 | 0.60 | 3.19 |
| 11-05 01:12 | +10 | ZEC | UP | 0.25 | 0.60 | 3.19 |
| 11-05 01:12 | +5 | ZEC | UP | 0.25 | 0.60 | 3.19 |
| 11-05 01:11 | +10 stop | HYPE | UP | 0.42 | 0.60 | 1.45 |
| 11-05 01:10 | +10 stop | ETH | UP | 0.65 | 0.81 | 1.33 |
| 11-05 01:10 | +10 stop | BTC | UP | 0.69 | 0.45 | -2.73 |
| 11-05 01:10 | +5 | BTC | UP | 0.69 | no | -7.05 |
| 11-05 01:10 | +10 stop | HYPE | DOWN | 0.57 | 0.36 | -2.45 |
| 11-05 01:10 | +10 stop | XRP | UP | 0.68 | 0.83 | 1.24 |
| 11-05 01:10 | +10 stop | BTC | DOWN | 0.49 | 0.62 | 0.95 |
| 11-05 01:10 | +5 | BTC | DOWN | 0.49 | 0.62 | 0.95 |
| 11-05 01:10 | +5 | XRP | UP | 0.69 | 0.83 | 1.15 |
| 11-05 01:09 | +10 stop | SOL | DOWN | 0.61 | 0.30 | -3.42 |
| 11-05 01:08 | +10 stop | ZEC | DOWN | 0.61 | 0.32 | -3.23 |
| 11-05 01:08 | +10 stop | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-05 01:08 | +10 stop | ETH | DOWN | 0.67 | 0.33 | -3.72 |
| 11-05 01:08 | +20 | ETH | DOWN | 0.67 | 0.90 | 2.08 |
| 11-05 01:07 | +10 stop | DOGE | DOWN | 0.62 | 0.33 | -3.27 |
| 11-05 01:07 | +10 stop | XRP | DOWN | 0.58 | 0.43 | -1.86 |
| 11-05 01:07 | +10 stop | BTC | DOWN | 0.56 | 0.70 | 1.07 |
| 11-05 01:07 | +10 stop | NEAR | UP | 0.69 | 0.53 | -1.93 |
| 11-05 01:07 | +10 stop | HYPE | DOWN | 0.68 | 0.44 | -2.74 |
| 11-05 01:07 | +10 stop | BTC | UP | 0.39 | 0.57 | 1.45 |
| 11-05 01:06 | +10 stop | ETH | DOWN | 0.57 | 0.71 | 1.07 |
