# Range-Scalp Bot

*Updated Tue Nov 03 12:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45937 | 39997 | 5940 (69) | 8 | $-13264.13 | -4.6% |
| **+10¢** | 34295 | 27413 | 6882 (91) | 9 | $-12135.73 | -5.6% |
| **+15¢** | 28701 | 21299 | 7402 (119) | 8 | $-11107.63 | -6.2% |
| **+20¢** | 25491 | 17734 | 7757 (155) | 8 | $-9886.80 | -6.2% |
| **+10¢ (15¢ stop)** | 56039 | 55950 | 89 (53) | 4 | $-21022.85 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 12:40 | +10 stop | BTC | UP | 0.67 | open |  |
| 11-03 12:40 | +10 stop | XRP | UP | 0.59 | open |  |
| 11-03 12:40 | +5 | XRP | UP | 0.59 | open |  |
| 11-03 12:39 | +10 stop | ETH | UP | 0.59 | 0.27 | -3.51 |
| 11-03 12:39 | +10 stop | SOL | DOWN | 0.64 | open |  |
| 11-03 12:39 | +10 | SOL | DOWN | 0.64 | open |  |
| 11-03 12:39 | +5 | SOL | DOWN | 0.64 | 0.73 | 0.59 |
| 11-03 12:39 | +10 stop | DOGE | UP | 0.66 | 0.51 | -1.84 |
| 11-03 12:39 | +10 | DOGE | UP | 0.66 | open |  |
| 11-03 12:39 | +5 | DOGE | UP | 0.66 | open |  |
| 11-03 12:39 | +10 stop | SOL | DOWN | 0.45 | 0.57 | 0.84 |
| 11-03 12:39 | +20 | SOL | DOWN | 0.45 | 0.73 | 2.48 |
| 11-03 12:39 | +15 | SOL | DOWN | 0.45 | 0.64 | 1.55 |
| 11-03 12:39 | +10 | SOL | DOWN | 0.45 | 0.57 | 0.84 |
| 11-03 12:39 | +5 | SOL | DOWN | 0.46 | 0.57 | 0.74 |
| 11-03 12:38 | +10 stop | NEAR | DOWN | 0.57 | open |  |
| 11-03 12:38 | +10 stop | DOGE | DOWN | 0.43 | 0.55 | 0.84 |
| 11-03 12:38 | +10 | DOGE | DOWN | 0.43 | 0.55 | 0.84 |
| 11-03 12:38 | +5 | DOGE | DOWN | 0.43 | 0.55 | 0.84 |
| 11-03 12:38 | +10 stop | XRP | UP | 0.48 | 0.65 | 1.36 |
| 11-03 12:38 | +5 | XRP | UP | 0.48 | 0.54 | 0.24 |
| 11-03 12:37 | +5 | BNB | DOWN | 0.60 | open |  |
| 11-03 12:36 | +10 stop | NEAR | DOWN | 0.71 | 0.51 | -2.33 |
| 11-03 12:36 | +10 stop | BTC | UP | 0.63 | 0.74 | 0.79 |
| 11-03 12:36 | +20 | ETH | DOWN | 0.70 | open |  |
| 11-03 12:36 | +5 | ETH | DOWN | 0.71 | open |  |
| 11-03 12:36 | +10 stop | BNB | DOWN | 0.59 | 0.44 | -1.85 |
| 11-03 12:36 | +10 | BNB | DOWN | 0.59 | open |  |
| 11-03 12:36 | +5 | BNB | DOWN | 0.59 | 0.64 | 0.16 |
| 11-03 12:35 | +10 stop | HYPE | UP | 0.56 | 0.74 | 1.48 |
| 11-03 12:35 | +10 stop | ETH | DOWN | 0.70 | 0.53 | -2.03 |
| 11-03 12:35 | +15 | ETH | DOWN | 0.70 | open |  |
| 11-03 12:35 | +10 | ETH | DOWN | 0.70 | open |  |
| 11-03 12:35 | +5 | ETH | DOWN | 0.70 | 0.76 | 0.32 |
| 11-03 12:34 | +10 stop | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 11-03 12:34 | +10 stop | BTC | UP | 0.50 | 0.64 | 1.05 |
| 11-03 12:34 | +5 | XRP | DOWN | 0.60 | 0.66 | 0.22 |
| 11-03 12:33 | +10 stop | ZEC | UP | 0.66 | 0.79 | 1.02 |
| 11-03 12:33 | +10 stop | ETH | DOWN | 0.56 | 0.69 | 0.97 |
| 11-03 12:33 | +20 | ETH | DOWN | 0.56 | 0.76 | 1.69 |
