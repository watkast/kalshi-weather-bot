# Range-Scalp Bot

*Updated Fri Oct 09 02:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8395 | 7270 | 1125 (13) | 1 | $-2678.61 | -5.1% |
| **+10¢** | 6361 | 5032 | 1329 (25) | 2 | $-2617.62 | -6.5% |
| **+15¢** | 5368 | 3967 | 1401 (37) | 0 | $-2114.76 | -6.3% |
| **+20¢** | 4773 | 3320 | 1453 (45) | 1 | $-1731.12 | -5.8% |
| **+10¢ (15¢ stop)** | 10194 | 10164 | 30 (19) | 0 | $-3722.59 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 02:27 | +10 stop | XRP | DOWN | 0.64 | 0.84 | 1.73 |
| 10-09 02:27 | +5 | XRP | DOWN | 0.64 | 0.84 | 1.73 |
| 10-09 02:26 | +10 stop | SOL | UP | 0.47 | 0.69 | 1.87 |
| 10-09 02:26 | +10 stop | SOL | DOWN | 0.41 | 0.67 | 2.27 |
| 10-09 02:24 | +10 stop | HYPE | DOWN | 0.70 | 0.96 | 2.42 |
| 10-09 02:24 | +10 | HYPE | DOWN | 0.70 | 0.96 | 2.42 |
| 10-09 02:24 | +5 | HYPE | DOWN | 0.70 | 0.77 | 0.39 |
| 10-09 02:24 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-09 02:24 | +10 stop | BNB | DOWN | 0.54 | 0.74 | 1.68 |
| 10-09 02:24 | +10 stop | DOGE | DOWN | 0.67 | 0.80 | 1.02 |
| 10-09 02:24 | +5 | DOGE | DOWN | 0.67 | 0.80 | 1.02 |
| 10-09 02:23 | +10 stop | SOL | UP | 0.63 | 0.74 | 0.79 |
| 10-09 02:23 | +15 | SOL | UP | 0.63 | 0.83 | 1.73 |
| 10-09 02:23 | +10 stop | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 10-09 02:23 | +10 | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 10-09 02:23 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 10-09 02:23 | +10 stop | BNB | UP | 0.57 | 0.39 | -2.15 |
| 10-09 02:22 | +10 stop | BTC | DOWN | 0.67 | 0.94 | 2.52 |
| 10-09 02:22 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 10-09 02:22 | +10 stop | DOGE | DOWN | 0.55 | 0.68 | 0.96 |
| 10-09 02:21 | +10 stop | XRP | UP | 0.60 | 0.79 | 1.63 |
| 10-09 02:21 | +5 | XRP | UP | 0.60 | 0.69 | 0.60 |
| 10-09 02:21 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.90 |
| 10-09 02:21 | +5 | DOGE | DOWN | 0.62 | 0.68 | 0.27 |
| 10-09 02:21 | +10 stop | ZEC | UP | 0.57 | 0.71 | 1.06 |
| 10-09 02:21 | +15 | ZEC | UP | 0.57 | 0.85 | 2.52 |
| 10-09 02:21 | +10 | ZEC | UP | 0.57 | 0.71 | 1.07 |
| 10-09 02:21 | +5 | ZEC | UP | 0.57 | 0.71 | 1.09 |
| 10-09 02:21 | +10 stop | SOL | UP | 0.54 | 0.70 | 1.27 |
| 10-09 02:21 | +15 | SOL | UP | 0.54 | 0.70 | 1.27 |
| 10-09 02:20 | +10 stop | HYPE | UP | 0.53 | 0.66 | 0.96 |
| 10-09 02:20 | +10 stop | DOGE | UP | 0.59 | 0.42 | -2.05 |
| 10-09 02:20 | +5 | DOGE | UP | 0.59 | 0.68 | 0.57 |
| 10-09 02:20 | +10 stop | NEAR | UP | 0.56 | 0.38 | -2.15 |
| 10-09 02:20 | +10 stop | BTC | UP | 0.44 | 0.59 | 1.15 |
| 10-09 02:20 | +10 stop | ETH | UP | 0.49 | 0.25 | -2.72 |
| 10-09 02:20 | +10 stop | BNB | UP | 0.71 | 0.50 | -2.43 |
| 10-09 02:20 | +10 | BNB | UP | 0.71 | open |  |
| 10-09 02:19 | +10 stop | NEAR | DOWN | 0.63 | 0.36 | -3.02 |
| 10-09 02:19 | +20 | NEAR | DOWN | 0.63 | 0.83 | 1.73 |
