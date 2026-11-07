# Range-Scalp Bot

*Updated Sat Nov 07 03:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50392 | 43925 | 6467 (76) | 0 | $-14173.73 | -4.5% |
| **+10¢** | 37608 | 30078 | 7530 (102) | 0 | $-13107.79 | -5.5% |
| **+15¢** | 31493 | 23378 | 8115 (131) | 2 | $-12032.37 | -6.1% |
| **+20¢** | 27999 | 19492 | 8507 (173) | 2 | $-10633.53 | -6.1% |
| **+10¢ (15¢ stop)** | 61357 | 61258 | 99 (58) | 0 | $-22717.77 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 03:17 | +10 stop | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-07 03:17 | +10 | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-07 03:17 | +5 | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-07 03:16 | +10 stop | ZEC | UP | 0.41 | 0.55 | 1.05 |
| 11-07 03:16 | +20 | ZEC | UP | 0.41 | open |  |
| 11-07 03:16 | +15 | ZEC | UP | 0.41 | open |  |
| 11-07 03:16 | +10 | ZEC | UP | 0.41 | 0.55 | 1.05 |
| 11-07 03:16 | +5 | ZEC | UP | 0.41 | 0.55 | 1.05 |
| 11-07 03:16 | +10 stop | ETH | UP | 0.39 | 0.60 | 1.76 |
| 11-07 03:16 | +20 | ETH | UP | 0.39 | 0.60 | 1.76 |
| 11-07 03:16 | +15 | ETH | UP | 0.39 | 0.60 | 1.76 |
| 11-07 03:16 | +10 | ETH | UP | 0.39 | 0.60 | 1.76 |
| 11-07 03:16 | +5 | ETH | UP | 0.39 | 0.60 | 1.76 |
| 11-07 03:16 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-07 03:16 | +20 | BTC | DOWN | 0.69 | open |  |
| 11-07 03:16 | +15 | BTC | DOWN | 0.69 | open |  |
| 11-07 03:16 | +10 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-07 03:16 | +5 | BTC | DOWN | 0.69 | 0.75 | 0.31 |
| 11-07 03:16 | +10 stop | HYPE | UP | 0.34 | 0.55 | 1.76 |
| 11-07 03:16 | +20 | HYPE | UP | 0.34 | 0.55 | 1.76 |
| 11-07 03:16 | +15 | HYPE | UP | 0.34 | 0.55 | 1.76 |
| 11-07 03:16 | +10 | HYPE | UP | 0.34 | 0.55 | 1.76 |
| 11-07 03:16 | +5 | HYPE | UP | 0.34 | 0.55 | 1.76 |
| 11-07 03:13 | +10 stop | HYPE | DOWN | 0.38 | 0.60 | 1.86 |
| 11-07 03:13 | +20 | HYPE | DOWN | 0.38 | 0.60 | 1.86 |
| 11-07 03:13 | +15 | HYPE | DOWN | 0.38 | 0.60 | 1.86 |
| 11-07 03:13 | +10 | HYPE | DOWN | 0.36 | 0.60 | 2.06 |
| 11-07 03:13 | +5 | HYPE | DOWN | 0.36 | 0.60 | 2.06 |
| 11-07 03:11 | +10 stop | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 11-07 03:10 | +10 stop | ZEC | UP | 0.57 | 0.31 | -2.93 |
| 11-07 03:10 | +20 | ZEC | UP | 0.57 | no | -5.88 |
| 11-07 03:10 | +15 | ZEC | UP | 0.58 | no | -5.98 |
| 11-07 03:10 | +10 | ZEC | UP | 0.58 | no | -5.98 |
| 11-07 03:10 | +5 | ZEC | UP | 0.58 | no | -5.98 |
| 11-07 03:06 | +5 | ZEC | UP | 0.64 | 0.69 | 0.18 |
| 11-07 03:04 | +10 stop | XRP | UP | 0.67 | 0.80 | 1.02 |
| 11-07 03:04 | +20 | XRP | UP | 0.67 | 0.89 | 1.97 |
| 11-07 03:04 | +15 | XRP | UP | 0.67 | 0.89 | 1.97 |
| 11-07 03:04 | +10 | XRP | UP | 0.67 | 0.80 | 1.02 |
| 11-07 03:04 | +5 | XRP | UP | 0.67 | 0.73 | 0.30 |
