# Range-Scalp Bot

*Updated Mon Oct 19 03:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23401 | 20350 | 3051 (30) | 0 | $-6962.07 | -4.7% |
| **+10¢** | 17608 | 14092 | 3516 (44) | 1 | $-6192.90 | -5.6% |
| **+15¢** | 14760 | 10969 | 3791 (66) | 1 | $-5628.36 | -6.1% |
| **+20¢** | 13070 | 9105 | 3965 (84) | 1 | $-4986.03 | -6.1% |
| **+10¢ (15¢ stop)** | 28803 | 28752 | 51 (30) | 0 | $-10906.23 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 03:27 | +10 stop | ETH | DOWN | 0.43 | 0.57 | 1.04 |
| 10-19 03:27 | +5 | ETH | DOWN | 0.43 | 0.57 | 1.04 |
| 10-19 03:26 | +10 stop | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 10-19 03:26 | +5 | ETH | DOWN | 0.65 | 0.74 | 0.60 |
| 10-19 03:25 | +10 stop | ETH | UP | 0.45 | 0.57 | 0.84 |
| 10-19 03:25 | +10 stop | HYPE | DOWN | 0.63 | 0.79 | 1.31 |
| 10-19 03:25 | +20 | HYPE | DOWN | 0.63 | 0.87 | 2.15 |
| 10-19 03:25 | +15 | HYPE | DOWN | 0.68 | 0.87 | 1.62 |
| 10-19 03:25 | +10 | HYPE | DOWN | 0.68 | 0.79 | 0.78 |
| 10-19 03:25 | +5 | HYPE | DOWN | 0.68 | 0.79 | 0.78 |
| 10-19 03:24 | +10 stop | XRP | UP | 0.27 | 0.60 | 2.99 |
| 10-19 03:23 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
| 10-19 03:23 | +10 stop | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-19 03:23 | +20 | ZEC | DOWN | 0.67 | 0.93 | 2.39 |
| 10-19 03:23 | +15 | ZEC | DOWN | 0.67 | 0.93 | 2.39 |
| 10-19 03:23 | +10 | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-19 03:23 | +5 | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-19 03:23 | +10 stop | HYPE | DOWN | 0.62 | 0.79 | 1.41 |
| 10-19 03:23 | +20 | HYPE | DOWN | 0.62 | 0.83 | 1.83 |
| 10-19 03:23 | +15 | HYPE | DOWN | 0.62 | 0.79 | 1.41 |
| 10-19 03:23 | +10 | HYPE | DOWN | 0.62 | 0.79 | 1.41 |
| 10-19 03:23 | +5 | HYPE | DOWN | 0.62 | 0.79 | 1.41 |
| 10-19 03:23 | +10 stop | DOGE | DOWN | 0.58 | 0.73 | 1.18 |
| 10-19 03:23 | +20 | DOGE | DOWN | 0.58 | 0.78 | 1.69 |
| 10-19 03:23 | +15 | DOGE | DOWN | 0.58 | 0.73 | 1.18 |
| 10-19 03:23 | +10 | DOGE | DOWN | 0.58 | 0.73 | 1.18 |
| 10-19 03:23 | +5 | DOGE | DOWN | 0.58 | 0.73 | 1.18 |
| 10-19 03:22 | +10 stop | ETH | UP | 0.59 | 0.72 | 0.98 |
| 10-19 03:22 | +5 | XRP | DOWN | 0.63 | 0.76 | 1.00 |
| 10-19 03:20 | +10 stop | ETH | DOWN | 0.60 | 0.42 | -2.15 |
| 10-19 03:18 | +10 stop | ZEC | DOWN | 0.67 | 0.81 | 1.13 |
| 10-19 03:18 | +10 | ZEC | DOWN | 0.67 | 0.81 | 1.13 |
| 10-19 03:18 | +5 | ZEC | DOWN | 0.67 | 0.72 | 0.19 |
| 10-19 03:18 | +10 stop | ETH | DOWN | 0.68 | 0.50 | -2.14 |
| 10-19 03:18 | +20 | ETH | DOWN | 0.68 | open |  |
| 10-19 03:18 | +15 | ETH | DOWN | 0.68 | open |  |
| 10-19 03:18 | +10 | ETH | DOWN | 0.68 | open |  |
| 10-19 03:18 | +5 | ETH | DOWN | 0.68 | 0.77 | 0.61 |
| 10-19 03:17 | +10 | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 10-19 03:17 | +10 stop | BNB | DOWN | 0.70 | 0.81 | 0.84 |
