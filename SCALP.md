# Range-Scalp Bot

*Updated Mon Oct 26 06:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34406 | 30028 | 4378 (43) | 1 | $-9597.31 | -4.4% |
| **+10¢** | 25760 | 20697 | 5063 (65) | 1 | $-8434.21 | -5.2% |
| **+15¢** | 21542 | 16092 | 5450 (89) | 1 | $-7561.04 | -5.6% |
| **+20¢** | 19090 | 13378 | 5712 (112) | 2 | $-6681.75 | -5.6% |
| **+10¢ (15¢ stop)** | 42154 | 42092 | 62 (33) | 0 | $-16066.34 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 06:43 | +10 stop | NEAR | DOWN | 0.68 | 0.91 | 2.12 |
| 10-26 06:43 | +15 | NEAR | DOWN | 0.68 | 0.91 | 2.12 |
| 10-26 06:37 | +10 stop | BTC | DOWN | 0.48 | 0.30 | -2.13 |
| 10-26 06:37 | +10 stop | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 10-26 06:37 | +5 | DOGE | UP | 0.70 | 0.81 | 0.84 |
| 10-26 06:37 | +10 stop | XRP | DOWN | 0.55 | 0.38 | -2.05 |
| 10-26 06:37 | +10 stop | NEAR | DOWN | 0.66 | 0.49 | -2.04 |
| 10-26 06:37 | +5 | ZEC | UP | 0.56 | 0.61 | 0.15 |
| 10-26 06:36 | +5 | BNB | UP | 0.55 | 0.60 | 0.15 |
| 10-26 06:36 | +10 stop | BTC | DOWN | 0.50 | 0.60 | 0.65 |
| 10-26 06:35 | +10 | DOGE | UP | 0.65 | 0.81 | 1.33 |
| 10-26 06:35 | +10 stop | DOGE | UP | 0.64 | 0.74 | 0.69 |
| 10-26 06:35 | +20 | DOGE | UP | 0.64 | 0.88 | 2.15 |
| 10-26 06:35 | +15 | DOGE | UP | 0.64 | 0.81 | 1.42 |
| 10-26 06:35 | +5 | DOGE | UP | 0.64 | 0.74 | 0.69 |
| 10-26 06:35 | +10 stop | XRP | DOWN | 0.59 | 0.42 | -2.05 |
| 10-26 06:35 | +20 | XRP | DOWN | 0.58 | open |  |
| 10-26 06:35 | +15 | XRP | DOWN | 0.57 | open |  |
| 10-26 06:35 | +10 | XRP | DOWN | 0.57 | open |  |
| 10-26 06:35 | +5 | XRP | DOWN | 0.57 | open |  |
| 10-26 06:35 | +10 stop | NEAR | DOWN | 0.70 | 0.51 | -2.23 |
| 10-26 06:35 | +10 | NEAR | DOWN | 0.70 | 0.91 | 1.89 |
| 10-26 06:35 | +5 | NEAR | DOWN | 0.70 | 0.91 | 1.89 |
| 10-26 06:35 | +10 stop | BNB | UP | 0.58 | 0.69 | 0.77 |
| 10-26 06:35 | +10 | BNB | UP | 0.58 | 0.69 | 0.77 |
| 10-26 06:35 | +5 | BNB | UP | 0.58 | 0.63 | 0.15 |
| 10-26 06:35 | +10 stop | ETH | UP | 0.61 | 0.76 | 1.20 |
| 10-26 06:35 | +10 | ETH | UP | 0.61 | 0.76 | 1.20 |
| 10-26 06:35 | +5 | ETH | UP | 0.61 | 0.76 | 1.20 |
| 10-26 06:35 | +10 stop | ZEC | UP | 0.53 | 0.65 | 0.89 |
| 10-26 06:35 | +20 | ZEC | UP | 0.52 | 0.75 | 1.98 |
| 10-26 06:35 | +15 | ZEC | UP | 0.51 | 0.75 | 2.08 |
| 10-26 06:35 | +10 | ZEC | UP | 0.52 | 0.65 | 0.96 |
| 10-26 06:35 | +5 | ZEC | UP | 0.52 | 0.61 | 0.55 |
| 10-26 06:35 | +5 | BTC | UP | 0.54 | 0.69 | 1.17 |
| 10-26 06:34 | +5 | NEAR | UP | 0.69 | 0.74 | 0.21 |
| 10-26 06:33 | +10 stop | NEAR | UP | 0.62 | 0.74 | 0.89 |
| 10-26 06:33 | +10 | NEAR | UP | 0.62 | 0.74 | 0.89 |
| 10-26 06:33 | +5 | NEAR | UP | 0.62 | 0.67 | 0.17 |
| 10-26 06:31 | +10 stop | ETH | UP | 0.67 | 0.77 | 0.71 |
