# Range-Scalp Bot

*Updated Fri Nov 06 17:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49788 | 43401 | 6387 (76) | 2 | $-13976.04 | -4.5% |
| **+10¢** | 37161 | 29731 | 7430 (101) | 3 | $-12871.56 | -5.5% |
| **+15¢** | 31124 | 23116 | 8008 (130) | 3 | $-11787.12 | -6.0% |
| **+20¢** | 27668 | 19272 | 8396 (171) | 3 | $-10424.59 | -6.0% |
| **+10¢ (15¢ stop)** | 60646 | 60549 | 97 (57) | 0 | $-22433.41 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 17:05 | +5 | BTC | DOWN | 0.62 | open |  |
| 11-06 17:03 | +5 | BTC | DOWN | 0.65 | 0.72 | 0.39 |
| 11-06 17:03 | +10 stop | BNB | DOWN | 0.66 | 0.81 | 1.23 |
| 11-06 17:03 | +15 | BNB | DOWN | 0.66 | 0.81 | 1.23 |
| 11-06 17:03 | +10 | BNB | DOWN | 0.66 | 0.81 | 1.23 |
| 11-06 17:03 | +5 | BNB | DOWN | 0.66 | 0.81 | 1.23 |
| 11-06 17:03 | +10 stop | NEAR | DOWN | 0.65 | 0.49 | -1.94 |
| 11-06 17:02 | +5 | XRP | DOWN | 0.67 | 0.75 | 0.50 |
| 11-06 17:02 | +5 | DOGE | DOWN | 0.66 | 0.74 | 0.50 |
| 11-06 17:02 | +10 stop | BTC | DOWN | 0.64 | 0.45 | -2.25 |
| 11-06 17:02 | +20 | BTC | DOWN | 0.64 | open |  |
| 11-06 17:02 | +15 | BTC | DOWN | 0.64 | open |  |
| 11-06 17:02 | +10 | BTC | DOWN | 0.64 | open |  |
| 11-06 17:02 | +5 | BTC | DOWN | 0.64 | 0.71 | 0.38 |
| 11-06 17:02 | +10 stop | ZEC | DOWN | 0.67 | 0.46 | -2.44 |
| 11-06 17:02 | +20 | ZEC | DOWN | 0.67 | open |  |
| 11-06 17:02 | +15 | ZEC | DOWN | 0.67 | open |  |
| 11-06 17:02 | +10 | ZEC | DOWN | 0.67 | open |  |
| 11-06 17:02 | +5 | ZEC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-06 17:01 | +10 stop | DOGE | DOWN | 0.55 | 0.70 | 1.17 |
| 11-06 17:01 | +20 | DOGE | DOWN | 0.55 | 0.76 | 1.79 |
| 11-06 17:01 | +15 | DOGE | DOWN | 0.56 | 0.74 | 1.48 |
| 11-06 17:01 | +10 | DOGE | DOWN | 0.56 | 0.70 | 1.09 |
| 11-06 17:01 | +5 | DOGE | DOWN | 0.56 | 0.64 | 0.47 |
| 11-06 17:01 | +10 stop | HYPE | DOWN | 0.64 | 0.75 | 0.79 |
| 11-06 17:01 | +20 | HYPE | DOWN | 0.64 | 0.87 | 2.05 |
| 11-06 17:01 | +15 | HYPE | DOWN | 0.64 | 0.79 | 1.21 |
| 11-06 17:01 | +10 | HYPE | DOWN | 0.64 | 0.75 | 0.79 |
| 11-06 17:01 | +5 | HYPE | DOWN | 0.64 | 0.70 | 0.28 |
| 11-06 17:01 | +10 stop | BNB | DOWN | 0.55 | 0.71 | 1.32 |
| 11-06 17:01 | +20 | BNB | DOWN | 0.55 | 0.81 | 2.36 |
| 11-06 17:01 | +15 | BNB | DOWN | 0.55 | 0.71 | 1.32 |
| 11-06 17:01 | +10 | BNB | DOWN | 0.55 | 0.71 | 1.32 |
| 11-06 17:01 | +5 | BNB | DOWN | 0.55 | 0.71 | 1.32 |
| 11-06 17:01 | +10 stop | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 11-06 17:01 | +20 | XRP | DOWN | 0.64 | 0.91 | 2.49 |
| 11-06 17:01 | +15 | XRP | DOWN | 0.64 | 0.83 | 1.63 |
| 11-06 17:01 | +10 | XRP | DOWN | 0.64 | 0.75 | 0.79 |
| 11-06 17:01 | +5 | XRP | DOWN | 0.64 | 0.69 | 0.18 |
| 11-06 17:01 | +10 stop | SOL | DOWN | 0.63 | 0.77 | 1.10 |
