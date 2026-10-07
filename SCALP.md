# Range-Scalp Bot

*Updated Wed Oct 07 07:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6169 | 5352 | 817 (9) | 0 | $-1871.46 | -4.8% |
| **+10¢** | 4704 | 3745 | 959 (16) | 1 | $-1741.29 | -5.9% |
| **+15¢** | 3951 | 2937 | 1014 (20) | 1 | $-1474.75 | -5.9% |
| **+20¢** | 3533 | 2474 | 1059 (27) | 1 | $-1198.75 | -5.4% |
| **+10¢ (15¢ stop)** | 7473 | 7458 | 15 (9) | 0 | $-2579.43 | -5.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 07:51 | +10 stop | NEAR | UP | 0.62 | 0.34 | -3.13 |
| 10-07 07:49 | +10 stop | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-07 07:49 | +10 | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-07 07:49 | +5 | ZEC | DOWN | 0.63 | 0.69 | 0.28 |
| 10-07 07:49 | +5 | BTC | DOWN | 0.64 | 0.71 | 0.38 |
| 10-07 07:49 | +5 | ETH | DOWN | 0.67 | 0.74 | 0.40 |
| 10-07 07:48 | +10 stop | NEAR | UP | 0.57 | 0.40 | -2.05 |
| 10-07 07:47 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-07 07:47 | +5 | XRP | DOWN | 0.71 | 0.79 | 0.53 |
| 10-07 07:47 | +10 stop | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-07 07:47 | +10 | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-07 07:47 | +5 | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-07 07:47 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 10-07 07:47 | +10 stop | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
| 10-07 07:47 | +20 | ZEC | DOWN | 0.63 | 0.84 | 1.83 |
| 10-07 07:47 | +15 | ZEC | DOWN | 0.63 | 0.79 | 1.31 |
| 10-07 07:47 | +10 | ZEC | DOWN | 0.63 | 0.74 | 0.78 |
| 10-07 07:47 | +5 | ZEC | DOWN | 0.63 | 0.74 | 0.78 |
| 10-07 07:46 | +10 stop | ETH | DOWN | 0.71 | 0.55 | -1.93 |
| 10-07 07:46 | +20 | ETH | DOWN | 0.71 | 0.92 | 1.85 |
| 10-07 07:46 | +15 | ETH | DOWN | 0.71 | 0.87 | 1.37 |
| 10-07 07:46 | +10 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-07 07:46 | +5 | ETH | DOWN | 0.71 | 0.77 | 0.32 |
| 10-07 07:46 | +10 stop | DOGE | DOWN | 0.58 | 0.70 | 0.87 |
| 10-07 07:46 | +20 | DOGE | DOWN | 0.58 | 0.81 | 2.01 |
| 10-07 07:46 | +15 | DOGE | DOWN | 0.58 | 0.81 | 2.01 |
| 10-07 07:46 | +10 | DOGE | DOWN | 0.58 | 0.70 | 0.87 |
| 10-07 07:46 | +5 | DOGE | DOWN | 0.58 | 0.70 | 0.87 |
| 10-07 07:46 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-07 07:46 | +20 | BTC | DOWN | 0.67 | 0.89 | 1.97 |
| 10-07 07:46 | +15 | BTC | DOWN | 0.67 | 0.82 | 1.23 |
| 10-07 07:46 | +10 | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-07 07:46 | +5 | BTC | DOWN | 0.67 | 0.75 | 0.50 |
| 10-07 07:45 | +10 stop | BNB | UP | 0.65 | 0.76 | 0.81 |
| 10-07 07:45 | +20 | BNB | UP | 0.65 | 0.86 | 1.85 |
| 10-07 07:45 | +15 | BNB | UP | 0.65 | 0.81 | 1.33 |
| 10-07 07:45 | +10 | BNB | UP | 0.65 | 0.76 | 0.81 |
| 10-07 07:45 | +5 | BNB | UP | 0.65 | 0.71 | 0.29 |
| 10-07 07:45 | +10 stop | NEAR | DOWN | 0.62 | 0.38 | -2.71 |
| 10-07 07:45 | +20 | NEAR | DOWN | 0.62 | 0.82 | 1.76 |
