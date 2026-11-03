# Range-Scalp Bot

*Updated Tue Nov 03 13:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45973 | 40028 | 5945 (69) | 0 | $-13277.42 | -4.6% |
| **+10¢** | 34323 | 27436 | 6887 (91) | 0 | $-12142.90 | -5.6% |
| **+15¢** | 28725 | 21320 | 7405 (119) | 0 | $-11096.10 | -6.2% |
| **+20¢** | 25513 | 17752 | 7761 (156) | 0 | $-9866.59 | -6.2% |
| **+10¢ (15¢ stop)** | 56077 | 55988 | 89 (53) | 0 | $-21031.89 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 12:58 | +10 stop | ETH | DOWN | 0.50 | 0.61 | 0.75 |
| 11-03 12:58 | +10 stop | BTC | UP | 0.59 | 0.75 | 1.29 |
| 11-03 12:58 | +15 | BTC | UP | 0.58 | 0.75 | 1.38 |
| 11-03 12:58 | +10 | BTC | UP | 0.58 | 0.75 | 1.38 |
| 11-03 12:58 | +5 | BTC | UP | 0.58 | 0.64 | 0.25 |
| 11-03 12:56 | +5 | DOGE | UP | 0.65 | 0.73 | 0.50 |
| 11-03 12:56 | +5 | ETH | UP | 0.62 | 0.78 | 1.30 |
| 11-03 12:55 | +10 stop | DOGE | UP | 0.57 | 0.73 | 1.28 |
| 11-03 12:55 | +15 | DOGE | UP | 0.57 | 0.73 | 1.28 |
| 11-03 12:55 | +10 | DOGE | UP | 0.57 | 0.73 | 1.28 |
| 11-03 12:55 | +5 | DOGE | UP | 0.57 | 0.65 | 0.46 |
| 11-03 12:55 | +10 stop | ETH | UP | 0.63 | 0.40 | -2.64 |
| 11-03 12:55 | +20 | ETH | UP | 0.63 | 0.84 | 1.83 |
| 11-03 12:55 | +15 | ETH | UP | 0.63 | 0.78 | 1.20 |
| 11-03 12:55 | +10 | ETH | UP | 0.63 | 0.78 | 1.20 |
| 11-03 12:55 | +5 | ETH | UP | 0.61 | 0.67 | 0.27 |
| 11-03 12:54 | +10 stop | HYPE | UP | 0.67 | 0.51 | -1.98 |
| 11-03 12:54 | +20 | HYPE | UP | 0.67 | 0.95 | 2.60 |
| 11-03 12:54 | +15 | HYPE | UP | 0.67 | 0.84 | 1.40 |
| 11-03 12:53 | +10 stop | XRP | UP | 0.53 | 0.37 | -1.95 |
| 11-03 12:51 | +10 stop | HYPE | UP | 0.62 | 0.75 | 0.95 |
| 11-03 12:51 | +10 stop | XRP | UP | 0.68 | 0.78 | 0.71 |
| 11-03 12:51 | +20 | BTC | UP | 0.70 | yes | 2.85 |
| 11-03 12:51 | +5 | BTC | UP | 0.70 | 0.78 | 0.52 |
| 11-03 12:50 | +10 stop | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 11-03 12:50 | +10 stop | HYPE | DOWN | 0.62 | 0.43 | -2.24 |
| 11-03 12:50 | +10 | HYPE | DOWN | 0.62 | yes | -6.36 |
| 11-03 12:50 | +5 | HYPE | DOWN | 0.60 | yes | -6.17 |
| 11-03 12:50 | +10 stop | BTC | UP | 0.69 | 0.81 | 0.94 |
| 11-03 12:50 | +10 stop | BNB | UP | 0.68 | 0.78 | 0.71 |
| 11-03 12:50 | +5 | XRP | DOWN | 0.61 | 0.74 | 0.99 |
| 11-03 12:50 | +10 stop | SOL | UP | 0.65 | 0.79 | 1.12 |
| 11-03 12:49 | +10 stop | ZEC | DOWN | 0.61 | 0.46 | -1.85 |
| 11-03 12:49 | +10 stop | HYPE | UP | 0.49 | 0.64 | 1.11 |
| 11-03 12:49 | +20 | HYPE | UP | 0.49 | 0.72 | 1.93 |
| 11-03 12:49 | +15 | HYPE | UP | 0.49 | 0.72 | 1.93 |
| 11-03 12:49 | +10 | HYPE | UP | 0.50 | 0.64 | 1.01 |
| 11-03 12:49 | +5 | HYPE | UP | 0.50 | 0.64 | 1.01 |
| 11-03 12:49 | +5 | ZEC | DOWN | 0.61 | yes | -6.27 |
| 11-03 12:49 | +5 | DOGE | UP | 0.56 | 0.65 | 0.56 |
