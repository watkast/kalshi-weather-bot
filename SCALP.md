# Range-Scalp Bot

*Updated Sat Oct 10 05:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9971 | 8605 | 1366 (18) | 3 | $-3366.01 | -5.4% |
| **+10¢** | 7535 | 5942 | 1593 (30) | 2 | $-3240.63 | -6.8% |
| **+15¢** | 6363 | 4683 | 1680 (43) | 2 | $-2674.49 | -6.7% |
| **+20¢** | 5656 | 3911 | 1745 (55) | 2 | $-2232.12 | -6.3% |
| **+10¢ (15¢ stop)** | 12254 | 12219 | 35 (22) | 0 | $-4813.39 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 04:57 | +10 stop | ZEC | DOWN | 0.70 | 0.88 | 1.57 |
| 10-10 04:57 | +20 | ZEC | DOWN | 0.69 | 0.91 | 1.96 |
| 10-10 04:57 | +15 | ZEC | DOWN | 0.69 | 0.88 | 1.65 |
| 10-10 04:57 | +10 | ZEC | DOWN | 0.69 | 0.88 | 1.65 |
| 10-10 04:57 | +5 | ZEC | DOWN | 0.69 | 0.88 | 1.65 |
| 10-10 04:55 | +10 stop | ZEC | UP | 0.68 | 0.50 | -2.14 |
| 10-10 04:52 | +10 stop | NEAR | UP | 0.55 | 0.70 | 1.19 |
| 10-10 04:52 | +10 stop | DOGE | DOWN | 0.57 | 0.37 | -2.37 |
| 10-10 04:52 | +10 stop | NEAR | DOWN | 0.39 | 0.58 | 1.54 |
| 10-10 04:51 | +10 stop | HYPE | UP | 0.65 | 0.80 | 1.21 |
| 10-10 04:51 | +20 | HYPE | UP | 0.65 | 0.87 | 1.96 |
| 10-10 04:51 | +15 | HYPE | UP | 0.65 | 0.80 | 1.22 |
| 10-10 04:51 | +10 | HYPE | UP | 0.65 | 0.80 | 1.22 |
| 10-10 04:51 | +5 | HYPE | UP | 0.65 | 0.80 | 1.22 |
| 10-10 04:51 | +10 stop | XRP | UP | 0.65 | 0.75 | 0.70 |
| 10-10 04:51 | +10 stop | SOL | DOWN | 0.50 | 0.28 | -2.53 |
| 10-10 04:51 | +10 stop | NEAR | DOWN | 0.58 | 0.70 | 0.86 |
| 10-10 04:50 | +10 stop | ETH | DOWN | 0.65 | 0.38 | -3.03 |
| 10-10 04:50 | +10 stop | DOGE | DOWN | 0.71 | 0.50 | -2.39 |
| 10-10 04:50 | +5 | DOGE | DOWN | 0.71 | open |  |
| 10-10 04:50 | +10 stop | XRP | DOWN | 0.62 | 0.39 | -2.62 |
| 10-10 04:49 | +10 stop | NEAR | DOWN | 0.57 | 0.41 | -1.94 |
| 10-10 04:48 | +5 | BTC | DOWN | 0.61 | open |  |
| 10-10 04:48 | +5 | DOGE | DOWN | 0.60 | 0.65 | 0.17 |
| 10-10 04:48 | +10 stop | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-10 04:48 | +10 | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-10 04:48 | +5 | ZEC | DOWN | 0.65 | 0.74 | 0.60 |
| 10-10 04:47 | +10 stop | DOGE | UP | 0.50 | 0.33 | -2.04 |
| 10-10 04:47 | +20 | DOGE | UP | 0.50 | 0.80 | 2.70 |
| 10-10 04:47 | +15 | DOGE | UP | 0.50 | 0.68 | 1.46 |
| 10-10 04:47 | +10 | DOGE | UP | 0.50 | 0.62 | 0.85 |
| 10-10 04:47 | +5 | DOGE | UP | 0.50 | 0.58 | 0.44 |
| 10-10 04:47 | +10 stop | XRP | UP | 0.61 | 0.45 | -1.94 |
| 10-10 04:47 | +20 | XRP | UP | 0.61 | 0.83 | 1.93 |
| 10-10 04:47 | +15 | XRP | UP | 0.61 | 0.83 | 1.93 |
| 10-10 04:47 | +10 | XRP | UP | 0.61 | 0.75 | 1.11 |
| 10-10 04:47 | +5 | XRP | UP | 0.61 | 0.75 | 1.11 |
| 10-10 04:47 | +10 stop | SOL | UP | 0.56 | 0.40 | -2.00 |
| 10-10 04:47 | +20 | SOL | UP | 0.56 | 0.77 | 1.74 |
| 10-10 04:47 | +15 | SOL | UP | 0.56 | 0.73 | 1.33 |
