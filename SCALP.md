# Range-Scalp Bot

*Updated Fri Oct 16 07:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18843 | 16368 | 2475 (28) | 4 | $-5718.68 | -4.8% |
| **+10¢** | 14194 | 11329 | 2865 (40) | 4 | $-5201.38 | -5.8% |
| **+15¢** | 11895 | 8812 | 3083 (59) | 6 | $-4709.55 | -6.3% |
| **+20¢** | 10564 | 7337 | 3227 (78) | 7 | $-4141.56 | -6.2% |
| **+10¢ (15¢ stop)** | 23191 | 23141 | 50 (29) | 3 | $-8963.54 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 07:19 | +5 | SOL | UP | 0.64 | 0.71 | 0.38 |
| 10-16 07:19 | +5 | SOL | UP | 0.58 | 0.64 | 0.25 |
| 10-16 07:18 | +5 | BTC | UP | 0.71 | 0.77 | 0.32 |
| 10-16 07:18 | +5 | ZEC | UP | 0.62 | open |  |
| 10-16 07:18 | +10 stop | HYPE | UP | 0.57 | open |  |
| 10-16 07:18 | +5 | DOGE | DOWN | 0.51 | open |  |
| 10-16 07:17 | +5 | DOGE | DOWN | 0.50 | 0.56 | 0.24 |
| 10-16 07:17 | +5 | NEAR | DOWN | 0.63 | open |  |
| 10-16 07:17 | +5 | DOGE | UP | 0.50 | 0.56 | 0.24 |
| 10-16 07:17 | +5 | XRP | UP | 0.58 | 0.67 | 0.56 |
| 10-16 07:16 | +10 stop | DOGE | UP | 0.56 | open |  |
| 10-16 07:16 | +20 | DOGE | UP | 0.56 | open |  |
| 10-16 07:16 | +15 | DOGE | UP | 0.56 | open |  |
| 10-16 07:16 | +10 | DOGE | UP | 0.56 | open |  |
| 10-16 07:16 | +5 | DOGE | UP | 0.56 | 0.64 | 0.45 |
| 10-16 07:16 | +10 stop | NEAR | UP | 0.55 | 0.71 | 1.27 |
| 10-16 07:16 | +20 | NEAR | UP | 0.55 | 0.77 | 1.89 |
| 10-16 07:16 | +15 | NEAR | UP | 0.54 | 0.71 | 1.37 |
| 10-16 07:16 | +10 | NEAR | UP | 0.55 | 0.71 | 1.27 |
| 10-16 07:16 | +5 | NEAR | UP | 0.55 | 0.61 | 0.25 |
| 10-16 07:16 | +10 stop | SOL | UP | 0.61 | 0.71 | 0.68 |
| 10-16 07:16 | +20 | SOL | UP | 0.62 | open |  |
| 10-16 07:16 | +15 | SOL | UP | 0.62 | open |  |
| 10-16 07:16 | +10 | SOL | UP | 0.62 | open |  |
| 10-16 07:16 | +5 | SOL | UP | 0.62 | 0.67 | 0.18 |
| 10-16 07:16 | +10 stop | XRP | UP | 0.63 | 0.76 | 1.00 |
| 10-16 07:16 | +20 | XRP | UP | 0.63 | open |  |
| 10-16 07:16 | +15 | XRP | UP | 0.63 | open |  |
| 10-16 07:16 | +10 | XRP | UP | 0.63 | 0.76 | 1.00 |
| 10-16 07:16 | +5 | XRP | UP | 0.63 | 0.68 | 0.17 |
| 10-16 07:16 | +10 stop | BTC | UP | 0.61 | 0.72 | 0.78 |
| 10-16 07:16 | +20 | BTC | UP | 0.61 | open |  |
| 10-16 07:16 | +15 | BTC | UP | 0.61 | 0.77 | 1.30 |
| 10-16 07:16 | +10 | BTC | UP | 0.61 | 0.72 | 0.78 |
| 10-16 07:16 | +5 | BTC | UP | 0.61 | 0.68 | 0.37 |
| 10-16 07:16 | +10 stop | ZEC | UP | 0.57 | open |  |
| 10-16 07:16 | +20 | ZEC | UP | 0.57 | open |  |
| 10-16 07:16 | +15 | ZEC | UP | 0.57 | open |  |
| 10-16 07:16 | +10 | ZEC | UP | 0.57 | open |  |
| 10-16 07:16 | +5 | ZEC | UP | 0.57 | 0.63 | 0.25 |
