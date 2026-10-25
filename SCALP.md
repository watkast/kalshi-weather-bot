# Range-Scalp Bot

*Updated Sun Oct 25 07:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32811 | 28615 | 4196 (42) | 3 | $-9301.64 | -4.5% |
| **+10¢** | 24564 | 19706 | 4858 (60) | 3 | $-8305.58 | -5.4% |
| **+15¢** | 20559 | 15329 | 5230 (83) | 4 | $-7490.39 | -5.8% |
| **+20¢** | 18214 | 12739 | 5475 (105) | 4 | $-6629.22 | -5.8% |
| **+10¢ (15¢ stop)** | 40294 | 40234 | 60 (32) | 0 | $-15386.85 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 07:54 | +5 | BTC | DOWN | 0.70 | open |  |
| 10-25 07:53 | +10 | BNB | DOWN | 0.56 | 0.71 | 1.15 |
| 10-25 07:53 | +10 stop | ETH | DOWN | 0.61 | 0.76 | 1.20 |
| 10-25 07:51 | +10 stop | ETH | UP | 0.64 | 0.48 | -1.95 |
| 10-25 07:51 | +10 stop | ETH | UP | 0.49 | 0.59 | 0.65 |
| 10-25 07:50 | +10 stop | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-25 07:50 | +10 | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-25 07:50 | +5 | ZEC | DOWN | 0.69 | 0.76 | 0.42 |
| 10-25 07:50 | +10 stop | HYPE | DOWN | 0.57 | 0.76 | 1.59 |
| 10-25 07:50 | +20 | HYPE | DOWN | 0.57 | 0.83 | 2.32 |
| 10-25 07:50 | +15 | HYPE | DOWN | 0.57 | 0.76 | 1.59 |
| 10-25 07:50 | +10 | HYPE | DOWN | 0.57 | 0.76 | 1.59 |
| 10-25 07:50 | +5 | HYPE | DOWN | 0.57 | 0.76 | 1.59 |
| 10-25 07:49 | +10 stop | NEAR | DOWN | 0.67 | 0.78 | 0.83 |
| 10-25 07:49 | +10 stop | BNB | DOWN | 0.59 | 0.71 | 0.88 |
| 10-25 07:48 | +10 stop | ETH | DOWN | 0.59 | 0.42 | -2.05 |
| 10-25 07:48 | +10 stop | BTC | DOWN | 0.60 | 0.73 | 0.99 |
| 10-25 07:48 | +20 | BTC | DOWN | 0.60 | open |  |
| 10-25 07:48 | +15 | BTC | DOWN | 0.60 | open |  |
| 10-25 07:48 | +10 | BTC | DOWN | 0.60 | 0.73 | 0.99 |
| 10-25 07:48 | +5 | BTC | DOWN | 0.60 | 0.69 | 0.58 |
| 10-25 07:48 | +5 | DOGE | DOWN | 0.71 | 0.80 | 0.63 |
| 10-25 07:47 | +5 | NEAR | DOWN | 0.71 | 0.78 | 0.47 |
| 10-25 07:47 | +5 | BNB | UP | 0.59 | open |  |
| 10-25 07:47 | +5 | DOGE | DOWN | 0.56 | 0.62 | 0.25 |
| 10-25 07:46 | +10 stop | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-25 07:46 | +20 | ZEC | DOWN | 0.63 | 0.87 | 2.15 |
| 10-25 07:46 | +15 | ZEC | DOWN | 0.63 | 0.78 | 1.20 |
| 10-25 07:46 | +10 | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-25 07:46 | +5 | ZEC | DOWN | 0.63 | 0.70 | 0.38 |
| 10-25 07:46 | +10 stop | XRP | DOWN | 0.55 | 0.69 | 1.07 |
| 10-25 07:46 | +20 | XRP | DOWN | 0.55 | 0.77 | 1.89 |
| 10-25 07:46 | +15 | XRP | DOWN | 0.55 | 0.73 | 1.48 |
| 10-25 07:46 | +10 | XRP | DOWN | 0.55 | 0.69 | 1.07 |
| 10-25 07:46 | +5 | XRP | DOWN | 0.55 | 0.69 | 1.07 |
| 10-25 07:46 | +10 stop | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 10-25 07:46 | +20 | HYPE | DOWN | 0.58 | 0.81 | 2.01 |
| 10-25 07:46 | +15 | HYPE | DOWN | 0.58 | 0.77 | 1.59 |
| 10-25 07:46 | +10 | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 10-25 07:46 | +5 | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
