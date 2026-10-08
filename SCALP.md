# Range-Scalp Bot

*Updated Thu Oct 08 04:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7291 | 6320 | 971 (13) | 0 | $-2252.71 | -4.9% |
| **+10¢** | 5528 | 4386 | 1142 (20) | 0 | $-2192.94 | -6.3% |
| **+15¢** | 4630 | 3425 | 1205 (29) | 0 | $-1831.34 | -6.3% |
| **+20¢** | 4132 | 2880 | 1252 (36) | 0 | $-1470.70 | -5.7% |
| **+10¢ (15¢ stop)** | 8818 | 8796 | 22 (14) | 0 | $-3189.59 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 03:57 | +5 | DOGE | DOWN | 0.63 | 0.70 | 0.38 |
| 10-08 03:57 | +10 stop | DOGE | DOWN | 0.55 | 0.70 | 1.17 |
| 10-08 03:57 | +10 | DOGE | DOWN | 0.55 | 0.70 | 1.17 |
| 10-08 03:57 | +5 | DOGE | DOWN | 0.55 | 0.62 | 0.35 |
| 10-08 03:56 | +10 stop | ETH | UP | 0.60 | 0.29 | -3.42 |
| 10-08 03:55 | +10 stop | ETH | DOWN | 0.65 | 0.44 | -2.44 |
| 10-08 03:52 | +10 stop | NEAR | DOWN | 0.65 | 0.81 | 1.34 |
| 10-08 03:52 | +15 | NEAR | DOWN | 0.65 | 0.81 | 1.34 |
| 10-08 03:52 | +10 | NEAR | DOWN | 0.65 | 0.81 | 1.34 |
| 10-08 03:52 | +5 | NEAR | DOWN | 0.65 | 0.73 | 0.51 |
| 10-08 03:51 | +10 stop | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 10-08 03:51 | +20 | DOGE | DOWN | 0.71 | 0.95 | 2.25 |
| 10-08 03:51 | +15 | DOGE | DOWN | 0.71 | 0.95 | 2.25 |
| 10-08 03:51 | +10 | DOGE | DOWN | 0.70 | 0.84 | 1.15 |
| 10-08 03:51 | +5 | DOGE | DOWN | 0.70 | 0.76 | 0.32 |
| 10-08 03:51 | +10 stop | ETH | DOWN | 0.57 | 0.68 | 0.76 |
| 10-08 03:51 | +10 stop | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-08 03:50 | +10 stop | BNB | DOWN | 0.61 | 0.75 | 1.04 |
| 10-08 03:50 | +10 stop | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-08 03:50 | +10 | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-08 03:50 | +5 | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-08 03:49 | +10 stop | ETH | UP | 0.66 | 0.47 | -2.24 |
| 10-08 03:49 | +10 | ETH | UP | 0.66 | no | -6.76 |
| 10-08 03:49 | +5 | ETH | UP | 0.66 | no | -6.76 |
| 10-08 03:49 | +5 | SOL | DOWN | 0.59 | 0.80 | 1.81 |
| 10-08 03:49 | +10 stop | BTC | UP | 0.69 | 0.50 | -2.23 |
| 10-08 03:49 | +10 | BTC | UP | 0.69 | no | -7.05 |
| 10-08 03:49 | +5 | BTC | UP | 0.69 | no | -7.05 |
| 10-08 03:49 | +10 stop | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-08 03:49 | +10 | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-08 03:49 | +5 | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-08 03:48 | +5 | BNB | DOWN | 0.62 | 0.75 | 0.99 |
| 10-08 03:48 | +5 | BTC | UP | 0.57 | 0.67 | 0.66 |
| 10-08 03:48 | +10 stop | SOL | DOWN | 0.57 | 0.80 | 2.00 |
| 10-08 03:48 | +20 | SOL | DOWN | 0.57 | 0.80 | 2.00 |
| 10-08 03:48 | +15 | SOL | DOWN | 0.57 | 0.80 | 2.00 |
| 10-08 03:48 | +10 | SOL | DOWN | 0.57 | 0.80 | 2.00 |
| 10-08 03:48 | +5 | SOL | DOWN | 0.57 | 0.63 | 0.25 |
| 10-08 03:47 | +10 stop | BNB | DOWN | 0.57 | 0.42 | -1.90 |
| 10-08 03:47 | +20 | BNB | DOWN | 0.57 | 0.79 | 1.86 |
