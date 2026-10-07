# Range-Scalp Bot

*Updated Wed Oct 07 00:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5711 | 4939 | 772 (9) | 0 | $-1825.57 | -5.1% |
| **+10¢** | 4353 | 3445 | 908 (16) | 0 | $-1746.89 | -6.4% |
| **+15¢** | 3654 | 2691 | 963 (20) | 0 | $-1547.78 | -6.8% |
| **+20¢** | 3265 | 2262 | 1003 (27) | 0 | $-1293.25 | -6.3% |
| **+10¢ (15¢ stop)** | 6954 | 6939 | 15 (9) | 0 | $-2511.77 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 00:36 | +10 stop | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 10-07 00:35 | +10 stop | NEAR | UP | 0.66 | 0.78 | 0.91 |
| 10-07 00:34 | +10 stop | SOL | DOWN | 0.58 | 0.28 | -3.32 |
| 10-07 00:34 | +10 stop | DOGE | UP | 0.51 | 0.67 | 1.26 |
| 10-07 00:34 | +10 stop | XRP | UP | 0.59 | 0.72 | 0.98 |
| 10-07 00:34 | +5 | ZEC | DOWN | 0.61 | yes | -6.30 |
| 10-07 00:34 | +5 | NEAR | DOWN | 0.68 | yes | -6.92 |
| 10-07 00:34 | +10 stop | BNB | UP | 0.68 | 0.78 | 0.71 |
| 10-07 00:34 | +10 stop | SOL | UP | 0.60 | 0.45 | -1.85 |
| 10-07 00:34 | +20 | SOL | UP | 0.60 | 0.81 | 1.82 |
| 10-07 00:34 | +15 | SOL | UP | 0.60 | 0.76 | 1.30 |
| 10-07 00:34 | +10 | SOL | UP | 0.60 | 0.71 | 0.78 |
| 10-07 00:34 | +5 | SOL | UP | 0.60 | 0.71 | 0.78 |
| 10-07 00:33 | +10 stop | BTC | UP | 0.64 | 0.78 | 1.10 |
| 10-07 00:33 | +10 stop | NEAR | DOWN | 0.62 | 0.36 | -2.94 |
| 10-07 00:33 | +20 | NEAR | DOWN | 0.62 | yes | -6.37 |
| 10-07 00:33 | +15 | NEAR | DOWN | 0.62 | yes | -6.37 |
| 10-07 00:33 | +10 | NEAR | DOWN | 0.61 | yes | -6.28 |
| 10-07 00:33 | +5 | NEAR | DOWN | 0.62 | 0.67 | 0.17 |
| 10-07 00:33 | +10 stop | DOGE | UP | 0.70 | 0.54 | -1.93 |
| 10-07 00:33 | +20 | DOGE | UP | 0.70 | 0.91 | 1.89 |
| 10-07 00:33 | +15 | DOGE | UP | 0.70 | 0.88 | 1.57 |
| 10-07 00:33 | +10 | DOGE | UP | 0.70 | 0.88 | 1.57 |
| 10-07 00:33 | +5 | DOGE | UP | 0.70 | 0.75 | 0.21 |
| 10-07 00:33 | +10 stop | ZEC | DOWN | 0.61 | 0.34 | -3.03 |
| 10-07 00:33 | +20 | ZEC | DOWN | 0.61 | yes | -6.27 |
| 10-07 00:33 | +15 | ZEC | DOWN | 0.60 | yes | -6.17 |
| 10-07 00:33 | +10 | ZEC | DOWN | 0.58 | yes | -5.98 |
| 10-07 00:33 | +5 | ZEC | DOWN | 0.57 | 0.63 | 0.25 |
| 10-07 00:32 | +10 stop | ETH | UP | 0.65 | 0.80 | 1.22 |
| 10-07 00:32 | +20 | ETH | UP | 0.65 | 0.87 | 1.96 |
| 10-07 00:32 | +15 | ETH | UP | 0.65 | 0.80 | 1.22 |
| 10-07 00:32 | +10 | ETH | UP | 0.65 | 0.80 | 1.22 |
| 10-07 00:32 | +5 | ETH | UP | 0.65 | 0.80 | 1.22 |
| 10-07 00:31 | +10 stop | SOL | UP | 0.52 | 0.62 | 0.65 |
| 10-07 00:31 | +20 | SOL | UP | 0.52 | 0.74 | 1.88 |
| 10-07 00:31 | +15 | SOL | UP | 0.52 | 0.74 | 1.88 |
| 10-07 00:31 | +10 | SOL | UP | 0.52 | 0.62 | 0.65 |
| 10-07 00:31 | +5 | SOL | UP | 0.52 | 0.62 | 0.65 |
| 10-07 00:31 | +5 | XRP | DOWN | 0.67 | yes | -6.86 |
