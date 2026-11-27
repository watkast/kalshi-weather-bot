# Range-Scalp Bot

*Updated Fri Nov 27 00:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73144 | 63838 | 9306 (158) | 1 | $-19523.19 | -4.2% |
| **+10¢** | 54530 | 43663 | 10867 (204) | 2 | $-18122.69 | -5.3% |
| **+15¢** | 45663 | 33955 | 11708 (262) | 2 | $-16238.67 | -5.7% |
| **+20¢** | 40638 | 28310 | 12328 (328) | 2 | $-14632.97 | -5.7% |
| **+10¢ (15¢ stop)** | 89072 | 88863 | 209 (128) | 2 | $-32857.90 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 00:38 | +10 stop | ZEC | DOWN | 0.59 | open |  |
| 11-27 00:38 | +20 | ZEC | DOWN | 0.59 | open |  |
| 11-27 00:38 | +5 | ZEC | DOWN | 0.59 | open |  |
| 11-27 00:37 | +10 stop | NEAR | UP | 0.63 | open |  |
| 11-27 00:37 | +20 | NEAR | UP | 0.63 | open |  |
| 11-27 00:37 | +15 | NEAR | UP | 0.63 | open |  |
| 11-27 00:37 | +10 | NEAR | UP | 0.63 | open |  |
| 11-27 00:37 | +5 | NEAR | UP | 0.62 | 0.72 | 0.63 |
| 11-27 00:34 | +15 | ZEC | UP | 0.71 | open |  |
| 11-27 00:34 | +5 | ZEC | UP | 0.66 | 0.74 | 0.47 |
| 11-27 00:33 | +10 stop | ZEC | UP | 0.65 | 0.43 | -2.54 |
| 11-27 00:33 | +10 | ZEC | UP | 0.65 | open |  |
| 11-27 00:32 | +5 | ZEC | UP | 0.60 | 0.65 | 0.17 |
| 11-27 00:32 | +5 | HYPE | UP | 0.62 | 0.67 | 0.17 |
| 11-27 00:31 | +10 stop | DOGE | UP | 0.67 | 0.79 | 0.93 |
| 11-27 00:31 | +20 | DOGE | UP | 0.67 | 0.90 | 2.12 |
| 11-27 00:31 | +15 | DOGE | UP | 0.67 | 0.82 | 1.24 |
| 11-27 00:31 | +10 | DOGE | UP | 0.67 | 0.79 | 0.94 |
| 11-27 00:31 | +5 | DOGE | UP | 0.66 | 0.79 | 1.02 |
| 11-27 00:31 | +10 stop | NEAR | UP | 0.60 | 0.79 | 1.61 |
| 11-27 00:31 | +20 | NEAR | UP | 0.60 | 0.81 | 1.82 |
| 11-27 00:31 | +15 | NEAR | UP | 0.60 | 0.79 | 1.61 |
| 11-27 00:31 | +10 | NEAR | UP | 0.60 | 0.79 | 1.61 |
| 11-27 00:31 | +5 | NEAR | UP | 0.60 | 0.79 | 1.61 |
| 11-27 00:31 | +10 stop | XRP | UP | 0.61 | 0.76 | 1.20 |
| 11-27 00:31 | +20 | XRP | UP | 0.60 | 0.84 | 2.13 |
| 11-27 00:31 | +15 | XRP | UP | 0.60 | 0.76 | 1.30 |
| 11-27 00:31 | +10 | XRP | UP | 0.61 | 0.76 | 1.20 |
| 11-27 00:31 | +5 | XRP | UP | 0.61 | 0.67 | 0.27 |
| 11-27 00:31 | +10 stop | BTC | UP | 0.65 | 0.77 | 0.91 |
| 11-27 00:31 | +20 | BTC | UP | 0.65 | 0.86 | 1.85 |
| 11-27 00:31 | +15 | BTC | UP | 0.65 | 0.83 | 1.54 |
| 11-27 00:31 | +10 | BTC | UP | 0.66 | 0.77 | 0.81 |
| 11-27 00:31 | +5 | BTC | UP | 0.66 | 0.73 | 0.40 |
| 11-27 00:31 | +10 stop | ZEC | UP | 0.50 | 0.63 | 0.98 |
| 11-27 00:31 | +20 | ZEC | UP | 0.50 | 0.74 | 2.10 |
| 11-27 00:31 | +15 | ZEC | UP | 0.51 | 0.68 | 1.36 |
| 11-27 00:31 | +10 | ZEC | UP | 0.51 | 0.63 | 0.85 |
| 11-27 00:31 | +5 | ZEC | UP | 0.51 | 0.56 | 0.16 |
| 11-27 00:31 | +10 stop | BNB | UP | 0.61 | 0.72 | 0.78 |
