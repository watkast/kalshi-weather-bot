# Range-Scalp Bot

*Updated Mon Oct 19 04:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23486 | 20425 | 3061 (30) | 2 | $-6987.47 | -4.7% |
| **+10¢** | 17665 | 14137 | 3528 (44) | 2 | $-6222.26 | -5.6% |
| **+15¢** | 14809 | 11007 | 3802 (66) | 2 | $-5634.38 | -6.1% |
| **+20¢** | 13110 | 9133 | 3977 (84) | 2 | $-4997.67 | -6.1% |
| **+10¢ (15¢ stop)** | 28923 | 28872 | 51 (30) | 0 | $-10973.43 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 04:27 | +10 stop | ETH | DOWN | 0.56 | 0.71 | 1.17 |
| 10-19 04:26 | +10 stop | NEAR | UP | 0.58 | 0.43 | -1.86 |
| 10-19 04:26 | +10 stop | ETH | UP | 0.64 | 0.37 | -3.04 |
| 10-19 04:26 | +20 | ETH | UP | 0.64 | open |  |
| 10-19 04:26 | +15 | ETH | UP | 0.64 | open |  |
| 10-19 04:26 | +10 | ETH | UP | 0.64 | open |  |
| 10-19 04:26 | +5 | ETH | UP | 0.64 | open |  |
| 10-19 04:25 | +10 stop | BTC | UP | 0.70 | 0.52 | -2.13 |
| 10-19 04:25 | +10 stop | SOL | DOWN | 0.52 | 0.65 | 0.96 |
| 10-19 04:24 | +10 stop | NEAR | UP | 0.67 | 0.38 | -3.23 |
| 10-19 04:24 | +10 stop | SOL | UP | 0.61 | 0.30 | -3.42 |
| 10-19 04:24 | +10 stop | XRP | UP | 0.71 | 0.48 | -2.63 |
| 10-19 04:24 | +10 stop | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 10-19 04:23 | +10 stop | DOGE | UP | 0.61 | 0.15 | -4.86 |
| 10-19 04:22 | +10 stop | XRP | UP | 0.68 | 0.81 | 1.03 |
| 10-19 04:22 | +10 stop | NEAR | DOWN | 0.66 | 0.42 | -2.74 |
| 10-19 04:22 | +15 | NEAR | DOWN | 0.66 | 0.89 | 2.07 |
| 10-19 04:22 | +10 | NEAR | DOWN | 0.66 | 0.89 | 2.07 |
| 10-19 04:22 | +5 | NEAR | DOWN | 0.66 | 0.71 | 0.19 |
| 10-19 04:22 | +10 stop | SOL | UP | 0.69 | 0.84 | 1.25 |
| 10-19 04:21 | +5 | HYPE | DOWN | 0.66 | 0.74 | 0.50 |
| 10-19 04:21 | +10 stop | HYPE | DOWN | 0.68 | 0.48 | -2.34 |
| 10-19 04:21 | +10 | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-19 04:21 | +5 | HYPE | DOWN | 0.62 | 0.67 | 0.17 |
| 10-19 04:20 | +5 | ETH | UP | 0.62 | 0.70 | 0.48 |
| 10-19 04:20 | +10 stop | BTC | UP | 0.58 | 0.75 | 1.38 |
| 10-19 04:20 | +10 stop | XRP | UP | 0.51 | 0.62 | 0.76 |
| 10-19 04:20 | +10 stop | BNB | UP | 0.53 | 0.71 | 1.47 |
| 10-19 04:19 | +10 stop | DOGE | DOWN | 0.69 | 0.54 | -1.85 |
| 10-19 04:19 | +10 | DOGE | DOWN | 0.69 | 0.84 | 1.24 |
| 10-19 04:19 | +5 | DOGE | DOWN | 0.69 | 0.84 | 1.24 |
| 10-19 04:18 | +10 stop | SOL | DOWN | 0.64 | 0.49 | -1.85 |
| 10-19 04:18 | +10 stop | BTC | DOWN | 0.56 | 0.40 | -1.95 |
| 10-19 04:18 | +20 | BTC | DOWN | 0.56 | 0.86 | 2.73 |
| 10-19 04:18 | +15 | BTC | DOWN | 0.56 | 0.86 | 2.73 |
| 10-19 04:18 | +10 | BTC | DOWN | 0.56 | 0.67 | 0.76 |
| 10-19 04:18 | +5 | BTC | DOWN | 0.56 | 0.67 | 0.76 |
| 10-19 04:17 | +10 stop | HYPE | DOWN | 0.54 | 0.67 | 0.96 |
| 10-19 04:17 | +20 | HYPE | DOWN | 0.54 | 0.74 | 1.68 |
| 10-19 04:17 | +15 | HYPE | DOWN | 0.54 | 0.74 | 1.68 |
