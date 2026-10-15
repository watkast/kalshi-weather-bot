# Range-Scalp Bot

*Updated Thu Oct 15 02:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16940 | 14699 | 2241 (28) | 1 | $-5208.50 | -4.9% |
| **+10¢** | 12808 | 10212 | 2596 (40) | 4 | $-4725.95 | -5.9% |
| **+15¢** | 10760 | 7969 | 2791 (59) | 2 | $-4235.77 | -6.3% |
| **+20¢** | 9558 | 6634 | 2924 (76) | 1 | $-3733.84 | -6.2% |
| **+10¢ (15¢ stop)** | 20855 | 20805 | 50 (29) | 0 | $-8074.15 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 02:21 | +10 stop | ETH | UP | 0.49 | 0.27 | -2.52 |
| 10-15 02:21 | +10 stop | BTC | UP | 0.53 | 0.14 | -4.17 |
| 10-15 02:21 | +20 | BTC | UP | 0.53 | open |  |
| 10-15 02:21 | +15 | BTC | UP | 0.53 | open |  |
| 10-15 02:21 | +10 | BTC | UP | 0.53 | open |  |
| 10-15 02:21 | +5 | BTC | UP | 0.53 | 0.60 | 0.35 |
| 10-15 02:21 | +10 stop | NEAR | DOWN | 0.70 | 0.88 | 1.57 |
| 10-15 02:21 | +10 stop | XRP | UP | 0.54 | 0.27 | -3.02 |
| 10-15 02:21 | +10 | XRP | UP | 0.54 | open |  |
| 10-15 02:21 | +5 | XRP | UP | 0.54 | 0.61 | 0.35 |
| 10-15 02:21 | +10 stop | BNB | UP | 0.53 | 0.30 | -2.63 |
| 10-15 02:21 | +10 | BNB | UP | 0.53 | open |  |
| 10-15 02:21 | +5 | BNB | UP | 0.57 | open |  |
| 10-15 02:20 | +5 | DOGE | UP | 0.44 | 0.54 | 0.64 |
| 10-15 02:20 | +10 stop | SOL | UP | 0.62 | 0.35 | -3.03 |
| 10-15 02:19 | +10 stop | SOL | UP | 0.58 | 0.71 | 0.98 |
| 10-15 02:19 | +10 stop | NEAR | DOWN | 0.66 | 0.47 | -2.24 |
| 10-15 02:19 | +15 | NEAR | DOWN | 0.66 | 0.88 | 1.96 |
| 10-15 02:19 | +10 | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 10-15 02:19 | +5 | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 10-15 02:19 | +10 stop | DOGE | UP | 0.69 | 0.48 | -2.41 |
| 10-15 02:19 | +15 | DOGE | UP | 0.69 | open |  |
| 10-15 02:19 | +10 | DOGE | UP | 0.67 | open |  |
| 10-15 02:19 | +5 | DOGE | UP | 0.67 | 0.73 | 0.30 |
| 10-15 02:19 | +10 stop | XRP | DOWN | 0.53 | 0.64 | 0.75 |
| 10-15 02:19 | +10 | XRP | DOWN | 0.53 | 0.64 | 0.75 |
| 10-15 02:19 | +5 | XRP | DOWN | 0.52 | 0.64 | 0.85 |
| 10-15 02:19 | +10 stop | ETH | DOWN | 0.38 | 0.54 | 1.25 |
| 10-15 02:19 | +10 stop | SOL | DOWN | 0.47 | 0.59 | 0.85 |
| 10-15 02:18 | +10 stop | BTC | UP | 0.43 | 0.63 | 1.65 |
| 10-15 02:18 | +10 stop | XRP | UP | 0.42 | 0.60 | 1.45 |
| 10-15 02:18 | +10 | XRP | UP | 0.42 | 0.60 | 1.45 |
| 10-15 02:18 | +5 | XRP | UP | 0.42 | 0.60 | 1.45 |
| 10-15 02:18 | +10 stop | ETH | UP | 0.46 | 0.62 | 1.25 |
| 10-15 02:18 | +5 | BNB | DOWN | 0.68 | 0.75 | 0.40 |
| 10-15 02:18 | +5 | BTC | UP | 0.56 | 0.63 | 0.35 |
| 10-15 02:17 | +5 | DOGE | DOWN | 0.56 | 0.67 | 0.76 |
| 10-15 02:17 | +10 stop | XRP | DOWN | 0.51 | 0.62 | 0.75 |
| 10-15 02:17 | +20 | XRP | DOWN | 0.51 | 0.72 | 1.77 |
| 10-15 02:17 | +15 | XRP | DOWN | 0.52 | 0.72 | 1.67 |
