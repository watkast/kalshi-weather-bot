# Range-Scalp Bot

*Updated Sun Oct 04 13:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2344 | 2024 | 320 (3) | 2 | $-764.22 | -5.1% |
| **+10¢** | 1829 | 1473 | 356 (4) | 2 | $-568.36 | -4.9% |
| **+15¢** | 1533 | 1156 | 377 (5) | 3 | $-479.55 | -5.0% |
| **+20¢** | 1356 | 959 | 397 (9) | 5 | $-413.36 | -4.8% |
| **+10¢ (15¢ stop)** | 2898 | 2897 | 1 (1) | 2 | $-1078.41 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 13:51 | +10 stop | BNB | DOWN | 0.56 | open |  |
| 10-04 13:51 | +10 stop | ETH | UP | 0.67 | open |  |
| 10-04 13:51 | +15 | ETH | UP | 0.67 | open |  |
| 10-04 13:51 | +10 | ETH | UP | 0.67 | open |  |
| 10-04 13:51 | +5 | ETH | UP | 0.67 | open |  |
| 10-04 13:50 | +10 stop | NEAR | DOWN | 0.59 | 0.75 | 1.29 |
| 10-04 13:50 | +10 stop | BNB | UP | 0.65 | 0.48 | -2.04 |
| 10-04 13:50 | +10 | BNB | UP | 0.65 | open |  |
| 10-04 13:50 | +5 | BNB | UP | 0.65 | open |  |
| 10-04 13:48 | +10 stop | BNB | DOWN | 0.58 | 0.43 | -1.86 |
| 10-04 13:48 | +10 stop | DOGE | UP | 0.70 | 0.84 | 1.16 |
| 10-04 13:48 | +20 | DOGE | UP | 0.70 | open |  |
| 10-04 13:48 | +15 | DOGE | UP | 0.70 | 0.86 | 1.37 |
| 10-04 13:48 | +10 | DOGE | UP | 0.70 | 0.84 | 1.16 |
| 10-04 13:48 | +5 | DOGE | UP | 0.70 | 0.77 | 0.43 |
| 10-04 13:47 | +10 stop | HYPE | UP | 0.62 | 0.73 | 0.79 |
| 10-04 13:47 | +20 | HYPE | UP | 0.62 | 0.91 | 2.61 |
| 10-04 13:47 | +15 | HYPE | UP | 0.62 | 0.82 | 1.67 |
| 10-04 13:47 | +10 | HYPE | UP | 0.62 | 0.73 | 0.74 |
| 10-04 13:47 | +5 | HYPE | UP | 0.62 | 0.71 | 0.53 |
| 10-04 13:47 | +10 stop | NEAR | DOWN | 0.63 | 0.48 | -1.88 |
| 10-04 13:47 | +20 | NEAR | DOWN | 0.63 | open |  |
| 10-04 13:47 | +15 | NEAR | DOWN | 0.63 | open |  |
| 10-04 13:47 | +10 | NEAR | DOWN | 0.64 | 0.75 | 0.81 |
| 10-04 13:47 | +5 | NEAR | DOWN | 0.64 | 0.75 | 0.81 |
| 10-04 13:47 | +5 | ETH | UP | 0.68 | 0.73 | 0.20 |
| 10-04 13:47 | +10 stop | ZEC | UP | 0.55 | 0.71 | 1.32 |
| 10-04 13:47 | +20 | ZEC | UP | 0.55 | 0.75 | 1.73 |
| 10-04 13:47 | +15 | ZEC | UP | 0.55 | 0.71 | 1.32 |
| 10-04 13:47 | +10 | ZEC | UP | 0.55 | 0.71 | 1.32 |
| 10-04 13:47 | +5 | ZEC | UP | 0.55 | 0.71 | 1.32 |
| 10-04 13:46 | +10 stop | BNB | UP | 0.58 | 0.43 | -1.87 |
| 10-04 13:46 | +10 | BNB | UP | 0.58 | 0.71 | 0.96 |
| 10-04 13:46 | +5 | BNB | UP | 0.58 | 0.71 | 0.96 |
| 10-04 13:46 | +10 stop | ETH | UP | 0.66 | 0.77 | 0.86 |
| 10-04 13:46 | +20 | ETH | UP | 0.65 | open |  |
| 10-04 13:46 | +15 | ETH | UP | 0.65 | 0.80 | 1.22 |
| 10-04 13:46 | +10 | ETH | UP | 0.65 | 0.77 | 0.91 |
| 10-04 13:46 | +5 | ETH | UP | 0.65 | 0.72 | 0.39 |
| 10-04 13:46 | +10 stop | BTC | UP | 0.65 | 0.76 | 0.81 |
