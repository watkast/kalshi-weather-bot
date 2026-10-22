# Range-Scalp Bot

*Updated Thu Oct 22 10:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28620 | 24941 | 3679 (39) | 4 | $-8215.42 | -4.6% |
| **+10¢** | 21476 | 17218 | 4258 (55) | 5 | $-7316.70 | -5.4% |
| **+15¢** | 17977 | 13397 | 4580 (78) | 5 | $-6544.73 | -5.8% |
| **+20¢** | 15904 | 11100 | 4804 (100) | 5 | $-5911.13 | -5.9% |
| **+10¢ (15¢ stop)** | 35112 | 35053 | 59 (32) | 0 | $-13157.58 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 10:57 | +10 stop | BNB | UP | 0.62 | 0.81 | 1.62 |
| 10-22 10:57 | +10 stop | BNB | DOWN | 0.63 | 0.45 | -2.15 |
| 10-22 10:55 | +5 | BNB | UP | 0.67 | 0.81 | 1.14 |
| 10-22 10:55 | +5 | ZEC | UP | 0.64 | 0.76 | 0.90 |
| 10-22 10:54 | +10 stop | BTC | DOWN | 0.64 | 0.83 | 1.63 |
| 10-22 10:53 | +10 stop | BNB | UP | 0.70 | 0.45 | -2.83 |
| 10-22 10:53 | +20 | BNB | UP | 0.70 | 0.97 | 2.55 |
| 10-22 10:53 | +15 | BNB | UP | 0.70 | 0.86 | 1.36 |
| 10-22 10:53 | +10 | BNB | UP | 0.70 | 0.81 | 0.84 |
| 10-22 10:53 | +5 | BNB | UP | 0.70 | 0.75 | 0.21 |
| 10-22 10:53 | +5 | ZEC | UP | 0.62 | 0.76 | 1.10 |
| 10-22 10:53 | +10 stop | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 10-22 10:53 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 10-22 10:52 | +10 stop | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-22 10:52 | +10 stop | BTC | UP | 0.53 | 0.33 | -2.34 |
| 10-22 10:52 | +10 | BTC | UP | 0.53 | open |  |
| 10-22 10:52 | +5 | BTC | UP | 0.53 | 0.59 | 0.25 |
| 10-22 10:51 | +10 stop | XRP | DOWN | 0.66 | 0.81 | 1.23 |
| 10-22 10:51 | +20 | XRP | DOWN | 0.67 | 0.87 | 1.76 |
| 10-22 10:51 | +15 | XRP | DOWN | 0.71 | 0.87 | 1.37 |
| 10-22 10:51 | +10 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-22 10:51 | +5 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-22 10:51 | +10 stop | SOL | DOWN | 0.68 | 0.81 | 1.03 |
| 10-22 10:51 | +10 stop | ZEC | UP | 0.71 | 0.89 | 1.58 |
| 10-22 10:51 | +10 stop | BTC | DOWN | 0.54 | 0.34 | -2.34 |
| 10-22 10:50 | +10 stop | ZEC | DOWN | 0.58 | 0.41 | -2.05 |
| 10-22 10:50 | +10 stop | ETH | DOWN | 0.58 | 0.40 | -2.15 |
| 10-22 10:49 | +10 stop | HYPE | DOWN | 0.69 | 0.80 | 0.85 |
| 10-22 10:49 | +10 stop | BNB | UP | 0.71 | 0.84 | 1.05 |
| 10-22 10:49 | +10 | BNB | UP | 0.71 | 0.84 | 1.05 |
| 10-22 10:49 | +5 | BNB | UP | 0.71 | 0.84 | 1.05 |
| 10-22 10:49 | +10 stop | NEAR | UP | 0.52 | 0.73 | 1.78 |
| 10-22 10:48 | +10 stop | DOGE | DOWN | 0.67 | 0.77 | 0.71 |
| 10-22 10:48 | +10 stop | SOL | DOWN | 0.56 | 0.68 | 0.86 |
| 10-22 10:47 | +10 stop | XRP | DOWN | 0.69 | 0.83 | 1.12 |
| 10-22 10:47 | +10 | XRP | DOWN | 0.69 | 0.83 | 1.12 |
| 10-22 10:47 | +10 stop | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-22 10:47 | +10 stop | BNB | UP | 0.66 | 0.76 | 0.71 |
| 10-22 10:47 | +20 | BNB | UP | 0.66 | 0.88 | 1.96 |
| 10-22 10:47 | +15 | BNB | UP | 0.66 | 0.84 | 1.54 |
