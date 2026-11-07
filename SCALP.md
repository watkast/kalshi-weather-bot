# Range-Scalp Bot

*Updated Sat Nov 07 16:48 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51217 | 44648 | 6569 (79) | 0 | $-14316.30 | -4.4% |
| **+10¢** | 38234 | 30577 | 7657 (105) | 2 | $-13308.85 | -5.5% |
| **+15¢** | 32007 | 23754 | 8253 (134) | 3 | $-12232.27 | -6.1% |
| **+20¢** | 28468 | 19818 | 8650 (177) | 3 | $-10796.44 | -6.0% |
| **+10¢ (15¢ stop)** | 62398 | 62295 | 103 (61) | 2 | $-23107.12 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 16:47 | +10 stop | BNB | DOWN | 0.70 | open |  |
| 11-07 16:47 | +20 | BNB | DOWN | 0.70 | open |  |
| 11-07 16:47 | +15 | BNB | DOWN | 0.70 | open |  |
| 11-07 16:47 | +10 | BNB | DOWN | 0.70 | open |  |
| 11-07 16:47 | +5 | BNB | DOWN | 0.70 | 0.76 | 0.27 |
| 11-07 16:46 | +10 stop | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 11-07 16:46 | +20 | ETH | DOWN | 0.65 | open |  |
| 11-07 16:46 | +15 | ETH | DOWN | 0.66 | open |  |
| 11-07 16:46 | +10 | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 11-07 16:46 | +5 | ETH | DOWN | 0.66 | 0.73 | 0.40 |
| 11-07 16:46 | +10 stop | NEAR | DOWN | 0.71 | open |  |
| 11-07 16:46 | +20 | NEAR | DOWN | 0.71 | open |  |
| 11-07 16:46 | +15 | NEAR | DOWN | 0.71 | open |  |
| 11-07 16:46 | +10 | NEAR | DOWN | 0.71 | open |  |
| 11-07 16:46 | +5 | NEAR | DOWN | 0.71 | 0.76 | 0.22 |
| 11-07 16:44 | +10 stop | XRP | DOWN | 0.67 | 0.06 | -6.27 |
| 11-07 16:44 | +5 | XRP | DOWN | 0.67 | 0.74 | 0.40 |
| 11-07 16:43 | +10 stop | NEAR | UP | 0.52 | 0.64 | 0.85 |
| 11-07 16:42 | +10 stop | BTC | UP | 0.67 | 0.51 | -1.94 |
| 11-07 16:41 | +10 stop | BNB | UP | 0.68 | 0.16 | -5.46 |
| 11-07 16:41 | +10 stop | DOGE | DOWN | 0.52 | 0.76 | 2.09 |
| 11-07 16:41 | +10 stop | SOL | UP | 0.68 | 0.84 | 1.34 |
| 11-07 16:40 | +10 stop | DOGE | DOWN | 0.49 | 0.61 | 0.85 |
| 11-07 16:40 | +10 stop | BNB | UP | 0.58 | 0.70 | 0.87 |
| 11-07 16:39 | +10 stop | NEAR | DOWN | 0.64 | 0.34 | -3.33 |
| 11-07 16:39 | +10 | NEAR | DOWN | 0.64 | 0.99 | 3.36 |
| 11-07 16:39 | +5 | NEAR | DOWN | 0.64 | 0.99 | 3.36 |
| 11-07 16:39 | +10 stop | BTC | DOWN | 0.71 | 0.54 | -2.03 |
| 11-07 16:39 | +5 | BTC | DOWN | 0.71 | yes | -7.25 |
| 11-07 16:39 | +10 stop | SOL | UP | 0.57 | 0.67 | 0.66 |
| 11-07 16:38 | +10 stop | HYPE | UP | 0.62 | 0.11 | -5.34 |
| 11-07 16:37 | +20 | ZEC | UP | 0.67 | 0.89 | 1.97 |
| 11-07 16:37 | +15 | ZEC | UP | 0.67 | 0.82 | 1.23 |
| 11-07 16:37 | +5 | ZEC | UP | 0.67 | 0.72 | 0.19 |
| 11-07 16:37 | +5 | XRP | UP | 0.64 | 0.73 | 0.59 |
| 11-07 16:36 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-07 16:36 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-07 16:36 | +10 stop | DOGE | DOWN | 0.62 | 0.45 | -2.05 |
| 11-07 16:36 | +10 stop | XRP | UP | 0.59 | 0.73 | 1.09 |
| 11-07 16:36 | +5 | XRP | UP | 0.59 | 0.66 | 0.37 |
