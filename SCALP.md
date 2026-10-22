# Range-Scalp Bot

*Updated Thu Oct 22 10:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28573 | 24900 | 3673 (39) | 5 | $-8205.52 | -4.6% |
| **+10¢** | 21440 | 17190 | 4250 (55) | 6 | $-7299.55 | -5.4% |
| **+15¢** | 17948 | 13375 | 4573 (78) | 5 | $-6538.29 | -5.8% |
| **+20¢** | 15879 | 11082 | 4797 (100) | 5 | $-5906.73 | -5.9% |
| **+10¢ (15¢ stop)** | 35057 | 34998 | 59 (32) | 0 | $-13151.80 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 10:28 | +10 stop | BTC | UP | 0.19 | 0.66 | 4.43 |
| 10-22 10:28 | +20 | BTC | UP | 0.20 | 0.66 | 4.32 |
| 10-22 10:28 | +15 | BTC | UP | 0.20 | 0.66 | 4.32 |
| 10-22 10:28 | +10 | BTC | UP | 0.21 | 0.66 | 4.22 |
| 10-22 10:28 | +5 | BTC | UP | 0.28 | 0.66 | 3.49 |
| 10-22 10:25 | +10 stop | BTC | UP | 0.66 | 0.81 | 1.23 |
| 10-22 10:25 | +10 | BTC | UP | 0.66 | 0.81 | 1.23 |
| 10-22 10:25 | +5 | BTC | UP | 0.66 | 0.81 | 1.23 |
| 10-22 10:23 | +10 stop | BNB | UP | 0.58 | 0.70 | 0.87 |
| 10-22 10:23 | +10 stop | BNB | DOWN | 0.40 | 0.67 | 2.37 |
| 10-22 10:22 | +10 stop | ZEC | UP | 0.67 | 0.80 | 1.02 |
| 10-22 10:21 | +5 | SOL | UP | 0.60 | 0.68 | 0.47 |
| 10-22 10:21 | +20 | ETH | UP | 0.60 | 0.85 | 2.24 |
| 10-22 10:20 | +10 stop | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 10-22 10:20 | +15 | HYPE | UP | 0.66 | 0.89 | 2.10 |
| 10-22 10:20 | +10 | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 10-22 10:20 | +5 | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 10-22 10:20 | +15 | ETH | UP | 0.59 | 0.78 | 1.60 |
| 10-22 10:20 | +10 stop | BNB | UP | 0.61 | 0.43 | -2.15 |
| 10-22 10:20 | +10 stop | NEAR | UP | 0.60 | 0.70 | 0.68 |
| 10-22 10:20 | +10 stop | DOGE | UP | 0.64 | 0.75 | 0.79 |
| 10-22 10:20 | +10 stop | SOL | UP | 0.63 | 0.85 | 1.94 |
| 10-22 10:20 | +10 stop | ETH | UP | 0.64 | 0.47 | -2.05 |
| 10-22 10:20 | +10 stop | BTC | UP | 0.63 | 0.46 | -2.05 |
| 10-22 10:20 | +20 | BTC | UP | 0.64 | 0.84 | 1.73 |
| 10-22 10:20 | +15 | BTC | UP | 0.64 | 0.81 | 1.42 |
| 10-22 10:20 | +10 | BTC | UP | 0.64 | 0.74 | 0.69 |
| 10-22 10:20 | +5 | BTC | UP | 0.64 | 0.73 | 0.59 |
| 10-22 10:19 | +10 stop | SOL | DOWN | 0.58 | 0.41 | -2.05 |
| 10-22 10:19 | +10 | SOL | DOWN | 0.58 | open |  |
| 10-22 10:19 | +10 stop | ZEC | DOWN | 0.54 | 0.25 | -3.22 |
| 10-22 10:19 | +10 | ZEC | DOWN | 0.54 | open |  |
| 10-22 10:18 | +10 stop | ETH | DOWN | 0.60 | 0.43 | -2.05 |
| 10-22 10:18 | +10 | ETH | DOWN | 0.60 | open |  |
| 10-22 10:18 | +5 | ETH | DOWN | 0.60 | open |  |
| 10-22 10:18 | +5 | XRP | DOWN | 0.58 | open |  |
| 10-22 10:18 | +5 | NEAR | DOWN | 0.65 | open |  |
| 10-22 10:18 | +10 stop | BNB | DOWN | 0.59 | 0.40 | -2.24 |
| 10-22 10:18 | +5 | ZEC | DOWN | 0.69 | open |  |
| 10-22 10:18 | +10 stop | ETH | UP | 0.45 | 0.55 | 0.64 |
