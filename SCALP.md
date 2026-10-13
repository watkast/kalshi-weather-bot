# Range-Scalp Bot

*Updated Tue Oct 13 23:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15138 | 13095 | 2043 (27) | 0 | $-4899.16 | -5.1% |
| **+10¢** | 11444 | 9071 | 2373 (39) | 0 | $-4597.71 | -6.4% |
| **+15¢** | 9619 | 7080 | 2539 (58) | 0 | $-4088.85 | -6.8% |
| **+20¢** | 8552 | 5900 | 2652 (74) | 0 | $-3585.82 | -6.7% |
| **+10¢ (15¢ stop)** | 18560 | 18510 | 50 (29) | 0 | $-7169.07 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 23:27 | +10 stop | NEAR | UP | 0.65 | 0.88 | 2.06 |
| 10-13 23:27 | +20 | NEAR | UP | 0.63 | 0.88 | 2.25 |
| 10-13 23:27 | +15 | NEAR | UP | 0.63 | 0.88 | 2.25 |
| 10-13 23:27 | +10 | NEAR | UP | 0.63 | 0.88 | 2.25 |
| 10-13 23:25 | +10 stop | BNB | UP | 0.61 | 0.31 | -3.32 |
| 10-13 23:25 | +20 | BNB | UP | 0.61 | no | -6.27 |
| 10-13 23:25 | +15 | BNB | UP | 0.61 | no | -6.27 |
| 10-13 23:25 | +10 | BNB | UP | 0.61 | no | -6.27 |
| 10-13 23:25 | +5 | BNB | UP | 0.61 | no | -6.27 |
| 10-13 23:24 | +10 stop | SOL | UP | 0.68 | 0.79 | 0.82 |
| 10-13 23:24 | +10 stop | XRP | DOWN | 0.53 | 0.72 | 1.57 |
| 10-13 23:24 | +10 | XRP | DOWN | 0.53 | 0.72 | 1.57 |
| 10-13 23:24 | +5 | XRP | DOWN | 0.53 | 0.62 | 0.55 |
| 10-13 23:23 | +5 | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-13 23:23 | +10 stop | HYPE | DOWN | 0.56 | 0.66 | 0.68 |
| 10-13 23:23 | +10 stop | SOL | UP | 0.71 | 0.49 | -2.53 |
| 10-13 23:23 | +15 | SOL | UP | 0.71 | 0.94 | 2.14 |
| 10-13 23:23 | +10 | SOL | UP | 0.71 | 0.81 | 0.74 |
| 10-13 23:23 | +5 | SOL | UP | 0.71 | 0.76 | 0.22 |
| 10-13 23:22 | +10 stop | NEAR | UP | 0.70 | 0.82 | 0.94 |
| 10-13 23:22 | +10 | NEAR | UP | 0.70 | 0.82 | 0.94 |
| 10-13 23:22 | +10 stop | ZEC | DOWN | 0.71 | 0.56 | -1.83 |
| 10-13 23:22 | +10 stop | HYPE | UP | 0.56 | 0.41 | -1.85 |
| 10-13 23:22 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-13 23:21 | +10 stop | BTC | DOWN | 0.59 | 0.75 | 1.29 |
| 10-13 23:21 | +5 | BTC | DOWN | 0.59 | 0.66 | 0.37 |
| 10-13 23:21 | +10 stop | BNB | UP | 0.58 | 0.74 | 1.29 |
| 10-13 23:21 | +20 | BNB | UP | 0.58 | 0.79 | 1.81 |
| 10-13 23:21 | +15 | BNB | UP | 0.58 | 0.74 | 1.29 |
| 10-13 23:21 | +10 | BNB | UP | 0.58 | 0.74 | 1.29 |
| 10-13 23:21 | +5 | BNB | UP | 0.58 | 0.74 | 1.29 |
| 10-13 23:20 | +10 stop | NEAR | DOWN | 0.56 | 0.36 | -2.35 |
| 10-13 23:20 | +10 stop | SOL | DOWN | 0.52 | 0.37 | -1.85 |
| 10-13 23:20 | +10 stop | ZEC | DOWN | 0.64 | 0.49 | -1.85 |
| 10-13 23:20 | +5 | NEAR | DOWN | 0.59 | yes | -6.07 |
| 10-13 23:20 | +10 stop | HYPE | DOWN | 0.67 | 0.40 | -3.03 |
| 10-13 23:20 | +5 | NEAR | UP | 0.44 | 0.53 | 0.54 |
| 10-13 23:19 | +10 stop | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 10-13 23:19 | +5 | BTC | UP | 0.44 | 0.60 | 1.25 |
| 10-13 23:19 | +5 | NEAR | UP | 0.56 | 0.62 | 0.26 |
