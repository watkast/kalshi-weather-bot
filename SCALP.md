# Range-Scalp Bot

*Updated Wed Nov 11 03:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55329 | 48253 | 7076 (94) | 5 | $-15112.32 | -4.3% |
| **+10¢** | 41329 | 33072 | 8257 (124) | 6 | $-14074.09 | -5.4% |
| **+15¢** | 34648 | 25747 | 8901 (158) | 6 | $-12832.93 | -5.9% |
| **+20¢** | 30852 | 21515 | 9337 (207) | 5 | $-11225.51 | -5.8% |
| **+10¢ (15¢ stop)** | 67381 | 67263 | 118 (73) | 0 | $-24845.41 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 03:26 | +10 stop | HYPE | DOWN | 0.46 | 0.59 | 0.95 |
| 11-11 03:26 | +5 | HYPE | DOWN | 0.43 | 0.59 | 1.25 |
| 11-11 03:25 | +10 stop | NEAR | UP | 0.60 | 0.77 | 1.45 |
| 11-11 03:25 | +20 | NEAR | UP | 0.60 | 0.92 | 3.04 |
| 11-11 03:25 | +15 | NEAR | UP | 0.60 | 0.77 | 1.45 |
| 11-11 03:25 | +10 | NEAR | UP | 0.60 | 0.77 | 1.45 |
| 11-11 03:25 | +5 | NEAR | UP | 0.60 | 0.77 | 1.45 |
| 11-11 03:25 | +10 stop | BTC | DOWN | 0.67 | 0.84 | 1.44 |
| 11-11 03:25 | +5 | HYPE | UP | 0.35 | 0.57 | 1.86 |
| 11-11 03:24 | +10 stop | HYPE | UP | 0.51 | 0.36 | -1.85 |
| 11-11 03:24 | +20 | HYPE | UP | 0.51 | open |  |
| 11-11 03:24 | +15 | HYPE | UP | 0.51 | open |  |
| 11-11 03:24 | +10 | HYPE | UP | 0.51 | open |  |
| 11-11 03:24 | +5 | HYPE | UP | 0.50 | 0.55 | 0.14 |
| 11-11 03:23 | +10 stop | ZEC | UP | 0.68 | 0.47 | -2.44 |
| 11-11 03:23 | +20 | ZEC | UP | 0.68 | open |  |
| 11-11 03:23 | +10 | ZEC | UP | 0.68 | open |  |
| 11-11 03:23 | +5 | ZEC | UP | 0.68 | open |  |
| 11-11 03:22 | +10 stop | BTC | UP | 0.56 | 0.30 | -2.93 |
| 11-11 03:21 | +5 | ETH | UP | 0.62 | open |  |
| 11-11 03:21 | +10 stop | HYPE | UP | 0.63 | 0.83 | 1.73 |
| 11-11 03:20 | +10 stop | XRP | DOWN | 0.59 | 0.74 | 1.19 |
| 11-11 03:20 | +20 | XRP | DOWN | 0.59 | 0.89 | 2.76 |
| 11-11 03:20 | +5 | ZEC | UP | 0.70 | 0.77 | 0.43 |
| 11-11 03:20 | +10 stop | BTC | DOWN | 0.63 | 0.48 | -1.85 |
| 11-11 03:20 | +5 | ZEC | UP | 0.60 | 0.66 | 0.27 |
| 11-11 03:19 | +10 stop | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 11-11 03:19 | +10 stop | HYPE | DOWN | 0.65 | 0.39 | -2.93 |
| 11-11 03:19 | +10 stop | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-11 03:19 | +20 | DOGE | DOWN | 0.69 | 0.93 | 2.18 |
| 11-11 03:19 | +15 | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-11 03:19 | +10 | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-11 03:19 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 11-11 03:19 | +5 | ETH | UP | 0.59 | 0.66 | 0.37 |
| 11-11 03:19 | +10 stop | ETH | UP | 0.62 | 0.32 | -3.33 |
| 11-11 03:19 | +10 | ETH | UP | 0.62 | open |  |
| 11-11 03:19 | +5 | ETH | UP | 0.62 | 0.68 | 0.27 |
| 11-11 03:19 | +10 stop | HYPE | UP | 0.59 | 0.42 | -2.05 |
| 11-11 03:19 | +15 | HYPE | UP | 0.59 | 0.83 | 2.13 |
| 11-11 03:19 | +10 | HYPE | UP | 0.58 | 0.83 | 2.22 |
