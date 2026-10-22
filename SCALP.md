# Range-Scalp Bot

*Updated Thu Oct 22 22:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29387 | 25577 | 3810 (39) | 0 | $-8686.16 | -4.7% |
| **+10¢** | 22032 | 17621 | 4411 (55) | 2 | $-7837.76 | -5.7% |
| **+15¢** | 18448 | 13711 | 4737 (78) | 0 | $-7024.44 | -6.1% |
| **+20¢** | 16330 | 11363 | 4967 (100) | 0 | $-6370.25 | -6.2% |
| **+10¢ (15¢ stop)** | 36056 | 35997 | 59 (32) | 0 | $-13601.84 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 22:42 | +15 | BTC | DOWN | 0.71 | 0.87 | 1.37 |
| 10-22 22:42 | +10 | BTC | DOWN | 0.71 | 0.87 | 1.37 |
| 10-22 22:42 | +10 stop | BTC | DOWN | 0.69 | 0.87 | 1.57 |
| 10-22 22:42 | +5 | BTC | DOWN | 0.69 | 0.87 | 1.57 |
| 10-22 22:41 | +10 stop | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 10-22 22:41 | +5 | ETH | DOWN | 0.62 | 0.69 | 0.38 |
| 10-22 22:41 | +10 stop | ZEC | UP | 0.56 | 0.38 | -2.15 |
| 10-22 22:40 | +10 stop | HYPE | DOWN | 0.59 | 0.79 | 1.71 |
| 10-22 22:40 | +10 stop | ETH | UP | 0.67 | 0.45 | -2.54 |
| 10-22 22:40 | +10 | ETH | UP | 0.67 | open |  |
| 10-22 22:40 | +5 | ETH | UP | 0.67 | 0.74 | 0.40 |
| 10-22 22:39 | +5 | SOL | DOWN | 0.58 | 0.64 | 0.25 |
| 10-22 22:39 | +10 stop | SOL | DOWN | 0.55 | 0.84 | 2.62 |
| 10-22 22:39 | +5 | SOL | DOWN | 0.55 | 0.63 | 0.45 |
| 10-22 22:38 | +10 stop | BNB | DOWN | 0.60 | 0.70 | 0.68 |
| 10-22 22:38 | +10 stop | BTC | UP | 0.68 | 0.47 | -2.44 |
| 10-22 22:38 | +5 | BTC | UP | 0.68 | 0.73 | 0.20 |
| 10-22 22:38 | +10 stop | XRP | DOWN | 0.53 | 0.68 | 1.16 |
| 10-22 22:38 | +10 stop | ETH | UP | 0.56 | 0.69 | 0.97 |
| 10-22 22:38 | +10 | ETH | UP | 0.56 | 0.69 | 0.97 |
| 10-22 22:38 | +5 | ETH | UP | 0.56 | 0.69 | 0.97 |
| 10-22 22:38 | +5 | SOL | UP | 0.51 | 0.64 | 0.95 |
| 10-22 22:38 | +10 stop | XRP | UP | 0.53 | 0.63 | 0.65 |
| 10-22 22:38 | +10 stop | HYPE | UP | 0.60 | 0.34 | -2.93 |
| 10-22 22:36 | +10 stop | XRP | UP | 0.58 | 0.68 | 0.66 |
| 10-22 22:36 | +10 stop | SOL | UP | 0.60 | 0.45 | -1.85 |
| 10-22 22:36 | +10 | SOL | UP | 0.60 | open |  |
| 10-22 22:36 | +5 | SOL | UP | 0.60 | 0.66 | 0.29 |
| 10-22 22:36 | +10 stop | BNB | UP | 0.61 | 0.42 | -2.25 |
| 10-22 22:36 | +10 stop | ETH | UP | 0.64 | 0.74 | 0.69 |
| 10-22 22:36 | +10 | ETH | UP | 0.63 | 0.74 | 0.79 |
| 10-22 22:36 | +5 | ETH | UP | 0.62 | 0.68 | 0.27 |
| 10-22 22:36 | +10 stop | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 10-22 22:36 | +10 stop | SOL | DOWN | 0.56 | 0.68 | 0.86 |
| 10-22 22:36 | +10 | SOL | DOWN | 0.56 | 0.68 | 0.86 |
| 10-22 22:36 | +5 | SOL | DOWN | 0.56 | 0.68 | 0.86 |
| 10-22 22:36 | +10 stop | ZEC | UP | 0.66 | 0.76 | 0.71 |
| 10-22 22:35 | +5 | NEAR | DOWN | 0.67 | 0.73 | 0.30 |
| 10-22 22:35 | +10 stop | BNB | DOWN | 0.65 | 0.49 | -1.94 |
| 10-22 22:35 | +10 | BNB | DOWN | 0.65 | 0.84 | 1.64 |
