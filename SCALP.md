# Range-Scalp Bot

*Updated Fri Oct 16 13:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 19312 | 16780 | 2532 (29) | 2 | $-5832.41 | -4.8% |
| **+10¢** | 14557 | 11630 | 2927 (41) | 2 | $-5259.19 | -5.7% |
| **+15¢** | 12189 | 9038 | 3151 (60) | 2 | $-4772.67 | -6.2% |
| **+20¢** | 10810 | 7507 | 3303 (79) | 2 | $-4258.34 | -6.3% |
| **+10¢ (15¢ stop)** | 23752 | 23702 | 50 (29) | 0 | $-9135.10 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-16 13:53 | +10 stop | SOL | DOWN | 0.70 | 0.55 | -1.83 |
| 10-16 13:52 | +10 stop | SOL | DOWN | 0.52 | 0.63 | 0.75 |
| 10-16 13:50 | +10 stop | SOL | DOWN | 0.70 | 0.83 | 1.05 |
| 10-16 13:49 | +10 stop | SOL | DOWN | 0.60 | 0.44 | -1.95 |
| 10-16 13:48 | +20 | DOGE | DOWN | 0.61 | 0.83 | 1.91 |
| 10-16 13:48 | +10 stop | DOGE | DOWN | 0.64 | 0.83 | 1.63 |
| 10-16 13:48 | +15 | DOGE | DOWN | 0.64 | 0.83 | 1.63 |
| 10-16 13:48 | +10 | DOGE | DOWN | 0.64 | 0.83 | 1.63 |
| 10-16 13:48 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.18 |
| 10-16 13:47 | +5 | NEAR | DOWN | 0.62 | 0.74 | 0.92 |
| 10-16 13:47 | +10 stop | XRP | DOWN | 0.62 | 0.75 | 0.99 |
| 10-16 13:47 | +10 stop | DOGE | DOWN | 0.53 | 0.65 | 0.86 |
| 10-16 13:47 | +10 | DOGE | DOWN | 0.55 | 0.65 | 0.66 |
| 10-16 13:47 | +5 | DOGE | DOWN | 0.55 | 0.65 | 0.66 |
| 10-16 13:47 | +10 stop | ZEC | DOWN | 0.55 | 0.71 | 1.24 |
| 10-16 13:47 | +20 | ZEC | DOWN | 0.55 | 0.75 | 1.68 |
| 10-16 13:47 | +15 | ZEC | DOWN | 0.55 | 0.71 | 1.25 |
| 10-16 13:47 | +10 | ZEC | DOWN | 0.56 | 0.71 | 1.17 |
| 10-16 13:47 | +5 | ZEC | DOWN | 0.57 | 0.71 | 1.07 |
| 10-16 13:47 | +10 stop | BNB | DOWN | 0.60 | 0.71 | 0.78 |
| 10-16 13:47 | +20 | BNB | DOWN | 0.60 | 0.84 | 2.13 |
| 10-16 13:47 | +15 | BNB | DOWN | 0.60 | 0.77 | 1.40 |
| 10-16 13:47 | +10 | BNB | DOWN | 0.60 | 0.71 | 0.78 |
| 10-16 13:47 | +5 | BNB | DOWN | 0.60 | 0.67 | 0.37 |
| 10-16 13:47 | +10 stop | HYPE | UP | 0.66 | 0.49 | -2.08 |
| 10-16 13:47 | +20 | HYPE | UP | 0.67 | open |  |
| 10-16 13:47 | +15 | HYPE | UP | 0.67 | open |  |
| 10-16 13:47 | +10 | HYPE | UP | 0.66 | open |  |
| 10-16 13:47 | +5 | HYPE | UP | 0.64 | open |  |
| 10-16 13:47 | +10 stop | NEAR | DOWN | 0.58 | 0.74 | 1.32 |
| 10-16 13:47 | +20 | NEAR | DOWN | 0.56 | 0.79 | 2.00 |
| 10-16 13:47 | +15 | NEAR | DOWN | 0.56 | 0.74 | 1.48 |
| 10-16 13:47 | +10 | NEAR | DOWN | 0.56 | 0.74 | 1.48 |
| 10-16 13:47 | +5 | NEAR | DOWN | 0.56 | 0.62 | 0.25 |
| 10-16 13:47 | +5 | XRP | DOWN | 0.63 | 0.71 | 0.48 |
| 10-16 13:46 | +10 stop | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-16 13:46 | +20 | BTC | DOWN | 0.68 | 0.89 | 1.87 |
| 10-16 13:46 | +15 | BTC | DOWN | 0.68 | 0.84 | 1.34 |
| 10-16 13:46 | +10 | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 10-16 13:46 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
