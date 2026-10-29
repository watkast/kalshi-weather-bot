# Range-Scalp Bot

*Updated Thu Oct 29 21:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39736 | 34695 | 5041 (50) | 2 | $-11001.42 | -4.4% |
| **+10¢** | 29624 | 23794 | 5830 (73) | 2 | $-9754.13 | -5.2% |
| **+15¢** | 24771 | 18500 | 6271 (100) | 2 | $-8753.94 | -5.6% |
| **+20¢** | 21980 | 15410 | 6570 (129) | 5 | $-7639.84 | -5.5% |
| **+10¢ (15¢ stop)** | 48524 | 48454 | 70 (37) | 1 | $-18389.44 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 21:34 | +10 stop | DOGE | UP | 0.71 | open |  |
| 10-29 21:34 | +15 | DOGE | UP | 0.71 | open |  |
| 10-29 21:34 | +10 | DOGE | UP | 0.71 | open |  |
| 10-29 21:34 | +5 | DOGE | UP | 0.71 | open |  |
| 10-29 21:34 | +5 | XRP | UP | 0.66 | 0.79 | 1.02 |
| 10-29 21:31 | +10 stop | SOL | UP | 0.57 | 0.67 | 0.66 |
| 10-29 21:31 | +20 | SOL | UP | 0.57 | 0.77 | 1.69 |
| 10-29 21:31 | +15 | SOL | UP | 0.57 | 0.77 | 1.69 |
| 10-29 21:31 | +10 | SOL | UP | 0.57 | 0.67 | 0.66 |
| 10-29 21:31 | +5 | SOL | UP | 0.57 | 0.67 | 0.66 |
| 10-29 21:31 | +10 stop | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 10-29 21:31 | +20 | DOGE | UP | 0.63 | open |  |
| 10-29 21:31 | +15 | DOGE | UP | 0.63 | 0.79 | 1.31 |
| 10-29 21:31 | +10 | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 10-29 21:31 | +5 | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 10-29 21:31 | +10 stop | NEAR | UP | 0.67 | 0.78 | 0.81 |
| 10-29 21:31 | +20 | NEAR | UP | 0.67 | open |  |
| 10-29 21:31 | +15 | NEAR | UP | 0.67 | 0.82 | 1.23 |
| 10-29 21:31 | +10 | NEAR | UP | 0.67 | 0.78 | 0.81 |
| 10-29 21:31 | +5 | NEAR | UP | 0.67 | 0.78 | 0.81 |
| 10-29 21:31 | +10 stop | ETH | UP | 0.64 | 0.76 | 0.90 |
| 10-29 21:31 | +20 | ETH | UP | 0.64 | 0.86 | 1.94 |
| 10-29 21:31 | +15 | ETH | UP | 0.64 | 0.79 | 1.21 |
| 10-29 21:31 | +10 | ETH | UP | 0.63 | 0.73 | 0.69 |
| 10-29 21:31 | +5 | ETH | UP | 0.63 | 0.69 | 0.28 |
| 10-29 21:30 | +10 stop | BNB | UP | 0.63 | 0.48 | -1.85 |
| 10-29 21:30 | +20 | BNB | UP | 0.63 | open |  |
| 10-29 21:30 | +15 | BNB | UP | 0.64 | open |  |
| 10-29 21:30 | +10 | BNB | UP | 0.64 | open |  |
| 10-29 21:30 | +5 | BNB | UP | 0.64 | open |  |
| 10-29 21:30 | +10 stop | XRP | UP | 0.66 | 0.79 | 1.02 |
| 10-29 21:30 | +20 | XRP | UP | 0.66 | open |  |
| 10-29 21:30 | +15 | XRP | UP | 0.66 | 0.82 | 1.34 |
| 10-29 21:30 | +10 | XRP | UP | 0.65 | 0.79 | 1.12 |
| 10-29 21:30 | +5 | XRP | UP | 0.65 | 0.70 | 0.19 |
| 10-29 21:30 | +10 stop | BTC | UP | 0.71 | 0.86 | 1.26 |
| 10-29 21:30 | +20 | BTC | UP | 0.70 | open |  |
| 10-29 21:30 | +15 | BTC | UP | 0.70 | 0.86 | 1.36 |
| 10-29 21:30 | +10 | BTC | UP | 0.70 | 0.86 | 1.36 |
| 10-29 21:30 | +5 | BTC | UP | 0.70 | 0.77 | 0.42 |
