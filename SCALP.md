# Range-Scalp Bot

*Updated Wed Oct 07 02:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5834 | 5052 | 782 (9) | 2 | $-1825.38 | -5.0% |
| **+10¢** | 4443 | 3520 | 923 (16) | 2 | $-1765.25 | -6.3% |
| **+15¢** | 3726 | 2748 | 978 (20) | 2 | $-1554.59 | -6.7% |
| **+20¢** | 3326 | 2305 | 1021 (27) | 2 | $-1310.99 | -6.3% |
| **+10¢ (15¢ stop)** | 7095 | 7080 | 15 (9) | 0 | $-2537.24 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 02:43 | +10 stop | BTC | DOWN | 0.70 | 0.82 | 0.94 |
| 10-07 02:40 | +10 stop | BTC | UP | 0.66 | 0.46 | -2.34 |
| 10-07 02:40 | +15 | BTC | UP | 0.66 | open |  |
| 10-07 02:40 | +10 | BTC | UP | 0.66 | open |  |
| 10-07 02:40 | +5 | BTC | UP | 0.66 | open |  |
| 10-07 02:39 | +10 stop | BTC | UP | 0.63 | 0.80 | 1.41 |
| 10-07 02:39 | +15 | BTC | UP | 0.63 | 0.80 | 1.41 |
| 10-07 02:39 | +10 | BTC | UP | 0.63 | 0.80 | 1.41 |
| 10-07 02:39 | +5 | BTC | UP | 0.63 | 0.68 | 0.17 |
| 10-07 02:38 | +5 | DOGE | UP | 0.69 | open |  |
| 10-07 02:34 | +5 | NEAR | UP | 0.61 | 0.76 | 1.20 |
| 10-07 02:34 | +5 | SOL | UP | 0.70 | 0.78 | 0.52 |
| 10-07 02:34 | +10 stop | NEAR | UP | 0.60 | 0.76 | 1.30 |
| 10-07 02:34 | +20 | NEAR | UP | 0.60 | 0.86 | 2.34 |
| 10-07 02:34 | +15 | NEAR | UP | 0.60 | 0.76 | 1.30 |
| 10-07 02:34 | +10 | NEAR | UP | 0.60 | 0.76 | 1.30 |
| 10-07 02:34 | +5 | NEAR | UP | 0.60 | 0.67 | 0.37 |
| 10-07 02:33 | +10 stop | HYPE | UP | 0.69 | 0.82 | 1.00 |
| 10-07 02:32 | +10 | XRP | UP | 0.63 | 0.76 | 1.00 |
| 10-07 02:32 | +5 | XRP | UP | 0.70 | 0.76 | 0.32 |
| 10-07 02:31 | +10 stop | XRP | UP | 0.58 | 0.72 | 1.07 |
| 10-07 02:31 | +20 | XRP | UP | 0.57 | 0.79 | 1.90 |
| 10-07 02:31 | +15 | XRP | UP | 0.57 | 0.72 | 1.17 |
| 10-07 02:31 | +10 | XRP | UP | 0.57 | 0.67 | 0.66 |
| 10-07 02:31 | +5 | XRP | UP | 0.57 | 0.62 | 0.15 |
| 10-07 02:31 | +10 stop | SOL | UP | 0.60 | 0.72 | 0.88 |
| 10-07 02:31 | +20 | SOL | UP | 0.60 | 0.80 | 1.71 |
| 10-07 02:31 | +15 | SOL | UP | 0.60 | 0.78 | 1.50 |
| 10-07 02:31 | +10 | SOL | UP | 0.60 | 0.72 | 0.88 |
| 10-07 02:31 | +5 | SOL | UP | 0.60 | 0.69 | 0.58 |
| 10-07 02:31 | +10 stop | DOGE | UP | 0.68 | 0.43 | -2.84 |
| 10-07 02:31 | +20 | DOGE | UP | 0.68 | open |  |
| 10-07 02:31 | +15 | DOGE | UP | 0.68 | open |  |
| 10-07 02:31 | +10 | DOGE | UP | 0.68 | open |  |
| 10-07 02:31 | +5 | DOGE | UP | 0.68 | 0.74 | 0.30 |
| 10-07 02:31 | +10 stop | ETH | UP | 0.57 | 0.69 | 0.87 |
| 10-07 02:31 | +20 | ETH | UP | 0.62 | 0.83 | 1.83 |
| 10-07 02:31 | +10 | ETH | UP | 0.65 | 0.79 | 1.12 |
| 10-07 02:31 | +5 | ETH | UP | 0.65 | 0.71 | 0.29 |
| 10-07 02:31 | +10 stop | BTC | UP | 0.64 | 0.75 | 0.79 |
