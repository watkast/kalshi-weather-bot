# Range-Scalp Bot

*Updated Thu Oct 22 14:49 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28867 | 25148 | 3719 (39) | 0 | $-8344.86 | -4.6% |
| **+10¢** | 21667 | 17366 | 4301 (55) | 0 | $-7427.78 | -5.5% |
| **+15¢** | 18138 | 13513 | 4625 (78) | 0 | $-6644.12 | -5.8% |
| **+20¢** | 16050 | 11200 | 4850 (100) | 1 | $-5990.43 | -5.9% |
| **+10¢ (15¢ stop)** | 35422 | 35363 | 59 (32) | 0 | $-13298.11 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 14:47 | +10 stop | BNB | DOWN | 0.68 | 0.80 | 0.92 |
| 10-22 14:47 | +20 | BNB | DOWN | 0.68 | open |  |
| 10-22 14:47 | +15 | BNB | DOWN | 0.68 | 0.83 | 1.24 |
| 10-22 14:47 | +10 | BNB | DOWN | 0.68 | 0.80 | 0.92 |
| 10-22 14:47 | +5 | BNB | DOWN | 0.68 | 0.75 | 0.40 |
| 10-22 14:41 | +10 stop | HYPE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-22 14:41 | +20 | HYPE | DOWN | 0.59 | yes | -6.07 |
| 10-22 14:41 | +15 | HYPE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-22 14:41 | +10 | HYPE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-22 14:41 | +5 | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
| 10-22 14:41 | +10 stop | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 10-22 14:41 | +15 | NEAR | UP | 0.66 | 0.91 | 2.22 |
| 10-22 14:40 | +10 stop | NEAR | UP | 0.48 | 0.59 | 0.75 |
| 10-22 14:39 | +10 stop | DOGE | UP | 0.55 | 0.68 | 0.96 |
| 10-22 14:39 | +10 | DOGE | UP | 0.55 | 0.68 | 0.96 |
| 10-22 14:39 | +10 stop | XRP | UP | 0.66 | 0.79 | 1.02 |
| 10-22 14:39 | +10 stop | BNB | UP | 0.66 | 0.78 | 0.91 |
| 10-22 14:39 | +10 stop | DOGE | DOWN | 0.46 | 0.56 | 0.64 |
| 10-22 14:39 | +20 | DOGE | DOWN | 0.46 | yes | -4.78 |
| 10-22 14:39 | +15 | DOGE | DOWN | 0.46 | yes | -4.78 |
| 10-22 14:39 | +10 | DOGE | DOWN | 0.46 | 0.56 | 0.64 |
| 10-22 14:38 | +10 stop | BNB | DOWN | 0.68 | 0.39 | -3.23 |
| 10-22 14:38 | +20 | BNB | DOWN | 0.68 | yes | -6.96 |
| 10-22 14:38 | +15 | BNB | DOWN | 0.68 | yes | -6.96 |
| 10-22 14:38 | +10 | BNB | DOWN | 0.68 | yes | -6.96 |
| 10-22 14:38 | +5 | BNB | DOWN | 0.68 | yes | -6.96 |
| 10-22 14:38 | +10 stop | ETH | DOWN | 0.63 | 0.32 | -3.40 |
| 10-22 14:38 | +20 | ETH | DOWN | 0.62 | yes | -6.37 |
| 10-22 14:38 | +15 | ETH | DOWN | 0.62 | yes | -6.37 |
| 10-22 14:38 | +10 | ETH | DOWN | 0.62 | yes | -6.37 |
| 10-22 14:38 | +5 | ETH | DOWN | 0.62 | yes | -6.37 |
| 10-22 14:37 | +10 stop | XRP | DOWN | 0.67 | 0.52 | -1.84 |
| 10-22 14:37 | +10 stop | NEAR | DOWN | 0.71 | 0.50 | -2.43 |
| 10-22 14:37 | +10 | NEAR | DOWN | 0.71 | yes | -7.25 |
| 10-22 14:37 | +5 | NEAR | DOWN | 0.71 | yes | -7.25 |
| 10-22 14:35 | +10 stop | BTC | DOWN | 0.64 | 0.46 | -2.15 |
| 10-22 14:35 | +20 | ZEC | DOWN | 0.70 | yes | -7.15 |
| 10-22 14:35 | +5 | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 10-22 14:35 | +10 | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 10-22 14:35 | +5 | ETH | DOWN | 0.62 | 0.69 | 0.38 |
