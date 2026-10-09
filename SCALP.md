# Range-Scalp Bot

*Updated Fri Oct 09 08:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8796 | 7608 | 1188 (13) | 2 | $-2891.06 | -5.2% |
| **+10¢** | 6660 | 5262 | 1398 (25) | 5 | $-2800.87 | -6.7% |
| **+15¢** | 5616 | 4143 | 1473 (37) | 6 | $-2288.54 | -6.5% |
| **+20¢** | 5000 | 3472 | 1528 (45) | 6 | $-1882.16 | -6.0% |
| **+10¢ (15¢ stop)** | 10727 | 10697 | 30 (19) | 2 | $-3997.01 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 08:21 | +10 stop | ETH | DOWN | 0.70 | open |  |
| 10-09 08:21 | +10 | ETH | DOWN | 0.71 | open |  |
| 10-09 08:21 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 10-09 08:21 | +5 | ZEC | UP | 0.56 | open |  |
| 10-09 08:21 | +15 | BTC | DOWN | 0.71 | open |  |
| 10-09 08:21 | +10 | BTC | DOWN | 0.71 | open |  |
| 10-09 08:21 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-09 08:21 | +10 stop | ETH | DOWN | 0.50 | 0.63 | 0.95 |
| 10-09 08:21 | +10 | ETH | DOWN | 0.50 | 0.63 | 0.95 |
| 10-09 08:21 | +5 | ETH | DOWN | 0.50 | 0.63 | 0.95 |
| 10-09 08:20 | +10 stop | ZEC | UP | 0.56 | 0.36 | -2.33 |
| 10-09 08:20 | +5 | ZEC | UP | 0.55 | 0.61 | 0.27 |
| 10-09 08:19 | +5 | BTC | DOWN | 0.68 | 0.77 | 0.61 |
| 10-09 08:19 | +10 stop | BNB | DOWN | 0.61 | 0.73 | 0.89 |
| 10-09 08:19 | +10 stop | BTC | DOWN | 0.69 | open |  |
| 10-09 08:19 | +10 stop | NEAR | UP | 0.58 | 0.73 | 1.18 |
| 10-09 08:18 | +5 | ZEC | DOWN | 0.54 | 0.62 | 0.45 |
| 10-09 08:18 | +5 | ETH | DOWN | 0.70 | 0.76 | 0.32 |
| 10-09 08:18 | +10 stop | BNB | DOWN | 0.65 | 0.48 | -2.04 |
| 10-09 08:18 | +10 | BNB | DOWN | 0.65 | open |  |
| 10-09 08:18 | +5 | BNB | DOWN | 0.65 | 0.73 | 0.50 |
| 10-09 08:17 | +10 stop | ZEC | DOWN | 0.57 | 0.38 | -2.25 |
| 10-09 08:17 | +20 | ZEC | DOWN | 0.57 | open |  |
| 10-09 08:17 | +15 | ZEC | DOWN | 0.57 | open |  |
| 10-09 08:17 | +10 | ZEC | DOWN | 0.57 | open |  |
| 10-09 08:17 | +5 | ZEC | DOWN | 0.57 | 0.62 | 0.15 |
| 10-09 08:17 | +10 stop | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 10-09 08:17 | +20 | ETH | DOWN | 0.64 | open |  |
| 10-09 08:17 | +15 | ETH | DOWN | 0.64 | open |  |
| 10-09 08:17 | +10 | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 10-09 08:17 | +5 | ETH | DOWN | 0.64 | 0.71 | 0.38 |
| 10-09 08:17 | +10 stop | BNB | DOWN | 0.62 | 0.75 | 0.99 |
| 10-09 08:17 | +20 | BNB | DOWN | 0.62 | open |  |
| 10-09 08:17 | +15 | BNB | DOWN | 0.62 | open |  |
| 10-09 08:17 | +10 | BNB | DOWN | 0.62 | 0.75 | 0.99 |
| 10-09 08:17 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
| 10-09 08:17 | +10 stop | XRP | DOWN | 0.59 | 0.74 | 1.19 |
| 10-09 08:17 | +20 | XRP | DOWN | 0.60 | 0.80 | 1.73 |
| 10-09 08:17 | +15 | XRP | DOWN | 0.60 | 0.75 | 1.19 |
| 10-09 08:17 | +10 | XRP | DOWN | 0.60 | 0.74 | 1.09 |
