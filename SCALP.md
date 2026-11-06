# Range-Scalp Bot

*Updated Fri Nov 06 23:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50164 | 43730 | 6434 (76) | 4 | $-14088.64 | -4.5% |
| **+10¢** | 37427 | 29939 | 7488 (102) | 6 | $-12998.88 | -5.5% |
| **+15¢** | 31347 | 23277 | 8070 (131) | 7 | $-11912.26 | -6.1% |
| **+20¢** | 27868 | 19407 | 8461 (173) | 7 | $-10530.81 | -6.0% |
| **+10¢ (15¢ stop)** | 61086 | 60987 | 99 (58) | 0 | $-22644.52 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 23:57 | +10 stop | BNB | DOWN | 0.69 | 0.85 | 1.36 |
| 11-06 23:57 | +20 | BNB | DOWN | 0.69 | 0.96 | 2.54 |
| 11-06 23:57 | +15 | BNB | DOWN | 0.69 | 0.85 | 1.36 |
| 11-06 23:57 | +10 | BNB | DOWN | 0.69 | 0.85 | 1.36 |
| 11-06 23:57 | +5 | BNB | DOWN | 0.69 | 0.85 | 1.36 |
| 11-06 23:56 | +5 | ZEC | DOWN | 0.66 | 0.78 | 0.91 |
| 11-06 23:55 | +10 stop | DOGE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-06 23:55 | +10 stop | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 11-06 23:55 | +10 stop | BTC | DOWN | 0.67 | 0.82 | 1.23 |
| 11-06 23:55 | +10 | BTC | DOWN | 0.67 | 0.82 | 1.23 |
| 11-06 23:55 | +5 | BTC | DOWN | 0.66 | 0.72 | 0.29 |
| 11-06 23:54 | +10 stop | ZEC | DOWN | 0.69 | 0.85 | 1.36 |
| 11-06 23:54 | +5 | ZEC | DOWN | 0.68 | 0.74 | 0.30 |
| 11-06 23:53 | +10 stop | SOL | UP | 0.69 | 0.48 | -2.43 |
| 11-06 23:53 | +10 | SOL | UP | 0.69 | open |  |
| 11-06 23:53 | +5 | ZEC | UP | 0.59 | 0.65 | 0.27 |
| 11-06 23:53 | +10 stop | DOGE | UP | 0.55 | 0.38 | -2.06 |
| 11-06 23:51 | +10 stop | DOGE | DOWN | 0.64 | 0.41 | -2.64 |
| 11-06 23:50 | +10 stop | HYPE | DOWN | 0.68 | 0.46 | -2.54 |
| 11-06 23:50 | +5 | BTC | UP | 0.66 | 0.75 | 0.60 |
| 11-06 23:50 | +10 stop | BNB | UP | 0.70 | 0.81 | 0.84 |
| 11-06 23:50 | +15 | BNB | UP | 0.70 | 0.85 | 1.26 |
| 11-06 23:50 | +10 | BNB | UP | 0.70 | 0.81 | 0.84 |
| 11-06 23:50 | +5 | BNB | UP | 0.70 | 0.76 | 0.32 |
| 11-06 23:49 | +5 | ETH | UP | 0.56 | open |  |
| 11-06 23:49 | +5 | DOGE | UP | 0.60 | open |  |
| 11-06 23:49 | +5 | SOL | UP | 0.67 | open |  |
| 11-06 23:48 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 11-06 23:48 | +5 | XRP | DOWN | 0.64 | 0.73 | 0.59 |
| 11-06 23:48 | +5 | NEAR | UP | 0.61 | 0.68 | 0.37 |
| 11-06 23:48 | +10 stop | SOL | UP | 0.59 | 0.69 | 0.68 |
| 11-06 23:48 | +20 | SOL | UP | 0.59 | open |  |
| 11-06 23:48 | +15 | SOL | UP | 0.59 | open |  |
| 11-06 23:48 | +10 | SOL | UP | 0.59 | 0.69 | 0.68 |
| 11-06 23:48 | +5 | SOL | UP | 0.58 | 0.66 | 0.46 |
| 11-06 23:48 | +5 | ETH | UP | 0.51 | 0.56 | 0.14 |
| 11-06 23:47 | +5 | BNB | UP | 0.67 | 0.73 | 0.35 |
| 11-06 23:47 | +10 stop | HYPE | UP | 0.59 | 0.38 | -2.44 |
| 11-06 23:46 | +10 stop | BTC | UP | 0.65 | 0.75 | 0.70 |
| 11-06 23:46 | +20 | BTC | UP | 0.65 | open |  |
