# Range-Scalp Bot

*Updated Mon Oct 19 04:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23498 | 20435 | 3063 (30) | 1 | $-6992.99 | -4.7% |
| **+10¢** | 17676 | 14146 | 3530 (44) | 1 | $-6226.13 | -5.6% |
| **+15¢** | 14819 | 11015 | 3804 (66) | 1 | $-5635.18 | -6.1% |
| **+20¢** | 13120 | 9141 | 3979 (84) | 1 | $-4993.98 | -6.1% |
| **+10¢ (15¢ stop)** | 28950 | 28899 | 51 (30) | 0 | $-10988.03 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 04:57 | +10 stop | NEAR | DOWN | 0.54 | 0.86 | 2.93 |
| 10-19 04:57 | +10 stop | DOGE | DOWN | 0.62 | 0.77 | 1.20 |
| 10-19 04:56 | +10 stop | NEAR | UP | 0.63 | 0.74 | 0.79 |
| 10-19 04:56 | +5 | DOGE | UP | 0.61 | open |  |
| 10-19 04:55 | +10 stop | SOL | DOWN | 0.59 | 0.42 | -2.05 |
| 10-19 04:55 | +10 stop | NEAR | DOWN | 0.60 | 0.41 | -2.24 |
| 10-19 04:55 | +10 stop | XRP | DOWN | 0.66 | 0.80 | 1.12 |
| 10-19 04:54 | +10 stop | DOGE | UP | 0.61 | 0.22 | -4.20 |
| 10-19 04:54 | +10 | DOGE | UP | 0.61 | open |  |
| 10-19 04:54 | +5 | DOGE | UP | 0.61 | 0.66 | 0.19 |
| 10-19 04:54 | +10 stop | SOL | DOWN | 0.56 | 0.68 | 0.86 |
| 10-19 04:53 | +10 stop | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 10-19 04:53 | +20 | DOGE | UP | 0.52 | open |  |
| 10-19 04:53 | +15 | DOGE | UP | 0.52 | open |  |
| 10-19 04:53 | +10 | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 10-19 04:53 | +5 | DOGE | UP | 0.52 | 0.61 | 0.55 |
| 10-19 04:53 | +10 stop | SOL | UP | 0.65 | 0.50 | -1.84 |
| 10-19 04:52 | +10 stop | XRP | UP | 0.67 | 0.51 | -1.94 |
| 10-19 04:51 | +10 stop | NEAR | UP | 0.50 | 0.69 | 1.57 |
| 10-19 04:51 | +10 stop | SOL | UP | 0.54 | 0.64 | 0.65 |
| 10-19 04:50 | +10 stop | NEAR | UP | 0.70 | 0.52 | -2.13 |
| 10-19 04:50 | +10 stop | ZEC | UP | 0.58 | 0.42 | -1.96 |
| 10-19 04:49 | +10 stop | SOL | UP | 0.63 | 0.78 | 1.20 |
| 10-19 04:47 | +10 stop | SOL | DOWN | 0.59 | 0.38 | -2.44 |
| 10-19 04:47 | +10 stop | NEAR | DOWN | 0.63 | 0.44 | -2.25 |
| 10-19 04:47 | +10 stop | XRP | UP | 0.61 | 0.77 | 1.30 |
| 10-19 04:46 | +10 stop | ETH | UP | 0.63 | 0.75 | 0.89 |
| 10-19 04:46 | +20 | ETH | UP | 0.63 | 0.88 | 2.25 |
| 10-19 04:46 | +15 | ETH | UP | 0.63 | 0.78 | 1.20 |
| 10-19 04:46 | +10 | ETH | UP | 0.63 | 0.75 | 0.89 |
| 10-19 04:46 | +5 | ETH | UP | 0.63 | 0.70 | 0.38 |
| 10-19 04:46 | +10 stop | BTC | UP | 0.63 | 0.73 | 0.69 |
| 10-19 04:46 | +20 | BTC | UP | 0.63 | 0.86 | 2.04 |
| 10-19 04:46 | +15 | BTC | UP | 0.63 | 0.79 | 1.31 |
| 10-19 04:46 | +10 | BTC | UP | 0.63 | 0.73 | 0.69 |
| 10-19 04:46 | +5 | BTC | UP | 0.63 | 0.73 | 0.69 |
| 10-19 04:46 | +10 stop | BNB | UP | 0.59 | 0.73 | 1.09 |
| 10-19 04:46 | +20 | BNB | UP | 0.59 | 0.85 | 2.34 |
| 10-19 04:46 | +15 | BNB | UP | 0.59 | 0.74 | 1.19 |
| 10-19 04:46 | +10 | BNB | UP | 0.59 | 0.73 | 1.09 |
