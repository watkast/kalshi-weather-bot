# Range-Scalp Bot

*Updated Sat Nov 07 14:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51053 | 44504 | 6549 (78) | 1 | $-14298.26 | -4.4% |
| **+10¢** | 38116 | 30484 | 7632 (105) | 4 | $-13262.60 | -5.5% |
| **+15¢** | 31902 | 23676 | 8226 (134) | 4 | $-12201.20 | -6.1% |
| **+20¢** | 28371 | 19748 | 8623 (177) | 4 | $-10777.92 | -6.1% |
| **+10¢ (15¢ stop)** | 62176 | 62073 | 103 (61) | 4 | $-22953.96 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 14:16 | +10 stop | BNB | UP | 0.53 | open |  |
| 11-07 14:16 | +20 | BNB | UP | 0.53 | open |  |
| 11-07 14:16 | +15 | BNB | UP | 0.53 | open |  |
| 11-07 14:16 | +10 | BNB | UP | 0.53 | open |  |
| 11-07 14:16 | +5 | BNB | UP | 0.53 | 0.62 | 0.55 |
| 11-07 14:16 | +10 stop | DOGE | UP | 0.39 | 0.61 | 1.86 |
| 11-07 14:16 | +20 | DOGE | UP | 0.39 | 0.61 | 1.86 |
| 11-07 14:16 | +15 | DOGE | UP | 0.39 | 0.61 | 1.86 |
| 11-07 14:16 | +10 | DOGE | UP | 0.39 | 0.61 | 1.86 |
| 11-07 14:16 | +5 | DOGE | UP | 0.39 | 0.61 | 1.86 |
| 11-07 14:16 | +10 stop | XRP | UP | 0.42 | 0.63 | 1.75 |
| 11-07 14:16 | +20 | XRP | UP | 0.42 | 0.63 | 1.75 |
| 11-07 14:16 | +15 | XRP | UP | 0.42 | 0.63 | 1.75 |
| 11-07 14:16 | +10 | XRP | UP | 0.42 | 0.63 | 1.75 |
| 11-07 14:16 | +5 | XRP | UP | 0.42 | 0.63 | 1.75 |
| 11-07 14:16 | +10 stop | BTC | UP | 0.66 | open |  |
| 11-07 14:16 | +20 | BTC | UP | 0.66 | open |  |
| 11-07 14:16 | +15 | BTC | UP | 0.66 | open |  |
| 11-07 14:16 | +10 | BTC | UP | 0.66 | open |  |
| 11-07 14:16 | +5 | BTC | UP | 0.66 | open |  |
| 11-07 14:16 | +10 stop | ETH | UP | 0.55 | open |  |
| 11-07 14:16 | +20 | ETH | UP | 0.55 | open |  |
| 11-07 14:16 | +15 | ETH | UP | 0.55 | open |  |
| 11-07 14:16 | +10 | ETH | UP | 0.55 | open |  |
| 11-07 14:16 | +5 | ETH | UP | 0.55 | 0.63 | 0.45 |
| 11-07 14:16 | +10 stop | ZEC | UP | 0.54 | open |  |
| 11-07 14:16 | +20 | ZEC | UP | 0.54 | open |  |
| 11-07 14:16 | +15 | ZEC | UP | 0.54 | open |  |
| 11-07 14:16 | +10 | ZEC | UP | 0.53 | open |  |
| 11-07 14:16 | +5 | ZEC | UP | 0.53 | 0.58 | 0.14 |
| 11-07 14:11 | +10 stop | BTC | DOWN | 0.69 | 0.53 | -1.93 |
| 11-07 14:10 | +10 stop | ETH | UP | 0.68 | 0.21 | -4.98 |
| 11-07 14:09 | +10 stop | SOL | DOWN | 0.62 | 0.82 | 1.72 |
| 11-07 14:07 | +10 stop | HYPE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-07 14:07 | +10 stop | ETH | UP | 0.62 | 0.47 | -1.85 |
| 11-07 14:07 | +15 | ETH | UP | 0.62 | 0.79 | 1.41 |
| 11-07 14:07 | +10 | ETH | UP | 0.62 | 0.79 | 1.41 |
| 11-07 14:06 | +10 stop | SOL | UP | 0.71 | 0.46 | -2.83 |
| 11-07 14:06 | +10 | SOL | UP | 0.71 | no | -7.25 |
| 11-07 14:06 | +10 stop | NEAR | UP | 0.56 | 0.37 | -2.25 |
