# Range-Scalp Bot

*Updated Fri Nov 27 03:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73208 | 63891 | 9317 (164) | 0 | $-19506.16 | -4.2% |
| **+10¢** | 54572 | 43694 | 10878 (210) | 2 | $-18099.52 | -5.3% |
| **+15¢** | 45700 | 33981 | 11719 (268) | 2 | $-16208.09 | -5.7% |
| **+20¢** | 40672 | 28332 | 12340 (334) | 3 | $-14603.72 | -5.7% |
| **+10¢ (15¢ stop)** | 89161 | 88949 | 212 (129) | 0 | $-32925.46 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 03:28 | +5 | ETH | DOWN | 0.48 | 0.61 | 0.95 |
| 11-27 03:28 | +10 stop | ETH | DOWN | 0.70 | 0.83 | 1.05 |
| 11-27 03:27 | +10 stop | XRP | DOWN | 0.64 | 0.94 | 2.77 |
| 11-27 03:27 | +15 | XRP | DOWN | 0.64 | 0.94 | 2.77 |
| 11-27 03:27 | +10 | XRP | DOWN | 0.63 | 0.73 | 0.70 |
| 11-27 03:27 | +5 | XRP | DOWN | 0.63 | 0.73 | 0.71 |
| 11-27 03:27 | +10 stop | ZEC | UP | 0.69 | 0.79 | 0.73 |
| 11-27 03:27 | +5 | ZEC | UP | 0.69 | 0.75 | 0.31 |
| 11-27 03:27 | +10 stop | DOGE | UP | 0.69 | 0.85 | 1.36 |
| 11-27 03:27 | +20 | DOGE | UP | 0.70 | 0.90 | 1.78 |
| 11-27 03:27 | +15 | DOGE | UP | 0.70 | 0.90 | 1.77 |
| 11-27 03:26 | +10 stop | ETH | DOWN | 0.68 | 0.50 | -2.14 |
| 11-27 03:26 | +5 | ETH | DOWN | 0.61 | 0.67 | 0.27 |
| 11-27 03:26 | +10 stop | ZEC | DOWN | 0.45 | 0.57 | 0.84 |
| 11-27 03:26 | +5 | ZEC | DOWN | 0.44 | 0.57 | 0.94 |
| 11-27 03:26 | +10 stop | SOL | DOWN | 0.55 | 0.18 | -3.99 |
| 11-27 03:26 | +5 | SOL | DOWN | 0.55 | 0.60 | 0.15 |
| 11-27 03:26 | +10 stop | ETH | DOWN | 0.56 | 0.66 | 0.66 |
| 11-27 03:26 | +5 | ETH | DOWN | 0.61 | 0.66 | 0.17 |
| 11-27 03:26 | +10 stop | BTC | DOWN | 0.55 | 0.39 | -1.95 |
| 11-27 03:25 | +10 stop | BTC | UP | 0.57 | 0.67 | 0.66 |
| 11-27 03:25 | +10 stop | SOL | UP | 0.38 | 0.56 | 1.50 |
| 11-27 03:24 | +5 | ETH | UP | 0.58 | 0.67 | 0.56 |
| 11-27 03:24 | +10 stop | XRP | DOWN | 0.63 | 0.77 | 1.10 |
| 11-27 03:24 | +10 | XRP | DOWN | 0.63 | 0.77 | 1.10 |
| 11-27 03:24 | +5 | XRP | DOWN | 0.63 | 0.77 | 1.10 |
| 11-27 03:24 | +10 stop | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 11-27 03:24 | +10 | ZEC | DOWN | 0.70 | open |  |
| 11-27 03:24 | +5 | ZEC | DOWN | 0.70 | 0.77 | 0.42 |
| 11-27 03:24 | +10 stop | DOGE | DOWN | 0.57 | 0.35 | -2.52 |
| 11-27 03:24 | +10 | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 11-27 03:24 | +5 | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 11-27 03:24 | +10 stop | SOL | DOWN | 0.59 | 0.44 | -1.85 |
| 11-27 03:23 | +5 | SOL | DOWN | 0.64 | 0.78 | 1.10 |
| 11-27 03:22 | +10 stop | XRP | DOWN | 0.60 | 0.73 | 0.99 |
| 11-27 03:22 | +10 stop | BNB | UP | 0.68 | 0.47 | -2.44 |
| 11-27 03:22 | +20 | BNB | UP | 0.68 | 0.93 | 2.25 |
| 11-27 03:22 | +15 | BNB | UP | 0.68 | 0.86 | 1.55 |
| 11-27 03:22 | +10 | BNB | UP | 0.69 | 0.86 | 1.46 |
| 11-27 03:22 | +5 | BNB | UP | 0.69 | 0.77 | 0.52 |
