# Range-Scalp Bot

*Updated Mon Oct 05 05:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3335 | 2861 | 474 (3) | 3 | $-1218.75 | -5.8% |
| **+10¢** | 2581 | 2043 | 538 (4) | 4 | $-1072.51 | -6.6% |
| **+15¢** | 2172 | 1602 | 570 (5) | 5 | $-971.72 | -7.1% |
| **+20¢** | 1937 | 1342 | 595 (10) | 5 | $-840.38 | -6.9% |
| **+10¢ (15¢ stop)** | 4153 | 4152 | 1 (1) | 0 | $-1608.45 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 05:12 | +10 stop | HYPE | UP | 0.59 | 0.79 | 1.71 |
| 10-05 05:12 | +10 stop | BTC | UP | 0.65 | 0.75 | 0.70 |
| 10-05 05:12 | +10 | BNB | DOWN | 0.50 | 0.63 | 0.95 |
| 10-05 05:12 | +5 | BNB | DOWN | 0.50 | 0.63 | 0.95 |
| 10-05 05:12 | +10 stop | HYPE | DOWN | 0.45 | 0.59 | 1.05 |
| 10-05 05:11 | +10 stop | BNB | DOWN | 0.62 | 0.35 | -3.03 |
| 10-05 05:10 | +10 stop | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 10-05 05:09 | +10 stop | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 10-05 05:09 | +5 | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 10-05 05:09 | +5 | ETH | DOWN | 0.65 | 0.71 | 0.29 |
| 10-05 05:09 | +10 stop | BTC | UP | 0.61 | 0.46 | -1.85 |
| 10-05 05:09 | +10 stop | ETH | DOWN | 0.61 | 0.71 | 0.68 |
| 10-05 05:09 | +10 | ETH | DOWN | 0.61 | 0.71 | 0.68 |
| 10-05 05:09 | +5 | ETH | DOWN | 0.61 | 0.68 | 0.37 |
| 10-05 05:08 | +10 stop | XRP | DOWN | 0.58 | 0.43 | -1.86 |
| 10-05 05:08 | +10 stop | HYPE | UP | 0.64 | 0.49 | -1.85 |
| 10-05 05:08 | +10 stop | BNB | UP | 0.65 | 0.49 | -1.94 |
| 10-05 05:06 | +10 stop | HYPE | UP | 0.62 | 0.74 | 0.89 |
| 10-05 05:06 | +10 stop | BTC | UP | 0.62 | 0.47 | -1.85 |
| 10-05 05:06 | +10 stop | ZEC | UP | 0.66 | 0.78 | 0.91 |
| 10-05 05:06 | +5 | ZEC | UP | 0.66 | 0.73 | 0.40 |
| 10-05 05:06 | +10 stop | SOL | UP | 0.58 | 0.42 | -1.96 |
| 10-05 05:06 | +10 stop | XRP | UP | 0.58 | 0.36 | -2.55 |
| 10-05 05:05 | +10 stop | ETH | DOWN | 0.55 | 0.74 | 1.58 |
| 10-05 05:05 | +10 | ETH | DOWN | 0.55 | 0.74 | 1.58 |
| 10-05 05:05 | +5 | ETH | DOWN | 0.55 | 0.61 | 0.24 |
| 10-05 05:05 | +5 | HYPE | DOWN | 0.65 | open |  |
| 10-05 05:04 | +10 stop | SOL | DOWN | 0.71 | 0.50 | -2.43 |
| 10-05 05:04 | +15 | SOL | DOWN | 0.71 | 0.88 | 1.47 |
| 10-05 05:04 | +10 | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 10-05 05:04 | +5 | SOL | DOWN | 0.71 | 0.76 | 0.22 |
| 10-05 05:04 | +10 stop | DOGE | UP | 0.46 | 0.57 | 0.74 |
| 10-05 05:04 | +10 stop | BNB | UP | 0.65 | 0.77 | 0.91 |
| 10-05 05:04 | +10 stop | XRP | DOWN | 0.70 | 0.54 | -1.93 |
| 10-05 05:04 | +10 | XRP | DOWN | 0.70 | 0.83 | 1.05 |
| 10-05 05:04 | +5 | XRP | DOWN | 0.70 | 0.83 | 1.05 |
| 10-05 05:04 | +10 stop | BTC | DOWN | 0.60 | 0.45 | -1.85 |
| 10-05 05:04 | +10 | BTC | DOWN | 0.60 | open |  |
| 10-05 05:04 | +5 | BTC | DOWN | 0.60 | open |  |
| 10-05 05:03 | +10 stop | ZEC | DOWN | 0.68 | 0.53 | -1.84 |
