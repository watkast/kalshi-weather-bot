# Range-Scalp Bot

*Updated Mon Oct 05 00:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2990 | 2565 | 425 (3) | 1 | $-1086.40 | -5.7% |
| **+10¢** | 2329 | 1850 | 479 (4) | 2 | $-924.01 | -6.3% |
| **+15¢** | 1960 | 1455 | 505 (5) | 2 | $-797.01 | -6.5% |
| **+20¢** | 1750 | 1223 | 527 (10) | 2 | $-663.18 | -6.0% |
| **+10¢ (15¢ stop)** | 3740 | 3739 | 1 (1) | 2 | $-1497.93 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 00:01 | +10 stop | ETH | DOWN | 0.70 | open |  |
| 10-05 00:01 | +20 | ETH | DOWN | 0.70 | open |  |
| 10-05 00:01 | +15 | ETH | DOWN | 0.70 | open |  |
| 10-05 00:01 | +10 | ETH | DOWN | 0.71 | open |  |
| 10-05 00:01 | +5 | ETH | DOWN | 0.71 | 0.78 | 0.42 |
| 10-05 00:01 | +10 stop | SOL | DOWN | 0.70 | open |  |
| 10-05 00:01 | +20 | SOL | DOWN | 0.70 | open |  |
| 10-05 00:01 | +15 | SOL | DOWN | 0.70 | open |  |
| 10-05 00:01 | +10 | SOL | DOWN | 0.70 | open |  |
| 10-05 00:01 | +5 | SOL | DOWN | 0.70 | open |  |
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
| 10-04 23:55 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 10-04 23:55 | +10 stop | ETH | DOWN | 0.66 | 0.49 | -2.04 |
| 10-04 23:55 | +20 | ETH | DOWN | 0.66 | no | 3.24 |
| 10-04 23:55 | +15 | ETH | DOWN | 0.66 | 0.84 | 1.54 |
| 10-04 23:55 | +10 | ETH | DOWN | 0.66 | 0.84 | 1.54 |
| 10-04 23:55 | +5 | ETH | DOWN | 0.66 | 0.84 | 1.54 |
| 10-04 23:55 | +10 stop | SOL | DOWN | 0.70 | 0.92 | 1.99 |
| 10-04 23:55 | +20 | SOL | DOWN | 0.70 | 0.92 | 1.99 |
| 10-04 23:55 | +15 | SOL | DOWN | 0.70 | 0.92 | 1.99 |
| 10-04 23:55 | +10 | SOL | DOWN | 0.70 | 0.92 | 1.99 |
| 10-04 23:55 | +5 | SOL | DOWN | 0.70 | 0.79 | 0.63 |
| 10-04 23:55 | +10 stop | HYPE | UP | 0.64 | 0.48 | -1.95 |
| 10-04 23:55 | +10 stop | DOGE | UP | 0.60 | 0.43 | -2.05 |
| 10-04 23:55 | +5 | HYPE | UP | 0.71 | 0.86 | 1.26 |
| 10-04 23:54 | +5 | ZEC | DOWN | 0.70 | 1.00 | 2.77 |
| 10-04 23:54 | +10 stop | BNB | UP | 0.61 | 0.71 | 0.68 |
| 10-04 23:54 | +10 stop | DOGE | DOWN | 0.57 | 0.40 | -2.05 |
| 10-04 23:53 | +10 | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 10-04 23:53 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 10-04 23:53 | +10 stop | HYPE | DOWN | 0.63 | 0.40 | -2.64 |
