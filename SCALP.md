# Range-Scalp Bot

*Updated Mon Oct 12 11:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13525 | 11704 | 1821 (25) | 0 | $-4292.68 | -5.0% |
| **+10¢** | 10243 | 8133 | 2110 (37) | 0 | $-3984.95 | -6.2% |
| **+15¢** | 8616 | 6361 | 2255 (55) | 0 | $-3495.90 | -6.5% |
| **+20¢** | 7670 | 5316 | 2354 (70) | 0 | $-2980.51 | -6.2% |
| **+10¢ (15¢ stop)** | 16635 | 16594 | 41 (25) | 0 | $-6494.68 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 11:36 | +10 stop | BTC | UP | 0.49 | 0.32 | -2.04 |
| 10-12 11:36 | +10 stop | ZEC | DOWN | 0.63 | 0.77 | 1.10 |
| 10-12 11:36 | +20 | ZEC | DOWN | 0.63 | 0.86 | 2.01 |
| 10-12 11:36 | +15 | ZEC | DOWN | 0.63 | 0.81 | 1.49 |
| 10-12 11:36 | +10 | ZEC | DOWN | 0.63 | 0.77 | 1.07 |
| 10-12 11:36 | +5 | ZEC | DOWN | 0.63 | 0.77 | 1.07 |
| 10-12 11:34 | +10 stop | BTC | DOWN | 0.59 | 0.44 | -1.85 |
| 10-12 11:33 | +10 stop | ETH | DOWN | 0.57 | 0.67 | 0.66 |
| 10-12 11:32 | +5 | DOGE | DOWN | 0.69 | 0.82 | 1.04 |
| 10-12 11:31 | +10 stop | ETH | DOWN | 0.63 | 0.44 | -2.25 |
| 10-12 11:31 | +20 | ETH | DOWN | 0.63 | 0.91 | 2.51 |
| 10-12 11:31 | +15 | ETH | DOWN | 0.63 | 0.80 | 1.41 |
| 10-12 11:31 | +10 | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-12 11:31 | +5 | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-12 11:31 | +10 stop | BTC | DOWN | 0.66 | 0.48 | -2.14 |
| 10-12 11:31 | +20 | BTC | DOWN | 0.66 | 0.89 | 2.07 |
| 10-12 11:31 | +15 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-12 11:31 | +10 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-12 11:31 | +5 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-12 11:31 | +10 stop | SOL | DOWN | 0.71 | 0.53 | -2.13 |
| 10-12 11:31 | +20 | SOL | DOWN | 0.71 | 0.93 | 2.01 |
| 10-12 11:31 | +15 | SOL | DOWN | 0.71 | 0.87 | 1.37 |
| 10-12 11:31 | +10 | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 10-12 11:31 | +5 | SOL | DOWN | 0.71 | 0.80 | 0.63 |
| 10-12 11:31 | +10 stop | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 10-12 11:31 | +20 | DOGE | DOWN | 0.67 | 0.87 | 1.76 |
| 10-12 11:31 | +15 | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 10-12 11:31 | +10 | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 10-12 11:31 | +5 | DOGE | DOWN | 0.68 | 0.74 | 0.26 |
| 10-12 11:31 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.71 |
| 10-12 11:31 | +20 | XRP | DOWN | 0.64 | 0.85 | 1.86 |
| 10-12 11:31 | +15 | XRP | DOWN | 0.64 | 0.82 | 1.54 |
| 10-12 11:31 | +10 | XRP | DOWN | 0.64 | 0.74 | 0.71 |
| 10-12 11:31 | +5 | XRP | DOWN | 0.64 | 0.74 | 0.71 |
| 10-12 11:31 | +10 stop | ZEC | DOWN | 0.68 | 0.87 | 1.66 |
| 10-12 11:31 | +20 | ZEC | DOWN | 0.68 | 0.92 | 2.18 |
| 10-12 11:31 | +15 | ZEC | DOWN | 0.68 | 0.87 | 1.66 |
| 10-12 11:31 | +10 | ZEC | DOWN | 0.68 | 0.87 | 1.66 |
| 10-12 11:31 | +5 | ZEC | DOWN | 0.68 | 0.75 | 0.40 |
| 10-12 11:31 | +10 stop | BNB | DOWN | 0.69 | 0.81 | 0.89 |
