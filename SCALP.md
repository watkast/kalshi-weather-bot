# Range-Scalp Bot

*Updated Wed Oct 14 04:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15459 | 13387 | 2072 (27) | 1 | $-4883.10 | -5.0% |
| **+10¢** | 11696 | 9290 | 2406 (39) | 1 | $-4557.71 | -6.2% |
| **+15¢** | 9821 | 7241 | 2580 (58) | 1 | $-4080.58 | -6.6% |
| **+20¢** | 8732 | 6031 | 2701 (75) | 1 | $-3599.95 | -6.6% |
| **+10¢ (15¢ stop)** | 18955 | 18905 | 50 (29) | 1 | $-7269.71 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 04:41 | +10 stop | BTC | DOWN | 0.52 | open |  |
| 10-14 04:39 | +10 stop | BTC | UP | 0.70 | 0.51 | -2.23 |
| 10-14 04:39 | +15 | BTC | UP | 0.70 | open |  |
| 10-14 04:39 | +10 | BTC | UP | 0.70 | open |  |
| 10-14 04:39 | +5 | BTC | UP | 0.69 | open |  |
| 10-14 04:34 | +10 stop | BTC | UP | 0.67 | 0.77 | 0.71 |
| 10-14 04:34 | +20 | BTC | UP | 0.67 | open |  |
| 10-14 04:34 | +15 | BTC | UP | 0.67 | 0.84 | 1.44 |
| 10-14 04:34 | +10 | BTC | UP | 0.67 | 0.77 | 0.71 |
| 10-14 04:34 | +5 | BTC | UP | 0.67 | 0.77 | 0.71 |
| 10-14 04:34 | +10 stop | BNB | UP | 0.62 | 0.73 | 0.79 |
| 10-14 04:34 | +20 | BNB | UP | 0.62 | 0.85 | 2.04 |
| 10-14 04:34 | +15 | BNB | UP | 0.62 | 0.81 | 1.62 |
| 10-14 04:34 | +10 | BNB | UP | 0.62 | 0.73 | 0.79 |
| 10-14 04:34 | +5 | BNB | UP | 0.62 | 0.73 | 0.79 |
| 10-14 04:30 | +10 stop | ETH | UP | 0.70 | 0.84 | 1.10 |
| 10-14 04:30 | +20 | ETH | UP | 0.71 | 0.93 | 2.02 |
| 10-14 04:30 | +15 | ETH | UP | 0.70 | 0.85 | 1.26 |
| 10-14 04:30 | +10 | ETH | UP | 0.70 | 0.84 | 1.15 |
| 10-14 04:30 | +5 | ETH | UP | 0.70 | 0.79 | 0.63 |
| 10-14 04:30 | +10 stop | NEAR | UP | 0.70 | 0.81 | 0.84 |
| 10-14 04:30 | +20 | NEAR | UP | 0.70 | 0.90 | 1.82 |
| 10-14 04:30 | +15 | NEAR | UP | 0.70 | 0.89 | 1.68 |
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
