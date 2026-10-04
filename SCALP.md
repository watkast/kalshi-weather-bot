# Range-Scalp Bot

*Updated Sun Oct 04 22:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2859 | 2453 | 406 (3) | 0 | $-1025.49 | -5.7% |
| **+10¢** | 2239 | 1784 | 455 (4) | 0 | $-840.84 | -5.9% |
| **+15¢** | 1885 | 1403 | 482 (5) | 0 | $-728.33 | -6.1% |
| **+20¢** | 1679 | 1174 | 505 (9) | 0 | $-634.45 | -6.0% |
| **+10¢ (15¢ stop)** | 3566 | 3565 | 1 (1) | 0 | $-1401.57 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 21:56 | +10 stop | XRP | DOWN | 0.71 | 0.93 | 1.98 |
| 10-04 21:56 | +20 | XRP | DOWN | 0.71 | 0.93 | 1.98 |
| 10-04 21:56 | +15 | XRP | DOWN | 0.71 | 0.93 | 1.98 |
| 10-04 21:56 | +10 | XRP | DOWN | 0.71 | 0.93 | 1.98 |
| 10-04 21:56 | +5 | XRP | DOWN | 0.71 | 0.93 | 1.98 |
| 10-04 21:56 | +10 stop | HYPE | DOWN | 0.70 | 0.83 | 1.05 |
| 10-04 21:55 | +10 stop | HYPE | DOWN | 0.52 | 0.62 | 0.65 |
| 10-04 21:55 | +10 stop | NEAR | DOWN | 0.67 | 0.85 | 1.55 |
| 10-04 21:54 | +10 stop | HYPE | UP | 0.55 | 0.31 | -2.73 |
| 10-04 21:54 | +20 | HYPE | UP | 0.55 | no | -5.68 |
| 10-04 21:54 | +15 | HYPE | UP | 0.55 | no | -5.68 |
| 10-04 21:54 | +10 | HYPE | UP | 0.55 | no | -5.68 |
| 10-04 21:54 | +5 | HYPE | UP | 0.55 | no | -5.68 |
| 10-04 21:54 | +10 stop | DOGE | UP | 0.33 | 0.58 | 2.16 |
| 10-04 21:54 | +15 | DOGE | UP | 0.33 | 0.58 | 2.16 |
| 10-04 21:54 | +10 | DOGE | UP | 0.33 | 0.58 | 2.16 |
| 10-04 21:54 | +10 stop | NEAR | UP | 0.51 | 0.36 | -1.85 |
| 10-04 21:54 | +5 | DOGE | UP | 0.49 | 0.58 | 0.54 |
| 10-04 21:54 | +10 stop | SOL | DOWN | 0.64 | 0.79 | 1.22 |
| 10-04 21:54 | +15 | SOL | DOWN | 0.64 | 0.79 | 1.22 |
| 10-04 21:54 | +10 | SOL | DOWN | 0.64 | 0.79 | 1.22 |
| 10-04 21:54 | +5 | SOL | DOWN | 0.63 | 0.79 | 1.32 |
| 10-04 21:54 | +10 stop | BNB | UP | 0.59 | 0.14 | -4.81 |
| 10-04 21:54 | +20 | BNB | UP | 0.59 | no | -6.12 |
| 10-04 21:54 | +15 | BNB | UP | 0.59 | no | -6.12 |
| 10-04 21:54 | +10 | BNB | UP | 0.59 | no | -6.12 |
| 10-04 21:54 | +5 | BNB | UP | 0.59 | no | -6.12 |
| 10-04 21:53 | +10 stop | DOGE | UP | 0.48 | 0.65 | 1.36 |
| 10-04 21:53 | +20 | DOGE | UP | 0.48 | no | -4.98 |
| 10-04 21:53 | +15 | DOGE | UP | 0.48 | 0.65 | 1.31 |
| 10-04 21:53 | +10 | DOGE | UP | 0.49 | 0.65 | 1.26 |
| 10-04 21:53 | +5 | DOGE | UP | 0.49 | 0.54 | 0.14 |
| 10-04 21:51 | +10 stop | BTC | DOWN | 0.60 | 0.73 | 0.99 |
| 10-04 21:51 | +10 stop | NEAR | UP | 0.58 | 0.30 | -3.13 |
| 10-04 21:50 | +5 | SOL | UP | 0.67 | 0.73 | 0.30 |
| 10-04 21:50 | +10 stop | ETH | DOWN | 0.48 | 0.65 | 1.36 |
| 10-04 21:49 | +10 stop | XRP | DOWN | 0.59 | 0.44 | -1.85 |
| 10-04 21:49 | +10 stop | BTC | DOWN | 0.68 | 0.53 | -1.84 |
| 10-04 21:49 | +10 stop | NEAR | DOWN | 0.68 | 0.43 | -2.84 |
| 10-04 21:48 | +5 | SOL | UP | 0.64 | 0.72 | 0.48 |
