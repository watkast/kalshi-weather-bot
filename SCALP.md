# Range-Scalp Bot

*Updated Sun Oct 04 09:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2088 | 1801 | 287 (3) | 3 | $-701.71 | -5.3% |
| **+10¢** | 1626 | 1308 | 318 (4) | 4 | $-509.04 | -5.0% |
| **+15¢** | 1369 | 1031 | 338 (5) | 4 | $-436.05 | -5.1% |
| **+20¢** | 1208 | 853 | 355 (7) | 4 | $-387.68 | -5.1% |
| **+10¢ (15¢ stop)** | 2595 | 2594 | 1 (1) | 3 | $-987.28 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 09:50 | +10 stop | NEAR | DOWN | 0.63 | open |  |
| 10-04 09:50 | +10 stop | SOL | UP | 0.62 | open |  |
| 10-04 09:50 | +15 | SOL | UP | 0.62 | open |  |
| 10-04 09:50 | +10 | SOL | UP | 0.62 | open |  |
| 10-04 09:50 | +5 | SOL | UP | 0.62 | open |  |
| 10-04 09:50 | +10 stop | BTC | DOWN | 0.62 | open |  |
| 10-04 09:50 | +10 | BTC | DOWN | 0.62 | open |  |
| 10-04 09:50 | +5 | BTC | DOWN | 0.62 | 0.68 | 0.27 |
| 10-04 09:48 | +10 stop | NEAR | DOWN | 0.69 | 0.54 | -1.83 |
| 10-04 09:48 | +20 | NEAR | DOWN | 0.69 | open |  |
| 10-04 09:48 | +15 | NEAR | DOWN | 0.69 | open |  |
| 10-04 09:48 | +10 | NEAR | DOWN | 0.69 | open |  |
| 10-04 09:48 | +5 | NEAR | DOWN | 0.69 | open |  |
| 10-04 09:47 | +10 stop | BTC | UP | 0.67 | 0.79 | 0.92 |
| 10-04 09:47 | +20 | BTC | UP | 0.67 | open |  |
| 10-04 09:47 | +15 | BTC | UP | 0.67 | open |  |
| 10-04 09:47 | +10 | BTC | UP | 0.67 | 0.79 | 0.92 |
| 10-04 09:47 | +5 | BTC | UP | 0.67 | 0.76 | 0.61 |
| 10-04 09:47 | +10 stop | BNB | UP | 0.55 | 0.18 | -3.99 |
| 10-04 09:47 | +20 | BNB | UP | 0.55 | open |  |
| 10-04 09:47 | +15 | BNB | UP | 0.55 | open |  |
| 10-04 09:47 | +10 | BNB | UP | 0.55 | open |  |
| 10-04 09:47 | +5 | BNB | UP | 0.55 | open |  |
| 10-04 09:46 | +5 | XRP | UP | 0.65 | 0.70 | 0.19 |
| 10-04 09:46 | +10 stop | ETH | UP | 0.67 | 0.80 | 1.02 |
| 10-04 09:46 | +20 | ETH | UP | 0.67 | 0.90 | 2.08 |
| 10-04 09:46 | +15 | ETH | UP | 0.67 | 0.82 | 1.23 |
| 10-04 09:46 | +10 | ETH | UP | 0.67 | 0.80 | 1.02 |
| 10-04 09:46 | +5 | ETH | UP | 0.67 | 0.80 | 1.02 |
| 10-04 09:46 | +10 stop | SOL | UP | 0.70 | 0.80 | 0.73 |
| 10-04 09:46 | +20 | SOL | UP | 0.70 | open |  |
| 10-04 09:46 | +15 | SOL | UP | 0.70 | 0.86 | 1.36 |
| 10-04 09:46 | +10 | SOL | UP | 0.70 | 0.80 | 0.73 |
| 10-04 09:46 | +5 | SOL | UP | 0.70 | 0.76 | 0.32 |
| 10-04 09:46 | +10 stop | DOGE | UP | 0.64 | 0.76 | 0.89 |
| 10-04 09:46 | +20 | DOGE | UP | 0.64 | 0.85 | 1.83 |
| 10-04 09:46 | +15 | DOGE | UP | 0.64 | 0.80 | 1.30 |
| 10-04 09:46 | +10 | DOGE | UP | 0.64 | 0.76 | 0.89 |
| 10-04 09:46 | +5 | DOGE | UP | 0.64 | 0.76 | 0.89 |
| 10-04 09:46 | +10 stop | XRP | UP | 0.59 | 0.70 | 0.78 |
