# Range-Scalp Bot

*Updated Fri Oct 09 23:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9650 | 8335 | 1315 (18) | 7 | $-3219.94 | -5.3% |
| **+10¢** | 7284 | 5745 | 1539 (30) | 8 | $-3111.56 | -6.8% |
| **+15¢** | 6140 | 4517 | 1623 (43) | 8 | $-2575.79 | -6.7% |
| **+20¢** | 5466 | 3780 | 1686 (55) | 7 | $-2126.61 | -6.2% |
| **+10¢ (15¢ stop)** | 11827 | 11792 | 35 (22) | 0 | $-4578.31 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 23:57 | +10 stop | DOGE | UP | 0.55 | 0.34 | -2.44 |
| 10-09 23:57 | +20 | DOGE | UP | 0.55 | open |  |
| 10-09 23:57 | +15 | DOGE | UP | 0.55 | open |  |
| 10-09 23:57 | +10 | DOGE | UP | 0.55 | open |  |
| 10-09 23:57 | +5 | DOGE | UP | 0.55 | open |  |
| 10-09 23:56 | +10 stop | XRP | UP | 0.64 | 0.29 | -3.79 |
| 10-09 23:56 | +15 | XRP | UP | 0.64 | open |  |
| 10-09 23:56 | +10 | XRP | UP | 0.64 | open |  |
| 10-09 23:56 | +5 | XRP | UP | 0.64 | open |  |
| 10-09 23:55 | +10 stop | ETH | DOWN | 0.71 | 0.90 | 1.71 |
| 10-09 23:53 | +10 stop | SOL | UP | 0.53 | 0.30 | -2.63 |
| 10-09 23:52 | +5 | BNB | DOWN | 0.63 | 0.80 | 1.41 |
| 10-09 23:51 | +10 stop | ETH | DOWN | 0.48 | 0.65 | 1.36 |
| 10-09 23:51 | +10 stop | BNB | DOWN | 0.57 | 0.80 | 2.00 |
| 10-09 23:51 | +10 stop | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-09 23:51 | +5 | BNB | DOWN | 0.55 | 0.61 | 0.25 |
| 10-09 23:50 | +10 stop | BTC | UP | 0.62 | 0.35 | -3.03 |
| 10-09 23:50 | +15 | BTC | UP | 0.62 | open |  |
| 10-09 23:50 | +10 | BTC | UP | 0.62 | open |  |
| 10-09 23:50 | +5 | BTC | UP | 0.64 | open |  |
| 10-09 23:50 | +10 stop | ZEC | UP | 0.58 | 0.38 | -2.35 |
| 10-09 23:50 | +10 | ZEC | UP | 0.58 | open |  |
| 10-09 23:50 | +5 | ZEC | UP | 0.58 | open |  |
| 10-09 23:50 | +10 stop | NEAR | DOWN | 0.57 | 0.81 | 2.11 |
| 10-09 23:50 | +10 stop | ZEC | DOWN | 0.35 | 0.50 | 1.16 |
| 10-09 23:50 | +10 | ZEC | DOWN | 0.35 | 0.50 | 1.16 |
| 10-09 23:50 | +5 | ZEC | DOWN | 0.35 | 0.50 | 1.16 |
| 10-09 23:50 | +10 stop | HYPE | DOWN | 0.60 | 0.73 | 0.95 |
| 10-09 23:50 | +5 | ETH | UP | 0.66 | open |  |
| 10-09 23:49 | +10 stop | NEAR | UP | 0.54 | 0.39 | -1.85 |
| 10-09 23:49 | +15 | NEAR | UP | 0.54 | open |  |
| 10-09 23:49 | +10 | NEAR | UP | 0.54 | open |  |
| 10-09 23:49 | +5 | NEAR | UP | 0.54 | open |  |
| 10-09 23:48 | +10 stop | ETH | UP | 0.63 | 0.45 | -2.15 |
| 10-09 23:48 | +10 stop | DOGE | UP | 0.58 | 0.69 | 0.77 |
| 10-09 23:48 | +10 | DOGE | UP | 0.58 | 0.69 | 0.77 |
| 10-09 23:48 | +5 | DOGE | UP | 0.58 | 0.69 | 0.77 |
| 10-09 23:48 | +10 stop | ZEC | UP | 0.54 | 0.72 | 1.48 |
| 10-09 23:48 | +10 stop | NEAR | DOWN | 0.49 | 0.65 | 1.26 |
| 10-09 23:48 | +15 | NEAR | DOWN | 0.49 | 0.65 | 1.26 |
