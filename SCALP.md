# Range-Scalp Bot

*Updated Tue Nov 17 23:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63272 | 55191 | 8081 (118) | 5 | $-17229.21 | -4.3% |
| **+10¢** | 47266 | 37810 | 9456 (159) | 7 | $-16115.92 | -5.4% |
| **+15¢** | 39626 | 29429 | 10197 (203) | 7 | $-14602.05 | -5.9% |
| **+20¢** | 35304 | 24603 | 10701 (258) | 7 | $-12847.51 | -5.8% |
| **+10¢ (15¢ stop)** | 77014 | 76856 | 158 (93) | 0 | $-28365.99 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 23:42 | +10 stop | SOL | UP | 0.36 | 0.61 | 2.16 |
| 11-17 23:42 | +10 stop | BTC | UP | 0.41 | 0.68 | 2.37 |
| 11-17 23:42 | +10 stop | XRP | DOWN | 0.60 | 0.77 | 1.40 |
| 11-17 23:42 | +10 stop | XRP | UP | 0.41 | 0.63 | 1.86 |
| 11-17 23:41 | +10 stop | SOL | UP | 0.70 | 0.55 | -1.83 |
| 11-17 23:41 | +20 | SOL | UP | 0.70 | open |  |
| 11-17 23:41 | +15 | SOL | UP | 0.70 | open |  |
| 11-17 23:41 | +10 | SOL | UP | 0.70 | open |  |
| 11-17 23:40 | +10 stop | XRP | UP | 0.71 | 0.48 | -2.63 |
| 11-17 23:40 | +20 | XRP | UP | 0.71 | open |  |
| 11-17 23:40 | +15 | XRP | UP | 0.71 | open |  |
| 11-17 23:40 | +10 | XRP | UP | 0.71 | open |  |
| 11-17 23:40 | +5 | XRP | UP | 0.71 | open |  |
| 11-17 23:39 | +10 stop | DOGE | UP | 0.70 | 0.82 | 0.94 |
| 11-17 23:38 | +5 | NEAR | UP | 0.69 | 0.79 | 0.70 |
| 11-17 23:38 | +10 stop | SOL | DOWN | 0.58 | 0.37 | -2.45 |
| 11-17 23:38 | +5 | SOL | DOWN | 0.58 | 0.71 | 0.97 |
| 11-17 23:38 | +10 stop | ZEC | UP | 0.63 | 0.82 | 1.62 |
| 11-17 23:38 | +10 stop | BNB | UP | 0.58 | 0.74 | 1.28 |
| 11-17 23:38 | +5 | BNB | UP | 0.56 | 0.66 | 0.66 |
| 11-17 23:38 | +10 stop | ETH | UP | 0.68 | 0.78 | 0.71 |
| 11-17 23:38 | +10 stop | BTC | UP | 0.59 | 0.74 | 1.19 |
| 11-17 23:37 | +5 | SOL | UP | 0.53 | 0.58 | 0.14 |
| 11-17 23:37 | +10 stop | XRP | UP | 0.58 | 0.37 | -2.45 |
| 11-17 23:37 | +10 stop | SOL | UP | 0.62 | 0.44 | -2.15 |
| 11-17 23:37 | +5 | XRP | UP | 0.59 | 0.69 | 0.68 |
| 11-17 23:37 | +10 stop | BNB | UP | 0.59 | 0.69 | 0.68 |
| 11-17 23:37 | +5 | BNB | UP | 0.59 | 0.69 | 0.68 |
| 11-17 23:37 | +10 stop | ETH | UP | 0.69 | 0.80 | 0.83 |
| 11-17 23:36 | +10 stop | BTC | DOWN | 0.60 | 0.38 | -2.54 |
| 11-17 23:36 | +20 | BTC | DOWN | 0.60 | open |  |
| 11-17 23:36 | +15 | BTC | DOWN | 0.60 | open |  |
| 11-17 23:36 | +10 | BTC | DOWN | 0.60 | open |  |
| 11-17 23:36 | +5 | BTC | DOWN | 0.59 | open |  |
| 11-17 23:36 | +10 stop | DOGE | UP | 0.64 | 0.46 | -2.15 |
| 11-17 23:35 | +15 | ETH | DOWN | 0.54 | open |  |
| 11-17 23:35 | +10 | ETH | DOWN | 0.54 | open |  |
| 11-17 23:35 | +5 | XRP | DOWN | 0.53 | 0.59 | 0.25 |
| 11-17 23:35 | +10 stop | DOGE | DOWN | 0.64 | 0.47 | -2.05 |
| 11-17 23:35 | +15 | DOGE | DOWN | 0.64 | open |  |
