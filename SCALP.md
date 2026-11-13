# Range-Scalp Bot

*Updated Fri Nov 13 16:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58324 | 50892 | 7432 (105) | 4 | $-15709.21 | -4.3% |
| **+10¢** | 43588 | 34897 | 8691 (139) | 4 | $-14664.78 | -5.4% |
| **+15¢** | 36540 | 27184 | 9356 (174) | 4 | $-13198.27 | -5.8% |
| **+20¢** | 32552 | 22727 | 9825 (225) | 4 | $-11592.16 | -5.7% |
| **+10¢ (15¢ stop)** | 71065 | 70931 | 134 (82) | 2 | $-26148.27 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 16:56 | +10 stop | BNB | DOWN | 0.66 | open |  |
| 11-13 16:56 | +10 | BNB | DOWN | 0.66 | open |  |
| 11-13 16:56 | +5 | BNB | DOWN | 0.66 | open |  |
| 11-13 16:56 | +10 stop | BTC | DOWN | 0.54 | open |  |
| 11-13 16:56 | +20 | BTC | DOWN | 0.52 | open |  |
| 11-13 16:56 | +15 | BTC | DOWN | 0.52 | open |  |
| 11-13 16:56 | +10 | BTC | DOWN | 0.51 | open |  |
| 11-13 16:56 | +5 | BTC | DOWN | 0.51 | 0.57 | 0.24 |
| 11-13 16:56 | +10 stop | ETH | UP | 0.61 | 0.71 | 0.68 |
| 11-13 16:56 | +20 | ETH | UP | 0.61 | 0.83 | 1.93 |
| 11-13 16:56 | +15 | ETH | UP | 0.61 | 0.79 | 1.48 |
| 11-13 16:56 | +10 | ETH | UP | 0.61 | 0.76 | 1.17 |
| 11-13 16:54 | +10 stop | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-13 16:54 | +20 | BTC | DOWN | 0.59 | 0.83 | 2.13 |
| 11-13 16:54 | +15 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-13 16:54 | +10 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-13 16:54 | +5 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-13 16:53 | +10 stop | DOGE | UP | 0.70 | 0.55 | -1.83 |
| 11-13 16:52 | +10 stop | ETH | DOWN | 0.56 | 0.34 | -2.54 |
| 11-13 16:52 | +10 stop | DOGE | DOWN | 0.53 | 0.34 | -2.24 |
| 11-13 16:52 | +5 | ETH | DOWN | 0.58 | open |  |
| 11-13 16:50 | +10 stop | BNB | DOWN | 0.57 | 0.70 | 0.97 |
| 11-13 16:50 | +10 stop | NEAR | UP | 0.66 | 0.82 | 1.33 |
| 11-13 16:50 | +10 | NEAR | UP | 0.66 | 0.82 | 1.33 |
| 11-13 16:50 | +5 | NEAR | UP | 0.66 | 0.82 | 1.33 |
| 11-13 16:49 | +10 stop | SOL | UP | 0.56 | 0.68 | 0.86 |
| 11-13 16:49 | +5 | DOGE | DOWN | 0.62 | open |  |
| 11-13 16:49 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-13 16:49 | +10 | BTC | DOWN | 0.61 | 0.72 | 0.78 |
| 11-13 16:49 | +5 | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-13 16:48 | +10 stop | BNB | DOWN | 0.66 | 0.49 | -2.03 |
| 11-13 16:48 | +20 | BNB | DOWN | 0.66 | open |  |
| 11-13 16:48 | +15 | BNB | DOWN | 0.66 | open |  |
| 11-13 16:48 | +10 | BNB | DOWN | 0.66 | 0.78 | 0.92 |
| 11-13 16:48 | +5 | BNB | DOWN | 0.66 | 0.73 | 0.41 |
| 11-13 16:48 | +10 stop | SOL | DOWN | 0.63 | 0.45 | -2.15 |
| 11-13 16:48 | +20 | SOL | DOWN | 0.63 | open |  |
| 11-13 16:48 | +15 | SOL | DOWN | 0.63 | open |  |
| 11-13 16:48 | +10 | SOL | DOWN | 0.63 | open |  |
| 11-13 16:48 | +5 | SOL | DOWN | 0.63 | open |  |
