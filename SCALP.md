# Range-Scalp Bot

*Updated Sat Oct 03 05:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 225 | 191 | 34 (1) | 6 | $-95.91 | -6.6% |
| **+10¢** | 184 | 148 | 36 (1) | 7 | $-62.61 | -5.3% |
| **+15¢** | 153 | 116 | 37 (1) | 7 | $-55.05 | -5.7% |
| **+20¢** | 355 | 249 | 106 (2) | 9 | $-127.70 | -5.7% |
| **+10¢ (15¢ stop)** | 303 | 303 | 0 (0) | 7 | $-144.89 | -7.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-03 05:17 | +10 stop | DOGE | UP | 0.62 | open |  |
| 10-03 05:17 | +20 | DOGE | UP | 0.62 | open |  |
| 10-03 05:17 | +15 | DOGE | UP | 0.62 | open |  |
| 10-03 05:17 | +10 | DOGE | UP | 0.62 | open |  |
| 10-03 05:17 | +5 | DOGE | UP | 0.62 | open |  |
| 10-03 05:17 | +10 stop | ZEC | UP | 0.67 | open |  |
| 10-03 05:17 | +20 | ZEC | UP | 0.67 | open |  |
| 10-03 05:17 | +15 | ZEC | UP | 0.67 | open |  |
| 10-03 05:17 | +10 | ZEC | UP | 0.67 | open |  |
| 10-03 05:17 | +5 | ZEC | UP | 0.67 | open |  |
| 10-03 05:17 | +5 | NEAR | UP | 0.63 | open |  |
| 10-03 05:17 | +5 | XRP | UP | 0.71 | 0.76 | 0.22 |
| 10-03 05:16 | +5 | ETH | UP | 0.68 | 0.77 | 0.61 |
| 10-03 05:16 | +10 stop | BNB | UP | 0.56 | open |  |
| 10-03 05:16 | +20 | BNB | UP | 0.56 | open |  |
| 10-03 05:16 | +15 | BNB | UP | 0.56 | open |  |
| 10-03 05:16 | +10 | BNB | UP | 0.56 | open |  |
| 10-03 05:16 | +5 | BNB | UP | 0.56 | open |  |
| 10-03 05:16 | +10 stop | XRP | UP | 0.61 | 0.73 | 0.89 |
| 10-03 05:16 | +20 | XRP | UP | 0.61 | open |  |
| 10-03 05:16 | +15 | XRP | UP | 0.61 | 0.76 | 1.20 |
| 10-03 05:16 | +10 | XRP | UP | 0.62 | 0.73 | 0.79 |
| 10-03 05:16 | +5 | XRP | UP | 0.62 | 0.67 | 0.17 |
| 10-03 05:16 | +10 stop | SOL | UP | 0.64 | open |  |
| 10-03 05:16 | +20 | SOL | UP | 0.64 | open |  |
| 10-03 05:16 | +15 | SOL | UP | 0.64 | open |  |
| 10-03 05:16 | +10 | SOL | UP | 0.64 | open |  |
| 10-03 05:16 | +5 | SOL | UP | 0.64 | 0.71 | 0.37 |
| 10-03 05:16 | +10 stop | NEAR | UP | 0.56 | open |  |
| 10-03 05:16 | +20 | NEAR | UP | 0.56 | open |  |
| 10-03 05:16 | +15 | NEAR | UP | 0.56 | open |  |
| 10-03 05:16 | +10 | NEAR | UP | 0.56 | open |  |
| 10-03 05:16 | +5 | NEAR | UP | 0.56 | 0.61 | 0.15 |
| 10-03 05:16 | +10 stop | BTC | UP | 0.61 | open |  |
| 10-03 05:16 | +20 | BTC | UP | 0.61 | open |  |
| 10-03 05:16 | +15 | BTC | UP | 0.61 | open |  |
| 10-03 05:16 | +10 | BTC | UP | 0.61 | open |  |
| 10-03 05:16 | +5 | BTC | UP | 0.61 | open |  |
| 10-03 05:16 | +10 stop | ETH | UP | 0.61 | 0.77 | 1.30 |
| 10-03 05:16 | +20 | ETH | UP | 0.61 | open |  |
