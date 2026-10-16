# Range-Scalp Bot

*Updated Fri Oct 16 06:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18787 | 16315 | 2472 (28) | 2 | $-5728.05 | -4.8% |
| **+10¢** | 14158 | 11298 | 2860 (40) | 5 | $-5201.58 | -5.8% |
| **+15¢** | 11871 | 8792 | 3079 (59) | 5 | $-4716.81 | -6.3% |
| **+20¢** | 10544 | 7322 | 3222 (78) | 5 | $-4141.86 | -6.3% |
| **+10¢ (15¢ stop)** | 23135 | 23085 | 50 (29) | 0 | $-8939.95 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 06:47 | +10 stop | NEAR | UP | 0.71 | 0.82 | 0.84 |
| 10-16 06:46 | +10 stop | BNB | UP | 0.69 | 0.80 | 0.83 |
| 10-16 06:46 | +20 | BNB | UP | 0.69 | 0.92 | 2.10 |
| 10-16 06:46 | +15 | BNB | UP | 0.69 | 0.87 | 1.57 |
| 10-16 06:46 | +10 | BNB | UP | 0.69 | 0.80 | 0.83 |
| 10-16 06:46 | +5 | BNB | UP | 0.69 | 0.74 | 0.21 |
| 10-16 06:46 | +10 stop | DOGE | DOWN | 0.57 | 0.26 | -3.42 |
| 10-16 06:46 | +20 | DOGE | DOWN | 0.57 | open |  |
| 10-16 06:46 | +15 | DOGE | DOWN | 0.57 | open |  |
| 10-16 06:46 | +10 | DOGE | DOWN | 0.57 | open |  |
| 10-16 06:46 | +5 | DOGE | DOWN | 0.57 | 0.63 | 0.25 |
| 10-16 06:46 | +10 stop | SOL | DOWN | 0.51 | 0.26 | -2.82 |
| 10-16 06:46 | +20 | SOL | DOWN | 0.51 | open |  |
| 10-16 06:46 | +15 | SOL | DOWN | 0.51 | open |  |
| 10-16 06:46 | +10 | SOL | DOWN | 0.51 | open |  |
| 10-16 06:46 | +5 | SOL | DOWN | 0.51 | 0.57 | 0.24 |
| 10-16 06:46 | +10 stop | XRP | DOWN | 0.51 | 0.26 | -2.82 |
| 10-16 06:46 | +20 | XRP | DOWN | 0.52 | open |  |
| 10-16 06:46 | +15 | XRP | DOWN | 0.52 | open |  |
| 10-16 06:46 | +10 | XRP | DOWN | 0.52 | open |  |
| 10-16 06:46 | +5 | XRP | DOWN | 0.52 | open |  |
| 10-16 06:46 | +10 stop | ZEC | DOWN | 0.54 | 0.31 | -2.63 |
| 10-16 06:46 | +20 | ZEC | DOWN | 0.54 | open |  |
| 10-16 06:46 | +15 | ZEC | DOWN | 0.54 | open |  |
| 10-16 06:46 | +10 | ZEC | DOWN | 0.54 | open |  |
| 10-16 06:46 | +5 | ZEC | DOWN | 0.54 | 0.63 | 0.55 |
| 10-16 06:45 | +10 stop | NEAR | DOWN | 0.64 | 0.39 | -2.81 |
| 10-16 06:45 | +20 | NEAR | DOWN | 0.64 | open |  |
| 10-16 06:45 | +15 | NEAR | DOWN | 0.64 | open |  |
| 10-16 06:45 | +10 | NEAR | DOWN | 0.64 | open |  |
| 10-16 06:45 | +5 | NEAR | DOWN | 0.64 | open |  |
| 10-16 06:31 | +10 stop | HYPE | UP | 0.66 | 0.78 | 0.91 |
| 10-16 06:31 | +20 | HYPE | UP | 0.66 | 0.88 | 1.96 |
| 10-16 06:31 | +15 | HYPE | UP | 0.66 | 0.81 | 1.23 |
| 10-16 06:31 | +10 | HYPE | UP | 0.66 | 0.78 | 0.91 |
| 10-16 06:31 | +5 | HYPE | UP | 0.66 | 0.71 | 0.19 |
| 10-16 06:31 | +10 stop | XRP | UP | 0.70 | 0.81 | 0.84 |
| 10-16 06:31 | +20 | XRP | UP | 0.70 | 0.93 | 2.12 |
| 10-16 06:31 | +15 | XRP | UP | 0.70 | 0.89 | 1.68 |
| 10-16 06:31 | +10 | XRP | UP | 0.70 | 0.81 | 0.84 |
