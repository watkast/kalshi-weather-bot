# Range-Scalp Bot

*Updated Thu Oct 22 18:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29121 | 25365 | 3756 (39) | 0 | $-8459.05 | -4.6% |
| **+10¢** | 21843 | 17495 | 4348 (55) | 0 | $-7582.96 | -5.5% |
| **+15¢** | 18284 | 13610 | 4674 (78) | 0 | $-6785.87 | -5.9% |
| **+20¢** | 16184 | 11285 | 4899 (100) | 0 | $-6114.88 | -6.0% |
| **+10¢ (15¢ stop)** | 35729 | 35670 | 59 (32) | 0 | $-13458.95 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 18:28 | +10 stop | SOL | DOWN | 0.47 | 0.61 | 1.05 |
| 10-22 18:28 | +5 | SOL | DOWN | 0.47 | 0.61 | 1.05 |
| 10-22 18:18 | +10 stop | DOGE | UP | 0.70 | 0.82 | 0.94 |
| 10-22 18:18 | +10 stop | SOL | UP | 0.60 | 0.74 | 1.09 |
| 10-22 18:18 | +10 stop | BNB | UP | 0.71 | 0.84 | 1.05 |
| 10-22 18:18 | +10 stop | ETH | UP | 0.68 | 0.78 | 0.71 |
| 10-22 18:17 | +10 stop | XRP | UP | 0.68 | 0.83 | 1.24 |
| 10-22 18:17 | +20 | XRP | UP | 0.68 | 0.88 | 1.76 |
| 10-22 18:17 | +15 | XRP | UP | 0.68 | 0.83 | 1.24 |
| 10-22 18:17 | +10 | XRP | UP | 0.68 | 0.83 | 1.24 |
| 10-22 18:17 | +5 | XRP | UP | 0.68 | 0.74 | 0.30 |
| 10-22 18:17 | +10 stop | BTC | UP | 0.66 | 0.83 | 1.44 |
| 10-22 18:17 | +20 | BTC | UP | 0.66 | 0.89 | 2.07 |
| 10-22 18:17 | +15 | BTC | UP | 0.66 | 0.83 | 1.44 |
| 10-22 18:17 | +10 | BTC | UP | 0.66 | 0.83 | 1.44 |
| 10-22 18:17 | +5 | BTC | UP | 0.66 | 0.72 | 0.29 |
| 10-22 18:16 | +10 stop | ZEC | UP | 0.69 | 0.83 | 1.15 |
| 10-22 18:16 | +20 | ZEC | UP | 0.69 | 0.89 | 1.78 |
| 10-22 18:16 | +15 | ZEC | UP | 0.69 | 0.84 | 1.25 |
| 10-22 18:16 | +10 | ZEC | UP | 0.69 | 0.83 | 1.15 |
| 10-22 18:16 | +5 | ZEC | UP | 0.69 | 0.77 | 0.52 |
| 10-22 18:16 | +10 stop | SOL | DOWN | 0.63 | 0.37 | -2.94 |
| 10-22 18:16 | +20 | SOL | DOWN | 0.63 | yes | -6.47 |
| 10-22 18:16 | +15 | SOL | DOWN | 0.63 | yes | -6.47 |
| 10-22 18:16 | +10 | SOL | DOWN | 0.63 | yes | -6.47 |
| 10-22 18:16 | +5 | SOL | DOWN | 0.64 | 0.70 | 0.28 |
| 10-22 18:16 | +10 stop | BNB | DOWN | 0.56 | 0.38 | -2.17 |
| 10-22 18:16 | +20 | BNB | DOWN | 0.56 | yes | -5.80 |
| 10-22 18:16 | +15 | BNB | DOWN | 0.56 | yes | -5.78 |
| 10-22 18:16 | +10 | BNB | DOWN | 0.56 | yes | -5.78 |
| 10-22 18:16 | +5 | BNB | DOWN | 0.56 | yes | -5.78 |
| 10-22 18:16 | +10 stop | DOGE | DOWN | 0.58 | 0.39 | -2.25 |
| 10-22 18:16 | +20 | DOGE | DOWN | 0.59 | yes | -6.07 |
| 10-22 18:16 | +15 | DOGE | DOWN | 0.59 | yes | -6.07 |
| 10-22 18:16 | +10 | DOGE | DOWN | 0.59 | yes | -6.07 |
| 10-22 18:16 | +5 | DOGE | DOWN | 0.59 | yes | -6.07 |
| 10-22 18:16 | +10 stop | ETH | DOWN | 0.59 | 0.40 | -2.24 |
| 10-22 18:16 | +20 | ETH | DOWN | 0.59 | yes | -6.07 |
| 10-22 18:16 | +15 | ETH | DOWN | 0.59 | yes | -6.07 |
| 10-22 18:16 | +10 | ETH | DOWN | 0.59 | yes | -6.07 |
