# Range-Scalp Bot

*Updated Thu Oct 22 01:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28045 | 24431 | 3614 (39) | 0 | $-8099.46 | -4.6% |
| **+10¢** | 21070 | 16895 | 4175 (55) | 0 | $-7149.22 | -5.4% |
| **+15¢** | 17650 | 13158 | 4492 (78) | 0 | $-6375.87 | -5.8% |
| **+20¢** | 15623 | 10915 | 4708 (98) | 0 | $-5720.77 | -5.8% |
| **+10¢ (15¢ stop)** | 34434 | 34375 | 59 (32) | 0 | $-12854.81 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 01:32 | +10 stop | NEAR | DOWN | 0.63 | 0.83 | 1.73 |
| 10-22 01:32 | +20 | NEAR | DOWN | 0.63 | 0.83 | 1.73 |
| 10-22 01:32 | +15 | NEAR | DOWN | 0.63 | 0.83 | 1.73 |
| 10-22 01:32 | +10 | NEAR | DOWN | 0.63 | 0.83 | 1.73 |
| 10-22 01:32 | +5 | NEAR | DOWN | 0.63 | 0.83 | 1.73 |
| 10-22 01:32 | +10 stop | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-22 01:32 | +20 | HYPE | DOWN | 0.70 | 0.90 | 1.82 |
| 10-22 01:32 | +15 | HYPE | DOWN | 0.70 | 0.90 | 1.82 |
| 10-22 01:32 | +10 | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-22 01:32 | +5 | HYPE | DOWN | 0.70 | 0.79 | 0.63 |
| 10-22 01:27 | +10 stop | XRP | UP | 0.71 | 0.84 | 1.05 |
| 10-22 01:27 | +5 | BNB | UP | 0.67 | 0.72 | 0.19 |
| 10-22 01:26 | +5 | BNB | UP | 0.55 | 0.65 | 0.66 |
| 10-22 01:25 | +10 stop | BNB | UP | 0.68 | 0.92 | 2.13 |
| 10-22 01:25 | +20 | BNB | UP | 0.68 | 0.92 | 2.13 |
| 10-22 01:25 | +15 | BNB | UP | 0.68 | 0.92 | 2.13 |
| 10-22 01:25 | +10 | BNB | UP | 0.68 | 0.92 | 2.13 |
| 10-22 01:25 | +5 | BNB | UP | 0.68 | 0.73 | 0.20 |
| 10-22 01:25 | +10 stop | XRP | UP | 0.68 | 0.47 | -2.43 |
| 10-22 01:25 | +20 | XRP | UP | 0.68 | 0.98 | 2.87 |
| 10-22 01:25 | +15 | XRP | UP | 0.68 | 0.84 | 1.36 |
| 10-22 01:25 | +10 | XRP | UP | 0.68 | 0.78 | 0.73 |
| 10-22 01:25 | +5 | XRP | UP | 0.67 | 0.78 | 0.81 |
| 10-22 01:23 | +10 stop | DOGE | DOWN | 0.58 | 0.76 | 1.49 |
| 10-22 01:23 | +10 | DOGE | DOWN | 0.58 | 0.76 | 1.49 |
| 10-22 01:23 | +5 | XRP | UP | 0.59 | 0.66 | 0.37 |
| 10-22 01:22 | +10 stop | HYPE | DOWN | 0.59 | 0.75 | 1.25 |
| 10-22 01:22 | +10 | HYPE | DOWN | 0.59 | 0.75 | 1.29 |
| 10-22 01:21 | +10 stop | SOL | DOWN | 0.71 | 0.86 | 1.26 |
| 10-22 01:21 | +5 | NEAR | DOWN | 0.59 | 0.72 | 0.98 |
| 10-22 01:20 | +10 stop | SOL | DOWN | 0.70 | 0.55 | -1.83 |
| 10-22 01:20 | +15 | SOL | DOWN | 0.69 | 0.86 | 1.46 |
| 10-22 01:20 | +10 | SOL | DOWN | 0.69 | 0.86 | 1.46 |
| 10-22 01:20 | +5 | SOL | DOWN | 0.69 | 0.76 | 0.42 |
| 10-22 01:19 | +5 | SOL | DOWN | 0.68 | 0.73 | 0.20 |
| 10-22 01:19 | +5 | BTC | UP | 0.68 | 0.73 | 0.20 |
| 10-22 01:18 | +10 stop | ETH | UP | 0.60 | 0.76 | 1.30 |
| 10-22 01:18 | +10 stop | NEAR | DOWN | 0.64 | 0.79 | 1.21 |
| 10-22 01:18 | +15 | NEAR | DOWN | 0.64 | 0.79 | 1.21 |
| 10-22 01:18 | +10 | NEAR | DOWN | 0.64 | 0.79 | 1.21 |
