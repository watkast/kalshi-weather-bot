# Range-Scalp Bot

*Updated Fri Oct 16 22:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19980 | 17380 | 2600 (29) | 3 | $-5902.18 | -4.7% |
| **+10¢** | 15048 | 12043 | 3005 (41) | 5 | $-5296.07 | -5.6% |
| **+15¢** | 12587 | 9355 | 3232 (60) | 5 | $-4783.56 | -6.1% |
| **+20¢** | 11162 | 7778 | 3384 (79) | 6 | $-4213.29 | -6.0% |
| **+10¢ (15¢ stop)** | 24554 | 24504 | 50 (29) | 0 | $-9335.60 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 22:56 | +10 stop | BTC | DOWN | 0.51 | 0.66 | 1.16 |
| 10-16 22:56 | +10 | BTC | DOWN | 0.55 | 0.66 | 0.76 |
| 10-16 22:56 | +5 | BTC | DOWN | 0.52 | 0.66 | 1.06 |
| 10-16 22:56 | +10 stop | DOGE | UP | 0.68 | 0.91 | 2.05 |
| 10-16 22:56 | +15 | DOGE | UP | 0.68 | 0.91 | 2.05 |
| 10-16 22:56 | +10 | DOGE | UP | 0.68 | 0.91 | 2.05 |
| 10-16 22:56 | +5 | DOGE | UP | 0.68 | 0.91 | 2.05 |
| 10-16 22:55 | +10 stop | BNB | UP | 0.51 | 0.72 | 1.77 |
| 10-16 22:55 | +10 stop | HYPE | UP | 0.46 | 0.21 | -2.80 |
| 10-16 22:55 | +15 | HYPE | UP | 0.46 | open |  |
| 10-16 22:55 | +10 | HYPE | UP | 0.46 | open |  |
| 10-16 22:55 | +5 | HYPE | UP | 0.46 | 0.54 | 0.44 |
| 10-16 22:55 | +10 stop | SOL | DOWN | 0.67 | 0.81 | 1.13 |
| 10-16 22:54 | +10 stop | BNB | DOWN | 0.52 | 0.37 | -1.85 |
| 10-16 22:53 | +5 | HYPE | UP | 0.63 | 0.84 | 1.83 |
| 10-16 22:52 | +10 stop | XRP | DOWN | 0.69 | 0.82 | 1.04 |
| 10-16 22:51 | +5 | HYPE | UP | 0.69 | 0.77 | 0.48 |
| 10-16 22:51 | +5 | BTC | UP | 0.64 | 0.70 | 0.28 |
| 10-16 22:51 | +10 stop | SOL | DOWN | 0.61 | 0.73 | 0.89 |
| 10-16 22:51 | +10 stop | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 10-16 22:51 | +5 | BTC | UP | 0.60 | 0.69 | 0.58 |
| 10-16 22:51 | +10 stop | XRP | DOWN | 0.71 | 0.55 | -1.93 |
| 10-16 22:50 | +10 stop | ETH | DOWN | 0.69 | 0.53 | -1.93 |
| 10-16 22:50 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 10-16 22:48 | +5 | NEAR | UP | 0.70 | 0.85 | 1.26 |
| 10-16 22:48 | +10 stop | BNB | UP | 0.66 | 0.44 | -2.53 |
| 10-16 22:48 | +10 | BNB | UP | 0.66 | open |  |
| 10-16 22:47 | +5 | BNB | UP | 0.70 | open |  |
| 10-16 22:47 | +10 stop | XRP | UP | 0.62 | 0.47 | -1.85 |
| 10-16 22:47 | +20 | XRP | UP | 0.62 | open |  |
| 10-16 22:47 | +15 | XRP | UP | 0.62 | open |  |
| 10-16 22:47 | +10 | XRP | UP | 0.62 | open |  |
| 10-16 22:47 | +5 | XRP | UP | 0.62 | open |  |
| 10-16 22:46 | +10 stop | HYPE | UP | 0.68 | 0.84 | 1.34 |
| 10-16 22:46 | +20 | HYPE | UP | 0.68 | open |  |
| 10-16 22:46 | +15 | HYPE | UP | 0.68 | 0.84 | 1.34 |
| 10-16 22:46 | +10 | HYPE | UP | 0.68 | 0.84 | 1.34 |
| 10-16 22:46 | +5 | HYPE | UP | 0.68 | 0.75 | 0.40 |
| 10-16 22:46 | +10 stop | DOGE | UP | 0.70 | 0.84 | 1.15 |
| 10-16 22:46 | +20 | DOGE | UP | 0.70 | 0.91 | 1.86 |
