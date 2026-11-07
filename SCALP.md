# Range-Scalp Bot

*Updated Sat Nov 07 15:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51156 | 44598 | 6558 (78) | 2 | $-14290.71 | -4.4% |
| **+10¢** | 38194 | 30549 | 7645 (105) | 3 | $-13268.17 | -5.5% |
| **+15¢** | 31972 | 23730 | 8242 (134) | 2 | $-12209.12 | -6.1% |
| **+20¢** | 28435 | 19796 | 8639 (177) | 3 | $-10777.44 | -6.0% |
| **+10¢ (15¢ stop)** | 62314 | 62211 | 103 (61) | 0 | $-23036.08 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 15:55 | +10 stop | SOL | UP | 0.65 | 0.83 | 1.54 |
| 11-07 15:55 | +10 stop | XRP | DOWN | 0.58 | 0.42 | -1.96 |
| 11-07 15:55 | +20 | XRP | DOWN | 0.58 | open |  |
| 11-07 15:55 | +15 | XRP | DOWN | 0.58 | open |  |
| 11-07 15:55 | +10 | XRP | DOWN | 0.58 | open |  |
| 11-07 15:55 | +5 | XRP | DOWN | 0.58 | open |  |
| 11-07 15:54 | +10 stop | SOL | DOWN | 0.58 | 0.38 | -2.35 |
| 11-07 15:54 | +10 stop | ZEC | DOWN | 0.56 | 0.40 | -1.95 |
| 11-07 15:54 | +5 | ZEC | DOWN | 0.56 | open |  |
| 11-07 15:53 | +10 stop | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-07 15:53 | +10 stop | SOL | DOWN | 0.58 | 0.69 | 0.77 |
| 11-07 15:52 | +5 | HYPE | DOWN | 0.70 | 0.87 | 1.47 |
| 11-07 15:52 | +10 stop | HYPE | DOWN | 0.71 | 0.87 | 1.37 |
| 11-07 15:52 | +5 | ZEC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-07 15:51 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 11-07 15:51 | +20 | XRP | DOWN | 0.64 | 0.89 | 2.22 |
| 11-07 15:51 | +15 | XRP | DOWN | 0.64 | 0.82 | 1.48 |
| 11-07 15:51 | +10 | XRP | DOWN | 0.64 | 0.82 | 1.48 |
| 11-07 15:51 | +5 | XRP | DOWN | 0.64 | 0.72 | 0.44 |
| 11-07 15:51 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-07 15:51 | +20 | DOGE | DOWN | 0.65 | 0.89 | 2.17 |
| 11-07 15:51 | +15 | DOGE | DOWN | 0.65 | 0.84 | 1.64 |
| 11-07 15:51 | +10 | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-07 15:51 | +5 | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-07 15:51 | +10 stop | ZEC | UP | 0.49 | 0.33 | -1.94 |
| 11-07 15:51 | +5 | ZEC | UP | 0.49 | 0.54 | 0.14 |
| 11-07 15:50 | +10 stop | SOL | UP | 0.59 | 0.43 | -1.95 |
| 11-07 15:50 | +15 | SOL | UP | 0.59 | 0.83 | 2.13 |
| 11-07 15:50 | +5 | SOL | UP | 0.60 | 0.66 | 0.27 |
| 11-07 15:49 | +10 stop | HYPE | DOWN | 0.49 | 0.59 | 0.65 |
| 11-07 15:49 | +20 | HYPE | DOWN | 0.47 | 0.67 | 1.66 |
| 11-07 15:49 | +15 | HYPE | DOWN | 0.55 | 0.70 | 1.17 |
| 11-07 15:49 | +10 | HYPE | DOWN | 0.55 | 0.67 | 0.86 |
| 11-07 15:49 | +5 | HYPE | DOWN | 0.56 | 0.64 | 0.45 |
| 11-07 15:49 | +5 | ZEC | DOWN | 0.54 | 0.69 | 1.17 |
| 11-07 15:48 | +10 stop | SOL | DOWN | 0.71 | 0.53 | -2.13 |
| 11-07 15:48 | +10 | SOL | DOWN | 0.71 | open |  |
| 11-07 15:48 | +5 | SOL | DOWN | 0.71 | 0.80 | 0.63 |
| 11-07 15:47 | +10 stop | ZEC | DOWN | 0.64 | 0.47 | -2.05 |
| 11-07 15:47 | +20 | ZEC | DOWN | 0.64 | open |  |
