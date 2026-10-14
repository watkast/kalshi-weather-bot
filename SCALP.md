# Range-Scalp Bot

*Updated Wed Oct 14 04:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15457 | 13385 | 2072 (27) | 0 | $-4884.60 | -5.0% |
| **+10¢** | 11694 | 9288 | 2406 (39) | 0 | $-4559.21 | -6.2% |
| **+15¢** | 9818 | 7238 | 2580 (58) | 1 | $-4085.32 | -6.6% |
| **+20¢** | 8729 | 6028 | 2701 (75) | 2 | $-3605.83 | -6.6% |
| **+10¢ (15¢ stop)** | 18952 | 18902 | 50 (29) | 0 | $-7268.98 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 04:30 | +10 stop | ETH | UP | 0.70 | 0.84 | 1.10 |
| 10-14 04:30 | +20 | ETH | UP | 0.71 | open |  |
| 10-14 04:30 | +15 | ETH | UP | 0.70 | 0.85 | 1.26 |
| 10-14 04:30 | +10 | ETH | UP | 0.70 | 0.84 | 1.15 |
| 10-14 04:30 | +5 | ETH | UP | 0.70 | 0.79 | 0.63 |
| 10-14 04:30 | +10 stop | NEAR | UP | 0.70 | 0.81 | 0.84 |
| 10-14 04:30 | +20 | NEAR | UP | 0.70 | open |  |
| 10-14 04:30 | +15 | NEAR | UP | 0.70 | open |  |
| 10-14 04:30 | +10 | NEAR | UP | 0.70 | 0.81 | 0.84 |
| 10-14 04:30 | +5 | NEAR | UP | 0.70 | 0.81 | 0.84 |
| 10-14 04:27 | +10 stop | DOGE | UP | 0.64 | 0.93 | 2.68 |
| 10-14 04:27 | +5 | BNB | DOWN | 0.69 | yes | -7.05 |
| 10-14 04:26 | +10 stop | BNB | DOWN | 0.65 | 0.36 | -3.25 |
| 10-14 04:26 | +10 stop | DOGE | UP | 0.49 | 0.59 | 0.65 |
| 10-14 04:25 | +10 stop | BNB | DOWN | 0.70 | 0.54 | -1.92 |
| 10-14 04:25 | +10 stop | XRP | UP | 0.56 | 0.68 | 0.86 |
| 10-14 04:25 | +5 | ETH | DOWN | 0.63 | 0.83 | 1.73 |
| 10-14 04:24 | +5 | ETH | DOWN | 0.56 | 0.65 | 0.56 |
| 10-14 04:24 | +10 stop | BNB | UP | 0.59 | 0.71 | 0.88 |
| 10-14 04:24 | +10 stop | ETH | DOWN | 0.59 | 0.83 | 2.17 |
| 10-14 04:24 | +5 | ETH | DOWN | 0.59 | 0.66 | 0.41 |
| 10-14 04:22 | +10 stop | BTC | UP | 0.53 | 0.63 | 0.65 |
| 10-14 04:22 | +10 stop | ETH | UP | 0.51 | 0.35 | -1.94 |
| 10-14 04:21 | +5 | BTC | DOWN | 0.60 | 0.75 | 1.19 |
| 10-14 04:21 | +5 | SOL | DOWN | 0.59 | 0.76 | 1.40 |
| 10-14 04:21 | +10 stop | BTC | DOWN | 0.59 | 0.43 | -1.95 |
| 10-14 04:21 | +20 | BTC | DOWN | 0.59 | 0.82 | 2.02 |
| 10-14 04:21 | +15 | BTC | DOWN | 0.59 | 0.75 | 1.29 |
| 10-14 04:21 | +10 | BTC | DOWN | 0.59 | 0.75 | 1.29 |
| 10-14 04:21 | +5 | BTC | DOWN | 0.59 | 0.64 | 0.16 |
| 10-14 04:21 | +10 stop | BNB | DOWN | 0.60 | 0.45 | -1.85 |
| 10-14 04:21 | +20 | BNB | DOWN | 0.60 | yes | -6.17 |
| 10-14 04:21 | +15 | BNB | DOWN | 0.60 | yes | -6.17 |
| 10-14 04:21 | +10 | BNB | DOWN | 0.60 | yes | -6.17 |
| 10-14 04:21 | +5 | BNB | DOWN | 0.60 | 0.65 | 0.17 |
| 10-14 04:21 | +10 stop | SOL | DOWN | 0.58 | 0.76 | 1.49 |
| 10-14 04:21 | +10 | SOL | DOWN | 0.58 | 0.76 | 1.49 |
| 10-14 04:21 | +5 | SOL | DOWN | 0.58 | 0.64 | 0.25 |
| 10-14 04:21 | +10 stop | NEAR | DOWN | 0.67 | 0.80 | 1.02 |
| 10-14 04:21 | +20 | NEAR | DOWN | 0.67 | 0.90 | 2.07 |
