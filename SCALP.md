# Range-Scalp Bot

*Updated Sat Oct 10 01:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9733 | 8404 | 1329 (18) | 2 | $-3256.34 | -5.3% |
| **+10¢** | 7353 | 5799 | 1554 (30) | 2 | $-3141.85 | -6.8% |
| **+15¢** | 6200 | 4561 | 1639 (43) | 2 | $-2604.28 | -6.7% |
| **+20¢** | 5514 | 3809 | 1705 (55) | 2 | $-2178.58 | -6.3% |
| **+10¢ (15¢ stop)** | 11922 | 11887 | 35 (22) | 0 | $-4583.35 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 00:59 | +10 stop | BNB | DOWN | 0.56 | 0.96 | 3.78 |
| 10-10 00:58 | +10 stop | HYPE | UP | 0.48 | 0.18 | -3.34 |
| 10-10 00:58 | +10 stop | BNB | DOWN | 0.47 | 0.60 | 0.95 |
| 10-10 00:57 | +10 stop | ETH | UP | 0.61 | 0.81 | 1.72 |
| 10-10 00:57 | +20 | ETH | UP | 0.61 | 0.81 | 1.72 |
| 10-10 00:57 | +15 | ETH | UP | 0.61 | 0.81 | 1.72 |
| 10-10 00:57 | +10 | ETH | UP | 0.61 | 0.81 | 1.72 |
| 10-10 00:57 | +5 | ETH | UP | 0.61 | 0.81 | 1.72 |
| 10-10 00:56 | +10 stop | HYPE | DOWN | 0.62 | 0.36 | -2.94 |
| 10-10 00:56 | +20 | HYPE | DOWN | 0.62 | 0.96 | 3.17 |
| 10-10 00:56 | +15 | HYPE | DOWN | 0.62 | 0.80 | 1.51 |
| 10-10 00:56 | +10 | HYPE | DOWN | 0.62 | 0.80 | 1.51 |
| 10-10 00:56 | +5 | HYPE | DOWN | 0.62 | 0.80 | 1.51 |
| 10-10 00:56 | +10 stop | BNB | UP | 0.42 | 0.24 | -2.11 |
| 10-10 00:54 | +5 | BNB | UP | 0.63 | open |  |
| 10-10 00:54 | +10 stop | DOGE | UP | 0.65 | 0.50 | -1.84 |
| 10-10 00:54 | +10 stop | BTC | UP | 0.71 | 0.52 | -2.23 |
| 10-10 00:53 | +5 | BNB | UP | 0.56 | 0.68 | 0.90 |
| 10-10 00:53 | +10 stop | XRP | DOWN | 0.45 | 0.55 | 0.64 |
| 10-10 00:51 | +10 stop | ZEC | UP | 0.68 | 0.46 | -2.54 |
| 10-10 00:51 | +10 stop | BNB | UP | 0.63 | 0.41 | -2.54 |
| 10-10 00:51 | +10 | BNB | UP | 0.63 | open |  |
| 10-10 00:51 | +5 | BNB | UP | 0.63 | 0.68 | 0.17 |
| 10-10 00:50 | +10 stop | ETH | UP | 0.68 | 0.82 | 1.13 |
| 10-10 00:50 | +10 | ETH | UP | 0.68 | 0.82 | 1.13 |
| 10-10 00:50 | +5 | ETH | UP | 0.68 | 0.74 | 0.30 |
| 10-10 00:50 | +10 stop | SOL | UP | 0.70 | 0.81 | 0.84 |
| 10-10 00:50 | +15 | SOL | UP | 0.70 | 0.86 | 1.36 |
| 10-10 00:50 | +10 | SOL | UP | 0.70 | 0.81 | 0.84 |
| 10-10 00:50 | +5 | SOL | UP | 0.70 | 0.81 | 0.84 |
| 10-10 00:50 | +10 stop | ZEC | DOWN | 0.53 | 0.32 | -2.44 |
| 10-10 00:50 | +10 stop | DOGE | UP | 0.64 | 0.76 | 0.90 |
| 10-10 00:50 | +10 stop | ZEC | UP | 0.41 | 0.59 | 1.46 |
| 10-10 00:49 | +10 stop | BTC | UP | 0.65 | 0.77 | 0.91 |
| 10-10 00:48 | +10 stop | DOGE | UP | 0.50 | 0.69 | 1.61 |
| 10-10 00:47 | +10 stop | ZEC | UP | 0.58 | 0.70 | 0.87 |
| 10-10 00:47 | +10 stop | DOGE | UP | 0.55 | 0.65 | 0.66 |
| 10-10 00:47 | +10 stop | SOL | UP | 0.64 | 0.77 | 1.00 |
| 10-10 00:47 | +20 | SOL | UP | 0.64 | 0.84 | 1.73 |
| 10-10 00:47 | +15 | SOL | UP | 0.64 | 0.80 | 1.31 |
