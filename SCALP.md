# Range-Scalp Bot

*Updated Thu Nov 26 01:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72151 | 62984 | 9167 (158) | 2 | $-19141.02 | -4.2% |
| **+10¢** | 53820 | 43115 | 10705 (203) | 2 | $-17726.87 | -5.2% |
| **+15¢** | 45064 | 33534 | 11530 (260) | 1 | $-15808.71 | -5.6% |
| **+20¢** | 40122 | 27979 | 12143 (326) | 2 | $-14193.77 | -5.6% |
| **+10¢ (15¢ stop)** | 87835 | 87626 | 209 (128) | 0 | $-32215.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 01:42 | +10 stop | BNB | DOWN | 0.67 | 0.18 | -5.16 |
| 11-26 01:42 | +5 | BNB | DOWN | 0.67 | open |  |
| 11-26 01:42 | +10 stop | ZEC | DOWN | 0.59 | 0.20 | -4.19 |
| 11-26 01:41 | +10 stop | BNB | UP | 0.52 | 0.21 | -3.40 |
| 11-26 01:41 | +10 stop | SOL | DOWN | 0.49 | 0.68 | 1.56 |
| 11-26 01:40 | +10 stop | BNB | DOWN | 0.67 | 0.44 | -2.64 |
| 11-26 01:39 | +10 stop | ZEC | DOWN | 0.59 | 0.43 | -1.95 |
| 11-26 01:38 | +10 stop | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 11-26 01:38 | +10 stop | BNB | DOWN | 0.67 | 0.44 | -2.64 |
| 11-26 01:38 | +5 | BNB | DOWN | 0.67 | 0.77 | 0.71 |
| 11-26 01:38 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-26 01:37 | +10 stop | DOGE | UP | 0.50 | 0.76 | 2.29 |
| 11-26 01:36 | +10 stop | ZEC | DOWN | 0.60 | 0.74 | 1.09 |
| 11-26 01:35 | +10 stop | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 11-26 01:35 | +10 stop | ZEC | UP | 0.57 | 0.39 | -2.15 |
| 11-26 01:34 | +10 stop | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 11-26 01:34 | +5 | XRP | UP | 0.61 | 0.67 | 0.27 |
| 11-26 01:34 | +10 stop | BNB | DOWN | 0.65 | 0.77 | 0.91 |
| 11-26 01:34 | +10 stop | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-26 01:34 | +10 | BNB | DOWN | 0.69 | open |  |
| 11-26 01:34 | +5 | BNB | DOWN | 0.69 | 0.77 | 0.52 |
| 11-26 01:34 | +10 stop | SOL | DOWN | 0.71 | 0.52 | -2.23 |
| 11-26 01:34 | +5 | XRP | UP | 0.56 | 0.62 | 0.25 |
| 11-26 01:33 | +10 stop | BTC | DOWN | 0.58 | 0.69 | 0.77 |
| 11-26 01:33 | +10 stop | ETH | DOWN | 0.60 | 0.72 | 0.88 |
| 11-26 01:33 | +5 | XRP | UP | 0.64 | 0.69 | 0.18 |
| 11-26 01:32 | +10 stop | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 11-26 01:32 | +20 | NEAR | UP | 0.70 | 0.95 | 2.33 |
| 11-26 01:32 | +15 | NEAR | UP | 0.70 | 0.85 | 1.26 |
| 11-26 01:32 | +10 | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 11-26 01:32 | +5 | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 11-26 01:31 | +10 stop | BNB | UP | 0.59 | 0.40 | -2.23 |
| 11-26 01:31 | +20 | BNB | UP | 0.58 | 0.80 | 1.86 |
| 11-26 01:31 | +15 | BNB | UP | 0.58 | 0.80 | 1.86 |
| 11-26 01:31 | +10 | BNB | UP | 0.56 | 0.66 | 0.66 |
| 11-26 01:31 | +5 | BNB | UP | 0.56 | 0.66 | 0.66 |
| 11-26 01:31 | +10 stop | ZEC | UP | 0.70 | 0.51 | -2.23 |
| 11-26 01:31 | +20 | ZEC | UP | 0.69 | 0.91 | 1.93 |
| 11-26 01:31 | +15 | ZEC | UP | 0.69 | 0.91 | 1.93 |
| 11-26 01:31 | +10 | ZEC | UP | 0.69 | 0.91 | 1.93 |
