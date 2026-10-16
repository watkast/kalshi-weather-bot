# Range-Scalp Bot

*Updated Fri Oct 16 10:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19085 | 16589 | 2496 (28) | 0 | $-5719.12 | -4.8% |
| **+10¢** | 14382 | 11495 | 2887 (40) | 0 | $-5162.43 | -5.7% |
| **+15¢** | 12041 | 8937 | 3104 (59) | 0 | $-4641.11 | -6.1% |
| **+20¢** | 10681 | 7428 | 3253 (78) | 2 | $-4114.75 | -6.1% |
| **+10¢ (15¢ stop)** | 23473 | 23423 | 50 (29) | 0 | $-9052.31 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 10:00 | +10 stop | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 10-16 10:00 | +20 | XRP | DOWN | 0.66 | open |  |
| 10-16 10:00 | +15 | XRP | DOWN | 0.66 | 0.83 | 1.46 |
| 10-16 10:00 | +10 | XRP | DOWN | 0.66 | 0.76 | 0.73 |
| 10-16 10:00 | +5 | XRP | DOWN | 0.66 | 0.72 | 0.31 |
| 10-16 10:00 | +10 stop | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 10-16 10:00 | +20 | BTC | DOWN | 0.66 | open |  |
| 10-16 10:00 | +15 | BTC | DOWN | 0.66 | 0.84 | 1.54 |
| 10-16 10:00 | +10 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-16 10:00 | +5 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-16 09:57 | +10 stop | DOGE | UP | 0.51 | 0.30 | -2.43 |
| 10-16 09:57 | +5 | DOGE | UP | 0.63 | no | -6.47 |
| 10-16 09:56 | +10 stop | BNB | UP | 0.62 | 0.74 | 0.89 |
| 10-16 09:56 | +5 | DOGE | DOWN | 0.41 | 0.58 | 1.35 |
| 10-16 09:56 | +5 | ETH | UP | 0.60 | no | -6.17 |
| 10-16 09:56 | +10 stop | ETH | UP | 0.60 | 0.29 | -3.42 |
| 10-16 09:56 | +10 | ETH | UP | 0.60 | no | -6.17 |
| 10-16 09:56 | +5 | ETH | UP | 0.54 | 0.68 | 1.06 |
| 10-16 09:55 | +10 stop | BNB | DOWN | 0.57 | 0.41 | -1.94 |
| 10-16 09:55 | +10 stop | DOGE | DOWN | 0.64 | 0.42 | -2.55 |
| 10-16 09:55 | +10 stop | HYPE | DOWN | 0.62 | 0.76 | 1.10 |
| 10-16 09:55 | +10 | HYPE | DOWN | 0.62 | 0.76 | 1.10 |
| 10-16 09:55 | +5 | HYPE | DOWN | 0.62 | 0.71 | 0.58 |
| 10-16 09:55 | +5 | DOGE | DOWN | 0.58 | 0.66 | 0.46 |
| 10-16 09:55 | +10 | SOL | DOWN | 0.51 | 0.65 | 1.06 |
| 10-16 09:55 | +5 | SOL | DOWN | 0.51 | 0.57 | 0.24 |
| 10-16 09:53 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-16 09:53 | +10 stop | SOL | DOWN | 0.69 | 0.48 | -2.48 |
| 10-16 09:53 | +10 stop | DOGE | DOWN | 0.71 | 0.54 | -2.03 |
| 10-16 09:53 | +20 | DOGE | DOWN | 0.71 | 0.92 | 1.94 |
| 10-16 09:53 | +15 | DOGE | DOWN | 0.71 | 0.89 | 1.58 |
| 10-16 09:53 | +10 | DOGE | DOWN | 0.71 | 0.89 | 1.58 |
| 10-16 09:53 | +5 | DOGE | DOWN | 0.71 | 0.78 | 0.42 |
| 10-16 09:53 | +10 stop | BTC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-16 09:53 | +10 | BTC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-16 09:53 | +10 stop | BNB | DOWN | 0.63 | 0.46 | -2.05 |
| 10-16 09:53 | +20 | BNB | DOWN | 0.63 | yes | -6.47 |
| 10-16 09:53 | +15 | BNB | DOWN | 0.63 | yes | -6.47 |
| 10-16 09:53 | +10 | BNB | DOWN | 0.63 | yes | -6.47 |
| 10-16 09:53 | +5 | BNB | DOWN | 0.63 | yes | -6.47 |
