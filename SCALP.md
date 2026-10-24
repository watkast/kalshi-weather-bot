# Range-Scalp Bot

*Updated Sat Oct 24 14:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32093 | 27979 | 4114 (40) | 1 | $-9185.53 | -4.5% |
| **+10¢** | 24020 | 19261 | 4759 (58) | 1 | $-8203.82 | -5.4% |
| **+15¢** | 20108 | 14989 | 5119 (81) | 1 | $-7354.38 | -5.8% |
| **+20¢** | 17815 | 12456 | 5359 (103) | 1 | $-6530.91 | -5.8% |
| **+10¢ (15¢ stop)** | 39436 | 39377 | 59 (32) | 0 | $-15098.87 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 13:59 | +10 stop | XRP | UP | 0.67 | 0.13 | -5.64 |
| 10-24 13:58 | +10 stop | BTC | UP | 0.65 | 0.21 | -4.68 |
| 10-24 13:57 | +10 stop | DOGE | UP | 0.38 | 0.55 | 1.35 |
| 10-24 13:56 | +10 stop | SOL | DOWN | 0.58 | 0.78 | 1.69 |
| 10-24 13:56 | +10 stop | BTC | DOWN | 0.59 | 0.37 | -2.54 |
| 10-24 13:54 | +10 stop | BNB | DOWN | 0.63 | 0.79 | 1.31 |
| 10-24 13:54 | +10 stop | DOGE | UP | 0.65 | 0.76 | 0.81 |
| 10-24 13:53 | +10 stop | BTC | UP | 0.62 | 0.47 | -1.85 |
| 10-24 13:52 | +5 | ZEC | DOWN | 0.66 | 0.75 | 0.60 |
| 10-24 13:52 | +10 stop | SOL | UP | 0.50 | 0.65 | 1.16 |
| 10-24 13:51 | +10 stop | ZEC | DOWN | 0.57 | 0.75 | 1.51 |
| 10-24 13:51 | +10 | ZEC | DOWN | 0.57 | 0.75 | 1.51 |
| 10-24 13:51 | +5 | ZEC | DOWN | 0.57 | 0.64 | 0.38 |
| 10-24 13:51 | +10 stop | DOGE | UP | 0.64 | 0.77 | 1.00 |
| 10-24 13:50 | +10 stop | XRP | DOWN | 0.55 | 0.36 | -2.25 |
| 10-24 13:50 | +10 stop | SOL | DOWN | 0.60 | 0.44 | -1.95 |
| 10-24 13:50 | +10 stop | ETH | UP | 0.63 | 0.76 | 1.00 |
| 10-24 13:49 | +10 stop | HYPE | UP | 0.63 | 0.73 | 0.73 |
| 10-24 13:48 | +10 stop | BNB | DOWN | 0.67 | 0.50 | -2.04 |
| 10-24 13:48 | +10 | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 10-24 13:48 | +5 | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 10-24 13:48 | +10 stop | BTC | DOWN | 0.68 | 0.50 | -2.14 |
| 10-24 13:48 | +20 | BTC | DOWN | 0.68 | 0.98 | 2.81 |
| 10-24 13:48 | +15 | BTC | DOWN | 0.68 | 0.98 | 2.81 |
| 10-24 13:48 | +10 | BTC | DOWN | 0.68 | 0.98 | 2.81 |
| 10-24 13:48 | +5 | BTC | DOWN | 0.68 | 0.77 | 0.61 |
| 10-24 13:47 | +10 stop | XRP | DOWN | 0.65 | 0.45 | -2.34 |
| 10-24 13:47 | +10 | XRP | DOWN | 0.66 | 0.80 | 1.12 |
| 10-24 13:47 | +5 | XRP | DOWN | 0.66 | 0.80 | 1.12 |
| 10-24 13:47 | +10 stop | SOL | DOWN | 0.70 | 0.53 | -2.03 |
| 10-24 13:47 | +20 | SOL | DOWN | 0.70 | 0.96 | 2.45 |
| 10-24 13:47 | +15 | SOL | DOWN | 0.70 | 0.86 | 1.36 |
| 10-24 13:47 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 10-24 13:47 | +5 | SOL | DOWN | 0.70 | 0.78 | 0.52 |
| 10-24 13:47 | +10 stop | DOGE | DOWN | 0.63 | 0.46 | -2.05 |
| 10-24 13:47 | +20 | DOGE | DOWN | 0.63 | 0.83 | 1.73 |
| 10-24 13:47 | +15 | DOGE | DOWN | 0.63 | 0.83 | 1.73 |
| 10-24 13:47 | +10 | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 10-24 13:47 | +5 | DOGE | DOWN | 0.63 | 0.70 | 0.38 |
| 10-24 13:47 | +10 stop | ETH | DOWN | 0.56 | 0.35 | -2.44 |
