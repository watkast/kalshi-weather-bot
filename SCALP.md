# Range-Scalp Bot

*Updated Mon Oct 05 07:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3508 | 3009 | 499 (3) | 0 | $-1292.04 | -5.8% |
| **+10¢** | 2707 | 2136 | 571 (4) | 1 | $-1176.98 | -6.9% |
| **+15¢** | 2275 | 1671 | 604 (6) | 1 | $-1064.22 | -7.5% |
| **+20¢** | 2029 | 1398 | 631 (11) | 1 | $-940.33 | -7.4% |
| **+10¢ (15¢ stop)** | 4349 | 4348 | 1 (1) | 0 | $-1714.33 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 07:41 | +5 | BTC | UP | 0.62 | 0.69 | 0.38 |
| 10-05 07:39 | +10 stop | BTC | UP | 0.70 | 0.87 | 1.47 |
| 10-05 07:39 | +10 stop | XRP | DOWN | 0.55 | 0.40 | -1.85 |
| 10-05 07:39 | +10 stop | SOL | DOWN | 0.47 | 0.27 | -2.32 |
| 10-05 07:38 | +10 stop | ETH | DOWN | 0.50 | 0.29 | -2.43 |
| 10-05 07:38 | +10 stop | BTC | UP | 0.55 | 0.36 | -2.25 |
| 10-05 07:36 | +10 stop | BTC | DOWN | 0.65 | 0.47 | -2.14 |
| 10-05 07:35 | +10 stop | XRP | DOWN | 0.52 | 0.66 | 1.06 |
| 10-05 07:35 | +10 stop | ETH | DOWN | 0.59 | 0.43 | -1.95 |
| 10-05 07:35 | +5 | HYPE | UP | 0.63 | 0.68 | 0.17 |
| 10-05 07:35 | +10 stop | BTC | UP | 0.50 | 0.31 | -2.23 |
| 10-05 07:34 | +10 stop | SOL | UP | 0.64 | 0.49 | -1.85 |
| 10-05 07:34 | +5 | SOL | UP | 0.64 | 0.72 | 0.48 |
| 10-05 07:34 | +10 stop | HYPE | UP | 0.58 | 0.68 | 0.66 |
| 10-05 07:34 | +10 | HYPE | UP | 0.59 | 0.74 | 1.19 |
| 10-05 07:34 | +5 | HYPE | UP | 0.59 | 0.64 | 0.16 |
| 10-05 07:33 | +10 stop | ETH | UP | 0.69 | 0.45 | -2.73 |
| 10-05 07:33 | +15 | ETH | UP | 0.69 | 0.90 | 1.91 |
| 10-05 07:33 | +10 | ETH | UP | 0.69 | 0.82 | 1.04 |
| 10-05 07:33 | +10 stop | NEAR | DOWN | 0.71 | 0.81 | 0.75 |
| 10-05 07:33 | +20 | NEAR | DOWN | 0.71 | 0.91 | 1.83 |
| 10-05 07:33 | +15 | NEAR | DOWN | 0.71 | 0.89 | 1.59 |
| 10-05 07:33 | +10 | NEAR | DOWN | 0.71 | 0.81 | 0.75 |
| 10-05 07:33 | +5 | NEAR | DOWN | 0.71 | 0.79 | 0.54 |
| 10-05 07:33 | +10 stop | BNB | DOWN | 0.59 | 0.78 | 1.60 |
| 10-05 07:33 | +20 | BNB | DOWN | 0.59 | 0.81 | 1.92 |
| 10-05 07:33 | +15 | BNB | DOWN | 0.59 | 0.78 | 1.60 |
| 10-05 07:33 | +10 | BNB | DOWN | 0.59 | 0.78 | 1.60 |
| 10-05 07:33 | +5 | BNB | DOWN | 0.59 | 0.78 | 1.60 |
| 10-05 07:33 | +5 | BTC | UP | 0.65 | 0.73 | 0.50 |
| 10-05 07:32 | +10 stop | XRP | UP | 0.65 | 0.49 | -1.94 |
| 10-05 07:32 | +20 | XRP | UP | 0.65 | 0.90 | 2.28 |
| 10-05 07:32 | +15 | XRP | UP | 0.65 | 0.80 | 1.22 |
| 10-05 07:32 | +10 | XRP | UP | 0.65 | 0.80 | 1.22 |
| 10-05 07:32 | +5 | XRP | UP | 0.65 | 0.73 | 0.50 |
| 10-05 07:32 | +5 | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 10-05 07:32 | +5 | ETH | UP | 0.68 | 0.73 | 0.20 |
| 10-05 07:31 | +10 stop | DOGE | UP | 0.56 | 0.73 | 1.38 |
| 10-05 07:31 | +20 | DOGE | UP | 0.56 | 0.80 | 2.10 |
| 10-05 07:31 | +15 | DOGE | UP | 0.56 | 0.73 | 1.38 |
