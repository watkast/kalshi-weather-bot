# Range-Scalp Bot

*Updated Thu Oct 08 22:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8096 | 7009 | 1087 (13) | 0 | $-2597.20 | -5.1% |
| **+10¢** | 6129 | 4842 | 1287 (25) | 0 | $-2563.29 | -6.6% |
| **+15¢** | 5161 | 3808 | 1353 (37) | 0 | $-2068.09 | -6.4% |
| **+20¢** | 4607 | 3204 | 1403 (45) | 0 | $-1646.18 | -5.7% |
| **+10¢ (15¢ stop)** | 9825 | 9795 | 30 (19) | 0 | $-3612.45 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 22:28 | +10 stop | BTC | DOWN | 0.60 | 0.82 | 1.92 |
| 10-08 22:27 | +10 stop | XRP | DOWN | 0.51 | 0.64 | 0.95 |
| 10-08 22:26 | +10 stop | BTC | DOWN | 0.68 | 0.53 | -1.84 |
| 10-08 22:26 | +5 | BTC | DOWN | 0.67 | 0.82 | 1.23 |
| 10-08 22:26 | +10 stop | XRP | DOWN | 0.47 | 0.58 | 0.74 |
| 10-08 22:25 | +10 stop | XRP | UP | 0.57 | 0.41 | -1.95 |
| 10-08 22:22 | +10 stop | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 10-08 22:22 | +10 stop | BNB | UP | 0.70 | 0.86 | 1.31 |
| 10-08 22:22 | +10 | BNB | UP | 0.70 | 0.86 | 1.31 |
| 10-08 22:22 | +10 stop | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-08 22:22 | +10 | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-08 22:22 | +5 | DOGE | DOWN | 0.71 | 0.77 | 0.32 |
| 10-08 22:22 | +5 | XRP | UP | 0.66 | no | -6.76 |
| 10-08 22:22 | +10 stop | DOGE | DOWN | 0.70 | 0.82 | 0.94 |
| 10-08 22:21 | +10 stop | NEAR | UP | 0.59 | 0.41 | -2.14 |
| 10-08 22:21 | +10 stop | ZEC | UP | 0.55 | 0.38 | -2.06 |
| 10-08 22:21 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 10-08 22:20 | +5 | BTC | DOWN | 0.58 | 0.65 | 0.36 |
| 10-08 22:20 | +10 stop | XRP | UP | 0.69 | 0.51 | -2.13 |
| 10-08 22:20 | +20 | XRP | UP | 0.69 | no | -7.05 |
| 10-08 22:20 | +15 | XRP | UP | 0.70 | no | -7.13 |
| 10-08 22:20 | +10 | XRP | UP | 0.70 | no | -7.13 |
| 10-08 22:20 | +5 | XRP | UP | 0.70 | 0.77 | 0.44 |
| 10-08 22:20 | +10 stop | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 10-08 22:20 | +10 stop | BTC | DOWN | 0.56 | 0.68 | 0.86 |
| 10-08 22:20 | +5 | BTC | DOWN | 0.56 | 0.63 | 0.35 |
| 10-08 22:19 | +15 | HYPE | DOWN | 0.68 | 0.87 | 1.62 |
| 10-08 22:19 | +10 stop | BNB | UP | 0.71 | 0.82 | 0.84 |
| 10-08 22:19 | +20 | BNB | UP | 0.71 | 0.94 | 2.07 |
| 10-08 22:19 | +15 | BNB | UP | 0.71 | 0.86 | 1.26 |
| 10-08 22:19 | +10 | BNB | UP | 0.71 | 0.82 | 0.84 |
| 10-08 22:19 | +10 stop | SOL | UP | 0.62 | 0.45 | -2.05 |
| 10-08 22:19 | +10 stop | BTC | UP | 0.49 | 0.34 | -1.84 |
| 10-08 22:19 | +20 | BTC | UP | 0.49 | no | -5.08 |
| 10-08 22:19 | +15 | BTC | UP | 0.49 | no | -5.08 |
| 10-08 22:19 | +10 | BTC | UP | 0.49 | no | -5.08 |
| 10-08 22:19 | +5 | BTC | UP | 0.49 | 0.56 | 0.34 |
| 10-08 22:19 | +15 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 10-08 22:19 | +5 | ETH | DOWN | 0.66 | 0.72 | 0.29 |
| 10-08 22:18 | +10 stop | NEAR | DOWN | 0.59 | 0.36 | -2.64 |
