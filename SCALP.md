# Range-Scalp Bot

*Updated Mon Nov 09 10:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53545 | 46690 | 6855 (86) | 0 | $-14753.84 | -4.4% |
| **+10¢** | 40003 | 32008 | 7995 (112) | 0 | $-13734.51 | -5.5% |
| **+15¢** | 33517 | 24902 | 8615 (143) | 1 | $-12532.26 | -6.0% |
| **+20¢** | 29825 | 20788 | 9037 (189) | 3 | $-11032.43 | -5.9% |
| **+10¢ (15¢ stop)** | 65251 | 65145 | 106 (63) | 0 | $-24156.80 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 10:31 | +10 stop | XRP | DOWN | 0.60 | 0.70 | 0.68 |
| 11-09 10:31 | +20 | XRP | DOWN | 0.60 | open |  |
| 11-09 10:31 | +15 | XRP | DOWN | 0.60 | 0.77 | 1.40 |
| 11-09 10:31 | +10 | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 11-09 10:31 | +5 | XRP | DOWN | 0.61 | 0.68 | 0.37 |
| 11-09 10:31 | +10 stop | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-09 10:31 | +20 | ZEC | DOWN | 0.66 | open |  |
| 11-09 10:31 | +15 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-09 10:31 | +10 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-09 10:31 | +5 | ZEC | DOWN | 0.66 | 0.72 | 0.29 |
| 11-09 10:31 | +10 stop | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-09 10:31 | +20 | DOGE | DOWN | 0.69 | open |  |
| 11-09 10:31 | +15 | DOGE | DOWN | 0.69 | open |  |
| 11-09 10:31 | +10 | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-09 10:31 | +5 | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-09 10:30 | +10 stop | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-09 10:30 | +20 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 11-09 10:30 | +15 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 11-09 10:30 | +10 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-09 10:30 | +5 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 11-09 10:30 | +10 stop | NEAR | DOWN | 0.71 | 0.81 | 0.75 |
| 11-09 10:30 | +20 | NEAR | DOWN | 0.71 | 0.92 | 1.89 |
| 11-09 10:30 | +15 | NEAR | DOWN | 0.71 | 0.90 | 1.71 |
| 11-09 10:30 | +10 | NEAR | DOWN | 0.71 | 0.81 | 0.75 |
| 11-09 10:30 | +5 | NEAR | DOWN | 0.71 | 0.81 | 0.75 |
| 11-09 10:26 | +10 stop | DOGE | UP | 0.37 | 0.52 | 1.15 |
| 11-09 10:26 | +20 | DOGE | UP | 0.37 | no | -3.87 |
| 11-09 10:26 | +15 | DOGE | UP | 0.37 | 0.52 | 1.15 |
| 11-09 10:26 | +10 | DOGE | UP | 0.37 | 0.52 | 1.15 |
| 11-09 10:26 | +5 | DOGE | UP | 0.37 | 0.52 | 1.15 |
| 11-09 10:24 | +10 stop | HYPE | DOWN | 0.68 | 0.50 | -2.14 |
| 11-09 10:24 | +20 | HYPE | DOWN | 0.68 | yes | -6.96 |
| 11-09 10:24 | +15 | HYPE | DOWN | 0.68 | yes | -6.96 |
| 11-09 10:24 | +10 | HYPE | DOWN | 0.68 | yes | -6.96 |
| 11-09 10:24 | +5 | HYPE | DOWN | 0.68 | yes | -6.96 |
| 11-09 10:24 | +10 stop | ZEC | UP | 0.62 | 0.82 | 1.72 |
| 11-09 10:24 | +20 | ZEC | UP | 0.62 | 0.82 | 1.72 |
| 11-09 10:24 | +15 | ZEC | UP | 0.62 | 0.82 | 1.72 |
| 11-09 10:24 | +10 | ZEC | UP | 0.62 | 0.82 | 1.72 |
| 11-09 10:24 | +5 | ZEC | UP | 0.62 | 0.82 | 1.72 |
