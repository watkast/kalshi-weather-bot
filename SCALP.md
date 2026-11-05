# Range-Scalp Bot

*Updated Thu Nov 05 01:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47817 | 41638 | 6179 (73) | 1 | $-13781.03 | -4.6% |
| **+10¢** | 35729 | 28558 | 7171 (98) | 1 | $-12611.37 | -5.6% |
| **+15¢** | 29937 | 22214 | 7723 (126) | 1 | $-11550.77 | -6.1% |
| **+20¢** | 26599 | 18511 | 8088 (166) | 2 | $-10184.57 | -6.1% |
| **+10¢ (15¢ stop)** | 58309 | 58216 | 93 (56) | 0 | $-21700.87 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 01:27 | +10 stop | NEAR | DOWN | 0.64 | 0.76 | 0.90 |
| 11-05 01:27 | +5 | NEAR | DOWN | 0.64 | 0.73 | 0.59 |
| 11-05 01:27 | +10 stop | ZEC | UP | 0.70 | 0.55 | -1.83 |
| 11-05 01:24 | +10 stop | NEAR | DOWN | 0.67 | 0.51 | -1.94 |
| 11-05 01:24 | +20 | NEAR | DOWN | 0.68 | open |  |
| 11-05 01:24 | +15 | NEAR | DOWN | 0.64 | 0.83 | 1.63 |
| 11-05 01:24 | +10 | NEAR | DOWN | 0.64 | 0.76 | 0.90 |
| 11-05 01:24 | +5 | NEAR | DOWN | 0.64 | 0.73 | 0.59 |
| 11-05 01:24 | +10 stop | ZEC | DOWN | 0.55 | 0.36 | -2.25 |
| 11-05 01:24 | +20 | ZEC | DOWN | 0.55 | open |  |
| 11-05 01:24 | +15 | ZEC | DOWN | 0.55 | open |  |
| 11-05 01:24 | +10 | ZEC | DOWN | 0.55 | open |  |
| 11-05 01:24 | +5 | ZEC | DOWN | 0.56 | open |  |
| 11-05 01:18 | +10 stop | NEAR | DOWN | 0.70 | 0.92 | 1.99 |
| 11-05 01:18 | +10 | NEAR | DOWN | 0.70 | 0.92 | 1.99 |
| 11-05 01:18 | +5 | NEAR | DOWN | 0.70 | 0.78 | 0.52 |
| 11-05 01:16 | +10 stop | NEAR | DOWN | 0.62 | 0.75 | 0.99 |
| 11-05 01:16 | +20 | NEAR | DOWN | 0.62 | 0.92 | 2.77 |
| 11-05 01:16 | +15 | NEAR | DOWN | 0.62 | 0.78 | 1.30 |
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
