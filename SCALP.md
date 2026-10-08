# Range-Scalp Bot

*Updated Thu Oct 08 02:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7155 | 6211 | 944 (13) | 0 | $-2138.72 | -4.7% |
| **+10¢** | 5429 | 4320 | 1109 (20) | 0 | $-2050.17 | -6.0% |
| **+15¢** | 4555 | 3384 | 1171 (28) | 0 | $-1690.25 | -5.9% |
| **+20¢** | 4068 | 2851 | 1217 (35) | 0 | $-1320.66 | -5.2% |
| **+10¢ (15¢ stop)** | 8664 | 8642 | 22 (14) | 0 | $-3110.56 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 02:28 | +5 | ETH | DOWN | 0.66 | 0.72 | 0.29 |
| 10-08 02:28 | +10 stop | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 10-08 02:28 | +15 | ETH | DOWN | 0.66 | yes | -6.76 |
| 10-08 02:28 | +10 | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 10-08 02:27 | +10 stop | ETH | UP | 0.40 | 0.61 | 1.76 |
| 10-08 02:27 | +15 | ETH | UP | 0.40 | 0.61 | 1.76 |
| 10-08 02:27 | +10 | ETH | UP | 0.40 | 0.61 | 1.76 |
| 10-08 02:26 | +10 stop | ZEC | DOWN | 0.70 | 0.88 | 1.57 |
| 10-08 02:25 | +10 stop | ETH | UP | 0.67 | 0.79 | 0.92 |
| 10-08 02:23 | +10 stop | BTC | UP | 0.70 | 0.80 | 0.73 |
| 10-08 02:23 | +10 stop | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 10-08 02:23 | +10 stop | ETH | DOWN | 0.54 | 0.39 | -1.85 |
| 10-08 02:23 | +5 | ETH | DOWN | 0.54 | 0.61 | 0.35 |
| 10-08 02:21 | +10 stop | HYPE | DOWN | 0.61 | 0.44 | -2.05 |
| 10-08 02:19 | +10 stop | HYPE | DOWN | 0.63 | 0.47 | -1.95 |
| 10-08 02:19 | +5 | BNB | DOWN | 0.65 | yes | -6.65 |
| 10-08 02:18 | +10 stop | SOL | DOWN | 0.57 | 0.38 | -2.25 |
| 10-08 02:18 | +10 stop | NEAR | UP | 0.68 | 0.79 | 0.82 |
| 10-08 02:18 | +20 | NEAR | UP | 0.68 | 0.89 | 1.87 |
| 10-08 02:18 | +15 | NEAR | UP | 0.68 | 0.86 | 1.55 |
| 10-08 02:18 | +10 | NEAR | UP | 0.68 | 0.79 | 0.82 |
| 10-08 02:18 | +5 | NEAR | UP | 0.68 | 0.74 | 0.30 |
| 10-08 02:18 | +10 stop | DOGE | DOWN | 0.70 | 0.28 | -4.50 |
| 10-08 02:18 | +10 stop | BTC | DOWN | 0.67 | 0.46 | -2.44 |
| 10-08 02:18 | +20 | BTC | DOWN | 0.67 | yes | -6.86 |
| 10-08 02:18 | +15 | BTC | DOWN | 0.66 | yes | -6.76 |
| 10-08 02:18 | +10 | BTC | DOWN | 0.64 | yes | -6.57 |
| 10-08 02:18 | +5 | BTC | DOWN | 0.63 | yes | -6.47 |
| 10-08 02:18 | +10 stop | BNB | DOWN | 0.62 | 0.26 | -3.91 |
| 10-08 02:18 | +20 | BNB | DOWN | 0.62 | yes | -6.37 |
| 10-08 02:18 | +15 | BNB | DOWN | 0.62 | yes | -6.37 |
| 10-08 02:18 | +10 | BNB | DOWN | 0.62 | yes | -6.37 |
| 10-08 02:18 | +5 | BNB | DOWN | 0.62 | 0.68 | 0.27 |
| 10-08 02:18 | +10 stop | XRP | DOWN | 0.69 | 0.54 | -1.83 |
| 10-08 02:18 | +15 | XRP | DOWN | 0.69 | yes | -7.05 |
| 10-08 02:18 | +10 | XRP | DOWN | 0.69 | yes | -7.05 |
| 10-08 02:18 | +5 | XRP | DOWN | 0.69 | yes | -7.05 |
| 10-08 02:17 | +10 stop | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 10-08 02:17 | +10 stop | SOL | UP | 0.58 | 0.42 | -1.96 |
| 10-08 02:17 | +20 | SOL | UP | 0.58 | 0.82 | 2.11 |
