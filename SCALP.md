# Range-Scalp Bot

*Updated Sat Nov 07 11:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50948 | 44415 | 6533 (76) | 3 | $-14274.45 | -4.5% |
| **+10¢** | 38036 | 30423 | 7613 (102) | 3 | $-13238.28 | -5.5% |
| **+15¢** | 31836 | 23633 | 8203 (131) | 5 | $-12161.10 | -6.1% |
| **+20¢** | 28308 | 19710 | 8598 (173) | 6 | $-10743.96 | -6.1% |
| **+10¢ (15¢ stop)** | 62056 | 61957 | 99 (58) | 0 | $-22919.58 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 11:43 | +10 stop | BNB | DOWN | 0.65 | 0.94 | 2.64 |
| 11-07 11:43 | +15 | BNB | DOWN | 0.65 | 0.94 | 2.64 |
| 11-07 11:43 | +10 | BNB | DOWN | 0.65 | 0.94 | 2.64 |
| 11-07 11:43 | +5 | BNB | DOWN | 0.65 | 0.94 | 2.64 |
| 11-07 11:40 | +10 stop | BNB | UP | 0.66 | 0.34 | -3.52 |
| 11-07 11:40 | +5 | BNB | UP | 0.66 | 0.75 | 0.60 |
| 11-07 11:40 | +10 stop | ZEC | UP | 0.69 | 0.82 | 1.04 |
| 11-07 11:40 | +10 | ZEC | UP | 0.69 | 0.82 | 1.04 |
| 11-07 11:40 | +5 | ZEC | UP | 0.69 | 0.82 | 1.04 |
| 11-07 11:39 | +10 stop | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 11-07 11:39 | +10 stop | ZEC | UP | 0.58 | 0.69 | 0.78 |
| 11-07 11:39 | +10 | ZEC | UP | 0.58 | 0.69 | 0.78 |
| 11-07 11:39 | +5 | ZEC | UP | 0.58 | 0.63 | 0.16 |
| 11-07 11:38 | +10 stop | BNB | DOWN | 0.50 | 0.67 | 1.36 |
| 11-07 11:38 | +5 | BNB | DOWN | 0.50 | 0.67 | 1.36 |
| 11-07 11:38 | +10 stop | HYPE | DOWN | 0.61 | 0.28 | -3.62 |
| 11-07 11:37 | +10 stop | XRP | UP | 0.26 | 0.56 | 2.68 |
| 11-07 11:37 | +10 stop | HYPE | DOWN | 0.57 | 0.68 | 0.76 |
| 11-07 11:36 | +10 stop | NEAR | UP | 0.67 | 0.79 | 0.92 |
| 11-07 11:35 | +10 stop | BNB | DOWN | 0.62 | 0.73 | 0.79 |
| 11-07 11:35 | +10 stop | XRP | UP | 0.67 | 0.51 | -1.89 |
| 11-07 11:35 | +20 | XRP | UP | 0.66 | open |  |
| 11-07 11:35 | +15 | XRP | UP | 0.66 | open |  |
| 11-07 11:35 | +10 | XRP | UP | 0.66 | open |  |
| 11-07 11:35 | +5 | XRP | UP | 0.66 | open |  |
| 11-07 11:35 | +5 | BNB | DOWN | 0.59 | 0.64 | 0.16 |
| 11-07 11:34 | +10 stop | HYPE | DOWN | 0.54 | 0.65 | 0.76 |
| 11-07 11:34 | +10 stop | ETH | UP | 0.66 | 0.82 | 1.33 |
| 11-07 11:34 | +10 | ETH | UP | 0.66 | 0.82 | 1.33 |
| 11-07 11:34 | +5 | ETH | UP | 0.66 | 0.82 | 1.33 |
| 11-07 11:34 | +5 | XRP | UP | 0.69 | 0.76 | 0.42 |
| 11-07 11:34 | +5 | BNB | UP | 0.49 | 0.62 | 0.95 |
| 11-07 11:34 | +10 stop | ETH | UP | 0.50 | 0.62 | 0.85 |
| 11-07 11:34 | +10 | ETH | UP | 0.50 | 0.62 | 0.85 |
| 11-07 11:34 | +5 | ETH | UP | 0.50 | 0.62 | 0.85 |
| 11-07 11:33 | +10 stop | ETH | DOWN | 0.41 | 0.54 | 0.95 |
| 11-07 11:33 | +10 | ETH | DOWN | 0.41 | 0.54 | 0.95 |
| 11-07 11:33 | +5 | ETH | DOWN | 0.41 | 0.54 | 0.95 |
| 11-07 11:32 | +10 stop | NEAR | DOWN | 0.60 | 0.24 | -3.90 |
| 11-07 11:32 | +20 | NEAR | DOWN | 0.60 | open |  |
