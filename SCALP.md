# Range-Scalp Bot

*Updated Fri Oct 23 04:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29746 | 25891 | 3855 (39) | 0 | $-8790.40 | -4.7% |
| **+10¢** | 22296 | 17834 | 4462 (55) | 0 | $-7917.22 | -5.6% |
| **+15¢** | 18675 | 13885 | 4790 (78) | 0 | $-7083.07 | -6.0% |
| **+20¢** | 16528 | 11508 | 5020 (101) | 0 | $-6404.24 | -6.2% |
| **+10¢ (15¢ stop)** | 36494 | 36435 | 59 (32) | 0 | $-13756.27 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 04:11 | +10 stop | HYPE | DOWN | 0.69 | 0.94 | 2.35 |
| 10-23 04:08 | +10 stop | HYPE | UP | 0.55 | 0.25 | -3.32 |
| 10-23 04:08 | +10 stop | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-23 04:08 | +10 | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-23 04:07 | +10 stop | HYPE | UP | 0.71 | 0.55 | -1.93 |
| 10-23 04:07 | +10 stop | ZEC | UP | 0.58 | 0.37 | -2.45 |
| 10-23 04:06 | +10 stop | BNB | UP | 0.70 | 0.48 | -2.53 |
| 10-23 04:06 | +10 stop | HYPE | UP | 0.63 | 0.79 | 1.27 |
| 10-23 04:05 | +10 stop | NEAR | DOWN | 0.68 | 0.52 | -1.93 |
| 10-23 04:04 | +10 stop | SOL | DOWN | 0.68 | 0.51 | -2.04 |
| 10-23 04:04 | +10 stop | ETH | DOWN | 0.66 | 0.79 | 1.02 |
| 10-23 04:04 | +15 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 10-23 04:04 | +10 | ETH | DOWN | 0.66 | 0.79 | 1.02 |
| 10-23 04:04 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
| 10-23 04:04 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 10-23 04:03 | +5 | SOL | DOWN | 0.71 | 0.79 | 0.53 |
| 10-23 04:03 | +5 | DOGE | DOWN | 0.64 | 0.78 | 1.10 |
| 10-23 04:03 | +5 | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 10-23 04:03 | +10 stop | HYPE | DOWN | 0.65 | 0.50 | -1.84 |
| 10-23 04:02 | +10 stop | NEAR | DOWN | 0.68 | 0.50 | -2.14 |
| 10-23 04:02 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-23 04:02 | +20 | XRP | DOWN | 0.71 | 0.92 | 1.89 |
| 10-23 04:02 | +15 | XRP | DOWN | 0.71 | 0.92 | 1.89 |
| 10-23 04:02 | +10 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-23 04:02 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 10-23 04:02 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 10-23 04:02 | +5 | ZEC | UP | 0.48 | 0.53 | 0.14 |
| 10-23 04:02 | +5 | ETH | DOWN | 0.59 | 0.72 | 0.98 |
| 10-23 04:02 | +5 | SOL | DOWN | 0.57 | 0.69 | 0.87 |
| 10-23 04:02 | +10 stop | ETH | DOWN | 0.57 | 0.72 | 1.17 |
| 10-23 04:02 | +20 | ETH | DOWN | 0.57 | 0.79 | 1.90 |
| 10-23 04:02 | +15 | ETH | DOWN | 0.57 | 0.72 | 1.17 |
| 10-23 04:02 | +10 | ETH | DOWN | 0.57 | 0.72 | 1.17 |
| 10-23 04:02 | +5 | ETH | DOWN | 0.57 | 0.64 | 0.35 |
| 10-23 04:02 | +10 stop | ZEC | DOWN | 0.49 | 0.30 | -2.23 |
| 10-23 04:02 | +20 | ZEC | DOWN | 0.49 | 0.71 | 1.87 |
| 10-23 04:02 | +15 | ZEC | DOWN | 0.49 | 0.71 | 1.87 |
| 10-23 04:02 | +10 | ZEC | DOWN | 0.49 | 0.62 | 0.95 |
| 10-23 04:02 | +5 | ZEC | DOWN | 0.47 | 0.57 | 0.59 |
| 10-23 04:02 | +5 | SOL | DOWN | 0.56 | 0.64 | 0.45 |
