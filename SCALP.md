# Range-Scalp Bot

*Updated Sat Nov 07 21:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51553 | 44953 | 6600 (80) | 7 | $-14284.51 | -4.4% |
| **+10¢** | 38464 | 30767 | 7697 (106) | 9 | $-13312.58 | -5.5% |
| **+15¢** | 32204 | 23908 | 8296 (135) | 9 | $-12223.01 | -6.1% |
| **+20¢** | 28645 | 19950 | 8695 (178) | 9 | $-10776.42 | -6.0% |
| **+10¢ (15¢ stop)** | 62786 | 62683 | 103 (61) | 2 | $-23258.18 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 21:42 | +10 stop | HYPE | DOWN | 0.53 | open |  |
| 11-07 21:42 | +10 stop | NEAR | UP | 0.65 | open |  |
| 11-07 21:41 | +10 stop | HYPE | UP | 0.65 | 0.34 | -3.42 |
| 11-07 21:41 | +15 | HYPE | UP | 0.65 | open |  |
| 11-07 21:41 | +10 | HYPE | UP | 0.65 | open |  |
| 11-07 21:41 | +5 | HYPE | UP | 0.65 | open |  |
| 11-07 21:38 | +10 stop | DOGE | DOWN | 0.47 | 0.22 | -2.81 |
| 11-07 21:37 | +5 | ETH | UP | 0.68 | 0.79 | 0.82 |
| 11-07 21:37 | +10 stop | BTC | DOWN | 0.56 | 0.31 | -2.83 |
| 11-07 21:37 | +10 stop | BNB | UP | 0.65 | 0.80 | 1.22 |
| 11-07 21:37 | +5 | ETH | UP | 0.50 | 0.66 | 1.26 |
| 11-07 21:35 | +10 stop | ETH | UP | 0.64 | 0.79 | 1.21 |
| 11-07 21:35 | +5 | ETH | UP | 0.66 | 0.73 | 0.40 |
| 11-07 21:35 | +10 stop | BTC | UP | 0.56 | 0.38 | -2.15 |
| 11-07 21:35 | +10 stop | NEAR | UP | 0.66 | 0.49 | -2.04 |
| 11-07 21:35 | +10 stop | DOGE | UP | 0.64 | 0.47 | -2.05 |
| 11-07 21:34 | +10 stop | NEAR | DOWN | 0.55 | 0.38 | -2.05 |
| 11-07 21:33 | +10 stop | SOL | UP | 0.67 | 0.79 | 0.92 |
| 11-07 21:33 | +10 stop | XRP | UP | 0.70 | 0.84 | 1.15 |
| 11-07 21:32 | +10 stop | BNB | UP | 0.61 | 0.74 | 0.94 |
| 11-07 21:32 | +10 stop | ETH | UP | 0.57 | 0.68 | 0.76 |
| 11-07 21:32 | +5 | ETH | UP | 0.57 | 0.68 | 0.76 |
| 11-07 21:32 | +10 stop | DOGE | DOWN | 0.56 | 0.36 | -2.40 |
| 11-07 21:32 | +20 | DOGE | DOWN | 0.56 | open |  |
| 11-07 21:32 | +15 | DOGE | DOWN | 0.56 | open |  |
| 11-07 21:32 | +10 | DOGE | DOWN | 0.56 | open |  |
| 11-07 21:32 | +5 | DOGE | DOWN | 0.56 | open |  |
| 11-07 21:32 | +10 stop | XRP | DOWN | 0.50 | 0.32 | -2.14 |
| 11-07 21:32 | +20 | XRP | DOWN | 0.50 | open |  |
| 11-07 21:32 | +15 | XRP | DOWN | 0.51 | open |  |
| 11-07 21:32 | +10 | XRP | DOWN | 0.51 | open |  |
| 11-07 21:32 | +5 | XRP | DOWN | 0.51 | open |  |
| 11-07 21:32 | +10 stop | NEAR | DOWN | 0.69 | 0.52 | -2.03 |
| 11-07 21:32 | +20 | NEAR | DOWN | 0.69 | open |  |
| 11-07 21:32 | +15 | NEAR | DOWN | 0.69 | open |  |
| 11-07 21:32 | +10 | NEAR | DOWN | 0.69 | open |  |
| 11-07 21:32 | +5 | NEAR | DOWN | 0.69 | open |  |
| 11-07 21:31 | +5 | BTC | DOWN | 0.69 | open |  |
| 11-07 21:31 | +5 | SOL | DOWN | 0.61 | open |  |
| 11-07 21:31 | +5 | ZEC | UP | 0.68 | 0.80 | 0.92 |
