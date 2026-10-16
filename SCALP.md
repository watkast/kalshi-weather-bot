# Range-Scalp Bot

*Updated Fri Oct 16 12:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19192 | 16678 | 2514 (29) | 1 | $-5774.96 | -4.8% |
| **+10¢** | 14466 | 11560 | 2906 (41) | 3 | $-5207.03 | -5.7% |
| **+15¢** | 12109 | 8982 | 3127 (60) | 4 | $-4708.66 | -6.2% |
| **+20¢** | 10742 | 7464 | 3278 (79) | 5 | $-4191.02 | -6.2% |
| **+10¢ (15¢ stop)** | 23601 | 23551 | 50 (29) | 0 | $-9092.69 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 12:02 | +10 stop | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-16 12:02 | +10 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-16 12:02 | +5 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-16 12:02 | +10 stop | HYPE | UP | 0.41 | 0.59 | 1.46 |
| 10-16 12:02 | +20 | HYPE | UP | 0.41 | open |  |
| 10-16 12:02 | +15 | HYPE | UP | 0.41 | 0.59 | 1.46 |
| 10-16 12:02 | +10 | HYPE | UP | 0.41 | 0.59 | 1.46 |
| 10-16 12:02 | +5 | HYPE | UP | 0.41 | 0.59 | 1.46 |
| 10-16 12:01 | +10 stop | NEAR | UP | 0.48 | 0.29 | -2.23 |
| 10-16 12:01 | +20 | NEAR | UP | 0.49 | open |  |
| 10-16 12:01 | +15 | NEAR | UP | 0.49 | open |  |
| 10-16 12:01 | +10 | NEAR | UP | 0.49 | open |  |
| 10-16 12:01 | +5 | NEAR | UP | 0.49 | open |  |
| 10-16 12:01 | +10 stop | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-16 12:01 | +20 | BTC | DOWN | 0.67 | 0.88 | 1.86 |
| 10-16 12:01 | +15 | BTC | DOWN | 0.67 | 0.83 | 1.34 |
| 10-16 12:01 | +10 | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-16 12:01 | +5 | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-16 12:01 | +10 stop | ZEC | UP | 0.46 | 0.56 | 0.64 |
| 10-16 12:01 | +20 | ZEC | UP | 0.46 | open |  |
| 10-16 12:01 | +15 | ZEC | UP | 0.46 | open |  |
| 10-16 12:01 | +10 | ZEC | UP | 0.46 | 0.56 | 0.64 |
| 10-16 12:01 | +5 | ZEC | UP | 0.46 | 0.56 | 0.64 |
| 10-16 12:01 | +10 stop | XRP | UP | 0.53 | 0.34 | -2.24 |
| 10-16 12:01 | +20 | XRP | UP | 0.53 | open |  |
| 10-16 12:01 | +15 | XRP | UP | 0.53 | open |  |
| 10-16 12:01 | +10 | XRP | UP | 0.54 | open |  |
| 10-16 12:01 | +5 | XRP | UP | 0.53 | 0.62 | 0.55 |
| 10-16 12:01 | +10 stop | SOL | UP | 0.54 | 0.27 | -3.02 |
| 10-16 12:01 | +20 | SOL | UP | 0.55 | open |  |
| 10-16 12:01 | +15 | SOL | UP | 0.54 | open |  |
| 10-16 12:01 | +10 | SOL | UP | 0.54 | open |  |
| 10-16 12:01 | +5 | SOL | UP | 0.54 | 0.60 | 0.25 |
| 10-16 12:00 | +10 stop | BNB | DOWN | 0.57 | 0.79 | 1.90 |
| 10-16 12:00 | +20 | BNB | DOWN | 0.57 | 0.79 | 1.90 |
| 10-16 12:00 | +15 | BNB | DOWN | 0.57 | 0.79 | 1.90 |
| 10-16 12:00 | +10 | BNB | DOWN | 0.57 | 0.79 | 1.90 |
| 10-16 12:00 | +5 | BNB | DOWN | 0.57 | 0.65 | 0.46 |
| 10-16 11:56 | +10 stop | NEAR | UP | 0.61 | 0.30 | -3.42 |
| 10-16 11:56 | +20 | NEAR | UP | 0.61 | yes | 3.73 |
