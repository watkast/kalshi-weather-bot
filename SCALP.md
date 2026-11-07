# Range-Scalp Bot

*Updated Sat Nov 07 13:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51025 | 44482 | 6543 (78) | 4 | $-14276.52 | -4.4% |
| **+10¢** | 38092 | 30466 | 7626 (105) | 5 | $-13244.34 | -5.5% |
| **+15¢** | 31884 | 23664 | 8220 (134) | 5 | $-12183.74 | -6.1% |
| **+20¢** | 28354 | 19737 | 8617 (177) | 5 | $-10761.42 | -6.1% |
| **+10¢ (15¢ stop)** | 62143 | 62040 | 103 (61) | 3 | $-22932.44 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 13:55 | +10 stop | BTC | UP | 0.70 | open |  |
| 11-07 13:55 | +10 stop | BNB | DOWN | 0.54 | open |  |
| 11-07 13:55 | +10 stop | XRP | UP | 0.63 | open |  |
| 11-07 13:54 | +10 stop | ZEC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-07 13:53 | +10 stop | BTC | UP | 0.57 | 0.68 | 0.76 |
| 11-07 13:53 | +10 stop | BNB | DOWN | 0.69 | 0.45 | -2.73 |
| 11-07 13:50 | +10 stop | ZEC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-07 13:50 | +10 stop | BNB | UP | 0.57 | 0.42 | -1.86 |
| 11-07 13:50 | +20 | BNB | UP | 0.57 | open |  |
| 11-07 13:50 | +15 | BNB | UP | 0.57 | open |  |
| 11-07 13:50 | +10 | BNB | UP | 0.57 | open |  |
| 11-07 13:50 | +5 | BNB | UP | 0.57 | open |  |
| 11-07 13:50 | +10 stop | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 11-07 13:49 | +10 stop | BTC | UP | 0.71 | 0.56 | -1.83 |
| 11-07 13:49 | +20 | BTC | UP | 0.71 | open |  |
| 11-07 13:49 | +15 | BTC | UP | 0.71 | open |  |
| 11-07 13:49 | +10 | BTC | UP | 0.71 | open |  |
| 11-07 13:49 | +5 | BTC | UP | 0.71 | open |  |
| 11-07 13:49 | +10 stop | ZEC | DOWN | 0.52 | 0.64 | 0.85 |
| 11-07 13:48 | +10 stop | ZEC | UP | 0.63 | 0.33 | -3.33 |
| 11-07 13:48 | +5 | XRP | UP | 0.56 | 0.64 | 0.45 |
| 11-07 13:47 | +10 stop | SOL | DOWN | 0.62 | 0.78 | 1.30 |
| 11-07 13:47 | +10 stop | XRP | UP | 0.57 | 0.31 | -2.93 |
| 11-07 13:47 | +10 | XRP | UP | 0.56 | open |  |
| 11-07 13:47 | +5 | XRP | UP | 0.56 | 0.64 | 0.45 |
| 11-07 13:47 | +10 stop | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-07 13:47 | +20 | HYPE | DOWN | 0.65 | 0.85 | 1.75 |
| 11-07 13:47 | +15 | HYPE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-07 13:47 | +10 | HYPE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-07 13:47 | +5 | HYPE | DOWN | 0.65 | 0.72 | 0.39 |
| 11-07 13:46 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-07 13:46 | +20 | DOGE | DOWN | 0.65 | 0.88 | 2.06 |
| 11-07 13:46 | +15 | DOGE | DOWN | 0.65 | 0.84 | 1.64 |
| 11-07 13:46 | +10 | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-07 13:46 | +5 | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-07 13:46 | +10 stop | NEAR | DOWN | 0.59 | 0.70 | 0.78 |
| 11-07 13:46 | +20 | NEAR | DOWN | 0.59 | 0.80 | 1.81 |
| 11-07 13:46 | +15 | NEAR | DOWN | 0.59 | 0.80 | 1.81 |
| 11-07 13:46 | +10 | NEAR | DOWN | 0.59 | 0.70 | 0.78 |
| 11-07 13:46 | +5 | NEAR | DOWN | 0.59 | 0.70 | 0.78 |
