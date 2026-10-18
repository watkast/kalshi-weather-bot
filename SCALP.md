# Range-Scalp Bot

*Updated Sun Oct 18 08:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22248 | 19369 | 2879 (29) | 3 | $-6463.32 | -4.6% |
| **+10¢** | 16747 | 13421 | 3326 (42) | 3 | $-5747.93 | -5.5% |
| **+15¢** | 14029 | 10440 | 3589 (62) | 3 | $-5247.12 | -6.0% |
| **+20¢** | 12413 | 8653 | 3760 (80) | 3 | $-4704.64 | -6.0% |
| **+10¢ (15¢ stop)** | 27371 | 27321 | 50 (29) | 0 | $-10450.36 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 07:58 | +10 stop | SOL | UP | 0.69 | 0.83 | 1.15 |
| 10-18 07:58 | +5 | SOL | UP | 0.69 | 0.83 | 1.15 |
| 10-18 07:58 | +10 stop | ZEC | DOWN | 0.49 | 0.63 | 1.05 |
| 10-18 07:58 | +10 | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 10-18 07:57 | +5 | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 10-18 07:57 | +10 stop | BNB | DOWN | 0.69 | 0.82 | 1.07 |
| 10-18 07:57 | +20 | BNB | DOWN | 0.69 | 0.91 | 2.06 |
| 10-18 07:57 | +15 | BNB | DOWN | 0.71 | 0.91 | 1.83 |
| 10-18 07:56 | +10 stop | DOGE | UP | 0.60 | 0.73 | 0.99 |
| 10-18 07:56 | +10 stop | SOL | UP | 0.58 | 0.82 | 2.11 |
| 10-18 07:56 | +5 | SOL | UP | 0.58 | 0.82 | 2.11 |
| 10-18 07:55 | +10 stop | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 10-18 07:55 | +15 | ETH | DOWN | 0.66 | 0.95 | 2.75 |
| 10-18 07:55 | +10 | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 10-18 07:55 | +5 | ETH | DOWN | 0.66 | 0.77 | 0.81 |
| 10-18 07:55 | +10 stop | SOL | DOWN | 0.43 | 0.54 | 0.74 |
| 10-18 07:55 | +5 | SOL | DOWN | 0.45 | 0.54 | 0.55 |
| 10-18 07:55 | +10 stop | ZEC | UP | 0.68 | 0.34 | -3.72 |
| 10-18 07:55 | +10 stop | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-18 07:55 | +20 | BNB | DOWN | 0.61 | 0.82 | 1.82 |
| 10-18 07:55 | +15 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-18 07:55 | +10 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-18 07:55 | +5 | BNB | DOWN | 0.61 | 0.66 | 0.17 |
| 10-18 07:54 | +10 stop | XRP | UP | 0.53 | 0.66 | 0.96 |
| 10-18 07:54 | +10 stop | DOGE | UP | 0.52 | 0.64 | 0.85 |
| 10-18 07:54 | +10 stop | ZEC | DOWN | 0.69 | 0.46 | -2.63 |
| 10-18 07:54 | +5 | ZEC | DOWN | 0.69 | open |  |
| 10-18 07:52 | +10 stop | XRP | DOWN | 0.56 | 0.32 | -2.74 |
| 10-18 07:50 | +10 stop | DOGE | UP | 0.59 | 0.41 | -2.14 |
| 10-18 07:50 | +5 | HYPE | DOWN | 0.63 | 0.69 | 0.24 |
| 10-18 07:50 | +10 stop | XRP | DOWN | 0.55 | 0.38 | -2.06 |
| 10-18 07:50 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 10-18 07:50 | +10 stop | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-18 07:49 | +10 stop | BNB | UP | 0.66 | 0.22 | -4.69 |
| 10-18 07:48 | +5 | HYPE | DOWN | 0.60 | 0.65 | 0.17 |
| 10-18 07:48 | +10 stop | DOGE | DOWN | 0.60 | 0.43 | -2.05 |
| 10-18 07:48 | +10 stop | ETH | DOWN | 0.56 | 0.66 | 0.66 |
| 10-18 07:48 | +5 | NEAR | UP | 0.61 | 0.66 | 0.17 |
| 10-18 07:47 | +5 | HYPE | DOWN | 0.58 | 0.65 | 0.36 |
| 10-18 07:47 | +5 | XRP | DOWN | 0.57 | open |  |
