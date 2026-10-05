# Range-Scalp Bot

*Updated Mon Oct 05 00:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2996 | 2571 | 425 (3) | 0 | $-1081.63 | -5.7% |
| **+10¢** | 2335 | 1856 | 479 (4) | 0 | $-916.20 | -6.2% |
| **+15¢** | 1966 | 1461 | 505 (5) | 0 | $-787.63 | -6.4% |
| **+20¢** | 1755 | 1228 | 527 (10) | 0 | $-652.99 | -5.9% |
| **+10¢ (15¢ stop)** | 3746 | 3745 | 1 (1) | 0 | $-1490.63 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 00:11 | +10 stop | ETH | DOWN | 0.50 | 0.60 | 0.65 |
| 10-05 00:11 | +20 | ETH | DOWN | 0.52 | 0.77 | 2.19 |
| 10-05 00:11 | +15 | ETH | DOWN | 0.52 | 0.67 | 1.16 |
| 10-05 00:11 | +10 | ETH | DOWN | 0.52 | 0.67 | 1.16 |
| 10-05 00:11 | +5 | ETH | DOWN | 0.51 | 0.60 | 0.55 |
| 10-05 00:07 | +5 | BTC | DOWN | 0.62 | 0.83 | 1.83 |
| 10-05 00:06 | +10 stop | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-05 00:06 | +20 | DOGE | DOWN | 0.65 | 0.85 | 1.75 |
| 10-05 00:06 | +15 | DOGE | DOWN | 0.65 | 0.82 | 1.43 |
| 10-05 00:06 | +10 | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-05 00:06 | +5 | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-05 00:06 | +10 stop | BTC | DOWN | 0.58 | 0.83 | 2.22 |
| 10-05 00:06 | +20 | BTC | DOWN | 0.58 | 0.83 | 2.22 |
| 10-05 00:06 | +15 | BTC | DOWN | 0.58 | 0.83 | 2.22 |
| 10-05 00:06 | +10 | BTC | DOWN | 0.57 | 0.83 | 2.32 |
| 10-05 00:06 | +5 | BTC | DOWN | 0.57 | 0.66 | 0.56 |
| 10-05 00:06 | +10 stop | ETH | DOWN | 0.65 | 0.82 | 1.43 |
| 10-05 00:06 | +15 | ETH | DOWN | 0.65 | 0.82 | 1.43 |
| 10-05 00:06 | +10 | ETH | DOWN | 0.65 | 0.82 | 1.43 |
| 10-05 00:06 | +5 | ETH | DOWN | 0.65 | 0.71 | 0.29 |
| 10-05 00:01 | +10 stop | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 10-05 00:01 | +20 | ETH | DOWN | 0.70 | 0.94 | 2.25 |
| 10-05 00:01 | +15 | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 10-05 00:01 | +10 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 10-05 00:01 | +5 | ETH | DOWN | 0.71 | 0.78 | 0.42 |
| 10-05 00:01 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-05 00:01 | +20 | SOL | DOWN | 0.70 | 0.90 | 1.78 |
| 10-05 00:01 | +15 | SOL | DOWN | 0.70 | 0.90 | 1.78 |
| 10-05 00:01 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-05 00:01 | +5 | SOL | DOWN | 0.70 | 0.79 | 0.63 |
| 10-04 23:58 | +10 stop | DOGE | UP | 0.67 | 0.88 | 1.86 |
| 10-04 23:57 | +10 stop | ETH | DOWN | 0.52 | 0.63 | 0.75 |
| 10-04 23:57 | +10 stop | ETH | UP | 0.50 | 0.60 | 0.65 |
| 10-04 23:57 | +10 stop | DOGE | UP | 0.52 | 0.63 | 0.75 |
| 10-04 23:56 | +20 | HYPE | UP | 0.58 | 0.86 | 2.53 |
| 10-04 23:56 | +10 stop | DOGE | DOWN | 0.57 | 0.41 | -1.95 |
| 10-04 23:55 | +10 stop | BTC | DOWN | 0.67 | 0.47 | -2.34 |
| 10-04 23:55 | +20 | BTC | DOWN | 0.67 | yes | -6.86 |
| 10-04 23:55 | +15 | BTC | DOWN | 0.67 | yes | -6.86 |
| 10-04 23:55 | +10 | BTC | DOWN | 0.67 | 0.78 | 0.81 |
