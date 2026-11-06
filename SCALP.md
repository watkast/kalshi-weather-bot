# Range-Scalp Bot

*Updated Fri Nov 06 23:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50119 | 43691 | 6428 (76) | 6 | $-14070.11 | -4.5% |
| **+10¢** | 37400 | 29920 | 7480 (102) | 7 | $-12968.78 | -5.5% |
| **+15¢** | 31325 | 23262 | 8063 (131) | 6 | $-11891.40 | -6.1% |
| **+20¢** | 27848 | 19394 | 8454 (173) | 6 | $-10515.62 | -6.0% |
| **+10¢ (15¢ stop)** | 61049 | 60950 | 99 (58) | 1 | $-22640.55 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 23:26 | +10 stop | ETH | UP | 0.61 | 0.82 | 1.82 |
| 11-06 23:24 | +10 stop | XRP | UP | 0.69 | 0.88 | 1.67 |
| 11-06 23:24 | +10 stop | DOGE | UP | 0.67 | 0.88 | 1.86 |
| 11-06 23:24 | +5 | XRP | UP | 0.70 | 0.88 | 1.57 |
| 11-06 23:23 | +10 stop | BNB | DOWN | 0.47 | open |  |
| 11-06 23:23 | +10 stop | XRP | DOWN | 0.54 | 0.38 | -1.95 |
| 11-06 23:23 | +10 | XRP | DOWN | 0.54 | open |  |
| 11-06 23:23 | +5 | XRP | DOWN | 0.54 | 0.59 | 0.15 |
| 11-06 23:22 | +10 stop | BTC | UP | 0.69 | 0.81 | 0.94 |
| 11-06 23:22 | +10 | BTC | UP | 0.69 | 0.81 | 0.94 |
| 11-06 23:22 | +5 | BTC | UP | 0.69 | 0.77 | 0.52 |
| 11-06 23:21 | +10 stop | BNB | UP | 0.60 | 0.34 | -2.93 |
| 11-06 23:21 | +10 stop | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 23:21 | +10 stop | SOL | UP | 0.56 | 0.71 | 1.17 |
| 11-06 23:21 | +5 | BTC | UP | 0.61 | 0.69 | 0.48 |
| 11-06 23:19 | +5 | BNB | DOWN | 0.63 | open |  |
| 11-06 23:19 | +15 | DOGE | DOWN | 0.64 | open |  |
| 11-06 23:19 | +5 | DOGE | DOWN | 0.64 | open |  |
| 11-06 23:19 | +10 stop | BNB | DOWN | 0.63 | 0.37 | -2.98 |
| 11-06 23:19 | +20 | BNB | DOWN | 0.63 | open |  |
| 11-06 23:19 | +15 | BNB | DOWN | 0.63 | open |  |
| 11-06 23:19 | +10 | BNB | DOWN | 0.63 | open |  |
| 11-06 23:19 | +5 | BNB | DOWN | 0.63 | 0.69 | 0.24 |
| 11-06 23:18 | +10 stop | HYPE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-06 23:18 | +10 stop | ZEC | DOWN | 0.64 | 0.77 | 1.00 |
| 11-06 23:17 | +10 stop | DOGE | DOWN | 0.65 | 0.50 | -1.84 |
| 11-06 23:17 | +10 | DOGE | DOWN | 0.65 | open |  |
| 11-06 23:17 | +10 stop | ETH | DOWN | 0.63 | 0.31 | -3.52 |
| 11-06 23:17 | +20 | ETH | DOWN | 0.63 | open |  |
| 11-06 23:17 | +15 | ETH | DOWN | 0.63 | open |  |
| 11-06 23:17 | +10 | ETH | DOWN | 0.63 | open |  |
| 11-06 23:17 | +5 | ETH | DOWN | 0.63 | open |  |
| 11-06 23:17 | +10 stop | SOL | DOWN | 0.62 | 0.42 | -2.35 |
| 11-06 23:17 | +20 | SOL | DOWN | 0.62 | open |  |
| 11-06 23:17 | +15 | SOL | DOWN | 0.62 | open |  |
| 11-06 23:17 | +10 | SOL | DOWN | 0.62 | open |  |
| 11-06 23:17 | +5 | SOL | DOWN | 0.62 | open |  |
| 11-06 23:17 | +5 | DOGE | DOWN | 0.64 | 0.71 | 0.38 |
| 11-06 23:17 | +10 stop | BNB | DOWN | 0.49 | 0.59 | 0.65 |
| 11-06 23:17 | +20 | BNB | DOWN | 0.49 | 0.71 | 1.87 |
