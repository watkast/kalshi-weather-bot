# Range-Scalp Bot

*Updated Tue Oct 06 00:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4382 | 3777 | 605 (6) | 0 | $-1486.16 | -5.4% |
| **+10¢** | 3374 | 2673 | 701 (9) | 0 | $-1364.69 | -6.4% |
| **+15¢** | 2831 | 2091 | 740 (12) | 0 | $-1181.70 | -6.6% |
| **+20¢** | 2534 | 1762 | 772 (17) | 0 | $-1007.05 | -6.3% |
| **+10¢ (15¢ stop)** | 5368 | 5357 | 11 (6) | 0 | $-1909.62 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 00:11 | +10 stop | DOGE | UP | 0.71 | 0.44 | -3.03 |
| 10-06 00:10 | +10 stop | DOGE | UP | 0.52 | 0.64 | 0.85 |
| 10-06 00:09 | +5 | XRP | UP | 0.65 | 0.71 | 0.29 |
| 10-06 00:09 | +5 | XRP | DOWN | 0.42 | 0.55 | 0.94 |
| 10-06 00:08 | +10 stop | DOGE | DOWN | 0.66 | 0.49 | -2.00 |
| 10-06 00:08 | +20 | DOGE | DOWN | 0.66 | 0.89 | 2.11 |
| 10-06 00:08 | +15 | DOGE | DOWN | 0.66 | 0.89 | 2.11 |
| 10-06 00:08 | +10 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-06 00:08 | +5 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-06 00:08 | +10 stop | BNB | DOWN | 0.62 | 0.46 | -1.95 |
| 10-06 00:08 | +20 | BNB | DOWN | 0.62 | yes | -6.37 |
| 10-06 00:08 | +15 | BNB | DOWN | 0.62 | yes | -6.37 |
| 10-06 00:08 | +10 | BNB | DOWN | 0.62 | yes | -6.37 |
| 10-06 00:08 | +5 | BNB | DOWN | 0.62 | yes | -6.37 |
| 10-06 00:08 | +10 stop | BTC | UP | 0.71 | 0.81 | 0.74 |
| 10-06 00:08 | +10 | BTC | UP | 0.71 | 0.81 | 0.74 |
| 10-06 00:08 | +5 | BTC | UP | 0.71 | 0.76 | 0.22 |
| 10-06 00:08 | +10 stop | NEAR | DOWN | 0.56 | 0.32 | -2.74 |
| 10-06 00:08 | +10 stop | XRP | DOWN | 0.51 | 0.32 | -2.21 |
| 10-06 00:08 | +5 | XRP | DOWN | 0.51 | 0.56 | 0.17 |
| 10-06 00:06 | +10 stop | NEAR | UP | 0.63 | 0.39 | -2.74 |
| 10-06 00:06 | +5 | SOL | UP | 0.65 | 0.73 | 0.50 |
| 10-06 00:05 | +5 | ETH | UP | 0.62 | 0.67 | 0.17 |
| 10-06 00:05 | +10 stop | HYPE | UP | 0.55 | 0.84 | 2.62 |
| 10-06 00:05 | +10 stop | ETH | UP | 0.58 | 0.70 | 0.87 |
| 10-06 00:05 | +10 stop | NEAR | DOWN | 0.60 | 0.38 | -2.58 |
| 10-06 00:05 | +10 stop | SOL | UP | 0.64 | 0.78 | 1.10 |
| 10-06 00:05 | +20 | SOL | UP | 0.64 | 0.84 | 1.73 |
| 10-06 00:05 | +15 | SOL | UP | 0.64 | 0.80 | 1.31 |
| 10-06 00:05 | +10 | SOL | UP | 0.64 | 0.78 | 1.10 |
| 10-06 00:05 | +5 | SOL | UP | 0.64 | 0.69 | 0.18 |
| 10-06 00:04 | +10 stop | BTC | UP | 0.56 | 0.69 | 0.97 |
| 10-06 00:04 | +15 | BTC | UP | 0.56 | 0.76 | 1.69 |
| 10-06 00:04 | +10 | BTC | UP | 0.56 | 0.69 | 0.97 |
| 10-06 00:04 | +5 | BTC | UP | 0.56 | 0.69 | 0.97 |
| 10-06 00:04 | +5 | ETH | UP | 0.57 | 0.63 | 0.25 |
| 10-06 00:04 | +5 | HYPE | UP | 0.62 | 0.84 | 1.89 |
| 10-06 00:04 | +10 stop | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 10-06 00:03 | +10 stop | HYPE | UP | 0.70 | 0.53 | -2.03 |
| 10-06 00:03 | +20 | HYPE | UP | 0.69 | 0.93 | 2.21 |
