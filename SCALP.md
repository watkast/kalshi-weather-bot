# Range-Scalp Bot

*Updated Tue Oct 06 08:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4799 | 4153 | 646 (7) | 5 | $-1512.38 | -5.0% |
| **+10¢** | 3682 | 2927 | 755 (11) | 7 | $-1414.07 | -6.1% |
| **+15¢** | 3091 | 2293 | 798 (14) | 8 | $-1211.07 | -6.2% |
| **+20¢** | 2769 | 1936 | 833 (19) | 8 | $-1006.26 | -5.8% |
| **+10¢ (15¢ stop)** | 5871 | 5858 | 13 (8) | 4 | $-2114.67 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 08:42 | +5 | ETH | DOWN | 0.60 | open |  |
| 10-06 08:42 | +10 stop | DOGE | UP | 0.62 | open |  |
| 10-06 08:42 | +20 | DOGE | UP | 0.62 | open |  |
| 10-06 08:42 | +15 | DOGE | UP | 0.62 | open |  |
| 10-06 08:42 | +10 | DOGE | UP | 0.62 | open |  |
| 10-06 08:42 | +5 | DOGE | UP | 0.62 | 0.69 | 0.38 |
| 10-06 08:41 | +10 stop | BTC | DOWN | 0.52 | open |  |
| 10-06 08:41 | +20 | BTC | DOWN | 0.52 | open |  |
| 10-06 08:41 | +15 | BTC | DOWN | 0.52 | open |  |
| 10-06 08:41 | +10 | BTC | DOWN | 0.52 | open |  |
| 10-06 08:41 | +5 | BTC | DOWN | 0.52 | 0.60 | 0.45 |
| 10-06 08:41 | +10 stop | NEAR | DOWN | 0.70 | open |  |
| 10-06 08:41 | +10 stop | ETH | DOWN | 0.58 | open |  |
| 10-06 08:41 | +20 | ETH | DOWN | 0.58 | open |  |
| 10-06 08:41 | +15 | ETH | DOWN | 0.58 | open |  |
| 10-06 08:41 | +10 | ETH | DOWN | 0.57 | open |  |
| 10-06 08:41 | +5 | ETH | DOWN | 0.57 | 0.62 | 0.15 |
| 10-06 08:41 | +10 stop | SOL | DOWN | 0.50 | 0.34 | -1.94 |
| 10-06 08:41 | +20 | SOL | DOWN | 0.50 | open |  |
| 10-06 08:41 | +15 | SOL | DOWN | 0.50 | open |  |
| 10-06 08:41 | +10 | SOL | DOWN | 0.50 | open |  |
| 10-06 08:41 | +5 | SOL | DOWN | 0.50 | open |  |
| 10-06 08:41 | +10 stop | BNB | UP | 0.70 | 0.80 | 0.77 |
| 10-06 08:41 | +20 | BNB | UP | 0.70 | open |  |
| 10-06 08:41 | +15 | BNB | UP | 0.70 | open |  |
| 10-06 08:41 | +10 | BNB | UP | 0.70 | 0.80 | 0.77 |
| 10-06 08:41 | +5 | BNB | UP | 0.70 | 0.77 | 0.38 |
| 10-06 08:40 | +10 stop | NEAR | DOWN | 0.69 | 0.51 | -2.13 |
| 10-06 08:39 | +10 stop | ZEC | UP | 0.71 | 0.93 | 2.00 |
| 10-06 08:38 | +10 stop | BNB | DOWN | 0.62 | 0.73 | 0.79 |
| 10-06 08:37 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 10-06 08:37 | +10 stop | XRP | DOWN | 0.56 | 0.69 | 0.97 |
| 10-06 08:37 | +5 | XRP | DOWN | 0.56 | 0.63 | 0.31 |
| 10-06 08:36 | +10 stop | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 10-06 08:36 | +5 | ETH | DOWN | 0.71 | 0.79 | 0.53 |
| 10-06 08:36 | +10 stop | NEAR | UP | 0.67 | 0.48 | -2.24 |
| 10-06 08:35 | +10 stop | BNB | UP | 0.55 | 0.39 | -1.95 |
| 10-06 08:35 | +10 stop | HYPE | DOWN | 0.69 | 0.49 | -2.33 |
| 10-06 08:34 | +10 stop | ETH | UP | 0.47 | 0.30 | -2.03 |
| 10-06 08:34 | +10 stop | SOL | UP | 0.49 | 0.64 | 1.15 |
